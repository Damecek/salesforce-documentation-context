**•** Events with a status of `InProgress` report (if applicable) the number of records
processed.

For _query_ jobs:

**•** Events with a status of `JobComplete` or `InProgress` report (if applicable) the
number of records processed.

```
RequestIdentifier

ResultSize

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

Number of megabytes returned in query. Empty for ingest jobs. For example: `670` .

ResultSizeMb currently does not emit events, but is shown here as a placeholder for future
enhancement.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects BulkApiEventLog

**Field** **Details**

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

```
Timestamp

Uri

UserIdentifier

### BulkApiEventLog

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

Bulk API event logs contain details about Bulk API requests. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects BulkApiEventLog

Fields

**Field** **Details**

```
BatchIdentifier

ClientIp

CpuTime

FailureCount

IsSuccess

JobIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API batch.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of failures that were returned with the request.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the callout request was successful.

**Type**
string


Standard Objects BulkApiEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API job.

```
LoginKey

Message

ObjectType

OperationType

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Any success or error message that’s associated with the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of entity that the Bulk API used.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Bulk API operation that was performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BulkApiEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RunTime

SessionKey

Timestamp

Uri

UserIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects BulkApiRequestEventLog

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### BulkApiRequestEventLog

The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiVersion

BatchIdentifier

ClientIp

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API batch.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BulkApiRequestEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

```
ClientName

ConcurrencyMode

ConnectedAppIdentifier

CpuTime

ErrorMessage

IsSuccess

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the client making the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The concurrency mode selected by the user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the connected app making a request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of entity that the Bulk API used.

**Type**
boolean


Standard Objects BulkApiRequestEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the batch was successful.

```
JobIdentifier

LoginKey

OperationType

RequestIdentifier

RequestPath

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API job

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the login id to allow click tracking across multiple transactions from login to
action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Bulk API operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The path of the request.


Standard Objects BulkApiRequestEventLog

**Field** **Details**

```
RunTime

SessionKey

StatusCode

Timestamp

Uri

UserIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Amount of time the request took, as measured by SFDC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the sid to allow click tracking across multiple transactions after login to action.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP Status code indicating whether the batch was successful.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URI of the page receiving the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects BusinessBrand

**Field** **Details**

**Description**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### BusinessBrand

Represents a unique brand for a business that belongs to a parent entity. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

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
Required. Name of this business brand.


Standard Objects BusinessBrand

**Field** **Details**

```
OrgId

OwnerId

ParentId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce ID of the business brand.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this business brand.

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
The ID of the parent entity that this business brand is a child of.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects BusinessAlert

**BusinessBrandChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### BusinessAlert

Represents information about insight notifications that Einstein Relationship Insights explores, such as news mentions, job updates, and
relationships. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The BusinessAlert object is available only if the ERI Growth User or ERI Starter User license is enabled.

Fields

**Field** **Details**

```
AlertData

AlertRecordId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Data associated with each alert.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that's referenced by the insight alert.

This field is a polymorphic relationship field.

**Relationship Name**
AlertRecord

**Relationship Type**
Lookup

**Refers To**
Account, Asset, AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, BusinessBrand, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, Contact, ContactPointAddress, ContactPointConsent,


Standard Objects BusinessAlert

**Field** **Details**

ContactPointEmail, ContactPointPhone, ContactPointTypeConsent, ContentVersion, Customer,
DataUseLegalBasis, DataUsePurpose, EmailMessage, EngagementChannelType, Idea, Image,
Individual, Lead, Location, Opportunity, PartyConsent, Pricebook2, Product2, ProfileSkill,
QuickText, Recommendation, Scorecard, ScorecardMetric, Seller, SocialPersona, SocialPost,
Solution, VideoCall, WorkBadgeDefinition

In addition to the listed standard object fields, this field can refer to custom objects as well,

```
AlertType

CurrentDesignation

CurrentEmployer

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type of insight alert.

Possible values are:

**•** `JOB_CHANGE`

**•** `NEWS`

**•** `RELATIONSHIP`

The default value is `NEWS` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current designation that's related to the job alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the current employer that's related to the job alert.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed a record related to this alert record.


Standard Objects BusinessAlert

**Field** **Details**

```
LastViewedDate

Name

OwnerId

PreviousDesignation

PreviousEmployer

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this alert.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the alert record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The previous designation that's related to the job alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the previous employer that's related to the job alert.


### Standard Objects BusinessAlertStatus BusinessAlertStatus

Represents information about the read status of an insight alert. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The BusinessAlertStatus object is available only if the ERI Growth User or ERI Starter User license is enabled.

Fields

**Field** **Details**

```
BusinessAlertId

IsAlertRead

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The insight alert related to the status.

This field is a relationship field.

**Relationship Name**
### BusinessAlert

**Relationship Type**
Lookup

**Refers To**
### BusinessAlert

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the insight alert is read by the user (true) or not (false).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects BusinessHours

**Field** **Details**

**Description**
Specifies the activation status of the insight alert.

```
UserId

### BusinessHours

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user who is associated with the alert.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Specifies the business hours of your support organization. Escalation rules are run only during these hours.

Limit a list view to a maximum of 10,000 business hours.

If business hours are associated with any Holiday records, then business hours and escalation rules associated with business hours are
suspended during the dates and times specified as holidays.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

All users, even those without the “View Setup and Configuration” user permission, can view business hours via the API.

Fields

**Field** **Details**

### `BusinessHoursId`

**Type**
reference


Standard Objects BusinessHours

**Field** **Details**

**Properties**
Filter, Group, Nillable,Sort

**Description**
ID of the BusinessHours associated with the SlaProcess.

```
IsActive

Name

IsDefault

LastViewedDate

FridayEndTime

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the business hours is active ( `true` ) or not active ( `false` ).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the business hours.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the business hours are set as the default business hours ( `true` ) or not
( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the business hours were last viewed.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.


Standard Objects BusinessHours

**Field** **Details**

```
FridayStartTime

MondayEndTime

MondayStartTime

SaturdayEndTime

SaturdayStartTime

SundayEndTime

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.


Standard Objects BusinessHours

**Field** **Details**

```
SundayStartTime

ThursdayEndTime

ThursdayStartTime

TimeZoneSidKey

TuesdayEndTime

TuesdayStartTime

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time zone of the business hours.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.


### Standard Objects Business Process

**Field** **Details**

```
 WednesdayEndTime

 WednesdayStartTime

```

Usage

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

Use this object to specify the business hours at which your support team operates. Escalation rules only run during the business hours
with which they are associated. To set business hours to 24-hours a day, set the times from midnight to midnight (00:00:00 ~ 00:00:00)
on each day.

By default, business hours are set from 12:00 AM to 12:00 AM in the default time zone specified in your organization's profile.

SEE ALSO:

Overview of Salesforce Objects and Fields

### Business Process

Represents a business process. Business Processes track separate sales, lead, support, and solution lifecycles by displaying different picklist
values according to each user’s profile.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.


Standard Objects Business Process

Fields

**Field** **Details**

```
Description

IsActive

Name

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of this business process. Limit: 255 characters.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this business process can be presented to users in the Salesforce user
interface ( `true` ) or not ( `false` ) when creating a new record type or changing the business
process of an existing record type.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this business process. Limit: 80 characters.

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


### Standard Objects BusinessProcessDefinition

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
 TableEnumOrId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. One of the following values: Case, Opportunity, or Solution. Label is **Entity**
**Enumeration Or ID** .

Use the BusinessProcess object to offer different subsets of picklist values to different users for the LeadStatus, CaseStatus, and
OpportunityStage fields. Similar to a RecordType, a BusinessProcess identifies the type of a row in a Case, Lead, or Opportunity and
implies a subset of picklist values for these three fields. The values for the remaining picklist fields are driven by RecordType.

SEE ALSO:

Overview of Salesforce Objects and Fields

### BusinessProcessDefinition

Setup object that stores information about stages in a customer lifecycle map. The stages are associated with surveys and questions
created using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BusinessProcessGroupId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the customer lifecycle map associated with the stage.


Standard Objects BusinessProcessDefinition

**Field** **Details**

```
DeveloperName

Language

MasterLabel

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the stage.

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

**•** `zh_TW` —Chinese (Traditional)

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the stage.


### Standard Objects BusinessProcessFeedback

**Field** **Details**

```
ProcessDescription

SequenceNumber

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the stage.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The position of the stage in the associated customer lifecycle map.

### BusinessProcessFeedback

Setup object that stores information about the survey and the question associated with each stage in a customer lifecycle map. Customer
lifecycle maps are used to track the scores provided by customers across their lifecycle using Salesforce Surveys. This object is reserved
for internal use, and is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionName

ActionParam

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the survey used to gather feedback.

**Type**
string

**Properties**
Filter, Group, Sort


### Standard Objects BusinessProcessGroup

**Field** **Details**

**Description**
Name of the question used to gather feedback.

```
ActionType

BusinessProcessDefinitionId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Method of collecting feedback.

Possible value is:

**•** `PHONE_CALL`

**•** `SURVEY`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the stage associated with the survey and question.

### BusinessProcessGroup

Setup object that stores information about customer lifecycle maps. Customer lifecycle maps are used to track the scores provided by
customers across their lifecycle using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CustomerSatisfactionMetric

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects BusinessProcessGroup

**Field** **Details**

**Description**
Represents the question type that measures the customers' Net Promote Score or satisfaction
score across their lifecycle.

Possible values are:

**•** `NPS`

**•** `Rating`

```
Description

DeveloperName

Language

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the customer lifecycle map.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name the customer lifecycle map.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

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


### Standard Objects BuyerAccount

**Field** **Details**

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

### BuyerAccount

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the customer lifecycle map.

Represents an account that is enabled as a buyer for Lightning B2B Commerce. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The BuyerAccount object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AvailableCredit

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of credit available to a buyer account.

This is a calculated field.


Standard Objects BuyerAccount

**Field** **Details**

```
BuyerId

BuyerStatus

CommerceType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the buyer account.

This is a relationship field.

**Relationship Name**
Buyer

**Relationship Type**
Lookup

**Refers To**
Account

Note: This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the buyer account.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `On Hold`

**•** `Pending`

The default value is 'Pending'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of commerce that the buyer account is conducting, using the Commerce app.

Possible values are:

**•** `Buyer`

**•** `Reseller`

**•** `Seller`

The default value is 'Buyer'.


Standard Objects BuyerAccount

**Field** **Details**

```
CreditLimit

CreditStatus

CurrencyIsoCode

CurrentBalance

IsActive

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The limit of credit available to the buyer account.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type or status of the buyer account's credit ranking.

Possible values are:

**•** `Bad Credit`

**•** `Delinquent`

**•** `Good Credit`

**•** `On Hold`

The default value is 'Good Credit'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO currency code associated with the buyer account record.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is 'USD'.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The balance carried by the buyer account.

**Type**
boolean


Standard Objects BuyerAccount

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the buyer account is active ( `true` ) or not ( `false` ).

The default value is 'false'.

```
MaximumOrderLimit

MinimumOrderLimit

Name

OwnerId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of orders that can be placed by the buyer account.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum number of orders that can be placed by the buyer account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the buyer account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the buyer account owner.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects BuyerAccount

**Field** **Details**

```
PayerId

SendToId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the buyer account payer.

This is a relationship field.

**Relationship Name**
Payer

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of account that an order is sent to.

This is a relationship field.

**Relationship Name**
SendTo

**Relationship Type**
Lookup

**Refers To**
Account

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerAccountFeed on page 55**
Feed tracking is available for the object.

**BuyerAccountHistory on page 63**
History is available for tracked fields of the object.

**BuyerAccountShare on page 67**
Sharing is available for the object.


### Standard Objects BuyerCriteria BuyerCriteria

Represents the buyer context qualifier of locale for any buyer groups of type Market This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CriteriaKey

CriteriaKeyType

CriteriaValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The label displayed to list supported markets with associated languages and
currencies.

Possible values are:

**•** `Locale`

**•** `DataCloudSegment`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Defines the type of key.

Possible values are:

**•** `SessionAttributes` Session Attributes

**•** `DataCloudObjects`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update, Nillable

**Description**
Required. The value of a `Locale` . For example, `fr-FR.`


Standard Objects BuyerCriteria

**Field** **Details**

```
CurrencyIsoCode

Description

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional. Three letter ISO currency codes associated with the buyer account record or a
locale. Auto populated if MultiCurrency is enabled in org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The supported criteria in this record.

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
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the buyer group the criteria apply to.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects BuyerCriteria

**Field** **Details**

**Description**
ID of the member group or Admin/Merchandiser .

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

BuyerCriteria is related to objects that enable a localized buyer experience. Together, these objects provide buyers with dynamic access
to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and shop in webstores
with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerCriteriaFeed on page 55**
Feed tracking is available for the object.

**BuyerCriteriaHistory on page 63**
History is available for tracked fields of the object.

**BuyerCriteriaOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BuyerCriteriaShare on page 67**
Sharing is available for the object.


### Standard Objects BuyerGroup BuyerGroup

Associates group qualifiers (entitlements, price books, promotions, and shipping methods) with buyer members based on buyer account
ID or on the localized language and currency of the market browsed in a webstore. This object is available in API version 57.0; amended
to support Market in version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Buyer group details.

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
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the buyer group.


Standard Objects BuyerGroup

**Field** **Details**

```
OwnerId

RecordTypeId

Role

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

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
ID of the record type of the version

This field is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines a fixed or dynamic relationship to the language and currency that products,
promotions, and entitlements are displayed in.

Possible values are:

**•** `AccountBased`

**•** `Market`

**•** `DataCloudSegments`


### Standard Objects BuyerGroupBuyerCriteria

**Field** **Details**

The default value is `AccountBased` . When set to `Market`, and when the org has multiple
locales, the currency and language for qualifiers (price books, promotions, entitlements)
dynamically change as the buyer views different locale-based markets.

Usage

BuyerGroup is related to objects that enable a localized buyer experience. Together, these objects provide buyers with dynamic access
to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and shop in webstores
with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

### • BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with

BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerGroupChangeEvent on page 68**
Change events are available for the object.

**BuyerGroupFeed on page 55**
Feed tracking is available for the object.

**BuyerGroupHistory on page 63**
History is available for tracked fields of the object.

**BuyerGroupOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BuyerGroupShare on page 67**
Sharing is available for the object.

### BuyerGroupBuyerCriteria

Associates a buyer group that is enabled for webstores supporting multiple languages and currencies with BuyerCriteria that define
those languages and currencies. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects BuyerGroupBuyerCriteria

Fields

**Field** **Details**

```
BuyerCriteriaId

BuyerGroupId

CurrencyIsoCode

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the buyer criteria this record is associated with.

This field is a relationship field.

**Relationship Name**
BuyerCriteria

**Relationship Type**
Lookup

**Refers To**
BuyerCriteria

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the buyer group this record is associated with.

This field is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional. Three letter ISO currency codes associated with the buyer account record or a
locale. Auto populated if MultiCurrency is enabled in org.

**Type**
string


### Standard Objects BuyerGroupMember

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

Usage

BuyerGroupBuyerCriteria is related to objects that enable a localized buyer experience. Together, these objects provide buyers with
dynamic access to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and
shop in webstores with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

### BuyerGroupMember

Represents a member of a buyer group. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The BuyerGroupMember object is available only if the Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
BuyerGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects BuyerGroupMember

**Field** **Details**

**Description**
The ID of the buyer group to which the member belongs.

`BuyerGroupId` is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

```
BuyerId

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the account or guest buyer profile.

`BuyerId` is a polymorphic relationship field.

**Relationship Name**
Buyer

**Relationship Type**
Lookup

**Refers To**
Account, GuestBuyerProfile

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the buyer group member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the member group or user.

`OwnerId` is a polymorphic relationship field.

**Relationship Name**
Owner


### Standard Objects BuyerGroupPricebook

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

### BuyerGroupPricebook

Represents a buyer group price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The BuyerGroupPricebook object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
BuyerGroupId

IsActive

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the buyer group that the price book record is assigned to.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the BuyerGroupPricebook is active ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects BuyerGroupPricebook

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

Pricebook2Id

Priority

```

Usage

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Buyer Group Price Book record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book assigned to the buyer group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequential priority used to determine the price of a product. This field is only available
for web stores that use the **Priority** pricing strategy.

Use the BuyerGroupPricebook object to assign a price book to a set of buyer users. Assigning a price book to a buyer group allows buyers
within that buyer group to retrieve product prices from the price book. When a buyer has multiple price book assignments, including
multiple prices for the same product, the store Pricing Strategy determines the price.


### Standard Objects BuyerGroupRelatedObject BuyerGroupRelatedObject

Used to associate currencies and supported ship-to countries with a buyer group and its price books, promotions, and entitlements.
Supports buyer experience when buyer group members shop in stores enabled for multiple locales. This object is available in API version
58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### BuyerGroupRelatedObject is availble only if the org is Market Enabled ( Commerce.orgHasCommerceMarketEnabled ).

Fields

**Field** **Details**

```
BuyerGroupId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the buyer group this record is associated with.

This field is a relationship field.

**Relationship Name**
### BuyerGroup

**Relationship Type**
Lookup

**Refers To**
### BuyerGroup

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime


Standard Objects BuyerGroupRelatedObject

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly..

```
Name

ObjectType

ObjectValues

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The names displayed in the picklist showing the ObjectValues - currency and
ship-to countries.

Possible values are:

**•** `DefaultCurrency`  - Default Currency

**•** `SupportedShipToCountries`  - Supported Ship-to Countries

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Optional. Values for ObjectType. The actual currency and supported ship-to countries. Possible
values are:

**•** Three-letter ISO currency code associated with the buyer account or a supported locale.

**•** ISO country code for supported ship-to countries.

BuyerGroupRelatedObject is related to objects that enable a localized buyer experience. Together, these objects provide buyers with
dynamic access to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and
shop in webstores with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.


### Standard Objects CalcProcStepRelationship

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerGroupRelatedObjectChangeEvent on page 68**
Change events are available for the object.

**BuyerGroupRelatedObjectFeed on page 55**
Feed tracking is available for the object.

**BuyerGroupRelatedObjectHistory on page 63**
History is available for tracked fields of the object.

### CalcProcStepRelationship

Defines a parent-child relationship between two Expression Set Steps in an Expression Set Version. The label for this object is Expression
Set Step Relationship. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Parent-child step relationships collectively determine the step order.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalcProcStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CalcProcStepRelationship

**Field** **Details**

**Description**
The ID of the child Expression Set Step.

This is a relationship field.

**Relationship Name**
CalcProcStep

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

```
CalcProcVersionId

Name

ParentCalcProcStepId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related Expression Set Version.

This is a relationship field.

**Relationship Name**
CalcProcVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Expression Set Step Relationship name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent Expression Set Step.

This is a relationship field.

**Relationship Name**
ParentCalcProcStep


### Standard Objects CalculatedInsightRangeBound

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

```
RelationshipType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of relationship between the parent and child steps.

Possible values are:

**•** `Bypass` —The parent is a condition step. If the condition is false, the child is the next
step.

**•** `ParentChild` —The child is the next step after the parent.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalcProcStepRelationshipFeed on page 55**
Feed tracking is available for the object.

**CalcProcStepRelationshipHistory on page 63**
History is available for tracked fields of the object.

### CalculatedInsightRangeBound

Stores the information required to calculate a range-bound data insight. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if a B2B Commerce or D2C Commerce license is enabled.


Standard Objects CalculatedInsightRangeBound

Fields

**Field** **Details**

```
InsightName

LastReferencedDate

LastViewedDate

LowerBoundRange

Name

Operator

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Name of the calculated insight.

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
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The lower limit of the calculated insight.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the insight.

**Type**
picklist


Standard Objects CalculatedInsightRangeBound

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Operation used to calculate the insight based on the upper bound range and lower bound
range.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_EQUAL_TO`

```
OwnerId

SalesStoreId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the insight.

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
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the webstore associated with the insight benchmarks.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore


### Standard Objects CalculationMatrix

**Field** **Details**

```
UpperBoundRange

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The upper limit of the calculated insight.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalculatedInsightRangeBoundOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CalculatedInsightRangeBoundShare on page 67**
Sharing is available for the object.

### CalculationMatrix

Matches input values to a table row and returns the row's output values. The label for this object is Decision Matrix. This object is available
in API version 53.0 and later.

Decision Matrices are useful for implementing complex rules in a systematic, readable way. There are two types: Standard and Grouped.
A Grouped Decision Matrix groups rows in different versions by one or two keys such as geographic region or product code.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search(), undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
DecisionMatrixDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects CalculationMatrix

**Field** **Details**

**Description**
The decision matrix definition record associated with this calculation matrix.

This field is a polymorphic relationship field.

**Relationship Name**
DecisionMatrixDefinition

**Relationship Type**
Lookup

**Refers To**
DecisionMatrixDefinition, DecisionTable

```
DecisionMatrixType

Description

GroupKey

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of lookup table.

Possible values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

The default value is `DecisionMatrix` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text description of the Decision Matrix.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A key for grouping matrix rows in different versions, such as geographic region or product
code.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CalculationMatrix

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

MigrationStatus

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.

**Type**
textarea

**Properties**
Nillable

**Description**
The status of migrating the data from the Calculation Matrix object to the Decision Matrix
Definition object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Decision Matrix name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this matrix. Default value is the user logged in to the
API to perform the create action.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects CalculationMatrix

**Field** **Details**

```
SubGroupKey

Type

UniqueName

UsageType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A subkey for grouping matrix rows in different versions, such as geographic region or product
code. For example, if the `GroupKey` is `Country`, the `SubGroupKey` can be `State`
or `Province` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The Decision Matrix type. A Standard Decision Matrix has no special features. A Grouped
Decision Matrix groups rows by one or two keys ( `GroupKey` and `SubGroupKey` ) such
as geographic region or product code.

Possible values are:

**•** `Grouped`

**•** `Standard`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the record, which is sourced from the value in the Name field of
CalculationMatrix (decision matrix). For example, if the name of the calculation matrix is
sample matrix, its UniqueName would be sample_matrix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A decision matrix’s usage type.

Available in API version 59.0 and later.

Possible value is:

**•** `Bre` -Default


### Standard Objects CalculationMatrixColumn

**Field** **Details**

When Business Rules Engine is enabled on your Salesforce org, the default value is Bre. Other
usage types may be available to you depending on your industry solution and permission
sets.

Usage

Expression Sets, OmniScripts, and Integration Procedures can call Decision Matrices.

### CalculationMatrixColumn

Defines a column in a Decision Matrix. The label for this object is Decision Matrix Column. This object is available in API version 53.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
ApiName

CalculationMatrixId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this column belongs.

This is a relationship field.


Standard Objects CalculationMatrixColumn

**Field** **Details**

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

```
ColumnType

DataType

DisplaySequence

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the column matches matrix input or is returned as output.

Possible values are:

**•** `Input`

**•** `Output`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data in the column.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Number`

**•** `NumberRange`

**•** `Percent`

**•** `Text`

**•** `TextRange`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The position of this column in the column order.


### Standard Objects CalculationMatrixRow

**Field** **Details**

```
IsWildcardColumn

Name

RangeValues

WildcardColumnValue

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this column can contain a wildcard value such as `ALL` .

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The column name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of values that define range boundaries.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value that indicates a wildcard, for example `ALL` . Applicable if `IsWildcardColumn`
is `true` .

### CalculationMatrixRow

Defines a row in a Decision Matrix. The label for this object is Decision Matrix Row. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CalculationMatrixRow

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
CalculationMatrixVersionId

EndDateTime

InputData

IsVersionEnabled

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Decision Matrix Version to which this row belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrixVersion

**Relationship Type**
Lookup

**Refers To**
CalculationMatrixVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this row version is active. Applicable if `IsVersionEnabled` is
`true` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input columns and associated values for this row of the matrix.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CalculationMatrixVersion

**Field** **Details**

**Description**
Specifies whether the associated matrix version is active. Derived from the associated Decision
Matrix Version (CalculationMatrixVersion object).

The default value is `false` .

```
Name

OutputData

StartDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The row name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The output columns and associated values for this row of the matrix.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this row version is active. Applicable if `IsVersionEnabled` is
`true` .

### CalculationMatrixVersion

Defines a version of a Decision Matrix. The label for this object is Decision Matrix Version. This object is available in API version 53.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.


Standard Objects CalculationMatrixVersion

Fields

**Field** **Details**

```
ApiName

CalculationMatrixId

DecisionMatrixDefinitionVerId

DscnModelNoteExportStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the decision matrix version. This field is available in API version 56.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this version belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The decision matrix definition version associated with this calculation matrix version.

This field is a relationship field.

**Relationship Name**
DecisionMatrixDefinitionVer

**Relationship Type**
Lookup

**Refers To**
DecisionMatrixDefinitionVersion

**Type**
reference


Standard Objects CalculationMatrixVersion

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the export status of a decision matrix version in the Decision Model and Notation
(DMN) format.

Possible values are:

**•** `Initiated`

**•** `InProgress`

**•** `Complete`

**•** `Failed`

```
EndDateTime

GroupKey

GroupKeyValue

IsEnabled

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this matrix version is active.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A key for grouping matrix rows in different versions, such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `GroupKey` for this version. For example, if the `GroupKey` is `Country`,
the `GroupKeyValue` can be `United States` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this version is active.

The default value is `false` .


Standard Objects CalculationMatrixVersion

**Field** **Details**

```
LoadProcessStatus

MatrixType

Name

Rank

StartDateTime

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of a data upload from a `.csv` file.

Possible values are:

**•** `Completed`

**•** `CompletedWithErrors`

**•** `Failed`

**•** `InProgress`

**•** `Pending`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The matrix type, either `Standard` or `Grouped` . A Grouped Decision Matrix groups rows
in different Decision Matrix Versions by one or two keys such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The matrix version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When the invocation time of a matrix call is between the `StartDateTime` and
`EndDateTime` of more than one enabled matrix version, the version with the highest
`Rank` is chosen.

**Type**
dateTime


### Standard Objects CalculationProcedure

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this matrix version is active.

```
SubGroupKey

SubGroupKeyValue

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A subkey for grouping matrix rows in different versions, such as geographic region or product
code. For example, if the `GroupKey` is `Country`, the `SubGroupKey` can be `State`
`or Province` . Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `SubGroupKey` for this version. For example, if the `SubGroupKey` is
`State or Province`, the `SubGroupKeyValue` can be `California` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number.

### CalculationProcedure

Performs a series of calculations using matrix lookups and user-defined variables and constants. The label for this object is Expression
Set. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Expression Sets accept input variables and return output variables, both in JSON format. Expression Sets are especially useful for determining
prices, rates, and quotes.


Standard Objects CalculationProcedure

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
Description

InputVariablesMetadata

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's input variables.

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
it's possible the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.


### Standard Objects CalculationProcedureStep

**Field** **Details**

```
Name

OutputVariablesMetadata

OwnerId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Expression Set name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's output variables.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this Expression Set. Default value is the user logged
in to the API to perform the create action.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

OmniScripts and Integration Procedures can call Expression Sets. Expression Sets can call Decision Matrices.

### CalculationProcedureStep

Defines a step in an Expression Set. The label for this object is Expression Set Step. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.


Standard Objects CalculationProcedureStep

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalculationMatrixId

CalculationMatrixType

CalculationProcedure

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Decision Matrix this step calls. Applicable only if the `StepType` is
`MatrixLookup` or `GroupMatrixLookup` .

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the Decision Matrix this step calls. Applicable only if this step calls a Decision
Matrix. If the `StepType` is `MatrixLookup`, the value of this field is `Standard` . If the
`StepType` is `GroupMatrixLookup`, the value of this field is `Grouped` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Expression Set to which this step belongs.


Standard Objects CalculationProcedureStep

**Field** **Details**

```
CalculationProcedureVersionId

ConditionsConvertedText

ConditionsExpressionText

ConditionsUiFormattedText

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this step belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to postfix notation. Applicable only if the `StepType`
is `Condition` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression as the user entered it. Applicable only if the `StepType` is
`Condition` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Condition` .

**Type**
string


Standard Objects CalculationProcedureStep

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Step.

```
FormulaConvertedText

FormulaExpressionText

FormulaUiFormattedText

InputVariablesFormatText

IsConditionalStep

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to postfix notation. Applicable only if the `StepType` is
`Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression as the user entered it. Applicable only if the `StepType` is
`Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of the input matrix columns or procedure variables applicable to the step.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this step is conditional.


Standard Objects CalculationProcedureStep

**Field** **Details**

The default value is `false` .

```
IsResultIncluded

Name

OutputVariablesFormatText

OutputVariablesMappingText

ReferenceProcedureId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that the result of this step is included in the Expression Set output.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The step name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of the output matrix columns or procedure variables applicable to the step. Applicable
only if the `StepType` is `MatrixLookup`, `GroupMatrixLookup`, or
`ReferenceProcedure` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Maps Decision Matrix output variables to Expression Set variables. Applicable only if the
`StepType` is `MatrixLookup` or `GroupMatrixLookup` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the child Expression Set this step calls. Applicable only if the `StepType` is
`ReferenceProcedure` .

This is a relationship field.


Standard Objects CalculationProcedureStep

**Field** **Details**

**Relationship Name**
ReferenceProcedure

**Relationship Type**
Lookup

**Refers To**
CalculationProcedure

```
ReturnMessageValueSet

Stage

StageStepSequence

StepType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A set of messages to return based on the result of a step with a `StepType` of `Condition` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The stage of Expression Set invocation. The `Aggregation` stage applies only to steps
with a `StepType` of `Aggregation` .

Possible values are:

**•** `Aggregation`

**•** `Calculation`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sequence order of the step within the Expression Set. Used only for Expression Sets migrated
from a Salesforce Industries package. New Expression Sets use Expression Set Step Relationship
objects to order their steps.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of action this step performs.

Possible values are:


### Standard Objects CalculationProcedureVariable

**Field** **Details**

**•** `Aggregation` —Returns an average, maximum, minimum, or sum of a list of values.

### • Calculation —Performs a mathematical operation, which can include variables and

constants.

**•** `Condition` —Defines a condition that determines whether other steps are invoked.

**•** `GroupMatrixLookup` —Calls a Grouped Decision Matrix.

**•** `MatrixLookup` —Calls a Standard Decision Matrix.

**•** `ReferenceProcedure` —Calls a child Expression Set.

### CalculationProcedureVariable

Defines a variable in an Expression Set. The label for this object is Expression Set Variable. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
ApiName

CalculationMatrixName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of this variable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CalculationProcedureVariable

**Field** **Details**

**Description**
The name of the Decision Matrix to which this variable belongs. Applicable only if this variable
references a Decision Matrix column.

```
CalculationProcedureVersionId

DataType

DefaultValue

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this variable belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this variable.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Number`

**•** `Percent`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value of this variable.


Standard Objects CalculationProcedureVariable

**Field** **Details**

```
DisplayName

IsEditable

IsUserDefined

Name

Precision

UiDisplayOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user-readable name of this variable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, specifies that a variable is NOT auto-imported from a step that calls a Decision
Matrix or a child Expression Set.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a variable is defined by the user.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this variable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of decimal places. Applicable if the `DataType` is Currency, Number, or Percent.

**Type**
int


### Standard Objects CalculationProcedureVersion

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The display order of the variable in the UI.

### CalculationProcedureVersion

Defines a version of an Expression Set. The label for this object is Expression Set Version. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalculationProcedureId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set to which this version belongs.

This is a relationship field.

**Relationship Name**
### CalculationProcedure

**Relationship Type**
Lookup

**Refers To**
### CalculationProcedure


Standard Objects CalculationProcedureVersion

**Field** **Details**

```
Constants

Description

EndDateTime

IsEnabled

IsLoopingEnabled

LastSimulatedVariablesInput

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A serialized JSON object containing information about each constant. This information
includes the name, data type, alias, and precision.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Version.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this Expression Set Version is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this Expression Set Version is active.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether looping is enabled in this Expression Set Version.

The default value is `false` .

**Type**
textarea


Standard Objects CalculationProcedureVersion

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The input variables and results of the most recent simulation.

```
LoopEnd

LoopIncrement

LoopStart

Name

Rank

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the end variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the interval variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the start variable for looping.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When more than one enabled version matches an Expression Set call, and the
`StartDateTime` to `EndDateTime` spans overlap, the version with the highest `Rank`
is chosen.


### Standard Objects Calendar

**Field** **Details**

```
StartDateTime

VersionNumber

### Calendar

```

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The first date on which this Expression Set Version is active.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number.

Represents a calendar. This can be a default user calendar, public calendar, resource calendar, or holiday calendar. This object is available
in API version 45.0 and later.

Newly created users are assigned a default calendar automatically. Similarly, holiday calendars are created automatically for each
organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

Users with "View Setup and Configuration" user permissions can create, edit, and delete public and resource calendars in the user
interface. All users, even those without the “View Setup and Configuration” user permission, can view calendars via the API.

Fields

All fields are readable only.

**Field** **Details**

```
IsActive

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CalendarView

**Field** **Details**

**Description**
This field indicates whether a user can save events to the calendar.

```
Name

Type

UserId

### CalendarView

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user provided name that identifies the calendar. It is text-indexed for searchability. Note
that this is not an enumerated field; it can be any string to a maximum length of 80 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the calendar. Possible values are:

**•** `Holiday` (Holiday Calendar)

**•** `Public` (Public Calendar)

**•** `Resource` (Resource Calendar)

**•** `User` (User Calendar)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that owns that calendar record. If Type=User, there’s a UserID associated
(foreign key reference to the user). Otherwise, the user field is null.

These calendars can be created and assigned to users other than the creator. Available calendars include object, shared, public, resource,
and user list calendars. Object calendars represent a calendar based on a Salesforce object, either standard or custom. This object is
available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CalendarView

Special Access Rules

All fields and entities referenced by field values must be accessible by the CalendarView creator even if the creator isn’t the CalendarView
owner.

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

DateHandlingType

DisplayField

EndField

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Represents the color used in the background for records displayed in a user’s calendar view
within the user interface.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determined by the data type of the `StartField` . Valid values include:

**•** `Date`

**•** `Datetime`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the `SobjectType` field used as the subject for records displayed in a user’s
calendar view within the user interface.

**Type**
string


Standard Objects CalendarView

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An optional field that represents the sObjectType field used as the end time for records
displayed in a user’s calendar view within the user interface. Must be a date or dateTime field
that matches the type in `StartField` .

```
FillPattern

IsDisplayed

ListViewFilterId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the pattern displayed as the background for records displayed in a user’s calendar
view within the user interface. Valid values include:

**•** `verticalStripes`

**•** `ascDiagonalStripes`

**•** `descDiagonalStripes`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether users can see a calendar’s records in their calendar view in the user interface.
When `true`, records are visible in the user’s calendar view. When `false`, records are
hidden from the user’s calendar view. The default is `true` . `IsDisplayed` can be `true`
for up to 50 calendars.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ListView used to filter records represented by the CalendarView. ListView
must have the same sObjectType. If no `ListViewFilterId` is defined, the calendar
displays only records with the same owner as the CalendarView.

This is a relationship field.

**Relationship Name**
ListViewFilter

**Relationship Type**
Lookup


Standard Objects CalendarView

**Field** **Details**

**Refers To**
ListView

```
Name

OwnerId

PublisherId

SobjectType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A user-provided name that identifies the calendar. This isn’t an enumerated field; it can be
any string to a maximum length of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the owner of the CalendarView.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the user, user list, public, or resource calendar from where event data is populated.

This is a polymorphic relationship field.

**Relationship Name**
Publisher

**Relationship Type**
Lookup

**Refers To**
Calendar, ListView, User

**Type**
picklist


Standard Objects CalendarView

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of standard or custom Salesforce object that is used to create records for the
CalendarView. Use the API name of the desired `SobjectType` .

```
StartField

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the `SobjectType` field used as the start time for records displayed in a user’s
calendar view within the user interface. Must be a date or dateTime field type.

To distribute a CalendarView to multiple users, IDs can be pulled from a group, user list, or profile. For this example, a CalendarView
based on opportunity close dates is being distributed to a sales team in a public group, Sales Group:

```
Group userGroup = [SELECT Id FROM Group WHERE Name = 'Sales Group' LIMIT 1];

List<Id> groupId = new List<Id>();

groupId.add(userGroup.id);

List<GroupMember> groupMembers = [SELECT UserOrGroupId FROM GroupMember

  WHERE GroupId IN: groupId];

List<CalendarView> calendarViews = new List<CalendarView>();

for (GroupMember groupMember : groupMembers) {

  CalendarView calendarView = new CalendarView(name = 'Opportunity Close Dates’,

   SobjectType = 'Opportunity', StartField = 'CloseDate', DisplayField =

   'Name', OwnerId = groupMember.UserOrGroupId);

  calendarViews.add(calendarView);

}

insert calendarViews;

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalendarViewChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects CallCenter CallCenter

Represents a call center, which is a logical representation of a single computer-telephony integration (CTI) system instance in an
organization.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AdapterUrl

CustomSettings

Id

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

An optional field that specifies the location of where the CTI adapter is hosted. For example,
`http://localhost:11000` .

This field is available in API version 23.0 or later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**

Specifies settings in the call center definition file, such as whether the call center uses the
Open CTI, and SoftPhone properties, such as height in pixels.

This field is available for Open CTI and in API version 25.0 or later.

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
System field that uniquely identifies this call center. Label is **Call Center ID** . This ID is created
automatically when the call center is created.


### Standard Objects CallCenterRoutingMap

**Field** **Details**

```
InternalName

Name

Version

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The internal name of the call center.

Limit is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**

The name of the call center.

Limit is 80 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The version of the CTI Toolkit used to create the call center (for versions 2.0 and later).

This field is available in API version 18.0 and later.

Create a call center or query an existing call center.

### CallCenterRoutingMap

Stores a mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center. This object is available
in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Access to standard objects requires Salesforce admin privileges or the Customize Application permission.


Standard Objects CallCenterRoutingMap

Access to call center routing map records requires Contact Center Admin, Contact Center Admin (Partner Telephony), Contact Center
Supervisor, or Manage Call Centers permission.

Fields

**Field** **Details**

```
CallCenterId

DeveloperName

ExternalId

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a call center.

This is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name is a combination of the Salesforce user ID or queue name, and the call
center ID, with an underscore between these two values.

**•** `[SALESFORCE_USER_ID]_[CALL_CENTER_ID]`

**•** `[SALESFORCE_QUEUE_NAME]_[CALL_CENTER_ID]`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique identifier for the external system’s user or queue.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects CallCoachingMediaProvider

**Field** **Details**

**Description**
The language of the MasterLabel.

```
MasterLabel

QuickConnect

ReferenceRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the CallCenterRoutingMap.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Amazon Connect QuickConnectId ARN used to determine agent availability for
Omni-Channel call transfers. Available in API version 56.0 and later.

This is a polymorphic relationship field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Lookup field to a Salesforce user or queue.

This is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Group, User

### CallCoachingMediaProvider

Represents the media provider for call recordings. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects CallCtrAgentFavTrfrDest

Fields

**Field** **Details**

```
IsActive

ProviderDescription

ProviderName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the connection with the provider is active or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the media provider.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the media provider.

### CallCtrAgentFavTrfrDest

Represents a transfer destination that has been marked (starred) as a favorite in the Omni-Channel softphone by a contact center agent
for voice call transfers. This object is available in API version 55.0 and later.

To see a list of transfer destinations that have been marked as favorites in the Omni-Channel softphone, add a participant to the call,
click the Phone tab, and select **Favorite** from the Filter dropdown menu. Examples of transfer destination types include agents, contacts,
directories, flows, and queues.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CallCtrAgentFavTrfrDest

Fields

**Field** **Details**

```
AgentId

CallCenterId

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the contact center agent who marked the transfer destination as a favorite.

This field is a relationship field.

**Relationship Name**
Agent

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the contact center from where the agent starred the transfer destination
as a favorite.

This field is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the transfer destination record that’s marked as a favorite.

**Type**
reference


### Standard Objects CallCtrAgentFavTrfrDestShare

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID of the user who owns this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
TransferDestination

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the transfer destination that’s marked as a favorite. This is an external ID.

### CallCtrAgentFavTrfrDestShare

Represents a sharing entry on a favorite transfer destination in the Omni-Channel softphone for voice call transfers. This object is available
in API version 55.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist


Standard Objects CallCtrAgentFavTrfrDestShare

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The level of access the User or Group has to the transfer destination that’s marked as a favorite.
Possible values are:

**•** `All`                   - Owner

**•** `Edit`                   - Read/Write

**•** `Read`                   - Read Only

```
ParentId

RowCause

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent object.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CallCtrAgentFavTrfrDest

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantDataSharing`  - Compliant Data Sharing

**•** `GuestParentImplicit`  - Associated guest user sharing

**•** `GuestPersonImplicit`  - Associated Guest User Sharing

**•** `GuestRule`  - Guest User Sharing Rule

**•** `ImplicitChild`  - Account Sharing

**•** `ImplicitParent`  - Associated record owner or sharing

**•** `ImplicitPerson`  - Person Contact

**•** `LearningAssignment`  - Learning Assignment Share


### Standard Objects CallDisposition

**Field** **Details**

**•** `LearningAssignmentImplicit`                   - Learning Assignment Implicit Share

**•** `LearningItemAssignment`                   - Learning Item Assignment Share

**•** `Manual`                   - Manual Sharing

**•** `MfgTargetShare`                   - Manufacturing Target Sharing Rule

**•** `Owner`

**•** `Rule`                   - Sharing Rule

**•** `SharingRecordCollection`                   - Record Collection

**•** `SurveyShare`                   - Survey Sharing Rule

**•** `Team`                   - Sales Team

**•** `Territory`                   - Territory Assignment Rule

**•** `Territory2AssociationManual`                   - Territory Manual

**•** `Territory2Forecast`                   - Territory assignment for forecasting and reporting

**•** `TerritoryManual`                   - Territory Manual

**•** `TerritoryRule`                   - Territory Sharing Rule

```
UserOrGroupId

### CallDisposition

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the User or Group that has been given access to the favorite transfer
destination.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Represents a call result value that sales reps select when logging a call. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects CallDispositionCategory

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field** **Details**

```
Disposition

DispositionCategoryId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The result of a phone call, such as whether a call was connected or the rep left a voicemail.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The related call outcome that is used in reports and branching criteria for cadences.

### CallDispositionCategory

Represents the call outcome of a phone call that is used in reports and branching criteria for cadences. This object is available in API
version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field** **Details**

```
Category

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects CallDispositionCategory

**Field** **Details**

**Description**
The name of the call outcome.

```
DeveloperName

Language

```

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

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the call category.

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


### Standard Objects CallTemplate

**Field** **Details**

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
 MasterLabel

### CallTemplate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The static name of the call outcome.

Represents a call script for users to read when making calls.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Description

HtmlBody

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the call script.

**Type**
textarea

**Properties**
Nillable

**Description**
The body content of the call script.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CallTemplate

**Field** **Details**

**Description**
The time stamp that indicates when the current user last viewed a record that is related to
this CallTemplate.

```
LastViewedDate

Name

OwnerId

TemplateType

TotalCalls

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this CallTemplate. If this
value is null, this record might have been only referenced ( `LastReferencedDate` ) and
not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the call script.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the call script.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of call template.

Possible values are:

**•** `Text`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CallTemplate

**Field** **Details**

**Description**
The total number of calls that use the CallTemplate.

```
TotalCallsCallBackLater

TotalCallsLeftVoicemail

TotalCallsMeaningfulConnect

TotalCallsNotInterested

TotalCallsUncategorized

TotalCallsUnqualified

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Call Back Later call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Left Voicemail call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Meaningful Connect call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Not Interested call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total uncategorized call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Campaign

**Field** **Details**

**Description**
The total Unqualified call results that use the CallTemplate.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CallTemplateChangeEvent (API version 48.0)**
Change events are available for the object.

### Campaign

Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ActualCost

AmountAllOpportunities

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of money spent to run the campaign. Label is Actual Cost in Campaign.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign, including closed/won
opportunities. Label is Value Opportunities in Campaign.


Standard Objects Campaign

**Field** **Details**

```
AmountWonOpportunities

BriefId

BudgetedCost

CampaignImageId

CampaignMemberRecordTypeId

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in closed or won opportunities associated with the campaign. Label is
Value Won Opportunities in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the brief that's associated with the campaign. A brief contains additional context
about the goals and audience for the campaign. The label is Brief.

**Relationship Name**
Brief

**Relationship Type**
Lookup

**Refers To**
Record

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money budgeted for the campaign. Label is Budgeted Cost in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the campaign image. Available in API version 42.0 and later. Only available to orgs with
Partner Community licenses and Digital Experience enabled or orgs that have installed the
Direct Marketing Managed package.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
The record type ID for CampaignMember records associated with the campaign.

This is a relationship field.

**Relationship Name**
CampaignMemberRecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

```
CampaignStage

CreatedByID

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available with Marketing Cloud Growth and Advanced editions. The lifecycle
stage of the campaign based on the status of all of its related flows. Possible values are:

**•** In Planning

**•** In Progress

**•** Completed

**•** Error

**•** Canceled

**•** Paused

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who created the campaign.

This is a relationship field.

**Relationship Name**
Creator

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


Standard Objects Campaign

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
Description

EndDate

ExpectedResponse

ExpectedRevenue

HierarchyActualCost

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the campaign. Limit: 32 KB. Only the first 255 characters display in reports.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ending date for the campaign. Responses received after this date are still counted.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of responses you expect to receive for the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money you expect to generate from the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money spent to run the campaigns in a campaign
hierarchy. Label is Total Actual Cost in Hierarchy.


Standard Objects Campaign

**Field** **Details**

```
HierarchyAmountAllOpportunities

HierarchyAmountWonOpportunities

HierarchyBudgetedCost

HierarchyExpectedRevenue

HierarchyNumberOfContacts

HierarchyNumberOfConvertedLeads

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign in a campaign hierarchy,
including closed/won opportunities. Label is Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of money in closed or won opportunities associated with the campaign in a
campaign hierarchy. Label is Value Won Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money budgeted for the campaigns in a campaign
hierarchy. Label isTotal Budgeted Cost in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money you expect to generate from the campaign
in a campaign hierarchy. Label is Total Expected Revenue in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the number of contacts associated with the campaign hierarchy. Label
is Total Contacts in Hierarchy.

**Type**
currency


Standard Objects Campaign

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of converted leads from the campaign in a campaign
hierarchy. Label is Converted Leads in Hierarchy.

```
HierarchyNumberOfLeads

HierarchyNumberOfOpportunities

HierarchyNumberOfResponses

HierarchyNumberOfWonOpportunities

HierarchyNumberSent

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of leads from the campaign in a campaign hierarchy. Label
is Leads in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of opportunities related to the campaign in a campaign
hierarchy. Label is Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Number of contacts and unconverted leads with a Member Status equivalent to “Responded”
for the campaign in a campaign hierarchy. Label is **Responses in Hierarchy** .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Hierarchy.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
Calculated field for the total number of individuals targeted by the campaign in a campaign
hierarchy. For example, the number of email messages sent. The label is Num Sent in
Hierarchy.

```
HierarchyTotalEmailsDelivered

HierarchyTotalFormSubmissions

HierarchyTotalFormViews

HierarchyTotalLandingPageFormSubmissions

HierarchyTotalLandingPageViews

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign in a campaign hierarchy. Label
is Total Emails Delivered in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign in a campaign hierarchy. Label
is Total Form Submissions in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign in a campaign hierarchy. Label is
Total Form Views in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign in a
campaign hierarchy. Label is Total Landing Page Form Submissions in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
int


Standard Objects Campaign

**Field** **Details**

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign in a campaign hierarchy.
Label is Total Landing Page Views in Hierarchy. This field is available with Marketing Cloud
Account Engagement.

```
HierarchyUniqueEmailOpens

HierarchyUniqueEmailTrackedLinkClicks

HierarchyUniqueMarketingLinkClicks

IsActive

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign in a campaign hierarchy. Excludes
repeat opens. Label is Unique Email Opens in Hierarchy. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign in a campaign hierarchy.
Excludes repeat clicks. Label is Unique Email Clicks in Hierarchy. This field is available with
Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign in a campaign
hierarchy. Excludes repeat clicks. Label is Unique Marketing Link Clicks in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this campaign is active ( `true` ) or not ( `false` ). The default value is
`false` . The label is **Active** .


Standard Objects Campaign

**Field** **Details**

```
LastActivityDate

LastModifiedById

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** The due date of the most recent event logged against the record.

**•** The due date of the most recently closed task associated with the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who last updated the campaign.

This is a relationship field.

**Relationship Name**
Last Modified

**Relationship Type**
Lookup

**Refers To**
User

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.


Standard Objects Campaign

**Field** **Details**

```
Name

NumberOfContacts

NumberOfConvertedLeads

NumberOfLeads

NumberOfOpportunities

NumberOfResponses

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Name of the campaign. Limit: is 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of contacts associated with the campaign. Label is Total Contacts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of leads that were converted to an account and contact due to the marketing efforts
in the campaign. Label is Converted Leads.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of leads associated with the campaign. Label is Leads in Campaign.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of opportunities associated with the campaign. Label is Opportunities in
Campaign.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
The number of contacts and unconverted leads with a Member Status equivalent to
“Responded” for the campaign. Label is Responses in Campaign.

```
NumberOfWonOpportunities

NumberSent

OwnerId

ParentCampaign

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Campaign.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of individuals targeted by the campaign. For example, the number of emails
sent. Label is Num Sent.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns this campaign. Default value is the user logging in to the API to
perform the create.

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
Create, Filter, Nillable, Update

**Description**
The campaign above the selected campaign in the campaign hierarchy.


Standard Objects Campaign

**Field** **Details**

```
ParentId

RecordTypeId

StartDate

Status

TenantId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the parent Campaign record, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Starting date for the campaign.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Status of the campaign, for example, Planned, In Progress. Limit: 40 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
ID of the associated Marketing Cloud Account Engagement business unit. Read-only. Available
with Marketing Cloud Account Engagement in API version 51.0 and later.

This is a relationship field.

**Relationship Name**
Business Unit

**Relationship Type**
Lookup

**Refers To**
PardotTenant

```
TotalAmountAllOpportunities

TotalAmountAllWonOpportunities

TotalEmailsDelivered

TotalFormSubmissions

```

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for total amount of all opportunities associated with the campaign hierarchy,
including closed/won opportunities. Label is Total Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for amount of all closed/won opportunities associated with the campaign
hierarchy. Label is Total Value Won Opportunities in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign. Label is Total Emails Delivered
in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign. Label is Total Form Submissions
in Campaign. This field is available with Marketing Cloud Account Engagement.


Standard Objects Campaign

**Field** **Details**

```
TotalFormViews

TotalLandingPageFormSubmissions

TotalLandingPageViews

TotalNumberofLeads

TotalNumberofOpportunities

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign. Label is Total Form Views in Campaign.
This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign. Label is
Total Landing Page Form Submissions in Campaign. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign. Label is Total Landing Page
Views in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for total number of leads associated with the campaign hierarchy. This
number also includes converted leads. Label is Total Leads in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of opportunities associated with the campaign hierarchy.
Label is Total Opportunities in Hierarchy.


Standard Objects Campaign

**Field** **Details**

```
TotalNumberofResponses

TotalNumberofWonOpportunities

Type

UniqueEmailOpens

UniqueEmailTrackedLinkClicks

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for number of contacts and unconverted leads that have a `Member`
`Status` equivalent to “Responded” for the campaign hierarchy. Label is Total Responses
in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of won opportunities associated with the campaign
hierarchy. Label is Total Won Opportunities in Hierarchy.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Type of campaign, for example, Direct Mail or Referral Program. Limit: 40 characters.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign. Excludes repeat opens. Label is
Unique Email Opens in Campaign. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign. Excludes repeat clicks.
Label is Unique Email Clicks in Campaign. This field is available with Marketing Cloud Account
Engagement.


### Standard Objects CampaignInfluence

**Field** **Details**

```
UniqueMarketingLinkClicks

```

Usage

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign. Excludes repeat
clicks. Label is Unique Marketing Link Clicks in Campaign. This field is available with Marketing
Cloud Account Engagement.

Client applications can create, update, delete, and query Attachment records associated with a campaign via the API.

The Campaign object is defined only for those organizations that have the marketing feature enabled and valid marketing licenses. In
addition, it is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature
or valid marketing licenses, this object does not appear in the `describeGlobal()` call, and you can’t use `describeSObjects()`
or `query()` with the Campaign object.

Note: The main constituent of a campaign is a CampaignMember. You will commonly need to update campaigns with
CampaignMember.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CampaignChangeEvent (API version 44.0)**
Change events are available for the object.

**CampaignFeed (API version 18.0)**
Feed tracking is available for the object.

**CampaignHistory (API version 40.0)**
History is available for tracked fields of the object.

**CampaignOwnerSharingRule**

Sharing rules are available for the object.

**CampaignShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CampaignInfluence

Represents the association between a campaign and an opportunity in Customizable Campaign Influence. This object is available in API
version 37.0 and later.


Standard Objects CampaignInfluence

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0 .](https://help.salesforce.com/s/articleView?id=sf.campaigns_influence_original.htm&language=en_US)

[To ingest this object in Data Cloud, set up the Data Cloud Salesforce Connector permission set. See Enable Object and Field Permissions](https://help.salesforce.com/s/articleView?id=data.c360_a_crm_enable_object_and_field_permissions.htm&type=5&language=en_US)
[for CRM Connections.](https://help.salesforce.com/s/articleView?id=data.c360_a_crm_enable_object_and_field_permissions.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Customizable Campaign Influence must be enabled. Customer Portal users can’t access this object.

Fields

**Field Name** **Details**

```
CampaignId

CampaignMemberId

ContactId

Influence

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign that’s related to the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign member related to the opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the contact on the associated opportunity.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


Standard Objects CampaignInfluence

**Field Name** **Details**

**Description**

The percentage of the Amount field for the related opportunity that’s attributed
to the campaign.

```
ModelId

OpportunityContactRoleId

OpportunityId

RevenueShare

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the campaign influence model that’s related to the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity contact role ID of the related opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of revenue from the related opportunity attributed to the campaign.

Use this object to create campaign influence records for your custom campaign influence models. Don’t create campaign influence
records for the Primary Campaign Source model. Records added to the Primary Campaign Source model via the API are deleted when
the model is recalculated.


### Standard Objects CampaignInfluenceModel CampaignInfluenceModel

This read-only object represents a campaign influence model in Customizable Campaign Influence. Use campaign influence models to
### group CampaignInfluence records created by a specific set of triggers and workflows that you define. The Primary Campaign

Source influence model is the default model. This object is available in API version 37.0 and later.

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0.](https://help.salesforce.com/s/articleView?id=sales.campaigns_influence_customizable.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, Customizable Campaign Influence must be enabled. Customer Portal users can’t access this object.

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
The API name of the influence model. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is active. Active models can generate campaign
influence records. Deactivating a model deletes its campaign influence records.
Custom models are always active and this field is ignored.


Standard Objects CampaignInfluenceModel

**Field Name** **Details**

```
IsDefaultModel

IsModelLocked

Language

MasterLabel

ModelDescription

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is the default model ( `true` ) or not ( `false` ).
`CampaignInfluence` records associated with the default model appear in
3 locations.

**•** The Campaign Influence related list on opportunities

**•** The Influenced Opportunities related list on campaigns

**•** The Campaign Statistics section on campaigns

The value of `IsDefaultModel` can only be true for 1 model at a time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is locked ( `true` ) or not ( `false` ). Records for locked
models can only be added, updated, or deleted via the API.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the influence model.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the influence model.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the influence model.


Standard Objects CampaignInfluenceModel

**Field Name** **Details**

```
ModelType

NamespacePrefix

RecordPreference

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the model is the Primary Campaign Source influence model,
or a custom model. These values are the allowed.

**•** 1: Primary Campaign Source Model

**•** 2: Custom Model

**•** 3: First Touch Model

**•** 4: Last Touch Model

**•** 5: Even Distribution Model

**•** 6: Data-Driven Model

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
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The value of this field determines when to create campaign influence records.

**•** AllRecords: Creates records regardless of the revenue attribution percentage.


### Standard Objects CampaignMember

**Field Name** **Details**

**•** RecordsWithAttribution: Creates records only when the revenue attribution
is greater than 0%.

### CampaignMember

The CampaignMember object represents the relationship between a campaign and either a lead or a contact. If the Accounts as Campaign
Members setting is enabled in an org, CampaignMember can also represent the relationship between a campaign and an account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
AccountId

CampaignId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account related to the campaign. This field is available only if the Accounts as
Campaign Members setting is enabled in the org.

This field is a relationship field.

**Relationship Name**
Related Record ID

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects CampaignMember

**Field** **Details**

**Description**
Required. The ID of the campaign related to the lead or contact.

This field is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

```
City

CompanyOrAccount

ContactId

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the city for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company or account of the lead or contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a contact that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. This field contains
the ISO code for any currency allowed by the organization.

```
Country

Description

DoNotCall

Email

Fax

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the country for the account.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the associated lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the description of the account.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the lead or contact doesn’t want to be called. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate the account doesn’t want to be
called.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the email address for the account.

**Type**
phone


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the lead or contact. In orgs with the Accounts as Campaign Members setting
enabled, this field can be the fax number for the account.

```
FirstName

FirstRespondedDate

HasOptedOutOfEmail

HasOptedOutOfFax

HasResponded

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the lead or contact.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field indicates the date that the campaign member received a status of Responded.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the email opt-out preference for the lead or contact. A value of `false`
indicates that the lead or contact is opted in to emails. A value of `true` indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
be the opt-out preference for the account email address.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the fax opt-out preferences for the lead or contact. A value of false indicates
that the lead or contact is opted in to receiving faxes. A value of true indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
indicate the account has opted out of faxes.

**Type**
boolean


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates whether the campaign member has responded to the campaign ( `true` )
or not ( `false` ). Label is **Responded** .

```
LastName

LeadId

LeadOrContactId

LeadOrContactOwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the lead or contact. The limit is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a lead that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of a lead or contact that's related to the campaign. In orgs with the Accounts as
Campaign Members setting enabled, this field also accepts an account ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CampaignMember

**Field** **Details**

**Description**
The ID of the owner of the associated lead or contact owner. In orgs with the Accounts as
Campaign Members setting enabled, this field can be the owner of the account.

This field is a polymorphic relationship field.

**Relationship Name**
LeadOrContactOwner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
LeadSource

MobilePhone

Name

Phone

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source where the lead was obtained.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile phone number of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the mobile phone number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first and last name of the lead or contact that's related to the campaign member.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the phone number for the account.


Standard Objects CampaignMember

**Field** **Details**

```
PostalCode

RecordTypeId

Salutation

State

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the postal code for the account.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object. To change the record type, modify the
`CampaignMemberRecordTypeId` field on the associated Campaign.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salutation for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state for the address of the lead or contact. The limit is 80 characters. In orgs with the
Accounts as Campaign Members setting enabled, this field can be the state of the account
address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the `HasResponded` flag on this object. You can't directly set the
`HasResponded` flag, as it’s read-only. You can set it indirectly by setting this field in a
create or update call. Each predefined value implies a `HasResponded` flag value. Each
time you update this field, you implicitly update the `HasResponded` flag. In the Salesforce
user interface, Marketing users can define valid status values for the `Status` picklist. They


Standard Objects CampaignMember

**Field** **Details**

can choose one status as the default status. For each `Status` field value, they can also
select which values to count as “Responded,” meaning that the `HasResponded` flag is
set to `true` for those values. The limit is 40 characters.

When you create or update campaign members, use the text value for `Status` instead of
the ID from the CampaignMemberStatus object.

```
Street

Title

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the street of the account address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Title for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates if the campaign member is a lead or a contact. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate an account.

Note: If you’re importing CampaignMember data into Salesforce and want to set the value for an audit field, such as
`CreatedDate`, contact Salesforce. Audit fields are automatically updated during API operations unless you request to set these
fields yourself.

Usage

Each record has a unique ID, and must contain either a `ContactId` or a `LeadId`, but can't contain both. Any attempt to create a
single record with both results in a successful insert but only the `ContactId` is inserted. However, you can create two separate records
on a Campaign—one for the Lead and one for the Contact.

In orgs with the Accounts as Campaign Members setting enabled, the unique ID can be an `AccountID` .


### Standard Objects CampaignMemberStatus

Standard fields from a lead or contact are associated with the CampaignMember object, but you can’t query them directly. To include
a `Phone` in your query, for example, query the field from the Lead object.

```
   SELECT Id, (SELECT Phone FROM Lead)

   FROM CampaignMember

```

This object is defined only for orgs that have the marketing feature and valid marketing licenses. If your org doesn’t have the marketing
feature or valid marketing licenses, this object doesn’t appear in the `describeGlobal()` call, and you can't use
`describeSObjects()` or `query()` with this object.

Note: If you want to track lead-based campaign members you convert to contacts, provide both a ContactId and a LeadId.
Otherwise, only use one ID type.

To issue `create()` requests to the API, your account only requires read access to campaigns.

If the record doesn’t exist for the specified `ContactId` or `LeadId`, then a new record is created. If the record exists, an error is
returned and no update is made. To update an existing record, specify the ID of the CampaignMember record to update.

To delete a record, specify the ID of the CampaignMember record.

When creating or updating records, the `Status` field value specified in the call is verified as a valid status for the given Campaign:

**•** If the specified `Status` value is a valid status, the value is updated, and the `HasResponded` field is updated to either `true`
or `false`, depending on the `Status` value association with `HasResponded` .

**•** If the specified `Status` value isn’t a valid status, the API assigns the default status to the `Status` field and updates the
`HasResponded` field with the associated value. However, if the given Campaign doesn’t have a default status, the API assigns
the value specified in the call to the `Status` field, and the `HasResponded` field is set to `false` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

### Campaign CampaignMemberStatus CampaignMemberStatus

One or more member status values defined for a campaign.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.


Standard Objects CampaignMemberStatus

You can't delete a CampaignMemberStatus if that status is designated as the default status or if the status is currently used in a Campaign.

Fields

**Field** **Details**

```
CampaignId

HasResponded

IsDefault

IsDeleted

Label

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the campaign associated with this member status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is equivalent to “Responded” ( `true` ) or not ( `false` ). Beginning
with API version 39.0, at least one `CampaignMemberStatus` on each campaign must
have a `hasResponded` value of `true` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is the default status ( `true` ) or not ( `false` ). Beginning with
API version 39.0, there must be a default CampaignMemberStatus defined for every campaign.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
string

**Properties**
Filter, Sort

**Description**
Label for the status in the picklist. Limited to 765 characters.


### Standard Objects CampaignOwnerSharingRule

**Field** **Details**

```
 SortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort, Update

**Description**
Unique number order where this campaign member status appears in the picklist.

Use this object to create picklist items for the member status in a campaign.

This object is defined only for those organizations that have the marketing feature and valid marketing licenses. In addition, the object
is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature or valid
marketing licenses, this object does not appear in a `describeGlobal()` call, and you can't use `describeSObjects()` or
`query()` with the CampaignMember object.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberStatusChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

### Campaign

CampaignMember

### CampaignOwnerSharingRule

Represents the rules for sharing a campaign with User records other than the owner or anyone above the owner in the role hierarchy.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CampaignOwnerSharingRule

Fields

**Field** **Details**

```
CampaignAccessLevel

Description

DeveloperName

GroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available in
API version 29.0 and later.

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
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CampaignShare

**Field** **Details**

**Description**
The ID representing the source group. A Campaign owned by a User in the source Group
triggers the rule to give access.

```
Name

UserOrGroupId

```

Usage

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

Use this object to manage the sharing rules for campaigns.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### CampaignShare

Represents a sharing entry on a Campaign.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CampaignShare

Special Access Rules

As of Summer ’20 and later, only users with access to the Campaign object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
CampaignId

CampaignAccessLevel

RowCause

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Campaign associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Campaign. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for creating or updating records.)

This field must be set to an access level that is higher than the organization’s default access
level for Campaign.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects CampaignTag

**Field** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values:

**•** `Rule` —The User or Group has access via a Campaign sharing rule.

**•** `GuestRule` —The User or Group has access via a Campaign guest user sharing rule.

**•** `Manual` —The User or Group has access because a User with “ `All` ” access manually
shared the Campaign with them.

**•** `Owner` —The User is the owner of the Campaign.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Campaign via an account relationship data sharing rule.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Campaign. This field can't be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view or edit Campaign records owned by other users.

### CampaignTag

Associates a word or short phrase with a Campaign.


Standard Objects CampaignTag

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

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .


### Standard Objects CardPaymentMethod

Usage

CampaignTag stores the relationship between its parent TagDefinition and the Campaign being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### CardPaymentMethod

Represents a credit card or debit card payment method, which implements the PaymentMethod object. This object is available in API
version 48.0 and later.

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
Customer account for the payment method.

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


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Email address of the card owner where audit information about payments gets sent.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for orgs that
upgraded from v48.0. Users must add it to the CardPaymentMethod page layout on their
own.

```
AutoCardType

CardBin

CardCategory

CardHolderFirstName

CardHolderLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Card network type, derived from the card number.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
First six digits of the card number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines whether the card is a credit card or debit card.

Possible values are:

**•** `CreditCard`

**•** `DebitCard`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the cardholder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Last name of the cardholder.

```
CardHolderName

CardLastFour

CardPaymentMethodNumber

CardType

CardTypeCategory

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Full name of the cardholder.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Last four digits of the credit card or debit card.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for the card payment method.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifies the credit card type.

Possible values are:

**•** `American Express`

**•** `Diners Club`

**•** `JCB`

**•** `Maestro`

**•** `Master Card`

**•** `Visa`

**Type**
picklist


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Further identifies the credit card. Used for internal reference.

Possible values are:

**•** `AmericanExpress`

**•** `DinersClub`

**•** `Discover`

**•** `Jcb`

**•** `Maestro`

**•** `MasterCard`

**•** `UnionPay`

**•** `Visa`

```
Comments

CompanyName

DisplayCardNumber

Email

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Payment admin can add comments to provide additional details about a record. Maximum
of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company of the cardholder.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Masked digits for the full credit card number except the last four digits.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Email address of the payer.

```
ExpiryMonth

ExpiryYear

GatewayDate

GatewayResultCode

GatewayResultCodeDescription

GatewayToken

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration year.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the payment gateway logs a card activity.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The result of the card payment method’s interaction with the payment gateway during a
transaction request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the gateway result code. Descriptions vary between payment
gateway providers.

**Type**
string


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the card
payment method during transactions. `GatewayToken` is for use with APIs earlier than
version 52.0. For version 53.0 and latter, use the GatewayTokenEncrypted field. To secure
the token, use the `GatewayTokenEncrypted` field.

An error message appears if you try to record a `GatewayToken` for a card payment
method that already has a `GatewayToken` or `GatewayTokenEncrypted` value.

```
GatewayTokenDetails

GatewayTokenEncrypted

InputCardNumber

IpAddress

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional information about the gateway token.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Encrypted unique token ID generated by the payment gateway to represent the card payment
method during transactions. Encrypted using Salesforce Classic Encryption.

Available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Used by a payer to enter a credit card number when storing an external-type card payment
method. After entry, the credit card number isn’t saved, so the `InputCardNumber` value
always appears blank. The credit card number appears as a masked value in
`DisplayCardNumber`, which shows only the last four digits.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address of the card payment method holder.


Standard Objects CardPaymentMethod

**Field** **Details**

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

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

**Description**
Indicates whether the payment method can be used for recurring payments ( `True` ) or not
( `False` ). The default value is `False` .

This field is available in API version 55.0 and later. For orgs that upgraded from version 54.0,
you must add this field to the Card Payment Method page layout in the UI. It isn't automatically
added.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record or list view related to this
record, but didn’t access it directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user referenced this record but didn’t view it directly.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
MAC address of the card payment method holder.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.


Standard Objects CardPaymentMethod

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
Payer-defined nickname for the card payment method.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The payment gateway used to create a gateway token. For transactions with a saved payment
method in Salesforce, this field stores the payment gateway ID used in the transaction.

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
Full address associated with the card payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Country of the address for the payment method.

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


Standard Objects CardPaymentMethod

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
Postal Code of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State of the address for the payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of payment method types such as Apple
Pay and Google Pay. This field is available in API version 57.0 and later.

**Type**
picklist


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction. This field is available in API version 57.0 and later.

Possible values are:

**•** `AfterpayClearpay`

**•** `AmericanExpress`

**•** `ApplePay`

**•** `BanContact`

**•** `DinersClub`

**•** `Discover`

**•** `EPS`

**•** `GooglePay`

**•** `Jcb`

**•** `Klarna`

**•** `Maestro`

**•** `MasterCard`

**•** `Other`

**•** `PayPal`

**•** `SepaDebit`

**•** `UnionPay`

**•** `Venmo`

**•** `Visa`

**•** `iDeal`

```
Phone

ProcessingMode

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payer.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Defines whether the card payment method is used for transactions made by Salesforce
Payments or by an external third-party payment provider.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` —Salesforce made and recorded an external call to the payment platform.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

You must enter a value for this field.

```
SavedPaymentMethodId

SfResultCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record. This field is available in API version 60.0 and
later.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The results of the card payment method’s interaction with the payment gateway.

Possible values are:

**•** `Decline`

**•** `Indeterminate`

**•** `PermanentFail`

**•** `RequiresReview`

**•** `Success`

**•** `SystemError`

**•** `ValidationError`


Standard Objects CardPaymentMethod

**Field** **Details**

```
StartMonth

StartYear

Status

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The month is activated.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the card is activated.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment method.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `InActive`

The following fields drop zeroes that appear at the beginning of the field value, and introduce commas for values with four or more
digits:

**•** `CardLastFour`

**•** `CardBin`

**•** `ExpiryYear`

For example, a `CardLastFour` entered value of _`0004112233445566`_ would appear as _`4,112,233,445,566`_ on the record.

As a workaround, create a String-type custom formula field with the same label as the field that you want to replace, then hide the
original field. Here are some examples for replacing `CardLastFour`, `CardBin`, and `ExpiryYear` .

**CardLastFour**

```
  IF(ISBLANK(CardLastFour), NULL,RIGHT("0000" & TEXT(CardLastFour), 4))

```

**CardBin**

```
  IF(ISBLANK(CardBin), NULL,RIGHT("000000" & TEXT(CardBin), 6))

```


### Standard Objects CartCheckoutSession

**ExpiryYear**

```
    IF(ISBLANK(ExpiryYear), NULL,TEXT(ExpiryYear)))

### CartCheckoutSession

```

Represents a checkout session used in Lightning B2B Commerce checkout. This object is available in API version 48.0 and later.

A checkout session is tied to a single web cart, but there can be multiple checkout sessions for a single cart.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
BackgroundOperationId

CurrencyIsoCode

IsArchived

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the in progress background operation.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for the checkout session. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CartCheckoutSession

**Field** **Details**

**Description**
Indicates whether checkout processing is archived ( `true` ) or not ( `false` ). After a session
is archived, it can’t be unarchived. Default value is `false` .

```
IsError

IsProcessing

Name

NextState

OrderId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the session is in error state ( `true` ) or not ( `false` ). Default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether checkout processing is in progress ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the checkout session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a created order after the checkout session has gone from cart to order.


### Standard Objects CartDeliveryGroup

**Field** **Details**

```
OrderReferenceNumber

State

WebCartId

### CartDeliveryGroup

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique reference number the shopper can use to refer to the order. In API version 63.0 and
later, LWR stores don't populate this field upon checkout. Instead, the
`InitialOrderReferenceNumber` field on the WebCart object is populated.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The current state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the cart that is used to create the checkout session.

Represents shipping information for the delivery of items in an order against a store built with B2B Commerce or D2C Commerce. This
object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects CartDeliveryGroup

Fields

**Field** **Details**

```
CartId

CompanyName

CurrencyIsoCode

DeliverToAddress

DeliverToCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID the `WebCart on page 5791` that’s associated with this delivery group.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with a delivery. This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `USD` —U.S. Dollar

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address to which a buyer order is delivered.

**Type**
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city to which a buyer order is delivered.

```
DeliverToCountry

DeliverToFirstName

DeliverToGeocodeAccuracy

DeliverToLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to which a buyer order is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the person set to receive an order. This field is available in API version 57.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The geocode location to which a buyer order is delivered. Possible values are:

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
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the person to whom a buyer order is delivered. This field is available in API
version 57.0 and later.

```
DeliverToLatitude

DeliverToLongitude

DeliverToName

DeliverToPostalCode

DeliverToState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of a buyer delivery location.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of a buyer delivery location.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the person to deliver a buyer order to. This field is set based on the `Name` field
of the `ContactPointAddress` associated with this delivery group.
`ContactPointAddress.Name` is generated by the system using the first and last
names entered by a buyer during checkout.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code to which to deliver a buyer order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartDeliveryGroup

**Field** **Details**

**Description**
The state to which to deliver a buyer order.

```
DeliverToStreet

DeliveryMethodId

DesiredDeliveryDate

GiftMessage

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street to which to deliver a buyer order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the delivery method to use to deliver a buyer order. Populated if the selected
`CartDeliveryGroupMethod` only has the `ShippingFee` populated, but it has
reference to an existing `DeliveryMethodId` which contains the fields `Carrier`,
`ClassOfService`, and `ReferenceNumber` . If not, the
`SelectedDeliveryMethod` field is used.

This field is a relationship field.

This field is deprecated in API version 64.0 and will be removed in API version 66.0. Instead,
use the `DeliveryMethodId` field on the `CartDeliveryGroupMethod` object.

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that a buyer requests to have an order delivered.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects CartDeliveryGroup

**Field** **Details**

**Description**
Personalized gift message for the order. This field is available in API version 64.0 and later.

```
GiftToName

GrandTotalAmount

IsDefault

IsGift

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the recipient for a gift order. This field is available in API version 64.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items’ `TotalAmount`, or `CartDeliveryGroupTotalAmount` plus
`CartDeliveryGroup TotalTaxAmount` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the delivery group is the default. This field is available in API version 59.0 and
later.

The default value is `false` .

B2B and D2C stores create a default delivery group, along with a WebCart, when a customer
adds an item to cart and doesn't have an existing cart. The default cart delivery group is
needed to complete the checkout flow, and can't be replaced by a non-default cart delivery
group. If you customize the standard checkout flow, make sure that you don't delete the
default cart delivery group.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the delivery group is a gift. This field is available in API version 64.0 and later.

The default value is `false` .

**Type**
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartDeliveryGroup` record. `Name` can be up to 255 characters. In
API version 62.0 and later, if `IsDefault` is `true`, the `Name` is `Shipment1`, a localized
string. In prior API versions, the `Name` for a default delivery group was `Cart Delivery`
`Group` . Due to this change, any queries intended to identify default delivery groups should
use the `IsDefault` rather than `Name` field.

```
SelectedDeliveryMethodId

ShipToPhoneNumber

ShippingInstructions

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the selected cart delivery group method. Populated if the selected
`CartDeliveryGroupMethod` has the fields `Carrier`, `ClassOfService`,
`ReferenceNumber`, and `ShippingFee`, but the `DeliveryMethodId` is null. If
not, the `DeliveryMethodId` field is used. This field is available in API version 59.0 or
later.

This field is a relationship field.

**Relationship Name**
SelectedDeliveryMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with a delivery. This field is available in API version 59.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Instructions for delivering an order.


Standard Objects CartDeliveryGroup

**Field** **Details**

```
TotalAdjustmentAmount

TotalAdjustmentTaxAmount

TotalAmount

TotalCartItemCount

TotalChargeAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all promotional adjustments on the cart delivery group. This field is
available in API version 54.0 and later.

For product bundles, this includes the aggregate adjustments of all child components.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total tax amount for all promotional adjustments on the cart delivery group. This field
is available in API version 54.0 and later.

For product bundles, this includes the aggregate of the tax amounts for all child components’
adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all cart items `TotalPrice`, or `TotalProductAmount` plus
`TotalChargeAmount` .

For product bundles, this includes the aggregate of all child component prices.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cart items, including their quantities, of the type `PRODUCT` in the delivery
group.

For product bundles, this count includes only the parent component.

If the total quantity of cart items of type `PRODUCT` in the delivery group exceeds the
system-defined maximum (INT_MAX), this field is set to INT_MAX.

**Type**
currency


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalPrice` for all cart items of type `CHARGE` . Cart items
can be of type Product or Charge.

For product bundles, if a child component includes a cart item of type `CHARGE`, its amount
is aggregated with the parent’s cart item's total charge amount.

```
TotalChargeTaxAmount

TotalProductAmount

TotalProductTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalTaxAmount` for all cart items of type `CHARGE` . Cart
items can be of type Product or Charge.

For product bundles, this includes the aggregate of all tax amounts associated with
bundle-level charges, including the taxes of individual child products.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalPrice` for all cart items of type `PRODUCT` . Cart items
can be of type Product or Charge.

For product bundles, this includes the aggregate of all child component prices.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalTaxAmount` for all cart items of type `PRODUCT` . Cart
items can be of type Product or Charge.

For product bundles, this includes the aggregate of all child component taxes based on their
individual prices.

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects CartDeliveryGroupMethod

**Field** **Details**

**Description**
The sum of all cart items `TotalTaxAmount`, or the combined value of
`TotalProductTaxAmount` plus `TotalChargeTaxAmount` .

For product bundles, this includes the aggregate of all child component taxes based on their
individual prices.

Associated Objects

**CartDeliveryGroupChangeEvent (API version 58.0)**
Change events are available for the object.

### CartDeliveryGroupMethod

Represents the selected delivery method for a cart delivery group used in Lightning B2B Commerce checkout. This object is available in
API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroupMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustedShippingFee

Carrier

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shipping fee, including `TotalAdjustmentAmount`, for the delivery method.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

**Description**
The carrier that the buyer chose for their delivery method. Values are defined based on the
user’s shipping service. This field is available in API version 59.0 or later.

```
CartCheckoutSessionId

CartDeliveryGroupId

ClassOfService

CurrencyIsoCode

DeliveryMethodId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID used to identify your cart checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the cart delivery group associated with the checkout session.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier class of service that the buyer chose for their delivery method. Values are defined
based on the user’s shipping service. This field is available in API version 59.0 or later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for your shipping fee. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the selected order delivery method.


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

```
ExternalProvider

IsActive

Name

ProcessTime

ProcessTimeUnit

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external shipping method provider. Optional field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Assign new delivery groups to active delivery methods. The default value is `False` . This
field is available in API version 59.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Merchant-specified process time for the delivery method. Process time includes the time
between when an order is placed and when the shipment is given to the shipping carrier.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to define `ProcessTime` .

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

```
ProductId

ReferenceNumber

ShippingFee

TotalAdjustmentAmount

TransitTimeMax

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. This product represents a delivery charge order product for a delivery using this
delivery method. For example, you could create a product that represents an overnight
express charge and assign it to an overnight express delivery method. If your store uses
[Salesforce Native Shipping, the](https://help.salesforce.com/s/articleView?id=commerce.comm_set_up_native_shipping.htm&type=5&language=en_US) `ProductId` is selected from a non-variation product with
`Shipping` in its name. The term `Shipping` in a product name isn’t localized. If no
matching product is found, a random non-variation product is used. This field is available in
API version 59.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference number for an external delivery method. This field is available in API version 59.0
or later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Shipping fee associated with the delivery method. Required field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The adjustment amount of a promotion applicable to the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects CartDeliveryGroupMethodAdj

**Field** **Details**

**Description**
Maximum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

```
TransitTimeMin

TransitTimeUnit

WebCartId

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to define `TransitTimeMax` and `TransitTimeMin` .

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the WebCart associated with the cart delivery group method. Required field.

Use the CartDeliveryGroupMethod object to give commerce buyers the ability to choose a delivery method for a cart delivery group.
Shipping integrations populate the delivery options that are available for a cart delivery group.

### CartDeliveryGroupMethodAdj

Represents the shipping promotion discount for a shipping method. This object is available in API version 60.0 and later.


Standard Objects CartDeliveryGroupMethodAdj

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroupMethodAdj object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentBasisReferenceId

AdjustmentType

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount subtracted from the price by the shipping promotion discount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the adjustment basis reference. This is the coupon that causes the adjustment. This
field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
AdjustmentBasisReference

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of shipping promotion discount.

Possible values are:

**•** `AdjustmentAmount`

**•** `AdjustmentPercentage`

**•** `OverrideAmount`


Standard Objects CartDeliveryGroupMethodAdj

**Field** **Details**

```
AdjustmentValue

CartDeliveryGroupMethodId

CurrencyIsoCode

Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Number representing the value of the price adjustment. For example, if the
`AdjustmentType` is `AdjustmentPercentage`, a -10 `AdjustmentValue`
means 10 percent off. If the `AdjustmentType` is `AdjustmentAmount`, a -10
`AdjustmentValue` means 10 dollars off.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cart delivery group method.

This field is a relationship field.

**Relationship Name**
CartDeliveryGroupMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the cart delivery group method adjustment.


### Standard Objects CartItem

**Field** **Details**

```
PriceAdjustmentCauseId

Priority

### CartItem

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the price adjustment cause.

This field is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple promotional adjustments, the order in which the shipping promotion
is applied.

Represents an item in a `WebCart` that’s active in a store built with B2B or D2C Commerce. Cart item can be of type `Product` or
`Charge` . This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItem object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects CartItem

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentTaxAmount

AssociatedItemPricing

CartDeliveryGroupId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Non-itemized adjustments for this cart item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax that’s calculated on the `AdjustmentAmount` .

**Type**
picklist

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies how a child cart item is priced relative to its parent cart item within a product
bundle. This field is `null` for standalone products that aren't part of a bundle. Available in
API version 65.0 and later.

Possible values are:

**•** `IncludedInBundlePrice` —Indicates that the parent product’s price includes
the aggregated prices of its child components.

**•** `NotIncludedInBundlePrice` —Indicates that the parent product’s price doesn’t
include the aggregated prices of its child components.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the `CartDeliveryGroup` that’s associated with a cart item.

This field is a relationship field.

**Relationship Name**
CartDeliveryGroup

**Relationship Type**
Lookup


Standard Objects CartItem

**Field** **Details**

**Refers To**
CartDeliveryGroup

```
CartId

ChildProductCount

ConfigureDuringSale

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the `WebCart` that’s associated with a cart item.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of child products associated with this cart item. If a child product is a
bundle, its own `ChildProductCount` is included in this total. For simple products that
don’t have any child products, the `ChildProductCount` value is zero.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specify whether a product bundle is configurable. Available in API version 65.0 and later.

Possible values are:

**•** `Allowed`

**•** `NotAllowed`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

```
DistributedAdjustment

Amount

DistributedAdjustment

TaxAmount

GrossAdjustmentAmount

GrossUnitPrice

```

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the amount of a cart-wide promotional adjustment when
distributed across all items in the cart. This field is for display purposes only and is valid only
during checkout. This field is available in API version 52.0 and later.

You receive $10 off, and there are 5 items in the cart. The distributed adjustment is (-$2).

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the amount of a cart-wide tax adjustment due to
promotions when distributed across all items in the cart. This field is available in API version
52.0 and later.

EXAMPLE: Your discount causes a cart-wide tax reduction of (-$10), and there are 5 items in
the cart. The distributed tax adjustment is (-$2).

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The gross amount of the price adjustment on the cart item (tax inclusive). This is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gross amount of the unit price for a cart item (tax inclusive). This is available in API version
55.0 and later.


Standard Objects CartItem

**Field** **Details**

```
IsShippingChargeNot

Applicable

ItemizedAdjustment

Amount

ItemizedAdjustment

TaxAmount

ListPrice

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether shipping charges are applicable ( `true` ) or not ( `false` ) to the cart item.
The default value is `false` .

This field is available in API version 64.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotional adjustments that are
specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. Your itemized adjustment amount
is (-$10) for that item.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotion-related tax adjustments
that are specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. This reduces the tax on that item
by (-$2). Your itemized adjustment tax amount is (-$2) for that item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The original price of the cart item. Typically shown with a line through it. List price is shown
only when it’s higher than the negotiated price. If the list price is the same or lower, it isn’t
shown to the buyer. This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The name of this `CartItem` record. `Name` can be up to 255 characters.

```
NetAdjustmentAmount

NetUnitPrice

ParentCartItemId

PerUnitWeight

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The net amount of the price adjustment made on the cart item (tax exclusive). This is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net amount of the unit price for the cart item (tax exclusive). This is available in API
version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the cart item's parent `CartItem` . The value is empty if the item is a top-level cart
item.

This field is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Weight per unit of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.


Standard Objects CartItem

**Field** **Details**

```
Product2Id

ProductClass

ProductRelated

ComponentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a product type cart item. Cart items can be of type `PRODUCT` or `CHARGE` .

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product class of the cart item. Default value is `Simple` . Possible values are:

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the cart item's `ProductRelatedComponent` . The
`ProductRelatedComponent` represents a product that is included in a product
bundle, a set, or a product and an add-on. The `ProductRelatedComponent` is empty
if the item is a top-level cart item.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup


Standard Objects CartItem

**Field** **Details**

**Refers To**
ProductRelatedComponent

```
ProductValidationKey

ProductRelationship

TypeId

Quantity

QtyScaleMethod

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product validation key of the cart item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product relationship type that defines the relationship between a product
bundle and its child product. Available in API version 65.0 and later.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**

[https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_productrelationshiptype.htmProductRelationshipType](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_productrelationshiptype.htm)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of a given cart item in a cart.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Determines how a child product's quantity scales when added to a cart or configured within
a product bundle. Available in API version 65.0 and later. Possible values are:

**•** `Constant` —Represents a value that remains fixed relative to the parent bundle.


Standard Objects CartItem

**Field** **Details**

**•** `Proportional` —Represents a value that varies in proportion to the parent bundle’s
price or quantity.

```
SalesPrice

Sku

StockCheckMethod

SubType

TaxTreatmentId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The discounted price of a cart item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Shelf-Keeping Unit ID of a cart item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines how inventory is assessed for a cart item that’s part of a bundle or set. Possible
values are:

**•** `ChildProducts` —Inventory is assessed based on the child product or products.

**•** `ParentProduct` —Inventory is assessed based on the parent product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the subtype of the product. Possible values are:

**•** `Bonus` —Bonus product.

**•** `GiftWrap` —Gift wrapped product.

This field is available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The ID of the related tax treatment for the cart item.

This field is available in API version 63.0 and later. This field is available with Subscription
Management.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

```
TotalAdjustmentAmount

TotalAmount

TotalLineAmount

TotalLineGrossAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total amount of all promotional adjustments on the item, both distributed and itemized.
This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total cost of this cart item, including taxes and adjustments.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on sales price and quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount of the line item (tax inclusive). This is available in API version 55.0
and later.


Standard Objects CartItem

**Field** **Details**

```
TotalLineNetAmount

TotalLineTaxAmount

TotalListPrice

TotalPrice

TotalPriceAfterAll

Adjustments

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total net amount of the line item (tax exclusive). This is available in API version 55.0 and
later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total tax amount for `TotalLineAmount` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on `ListPrice` . We provide this value for comparison.
It's not the price that the buyer is paying.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, including adjustments but excluding taxes.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after all price adjustments are applied. This field is available in API version 52.0
and later.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)


Standard Objects CartItem

**Field** **Details**

```
TotalPriceTaxAmount

TotalPromo

AdjustmentAmount

TotalPromoAdjustment

TaxAmount

TotalTaxAmount

TotalWeight

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for a cart item before promotional adjustments, including quantity-based
adjustments. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total itemized and distributed adjustment amount in cart (only for promotions). This field is
available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total itemized and distributed adjustment tax amount in cart (only for promotions). This
field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for this cart item. This value includes taxes for both `TotalLineAmount`
and `AdjustmentAmount` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total weight of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.

**Type**
picklist


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `CartItem` type. Possible values are:

**•** `Product`

**•** `Charge`

```
UnitAdjustedPrice

UnitAdjustedPrice

WithItemAdj

UnitAdjustmentAmount

UnitItemAdjustment

Amount

WeightUnit

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Price per quantity unit after a tier discount or surcharge is applied. This field is available in
API version 50.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price, including both tier and item level discounts, for the item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tier discount or surcharge to apply to a quantity unit. This amount is added to the
`SalesPrice` to get the `UnitAdjustedPrice` . This field is available in API version
50.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Item level adjustments made to the unit price for the item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects CartItemAttribute

**Field** **Details**

**Description**
Unit of measurement for the weight of the cart item. This field is available in API version 62.0
and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

CartDeliveryGroup

WebCart

### CartItemAttribute

Represents the attributes associated with a cart item, stored as key-value pairs. These attributes are derived from the product and carried
forward to the order during checkout. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The CartItemAttribute object is available:only if the B2B Commerce license, the Salesforce CPQ feature, and Commerce Dynamic Bundles
are enabled in your Salesforce org.


Standard Objects CartItemAttribute

Fields

**Field** **Details**

```
AttributeDefinitionId

AttributeName

AttributePicklistValueId

AttributeValue

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the attribute definition associated with the cart item attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup

**Refers To**

[AttributeDefinition](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_attributedefinition.htm)

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the cart item attribute.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the picklist value associated with the cart item attribute.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**

[AttributePicklistValue](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_attributepicklistvalue.htm)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItemAttribute

**Field** **Details**

**Description**
The value of the cart item attribute, such as Blue or Large.

```
CartItemId

ExternalId

IsPriceImpacting

UnitOfMeasure

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the cart item to which this attribute is assigned.

This field is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Master-detail

**Refers To**

[CartItem (the master object)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_cartitem.htm)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An auto-generated ID for the attribute record that's stored in an external system, such as the
HBase database.

**Type**
boolean

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the attribute affects cart pricing ( `true` ) or not ( `false` ). This field
determines whether the Commerce Pricing API calls must be triggered to update the price.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the unit of measure associated with the cart item attribute.

This field is available only if the AttributeUomPilot Org perm is enabled. Contact Salesforce
support for assistance.


### Standard Objects CartItemPriceAdjustment

**Field** **Details**

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**

[UnitOfMeasure](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_unitofmeasure.htm)

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CartItemAttributeChangeEvent on page 68**
Change events are available for the object.

**CartItemAttributeFeed on page 55**
Feed tracking is available for the object.

**CartItemAttributeHistory on page 63**
History is available for tracked fields of the object.

**CartItemAttributeOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CartItemAttributeShare on page 67**
Sharing is available for the object.

### CartItemPriceAdjustment

Price adjustment for a cart item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItemPriceAdjustment object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects CartItemPriceAdjustment

Fields

**Field** **Details**

```
AdjustmentAmountScope

AdjustmentBasisReferenceId

AdjustmentSource

AdjustmentTargetType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Scope of the adjustment amount for a promotion.

Possible values are:

**•** `Total` —The amount off the total price.

This field is available in API version 54.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon code of the coupon associated with a promotion. This field is available in API version
54.0 and later.

This is a relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`

**•** `System`

**Type**
picklist


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target for the price adjustment (the cart itself or individual items).

Possible values are:

**•** `Cart`

**•** `Item`

```
AdjustmentType

AdjustmentValue

CartId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates if the price adjustment is applied as percentage or an absolute amount.

Possible values are:

**•** `AdjustmentAmount`

**•** `AdjustmentPercentage`

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Numeric value of the adjustment (for example, 10 if the price adjustment is either 10% off
or $10 off).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the WebCart that’s associated with a cart item. This field is available in API version
55.0 and later.

This is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart


Standard Objects CartItemPriceAdjustment

**Field** **Details**

```
CartItemId

CurrencyIsoCode

Description

Name

PriceAdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent cart item to which this adjustment belongs.

This is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the price adjustment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the price adjustment.

**Type**
reference


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
ID of entity that caused this adjustment (for example, a promotion ID). If unspecified, then
`Description` populates the display name.

This is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

```
Priority

TotalAmount

TotalGrossAmount

TotalNetAmount

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple price adjustments, sequence in which the price adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total price after applying price adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount (tax inclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects CartTax

**Field** **Details**

**Description**
The total net amount (tax exclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

```
TotalTax

WebCartAdjustmentGroupId

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the total adjusted price.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the cart’s adjustment group.

This is a relationship field.

**Relationship Name**
WebCartAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
WebCartAdjustmentGroup

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemPriceAdjustmentChangeEvent (API version 58.0)**
Change events are available for the object.

### CartTax

Represents taxes for a line item in a `WebCart` that’s active in a store built with B2B Commerce or D2C Commerce. This object is available
in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects CartTax

Special Access Rules

The CartTax object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentTargetType

Amount

CartId

CartItemId

CartItemPriceAdjustmentId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Target for the price adjustment (the cart itself or individual items). This field is available in
API version 52.0 and later.

Possible values are:

**•** `Cart`

**•** `Item`

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Calculated tax amount.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the `WebCart` being taxed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a cart item being taxed.

**Type**
reference


Standard Objects CartTax

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a price adjustment for a cart item being taxed. (This field is available in API version
52.0 and later.)

**Refers To**
CartItemPriceAdjustment

```
CurrencyIsoCode

Description

Name

TaxCalculationDate

TaxRate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Valid values include:

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the tax. Enter up to 2000 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartTax` record. `Name` can be up to 255 characters.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date this tax was calculated.

**Type**
percent


### Standard Objects CartValidationOutput

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The applied tax rate for this line of tax.

```
TaxType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of tax for this line of tax. Possible values are:

**•** `Actual`

**•** `Estimated`

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartTaxChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart

### CartValidationOutput

Associate errors to cart entities, such as cart line items, delivery groups, and the like, in a store built with B2B Commerce or D2C Commerce.
An example error is “Out of stock.” Available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout() describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartValidationOutput object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects CartValidationOutput

Fields

**Field** **Details**

```
BackgroundOperationId

CartId

CurrencyIsoCode

IsDismissed

Level

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the background operation that ran the validation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related `WebCart` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is
`USD` .Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the validation process is finished. Default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of output resulting from the validation process. Possible values are:

**•** 0 ( `Info` )

**•** 1 ( `Error` )


Standard Objects CartValidationOutput

**Field** **Details**

**•** 2 ( `Warning` )

```
Message

Name

RelatedEntityId

RelatedEntityPrefix

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the message to show in the log when validation is complete. Message can be up to
255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartValidationOutput` record. `Name` can be up to 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Foreign key to `WebCart`, `CartItem`, and `CartDeliveryGroup` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Three-character prefix for the related entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The `CartValidationOutput` type. Possible values are:

**•** `CartSave`  - Available in API version 64.0 and later.

**•** `Entitlement`

**•** `Inventory`

**•** `Other`


### Standard Objects Case

**Field** **Details**

**•** `Pricing`

**•** `Promotions`

**•** `Shipping`

**•** `ShippingPromotions`

**•** `SystemError`

**•** `Taxes`

Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartValidationOutputChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart

CartItem

CartDeliveryGroup

### Case

Represents a case, which is a customer issue or problem.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this case.

This is a relationship field.

**Relationship Name**
Account


Standard Objects Case

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
AssetWarrantyID

BusinessHoursId

Comments

CaseNumber

ClosedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Asset associated with the warranty. Must be a valid asset warranty ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the business hours associated with this case.

**Type**
textarea

**Properties**
Create, Delete, Layout, Nillable, Query, Retrieve, Search, Sort, Undelete, Update

**Description**
Used to insert a new CaseComment. Email textarea has a length of 4000 chars.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Assigned automatically when each case is inserted. It can't be set directly, and it can't be
modified after the case is created.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was closed.


Standard Objects Case

**Field** **Details**

```
CommunityId

ConnectionReceivedId

ConnectionSentId

ContactEmail

ContactFax

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the zone associated with this case.

This field is available in API version 24.0 and later.

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
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the contact. The Case.ContactEmail field displays the Email field on the
contact on page 1366 that is referenced by Case.ContactId. Label is `Contact Email` . This
field is available in API version 38.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the contact. Label is `Contact Fax` . This field is available in API version
38.0 and later.


Standard Objects Case

**Field** **Details**

```
ContactId

ContactMobile

ContactPhone

CreatorFullPhotoUrl

CreatorName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile telephone number for the contact. Label is `Contact Mobile` . This field is available
in API version 38.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Telephone number for the contact. Label is `Contact Phone` . This field is available in API
version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string


Standard Objects Case

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal users
(agents) appears to portal users in the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

```
CreatorSmallPhotoUrl

Description

FeedItemId

HasCommentsUnreadByOwner

HasSelfServiceComments

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text description of the case. Limit: 32 KB.

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the question in Chatter associated with the case. This field is available in API version
33.0 and later, and is only accessible in organizations where Question-to-Case is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case contains comments that the case owner hasn’t read ( `true` ) or not
( `false` ).

**Type**
boolean


Standard Objects Case

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case has comments added by a Self-Service user ( `true` ) or not ( `false` ).
Only visible when Customer Portal is enabled.

```
IsClosed

IsClosedOnCreate

IsDeleted

IsEscalated

IsSelfServiceClosed

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed ( `true` ) or open ( `false` ). This field is controlled by the
`Status` field; it can't be set directly. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case was closed at the same time that it was created ( `true` ) or not
( `false` ). This flag is read-only and is automatically set when a record is created. It can't be
set to `true` unless the `IsClosed` flag is also `true` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the case has been escalated ( `true` ) or not. A case's escalated state does
not affect how you can use a case, or whether you can query, delete, or update it. You can
set this flag via the API. Label is `Escalated` .

**Type**
boolean


Standard Objects Case

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed for Self-Service users ( `true` ) or not ( `false` ).

```
IsStopped

IsVisibleInSelfService

Language

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an entitlement process on a case is stopped ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case can be viewed in the Customer Service Portal, Partner Service
Portal, and Self-Service Portal ( `true` ) or not ( `false` ). This field is applied for case visibility
in the Partner Relationship Management, Customer Service Portal, and the earlier version of
Self Service Portal. The field does not alter sharing and will not prevent usage of a direct URL
to a case if a portal user has read or write access.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case. The Language field is available when you enable Einstein Case
Classification in Enterprise, Performance, and Unlimited edition orgs with Service Cloud. By
default, only Einstein classification apps use this field.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime


Standard Objects Case

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
MasterRecordId

Origin

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this object was deleted for any other reason, or has not been deleted, the value
is `null` .

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable,Sort, Update

**Description**
The source of the case, such as `Email`, `Phone`, or `Web` . Label is `Case Origin` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the case.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects Case

**Field** **Details**

**Refers To**
Group, User

```
ParentId

Priority

QuestionId

Reason

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent case in the hierarchy. The label is `Parent Case` .

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The importance or urgency of the case, such as `High`, `Medium`, or `Low` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The question in the answers zone that is associated with the case. This field does not appear
if you don't have an answers zone enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the case was created, such as `Instructions not clear`, or `User`
`didn’t attend training` .


Standard Objects Case

**Field** **Details**

```
RecordTypeId

ServiceContractId

SlaStartDate

SourceId

Status

StopStartDate

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid ID.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Shows the time that the case entered an entitlement process. If you have the Edit permission
on cases, you can update or reset the time.

This field is available in API version 18.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the social post source.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the case, such as New, Closed, or Escalated. This field directly controls the
`IsClosed` flag. Each predefined `Status` value implies an `IsClosed` flag value. For
more information, see CaseStatus.

**Type**
dateTime


Standard Objects Case

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time an entitlement process was stopped on the case.

This field is available in API version 18.0 and later.

```
Subject

SuppliedCompany

SuppliedEmail

SuppliedName

SuppliedPhone

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the case. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company name that was entered when the case was created. Label is `Company` .

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address that was entered when the case was created. Label is `Email` .

If your organization has an active auto-response rule, `SuppliedEmail` is required when
creating a case via the API. Auto-response rules use the email in the contact specified by
`ContactId` . If no email address is in the contact record, the email specified here is used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name that was entered when the case was created. Label is `Name` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Case

**Field** **Details**

**Description**
The phone number that was entered when the case was created. Label is `Phone` .

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of case, such as `Feature Request` or `Question` .

Note: If you are importing Case data and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Audit fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

Use the Case object to manage cases for your organization. Client applications can query, update, and delete Attachment records
associated with a case via the API.

Assignment Rules

When you query or update a case, your client application can have the case automatically assigned to one or more User records based
on assignment rules that have been configured in the user interface. To use this feature, your client application must set either of the
following options (but not both) in the AssignmentRuleHeader used in the create or update:

**Field** **Field Type** **Details**

`assignmentRuleId` reference ID of the assignment rule to use. Can be an inactive assignment
rule. If unspecified and `useDefaultRule` is `true`, then the

default assignment rule is used. To find the ID for a given
assignment rule, query the AssignmentRule object (specifying
`RuleType="caseAssignment"` ), iterate through the
returned AssignmentRule objects, find the one you want to use,
retrieve its ID, and then specify its ID in this field in the
AssignmentRuleHeader.

`useDefaultRule` boolean

Specifies whether to use the default rule for rule-based assignment
( `true` ) or not ( `false` ). The default rule is assigned by users in
the Salesforce user interface.

For a code example that shows setting the AssignmentRuleHeader for a Lead (which is similar to setting the AssignmentRuleHeader for
a Case), see Lead.


### Standard Objects CaseArticle

Separating Accounts from Contacts in Cases

In releases before 8.0, the `AccountId` could not be specified, it was derived from the contact’s account. This behavior will continue
to be supported in future releases, but you can also now specify an `AccountId` . If you do not specify the `AccountId` during the
creation of a case, the value will default to the contact’s `AccountId` .

Note: When a record is updated, if the `ContactId` has not changed, then the `AccountId` is not regenerated. This prevents
the API from overwriting a value previously changed in the Salesforce user interface. However, if an API call changes the ContactId
and the `AccountId` field is empty, then the `AccountId` is generated using the contact’s account.

Using **`_case`** with Java

### Depending on the development tool you use, you might need to write your application using _case instead of Case, because case

is a reserved word in Java.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseChangeEvent (API version 44.0)**
Change events are available for the object.

**CaseFeed (API version 18.0)**
Feed tracking is available for the object.

**CaseHistory**

History is available for tracked fields of the object.

**CaseOwnerSharingRule**

Sharing rules are available for the object.

**CaseShare**

Sharing is available for the object.

SEE ALSO:

Account

CaseMilestone

### CaseArticle

Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects CaseArticle

Special Access Rules

Access to this object is controlled by the parent Case and KnowledgeArticle. However, when querying, access is only controlled by the
parent Case.

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ArticleLanguage

ArticleVersionNumber

CaseId

IsSharedByEmail

KnowledgeArticleId

```

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
The language of the article associated with the case.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with the KnowledgeArticle.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
Indicates that the article has been shared with the customer through an email.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CaseComment

**Field** **Details**

**Description**
ID of the KnowledgeArticle associated with the Case.

Usage

This object represents the association of a knowledge article with a Case. An article is associated with a case when it’s relevant to a
specific issue, when it helps an agent solve the case, or when the agent sends the article to a customer.

You can use this object to include case-article associations in Apex and Visualforce.

You can't update this object via the API. If you attempt to create a record that matches an existing record, the create request simply
returns the existing record.

SEE ALSO:

### Case

KnowledgeArticle

### CaseComment

Represents a comment that provides additional information about the associated Case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommentBody

ConnectionReceivedId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is
**Body** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CaseComment

**Field** **Details**

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

```
ConnectionSentId

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

IsDeleted

```

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal users
(agents) appears to portal users in the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

**Type**
boolean


Standard Objects CaseComment

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
IsNotificationSelected

IsPublished

ParentId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Update

**Description**
Indicates whether an email notification is sent to the case contact when a CaseComment is
created or updated. When this field is queried, it always returns null.

This field is available only when the `Enable Case Comment Notification to`
`Contacts` setting is enabled on the Support Settings page in Setup. To send email
notifications for CaseComment, you must use the `EmailHeader triggerUserEmail` .

Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the CaseComment is visible to customers in the Self-Service portal ( `true` )
or not ( `false` ). Label is **Published** . This is the only CaseComment field that can be updated
via the API.

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
Required. ID of the parent Case of the CaseComment.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case


### Standard Objects CaseContactRole

Note: If you're importing CaseComment data and must set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Record id's can't delete CaseComments entities when calling the Database.delete() Apex method or its analogous SOAP API. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

In the Salesforce user interface, comments are entered by a User working on a Case. All users have access to create and view CaseComment
in the Salesforce user interface and when using the API. In the API, CaseComment records can't be modified after insertion unless the
user has the “Modify All Records” object-level permission for Cases or the “Modify All Data” permission. If not, users can only update the
`IsPublished` field, and can't delete CaseComment.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseContactRole

Represents the role that a given Contact plays on a Case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CasesId

ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cases associated with this contact.

This is a relationship field.

**Relationship Name**
Cases

**Relationship Type**
Lookup

**Refers To**
### Case

**Type**
reference


### Standard Objects CaseHistory

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

```
 IsDeleted

 Role

```

Usage

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the contact on this case, such as Technical Contact, Business
Contact, Decision Maker, and so on. Must be unique—there can't be multiple records in
which the `CaseId`, `ContactId`, and `Role` values are identical. Different contacts can
play the same role on the same case. A contact can play different roles on the same case.

Use this object to define the role that a given Case plays on a given Contact. For example, you can use this object to be able to see all
contacts who are associated to a case, or, given a contact, be able to query all cases that they are associated with, even if they are not
the primary contact on the case.

### CaseHistory

Represents historical information about changes that have been made to the associated Case.


Standard Objects CaseHistory

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

DataType

Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

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
Name of the case field that was modified, or a special value to indicate some other
modification to the case. The possible values, in addition to the case field names, are:

**•** **ownerAssignment** —The owner of the case was changed.

**•** **ownerAccepted** —A user took ownership of a case from a queue.


### Standard Objects CaseHistory2

**Field** **Details**

**•** **ownerEscalated** —The owner of the case was changed due to case escalation.

**•** **external** —A user made the case visible to customers in the Customer Self-Service Portal.

```
 IsDeleted

 NewValue

 OldValue

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified case field. Maximum of 255 characters.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified case field. Maximum of 255 characters.

Case history entries are indirectly created each time a case is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseHistory2

Represents historical information about owner and status changes that have been made to the associated Case. This object is available
in API version 59.0 and later.


Standard Objects CaseHistory2

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

IsDeleted

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the contact who owns the case.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


### Standard Objects CaseMilestone

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PreviousUpdate

Status

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was last updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the case, such as `New`, `Closed`, or `Escalated` .

CaseHistory2 entries are intended for case history reports.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseHistory2ChangeEvent on page 68**
Change events are available for the object in API version 60.0 or later.

### CaseMilestone

Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects CaseMilestone

Fields

**Field** **Details**

```
BusinessHoursId

CaseId

CompletionDate

ElapsedTimeInDays

ElapsedTimeInHrs

ElapsedTimeInMins

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the BusinessHours associated with the CaseMilestone.

**Type**
reference

**Properties**
Filter

**Description**
ID of the case.

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone was completed.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in days.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in hours.

**Type**
int

**Properties**
Filter, Nillable


Standard Objects CaseMilestone

**Field** **Details**

**Description**
The time required to complete a milestone in minutes.

```
IsCompleted

IsViolated

MilestoneTypeId

StartDate

TargetDate

TargetResponseInDays

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is completed ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is violated ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The ID of the milestone on the case.

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone started on the case.

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time the milestone must be completed.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects CaseMilestone

**Field** **Details**

**Description**
The time to complete the milestone in days.

```
TargetResponseInHrs

TargetResponseInMins

TimeRemainingInDays

TimeRemainingInHrs

TimeRemainingInMins

TimeSinceTargetInDays

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time to complete the milestone in hours.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time to complete the milestone in minutes.

**Type**
double

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target, measured in days.

**Type**
text

**Properties**
Nillable

**Description**
Time remaining to reach the milestone target, measured in hours.

**Type**
text

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target. The format is minutes and seconds.

**Type**
double

**Properties**
Nillable, Sort


### Standard Objects CaseOwnerSharingRule

**Field** **Details**

**Description**
The time elapsed since the milestone target, measured in days.

```
TimeSinceTargetInHrs

TimeSinceTargetInMins

```

Usage

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target, measured in hours.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target. The format is minutes and seconds.

This object lets you view a milestone on a case. It also lets you view if the milestone was completed and when it must be completed.

SEE ALSO:

### Case

MilestoneType

SlaProcess

### CaseOwnerSharingRule

Represents the rules for sharing a case with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal users can’t access this object.


Standard Objects CaseOwnerSharingRule

Fields

**Field** **Details**

```
CaseAccessLevel

Description

DeveloperName

GroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

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

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CaseParticipant

**Field** **Details**

**Description**
The ID representing the source group. Cases owned by users in the source group
trigger the rule to give access.

```
Name

UserOrGroupId

```

Usage

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
The ID representing the target user or group. Target users or groups are given access.

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

### Case

CaseShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### CaseParticipant

Represents a junction between a case, and an account or a contact. This object stores the details of the participant associated with a
case. This participant could be the applicant, co-applicant, a household, or even a business account. This object is available in API version
54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CaseParticipant

Special Access Rules

Fields and values added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

Fields

**Field** **Details**

```
AuthorizationProof

CaseId

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant communicated their consent. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email Consent`

**•** `Joint Ownership`

**•** `Power of Attorney`

**•** `Verbal Consent`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The case associated with the case participant record.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects CaseParticipant

**Field** **Details**

```
LastViewedDate

Name

ParticipantId

PreferredCallTimeFrom

PreferredCallTimeTo

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
possibly the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the case participant record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The participant associated with the case participant record.

This field is a polymorphic relationship field.

**Relationship Name**
Participant

**Relationship Type**
Lookup

**Refers To**
Account, Contact

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
time


Standard Objects CaseParticipant

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

```
PreferredCommunicationMode

Role

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant prefers to receive messages. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email`

**•** `Phone`

**•** `SMS`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the case participant.

Possible values are:

**•** `Applicant`

**•** `Complainant Representative` (Available in API version 58.0 and later.)

**•** `Inspection Officer`

**•** `Lawyer`

**•** `Observer`

**•** `Perpetrator`

**•** `Primary Caretaker`

**•** `Victim`

The default value is `Applicant` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects CaseRelatedIssue

**Field** **Details**

**Description**
The status of the case participant.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `In Review` (Available in API version 58.0 and later.)

**•** `Pending` (Available in API version 58.0 and later.)

**•** `Submitted` (Available in API version 58.0 and later.)

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseParticipantFeed on page 55**
Feed tracking is available for the object.

**CaseParticipantHistory on page 63**
History is available for tracked fields of the object.

### CaseRelatedIssue

This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service failure.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A relationship field that represents the case you're linking a Problem or Incident to.

**Relationship Name**
### Case


Standard Objects CaseRelatedIssue

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Case

```
Name

RelatedEntityType

RelatedIssueId

RelationshipType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A brief description of the related case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows what type of object the related entity is.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how two records relate to each other.


### Standard Objects CaseShare

**Field** **Details**

Possible values are:

**•** `Root Cause`

**•** `Similar`

The default value is 'Root Cause'.

```
UniqueKeyIndex

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
This field is unique within your organization.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseRelatedIssueChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**CaseRelatedIssueFeed on page 55**
Feed tracking is available for the object.

**CaseRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### CaseShare

Represents a sharing entry on a Case.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Case object can access this object.


Standard Objects CaseShare

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
CaseAccessLevel

CaseId

IsDeleted

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Case. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value isn’t valid for creating or deleting records.

This field must be set to an access level that is higher than the organization’s default access
level for cases.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist


Standard Objects CaseShare

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Case with them.

**•** `Owner` —The User is the owner of the Case.

**•** `ImplicitChild` —The User or Group has access to the Case on the Account
associated with this Case. After faster account sharing recalculation is enabled for your
org, sharing entries with this value aren’t returned in queries. Instead of storing implicit
child shares, record access is determined dynamically.

**•** `RelatedPortalUser` —The portal user is the contact on the Case.

**•** `Rule` —The User or Group has access via a Case sharing rule.

**•** `GuestRule` —The User or Group has access via a Case guest user sharing rule.

**•** `Team` —The User or Group has team access.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Case via an account relationship data sharing rule.

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Case. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects CaseSolution

Usage

This object allows you to determine which users and groups can view and edit Case records owned by other users. If you attempt to
create a record that matches an existing record, request updates any modified fields and returns the existing record.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child case records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child case records when they
try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare

LeadShare

OpportunityShare

### CaseSolution

Represents the association between a Case and a Solution.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Case associated with the Solution.

This is a relationship field.

**Relationship Name**
### Case

**Relationship Type**
Lookup

**Refers To**
### Case


### Standard Objects CaseStatus

**Field** **Details**

```
 IsDeleted

 SolutionId

```

Usage

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
Create, Filter, Group, Sort

**Description**
Required. ID of the Solution associated with the case.

This is a relationship field.

**Relationship Name**
Solution

**Relationship Type**
Lookup

**Refers To**
Solution

You can't update this object via the API. If you attempt to create a record that matches an existing record, the request simply returns
the existing record.

SEE ALSO:

CaseShare

SolutionStatus

### CaseStatus

Represents the status of a Case, such as New, On Hold, or In Process.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects CaseStatus

Fields

**Field** **Details**

```
ApiName

IsClosed

IsDefault

MasterLabel

SortOrder

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
Indicates whether this case status value represents a closed Case ( `true` ) or not ( `false` ).
Multiple case status values can represent a closed Case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default case status value ( `true` ) or not ( `false` ) in the picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this case status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the case status picklist. These numbers are not guaranteed
to be sequential, as some previous case status values might have been deleted.


### Standard Objects CaseSubjectParticle

Usage

This object represents a value in the case status picklist. The case status picklist provides additional information about the status of a
Case, such as whether a given `Status` value represents an open or closed case. Query the CaseStatus object to retrieve the set of
values in the case status picklist, and then use that information while processing Case records to determine more information about a
given case. For example, the application could test whether a given case is open or closed based on its `Status` value and the value
of the `IsClosed` property in the associated CaseStatus object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseSubjectParticle

Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts. This object
is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

Index

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for the CaseSubjectParticle object.

This name can contain only underscores and alphanumeric characters, and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This field is automatically generated, but you can
supply your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects CaseSubjectParticle

**Field** **Details**

**Description**
Required. The order in which the custom **Case Subject** is generated, meaning if the social
network is 0 and the social message is 1, then the subject generates as `Twitter |`
`Tweet` .

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case subject field.

Possible values are:

**•** `ar` —Arabic

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `iw` —Hebrew

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

**Description**
Label for the case subject field.


### Standard Objects CaseTag

**Field** **Details**

```
TextField

Type

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies inbound social content added to **Case Subject** in case records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the custom **Case Subject** format from which inbound social content
appears in case records.

Possible values are:

**•** `ColonSeparator`

**•** `Content` —Message

**•** `HyphenSeparator`

**•** `MessageType`

**•** `PipeSeparator`

**•** `ProvidedString`

**•** `RealName`

**•** `Sentiment`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Source`

In the Salesforce UI, case subjects are brief descriptions of cases. They are what agents see on cases first. Social Business Rules specify
the brief descriptions of cases created from social posts. Using CaseSubjectParticle objects you can build your own case subject format,
where each object represents a social post's component. For example, combining CaseSubjectParticle objects with components for
types `MessageType`, `RealName`, and `SocialNetwork` results in "Tweet Customer123 Twitter".

### CaseTag

Associates a word or short phrase with a Case


Standard Objects CaseTag

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

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .


### Standard Objects CaseTeamMember

Usage

CaseTag stores the relationship between its parent TagDefinition and the Case being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### CaseTeamMember

Represents a case team member, who works with a team of other users to help resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

When accessing from Apex code, use the `WITH USER_MODE` clause to enable field-level and object-level security permissions checking
for `SOQL SELECT` [queries, including subqueries and cross-object relationships. See Enforce User Mode for Database Operations.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm)

Fields

**Field** **Details**

```
MemberId

ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a member on a case team.

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
reference


Standard Objects CaseTeamMember

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team member is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

```
TeamRoleId

TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the case team role with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamRole

**Relationship Type**
Lookup

**Refers To**
CaseTeamRole

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the predefined team with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate


### Standard Objects CaseTeamRole

**Field** **Details**

```
TeamTemplateMemberId

### CaseTeamRole

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the team member included in a predefined case team.

This is a relationship field.

**Relationship Name**
TeamTemplateMember

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplateMember

Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for cases. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`


### Standard Objects CaseTeamTemplate

**Field** **Details**

```
Name

PreferencesVisibleInCSP

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the case team role.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether or not the case team role is visible to Customer Portal users.

### CaseTeamTemplate

Represents a predefined case team, which is a group of users that helps resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
Description

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A text description of the predefined case team.

**Type**
string


### Standard Objects CaseTeamTemplateMember

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the predefined case team.

### CaseTeamTemplateMember

Represents a member on a predefined case team, which is a group of users that helps resolve cases.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
MemberId

TeamRoleId

TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a team member on a predefined case team.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the predefined case team member's case team role.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CaseTeamTemplateRecord

**Field** **Details**

**Description**
The ID of the predefined case team's template.

### CaseTeamTemplateRecord

The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined case
team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the `ParentId` to the case and the
`TeamTemplateId` to the predefined case team.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
ParentId

TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
### Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CategoryData

**Field** **Details**

**Description**
The ID of the predefined case team with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate

### CategoryData

Represents a logical grouping of Solution records.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
CategoryNodeId

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the CategoryNode associated with the solution.

**Type**
boolean

**Properties**
Defaulted on create, Filter


### Standard Objects CategoryNode

**Field** **Details**

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
 RelatedSobjectId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the solution related to the category.

This object allows you to assign one or more categories to a Solution. It is an intermediate data table with two foreign keys that defines
the relationship between a CategoryNode and a Solution record.

CategoryData has two foreign keys:

### • The first foreign key, CategoryNodeId, refers to the ID of a CategoryNode.

**•** The other foreign key, `RelatedSobjectId`, refers to a Solution ID.

### This is a many-to-many relationship, so there can be multiple rows returned with a CategoryNodeId . A Solution can be associated

with multiple categories.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CategoryNode

Represents a tree of Solution categories.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

**•** Customer Portal users can't access this object.

**•** Attempting to delete a CategoryNode that has children (referred by CategoryNode.Parent), or is referred to elsewhere, causes a
failure.


Standard Objects CategoryNode

Fields

**Field** **Details**

```
 MasterLabel

ParentId

 SortOrder

 SortStyle

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of this node, if any.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sort order of child CategoryNode objects.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the sort order is alphabetical or custom.

A CategoryNode defines a category of solutions. In the user interface, you can edit category definitions from Setup by entering _`Solution`_
_`Categories`_ in the `Quick Find` box, then selecting **Solution Categories** .

SEE ALSO:

CategoryData

Solution


### Standard Objects CategoryNodeLocalization CategoryNodeLocalization

When the Translation Workbench is enabled for your organization, the CategoryNodeLocalization object provides the translation of the
label of a solution category.

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
CategoryNodeId

LanguageLocaleKey

Language

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the solution CategoryNode that is being translated.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

This picklist contains the following fully-supported languages:


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in
English.

The following end-user only languages are available.

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


Standard Objects CategoryNodeLocalization

**Field** **Details**

The following platform languages are available for organizations that use Salesforce
exclusively as a platform.

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

**•** English (Belgium): `en_BE`

**•** English (Canada): `en_CA`

**•** English (Cyprus): `en_CY`

**•** English (Germany): `en_DE`

**•** English (Hong Kong): `en_HK`


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

**•** Khmer: `km`

**•** Latvian: `lv`

**•** Lithuanian: `lt`


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

**•** Spanish (Uruguay): `es_UY`


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

The values in this field are not related to the default locale selection.

```
NamespacePrefix

Value

```

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

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the solution category. Label is **Translation** .


### Standard Objects ChangeRequest

Usage

Use this object to translate the labels of your solution categories into a supported language. Users with the Translation Workbench
enabled can view category node translations, but either the “Customize Application,” “Manage Translation,” or “Manage Categories”
permission is required to create or update category node translations.

SEE ALSO:

ScontrolLocalization

WebLinkLocalization

### ChangeRequest

Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessJustification

BusinessReason

Category

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the business reason to implement the change. This field can store up to 32
KB of data, but only the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The core reason for creating the change request.

Possible values are:

**•** `t2`

**Type**
picklist


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of change request. Administrators set field values.

```
ChangeRequestNumber

ChangeType

Description

EstimatedEndTime

EstimatedStartTime

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated change request number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of change request. Administrators set field values.

Possible values are:

**•** `Emergency`

**•** `Major`

**•** `Normal`

**•** `Standard`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request. This field can store up to 32 KB of data, but only the
first 255 characters display in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request is estimated to be implemented.

**Type**
dateTime


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated date and time (in UTC) when the change request is implemented.

```
FinalReviewDateTime

FinalReviewNotes

Impact

LastReferencedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request was reviewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes left by the change request reviewer. This field can store up to 32 KB of data, but only
the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows the impact of a requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects ChangeRequest

**Field** **Details**

```
LastViewedDate

OwnerId

Priority

RemediationPlan

```

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
A polymorphic relationship field that represents the user or group assigned as the change
reviewer.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of a requested change.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects ChangeRequest

**Field** **Details**

**Description**
A description of the steps required to resolve the incident. This field can store up to 32 KB
of data, but only the first 255 characters display in reports.

```
ReviewerId

RiskImpactAnalysis

RiskLevel

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who reviewed the change request.

This is a relationship field.

**Relationship Name**
Reviewer

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An assessment of the risk involved with the implementation of the change request.
Administrators set field values, and each value can have up to 20 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The risk level associated with adopting the requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
picklist


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents any custom or granular stages a customer may want to track. This will be a
dependent picklist.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

```
StatusCode

Subject

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the change.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

**Type**
string


### Standard Objects ChangeRequestRelatedIssue

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the requested change.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**ChangeRequestFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestHistory on page 63**
History is available for tracked fields of the object.

**ChangeRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ChangeRequestShare on page 67**
Sharing is available for the object.

### ChangeRequestRelatedIssue

Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available in
API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ChangeRequestId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that's linked to the Problem or Incident.


Standard Objects ChangeRequestRelatedIssue

**Field** **Details**

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

```
Name

RelatedEntityType

RelatedIssueId

RelationshipType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A description of the change request as it relates to the problem or incident.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the related object type.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents the related Problem or Incident.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Description**
Shows how the ChangeRequest and Incident or Problem records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Fixed By`

The default value is 'Caused By'.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedIssueChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedIssueFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### ChangeRequestRelatedItem

Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the ChangeRequest.

This field is a relationship field.

**Relationship Name**
Asset


Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Asset

```
ChangeRequestId

Comment

ImpactLevel

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that’s linked to the Asset.

This field is a relationship field.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item's impact on the change request.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High` .

**Type**
string


### Standard Objects ChangeSetOperationEventLog

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the item that's related to the change request.

```
RelationshipType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Asset records relate to each other.

Possible values are:

**•** `Broke Item`

**•** `Fixed Item`

The default value is `Broke Item` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedItemChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedItemFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedItemHistory on page 63**
History is available for tracked fields of the object.

### ChangeSetOperationEventLog

Change Set Operation events contain information from change set migrations. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects ChangeSetOperationEventLog

Fields

**Field** **Details**

```
ChangeSetName

ClientIp

CpuTime

LoginKey

OperationType

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the change set.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

**Type**
string


Standard Objects ChangeSetOperationEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
RunTime

SessionKey

TargetOrganizationIdentifier

Timestamp

Uri

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the organization that’s receiving the change set.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URI of the page receiving the request.


### Standard Objects ChannelObjectLinkingRule

**Field** **Details**

```
UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### ChannelObjectLinkingRule

Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version 47.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionForNoRecordFound

ActionForSingleRecordFound

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when no matching records are found.

Possible values are:

**•** `CreateNewRecordAndLink` —Create Record and Link (Recommended)

**•** `PromptAgent` —Prompt Agent

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when one matching record is found.

Possible values are:

**•** `AutoLink` —Auto-Link Record (Recommended)


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**•** `PromptAgent` —Prompt Agent

```
ChannelType

Description

DeveloperName

IsLinkedRecordOpenedAsSubTab

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of channel used for this rule.

Possible values are:

**•** `FacebookMessenger`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WhatsApp`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description for this linking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to open the linked record as a subtab when the link is established.

```
IsRuleActive

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this linking rule.

Possible values are:

**•** `ar` —Arabic

**•** `bg` —Bulgarian

**•** `cs` —Czech

**•** `da` —Danish

**•** `de` —German

**•** `el` —Greek

**•** `en_GB` —English (UK)

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `in` —Indonesian

**•** `it` —Italian

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**•** `no` —Norwegian

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `ro` —Romanian

**•** `ru` —Russian

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sv` —Swedish

**•** `th` —Thai

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `vi` —Vietnamese

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

ObjectToLink

RuleName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique label name for this rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of object to link to the channel interaction.

Possible values are:

**•** `Contact`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the rule as it appears in the UI. Maximum length is 80 characters.


### Standard Objects ChannelProgram ChannelProgram

Represents a channel program that vendors use to market and sell their products through channel partners. This object is available in
API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Description

IsActive

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Category of the channel program. Categories group channel programs by type.
For example, a reseller category would include all the different regional reseller
channel programs.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel program is active. New channel programs are
inactive by default.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ChannelProgram

**Field Name** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

```
LastViewedDate

Name

OwnerId

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the channel program.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the channel program.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramFeed**

Feed tracking is available for the object.

**ChannelProgramHistory**

History is available for tracked fields of the object.

**ChannelProgramOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramShare**

Sharing is available for the object.


### Standard Objects ChannelProgramLevel ChannelProgramLevel

Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program level.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the channel program level.


Standard Objects ChannelProgramLevel

**Field Name** **Details**

```
OwnerId

ProgramId

Rank

RecordTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An integer associated with the level. For example, 1 represents the lowest level,
2 the next level up, etc.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramLevelFeed**

Feed tracking is available for the object.

**ChannelProgramLevelHistory**

History is available for tracked fields of the object.

**ChannelProgramLevelOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramLevelShare (API version 43.0)**
Sharing is available for the object.


### Standard Objects ChannelProgramMember ChannelProgramMember

Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

LevelId

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced. This field is available in API version 45.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed. This field is available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel program level.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the channel program member.

**Type**
reference


### Standard Objects ChatterActivity

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

```
PartnerId

ProgramId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramMemberFeed (API version 46.0)**
Feed tracking is available for the object.

**ChannelProgramMemberHistory (API version 46.0)**
History is available for tracked fields of the object.

**ChannelProgramMemberOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramMemberShare (API version 43.0)**
Sharing is available for the object.

### ChatterActivity ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts and

comments received by the same user. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ChatterActivity

Fields

**Field Name** **Details**

```
CommentCount

CommentReceivedCount

InfluenceRawRank

LikeReceivedCount

NetworkId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments made by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments received by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number indicating the ParentId’s Chatter influence rank, which is calculated based
on the ParentId’s ChatterActivity statistics, relative to the other users in the
organization. This field is available in API version 26.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedLikes received by the ParentId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site to which the ChatterActivity belongs. This field is
available only if digital experiences is enabled in your org. This field is available in API
version 26.0 and later.


### Standard Objects ChatterAnswersActivity

**Field Name** **Details**

```
ParentId

PostCount

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object type to which the ChatterActivity is related. In API version 66.0, the
`ParentId` must be a `UserId` or SelfServiceUser ID.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedItems made by the ParentId.

**•** Use this object to reference the Chatter activity statistics, which include the number of posts and comments made by a user and
the number of comments and likes on posts and comments received by the same user.

**•** You can directly query for ChatterActivity.

```
  SELECT Id, PostCount, LikeReceivedCount

  FROM ChatterActivity

  WHERE ParentId = UserId

```

Note: To query ChatterActivity, you must provide the `ParentId` . In API version 66.0, the `ParentId` must be a `UserId`
or SelfServiceUser ID.

**•** A ChatterActivity record is created for users the first time they post or comment. Users who have never posted or commented don’t
have ChatterActivity records. If users make only one post and then delete it, they do have ChatterActivity records. In both cases, the
user interface displays zeros for their Chatter activity.

**•** Use the `InfluenceRawRank` field to reference a user’s Chatter influence rank. This field is available in API version 26.0 and later.

SEE ALSO:

FeedItem

FeedComment

FeedLike

### ChatterAnswersActivity

Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.


Standard Objects ChatterAnswersActivity

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
BestAnswerReceivedCount

BestAnswerSelectedCount

QuestionsCount

QuestionSubscrCount

QuestionSubscrReceivedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of best answers the User has received from other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of best answers the User has selected.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records the User has selected to follow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users following Question records posted by the User.


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

```
QuestionUpVotesCount

QuestionUpVotesReceivedCount

RepliesCount

ReplyDownVotesCount

ReplyDownVotesReceivedCount

ReplyUpVotesCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes the User has marked on Question records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Question
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Reply records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has marked on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has marked on the Reply records posted by
other users.

```
ReplyUpVotesReceivedCount

ReportAbuseOnQuestionsCount

ReportAbuseOnRepliesCount

ReportAbuseReceivedOnQnCount

ReportAbuseReceivedOnReCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Question records posted
by other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses reported by other users on the Question records posted
by the User.

**Type**
int


### Standard Objects ChatterAnswersReputationLevel

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

the number of abuses reported by other users on the Reply records posted by
the User.

```
UserId

CommunityId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The User ID associated with this reputation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID for the zone associated with this reputation.

Use this object to view metrics on User activity in Chatter Answers. For example, you can use the ChatterAnswersActivity object to view
the number of Question records a user is following in Chatter Answers zones.

SEE ALSO:

Question

Reply

User

### ChatterAnswersReputationLevel

Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`


### Standard Objects ChatterConversation

Fields

**Field** **Details**

```
CommunityID

Name

Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the zone for which you’re creating the reputation level.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level.

Use to create or edit reputation levels for the zone.

### ChatterConversation

Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object is
available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects ChatterConversationMember

Fields

**Field Name** **Details**

```
Id

```

Usage

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the conversation.

Use this object to identify private conversations in Chatter. Users can access this object if they have the Manage Chatter Messages and
Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users' Chatter
messages; for example, for compliance purposes.

SEE ALSO:

### ChatterConversationMember

ChatterMessage

### ChatterConversationMember

Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other
conversation participants. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ConversationId

MemberId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated ChatterConversation.

**Type**
reference


### Standard Objects ChatterExtension

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation member.

Usage

Use this object to view members of private conversations in Chatter. Users can access this object if they have the Manage Chatter
Messages and Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users'
Chatter messages; for example, for compliance purposes.

SEE ALSO:

ChatterConversation

ChatterMessage

### ChatterExtension

Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CompositionComponentEnumOrId

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ID of the composition component for the Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of your custom Rich Publisher App. This field requires a value.


Standard Objects ChatterExtension

**Field** **Details**

```
DeveloperName

ExtensionName

HeaderText

HoverText

IconId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the developer who is responsible for the app.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of your extension. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show in the header of your app composer. Header text is required for Lightning
type extensions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show when a user mouses over your extension’s icon. Mouse-over text is required
for Lightning type extensions.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The icon to show in the Chatter publisher. Use an existing file asset ID from your org. This
field requires a value.

This is a relationship field.


Standard Objects ChatterExtension

**Field** **Details**

**Relationship Name**
Icon

**Relationship Type**
Lookup

**Refers To**
ContentAsset

```
IsProtected

Language

MasterLabel

NamespacePrefix

RenderComponentEnumOrId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
An auto-generated value. It currently has no impact.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for this instance of the `ChatterExtension` . This field requires a
value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the `ChatterExtension` object. This field requires a value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prefix to use for the extension’s namespace.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ChatterExtensionConfig

**Field** **Details**

**Description**
The rendering component of the Rich Publisher App that you provide. It’s comprised of the
`lightning:availableForChatterExtensionRenderer` interface. This field
requires a value.

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of the extension. Currently, the only value supported is _`Lightning`_ .
Included to allow for other possible types in the future.

### ChatterExtensionConfig

Configuration for the Chatter extension for Experience Cloud sites. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CanCreate

CanRead

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can create an instance that appears by

rendering.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can be viewed.


### Standard Objects ChatterMessage

**Field** **Details**

```
ChatterExtensionId

NetworkId

Position

### ChatterMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the `ChatterExtension` .

This is a relationship field.

**Relationship Name**
ChatterExtension

**Relationship Type**
Lookup

**Refers To**
ChatterExtension

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site where the `ChatterExtension` is deployed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The position of the `ChatterExtension` icon in the Chatter publisher.

Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects ChatterMessage

Fields

**Field Name** **Details**

```
Body

ConversationId

SenderId

SenderNetworkId

SentDate

```

**Type**
textarea

**Properties**
Update

**Description**
Text of the message.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation that the message is associated with.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the sender.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site from which the message was sent. This field is
available only if digital experiences is enabled in your org.

This field is available in API version 32.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the message was sent.


### Standard Objects ClientBrowser

Usage

Use this object to view and delete messages sent or received via private conversations in Chatter. Users can access this object if they
have the Manage Chatter Messages and Direct Messages permission. Users with the Moderate Experiences Chatter Messages permission
can access this object in Experience Cloud sites they’re a member of, only if the message has been flagged as inappropriate. This object
is provided to allow administrators to view and delete users’ Chatter messages, for example, for compliance purposes.

Messages are hard deleted. That is, they’re removed completely without a trip to the Recycle Bin.

Deleting a message that resulted from sharing a file with someone doesn’t also delete the file.

SEE ALSO:

ChatterConversation

ChatterConversationMember

### ClientBrowser

Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie
was inserted. This object is available in version 28.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
FullUserAgent

LastUpdate

ProxyInfo

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Detailed information about the client (browser). For example, `Mozilla/5.0`

```
  (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1)

  Gecko/2008070208 Firefox/3.0.1

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the last time the cookie was changed.

**Type**
string


### Standard Objects CollaborationGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The browser’s current proxy information.

```
UsersId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

At every login, the device the login request is from is checked against the known devices using ClientBrowser. A match means a cookie
was found on the browser that matches an entry in the ClientBrowser table, so the device is known. No match means that no matching
cookie was found, so the device is unknown, and the user is asked to confirm their identity.

### CollaborationGroup

Represents a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`,

```
upsert()

```

Special Access Rules

The visibility of information in groups depends on the type of group and the user’s permissions.

**•** **Members** : Any user with the Create and Own New Chatter Groups permission can create public, private, and unlisted groups,
including in any Experience Cloud sites they belong to.

**•** **Owners and managers** : Users can modify group details for any group they own or manage. Owners can also delete groups they
own.


Standard Objects CollaborationGroup

**•** **Nonmembers** : These user permissions allow group access regardless of group membership.

**–** View All Data—Allows users to view all public and private groups across their org and its Experience Cloud sites. Users with this
permission can’t view unlisted group information, unless they have the Modify Unlisted Groups permission as well.

**–** Modify All Data—Allows users to view, modify, and delete all public and private groups across their org and its Experience Cloud
sites. Users with this permission can’t view or modify unlisted group information, unless they have the Manage Unlisted Groups
permission as well.

**–** Create and Set Up Experiences—Allows users to view, modify, and delete all public and private groups in Experience Cloud sites.

**–** Manage Unlisted Groups—Allows users to search for, access, and modify any unlisted group in an org and its Experience Cloud
sites.

**–** Data Export—Allows users to export any data from Salesforce, including private and unlisted group data from an org and its
Experience Cloud sites.

**•** **Apex and Visualforce** : Apex code runs in system mode, which means that the permissions of the current user aren’t taken into
account.

**–** Visualforce pages that display groups might expose unlisted or private group data to users who aren’t members.

**–** Because system mode disregards the user’s permissions, all users who are accessing a Visualforce page that’s showing a group
can act as an owner of that group.

**–** AppExchange apps that are written in Apex and that access all groups will expose unlisted groups to users who aren’t members.

To limit and manage access to the unlisted and private groups in your org:

**•** Explicitly filter out unlisted and private group information from SOQL queries in all Apex code.

**•** Use permission sets, profile-level permissions, and sharing checks in your code to further limit group access.

**•** Use Apex triggers on the CollaborationGroup object to monitor and manage the creation of groups. In Setup, enter _`Group`_
_`Triggers`_ in the `Quick Find` box, then select **Group Triggers** to add triggers.

Fields

**Field** **Details**

```
AnnouncementId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the ID of the Announcement last associated with the group. This field is available
in API version 30.0 and later.

This is a relationship field.

**Relationship Name**
Announcement

**Relationship Type**
Lookup

**Refers To**
Announcement


Standard Objects CollaborationGroup

**Field** **Details**

```
BannerPhotoUrl

CanHaveGuests

CollaborationType

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's banner photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, indicates that a group allows customers. Chatter customers are people outside
your company's email domains. Customers can see only the groups they're invited to. They
can interact only with members of those groups. Customers can’t see any Salesforce
information.

This field is available starting in API version 23.0, but groups that allow customers are
accessible from earlier API versions. However, when accessed from earlier API versions, groups
that allow customers aren't distinguishable from private groups. We strongly recommend
that you upgrade to the latest API version. If you must use an earlier version, name groups
that allow customers to indicate that they include customers.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of Chatter group. Available values are:

**•** `Public` —Anyone can see and post updates. Anyone can join a public group.

**•** `Private` —Only members can see the group feed and post updates. Non-members
can only see the group name and a few other details in list views, search, and on the
group page. The group's owner or managers must add members who request to join
the group.

**•** `Unlisted` —Only members and users with the Manage Unlisted Groups permission
can see the group and post updates. Other users can’t access the group or see it in lists,
search, and feeds.


Standard Objects CollaborationGroup

**Field** **Details**

```
Description

FullPhotoUrl

GroupEmail

HasPrivateFieldsAccess

InformationBody

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the group.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
email

**Properties**
Nillable, Sort

**Description**
The email address for posting to the group. For private groups, only visible to members and
users with Modify All Data or View All Data permissions.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If set to `true`, indicates that a user can see the `InformationBody` and
`InformationTitle` fields in a private group. This field is set to `true` for members of
a private group and users with Modify All Data or View All Data permissions.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
The text of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

```
InformationTitle

IsArchived

IsAutoArchiveDisabled

IsBroadcast

LastFeedModifiedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is archived ( `true` ) or not ( `false` ).

This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether automatic archiving is disabled for the group ( `true` ) or not ( `false` ).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is a broadcast group ( `true` ) or not ( `false` ).

This field is available in API version 36.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
The date of the last post or comment on the group.

```
LastReferencedDate

LastViewedDate

MediumPhotoUrl

MemberCount

Name

NetworkId

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
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the larger, cropped photo size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of members in the group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the group. Group names must be unique across public and private groups. Unlisted
groups don’t require unique names.

**Type**
reference


Standard Objects CollaborationGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can only add a `NetworkId` when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 26.0 and later.

```
OwnerId

SmallPhotoUrl

```

Usage

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the group. Only the current group owner or people with the Modify All
Data permission can update the `OwnerId` .

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

Use this object to create, edit, or delete groups in an org or Experience Cloud site. Deleting a group permanently deletes all posts and
comments to the group. It also deletes all files and links posted to the group and removes the files from other locations where they were
shared.

As a Chatter group member, you can post to the group using the CollaborationGroupFeed object. As a Chatter group owner or manager,
you can add or remove group members using the CollaborationGroupMember object, post announcements to the group using the


### Standard Objects CollaborationGroupMember

Announcement object, and accept or decline requests to join private groups using the CollaborationGroupMemberRequest object.
Additionally, the group owner, manager, or your Salesforce system administrator can invite people to join the group using the
CollaborationInvitation object.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CollaborationGroupFeed**

Feed tracking is available for the object.

SEE ALSO:

### CollaborationGroupMember CollaborationGroupMemberRequest CollaborationGroupMember

Represents a member of a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated CollaborationGroup.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
### CollaborationGroup


Standard Objects CollaborationGroupMember

**Field** **Details**

```
CollaborationRole

LastFeedAccessDate

MemberId

NotificationFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The role of a group member. Group owners and managers can change roles for members
of their groups. The valid values are:

**•** `Standard` —Indicates that a user is a group member. Members can post and comment
in the group.

**•** `Admin` —Indicates that a user is a group manager. Managers can post and comment,
change member roles, edit group settings, add and remove members, delete posts and
comments, and edit the group information field.

Note: To change the group owner, use the `OwnerId` field on the
CollaborationGroup object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when a group member last accessed the group’s feed. The value is only
updated when a member explicitly consumes the group’s feed, not when the member sees
group posts in other feeds, like the profile feed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group member.

This is a relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


### Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The frequency at which Salesforce sends Chatter group email digests to this
member. Can only be set by the member or users with the “Modify All Data” permission.
The valid values are:

**•** `D` —Daily

**•** `W` —Weekly

**•** `N` —Never

**•** `P` —On every post

The default value is specified by the member in their Chatter email settings. In communities,
the `Email on every post` option is disabled once more than 10,000 members
choose this setting for the group. All members who had this option selected are automatically
switched to `Daily digests` .

Usage

Use this object to view, create, and delete Chatter group members. You must be a group owner or manager to create members for
private Chatter groups.

SEE ALSO:

### CollaborationGroup CollaborationGroupMemberRequest CollaborationGroupMemberRequest

Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**Description**
ID of the private Chatter group.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

```
RequesterId

ResponseMessage

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user requesting to join the group; must be the ID of the context user.

This is a relationship field.

**Relationship Name**
Requester

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Optional message to be included in the notification email when `Status` is `Declined` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the request. Available values are:

**•** `Accepted`

**•** `Declined`

**•** `Pending`


### Standard Objects CollaborationGroupRecord

Usage

This object represents a request to join a private Chatter group, and can be used to accept or decline requests to join private groups you
own or manage. On create, an email is sent to the owner and managers of the private group to be accepted or declined. When the
`Status` is `Accepted` or `Declined`, an email is sent to notify the requester. When the `Status` is `Declined`, a
`ResponseMessage` is optionally included to provide additional details.

Note the following when working with requests:

**•** Users with the “Modify All Data” or “View All Data” permission can view records for all groups, regardless of membership.

**•** A user can be a member of 300 groups. Requests to join groups count against this limit.

**•** `Status` can't be specified on create.

**•** You can only update a request when the `Status` is `Pending` .

**•** You can't delete or update a request with a `Status` of `Accepted` or `Declined` .

SEE ALSO:

### CollaborationGroup

CollaborationGroupMember

### CollaborationGroupRecord

Represents the records associated with Chatter groups.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Chatter group.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup


### Standard Objects CollaborationInvitation

**Field** **Details**

**Refers To**
CollaborationGroup

```
NetworkId

RecordId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. The ID of the Experience Cloud site that the group belongs to. Available from API
version 34.0.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the record associated with the Chatter group.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, Contract, Lead, Opportunity

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollaborationGroupRecordChangeEvent (API version 62.0)**
Change events are available for the object.

### CollaborationInvitation

Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects CollaborationInvitation

Special Access Rules

Invitations are available if “Allow Invitations” is enabled for your organization.

Invitations are limited to your allowed domain(s) unless the invite is sent from a private group that allows customers. Allowed domains
are set by the administrator.

Invitations to customers are available if “Allow Customer Invitations” is enabled for your organization. Users must have the “Invite
Customers to Chatter” permission to send invitations to people outside their Chatter domain.

Fields

**Field** **Details**

```
InvitedUserEmail

InvitedUserEmailNormalized

InviterId

OptionalMessage

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The email address for the user invited to join Chatter. Label is `Invited Email` .

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
A normalized version of the `InvitedUserEmail` entered. Label is `Invited Email`
`(Normalized)` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The person that initiated the invitation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
An optional message from the person sending the invitation to the person receiving it.

**Type**
reference


Standard Objects CollaborationInvitation

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used when the email address on the invitation is different than the one entered when the
invitee accepts the invitation.

```
SharedEntityId

Status

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group associated with this invitation.

**•** If the invitation is to join Chatter, the `SharedEntityId` is the ID of the User that
created the invitation. The invitee will auto-follow the inviter.

**•** If the invitation is to join a group within Chatter, the `SharedEntityId` is the ID of
the Chatter CollaborationGroup.

**•** To invite a customer, set `SharedEntityId` to the ID of the private
CollaborationGroup with Allow Customers turned on.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the invitation. Possible values are:

**•** `Sent`

**•** `Accepted`

**•** `Canceled`

Use this object to create or delete (cancel) invitations to join Chatter. You can either invite a user to join Chatter directly or as part of a
CollaborationGroup.

Note: To invite someone to join a CollaborationGroup, you must be either the owner or a manager of the group or a Salesforce
system administrator.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

When the person accepts your CollaborationGroup invitation, they join the CollaborationGroup and Chatter as well.

Note: You can't send invitations to users of the organization the invite was sent from.

Invited users can view profiles, post on their feed, and join groups, but they can't see your Salesforce data or records.


### Standard Objects CollaborationRoom

If your organization allows groups with customers, owners and managers of private groups with the “Allow Customers” setting, as well
as system administrators, can use this object to invite customers.

Java Samples

The following example shows how to send an invitation to join Chatter:

```
   public void invitePeople(String inviterUserId, String invitedEmail) throws Exception {

      CollaborationInvitation invitation = new CollaborationInvitation();

      invitation.setSharedEntityId(inviterUserId);//pass the userId of the inviter

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

The following example shows how to send an invitation to a customer user from a group that allows customers:

```
   public void inviteToGroup(String GroupName, String invitedEmail) throws Exception {

      QueryResult qr = query("select id from collaborationgroup where name = '" +

        GroupName); //pass the group name

      String groupId = qr.getRecords()[0].getId();

      CollaborationInvitation invitation = new CollaborationInvitation();

      invitation.setSharedEntityId(groupId);//pass the groupId

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

Apex Samples

```
   String emailAddress = 'bob@external.com';

   CollaborationGroup chatterGroup = [SELECT Id

       FROM CollaborationGroup

       WHERE Name='All acme.com'

       LIMIT 1];

   CollaborationInvitation inv = New CollaborationInvitation();

   inv.SharedEntityId = chatterGroup.id;

   inv.InvitedUserEmail = emailAddress;

   try {

     Insert inv;

   } catch(DMLException e){

     System.debug('There was an error with the invite: '+e);

   }

### CollaborationRoom

```

Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as swarming
or reporting. This object is available in API version 55.0 and later.


Standard Objects CollaborationRoom

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable the Slack Terms of Service and one of:

**•** Sales Cloud for Slack App

**•** Service Cloud for Slack App

**•** CRM Analytics for Slack App

**•** Industries Cloud for Slack App

**•** Health Cloud for Slack App

Fields

**Field** **Details**

```
IsArchived

IsAutoJoin

IsExternal

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the collaboration room is archived ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether new users automatically join the collaboration room. Used for Sales Cloud
for Slack App.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether external users are members of the Slack channel ( `true` ) or not ( `false` ).

The default value is `false` .


Standard Objects CollaborationRoom

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

PlatformKey

TeamKey

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of collaboration room.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack workspace.


### Standard Objects CollabDocumentMetric CollabDocumentMetric

Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Document

Site

SourceTemplate

DocumentTitle

MetricDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site in which the thread is located.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template (if any) on which a Quip thread is based.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the thread.

**Type**
dateTime


Standard Objects CollabDocumentMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

```
MetricDateOnly

LastUpdatedDate

LastUpdatedDateOnly

ViewerCount

UpdateCount

```

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of thread views by user for the specified MetricDate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits made on the thread on a given day.


### Standard Objects CollabDocumentMetricRecord

**Field** **Details**

```
EditorCount

CommenterCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who edited the Quip thread.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who commented on the Quip thread.

### CollabDocumentMetricRecord

Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric. CollabDocumentMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollabTemplateMetric

**Field** **Details**

**Description**
The ID of the CollabDocumentMetric record.

```
MetricDate

MetricDateOnly

EntityType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabTemplateMetric

Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Template

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects CollabTemplateMetric

**Field** **Details**

**Description**
The ID of the template.

```
TemplateTitle

Site

MetricDate

MetricDateOnly

LastUpdatedDate

LastUpdatedDateOnly

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site on which the template is available.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort


### Standard Objects CollabTemplateMetricRecord

**Field** **Details**

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

```
TotalDocumentCount

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of documents created based on the template.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollabTemplateMetricChangeEvent (API version 62.0)**
Change events are available for the object.

### CollabTemplateMetricRecord

Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric. CollabTemplateMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference


### Standard Objects CollabUserEngagementMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabTemplateMetric record.

```
MetricDate

MetricDateOnly

EntityType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabUserEngagementMetric

Represents the user engagement metrics for a Quip thread in a Quip template or document. This object is available in API version 50.0
and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects CollabUserEngagementMetric

Fields

**Field** **Details**

```
CommentCount

EditCount

MetricDate

MetricDateOnly

Name

QuipThread

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments by the user for the specified `MetricDate` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits by the user for the specified `MetricDate` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngagementMetric object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects CollabUserEngagementMetric

**Field** **Details**

**Description**
The Quip thread ID.

```
QuipThreadTitle

QuipThreadType

QuipUser

SalesforceUserId

Site

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the Quip document, sheet, slide, and so forth.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Quip thread. The possible values are:

**•** `CHAT`

**•** `DOCUMENT`

**•** `SHEET`

**•** `SLIDE`

**•** `TEMPLATE`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Quip user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollabUserEngmtRecordLink

**Field** **Details**

**Description**
The ID of the Quip site.

```
SourceTemplate

ViewCount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the source template.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of views by the user for the specified `MetricDate` .

### CollabUserEngmtRecordLink

Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such as
an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.

Note: The CollabUserEngmtRecordLink object is now deprecated. You can still access user engagement metrics for metric dates
before August 12, 2021. To obtain user engagement metric for dates starting from August 12, 2021, follow the instructions in the
[Quip Engagement Metrics documentation.](https://help.salesforce.com/articleView?id=xcloud.quip_template_metrics.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
MetricDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the gathered metric.


### Standard Objects ColorDefinition

**Field** **Details**

```
Name

ObjectType

ParentRecordId

UserEngagementMetricId

### ColorDefinition

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngmtRecordLink object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabUserEngagementMetric record.

Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ColorDefinition

Fields

**Field Name** **Details**

```
Color

Context

DurableId

TabDefinitionId

Theme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color described in web color RGB format—for example, “00FF00”.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color context, which determines whether the color is the main color (or
primary) for the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The `TabDefinition` ID.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string


### Standard Objects ContCalloutSummaryEventLog

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon’s theme.

### ContCalloutSummaryEventLog

Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction, their
response status codes, execution times, and URL endpoint destinations. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ContinuationIdentifier

Duration

IsSuccess

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique ID identifying a sequence of events within a request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total duration of continuation, in milliseconds.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ContCalloutSummaryEventLog

**Field** **Details**

**Description**
Indicates whether the continuation was successful or not.

```
OriginRequestIdentifier

RequestFormSize

RequestIdentifier

ResponseSize

StatusCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the request that initiated a callout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Continuation request form size, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the callout response, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP status or internal code returned by the remote endpoint. A status code of 200
indicates that the request was successful. Other status code values indicate the type of


### Standard Objects CombinedAttachment

**Field** **Details**

problem that was encountered. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

```
Timestamp

Url

UserIdentifier

VisualforceControllerSize

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The callout endpoint URL. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

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
Continuation Visualforce controller size, in bytes. Depending on how many HTTP requests
were used in a continuation, this field can contain up to three space-separated values.

### CombinedAttachment

This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM content, and
files added to Chatter that are associated with a record.


Standard Objects CombinedAttachment

Supported Calls

```
   describeSObjects()

```

Fields

**Field Name** **Details**

```
ContentSize

ContentSizeLong

ContentUrl

ExternalDataSourceName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for documents smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL for links and Google Docs. This field is set only for links and Google Docs,
and is one of the fields that determine the `FileType` .

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the external data source in which the document is stored. This field
is set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.


Standard Objects CombinedAttachment

**Field Name** **Details**

```
ExternalDataSourceType

FileExtension

FileType

ParentId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in API version 35.0 and later.

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

Type of document, which is determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the parent object.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,


Standard Objects CombinedAttachment

**Field Name** **Details**

AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentWorkspace, Contract, ConversationEntry,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria,
Event, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
IdentityDocument, Image, IndividualApplication, Invoice, InvoiceLine, Lead,
ListEmail, Location, MarketSegment, MarketSegmentActivation, MemberPlan,
MessagingSession, MktCalculatedInsight, OperatingHours, Opportunity, Order,
OrderItem, Organization, OtherComponentTask, PartyConsent, PersonEducation,
PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit, PlanBenefitItem,
Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report,
ReportAnomalyEventStore, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement,
SocialPost, Solution, Task, ThreatDetectionFeedback, User, Visit, VisitedParty,
Visitor, VoiceCall, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
RecordType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The parent object type.


### Standard Objects CommerceEntitlementBuyerGroup

**Field Name** **Details**

```
 SharingOption

Title

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Controls whether sharing is frozen for a file. Only Salesforce admins and file
owners with Collaborator access to the file can modify this field. The default is
`Allowed`, which means that new shares are allowed. When set to
`Restricted`, new shares are prevented without affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the attached file.

Use this object to list all notes, attachments, documents uploaded to libraries in Salesforce CRM content, and files added to Chatter for
a record, such as a related list on a detail page.

To determine if an object supports the CombinedAttachment object, call `describeSObject()` on the object. For example,
`describeSObject('Account')` returns all the child relationships of the Account object, including `CombinedAttachment` .
You can then query the CombinedAttachment child relationship.

```
SELECT Name, (SELECT Title FROM CombinedAttachments)

FROM Account

```

You can’t directly query CombinedAttachment.

### CommerceEntitlementBuyerGroup

Represents the entitlement policy for a buyer group. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`


Standard Objects CommerceEntitlementBuyerGroup

Special Access Rules

The CommerceEntitlementBuyerGroup object is available when you meet these requirements. The B2B Commerce license is enabled.
The Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
BuyerGroupId

CurrencyIsoCode

Name

PolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the buyer group.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the entitlement buyer group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the entitlement policy.


### Standard Objects CommerceEntitlementPolicy

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementBuyerGroupChangeEvent on page 68**
Change events are available for the object.

### CommerceEntitlementPolicy

Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version 49.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CommerceEntitlementPolicy object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CanViewPrice

CanViewProduct

CurrencyIsoCode

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the price of a product ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the product ( `true` ) or not ( `false` ). Default value is
`false` .

**Type**
picklist


Standard Objects CommerceEntitlementPolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

```
Description

IsActive

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entitlement policy description.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines if the entitlement policy is active ( `true` ) or inactive ( `false` ). Default value is
`false` .

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
The timestamp for when the current user last viewed this record. If this value is null, it can
mean that the record was only referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string


### Standard Objects CommerceEntitlementPolicyShare

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the entitlement policy.

```
OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID for the entitlement policy owner.

This object has the following associated objects. Except where noted, these objects are available in the same API version as
CommerceEntitlementPolicy.

**CommerceEntitlementPolicyChangeEvent on page 68**
Change events are available for the object.

**CommerceEntitlementPolicyOwnerFeed on page 55**
Feed tracking is available for the object.

**CommerceEntitlementPolicyHistory on page 63**
History is available for tracked fields of the object.

**CommerceEntitlementPolicyOwnerSharingRule**

Sharing rules are available for this object.

### CommerceEntitlementPolicyShare

Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version
49.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CommerceEntitlementPolicyShare

Special Access Rules

The CommerceEntitlementPolicyShare object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

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
Possible values are:

**•** `All` —Owner

**•** `Edit` —Read/Write

**•** `Read` —Read Only

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent entitlement policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantCollaboration` —Compliant Data Sharing

**•** `GuestParentImplicit` —Associated guest user sharing

**•** `GuestPersonImplicit` —Associated Guest User Sharing

**•** `GuestRule` —Guest User Sharing Rule

**•** `ImplicitChild` —Account Sharing

**•** `ImplicitParent` —Associated record owner or sharing

**•** `ImplicitPerson` —Person Contact

**•** `Manual` —Manual Sharing


### Standard Objects CommerceEntitlementProduct

**Field** **Details**

**•** `Owner`

**•** `Rule` —Sharing Rule

**•** `SurveyShare` —Survey Sharing Rule

**•** `Team` —Sales Team

**•** `Territory` —Territory Assignment Rule

**•** `Territory2AssociationManual` —Territory Manual

**•** `Territory2Forecast` —Territory assignment for forecasting and reporting

**•** `TerritoryManual` —Territory Manual

**•** `TerritoryRule` —Territory Sharing Rule

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the associated user or buyer group.

### CommerceEntitlementProduct

Represents the entitlement policy for a product. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Special Access Rules

The CommerceEntitlementProduct object is available when you meet these requirements. The B2B Commerce license is enabled. The
Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

```
Name

PolicyId

ProductId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The product entitlement policy name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product entitlement policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product referenced in the entitlement policy.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementProductChangeEvent on page 68**
Change events are available for the object.

### CommissionSchedule

Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.


Standard Objects CommissionSchedule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ApplicableObject

CalcProcessInputMapping

CalcProcessOutput

CalcProcessOutputConvNotation

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The object for which this Commission Schedule calculates commissions.

Possible values are:

**•** `Contract`

**•** `InsurancePolicy`

**•** `Producer`

**•** `Quote`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input mappings from the object fields to the variables used in the commission calculation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula applied to this Commission Schedule’s process output that calculates the final
commission amount.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optimized version of the CalcProcessOutput formula that calculates the commission. Not
user-editable.


Standard Objects CommissionSchedule

**Field** **Details**

```
CalculationProcessName

CalculationType

CommissionAmount

CommissionRate

CommissionStructureType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Integration Procedure, Calculation Matrix, or Calculation Procedure this
Commission Schedule uses for calculations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of calculation or process used when this Commission Schedule is used.

Possible values are:

**•** `Amount`

**•** `CalculationMatrix`

**•** `CalculationProcedure`

**•** `IntegrationProcedure`

**•** `Rate`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission amount for the Commission Schedule when the process type is Amount.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission percentage for the Commission Schedule when the process type is Rate.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
Indicates whether the commission calculation is Flat or Tiered when the process type is
Matrix.

Possible values are:

**•** `Flat`

**•** `Tiered`

The default value is `Flat` .

```
EffectiveEndDate

EffectiveStartDate

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The effective end date of the Commission Schedule.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The effective start date of the Commission Schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Commission Schedule is active.

The default value is `false` .

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


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

```
Name

OwnerId

TierDefinition

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Commission Schedule.

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

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Internal-only. Applies when the CalculationType is CalculationMatrix.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleFeed**

Feed tracking is available for the object.


### Standard Objects CommissionScheduleAssignment

**CommissionScheduleHistory**

History is available for tracked fields of the object.

**CommissionScheduleOwnerSharingRule**

Sharing rules are available for the object.

**CommissionScheduleShare**

Sharing is available for the object.

### CommissionScheduleAssignment

Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommissionableEventType

CommissionScheduleId

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The event that results in the commission calculation.

Possible values are:

**•** `Contracting`

**•** `Endorsement`

**•** `Issue Policy`

**•** `Policy Issuance`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
### CommissionSchedule


Standard Objects CommissionScheduleAssignment

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule

```
EffectiveEndDate

EffectiveStartDate

LastReferencedDate

LastViewedDate

MaxCommissionAmount

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date when the Commission Schedule is in effect for the product or producer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first date when the Commission Schedule is in effect for the product or producer.

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.


Standard Objects CommissionScheduleAssignment

**Field** **Details**

```
MaxCommissionRate

MinCommissionAmount

MinCommissionRate

Name

ProducerId

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission rate that a producer receives for a commissionable event.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission rate that a producer receives for a commissionable event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the Commission Schedule Assignment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.

This is a relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup


### Standard Objects CommSubscription

**Field** **Details**

**Refers To**
Producer

```
Product2Id

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product for which commissions are calculated.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleAssignmentChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleAssignmentFeed**

Feed tracking is available for the object.

**CommissionScheduleAssignmentHistory**

History is available for tracked fields of the object.

**CommissionScheduleAssignmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CommissionScheduleAssignmentShare on page 67**
Sharing is available for the object.

### CommSubscription

Represents the subscription options for a specific communication. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CommSubscription

Fields

**Field** **Details**

```
DataUsePurposeId

IsDefault

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
ID of the data use purpose record associated with the communication subscription.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this communication subscription is the default ( `true` ) or not ( `false` ). This field
has a default value of `false` . Only one communication subscription record can be the
default.

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
Required. Name of the communication subscription record.

**Type**
reference


### Standard Objects CommSubscriptionChannelType

**Field** **Details**

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

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionFeed**

Feed tracking is available for the object.

**CommSubscriptionHistory**

History is available for tracked fields of the object.

**CommSubscriptionOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionShare**

Sharing is available for the object.

### CommSubscriptionChannelType

Represents the engagement channel through which you can reach a customer for a communication subscription. This object is available
in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CommSubscriptionChannelType

Fields

**Field** **Details**

```
CommunicationSubscriptionId

EngagementChannelTypeId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription record.

This is a relationship field.

**Relationship Name**
CommunicationSubscription

**Relationship Type**
Lookup

**Refers To**
CommSubscription

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated engagement channel type record.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

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


Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
MessagingChannelUsageId

Name

OwnerId

```

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription channel type record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects CommSubscriptionConsent

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionChannelTypeFeed**

Feed tracking is available for the object.

**CommSubscriptionChannelTypeHistory**

History is available for tracked fields of the object.

**CommSubscriptionChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionChannelTypeShare**

Sharing is available for the object.

### CommSubscriptionConsent

Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.

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

**Description**
The ID of the Business Brand that the individual has given consent to for a communication
subscription. This is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand


Standard Objects CommSubscriptionConsent

**Field** **Details**

```
CommSubscriptionChannelTypeId

ConsentCapturedDateTime

ConsentCapturedSource

ConsentGiverId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription channel type record.

This is a relationship field.

**Relationship Name**
CommSubscriptionChannelType

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionChannelType

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when the customer’s consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Source through which consent was captured. For example, user@example.com
or www.example.com.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the person who gave consent to the communication subscription on behalf of the
contact point.

Note: If the contact point gave consent, don't use `ConsentGiverId` .

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, User

```
ContactPointId

DataUsePurposeId

EffectiveFromDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point, such as an Individual or person account, associated with the
communication subscription consent.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent with.
This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when consent starts.


Standard Objects CommSubscriptionConsent

**Field** **Details**

```
EffectiveToDate

EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when consent ends. This field is restricted by field-level security.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the contact method you want to apply consent to. This field is available in API
version 57.0 and later.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

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


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Description**
Required. Name of the communication subscription consent record.

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
The ID of the account owner associated with this customer.

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
Filter, Group, Nillable, Sort

**Description**
Represents the record based on the Individual object that you want to associate consent
with. This field is available in API version 57.0 and later.

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
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole


### Standard Objects CommSubscriptionTiming

**Field** **Details**

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
Identifies whether the individual or person account associated with this record agrees to
this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.

**•** `Seen`

The default value is `NotSeen` . This field is available in API version 57.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommSubscriptionConsentChangeEvent (API version 49.0)**
Change events are available for the object.

**CommSubscriptionConsentFeed**

Feed tracking is available for the object.

**CommSubscriptionConsentHistory**

History is available for tracked fields of the object.

**CommSubscriptionConsentOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionConsentShare**

Sharing is available for the object.

### CommSubscriptionTiming

Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0 and
later.


Standard Objects CommSubscriptionTiming

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommSubscriptionConsentId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated communication subscription consent record.

This is a relationship field.

**Relationship Name**
CommSubscriptionConsent

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionConsent

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
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects CommSubscriptionTiming

**Field** **Details**

**Description**
Required. Name of the communication subscription timing record.

```
Offset

PreferredTimeEnd

PreferredTimeStart

PreferredTimeZone

Unit

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of time before or after an event or the specific day of the week to communicate
with the contact point. Set the unit of time in the `Unit` field.

For example, if you set `Unit` as _`Week`_ and `Offset` as _`-4`_, communicate with the contact
point four weeks before the event. If you set `Offset` as _`4`_, communicate with the contact
point four weeks after the event.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
End of the preferred time span in which to reach the customer.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Start of the preferred time span in which to reach the customer.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the preferred time span.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of time that works with the `Offset` field to determine the communication timing.


### Standard Objects Community (Zone)

**Field** **Details**

Possible values are:

**•** `Day`

**•** `DayOfWeek`

**•** `Hour`

**•** `Month`

**•** `Week`

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionTimingChangeEvent (API version 62.0)**
Change events are available for the object.

**CommSubscriptionTimingFeed**

Feed tracking is available for the object.

**CommSubscriptionTimingHistory**

History is available for tracked fields of the object.

### Community (Zone)

Represents a zone that contains Idea or Question objects.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas communities were renamed to zones. In API version 28,
### the API object label has changed to Zone, but the API type is still Community .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CanCreateCase

DataCategoryName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether users can ask private questions in the zone using Chatter Answers.

**Type**
string


Standard Objects Community (Zone)

**Field** **Details**

**Properties**
Filter, Nillable, Group, Sort

**Description**
The data category associated with the zone.

```
Description

HasChatterService

IsActive

IsPublished

Name

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text description of the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether Chatter Answers is available in the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is active or inactive. An idea or question can only be posted to
an active zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is available in portals.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the zone.


### Standard Objects ConcurApexLimitEventLog

**Field** **Details**

```
NetworkId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this zone is associated with. This field is available only if
digital experiences is enabled in your org. This field is available in API version 66.0 and later.

Use this object to create a zone in Ideas, Chatter Answers, or Answers. Zones help organize ideas and questions into logical groups and
are shared by the Ideas, Answers, and Chatter Answers.

### ConcurApexLimitEventLog

Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce terminated
after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted towards
your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the long-running
requests exceed the org default limit, additional long-running requests are denied. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
RequestCount

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.


Standard Objects ConcurApexLimitEventLog

**Field** **Details**

```
RequestIdentifier

RequestLimit

RequestUri

Timestamp

UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `RequestCount` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.) See
_Apex Developer Guide_ [: Lightning Platform Apex Limits. For example:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section) `10` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the long-running Apex request that Salesforce terminated. For example:
`/apex/ApexClassName` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .


### Standard Objects ConnectedApplication ConnectedApplication

Represents a connected app and its details; all fields are read-only.

Connected apps link client applications, third-party services, other Salesforce organizations, apps, and resources to your organization.
The connected app configuration specifies authorization and security settings for these resources. This object exposes the settings for
a specified connected app.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
MobileSessionTimeout

MobileStartUrl

Name

NamedUserUvidTimeout

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Length of time after which the system logs out inactive mobile users.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

Users are directed to this URL after they’ve authenticated when the app is accessed
from a mobile device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ConnectedApplication

**Field Name** **Details**

**Description**

The timeout value for a JSON Web Token (JWT)-based access token that's issued
to a named user. This field defines the timeout only if the app is configured to
have an app-specific timeout. If the app uses the user's session timeout, the
timeout value is defined based on the user's profile or the org session settings.
For more information about defining JWT-based access token timeout, see
[Configure a Connected App to Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

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

This field is available in API version 59.0 and later.

```
OptionsAllowAdminApprovedUsersOnly

```

**Type**
boolean

**Properties**
Filter

**Description**

Indicates whether access is limited to users granted approval to use the connected
app by an administrator. Manage profiles for the app by editing each profile’s
Access list.

`OptionsCodeCredentialGuestEnabled` Reserved for future use.

`OptionsFullContentPushNotifications` For internal use only.

```
OptionsHasSessionLevelPolicy

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the connected app requires a High Assurance level session.


Standard Objects ConnectedApplication

**Field Name** **Details**

`OptionsIsInternal` For internal use only.

```
OptionsRefreshTokenValidityMetric

OptionsTokenExchangeManageBitEnabled

PinLength

RefreshTokenValidityPeriod

StartUrl

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the refresh token validity is based on duration or inactivity. If
`true`, the token validity is measured based on the last use of the token;
otherwise, it’s based on the token duration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, the OAuth 2.0 token exchange flow is enabled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

For mobile apps, this field is the PIN length requirement for users of the connected
app. Valid values are `4`, `5`, `6`, `7`, or `8` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The duration of an authorization token until it expires in hours, months, or days
as set in the connected app management page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

If the app isn’t accessed from a mobile device, users are directed to this URL after
they’ve authenticated.


### Standard Objects ConferenceNumber

**Field Name** **Details**

```
UvidTimeout

### ConferenceNumber

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The timeout value for a JWT-based access token that's issued to an unknown
user as a result of the guest user variation of the Authorization Code and
Credentials Flow. JWT-based access tokens issued during this flow variation
always contain a UVID.

This field defines the timeout only if the app is configured to have an app-specific
timeout. If the app uses the user's session timeout, the timeout value is defined
based on the user's profile or the org session settings. For more information about
[defining JWT-based access token timeout, see Configure a Connected App to](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)
[Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

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

This field is available in API version 59.0 and later.

Holds the telephone number for an external event shown in the Salesforce Today feature in the Salesforce mobile app. This object is
available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects ConferenceNumber

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
AccessCode

ExternalEventId

IsLocked

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the access code to enter in order to validate identity and join the call.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external event associated with the conference number.

This field is a relationship field.

**Relationship Name**
ExternalEvent

**Refers To**
ExternalEvent

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the conference number is locked, or `false` if it’s not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the conference number.


### Standard Objects Consumption Rate

**Field** **Details**

```
MayEdit

Name

Number

Vendor

```

Associated Objects

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

Indicates whether the conference number can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the conference call’s organizer.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number used to connect to the conference call.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The vendor or company associated with the conference number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ConferenceNumberChangeEvent**

### Consumption Rate

Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require at
least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.

The consumption rate sets a quantity-based boundary for usage and defines how much your product costs when its usage falls within
that boundary. Consumption rates price usage at a per-unit fee or a flat fee across the entire range of usage.


Standard Objects Consumption Rate

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsumptionScheduleId

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The consumption schedule that contains the consumption rate.

This is a relationship field.

**Relationship Name**
ConsumptionSchedule

**Relationship Type**
Lookup

**Refers To**
ConsumptionSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption rate.


Standard Objects Consumption Rate

**Field** **Details**

```
LowerBound

Name

Price

PricingMethod

ProcessingOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The lowest quantity of usage for the consumption rate.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The price for usage that falls within the consumption rate’s bounds.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How Salesforce applies the consumption rate’s price to the total quantity of usage within a
usage summary.

Possible values are:

**•** `FlatFee` —Salesforce applies the rate’s price to the entire quantity of usage.

**•** `PerUnit` —Salesforce applies the rate’s price to each individual quantity of usage
within the usage summary.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order for processing the usage rate across multiple rates. Consumption rates are evaluated
beginning with the lowest processing order.


### Standard Objects Consumption Schedule

**Field** **Details**

```
UpperBound

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The highest quantity of usage for the consumption rate.

### Consumption Schedule

A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object is
available in API version 45.0 and later.

Salesforce uses consumption schedules to group consumption rates. Your consumption schedule defines the unit of measurement and
rating method for the schedule's rates. It also defines the billing frequency that Salesforce Billing uses to invoice a usage product.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BillingTerm

BillingTermUnit

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number used with the billing term unit to determine billing frequency.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit used with the billing term to determine billing frequency

Possible values are:

**•** `Month`  

**•** `Quarter`  

**•** `Year`  


Standard Objects Consumption Schedule

**Field** **Details**

```
CurrencyIsoCode

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Label is **Active** .

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


Standard Objects Consumption Schedule

**Field** **Details**

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
MatchingAttribute

Name

NumberOfRates

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce Billing matches usage with a consumption schedule if the records share Matching
Attribute value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of consumption rates in this consumption schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns a consumption schedule record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects Consumption Schedule

**Field** **Details**

```
RatingMethod

SBQQ__Category__c

Type

UnitOfMeasure

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A specific use case to rate usage against the schedule. This field is the controlling picklist for
the Type field.

Possible values are:

**•** `Tier`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is available only with Salesforce CPQ.

You can define custom categories to organize consumption schedules in separate tabs on
sales rep UI. If you do this, make sure to create a field set for each category.

Possible values are:

**•** `Rates`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how rate tiers are calculated.

Possible values are:

**•** `Range` —The schedule prices only using the tier that applies to the usage quantity.

**•** `Slab` —Usage within a given bound receives pricing equal to its tier’s value.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unit of measure defines how you quantify instances of usage for your usage products. For
example, if your usage product is a cloud storage subscription, you could provide a value of
GB for your unit of measure.


### Standard Objects Contact

**Field** **Details**

```
 blng__BillingRule__c

 blng__RevenueRecognitionRule__c

 blng__TaxRule__c

### Contact

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing invoices usage summaries based off their related consumption schedule's
billing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing recognizes usage summary revenue based off the summary's related revenue
recognition rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing taxes usage summary invoice lines based off the summary's related tax
rule.

Represents a contact, which is a person associated with an account.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Contact

Special Access Rules

Customer Portal users can access only portal-enabled contacts.

Fields

**Field** **Details**

```
AccountId

ActionCadenceAssigneeId

ActionCadenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account that’s the parent of this contact.

We recommend that you update up to 50 contacts simultaneously when changing the
accounts on contacts enabled for a Customer Portal or partner portal. We also recommend
that you make this update after business hours.

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
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 48.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 48.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.


Standard Objects Contact

**Field** **Details**

```
ActionCadenceState

ActiveTrackerCount

ActivityMetricId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. This field is available in API version 50.0 and
later when the Sales Engagement license is enabled. To see this field, the user also needs
the Sales Engagement User or Sales Engagement Quick Cadence Creator user permission
set.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cadences that are actively running on this contact. This field is available in
API version 57.0 and later when the Sales Engagement license is enabled. To see this field,
the user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric


Standard Objects Contact

**Field** **Details**

```
ActivityMetricRollupId

AssistantName

AssistantPhone

Birthdate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s name.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s phone number. Label is **Asst. Phone** .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s birthdate.

Filter criteria for report filters, list view filters, and SOQL queries ignore the year portion of
the `Birthdate` field. For example, this SOQL query returns contacts with birthdays later
in the year than today:

```
  SELECT Name, Birthdate

  FROM Contact

  WHERE Birthdate > TODAY

```


Standard Objects Contact

**Field** **Details**

```
BuyerAttributes

CanAllowPortalSelfReg

CleanStatus

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the role of the contact in the opportunity or account. Possible values are:

**•** `BusinessUser` —For example, an end user. Key value.

**•** `Buyer` —Key value

**•** `Champion` —Key value

**•** `DecisionMaker` —Shown in green on a contact in the buyer relationship map UI.
Key value.

**•** `Detractor` —Shown in red on a contact in the buyer relationship map UI. Key value.

**•** `Evaluator`

**•** `ExecutiveSponsor` —Key value

**•** `TechnicalExpert`

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success.

Warning: To ensure that the buyer relationship map feature works as expected,
don't modify field values. For example, if you change `Detractor` to `Detract`,
the value isn’t shown in red in a buyer relationship map.

This field is available with all profiles except custom and minimum-access. To provide access,
use field-level security in Object Manager.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this contact can self-register for your Customer Portal ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Indicates the record’s clean status as compared with Data.com. Values include: `Matched`,
`Different`, `Acknowledged`, `NotFound`, `Inactive`, `Pending`, `SelectMatch`,
or `Skipped` .

Several values for `CleanStatus` appear with different labels on the contact record.

**•** `Matched` appears as `In Sync`

**•** `Acknowledged` appears as `Reviewed`

**•** `Pending` appears as `Not Compared`

```
ConnectionReceivedId

ConnectionSentId

ContactSource

Department

```

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
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Creation is enabled, this field indicates whether the contact was created
automatically. A possible value is:

**•** `Auto Create`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s department.


Standard Objects Contact

**Field** **Details**

```
DepartmentGroup

Description

DoNotCall

Email

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the business unit, function, or department that the contact belongs to in the organization.
Possible values are:

**•** `chiefExecutive` —Key value

**•** `customerSuccess` —For example, wealth management, consumer banking, subject
matter experts, or healthcare research experts.

**•** `finance` —Includes pricing and procurement. Key value.

**•** `humanResources`

**•** `legal` —Key value

**•** `marketing`

**•** `other`

**•** `sales`

**•** `support` —For example, tech support or customer support.

**•** `tech` —For example, IT or engineering. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success. This field is available with all profiles except custom and minimum-access. To
provide access, use field-level security in Object Manager.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contact. Label is **Contact Description** up to 32 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the contact doesn’t want to receive calls.

**Type**
email


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The contact’s email address.

```
EmailBouncedDate

EmailBouncedReason

Fax

FirstCallDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the date and time of the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the reason for the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s fax number. Label is **Business Fax** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.


Standard Objects Contact

**Field** **Details**

```
FirstEmailDateTime

FirstName

GenderIdentity

HasOptedOutOfEmail

HasOptedOutOfFax

HomePhone

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s first name up to 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact doesn’t want to receive email from Salesforce ( `true` ) or does
( `false` ). Label is **Email Opt Out** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact prohibits receiving faxes.

**Type**
phone


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s home phone number. Label is **Home Phone** .

```
IndividualId

IsDeleted

IsEmailBounced

IsPersonAccount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this contact. This field is available if Data
Protection and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

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
If bounce management is activated and an email is sent to a contact, indicates whether the
email results in a soft or hard bounce ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Contact

**Field** **Details**

**Description**
Read only. Indicates whether this account has a record type of Person Account ( `true` ) or
not ( `false` ). Label is **Is Person Account** .

```
IsPriorityRecord

Jigsaw

JigsawContactId

LastActivityDate

```

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the contact as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the company’s ID in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is `null`, the account wasn’t
imported from Data.com. Maximum size is 20 characters. Available in API version 22.0 and
later. Label is **Data.com Key** .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify this value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to `Jigsaw` .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent of either:

**•** Due date of the most recent event logged against the record.


Standard Objects Contact

**Field** **Details**

**•** Due date of the most recently closed task associated with the record.

```
LastName

LastReferencedDate

LastViewedDate

LeadSource

MailingAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the contact up to 80 characters.

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
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the lead that was converted to this contact.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. For details on compound address
fields, see Address Compound Fields.


Standard Objects Contact

**Field** **Details**

```
MailingCity

MailingCountry

MailingCountryCode

MailingGeocodeAccuracy

MailingLatitude

MailingLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the mailing address. For details on geolocation compound
field, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `MailingLongitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Used with `MailingLatitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

```
MailingPostalCode

MailingState

MailingStateCode

MailingStreet

MasterRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for mailing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
remains. If this record was deleted for any other reason, or hasn’t been deleted, the value is
`null` .

This is a relationship field.


Standard Objects Contact

**Field** **Details**

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Contact

```
MiddleName

MobilePhone

Name

OtherAddress

OtherCity

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s middle name. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contact’s mobile phone number. Label is **Mobile Phone** .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the other address. Read-only. For details on compound address fields,
see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Alternate address details.

```
OtherCountry

OtherCountryCode

OtherGeocodeAccuracy

OtherLatitude

OtherLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the other address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLongitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLatitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.


Standard Objects Contact

**Field** **Details**

```
OtherPhone

OtherPostalCode

OtherState

OtherStateCode

OtherStreet

OwnerId

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone for alternate address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street for alternate address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this contact.


Standard Objects Contact

**Field** **Details**

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
Phone

PhotoUrl

Pronouns

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the contact. Label is **Business Phone** .

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance ( _Example:_
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the contact. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the contact.

Empty if Social Accounts and Contacts isn't enabled or if Social Accounts and Contacts is
disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the contact in the third person. The entry is selected from a picklist of
available values, which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`


Standard Objects Contact

**Field** **Details**

**•** `They/Them`

```
RecordTypeId

ReportsToId

Salutation

ScheduledResumeDateTime

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that this contact reports to.

This is a relationship field.

**Relationship Name**
ReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr.
or Mrs.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.


Standard Objects Contact

**Field** **Details**

```
Suffix

Title

TitleType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the contact. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the contact, such as CEO or Vice President.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the hierarchical position that the contact holds in the organization. In the UI, this field is
shown as Seniority Level. Possible values are:

**•** `ceo` —Key value

**•** `directorOrManager` —Key value

**•** `executive` —Key value

**•** `individualContributor`

**•** `vp` —VP or Head of Department. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t show contacts with key values, then Salesforce prompts you to add them. Having
all key values represented on the map provides a complete picture of the deal or account,
increasing sales success. This field is available with all profiles except custom and
minimum-access. To provide access, use field-level security in Object Manager.

Note: When importing contact data, users need the Set Audit Fields upon Record Creation permission to assign values to audit
fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields yourself.

Usage

Use this object to manage individual people who are associated with an account. You can create, query, delete, or update any attachment
associated with a contact.

Create or update contacts by converting a lead with the `convertLead()` call.


### Standard Objects ContactCenterChannel

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ContactFeed (API version 18.0)**
Feed tracking is available for the object.

**ContactHistory (API version 11.0)**
History is available for tracked fields of the object.

**ContactOwnerSharingRule**

Sharing rules are available for the object.

**ContactShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ContactCenterChannel

Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration and
routing information for callback requests. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Service Cloud Voice with Amazon Connect, Service Cloud Voice with Partner Telephony, Service Cloud Voice with
Partner Telephony from Amazon Connect, or Bring Your Own Channel for Contact Center as a Service (CCaaS) must be enabled. To
access this object, you must be a SysAdmin user or have ViewSetup user permissions.

Fields

**Field** **Details**

```
ChannelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ContactCenterChannel

**Field** **Details**

**Description**
For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring Your
Own Channel messaging channel (MessagingChannel) that’s associated with the contact
center (CallCenterId). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
Channel

**Refers To**
MessagingChannel

```
ContactCenterId

OmniCallbackFallbackQueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field. For Bring Your Own Channel for CCaaS, this field represents
the unique ID of the contact center (CallCenterId) that’s associated with the Bring Your Own
Channel messaging channel (MessagingChannel). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ContactCenter

**Relationship Type**
Master-detail

**Refers To**
CallCenter (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the fallback queue to use if contact
request routing through an Omni-Channel flow fails. Don't change the value in this field.
Instead, configure contact request routing in Lightning Experience.

Available in API version 65.0 and later.

This field is a relationship field.

**Relationship Name**
OmniCallbackFallbackQueue

**Refers To**
Group


Standard Objects ContactCenterChannel

**Field** **Details**

```
OmniCallbackHandler

UserId

VoicemailFallbackQueueId

VoicemailHandler

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the flow or queue used to route contact
requests. Don't change the value in this field. Instead, configure contact request routing in
Lightning Experience.

Available in API version 65.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Available in API version 63.0 only. For internal use.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the fallback queue to use if voicemail routing fails. Don't change the value in this field.
Instead, configure voicemail routing in Lightning Experience.

This field is a relationship field.

**Relationship Name**
VoicemailFallbackQueue

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the flow used to route voicemails. Don't change the value in this field. Instead, configure
voicemail routing in Lightning Experience.


### Standard Objects ContactCleanInfo ContactCleanInfo

Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related
processing of contact records. ContactCleanInfo includes a number of bit vector fields.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Contact Clean Info provides a snapshot of the data in your Salesforce contact record and its matched Data.com record at the time the
Salesforce record was cleaned.

Contact Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field `IsDifferent` has an `IsDifferentEmail`
field. If the `IsDifferentEmail` field’s value is `False`, that means the `Email` field value is _the same_ on the Salesforce contact
record and its matched Data.com record.

### ContactCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the contact record.

**•** `IsDifferent` indicates whether or not a field on the contact record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the contact record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the contact record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

Fields

**Field Name** **Details**

```
Address

City

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
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
CleanedByJob

CleanedByUser

ContactId

ContactStatusDataDotCom

Country

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Data.com Clean job ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Salesforce user ( `true` )
or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the contact record was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the contact per Data.com. Values are: `Contact is Active`
`per Data.com`, `Phone is Wrong per Data.com`, `Email is`
`Wrong per Data.com`, `Phone and Email are Wrong per`
`Data.com`, `Contact Not at Company per Data.com`, `Contact`
`is Inactive per Data.com`, `Company this contact`
`belongs to is out of business per Data.com`, `Company`

```
  this contact belongs to never existed per Data.com
```

or `Email address is invalid per Data.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**

Details for the billing address of the contact.

```
DataDotComID

Email

FirstName

IsDifferentCity

IsDifferentCountry

IsDifferentCountryCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s first name.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `City` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country Code` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentEmail

IsDifferentFirstName

IsDifferentLastName

IsDifferentPhone

IsDifferentPostalCode

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Email` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `First Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Last Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Phone` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Postal Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentState

IsDifferentStateCode

IsDifferentStreet

IsDifferentTitle

IsFlaggedWrongAddress

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Street` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Title` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongEmail

IsFlaggedWrongName

IsFlaggedWrongPhone

IsFlaggedWrongTitle

IsInactive

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Title` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact has been reported to Data.com as _`Inactive`_
( `true` ) or not ( `false` ).

```
IsReviewedAddress

IsReviewedEmail

IsReviewedName

IsReviewedPhone

IsReviewedTitle

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Title` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
LastMatchedDate

LastName

LastStatusChangedById

LastStatusChangedDate

Latitude

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the contact record was last matched and linked to a Data.com record.

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


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
Longitude

Name

Phone

PostalCode

State

Street

```

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

**Description**
Field label is **Contact Clean Info Name** . The name of the contact. Maximum
size is 255 characters.

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


### Standard Objects ContactDailyMetric

**Field Name** **Details**

**Description**

Details for the billing address of the contact.

```
Title

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s title.

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


Standard Objects ContactDailyMetric

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

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


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The number of calls in the day for this contact with the call result Unqualified.

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsDeliveredRate

AllEmailsHardBouncedCount

AllEmailsOutOfOfficeCount

```

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

**Description**
The number of successfully delivered emails for this contact in the day.

This is a calculated field.

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


Standard Objects ContactDailyMetric

**Field** **Details**

```
AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

ContactId

```

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


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

```
DailyCutOffTimeStamp

Date

DateInt

HardBounceTrackableSends

InboundEngagementsCount

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.

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


Standard Objects ContactDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `UniqueEmailsOpenedCount`,
`UniqueEmailsRepliedCount`, and `UniqueEmailsLinkClickedCount` .

Available in API version 58.0 and later.

```
LinkClickTrackableSends

OpenTrackableSends

OutOfOfficeTrackableSends

OutboundEngagementsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking.

Available in API version 54.0 and later.

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


Standard Objects ContactDailyMetric

**Field** **Details**

```
ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

```

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

**Description**
The number of emails sent to this contact with soft bounce tracking.

Available in API version 54.0 and later.

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


Standard Objects ContactDailyMetric

**Field** **Details**

Available in API version 54.0 and later.

```
TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.

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


### Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of individual emails opened by the contact in the day.

```
UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the day.

### ContactMonthlyMetric

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


Standard Objects ContactMonthlyMetric

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
The number of calls in the month for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Not Interested.

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


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of successfully delivered emails for this contact in the month.

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
The percentage of tracked emails sent that were successfully delivered to this contact.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the month.

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


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

ContactId

HardBounceTrackableSends

```

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


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent to this contact with hard bounce tracking. Available in API version
54.0 and later.

```
LinkClickTrackableSends

Month

MonthInt

OpenTrackableSends

OutOfOfficeTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking. Available in API version
54.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

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


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

```

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

**Description**
The number of emails sent to this contact with soft bounce tracking. Available in API version
54.0 and later.

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


Standard Objects ContactMonthlyMetric

**Field** **Details**

This field is a calculated field.

```
TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. Available in API version 54.0 and later.

This field is a calculated field.

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


### Standard Objects ContactPointAddress

**Field** **Details**

**Description**
The number of individual emails opened by the contact in the month.

```
UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the month.

### ContactPointAddress

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


Standard Objects ContactPointAddress

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
The full address.

```
AddressFirstName

AddressLastName

AddressMiddleName

AddressType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

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


Standard Objects ContactPointAddress

**Field** **Details**

**•** `Shipping`

```
BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

City

CompanyName

ContactPointPhoneId

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


Standard Objects ContactPointAddress

**Field** **Details**

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

```
Country

GeocodeAccuracy

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


Standard Objects ContactPointAddress

**Field** **Details**

```
IsDefault

IsPrimary

IsThirdPartyAddress

LastReferencedDate

LastViewedDate

Latitude

```

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

**Description**
Indicates whether a contact’s address is their primary address ( `true` ) or not ( `false` ). The
default value is `false` .

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


Standard Objects ContactPointAddress

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –90 and 90 with up to 15 decimal places.

```
Longitude

Name

OwnerId

ParentId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –180 and 180 with up to 15 decimal places.

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


Standard Objects ContactPointAddress

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

```
PhoneNumber

PostalCode

PreferenceRank

State

Street

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


### Standard Objects ContactPointConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this address. For instance, whether it’s a work address or a home
address.

Possible values are:

**•** `Home`

**•** `Inactive`

**•** `Temporary`

**•** `Work`

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


Standard Objects ContactPointConsent

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field** **Details**

```
BusinessBrandId

CaptureContactPointType

CaptureDate

CaptureSource

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact point. This
is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

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


Standard Objects ContactPointConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

```
ContactPointId

DataUsePurposeId

DoubleConsentCaptureDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point record through which the customer is consenting to be contacted.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

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


Standard Objects ContactPointConsent

**Field** **Details**

```
EffectiveFrom

EffectiveTo

EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

```

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


Standard Objects ContactPointConsent

**Field** **Details**

**Description**
Name of the contact point type consent record.

```
OwnerId

PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the account owner associated with this customer.

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


### Standard Objects ContactPointEmail

**Field** **Details**

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `Seen`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

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

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email became active.

**Type**
date


Standard Objects ContactPointEmail

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email is no longer active.

```
BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

EmailAddress

EmailDomain

EmailLatestBounceDateTime

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


Standard Objects ContactPointEmail

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when an email failed to reach its recipient.

```
EmailLatestBounceReasonText

EmailMailBox

IsPrimary

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the email didn’t reach its recipient.

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


Standard Objects ContactPointEmail

**Field** **Details**

```
Name

OwnerId

ParentId

UsageType

```

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

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ContactPointPhone

**Field** **Details**

**Description**
Specify the usage type of this email. For instance, whether it’s a work email or a temporary
email.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

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

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
The date when the contact’s phone number became active.

```
ActiveToDate

AreaCode

BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

ExtensionNumber

```

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


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
The phone number extension for the contact.

```
FormattedInternationalPhoneNumber

FormattedNationalPhoneNumber

IsBusinessPhone

IsFaxCapable

IsPersonalPhone

IsPrimary

```

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


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
Indicates whether a contact’s phone number is their primary number ( `true` ) or not ( `false` ).

```
IsSmsCapable

LastReferencedDate

LastViewedDate

Name

OwnerId

```

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
Required. The name of the contact point phone record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

This is a polymorphic relationship field.


Standard Objects ContactPointPhone

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ParentId

PhoneType

PreferenceRank

TelephoneNumber

```

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


### Standard Objects ContactPointTypeConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The phone number for the contact.

```
UsageType

```

Associated Objects

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


Standard Objects ContactPointTypeConsent

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field Name** **Details**

```
BusinessBrandId

CaptureContactPointType

CaptureDate

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

**Refers To**
BusinessBrand

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

```
CaptureSource

ContactPointType

DataUsePurposeId

DoubleConsentCaptureDate

```

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

**•** `Web`

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Description**
Date when double opt-in was captured.

```
EffectiveFrom

EffectiveTo

EngagementChannelType

```

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

```
LastReferencedDate

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
Name of the contact point type consent record.

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

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

```
PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with.
This is a polymorphic relationship field. This field is available in API version 53.0
and later.

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
Required. Identify whether the individual associated with this record agrees to
this form of contact. Possible values are:

**•** `NotSeen`

**•** `Seen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.


### Standard Objects ContactOwnerSharingRule

Associated Objects

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
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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


Standard Objects ContactOwnerSharingRule

**Field** **Details**

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

```
DeveloperName

GroupId

Name

UserOrGroupId

```

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


### Standard Objects ContactRequest

**Field** **Details**

**Description**
The ID representing the User or Group being granted access.

Usage

Use this object to manage the sharing rules for contacts.

SEE ALSO:

### Contact

ContactShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### ContactRequest

Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AvailableCallbackAttempts

DelayBetweenCallbackAttempts

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


Standard Objects ContactRequest

**Field Name** **Details**

**Description**
Specifies the delay between voice callback attempts in minutes. Applies to calls
routed through Omni-Channel Unified Routing. Valid values are `0` through
`10,080`, and the default is `0` .

Available in API version 66.0 and later.

```
IsCallback

LastReferencedDate

LastViewedDate

```

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


Standard Objects ContactRequest

**Field Name** **Details**

```
Name

OwnerId

PreferredChannel

PreferredPhone

RequestDescription

```

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

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The channel the customer selected as their preferred method of communication
in the contact request flow. For example:

**•** Phone

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number the customer provided when requesting help in the contact
request flow.

**Type**
textarea


Standard Objects ContactRequest

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the customer’s issue that they provided when requesting help
in the contact request flow.

```
RequestReason

Status

WhatId

```

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

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the contact request. For example:

**•** Abandoned

**•** Attempted

**•** Contacted

**•** New

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce record the contact request is related to, such as an account,
case, opportunity, voice call, or work order.

This is a polymorphic relationship field.


Standard Objects ContactRequest

**Field Name** **Details**

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact Request, Opportunity, WorkOrder

```
WhoId

```

Usage

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


### Standard Objects ContactRequestShare **ContactRequestShare**

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

Fields

**Field Name** **Details**

```
AccessLevel

ParentId

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


Standard Objects ContactRequestShare

**Field Name** **Details**

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ContactRequest

```
RowCause

UserOrGroupId

```

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

**•** `Owner` —The User is the owner of the ContactRequest.

**•** `Rule` —The User or Group has access via a ContactRequest sharing rule.

**•** `GuestRule` —The User or Group has access via a ContactRequest guest
user sharing rule.

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


### Standard Objects ContactShare

Usage

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

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Contact object can access this object.

Fields

**Field** **Details**

```
ContactId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Contact associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
### Contact

**Relationship Type**
Lookup


Standard Objects ContactShare

**Field** **Details**

**Refers To**
Contact

```
ContactAccessLevel

IsDeleted

RowCause

```

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

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

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


### Standard Objects ContactSuggestionInsight

**Field** **Details**

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

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Contact. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

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


Standard Objects ContactSuggestionInsight

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To add or decline contact suggestions, users need a Sales Cloud Einstein license and edit access on accounts. As of the Spring ’20 release,
Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
AccountId

Address

City

ContactTitle

Country

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related account.

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


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country of the suggested contact.

```
CreatedRecordId

CurrencyIsoCode

Division

Email

FirstName

```

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

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

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


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
GeocodeAccuracy

LastName

LastOperationUserId

LastReferencedDate

LastViewedDate

```

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


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
Latitude

Longitude

Phone

PostalCode

RationaleLabel

State

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the suggested contact.

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


### Standard Objects ContactTag

**Field Name** **Details**

**Description**
The state of the suggested contact.

```
Status

Street

```

Usage

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

**Description**
The street of the suggested contact.

This object is read-only and isn’t supported in workflows, triggers, process builder, or Visualforce pages.

### ContactTag

Associates a word or short phrase with a Contact.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

```

**Type**
reference


Standard Objects ContactTag

**Field Name** **Details**

**Properties**
Create, Filter

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

ContactTag stores the relationship between its parent TagDefinition and the Contact being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.


### Standard Objects ContentAsset ContentAsset

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

Fields

**Field** **Details**

```
ContentDocumentId

DeveloperName

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


Standard Objects ContentAsset

**Field** **Details**

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

```
IsVisibleByExternalUsers

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether unauthenticated users can see the asset file.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned. The value must be a
valid user locale (language and country), such as `de_DE` or `en_GB` . For more information
on locales, see the `Language` field on the CategoryNodeLocalization object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the asset file. This internal label doesn’t get translated.

**Type**
string


### Standard Objects ContentBody

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

### ContentBody

Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.

Supported Calls

```
   describeSObjects()

```

Special Access Rules

Cannot be queried, inserted, updated, or deleted directly.

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

### ContentBody is intended for internal Salesforce use. If you need to access the file content body, please use ContentVersion on page 1513. ContentDistribution

Represents information about sharing a document externally. This object is available in API version 32.0 and later.


Standard Objects ContentDistribution

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

**•** Chatter Free users can’t access this object.

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentDownloadUrl

ContentVersionId

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


Standard Objects ContentDistribution

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
DistributionPublicUrl

ExpiryDate

FirstViewDate

LastViewDate

Name

```

**Type**
string

**Properties**
Nillable, Sort

**Description**
URL of the link to the shared document.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the shared document becomes inaccessible.

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


Standard Objects ContentDistribution

**Field Name** **Details**

**Description**
Name of the content delivery.

```
OwnerId

PdfDownloadUrl

Password

PreferencesAllowOriginalDownload

```

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


Standard Objects ContentDistribution

**Field Name** **Details**

When `false`, download availability depends on whether a preview of the file
exists. If a preview exists, the file can’t be downloaded. If a preview doesn’t exist,
the file can still be downloaded.

If the shared document is a link, it can’t be downloaded.

```
PreferencesAllowPDFDownload

PreferencesAllowViewInBrowser

PreferencesExpires

PreferencesLinkLatestVersion

PreferencesNotifyOnVisit

```

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


Standard Objects ContentDistribution

**Field Name** **Details**

**Description**
When `true`, the owner of the shared document is emailed the first time that
someone views or downloads the shared document.

```
PreferencesNotifyRndtnComplete

PreferencesPasswordRequired

RelatedRecordId

ViewCount

```

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


Standard Objects ContentDistribution

Usage

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


### Standard Objects ContentDistributionEventLog ContentDistributionEventLog

Content Distribution events contain information about content distributions and deliveries to users. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
Action

DeliveryIdentifier

DeliveryLocation

RelatedObjectIdentifier

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


### Standard Objects ContentDistributionView

**Field** **Details**

**Description**
The 15-character ID of the record that’s associated with the delivery distribution.

```
RequestIdentifier

Timestamp

UserIdentifier

VersionIdentifier

```

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

**Description**
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

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


Standard Objects ContentDistributionView

Special Access Rules

**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** ContentDistributionView can be deleted by an admin.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistributionView. The ContentDistributionView is
still queryable by using the `QueryAll` verb.

**•** Customer Portal users can’t access this object.

**•** Chatter Free users can’t access this object.

Fields

**Field Name** **Details**

```
DistributionId

IsDownload

IsInternal

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


### Standard Objects ContentDocument

**Field Name** **Details**

**Description**
`true` if the shared document is viewed by a user in the same organization;
`false` if viewed by an external user.

```
ParentViewId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this instance of accessing the shared document.

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


Standard Objects ContentDocument

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


Standard Objects ContentDocument

**Field** **Details**

This field is available in API version 24.0 and later.

```
ContentAssetId

ContentModifiedDate

ContentSize

ContentSizeLong

```

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

**Relationship Type**
Lookup

**Refers To**
ContentAsset

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


Standard Objects ContentDocument

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 65.0 and later.

```
Description

Division

FileExtension

FileType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**

A description of the document.

This field is available in API version 31.0 and later.

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


Standard Objects ContentDocument

**Field** **Details**

```
IsArchived

IsInternalOnly

LastReferencedDate

LastViewedDate

LatestPublishedVersionId

```

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

This field is available in API version 62.0 and later.

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


Standard Objects ContentDocument

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContentVersion

`MalwareScanDate` (Beta)

`MalwareScanStatus` (Beta)

```
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the document was scanned for malware. This field is available as a beta feature in
API version 66.0 and later.

Note: The `MalwareScanDate` field is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

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


Standard Objects ContentDocument

**Field** **Details**

**Description**
ID of the owner of this document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
ParentId

PublishStatus

SharingOption

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the library that owns the document. Created automatically when inserting a
ContentVersion via the API for the first time.

This field is available in API version 24.0 and later when Salesforce CRM content is enabled.

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


Standard Objects ContentDocument

**Field** **Details**

This field is available in API versions 35.0 and later.

```
SharingPrivacy

Title

```

Usage

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


### Standard Objects ContentDocumentHistory

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


Standard Objects ContentDocumentHistory

Fields

**Field** **Details**

```
ContentDocumentId

DataType

Division

Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

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


### Standard Objects ContentDocumentLink

**Field** **Details**

**•** `contentDocUnpublished` —The document is archived or removed from a library,
either directly or when the owning library is changed.

**•** `contentDocRepublished` —The document is removed from the archive.

**•** `contentDocFeatured` —The document is featured.

**•** `contentDocSubscribed` —The document is subscribed to.

**•** `contentDocUnsubscribed` —The document is no longer subscribed to.

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

Use this read-only object to query the history of a document.

SEE ALSO:

### ContentDocument ContentDocumentLink

Represents the link between a Salesforce CRM Content document, Salesforce file, or ContentNote and where it's shared. A file can be
shared with other users, groups, records, and Salesforce CRM Content libraries. This object is available in versions 21.0 and later for
Salesforce CRM Content documents and Salesforce Files.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ContentDocumentLink

Special Access Rules

**•** In API versions 59.0 and later, enable the Query All Files permission to query without a filter on `id`, `LinkedEntityId`, and
`documentID` fields. The View All Data permission is required to enable Query All Files.

**•** In API versions 33.0 and later, you can create and delete ContentDocumentLink objects with a `LinkedEntityId` of any record
type that can be tracked in the feed, even if feed tracking is disabled for that record type.

**•** In API versions 25.0 and later, you can create ContentDocumentLink objects with a `LinkEntityId` of type User, CollaborationGroup,
or Organization.

**•** In API versions 21.0 and later, users with explicit Viewer access (the file has been directly shared with the user) to a file can delete
ContentDocumentLink objects between the file and other users who have Viewer access. In the same API versions, any user with
Viewer access to a file can delete ContentDocumentLink objects between the file and organizations or groups of which they are a
member.

**•** For orgs with Digital Experiences enabled, a document can only be shared with users and groups that are a part of the Experience
Cloud site the file was created in.

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


Standard Objects ContentDocumentLink

**Field** **Details**

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


Standard Objects ContentDocumentLink

**Field** **Details**

```
ShareType

Visibility

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
with a library, this is defined by the permissions the user has in that library. Inferred
permission on shares with libraries and file owners is available in API versions 21.0 and
later. Inferred permission on shares with standard objects is available in API versions 36.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies whether this file is available to all users, internal users, or shared users. This field is
available in API version 26.0 and later.

`Visibility` can have the following values.

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


Standard Objects ContentDocumentLink

**Field** **Details**

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

```


Standard Objects ContentDocumentLink

```
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

ContentDocument


### Standard Objects ContentDocumentListViewMapping ContentDocumentListViewMapping

Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping
between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available in API
version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To use this object, the Files Connect and Quip permissions must be enabled in the org.

To insert and update this object through the API, the QuipMassAction gater permission must also be enabled.

Fields

**Field** **Details**

```
ContentDocumentId

LastReferencedDate

LastViewedDate

ListViewId

```

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


### Standard Objects ContentDocumentSubscription

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the list view associated with the document.

```
Name

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the document.

ContentDocumentListViewMapping is used primarily by the Quip list view integration feature. Only Quip file types (Quip sheets and
docs) are supported. The ContentDocumentId field must point to a Quip file.

### ContentDocumentSubscription

Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

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
ID of the file.

This is a relationship field.


### Standard Objects ContentDocLinkEventLog

**Field** **Details**

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

```
IsCommentSub

IsDocumentSub

UserId

```

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


Standard Objects ContentDocLinkEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

RequestIdentifier

SharedWithObjectIdentifier

SharingOperation

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

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


### Standard Objects ContentFolder

**Field** **Details**

**•** `DELETE`

```
SharingPermission

Timestamp

UserIdentifier

### ContentFolder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
What permissions the document was shared with.

**Possible Values**

**•** `V` : Viewer

### • C : Collaborator

**•** `I` : Inferred—that is, the sharing permissions were inferred from a relationship between
the viewer and document. For example, a document’s owner has a sharing permission
to the document itself. Or, a document can be a part of a content collection, and the
viewer has sharing permissions to the collection rather than explicit permissions to the
document directly.

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
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.


Standard Objects ContentFolder

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

ParentContentFolderId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the folder.

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
ContentFolder

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContentFolderChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ContentFolderItem ContentFolderItem

Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object is
available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`

Special Access Rules

Fields

**Field Name** **Details**

```
ContentSize

ContentSizeLong

FileExtension

FileType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the file or folder in bytes, when the size is smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for files smaller than 2 GB.

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


### Standard Objects ContentFolderLink

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the type of file if the ContentFolderItem is a file.

```
IsFolder

ParentContentFolderId

Title

### ContentFolderLink

```

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

**Description**

The ID of the ContentFolder that the ContentFolderItem resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
### ContentFolder

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the file or folder.

Defines the association between a library and its root folder. This object is available in API version 34.0 and later.


Standard Objects ContentFolderLink

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Salesforce CRM Content must be enabled to access ContentFolderLink.

**•** ContentFolderLink is read-only in the context of a library.

Fields

**Field Name** **Details**

```
ContentFolderId

EnableFolderStatus

ParentEntityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the folder.

This is a relationship field.

**Relationship Name**
ContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of enabling folders for the library. Valid values are:

**•** `C`  - Completed folder enablement

**•** `S`  - Started folder enablement

**•** `F`  - Failed folder enablement

This field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects ContentFolderMember

**Field Name** **Details**

**Description**
Name of the entity the folder hierarchy is linked to.

### ContentFolderMember

Defines the association between a file and a folder. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolderMember.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify ContentFolderMember, the user must be a member of the library and have permission to modify folders.

Fields

**Field Name** **Details**

```
ChildRecordId

ParentContentFolderId

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


### Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
ID of the folder the file is in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

### ContentHubItem

Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object is
available in API version 33.0 and later.

Special Access Rules

Chatter and Files Connect must be enabled for the organization.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
ContentHubRepositoryId

ContentItemSize

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


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
The size of the file or folder. Available in API version 65.0 and later.

```
ContentModifiedDate

ContentSize

Description

ExternalContentUrl

ExternalDocumentUrl

ExternalId

```

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


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
ID for the file or folder in the external data source.

```
FileExtension

FileType

IsFolder

MimeType

Name

Owner

```

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


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
Username of the content owner in the external data source.

```
ParentId

Title

UpdatedBy

```

Usage

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

**Description**
The title that appears in the content, which often differs from the `Name` of the
containing file or folder.

**Type**
string

**Properties**
Group, Nillable

**Description**
Username for the person who last updated the file.

The following SOQL query examples show how to retrieve files and folders from a Files Connect external data source. These examples
use placeholders for ID values for the repository ID and folder IDs. Before running these queries, replace the placeholders with valid ID
values for your external data source and folders.


### Standard Objects ContentHubRepository Important: You must filter queries and searches on ContentHubItem with the ContentHubRepositoryId field; for

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


Standard Objects ContentHubRepository

Special Access Rules

Chatter and Files Connect must be enabled for the organization.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DeveloperName

MasterLabel

Type

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


### Standard Objects ContentNote

**Field Name** **Details**

**•** `contenthubBox`

**•** `contenthubQuip`

### ContentNote

Represents a note created with the enhanced note-taking tool, released in Winter ’16. This object is available in API version 32.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`

Special Access Rules

**•** Notes must be enabled.

Fields

**Field** **Details**

### `Content`

```
ContentModifiedDate

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it must be base64 encoded (for
### upload) or decoded (for download). Any special characters within plain text in the Content

field must be escaped. You can escape special characters by calling
`content.escapeHtml4()` . If the input contains unsafe HTML characters or new lines,
we automatically strip them out before saving the content.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the document was modified. ContentModifiedDate updates when, for example,
the document is renamed or a new document version is uploaded.

This field is available in API version 48.0 and later.


Standard Objects ContentNote

**Field** **Details**

```
ContentSize

ContentSizeLong

FileExtension

FileType

IsReadOnly

LastViewedDate

```

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


Standard Objects ContentNote

**Field** **Details**

**Description**
The date the note was last viewed. This field is available in API version 35.0 and later.

```
LatestContentId

LatestPublishedVersionId

OwnerId

SharingPrivacy

```

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


Standard Objects ContentNote

**Field** **Details**

This field is available in API versions 41.0 and later.

```
TextPreview

Title

```

Usage

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


### Standard Objects ContentNotification

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

Fields

**Field** **Details**

```
EntityIdentifierId

EntityType

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


### Standard Objects ContentTagSubscription

**Field** **Details**

**•** `User`

```
Nature

Subject

Text

UsersId

```

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

**Description**
Text of the notification.

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


### Standard Objects ContentTaxonomy

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
UserId

### ContentTaxonomy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user following the tag on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a content
taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and
### ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.


### Standard Objects ContentTaxonomyRelatedTerm

Fields

**Field** **Details**

```
Description

Language

Name

```

SEE ALSO:

### ContentTaxonomyRelatedTerm

ContentTaxonomyTerm

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


Standard Objects ContentTaxonomyRelatedTerm

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

ContentTaxonomyTermId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that belongs to the content taxonomy.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object


### Standard Objects ContentTaxonomyTerm

Usage

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

Fields

**Field** **Details**

```
Description

DeveloperName

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


### Standard Objects ContentTaxonomyTermRelatedTerm

**Field** **Details**

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain 2 consecutive underscores

```
ExternalId

Name

```

Usage

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


Standard Objects ContentTaxonomyTermRelatedTerm

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

ContentTaxonomyTermId

ContentTaxonomyTrmRelaTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

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


### Standard Objects ContentTaxonomyTermRelationshipType

**Field** **Details**

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTrmRelaType

**Relationship Type**
Lookup

**Refers To**
### ContentTaxonomyTermRelationshipType object

```
RelatedContentTaxonomyTermId

```

Usage

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

**Refers To**
ContentTaxonomyTerm object

To relate a term to another term in a content taxonomy, use this object in addition to the ContentTaxonomyTerm object. This object
can’t be updated. You can only create and delete it.

SEE ALSO:

### ContentTaxonomyTerm ContentTaxonomyTermRelationshipType

Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled.


### Standard Objects ContentTransferEventLog

Fields

**Field** **Details**

```
ContentTaxonomyTrmRelaCatg

Description

Name

```

Usage

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

**Description**
Description of the relationship type.

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


Standard Objects ContentTransferEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

FilePreviewType

FileSize

FileType

OperationType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file preview.

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


Standard Objects ContentTransferEventLog

**Field** **Details**

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

```
RequestIdentifier

Timestamp

UserIdentifier

VersionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

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


### Standard Objects ContentUserSubscription ContentUserSubscription

Represents a subscription for a user following another user. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
SubscribedToUserId

SubscriberUserId

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


### Standard Objects ContentVersion

**Field** **Details**

**Refers To**
User

### ContentVersion

Represents a specific version of a document in Salesforce CRM content or Salesforce Files. This object is available in versions 17.0 and
later for Salesforce CRM content documents. This object is available in versions 20.0 and later for Salesforce Files.

The maximum number of versions that can be published in a 24-hour period is 200,000.

Note: Depending on how files are shared, queries on ContentDocument and ContentVersion without specifying an ID don’t
return all files a user has access to. For example, if a user only has access to a file because they have access to a record that the file
is shared with, the file won't be returned in a query such as "SELECT Id FROM ContentDocument."

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


Standard Objects ContentVersion

**•** In API version 34.0 and later, any file can be shared with libraries, whether the file originated in Chatter or in Salesforce CRM Content.

**•** [In API version 39.0 and later, custom Apex download handlers can be created that can control access to documents. See the Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)
[Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

Fields

**Field** **Details**

```
Checksum

ContentBodyId

ContentDocumentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
MD5 checksum for the file.

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


Standard Objects ContentVersion

**Field** **Details**

**Refers To**
ContentDocument

```
ContentLocation

ContentModifiedById

ContentModifiedDate

ContentSize

```

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


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the document in bytes for documents smaller than 2 GB. The value is zero for links.

In API version 66.0 and later, we recommend that you use the `ContentSizeLong` field
even for documents smaller than 2 GB.

```
ContentSizeLong

ContentUrl

Description

Division

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB. The value is zero for links.

This field is available in API version 66.0 and later.

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


Standard Objects ContentVersion

**Field** **Details**

```
ExternalDataSourceId

ExternalDocumentInfo1

ExternalDocumentInfo2

FeaturedContentBoost

```

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


Standard Objects ContentVersion

**Field** **Details**

**Description**
Read only. Designates a document as featured.

```
FeaturedContentDate

FileExtension

FileType

FirstPublishLocationId

```

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

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

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


Standard Objects ContentVersion

**Field** **Details**

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


Standard Objects ContentVersion

**Field** **Details**

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

IsLatest

IsMajorVersion

Language

```

**Type**
boolean

**Properties**
Create, Group, Defaulted on create

**Description**
Can be specified on insert of ContentVersion to automatically convert a ContentDocument
file into a ContentAsset. This field can be SOQL queried, but it can’t be edited. This field is
available in API version 38.0 and later.

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


Standard Objects ContentVersion

**Field** **Details**

Specifies the language of the labels returned. The value must be a valid user locale (language
and country), such as `de_DE` or `en_GB` . For more information on locales, see the
`Language` field on the CategoryNodeLocalization object.

`MalwareScanDate` (Beta)

`MalwareScanStatus` (Beta)

```
NegativeRatingCount

```

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


Standard Objects ContentVersion

**Field** **Details**

**Description**
Read only. The number of times different users have given the document a thumbs down.

Rating counts for the latest version are not version-specific. If Version 1 receives 10
thumbs-down votes, and Version 2 receives 2 thumbs-down votes, the
`NegativeRatingCount` on Version 2 is 12. However, rating counts are not retroactive
for prior versions. The `NegativeRatingCount` on Version 1 is 10.

```
NetworkId

Origin

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this file originated from. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

You can add a `NetworkId` only when creating a file. You can’t change or add a
`NetworkId` for an existing file.

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


Standard Objects ContentVersion

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
PathOnClient

PositiveRatingCount

PublishStatus

RatingCount

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs up.

Rating counts for the latest version are not version-specific. If Version 1 receives 10 thumbs-up
votes, and Version 2 receives 2 thumbs-up votes, the `PositiveRatingCount` on Version
2 is 12. However, rating counts are not retroactive for prior versions. The
`PositiveRatingCount` on Version 1 is 10.

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


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Total number of positive and negative ratings.

```
ReasonForChange

RecordTypeId

SharingOption

SharingPrivacy

```

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


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator access
to the file can modify this field. Default is `Visible to Anyone With Record`
`Access` . When set to `Private on Records`, the file is private on records but can be
shared selectively with others.

This field is available in API versions 41.0 and later.

```
TagCsv

TextPreview

Title

VersionData

```

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
Text used to apply tags to a content version via the API.

**Type**
string

**Properties**
Nillable, Filter,Group, Sort

**Description**
A preview of a document. Available in API version 35.0 and later.

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


Standard Objects ContentVersion

**Field** **Details**

The maximum file size you can upload via the SOAP API is 50 MB. When a document is
uploaded or downloaded via the API, it is converted to base64 and stored in `VersionData` .
This conversion increases the document size by approximately 37%. Account for the base64
conversion increase so that the file you plan to upload is less than 50 MB after conversion.

If a custom Apex download handler is active, this field is accessed from the API, and the
download is not allowed, Salesforce will return a
`CONTENT_CUSTOMIZED_DOWNLOAD_EXCEPTION` error.

```
VersionDataURL

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL used to fetch a file from the binary data endpoint. This field is only populated on
direct queries to ContentVersion, and not when queried through a related entity’s foreign
key to ContentVersion.

If available, access preview images of a file by appending a `thumb` query parameter to this
URL. For example:

```
  myContentVersion.VersionDataUrl + '?thumb=THUMB240BY180'

```

Available `thumb` parameter values are:

**•** `THUMB720BY480`  - corresponds to the `big-thumbnail` preview format

**•** `THUMB240BY180`  - corresponds to the `thumbnail` preview format

**•** `THUMB120BY90`  - corresponds to the `tiny-thumbnail` preview format

[See File Preview in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_files_preview_format.htm) _Connect REST API Developer Guide_ for additional details about file
previews.

This field can't be set for links.

This field is available in API versions 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number. The number increments with each version of the document, for example,
1, 2, 3.


Standard Objects ContentVersion

Usage

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


Standard Objects ContentVersion

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


### Standard Objects ContentVersionComment ContentVersionComment

Represents a comment on a version of a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentDocumentId

ContentVersionId

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
### ContentVersion

**Relationship Type**
Lookup


### Standard Objects ContentVersionHistory

**Field** **Details**

**Refers To**
### ContentVersion

```
UserComment

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
ID of the user who commented on the file.

### ContentVersionHistory

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

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version.


Standard Objects ContentVersionHistory

**Field** **Details**

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
DataType

Division

Field

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


### Standard Objects ContentVersionRating

**Field** **Details**

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


Standard Objects ContentVersionRating

**Field** **Details**

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

```
Rating

UserComment

UserId

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


### Standard Objects ContentWorkspace ContentWorkspace

Represents a content library. This object is available in versions 17.0 and later.

Note: This object doesn’t apply to personal libraries.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Note: create( ), update( ) and delete( ) on ContentWorkspace are supported in API version 40.0 and later only.

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


Standard Objects ContentWorkspace

**Field** **Details**

```
DeveloperName

IsRestrictContentTypes

IsRestrictLinkedContentTypes

Name

NamespacePrefix

```

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
end with an underscore, and not contain two consecutive underscores. Label
is Unique Name.

This field is available in API version 39.0 and later.

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


Standard Objects ContentWorkspace

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Limit: 15 characters. This
field is available in API version 39.0 and later.

```
RootContentFolderId

ShouldAddCreatorMembership

TagModel

WorkspaceImageId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of root folder of the library. This field is available in API version 39.0 and later.

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


Standard Objects ContentWorkspace

**Field** **Details**

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

ContentWorkspaceDoc


### Standard Objects ContentWorkspaceDoc ContentWorkspaceDoc

Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and later.

Note: This object does not apply to documents and versions in a personal library.

Supported Calls

`create()`, `delete()`, `describeSObjects()query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission in order to query and obtain content in libraries
where they have access.

**•** Customer and Partner Portal users can only edit documents if they have a Salesforce CRM Content feature license.

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


Standard Objects ContentWorkspaceDoc

**Field** **Details**

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

```
IsOwner

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether the library owns the document and determines
permissions for that document ( `true` ) or not ( `false` ). Documents can belong to
more than one library, but only one library owns the document and determines its
permissions.

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

ContentWorkspace


### Standard Objects ContentWorkspaceMember ContentWorkspaceMember

Represents a member of a content library. This object is available in API version 40.0 and later.

Manage library membership from the API.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

A user can create/update/delete memberships if they have the Manage Salesforce CRM Content admin perm or the Manage Library
permission for the library concerned.

Fields

**Field** **Details**

```
ContentWorkspaceId

ContentWorkspacePermissionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The id of the library permission or role.

This is a relationship field.

**Relationship Name**
ContentWorkspacePermission


### Standard Objects ContentWorkspacePermission

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
### ContentWorkspacePermission

```
MemberId

MemberType

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group,Namepointing, Sort

**Description**
ID of the library member (the member is either a user or a group).

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Group, User

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


Standard Objects ContentWorkspacePermission

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The ability to create permissions requires either the Manage Salesforce CRM Content admin perm or the Manage Content Permissions
user perm.

Fields

**Field** **Details**

```
Description

Name

PermissionsAddComment

PermissionsAddContent

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

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


Standard Objects ContentWorkspacePermission

**Field** **Details**

```
PermissionsAddContentOBO

PermissionsArchiveContent

PermissionsChatterSharing

PermissionsDeleteContent

PermissionsDeliverContent

PermissionsFeatureContent

```

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


Standard Objects ContentWorkspacePermission

**Field** **Details**

**Description**
Permission for user to identify any content in the library as “featured.”

```
PermissionsManageWorkspace

PermissionsModifyComments

PermissionsOrganizeFileAndFolder

PermissionsTagContent

PermissionsViewComments

```

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


### Standard Objects ContentWorkspaceSubscription

**Field** **Details**

```
Type

```

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

### ContentWorkspaceSubscription

Represents a subscription for a user following a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentWorkspaceId

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


### Standard Objects ContextParamMap

**Field** **Details**

**Refers To**
ContentWorkspace

```
UserId

### ContextParamMap

```

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

**Refers To**
User

Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ContextEntityId

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


### Standard Objects Contract

**Field** **Details**

```
MapKey

MapValue

### Contract

```

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

Represents a contract (a business agreement) associated with an Account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

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


Standard Objects Contract

**Field** **Details**

```
ActivatedById

ActivatedDate

ActivityMetricId

ActivityMetricRollupId

```

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

**Properties**
Filter, Nillable, Sort, Update

**Description**
Date and time when this contract was activated.

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


Standard Objects Contract

**Field** **Details**

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

```
AggregationStrategy

BillingAddress

BillingCity

BillingCountry

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The aggregation strategy when creating a pricing contract.

Valid value is `Cumulative` . This field is available with Revenue Cloud in API version 64.0
and later.

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


Standard Objects Contract

**Field** **Details**

```
BillingCountryCode

BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

```

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
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

```
BillingPostalCode

BillingState

BillingStateCode

BillingStreet

CompanySignedDate

CompanySignedId

```

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

**Description**
The ISO state code for the contract's billing address.

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


Standard Objects Contract

**Field** **Details**

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

```
ContractNumber

ContractTerm

CustomerSignedDate

CustomerSignedId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the contract.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of months that the contract is valid.

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


Standard Objects Contract

**Field** **Details**

**Relationship Name**
CustomerSigned

**Relationship Type**
Lookup

**Refers To**
Contact

```
CustomerSignedTitle

Description

EndDate

HasContractCotermination

IsPricingContract

```

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


Standard Objects Contract

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contract has related contract item prices ( `true` ) or if there are no
contract item prices for the contract ( `false` ). This field is available with Revenue Cloud in
API version 63.0 and later.

```
IsDeleted

LastActivityDate

LastApprovedDate

LastReferencedDate

LastViewedDate

```

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

**•** The due date of the most recently closed task associated with the record.

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


Standard Objects Contract

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` )
but didn’t view it.

```
OwnerExpirationNotice

OwnerId

Pricebook2Id

PricingSource

```

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

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

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


Standard Objects Contract

**Field** **Details**

**Description**
Source of the pricing for the contract.

Valid values are:

**•** `LastTransaction`

**•** `PriceBookListPrice` —Price Book or List Price

Available in API version 60.0 and later.

```
RecordTypeId

RenewalTerm2

RenewalTermUnit

ShippingAddress

```

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


Standard Objects Contract

**Field** **Details**

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

```
ShippingCity

ShippingCountry

ShippingCountryCode

ShippingGeocodeAccuracy

```

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


Standard Objects Contract

**Field** **Details**

**•** `Street`

**•** `Unknown`

**•** `Zip`

Available in API version 60.0 and later.

```
ShippingLatitude

ShippingLongitude

ShippingPostalCode

ShippingState

ShippingStateCode

```

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

**Description**
Details of the shipping address. The postal code maximum size is 20 characters.

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


Standard Objects Contract

**Field** **Details**

```
ShippingStreet

SourceQuoteId

SpecialTerms

StartDate

Status

```

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

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Special terms that apply to the contract.

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


Standard Objects Contract

**Field** **Details**

**Description**
The picklist of values that indicate order status. Each value is within one of two status
categories defined in `StatusCode` . For example, the status picklist may contain: Ready
to Ship, Shipped, Received as values within the Activated `StatusCode` .

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `In Approval Process`

Available in API version 60.0 and later.

```
StatusCode

UnitPriceUplift

```

Usage

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


### Standard Objects ContractContactRole

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

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactId

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


Standard Objects ContractContactRole

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
ContractId

IsDeleted

IsPrimary

Role

```

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

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

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


### Standard Objects ContractLineItem

**Field** **Details**

**Description**
Name of the role played by the Contact on this Contract, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`ContractId`, `ContactId`, and `Role` values are identical. Different contacts can play
the same role on the same contract. A contact can play different roles on the same contract.

SEE ALSO:

ContractStatus

### ContractLineItem

Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

Description

Discount

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the Asset associated with the contract line item. Must be a valid asset ID.

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


Standard Objects ContractLineItem

**Field** **Details**

**Description**
The discount for the product as a percentage.

When updating, if you specify `Discount` without specifying `TotalPrice`, the
`TotalPrice` will be adjusted to accommodate the new `Discount` value, and the
`UnitPrice` will be held constant.

If you specify both `Discount` and `Quantity`, you must also specify either
`TotalPrice` or `UnitPrice` so the system can determine which one to automatically
adjust.

```
EndDate

LastReferencedDate

LastViewedDate

LineItemNumber

ListPrice

```

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

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Update

**Description**
Automatically-generated number that identifies the contract line item.

**Type**
currency


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard pricebook or a custom pricebook. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the pricebook entry list price.

```
LocationId

ParentContractLineItemId

PricebookEntryId

Product2Id

Quantity

```

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

**Properties**
Create, Filter, Update

**Description**
Required. ID of the associated PricebookEntry.

Only exists if Product2 is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related to the contract line item.

**Type**
double


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Number of units of the contract line item (product) included in the associated service contract.

```
RootContractLineItemId

ServiceContractId

StartDate

Status

Subtotal

```

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

**Description**
The first day the contract line item is in effect.

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


### Standard Objects ContractLineOutcome

**Field** **Details**

```
TotalPrice

UnitPrice

```

Associated Objects

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


Standard Objects ContractLineOutcome

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

CaptureFrequency

ComplianceStatus

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


Standard Objects ContractLineOutcome

**Field** **Details**

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

```
ContractLineItemId

Description

EndDate

```

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

**Refers To**
ContractLineItem

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


Standard Objects ContractLineOutcome

**Field** **Details**

**Description**
The contract line outcome's data capture end date.

```
LastReferencedDate

LastViewedDate

Name

NextDataCaptureDate

OwnerId

```

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

**Properties**
Filter, Nillable, Sort

**Description**
The date of the next data capture and compliance check based on the capture frequency.
The date is auto-populated and updated after each capture

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The contract line outcome’s owner. By default, the owner is the user who created the contract
line outcome record. Its UI label is Contract Line Outcome Owner.

This field is a polymorphic relationship field.


Standard Objects ContractLineOutcome

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RecordsetFilterCriteriaId

ServiceContractId

StartDate

```

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

**Description**
The service contract associated with the contract line item and the contract line outcome.

This field is a relationship field.

**Relationship Name**
ServiceContract

**Relationship Type**
Lookup

**Refers To**
ServiceContract

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


### Standard Objects ContractLineOutcomeData

**Field** **Details**

**Description**
The contract line outcome's data capture start date.

Usage

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

### ContractLineOutcomeData ContractLineOutcomeData

Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s start
date and end date. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.


Standard Objects ContractLineOutcomeData

Fields

**Field** **Details**

```
CalculatedValue

CaptureDate

ContractLineOutcomeId

KeyPerformanceIndicator

LastReferencedDate

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
ContractLineOutcome

**Relationship Type**
Lookup

**Refers To**
ContractLineOutcome

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key performance indicators (fields or asset attributes) that define the contract line
outcome’s compliance status.

**Type**
dateTime


Standard Objects ContractLineOutcomeData

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last modified. Its UI label
is Last Modified Date.

```
LastViewedDate

Name

Value

```

Associated Objects

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


### Standard Objects ContractStatus ContractStatus

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

MasterLabel

SortOrder

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


### Standard Objects ContractTag

**Field** **Details**

**Description**
Number used to sort this value in the contract status picklist. These numbers are not
guaranteed to be sequential, as some previous contract status values might have been
deleted.

```
 StatusCode

```

Usage

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

### ContractTag

Associates a word or short phrase with a Contract.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects ContractTag

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

ContractTag stores the relationship between its parent TagDefinition and the Contract being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.


### Standard Objects ConvAnalysisSummary

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

Error

FlowIdentifier

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

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The error message sent by Hawking when a refresh fails.

**Type**
string


Standard Objects ConvAnalysisSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The UUID used to track the Hawking flow ID.

```
RefreshDate

Status

TotalCalls

TotalMentions

```

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

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of mentions or keywords that were analyzed.


### Standard Objects ConvAnalysisTopic ConvAnalysisTopic

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

ConvAnalysisSummaryId

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

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis summary associated with the topic.

This field is a relationship field.

**Relationship Name**
ConvAnalysisSummary


Standard Objects ConvAnalysisTopic

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisSummary (the parent object)

```
GenerationsIdentifier

Keyword

MentionCount

Order

Summary

```

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

**Description**
Required. A numerical value used to sort topics in a sequence.

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. A detailed explanation of the topic.


Standard Objects ConvAnalysisTopic

**Field** **Details**

```
Title

TopicSentiment

TotalCalls

TotalCallsForCategoryKeyword

TotalMentionsForCategoryKeyword

TurnIdentifier

```

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

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of mentions analyzed for `category:keyword` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects ConvAnalysisTopicEntry

**Field** **Details**

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

**Description**
The unique identifier of the voice or video call that corresponds to the entry.

This field is a polymorphic relationship field.

**Relationship Name**
Call

**Refers To**
VideoCall, VoiceCall


### Standard Objects Conversation

**Field** **Details**

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

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects Conversation

Fields

**Field** **Details**

```
ConversationChannelId

ConversationIdentifier

EndTime

Name

StartTime

```

**Type**
reference

**Properties**
Filter, Group, idLookup, Sort

**Description**
The record ID of the channel used to initialize the conversation. This can either be a messaging
channel for the Messaging product or a call center for the Service Cloud Voice product.
Available in API version 50.0 and later.

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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a conversation starts.


### Standard Objects ConversationApiLog ConversationApiLog

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

Operation

OwnerId

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


Standard Objects ConversationApiLog

**Field** **Details**

**Description**
Owner ID that triggered the Conversation API log.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
RequestedById

RequestedDate

RequestedEntityIdentifier

RequestedEntityType

```

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

**Properties**
Create, Filter, Group, Sort

**Description**
The entity ID being created, updated, or deleted.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entity being created, updated, or deleted.

Possible values are:


### Standard Objects ConversationContextEntry

**Field** **Details**

**•** `MessagingEndUser` —Messaging End User

```
Status

```

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

Fields

**Field** **Details**

### `ConversationContextEntryName`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated number of the entry.


### Standard Objects ConversationChannelDefinition

**Field** **Details**

```
 CustomDetailContextKey

 CustomDetailContextValue

 ParentId

```

Associated Objects

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

### ConversationChannelDefinition

Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel
for Messaging and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ConversationChannelDefinition

Special Access Rules

To access this object, interaction service must be configured. Access to standard objects requires Salesforce admin privileges or the
Customize Application permission.

Fields

**Field** **Details**

```
CapabilitiesSupportsCustomChannelParameters

CapabilitiesSupportsDoubleOptInConsent

CapabilitiesSupportsExplicitConsent

CapabilitiesSupportsImplicitConsent

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

**Description**
Indicates whether the channel supports ( _`true`_ ) the Explicit Opt-In consent level. This field
is optional.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Implicit Opt-In consent level. This value
is required and must always be set to true. The default value is false.


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
CapabilitiesSupportsIsoCountryCode

CapabilitiesSupportsKeywords

ConnectedAppOauthLink

ConnectedAppType

ConsentOwner

```

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

**Type**
picklist


Standard Objects ConversationChannelDefinition

**Field** **Details**

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

```
ConversationVendorInfoId

customEventChnlAddrIdField

CustomEventPayloadField

```

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


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the `Payload` field in
the format _`<orgNamespace>`_ __ _`<CustomFieldName>`_ __c. This is the API name of
the custom Payload field in the custom platform event. For example, devorg__Payload__c.

```
customEventRecipientField

CustomEventTypeField

CustomIconId

```

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


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Refers To**
StaticResource

```
CustomPlatformEvent

CustomerConnectedAppOauthLink

DeveloperName

EventCapabilitiesIsInboundAcknwOptionExposed

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
app. For example, Partner1_ChannelDefinition1, where Partner1 is the prefix and
ChannelDefinition1 is the given name.

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


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
EventCapabilitiesIsProgressIndicatorOptExposed

EventCapabilitiesIsRoutingWorkResultSupported

EventCapabilitiesIsTypingIndicatorOptionHidden

IsConferenceSupported

```

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
whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

This field is available in API version 65.0 and later. Use this field instead of
`IsTypingIndicatorDisabled` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports conferencing for Bring Your Own Channel ( `true` ),
or not ( `false` ). With conferencing, more than two participants are allowed in a Messaging
session. The default is `false` .

This field is available in API version 64.0 and later.


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
IsInboundReceiptsEnabled

IsRoutingWorkResultEnabled

IsTypingIndicatorDisabled

MasterLabel

```

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

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings ( `true` ) or
whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsTypingIndicatorOptionHidden` instead.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Description**
The UI label name for the custom metadata type object in the API. This name appears in
several places in the UI, so include the partner channel name for easy identification. For
example, Channel Definition 1.

```
MaxParticipantsForCnfrOverride

NamespacePrefix

RoutingOwner

```

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
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

`NamespacePrefix` is null if the publisher is Salesforce.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage routing for Bring Your Own Channel for Messaging
or Bring Your Own Channel for CCaaS.


### Standard Objects ConversationEntry

**Field** **Details**

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce` .

For example, if set to _`Salesforce`_, routing is managed by the Salesforce system. If set to
_`Partner`_, routing is managed by the partner’s system.

For Bring Your Own Channel for Messaging, this value must be set to _`Salesforce`_ .

### ConversationEntry

Represents a message or event in a voice call or a standard or enhanced messaging session. This object is available in API version 43.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To use the ConversationEntry object, enable the Access Conversation Entries user permission, which is available in API version 50.0 and
later. Earlier versions do not require permissions.

Fields

**Field** **Details**

```
ActorId

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


Standard Objects ConversationEntry

**Field** **Details**

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser, User

```
ActorName

ActorType

ClientDuration

ClientTimestamp

```

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


Standard Objects ConversationEntry

**Field** **Details**

**Description**
The timestamp sent by the client when it generated the entry. This field is available in API
version 51.0 and later.

```
ConversationId

EntryEndTime

EntryTime

EntryTimeMilliSecs

```

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

**Properties**
Create, Filter, Sort

**Description**
The timestamp of this entry in the chat history.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The milliseconds value for the time when an entry was received by the server. Note that the
related `EntryTime` field does not provide millisecond accuracy. This field is available in
API version 51.0 and later.


Standard Objects ConversationEntry

**Field** **Details**

```
EntryType

HasAttachments

Message

MessageDeliverTime

```

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


Standard Objects ConversationEntry

**Field** **Details**

**Description**
Unused field reserved for future use.

```
MessageIdentifier

MessageReadTime

MessageSendTime

MessageStatus

MessageStatusCode

```

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

**Description**
The status of the message sent by the author. The valid values include:

**•** `Delivered`

**•** `Error`

**•** `Pending`

**•** `Read`

**•** `Sent`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ConversationParticipant

**Field** **Details**

**Description**
The code associated with a message status. `MessageStatusCode` is only populated
when a message is undeliverable

```
Seq

ServerReceivedTimestamp

```

Usage

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

In standard SMS, WhatsApp, and Facebook Messenger channels, a ConversationEntry record is created for each message sent by a
messaging end user or an agent, bot, or automation. Each ConversationEntry record is associated with a MessagingSession record, which
represents the interaction between the messaging end user and the business. Access and work with ConversationEntry records like any
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


Standard Objects ConversationParticipant

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AppType

ConversationId

JoinedTime

LastActiveTime

LeftTime

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


### Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

```
Name

ParticipantContext

ParticipantEntityId

ParticipantKey

ParticipantRole

```

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

**Description**
The ID of the record connected to this participant record, such as a Contact, Messaging End
User, or User record.

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


Standard Objects ConvIntelligenceSignalRule

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.

Fields

**Field** **Details**

```
ActionType

ActionValue

ConversationChannelId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Required. Action to take based on the conversation intelligence signal detected during a
conversation. Possible values are:

Possible values are:

**•** `AlertSupervisor` –Sends an alert to the supervisor.

**•** `AlertSupervisorAndAgent` –Sends an alert to the rep and supervisor.

**•** `LaunchFlow` –Triggers an auto-launched flow. If set, also set `ActionValue` .

**•** `LaunchNBA` –Recommends the next best action to the rep.

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


Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Description**

Required. ID ( `ChannelAddressIdentifier` ) of the Messaging channel or name
( `InternalName` ) of the Voice channel.

This field is a polymorphic relationship field.

**Relationship Name**
ConversationChannel

**Refers To**
CallCenter, MessagingChannel

```
Criteria

DeveloperName

IsActive

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Filter logic applied to the rule conditions (subrules). For example, ((1 AND 2) OR
3). The numbers in the formula are derived from the
`ConvIntelligenceSignalSubrule.Order` value plus 1. For example, filter logic
(1 AND 2) is calculated by adding the first condition ( `Order` =0) with the second condition
( `Order` =1).

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


### Standard Objects ConvIntelligenceSignalSubRule

**Field** **Details**

```
ParticipantRole

Service

```

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

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.


Standard Objects ConvIntelligenceSignalSubRule

Fields

**Field** **Details**

```
ConvIntelligenceSignalRuleId

OperandValue

Operator

Order

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


### Standard Objects ConvMessageSendRequest

**Field** **Details**

`Type` values, the maximum value is 4. This value is used when applying filter logic to the
rule.

```
Type

```

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

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
Indicates whether the message can be sent only at certain times.

Possible values are:

**•** `Any` —Send the message regardless of whether the messaging user is engaged in an
active messaging session with the business.

**•** `Closed` —Send the message unless the messaging user is engaged in a messaging
session with a status other than Error or Ended, in which case it’s never sent.

**•** `NonActive` —Send the message unless the messaging user is engaged in a messaging
session with a status of Active, in which case it’s never sent.

```
CommSubscriptionId

CompletedDate

FailedMessageCount

FailedMessageErrorReasons

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related communication subscription, if applicable. This field is a relationship
field that refers to CommSubscription.

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


Standard Objects ConvMessageSendRequest

**Field** **Details**

```
FailedMessageIdentifiers

FailedMeuPlatformKeys

InProgressMessageCount

InProgressMessageIdentifiers

InProgressMessagingEndUserIds

InProgressMessagingSessionIds

```

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

**Description**
A list of platform keys for messaging end users with messages that failed to send. Available
in API version 65.0 and later.

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


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
A list of IDs of messaging sessions with messages that are being sent. Available in API version
65.0 and later.

```
InProgressMeuPlatformKeys

MessageDefinition

MessageDefinitionParameters

Name

PendingMessageCount

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that are being sent. Available
in API version 65.0 and later.

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


Standard Objects ConvMessageSendRequest

**Field** **Details**

```
PendingMessageEndUserIds

PendingMeuPlatformKeys

PendingMessageIdentifiers

RequestConsentType

RequestStatus

```

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

**Description**
A list of platform keys of the messaging end users with pending messages. Available in API
version 65.0 and later.

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


Standard Objects ConvMessageSendRequest

**Field** **Details**

**•** `Completed`

**•** `Pending`

**•** `In Progress` —The system is actively trying to send the message. If a message can’t
be sent, the RequestStatus returns to Pending and sending is tried again later.

```
RequestType

SessionLongevityPreference

ShouldEnforceChannelConsent

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of request.

Possible values are:

**•** `SendNotificationMessages`

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


Standard Objects ConvMessageSendRequest

**Field** **Details**

to customize a flow to send the message to both implicitly opted-in users and explicitly
opted-in users.

```
SuccessMessageCount

SuccessMessageIdentifiers

SuccessMeuPlatformKeys

TotalMessageCount

```

Usage

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

**Properties**
Nillable

**Description**
A list of IDs of the messages that were sent.

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


### Standard Objects ConversationVendorInfo ConversationVendorInfo

This setup object connects the partner vendor system to the Service Cloud feature. For example, for Service Cloud Voice, this object
contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For Bring Your Own Channel
for Messaging this object contains information about the partner messaging system, and for Bring Your Own Channel for CCaaS, this
object contains information about the CCaaS partner system. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object requires an add-on license for Service Cloud Voice for Partner Telephony or Digital Engagement.

Fields

The fields in the ConversationVendorInfo object apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Service Cloud Voice telephony model setup or is applied differently by different partner systems,
this is stated in the field description.


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


### Standard Objects CorsWhitelistEntry CorsWhitelistEntry

Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources
from that Salesforce org.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

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


Standard Objects CorsWhitelistEntry

**Field Name** **Details**

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

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

```
MasterLabel

NamespacePrefix

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


### Standard Objects Coupon

**Field Name** **Details**

```
UrlPattern

```

Usage

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


Standard Objects Coupon

Special Access Rules

The Coupon object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CouponCode

CurrencyIsoCode

Description

EndDateTime

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Coupon code for the coupon. A buyer can use the coupon code to qualify for a promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

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


Standard Objects Coupon

**Field** **Details**

```
LastViewedDate

Name

OwnerId

PromotionId

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
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the coupon.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this coupon.

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
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the coupon.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup


Standard Objects Coupon

**Field** **Details**

**Refers To**
Promotion

```
RedemptionLimitAllBuyers

RedemptionLimitPerBuyer

StartDateTime

Status

```

Associated Objects

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


### Standard Objects CouponCodeRedemption

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

Fields

**Field** **Details**

```
Buyer

CouponId

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
### Coupon

**Relationship Type**
Lookup

**Refers To**
### Coupon


### Standard Objects CreditMemo

**Field** **Details**

```
Name

OwnerId

Transaction

### CreditMemo

```

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

**Refers To**
Group, User

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


Standard Objects CreditMemo

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)

Fields

**Field** **Details**

```
AppType

Balance

BillToContactId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field that indicates which Salesforce application generated the credit memo.

Possible values are:

**•** `Commerce Cloud`

**•** `Revenue Cloud`

This field is available in API versions 54.0 to 55.0

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


Standard Objects CreditMemo

**Field** **Details**

```
BillingAccountId

CreationMode

CreditDate

CreditMemoNumber

```

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

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the credit memo originated in Salesforce or an external system.

Possible values are:

**•** `External`

**•** `Salesforce`

This field is available in API version 55.0 and later.

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


Standard Objects CreditMemo

**Field** **Details**

```
CurrencyIsoCode

Description

DocumentNumber

EffectiveDate

ExternalReference

```

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


Standard Objects CreditMemo

**Field** **Details**

```
ExternalReferenceDataSource

LastReferencedDate

LastViewedDate

NetCreditsApplied

OwnerId

```

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

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible that this record was only referenced ( `LastReferencedDate` ) and not viewed.

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


Standard Objects CreditMemo

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ReferenceEntityId

SourceAction

Status

```

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

**Refers To**
Invoice, Order

This field is available in API version 53.0 and later.

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


Standard Objects CreditMemo

**Field** **Details**

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

```
TotalAdjustmentAmount

TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

TotalAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s adjustment lines.

This field is a calculated field.

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


Standard Objects CreditMemo

**Field** **Details**

This field is a calculated field.

```
TotalAmountWithTax

TotalChargeAmount

TotalChargeAmountWithTax

TotalChargeTaxAmount

TotalCreditAmountApplied

```

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

**Description**
Sum of `TotalAmount` values for the credit memo’s charge lines.

This field is a calculated field.

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


### Standard Objects CreditMemoAddressGroup

**Field** **Details**

```
TotalCreditAmountUnapplied

 TotalTaxAmount

```

Associated Objects

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

This field is a calculated field.

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


Standard Objects CreditMemoAddressGroup

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)

Fields

**Field** **Details**

```
Address

City

Country

CreditMemoAddressGroupNumber

CreditMemoId

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer’s address.

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


Standard Objects CreditMemoAddressGroup

**Field** **Details**

**Description**
ID of the credit memo associated with the address group.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

```
CurrencyIsoCode

GeocodeAccuracy

LastReferencedDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

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


Standard Objects CreditMemoAddressGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this address group.

```
LastViewedDate

Latitude

Longitude

PostalCode

State

Street

```

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

**Description**
Latitude of the buyer’s address.

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


### Standard Objects CreditMemoInvApplication

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s street number and name.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoAddressGroupHistory on page 63**
History is available for tracked fields of the object.

### CreditMemoInvApplication

Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)

Fields

**Field** **Details**

```
Amount

AppliedDate

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of the credit memo that was applied to or unapplied from the invoice.

**Type**
dateTime


Standard Objects CreditMemoInvApplication

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the credit memo was applied. If the credit memo invoice application's type
is `Unapplied`, this value is inherited from the Applied date of the credit memo referenced
in the AssociatedLineId.

```
AssociatedLineId

CreditMemoBalance

CreditMemoId

```

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

**Refers To**
CreditMemoInvApplication

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


Standard Objects CreditMemoInvApplication

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CreditMemo

```
CreditMemoInvoiceNumber

Date

Description

EffectiveDate

HasBeenUnapplied

```

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


Standard Objects CreditMemoInvApplication

**Field** **Details**

Possible values are:

**•** `NA`

**•** `No`

**•** `Yes`

```
ImpactAmount

InvoiceBalance

InvoiceId

Type

```

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

**Properties**
Filter, Nillable, Sort

**Description**
The balance of the credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.

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


### Standard Objects CreditMemoLine

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the credit memo line application was generated because of an apply
action (application) or an unapply action (unapplication).

Possible values are:

**•** `Applied`

**•** `Unapplied`

```
UnappliedDate

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when this application was unapplied from the target invoice.

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

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)


Standard Objects CreditMemoLine

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentAmountWithTax

AdjustmentTaxAmount

BillingAddressId

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


Standard Objects CreditMemoLine

**Field** **Details**

```
ChargeAmount

ChargeAmountWithTax

ChargeTaxAmount

CreditMemoId

CurrencyIsoCode

```

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


Standard Objects CreditMemoLine

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo line.

The default value is USD.

```
Description

EndDate

LineAmount

Name

Product2Id

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo line.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memos made from a time-based service, the end date of the line item being
credited.

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


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
The product or service being credited in the credit memo line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ReferenceEntityItemId

ReferenceEntityItemType

ReferenceEntityItemTypeCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order product or invoice line corresponding to this credit memo line.

This field is a polymorphic relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary, OrderProduct, InvoiceLine

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


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
The type of object that generated the credit memo line.

Possible values are:

**•** `Charge`

**•** `Product`

```
RelatedLineId

ShippingAddressId

StartDate

```

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

**Refers To**
CreditMemoLine

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


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
For credit memo lines generated from a time-based service, the first date of the billing for
the service.

```
Status

TaxAmount

TaxCode

TaxDocumentNumber

TaxEffectiveDate

```

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


Standard Objects CreditMemoLine

**Field** **Details**

```
TaxName

TaxRate

TotalAmount

TotalAmountWithTax

TaxStatus

```

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

**Description**
The total amount of the credit memo line before any applicable tax.

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


Standard Objects CreditMemoLine

**Field** **Details**

```
TaxTransactionNumber

TaxTreatmentId

 Type

```

Associated Objects

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

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

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


### Standard Objects Crisis

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

Special Access Rules

To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

Fields

**Field** **Details**

### `CrisisType`

```
Description

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


Standard Objects Crisis

**Field** **Details**

**Description**
The crisis description.

```
EndDate

LastReferencedDate

LastViewedDate

Name

OwnerId

StartDate

```

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


### Standard Objects CronJobDetail

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the crisis started.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CrisisHistory (API version 49.0)**
History is available for tracked fields of the object.

**CrisisOwnerSharingRule**

Sharing rules are available for the object.

**CrisisShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### CronJobDetail

Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
JobType

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


### Standard Objects CronTrigger

**Field** **Details**

**•** `4` —Reporting Snapshot

**•** `6` —Scheduled Flow

**•** `7` —Scheduled Apex

**•** `8` —Report Run

**•** `9` —Batch Job

**•** `A` —Reporting Notification

```
Name

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the associated scheduled job.

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


Standard Objects CronTrigger

**Field** **Details**

See `[schedule(jobName, cronExpression, schedulableClass)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexref/apex_methods_system_system.htm)` in the
_Apex Reference Guide_ .

```
CronJobDetailId

EndTime

NextFireTime

OwnerId

PreviousFireTime

```

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


Standard Objects CronTrigger

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time the job ran. `null` if the job has not run before current local
time.

```
StartTime

State

TimesTriggered

```

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

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this job has been triggered.


### Standard Objects CryptoProdCatgWalletGroup

**Field** **Details**

```
TimeZoneSidKey

```

Usage

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

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object has read, create, update, delete, modify all, and view all access.

Fields

**Field** **Details**

```
CryptoWalletGroupId

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


Standard Objects CryptoProdCatgWalletGroup

**Field** **Details**

**Refers To**
CryptoWalletGroup

```
LastReferencedDate

LastViewedDate

Name

ProductCategoryId

```

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


### Standard Objects CspTrustedSite

**Field** **Details**

```
Status

Type

### CspTrustedSite

```

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

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CspTrustedSite

**Field** **Details**

**Description**
Indicates whether this CspTrustedSite can access the user’s camera. The default value is
`false` .

This field takes effect only when the `enablePermissionsPolicy` field equals `true`
and the `grantCameraAccess` field equals `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

```
CanAccessMicrophone

Context

Description

```

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

**Type**
textarea


Standard Objects CspTrustedSite

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the trusted URL. Limit: 255 characters.

```
DeveloperName

EndpointUrl

IsActive

IsApplicableToConnectSrc

```

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

To reduce repetition, you can use the wildcard character `*` (asterisk). For example,
`*.example.com` . For a third-party API, the URL must begin with https://. For example,
`https://example.com` . For a WebSocket connection, the URL must begin with wss://.
For example, `wss://example.com` .

Otherwise, the URL cannot be malformed. Examples of malformed URLs that fail a syntax
check are `malformed^url.example.com`, and
`https://{subdomain}.example.com` .

To add a URL based on parameters, build the URL before you update the `EndpointUrl`
field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite is active.

**Type**
boolean


Standard Objects CspTrustedSite

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load URLs using script interfaces from this trusted URL.

```
IsApplicableToFontSrc

IsApplicableToFrameSrc

IsApplicableToImgSrc

IsApplicableToMediaSrc

IsApplicableToStyleSrc

```

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

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load resources contained in `<iframe>` elements from this trusted URL.

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


### Standard Objects CspViolationEventLog

**Field** **Details**

**Description**
Indicates whether Lightning components can load style sheets from this trusted URL.

```
Language

MasterLabel

NamespacePrefix

```

Usage

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


Standard Objects CspViolationEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BlockedUri

BlockedUriDomain

ColumnNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The full string of the blocked resource. If the call to the blocked resource used a URL,
`BLOCKED_URI` is the full URL. Or,for violations with a `DIRECTIVE` of `script-src`
directives, `inline` or `eval` .

**Examples**

**•** https://www.example.com/images/picture.png

**•** file://host1:0002/media/video.mp4

**•** inline

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow resources to be loaded from
the `BLOCKED_URI`, `BLOCKED_URI_DOMAIN` is the `endpointUrl` value to add or
[update in the CspTrustedSite Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The column number in the document or worker script at which the violation occurred. This
value is relevant only when `DIRECTIVE` is `script-src` .

For those violations, use this value with `LINE_NUMBER` to identify the location of the
violation.


Standard Objects CspViolationEventLog

**Field** **Details**

**Example**

```
Context

Directive

Disposition

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content security policy (CSP) context for the request. The CSP context controls which
[pages can load content from a CspTrustedSite.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

CSP violation events capture details about blocked resource requests from only Lightning
Experience pages, this value is always `Lightning` .

**Type**
string

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


Standard Objects CspViolationEventLog

**Field** **Details**

```
LineNumber

RequestIdentifier

ResourceSample

Source

SourceFile

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

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


### Standard Objects CurrencyType

**Field** **Details**

```
Timestamp

UniqueIdentifier

```

Usage

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
A string identifier for the CSP violation.

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


Standard Objects CurrencyType

Fields

**Field** **Details**

```
ConversionRate

DecimalPlaces

IsActive

IsCorporate

IsoCode

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


### Standard Objects CustExpIntlTransfSetup

**Field** **Details**

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter
currency ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` .
Must be unique within your organization. Label is **Currency ISO Code** .

Usage

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

Fields

**Field** **Details**

```
DataSourceChannelName

DataSourceChannelType

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


Standard Objects CustExpIntlTransfSetup

**Field** **Details**

**Description**
Specifies the channel type as standard or custom.

Possible values are:

**•** `Custom`

**•** `Standard`

The default value is `Standard` .

```
IsDataProcessingPaused

IsEnabled

LastReferencedDate

LastViewedDate

```

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


### Standard Objects CustomBrand

**Field** **Details**

```
Name

ProcessingStartDate

### CustomBrand

```

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

Fields

**Field Name** **Details**

```
ParentId

```

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


### Standard Objects CustomBrandAsset

**Field Name** **Details**

ID, the branding applies to the organization that it is accessed through, and so
on. Label is `Branded Entity ID` .

Usage

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


Standard Objects CustomBrandAsset

**Field Name** **Details**

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


Standard Objects CustomBrandAsset

**Field Name** **Details**

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

**•** `MediumLogoAssetId` —Featured topic images. Label is `Medium`
`logo asset image` .

```
AssetSourceId

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


Standard Objects CustomBrandAsset

**Field Name** **Details**

**•** `LoginLogoImageId`

**•** `LargeLogoImageId`

**•** `SmallLogoImageId`

ID of the content asset if the value of the `AssetCategory` is:

**•** `LogoAssetId`

**•** `LargeLogoAssetId`

**•** `MediumLogoAssetId`

```
CustomBrandId

ForeignKeyAssetId

TextAsset

```

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


### Standard Objects CustomFieldDisplayValue

Usage

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

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

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


Standard Objects CustomFieldDisplayValue

**Field** **Details**

```
CustomFieldDisplayId

Name

PickListApiValue

```

Usage

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


### Standard Objects CustomHelpMenuItem CustomHelpMenuItem

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

MasterLabel

ParentId

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


### Standard Objects CustomHelpMenuSection

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
### CustomHelpMenuSection

```
SortOrder

```

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

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
### CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

Fields

**Field** **Details**

```
DeveloperName

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


Standard Objects CustomHelpMenuSection

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

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
