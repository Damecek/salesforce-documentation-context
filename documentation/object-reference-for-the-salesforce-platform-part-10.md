**Refers To**
LoginGeo

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the record of the user’s successful or unsuccessful login attempt.

This is a relationship field.

**Relationship Name**
LoginHistory

**Relationship Type**
Lookup

**Refers To**
LoginHistory

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The identity verification security policy or setting. The label is Triggered By.
Available values are:


Standard Objects VerificationHistory

**Field Name** **Details**

**•** `CustomApex` —Identity verification made by a verification Apex method.

**•** `DeviceActivation` —Identity verification required for users logging in
from an unrecognized device or new IP address. This verification is part of
Salesforce’s risk-based authentication.

**•** `EnableLightningLogin` —Identity verification required for users
enrolling in Lightning Login. This verification is triggered when the user
attempts to enroll. Users are eligible to enroll if they have the Lightning Login
User user permission and the org has enabled Allow Lightning Login in
Session Settings.

**•** `ExtraVerification` —Reserved for future use.

**•** `HighAssurance` —High assurance session required for resource access.
This verification is triggered when the user tries to access a resource, such as
a connected app, report, or dashboard, that requires a high-assurance session
level.

**•** `LightningLogin` —Identity verification required for internal users logging
in via Lightning Login. This verification is triggered when the enrolled user
attempts to log in. Users are eligible to log in if they have the Lightning Login
User user permission and have successfully enrolled in Lightning Login. Also,
from Session Settings in Setup, Allow Lightning Login must be enabled.

**•** `PageAccess` —Identity verification required for users attempting to
perform an action, such as changing an email address or adding a verification
method for multi-factor authentication (MFA).

**•** `PasswordlessLogin` —Identity verification required for customers
attempting to log in to an Experience Cloud site that is set up for passwordless
login. The admin controls which registered verification methods can be used,
for example, email, SMS, Salesforce Authenticator, or TOTP.

**•** `ProfilePolicy` —Session security level required at login. This verification
is triggered by the Session security level required at login setting on the user’s
profile.

**•** `TwoFactorAuthentication` —Multi-factor authentication (formerly
called two-factor authentication) required at login. This verification is triggered
by the Multi-Factor Authentication for User Interface Logins user permission
assigned to a custom profile. Or the user permission is included in a
permission set that is assigned to a user.

```
Remarks

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The text the user sees on the page or in Salesforce Authenticator when prompted
to verify identity. For example, if identity verification is required for a user’s login,
the user sees “You’re trying to Log In to Salesforce.” In this case, the Remarks
value is “Log In to Salesforce.” But if the Activity value is Apex, the Remarks value


Standard Objects VerificationHistory

**Field Name** **Details**

is a custom description passed by an Apex method. If the user is verifying identity
using Salesforce Authenticator, the custom description also appears in the app.
If the custom description isn’t specified, the value is the name of the Apex method.
The label is Activity Message.

```
ResourceId

SourceIp

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the `Activity` value is ConnectedApp, the `ResourceId` value is the ID
of the connected app. The label is Connected App ID.

This is a relationship field.

**Relationship Name**
Resource

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The IP address of the machine from which the user attempted the action that
requires identity verification. For example, the IP address of the machine from
where the user tried to log in or access reports. If it’s a non-login action that
required verification, the IP address can be different from the address from where
the user logged in. This address can be an IPv4 or IPv6 address.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the identity verification attempt. Available values are:

**•** `AutomatedSuccess` —Salesforce Authenticator approved the request
for access because the request came from a trusted location. After users
enable location services in Salesforce Authenticator, they can designate
trusted locations. When a user trusts a location for a particular activity, such
as logging in from a recognized device, that activity is approved from the
trusted location for as long as the location is trusted.


Standard Objects VerificationHistory

**Field Name** **Details**

**•** `Denied` —The user denied the approval request in the authenticator app,
such as Salesforce Authenticator.

**•** `FailedGeneralError` —An error caused by something other than an
invalid verification code, too many verification attempts, or authenticator
app connectivity.

**•** `FailedInvalidCode` —The user entered an invalid verification code.

**•** `FailedInvalidPassword` —The user entered an invalid password.

**•** `FailedPasswordLockout` —The user attempted to enter a password
too many times.

**•** `FailedTooManyAttempts` —The user attempted to verify identity too
many times. For example, the user entered an invalid verification code
repeatedly.

**•** `Initiated` —Salesforce initiated identity verification but hasn’t yet
challenged the user.

**•** `InProgress` —Salesforce challenged the user to verify identity and is
waiting for the user to respond or for Salesforce Authenticator to send an
automated response.

**•** `RecoverableError` —Salesforce can’t reach the authenticator app to
verify identity, but it continues to retry.

**•** `ReportedDenied` —The user denied the approval request in the
authenticator app, such as Salesforce Authenticator, and also flagged the
approval request to report to an administrator.

**•** Succeeded—The user’s identity was verified.

```
UserId

VerificationMethod

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user verifying identity.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects VerificationHistory

**Field Name** **Details**

**Description**
The method by which the user attempted to verify identity in the verification
event. The label is Method. Available values are:

**•** `BuiltInAuthenticator` —A built-in authenticator set up on the user’s
device, such as Touch ID or Windows Hello, generated the required
credentials. This value is available in API version 53.0 and later.

**•** `Email` —Salesforce sent an email with a verification code to the address
associated with the user’s account.

**•** `EnableLL` —Salesforce Authenticator sent a notification to the user’s mobile
device to enroll in Lightning Login. This value is available in API version 38.0
and later.

**•** `LL` —Salesforce Authenticator sent a notification to the user’s mobile device
to approve login via Lightning Login. This value is available in API version
38.0 and later.

**•** `PwlessPasskey` (beta)—Salesforce prompted the user to use a passkey
to perform passwordless login. This value is available in API version 66.0 and
later.

Passwordless login with passkeys is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified](https://www.salesforce.com/company/legal/agreements/)
[Pilot Agreement if executed by Customer, and applicable terms in the Product](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
discretion.

**•** `SalesforceAuthenticator` —Salesforce Authenticator sent a
notification to the user’s mobile device to verify account activity.

**•** `Sms` —Salesforce sent a text message with a verification code to the user’s
mobile device. SMS messaging requires a Salesforce add-on license for Identity
Verification Credits.

**•** `TempCode` —A Salesforce admin or a user with the Manage Multi-Factor
Authentication in User Interface permission generated a temporary verification
code for the user. This value is available in API version 37.0 and later.

**•** `Totp` —An authenticator app generated a time-based, one-time password
(TOTP) on the user’s mobile device.

**•** `U2F` —A U2F security key generated required credentials for the user. This
value is available in API version 38.0 and later.

```
VerificationTime

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the identity verification attempt, for example,
`7/19/2025, 3:19:13 PM PDT.` The time zone is based on GMT. The
label is Time.


### Standard Objects VisualforceAccessMetrics

Usage

Here are two examples queries that you can perform on VerificationHistory.

**Query** **String**

Show verification history for a user’s login record `SELECT Activity, EventGroup, Policy,`

```
                             Remarks, Status, UserId,VerificationMethod,

                             VerificationTime FROM VerificationHistory

                             WHERE LoginHistoryId = '0YaD000#########'

```

Get detailed geographic location information for a user’s verification
attempt

### VisualforceAccessMetrics

Represents summary statistics for Visualforce pages.

Supported Calls

```
SELECT City, CountryIso, Latitude,

Longitude, PostalCode FROM LoginGeo WHERE

LoginGeoId = '0LE###############'

```

`count()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, to access VisualforceAccessMetrics, users must have the Customize Application permission.

Fields

**Field** **Details**

```
ApexPageId

```

**Type**
reference

**Properties**
Aggregate, Filter, Group, Sort

**Description**
The ID of the Visualforce page.

This is a relationship field.

**Relationship Name**
ApexPage

**Relationship Type**
Lookup

**Refers To**
ApexPage


Standard Objects VisualforceAccessMetrics

**Field** **Details**

```
ProfileId

DailyPageViewCount

MetricsDate

LogDate

```

Usage

**Type**
reference

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The ID of the use who viewed the Visualforce page.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of views received by the specified Visualforce page.

**Type**
date

**Properties**
Aggregate, Filter, Group, Sort

**Description**
The date the metrics are queried.

**Type**
date

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The most recent page access date.

Use this object to query information on the Visualforce pages in your org.

```
SELECT ApexPageId, DailyPageViewCount, Id, ProfileId, MetricsDate, LogDate FROM

VisualforceAccessMetrics

```


### Standard Objects VisualforceRequestEventLog VisualforceRequestEventLog

Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI). This object is available
in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

Fields

**Field** **Details**

```
ClientIp

ControllerType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of controller that’s used by the requested Visualforce page.

Possible values are:

**•** `0` —Not Specified

**•** `1` —Standard

**•** `2` —Standard Set

**•** `3` —Custom

**•** `4` —Java

**•** `5` —Spring


Standard Objects VisualforceRequestEventLog

**Field** **Details**

```
CpuTime

DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

HttpMethod

```

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
Indicates how much activity is occurring in the database. A high value for this field suggests
that adding indexes or filters on your queries benefits performance.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: `GET`, `POST`, `PUT`, and so on.


Standard Objects VisualforceRequestEventLog

**Field** **Details**

```
IsAjaxRequest

IsFirstRequest

LoginKey

ManagedPackageNamespace

PageName

QueryString

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The value is `true` if the request is a partial page request. The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`1` if this page is the first Visualforce transaction in the request, or `0` if it isn't. The default
value is `0` .

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
Filter, Group, Nillable, Sort

**Description**
If the page is part of a managed package, the namespace of that package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Visualforce page that was requested.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects VisualforceRequestEventLog

**Field** **Details**

**Description**
The query string used to access the requested Visualforce page.

**Example**
Let’s assume that the requested Visualforce page
( `/apex/myAccountDetailPage?id=001xx000003GYv6AAG` ) shows details
of the account whose ID is in the URL. The value of `QueryString` in this case is
`?id=001xx000003GYv6AAG` .

```
RequestIdentifier

RequestSize

RequestStatus

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
The size of the callout response, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.


Standard Objects VisualforceRequestEventLog

**Field** **Details**

```
RequestType

ResponseSize

RunTime

SessionKey

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The request type.

Possible values are:

**•** `page` —A normal request for a page

**•** `content_UI` —A content request for a page that originated in the user interface

**•** `content_apex` —A content request initiated by an Apex call

**•** `PDF_UI` —A request for a page in PDF format through the user interface

**•** `PDF_apex` —A request for PDF format by an Apex call (usually a Web Service call)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout request body, in bytes.

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


Standard Objects VisualforceRequestEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Uri

UserIdentifier

UserType

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.


### Standard Objects VideoCall

**Field** **Details**

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

```
ViewStateSize

### VideoCall

```

Represents a video call.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the Visualforce view state in bytes.

### One VideoCall record can be related to several VideoCallRecording records — for example, a video call can have several

video recordings and a transcript. As well, one video call record can be associated with several video call participant records.

This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`

Fields

**Field** **Details**

AcceptanceTimeStamp

ConsentedUserId

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp when the user consented for uploading the video call recording. Reserved
for future use.

This field is available in API version 62.0 and later.

**Type**
reference


Standard Objects VideoCall

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user who consented to upload the video call recording. Reserved for future
use.

This field is available in API version 62.0 and later.

This field is a relationship field.

**Relationship Name**
ConsentedUser

**Refers To**
User

```
Description

DurationInSeconds

EndDateTime

EventId

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the video call. Typically, the sales rep enters the description.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The video call duration in seconds.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time the video call ended, in universal time coordinated (UTC).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the event record associated with this video call. Reserved for future use.

This is a relationship field.


Standard Objects VideoCall

**Field** **Details**

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

```
ExternalId

HostId

IntelligenceScore

IsCallCoachingIncluded

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the video call, sent by the video call provider.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who hosted the meeting.

This is a relationship field.

**Relationship Name**
Host

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Einstein Intelligence score for the video call. Video calls with higher scores are likely to
contain more relevant information. For example, video calls where product names and
competitor names are mentioned tend to have a higher score.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects VideoCall

**Field** **Details**

**Description**
Indicates whether Einstein Conversation Insights is available for this org and this user
`(true)` or not `(false)` .

```
IsDiarizationOptIn

IsRecorded

LastReferencedDate

LastViewedDate

```

MeetingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether optimal speaker separation (diarization) is opted in `(true)` or not
`(false)` for the call.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the video call was recorded `(true)` or not `(false)` .

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
The timestamp when the current user last viewed this record or list view. If this value is
`null`, the user might have only accessed this record or list view ( `LastReferencedDate` )
but not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the call. Reserved for future use.


Standard Objects VideoCall

**Field** **Details**

This field is available in API version 61.0 and later.

Possible values are:

**•** `EXTERNAL` —A call with two or more participants (default).

**•** `MANUAL` —A call that is manually uploaded.

**•** `SINGLE_USER` —A single user call where the sales rep is evaluated and coached.

```
Name

OwnerId

RelatedRecordId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the video call. Typically entered by the sales rep.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user who created the video call.

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
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the account or opportunity related to this video call.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Opportunity


Standard Objects VideoCall

**Field** **Details**

```
StartDateTime

TranscribedLanguage

```

UsageType

```
VendorMeetingKey

VendorMeetingUuid

VendorName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the video call started, in universal time coordinated (UTC).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The language that is transcribed for this video call.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The cloud using the VideoCall.

This field is available in API version 63.0 and later.

Possible values are:

**•** `Life Sciences` —Remote Engagement.

**•** `Sales Cloud`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The vendor's ID for this video call.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The vendor's unique identifier for this video call.

**Type**
picklist


### Standard Objects VideoCallInsight

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the vendor providing the video call software.

Possible values are:

**•** `ZOOM`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VideoCallChangeEvent (API version 51.0)**
Change events are available for the object.

SEE ALSO:

VideoCallParticipant

VideoCallRecording

### VideoCallInsight

Represents the video call insight data associated with a video call. Each record represents the call insight of a specific recording or
transcript within a call. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.


Standard Objects VideoCallInsight

Fields

**Field** **Details**

```
EngagementInsightType

GenerationDateTime

InsightConfigName

InsightLanguage

InsightModel

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique identifier of the platform setup entity that defines the configuration
for this engagement insight type.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The timestamp when the call insight was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the insight configuration, or category, used to classify the insight.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The language associated with the insight type. Each insight type is currently limited
to a single language. If the same insight type is mapped to a different language, a new insight
type is created.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The category of the insight type.

Possible values are:

**•** `GENERATIVE` —Generative


Standard Objects VideoCallInsight

**Field** **Details**

**•** `KEYWORD` —Keyword

**•** `SITUATIONAL` —Situational

**•** `TIME_BASED` —Time-Based

The default value is `KEYWORD` .

```
InsightOccurenceCount

InsightSubject

InsightText

Name

Scope

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a particular insight occurred in the transcript.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The specific text, phrase, or subject identified in the video call transcript that serves as the
basis for the insight.

**Type**
textarea

**Properties**
Nillable

**Description**
The text content of the insight derived from the video call transcript.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The display name of the insight type.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The scope of the insight type.

Possible values are:


Standard Objects VideoCallInsight

**Field** **Details**

**•** `Organization`

**•** `User`

The default value is `Organization` .

```
VideoCallId

VideoCallRecordingId

VideoCallTranscriptId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the associated parent VideoCall.

This field is a relationship field.

**Relationship Name**
VideoCall

**Relationship Type**
Master-detail

**Refers To**
VideoCall (the master object)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the associated parent VideoCallRecording.

This field is a relationship field.

**Relationship Name**
VideoCallRecording

**Refers To**
VideoCallRecording

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the associated VideoCallTranscript record.

**Relationship Name**
VideoCallTranscript

**Refers To**
VideoCallTranscript


### Standard Objects VideoCallInsightAction VideoCallInsightAction

Represents a suggested follow-up action derived from a video call insight. VideoCallInsightAction manages recommended steps—such
as sending an email, creating a task, or scheduling a meeting—that address specific moments, including competitor mentions, pricing
discussions, or objections. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.

Fields

**Field** **Details**

```
ActionCategory

ActionReferenceId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that classifies the purpose of the action.

Possible values are:

**•** `FollowUp`

**•** `NeedsAttention`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the reference record associated with the generated action.

This field is a relationship field.


Standard Objects VideoCallInsightAction

**Field** **Details**

**Relationship Name**
ActionReference

**Refers To**
VideoCallInsightReason

```
ActionType

CompletionDateTime

Name

Status

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The specific type of action to be performed for the insight.

Possible values are:

**•** `CreateCalendarEvent`

**•** `CreateTaskWithDate`

**•** `EciCreateCallback`

**•** `EciScheduleMeetings`

**•** `EciSendCallResponse`

**•** `ViewContactProfile`

The default value is `CreateTaskWithDate` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Required. The timestamp when the action was completed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the insight action.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the insight action.


### Standard Objects VideoCallInsightReason

**Field** **Details**

Possible values are:

**•** `Active`

**•** `Completed`

The default value is `Active` .

```
VideoCallInsightId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the VideoCallInsight record associated with a video call. Each record represents
the call insight of a specific recording or transcript within a call.

This field is a relationship field.

**Relationship Name**
### VideoCallInsight

**Relationship Type**
Master-detail

**Refers To**
VideoCallInsight (the master object)

### VideoCallInsightReason

Represents the video call insight reason that contains the insight keyword, insight moments associated with a keyword, and the number
of keyword occurrences. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.


Standard Objects VideoCallInsightReason

Fields

**Field** **Details**

```
Name

OccurrenceInfo

OccurrenceSnippet

VideoCallInsightId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the insight reason.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The number of times the given keyword was mentioned in the call.

**Type**
textarea

**Properties**
Nillable

**Description**
The specific excerpt from the video call transcript that helped generate the insight. Reserved
for future use.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the VideoCallInsight record associated with a video call. Each record represents
the call insight of a specific recording or transcript within a call.

This field is a relationship field.

**Relationship Name**
VideoCallInsight

**Relationship Type**
Master-detail

**Refers To**
VideoCallInsight (the master object)


### Standard Objects VideoCallParticipant VideoCallParticipant

Represents a participant in a video call. Participant information can come from the video call provider (for example, Zoom), or Salesforce.
This object is available in API version 51.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Email

IsAllowed

JoinDateTime

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the participant, from the video call provider.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the participant is admitted into the video call (true) or not (false).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the participant joins the video call.

**Type**
dateTime


Standard Objects VideoCallParticipant

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

LeaveDateTime

Name

ParticipantType

RelatedPersonId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
`null`, the user might have only accessed this record or list view ( `LastReferencedDate` )
but not viewed it.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the participant leaves the video call.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The participant's name or phone number. This information is provided by the video call
provider.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the participant in the video call. Available in API version 65.0 and later.

Possible values are:

**•** `Attendee`

**•** `Organizer`

**Type**
reference


Standard Objects VideoCallParticipant

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the user, lead, or contact record for this participant.

This is a polymorphic relationship field.

**Relationship Name**
RelatedPerson

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

```
VideoCallId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the video call record.

This is a relationship field.

**Relationship Name**
VideoCall

**Relationship Type**
Lookup

**Refers To**
VideoCall

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VideoCallParticipantChangeEvent (API version 55.0)**
Change events are available for the object.

SEE ALSO:

VideoCall

VideoCallRecording


### Standard Objects VideoCallRecording VideoCallRecording

Represents a recording from a video call, such as a video recording, a voice recording, or a transcript. Video call recordings aren’t saved
in Salesforce. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DurationInSeconds

EndDateTime

ExpirationDateTime

ExternalRecordingKey

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The video call duration in seconds, not the recording duration.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time the call ended, in universal time coordinated (UTC).

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Reserved for internal use. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the video call recording, from the recording provider. For example, the Zoom ID
of the recording. This value is unique.


Standard Objects VideoCallRecording

**Field** **Details**

```
ExternalRecordingKeyLong

FileSizeInByte

FileType

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The ID of the video call recording, from the recording provider, that's more than 255
characters. For example, the MS Team ID of the recording. This value is unique.

If `ExternalRecordingKey` is null, this ID is used by default.

Available in API version 61.0 and later.

**Type**
long

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The size of the video call recording, in bytes.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The file type of the video call recording.

Possible values are:

**•** `MP4` —Video file

**•** `M4A` —Audio-only file

**•** `TIMELINE` —Time stamp file in JSON format.

**•** `TRANSCRIPT` —Transcription files in VTT format.

**•** `CHAT` —Text file containing chat messages from the video call.

**•** `CC` —File containing closed captions of the video call recording. The file is in VTT format.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects VideoCallRecording

**Field** **Details**

```
LastViewedDate

Name

StartDateTime

VideoCallRecordId

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
`null`, the user only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the video call recording, entered by the sales rep.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start time of the video call recording.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the VideoCall record (the parent record).

This is a relationship field.

**Relationship Name**
VideoCallRecord

**Relationship Type**
Lookup

**Refers To**
VideoCall

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects VideoCallRecordingStructure

**VideoCallRecordingChangeEvent (API version 51.0)**
Change events are available for the object.

SEE ALSO:

VideoCallParticipant

### VideoCall VideoCallRecordingStructure

Represents the structure of a video call recording, having relation to a video call participant, speaking order, start offset, and end offset.
This object is available in API version 65.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.

Fields

**Field** **Details**

```
ListenRatio

Name

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The ratio of the time the speaker spent listening versus talking on the call.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the video call recording.


Standard Objects VideoCallRecordingStructure

**Field** **Details**

```
ParticipantSpeakingOrder

TalkRatio

TalkSegment

VideoCallId

VideoCallParticipantId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The sequence in which participants first spoke during the call. Only the initial speaking turn
of each participant is captured.

**Type**
double

**Properties**
Filter, Sort

**Description**
The ratio of the time that the speaker spent talking versus listening on the call.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The transcript of specific segments that the participant was speaking.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated VideoCall.

This field is a relationship field.

**Relationship Name**
VideoCall

**Relationship Type**
Master-detail

**Refers To**
VideoCall (the master object)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects VoiceCall

**Field** **Details**

**Description**
ID of the associated VideoCallParticipant.

This field is a relationship field.

**Relationship Name**
VideoCallParticipant

**Refers To**
VideoCallParticipant

```
VideoCallRecordingId

### VoiceCall

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated VideoCallRecording.

This field is a relationship field.

**Relationship Name**
VideoCallRecording

**Refers To**
VideoCallRecording

Represents a call in Service Cloud Voice, Sales Dialer, or other supported voice connectors. For Service Cloud Voice, this can be a phone
or Voice over Internet Protocol (VoIP) call. This object is available in API version 40.0 and later.

[To manage VoiceCall records when using Service Cloud Voice, see the Telephony Integration REST API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm)

The fields in the VoiceCall object apply to the Sales Dialer and Service Cloud Voice features unless otherwise stated in the field description.

In addition to the standard fields listed in this page, you can define up to 300 custom fields for the VoiceCall object.

Note: The VoiceCall object supports implicit sharing. When a VoiceCall record is associated with a parent record via the
RelatedRecordId field, users with access to the parent record inherit access to the VoiceCall. The parent record can be a supported
standard object such as an Account, Case, Contact, Lead, Collection Plan, Contact Request, or Opportunity, or a custom object.
This applies even if the Organization-Wide Defaults for VoiceCall is set to Private.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Only users with the Modify All Data permission can delete call records.


Standard Objects VoiceCall

To edit voice call records, Sales Dialer or Service Cloud Voice permissions are required. This includes the Dialer Outbound permission set
for Sales Dialer, or the Contact Center Agent or Contact Center Admin permission sets for Service Cloud Voice, or Agentforce Contact
Center Admin (Salesforce Voice) permission set.

Fields

**Field Name** **Details**

```
ActivityId

AgentSentimentScore

CallAcceptDateTime

CallCenterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the activity record. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
Activity

**Refers To**
Task

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
[If Sentiment Journey in Service Cloud Voice is set up, this field represents the](https://help.salesforce.com/s/articleView?id=service.voice_conversation_sentiments.htm&type=5&language=en_US)
rep’s overall sentiment score post-call in a conversation event. The value must
be between -5 (lowest negative sentiment score) and 5 (highest positive
sentiment score), with 0 being a neutral sentiment score. Available in API version
59.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the date and time (in UTC)
when an agent accepts the call. Available in API version 48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects VoiceCall

**Field Name** **Details**

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the call
center (CallCenter `Id` ) where the activity took place. Available in API version 48.0
and later.

This is a relationship field.

```
CallConnectDateTime

CallDisposition

CallDurationInSeconds

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
For Sales Dialer, this field represents the date and time (in UTC) when the call
was connected.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The status of the phone call.

For Sales Dialer, possible values are:

**•** `in progress`

**•** `busy`

**•** `failed`

For Service Cloud Voice, possible values are:

**•** `new` —The voice call record has been created.

**•** `in-progress` —The call has been accepted (or, for outbound messages,
initiated) by an agent.

**•** `completed` —The call has ended. This includes calls that are transferred.
(If a call is transferred, another voice call record is created to track the state
of the transferred call.) If After Conversation Work (ACW) is enabled, that work
begins after the call completes.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total duration (in seconds) of the call.


Standard Objects VoiceCall

**Field Name** **Details**

```
CallEndDateTime

CallerId

CallerIdType

CallOrigin

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date and time (in UTC) when the call ended.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, this field represents the unique ID of the participant who
initiated the call. If “Match Callers to End User Records” is enabled in Lightning
Experience, the value is null and the `EndUserId` field is used instead to
determine the end user associated with this voice call. Available in API version
48.0 and later.

This is a relationship field.

**Relationship Name**
Caller

**Relationship Type**
Lookup

**Refer To**
ConversationParticipant

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the number displayed for outbound calls.
Possible values are:

**•** `VendorLine` —User.

**•** `CompanyNumber` —Company.

**•** `LocalPresence` —Local Presence.

**•** `CustomCallerId` —Custom Caller ID.

Available in API version 41.0 and later.

**Type**
picklist


Standard Objects VoiceCall

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Information about how this call originated. For Service Cloud Voice, possible
values are:

**•** `Preview` —Preview dialer.

**•** `Progressive` —Progressive dialer.

**•** `Voicemail` —Voicemail call.

Available in API version 56.0 and later.

```
CallQueuedDateTime

CallRecordingId

CallResolution

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the date and time (in UTC)
when the call was added to a queue to be routed to an agent. Available in API
version 48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, this field represents the unique ID of the call recording
for the voice call. An update to the `CallRecordingId` value is an internal
process and doesn't trigger automation such as flows. Available in API version
41.0 and later.

This is a relationship field.

**Relationship Name**
CallRecording

**Relationship Type**
Lookup

**Refers To**
VoiceCallRecording

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects VoiceCall

**Field Name** **Details**

**Description**
The resolution outcome of the call. The default value is `Resolved`, meaning
the call has been resolved. Available in API version 48.0 and later.

```
CallStartDateTime

CallStatus

CallSubtype

CallType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date and time (UTC) when the call started.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For internal use only.

Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Service Cloud Voice, this field represents the network or protocol over which
the phone or Voice over Internet Protocol (VoIP) call is made. Possible values are:

**•** `PSTN`

**•** `WebRTC`

Available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The types of call.

For Sales Dialer, possible values are:

**•** `Bridge`

**•** `Coach`

**•** `Inbound`


Standard Objects VoiceCall

**Field Name** **Details**

**•** `Internal`

**•** `Outbound`

For Service Cloud Voice, possible values are:

**•** `Callback`

**•** `Consult`

**•** `Inbound`

**•** `InternalCall`

**•** `Outbound`

**•** `Transfer`

```
CoachingDurationInSeconds

ConferenceKey

ConversationId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the total duration (in seconds) of the coaching
session. This field only appears if call coaching is enabled. Available in API version
41.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the related conference key. This field is only
available if call monitoring is enabled. Available in API version 41.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the
conversation. This field is only available if call monitoring is enabled. Available in
API version 48.0 and later.

This is a relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup


Standard Objects VoiceCall

**Field Name** **Details**

**Refers To**
Conversation

```
CurrencyCode

CustomerHoldDuration

CustomerSentimentScore

Description

DisconnectReason

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the ISO currency code used to bill the call.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the total duration (in
seconds) of all the holds that occurred during the voice call. Available in API
version 49.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
[If Sentiment Journey in Service Cloud Voice is set up, this field represents the](https://help.salesforce.com/s/articleView?id=service.voice_conversation_sentiments.htm&type=5&language=en_US)
customer’s overall sentiment score post-call in a conversation event. The value
must be between -5 (lowest negative sentiment score) and 5 (highest positive
sentiment score), with 0 being a neutral sentiment score. Available in API version
59.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
If Service Cloud Voice is enabled, this field represents a text field where the agent
can enter a summary of the call. Available in API version 48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable


Standard Objects VoiceCall

**Field Name** **Details**

**Description**
If Service Cloud Voice is enabled, this field represents the reason why the voice
call was disconnected. The reason is provided by the partner telephony. For
Amazon Connect instances, this value is automatically populated through the
contact record if you have Contact Center version 13.0 or later. See
[DisconnectReason in the Amazon Connect contact records data model page for](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html)
a list of possible reasons why a voice call may be disconnected. For all other
partner telephony models, configure this feature through
the `disconnectReason` parameter in the Update a Voice Call Record
Telephony Integration API. Available in API version 59.0 and later.

```
EndUserId

FromPhoneNumber

IsDiarizationOptIn

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, if “Match Callers to End User Records” is enabled in
Lightning Experience, this field represents the unique ID of the messaging end
user (MessagingEndUser `ID` ) associated with this voice call. Available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
EndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
phone

**Properties**
Create, Filter, Group, Sort

**Description**
The number of the user who initiated the call.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether optimal speaker separation (diarization) is opted in ( `true` ) or
not ( `false` ) for the call.


Standard Objects VoiceCall

**Field Name** **Details**

```
IsRecorded

```

IvrDuration

```
LastReferencedDate

LastViewedDate

LongestHoldDuration

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a Voice Call Recording record was created ( `true` ) or not
( `false` ) for this voice call. The default value is `false` . Available in API version
44.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Total duration, in seconds, that a caller spends in the Interactive Voice Response
(IVR) system. The duration includes time spent on automated prompts and
responses before being placed in a queue or connected to a service rep. This
field is available in API version 66.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last viewed a record related
to this voice call.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last viewed this voice call. If
the record has not been viewed before, this value is null. Referencing a record
( `LastReferencedDate` ) doesn’t count as viewing it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects VoiceCall

**Field Name** **Details**

**Description**
If Service Cloud Voice is enabled, this field represents the longest hold duration
(in seconds) that occurred during the call. Available in API version 49.0 and later.

```
MediaProviderId

Name

NextCallId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID of the related media provider. Available in API version 49.0 and
later.

This is a relationship field.

**Relationship Name**
MediaProvider

**Relationship Type**
Lookup

**Refers To**
CallCoachingMediaProvider

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the voice call record. For example, `VC-00000001` . Available in
API version 60.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the next
call if the call was transferred to another agent. If there is no other agent, this
value is null. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
NextCall

**Relationship Type**
Lookup


Standard Objects VoiceCall

**Field Name** **Details**

**Refers To**
VoiceCall

```
NumberOfHolds

OwnerId

PreviousCallId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the number of times the
customer was put on hold. Available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID of the user who owns the voice call record.

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
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the previous
call if the call was transferred from another agent. When there is no previous call,
this value is null. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
PreviousCall

**Relationship Type**
Lookup

**Refers To**
VoiceCall


Standard Objects VoiceCall

**Field Name** **Details**

```
Price

QualityScore

QueueName

RecipientId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
For Sales Dialer, this field represents the cost of the phone call.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If Service Cloud Voice is enabled, this field represents the value of the Mean
Opinion Score (MOS) that measures voice call quality. This algorithm is based on
packet loss percentage, average latency, and average jitter. Available in API version
53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the name of the agent
queue. Available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, this field represents the unique ID of the participant who
received the call. If “Match Callers to End User Records” is enabled in Lightning
Experience, this value is null and the `EndUserId` field is used instead to
determine the end user associated with this voice call.

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
ConversationParticipant


Standard Objects VoiceCall

**Field Name** **Details**

```
RecordyTypeId

RelatedRecordId

SourceType

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Updates

**Description**
The ID of the voice call record type assigned to this voice call. If a record type
isn't assigned to this voice call, the value is null. Available in API version 59.0 and
later.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the related record. Associates the VoiceCall record to a standard
or custom object record. For Service Cloud Voice, supported related records
include the standard objects Account, Case, Collection Plan, Contact, Contact
Request, Lead, and Opportunity. For Sales Dialer, supported related records
include custom objects.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, CollectionPlan, Contact, ContactRequest, Lead, Opportunity

**Type**
picklist

**Properties**
Create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The general purpose of the call. The permission sets assigned to the voice call
owner determine the value. A call’s source type controls which insights Einstein
Conversation Insights applies during analysis.


Standard Objects VoiceCall

**Field Name** **Details**

Possible values are:

**•** Sales

**•** Service

Available in API version 52.0 and later.

```
ToPhoneNumber

TranscribedLanguage

UserId

VendorCallKey

```

**Type**
phone

**Properties**
Create, Filter, Group, Sort

**Description**
The recipient of the call. For inbound, transfer, and callback calls, this value is the
agent's number. For outbound calls, this value is the customer's number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The language that is transcribed for this voice call.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID of the Salesforce user who initiates an outbound call or accepts
an inbound call. If no one takes the call, this value defaults to null.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, idLookup, Sort


Standard Objects VoiceCall

**Field Name** **Details**

**Description**
The unique ID of the child leg of the call that’s provided by the Sales Dialer vendor
or Service Cloud Voice telephony provider.

```
VendorParentCallKey

VendorType

VoiceVendorLineId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the unique ID of the parent leg of the call
that’s provided by the Dialer vendor.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the type of Dialer vendor. For Service Cloud
Voice, this field is always set to `ContactCenter` . Available in API version 41.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the unique ID of the associated Dialer vendor
line.

This is a relationship field.

**Relationship Name**
VoiceVendorLine

**Relationship Type**
Lookup

**Refers To**
VoiceVendorLine

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.


### Standard Objects VoiceCallInsight

**VoiceCallChangeEvent (Available in API version 48.0 and later)**
Change events are available for the object.

**VoiceCallFeed (Available in API version 50.0 and later.)**
Feed tracking is available for the object.

**VoiceCallOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallShare**

Sharing is available for the object.

### VoiceCallInsight

Represents the voice call insight data associated with a voice call. Each record represents the call insight of a specific recording or transcript
within a call. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.

Fields

**Field** **Details**

```
EngagementInsightType

GenerationDateTime

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique identifier of the platform setup entity that defines the configuration
for this engagement insight type.

**Type**
dateTime


Standard Objects VoiceCallInsight

**Field** **Details**

**Properties**
Filter, Sort

**Description**
Required. The timestamp when the call insight was generated.

```
InsightConfigName

InsightLanguage

InsightModel

InsightOccurrenceCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the insight configuration, or category, used to classify the insight.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The language associated with the insight type. Each insight type is currently limited
to a single language. If the same insight type is mapped to a different language, a new insight
type is created.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The category of the insight type.

Possible values are:

**•** `GENERATIVE` —Generative

**•** `KEYWORD` —Keyword

**•** `SITUATIONAL` —Situational

**•** `TIME_BASED` —Time-Based

The default value is `KEYWORD` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a particular insight occurred in the transcript.


Standard Objects VoiceCallInsight

**Field** **Details**

```
InsightSubject

InsightText

Name

Scope

VoiceCallId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The specific text, phrase, or subject identified in the voice call transcript that serves as the
basis for the insight.

**Type**
textarea

**Properties**
Nillable

**Description**
The text content of the insight derived from the voice call transcript.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the insight type.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The scope of the insight type.

Possible values are:

**•** `Organization`

**•** `User`

The default value is `Organization` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the associated parent VoiceCall.

This field is a relationship field.


### Standard Objects VoiceCallInsightAction

**Field** **Details**

**Relationship Name**
### VoiceCall

**Relationship Type**
Master-detail

**Refers To**
VoiceCall (the master object)

```
VoiceCallRecordingId

VoiceCallTranscript

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the associated parent VoiceCallRecording.

This field is a relationship field.

**Relationship Name**
VoiceCallRecording

**Refers To**
VoiceCallRecording

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the voice call transcript record associated with this insight.

### VoiceCallInsightAction

Represents a suggested follow-up action derived from a voice call insight. VoiceCallInsightAction manages recommended steps—such
as sending an email, creating a task, or scheduling a meeting—that address specific moments, including competitor mentions, pricing
discussions, or objections. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Standard Objects VoiceCallInsightAction

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.

Fields

**Field** **Details**

```
ActionCategory

ActionReferenceId

ActionType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that classifies the purpose of the action.

Possible values are:

**•** `FollowUp`

**•** `NeedsAttention`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the record associated with the generated action.

This field is a relationship field.

**Relationship Name**
ActionReference

**Refers To**
VoiceCallInsightReason

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The specific type of action to be performed for the insight.

Possible values are:

**•** `CreateCalendarEvent`


Standard Objects VoiceCallInsightAction

**Field** **Details**

**•** `CreateTaskWithDate`

**•** `EciCreateCallback`

**•** `EciScheduleMeetings`

**•** `EciSendCallResponse`

**•** `ViewContactProfile`

The default value is `CreateTaskWithDate` .

```
CompletionDateTime

Name

Status

VoiceCallInsightId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Required. The timestamp when the action was completed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the insight action.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the insight action.

Possible values are:

**•** `Active`

**•** `Completed`

The default value is `Active` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the VoiceCallInsight record associated with a voice call. Each record represents
the call insight of a specific recording or transcript within a call.

This field is a relationship field.


### Standard Objects VoiceCallInsightReason

**Field** **Details**

**Relationship Name**
### VoiceCallInsight

**Relationship Type**
Master-detail

**Refers To**
VoiceCallInsight (the master object)

### VoiceCallInsightReason

Represents the voice call insight reason that contains the insight keyword, insight moments associated with a keyword, and the number
of keyword occurrences. This object is available in API version 66.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Einstein Conversation Insight must be enabled and the user requires the Conversation Insights for Sales permission set.

Fields

**Field** **Details**

```
Name

OccurrenceInfo

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the insight reason.

**Type**
string


### Standard Objects VoiceCallMetrics

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The number of times the given keyword was mentioned in the call.

```
OccurrenceSnippet

VoiceCallInsightId

### VoiceCallMetrics

```

**Type**
textarea

**Properties**
Nillable

**Description**
The specific excerpt from the voice call transcript that helped generate the insight. Reserved
for future use.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the VoiceCallInsight data associated with a voice call. Each record represents
the call insight of a specific recording or transcript within a call.

This field is a relationship field.

**Relationship Name**
VoiceCallInsight

**Relationship Type**
Master-detail

**Refers To**
VoiceCallInsight (the master object)

Represents metrics for a VoiceCall lifecycle event, aggregated daily. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects VoiceCallMetrics

Fields

**Field** **Details**

```
AverageSCVCallDuration

AvgMessagesPerCall

InboundCallsAgentsConnected

MaxMessagesPerCall

MaxSCVCallDuration

MetricsDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average call duration, measured in minutes, for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The average number of transcription messages per call for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where agents connect with callers for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of transcription messages for the call with the highest number of said messages
for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longest call duration, measured in minutes, for a given day.

**Type**
date

**Properties**
Filter, Group, Sort


Standard Objects VoiceCallMetrics

**Field** **Details**

**Description**
The date and time (in UTC) when the metric was gathered. For example, daily metrics jobs
run at 12am local instance time (not UTC).

```
NumACWInitiated

NumCallbackCallsCtrCompleted

NumInboundCallsCtrCompleted

NumInboundIVRAbandonCalls

NumInboundQueueAbandonCalls

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where After Conversation Work (ACW) is initiated for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of callback calls where interactive voice response (IVR) data is fully and completely
captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where interactive voice response (IVR) data is fully and
completely captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where callers disconnected while waiting in the interactive
voice response (IVR) system for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where callers disconnected while waiting in the queue for a
given day.


Standard Objects VoiceCallMetrics

**Field** **Details**

```
NumOutboundCallsCtrCompleted

NumRecordedCalls

NumSCVCallbackCalls

NumSCVInboundCalls

NumSCVOutboundCalls

NumSCVTransferCalls

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound calls where interactive voice response (IVR) data is fully and
completely captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where the conversation between an agent and caller is recorded for a
given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of callback calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects VoiceCallMetrics

**Field** **Details**

**Description**
The number of transfer calls for a given day.

```
NumTransferCallsCtrCompleted

OutboundCallsAgentsConnected

TotalACWInboundMinutes

TotalACWOutboundMinutes

TotalAgentInboundMinutes

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of transfer calls where interactive voice response (IVR) data is fully and completely
captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound calls where an agent is connected with a caller for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent in After Conversation Work (ACW) for inbound
calls for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent in After Conversation Work (ACW) for outbound
calls for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent talking to callers on inbound calls for a given day.


### Standard Objects VoiceCallList

**Field** **Details**

```
TotalHoldDurationMinutes

TotalIVRInboundMinutes

TotalMessages

TotalOutboundMinutes

TotalQueueInboundMinutes

### VoiceCallList

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of minutes callers were put on hold for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes callers spent in the IVR system on inbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of transcription messages for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent talking to callers on outbound calls for a given
day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For inbound calls, the total number of minutes callers spent in the queue waiting for a given
day.

Represents a prioritized list of numbers to call.


Standard Objects VoiceCallList

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
IsActive

Name

OwnerId

```

Associated Objects

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the call list is active or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the call list.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the call list owner.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceCallListOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallListShare**

Sharing is available for the object.


### Standard Objects VoiceCallListItem VoiceCallListItem

Represents a single phone number in a prioritized call list.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
CallListId

Ordinal

RelatedRecordId

State

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related call list.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order of the item in the overall call list.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the related record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects VoiceCallQualityFeedback

**Field Name** **Details**

**Description**
Whether the call list item is not called, called, or skipped.

### VoiceCallQualityFeedback

Represents feedback given by a Sales Dialer user about the quality of a VoiceCall .

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
FeedbackText

FeedbackType

OwnerId

VoiceCallId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The detailed feedback about a call left by a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feedback category (Call could not connect, Audio lagged, etc.) selected by
a user.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user leaving the feedback.

**Type**
reference


### Standard Objects VoiceCallRecording

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the related VoiceCall.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceCallQualityFeedbackOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallQualityFeedbackShare**

Sharing is available for the object.

### VoiceCallRecording

Represents a call recording in Service Cloud Voice and Sales Dialer. Call recordings for Service Cloud Voice with Amazon Connect and
for Service Cloud Voice with Partner Telephony from Amazon Connect are stored in S3 buckets on your Amazon Web Services (AWS)
account and can be accessed via AWS. Call recordings for Sales Dialer are saved as files in Salesforce.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
DurationInSeconds

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total length (in seconds) of the voice call recording.

This value depends on which parameters are passed to the `PATCH`
`/telephony/v1/voiceCalls/{CALL ID}` API.


Standard Objects VoiceCallRecording

**Field Name** **Details**

**•** If the totalRecordingDuration parameter is passed, then
`DurationInSeconds` = `totalRecordingDuration` .

**•** If the agentInteractionDuration and totalHoldDuration parameters are passed,
then `DurationInSeconds` = `agentInteractionDuration` +
`totalHoldDuration` .

**•** If the agentInteractionDuration, totalHoldDuration, and
totalRecordingDuration parameters are passed, then
`DurationInSeconds` = `totalRecordingDuration` .

```
IntelligenceScore

IsConsented

MediaContentId

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The intelligence score of the recording.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the call recording was indicated as consented or not.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related media content, a ContentDocument. The record counts
toward your org’s file storage quota.

This is a relationship field.

**Relationship Name**
MediaContent

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects VoiceCallRecording

**Field Name** **Details**

**Description**
The name of the call recording file.

```
OwnerId

UploadDateTime

VoiceCallId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the call recording.

This is a polymorphic relationship field.

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
The time and date that the recording was uploaded.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the related phone call. The property `nillable` has been
removed in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
VoiceCall

**Relationship Type**
Lookup

**Refers To**
VoiceCall


### Standard Objects VoiceCoaching

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VoiceCallRecordingChangeEvent (API version 48.0)**
Change events are available for the object.

**VoiceCallRecordingOwnerSharingRule**

Sharing rules are available for the object. Removed in API version 50.0 and later.

**VoiceCallRecordingShare**

Sharing is available for the object. Removed in API version 50.0 and later.

### VoiceCoaching

Represents a call that is using call monitoring.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
OwnerId

RelatedRecordId

TraineeId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the manager monitoring the call.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the call list owner.

**Type**
reference


### Standard Objects VoiceLocalPresenceNumber

**Field Name** **Details**

**Properties**
Filter, Group, Sort, Unique

**Description**
The ID of the call list owner.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceCoachingOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCoachingShare**

Sharing is available for the object.

### VoiceLocalPresenceNumber

Represents a phone number with the same area code as the person who’s being called.

Supported Calls

`query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
CountryCode

LastUsedDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The country code of the phone number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects VoiceMailContent

**Field Name** **Details**

**Description**
The date the phone number was last used.

```
PhoneNumber

Prefix

### VoiceMailContent

```

**Type**
phone

**Properties**
Filter, Group, Sort

**Description**
The local presence phone number.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The area code of the phone number.

Represents a voicemail message left by a caller to the context user.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
DurationInSeconds

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the voicemail message in seconds.


Standard Objects VoiceMailContent

**Field Name** **Details**

```
FirstHeardDateTime

MediaContentId

Name

OwnerId

VoiceCallId

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time and date when the user first listened to the voicemail message.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
[The ID of the related media content, a ContentDocument. The record counts](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_contentdocument.htm)
toward your org’s file storage quota.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the voicemail message.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the voicemail message.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related Dialer call.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailContentOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects VoiceMailGreeting

**VoiceMailContentShare**

Sharing is available for the object.

### VoiceMailGreeting

Represents a custom greeting message that plays upon reaching a user’s voicemail. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
DurationInSeconds

IsDefault

MediaContentId

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the voicemail greeting message in seconds.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the greeting is the user’s default greeting ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the related content document.

**Type**
string


### Standard Objects VoiceMailMessage

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the voicemail greeting message.

```
OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the voicemail greeting message owner.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailGreetingOwnerSharingRule**

Sharing rules are available for the object.

**VoiceMailGreetingShare**

Sharing is available for the object.

### VoiceMailMessage

Represents a prerecorded voicemail message.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
DurationInSeconds

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects VoiceMailMessage

**Field Name** **Details**

**Description**
The duration of a prerecorded voicemail message in seconds.

```
IsDefault

MediaContentId

Name

OwnerId

```

Associated Objects

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the message is the context user’s default voicemail drop
message.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the file.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the prerecorded voicemail message.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the prerecorded voicemail message.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailMessageOwnerSharingRule**

Sharing rules are available for the object.

**VoiceMailMessageShare**

Sharing is available for the object.


### Standard Objects VoiceOrgSetting VoiceOrgSetting

Represents the org's customized voice settings. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsentMessage

CustomDisposition

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
A custom message displayed for recording consent.

Available in API version 49.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If set, this field identifies which custom field in the Activity object is used as the call dispositions
picklist.

Possible values are:

**•** `AccountContactRole`

**•** `AccountOwnership`

**•** `AccountRating`

**•** `AccountType`

**•** `AgeOver`

**•** `AssetRelationshipType`

**•** `AssetStatus`

**•** `AssociatedLocationType`

**•** `BuyerAttributes`

**•** `CampaignMemberStatus`

**•** `CaseContactRole`

**•** `CaseOrigin`

**•** `CasePriority`


Standard Objects VoiceOrgSetting

**Field** **Details**

**•** `CaseReason`

**•** `CaseStatus`

**•** `CaseType`

**•** `ComplianceGroup`

**•** `ConsequenceOfFailure`

**•** `ContactPointAddressType`

**•** `ContactPointUsageType`

**•** `ContactRequestReason`

**•** `ContactRequestRequestedChannel`

**•** `ContactRequestStatus`

**•** `ContactRole`

**•** `ContractContactRole`

**•** `ContractStatus`

**•** `DataImportRefreshHours`

**•** `DataModelSupplierType`

**•** `DigitalAssetStatus`

**•** `EventSubject`

**•** `EventType`

**•** `ExceptionType`

**•** `FieldBusinessStatus`

**•** `FieldClassification`

**•** `FiscalYearPeriodName`

**•** `FiscalYearPeriodPrefix`

**•** `FiscalYearQuarterName`

**•** `FiscalYearQuarterPrefix`

**•** `FlowEnvironment`

**•** `ForecastCategoryName`

**•** `ForecastingItemCategory`

**•** `GenderIdentity`

**•** `IdeaMultiCategory`

**•** `IdeaStatus`

**•** `Industry`

**•** `LeadSource`

**•** `LeadStatus`

**•** `LocationType`

**•** `MilitaryService`

**•** `OpportunityCompetitor`

**•** `OpportunityStage`


Standard Objects VoiceOrgSetting

**Field** **Details**

**•** `OpportunityType`

**•** `OrderStatus`

**•** `OrderType`

**•** `OrgMetricCategory`

**•** `OrgMetricErrorMessage`

**•** `OrgMetricImplEffort`

**•** `OrgMetricStatus`

**•** `OrgMetricType`

**•** `PartnerRole`

**•** `ProcessExceptionCategory`

**•** `ProcessExceptionPriority`

**•** `ProcessExceptionSeverity`

**•** `ProcessExceptionStatus`

**•** `Product2Family`

**•** `Pronoun`

**•** `QuantityUnitOfMeasure`

**•** `QuickTextCategory`

**•** `QuickTextChannel`

**•** `SalesEngagementActivityType`

**•** `SalesTeamRole`

**•** `Salutation`

**•** `ScorecardMetricCategory`

**•** `SecurityClassification`

**•** `SocialPostClassification`

**•** `SocialPostEngagementLevel`

**•** `SocialPostReviewedStatus`

**•** `SolutionStatus`

**•** `StatusReason`

**•** `TaskPriority`

**•** `TaskStatus`

**•** `TaskSubject`

**•** `TaskType`

**•** `WorkOrderLineItemStatus`

**•** `WorkOrderPriority`

**•** `WorkOrderStatus`

```
DefaultDisposition

```

**Type**
picklist


Standard Objects VoiceOrgSetting

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies which picklist value set is used as default for call dispositions.

Possible values are:

**•** `AccountContactRole`

**•** `AccountOwnership`

**•** `AccountRating`

**•** `AccountType`

**•** `AgeOver`

**•** `AssetRelationshipType`

**•** `AssetStatus`

**•** `AssociatedLocationType`

**•** `BuyerAttributes`

**•** `CampaignMemberStatus`

**•** `CaseContactRole`

**•** `CaseOrigin`

**•** `CasePriority`

**•** `CaseReason`

**•** `CaseStatus`

**•** `CaseType`

**•** `ComplianceGroup`

**•** `ConsequenceOfFailure`

**•** `ContactPointAddressType`

**•** `ContactPointUsageType`

**•** `ContactRequestReason`

**•** `ContactRequestRequestedChannel`

**•** `ContactRequestStatus`

**•** `ContactRole`

**•** `ContractContactRole`

**•** `ContractStatus`

**•** `DataImportRefreshHours`

**•** `DataModelSupplierType`

**•** `DigitalAssetStatus`

**•** `EventSubject`

**•** `EventType`

**•** `ExceptionType`

**•** `FieldBusinessStatus`


Standard Objects VoiceOrgSetting

**Field** **Details**

**•** `FieldClassification`

**•** `FiscalYearPeriodName`

**•** `FiscalYearPeriodPrefix`

**•** `FiscalYearQuarterName`

**•** `FiscalYearQuarterPrefix`

**•** `FlowEnvironment`

**•** `ForecastCategoryName`

**•** `ForecastingItemCategory`

**•** `GenderIdentity`

**•** `IdeaMultiCategory`

**•** `IdeaStatus`

**•** `Industry`

**•** `LeadSource`

**•** `LeadStatus`

**•** `LocationType`

**•** `MilitaryService`

**•** `OpportunityCompetitor`

**•** `OpportunityStage`

**•** `OpportunityType`

**•** `OrderStatus`

**•** `OrderType`

**•** `OrgMetricCategory`

**•** `OrgMetricErrorMessage`

**•** `OrgMetricImplEffort`

**•** `OrgMetricStatus`

**•** `OrgMetricType`

**•** `PartnerRole`

**•** `ProcessExceptionCategory`

**•** `ProcessExceptionPriority`

**•** `ProcessExceptionSeverity`

**•** `ProcessExceptionStatus`

**•** `Product2Family`

**•** `Pronoun`

**•** `QuantityUnitOfMeasure`

**•** `QuickTextCategory`

**•** `QuickTextChannel`

**•** `SalesEngagementActivityType`

**•** `SalesTeamRole`


Standard Objects VoiceOrgSetting

**Field** **Details**

**•** `Salutation`

**•** `ScorecardMetricCategory`

**•** `SecurityClassification`

**•** `SocialPostClassification`

**•** `SocialPostEngagementLevel`

**•** `SocialPostReviewedStatus`

**•** `SolutionStatus`

**•** `StatusReason`

**•** `TaskPriority`

**•** `TaskStatus`

**•** `TaskSubject`

**•** `TaskType`

**•** `WorkOrderLineItemStatus`

**•** `WorkOrderPriority`

**•** `WorkOrderStatus`

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
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters and must be unique in your organization. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the MasterLabel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the voice org setting.


### Standard Objects VoiceUserLine VoiceUserLine

Represents a user’s forwarding phone number.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
IsCustomCallerId

IsVerified

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the number is a custom caller ID ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**

The name of the phone number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects VoiceUserLine

**Field Name** **Details**

**Description**

The ID of the user who owns the phone number.

```
PhoneNumber

UserId

VendorVerifiedCallerIdKey

VoiceVendorInfoId

```

Associated Objects

**Type**
phone

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The user’s phone number.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user using the phone number.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The ID for a custom phone number provided by the Sales Dialer service provider.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related Sales Dialer service provider.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceUserLineOwnerSharingRule**

Sharing rules are available for the object.

**VoiceUserLineShare**

Sharing is available for the object.


### Standard Objects VoiceUserPreferences VoiceUserPreferences

Represents the number the user displays when making outbound calls. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
CallerIdType

DeskPhoneNumber

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The number displayed for outbound calls. The possible values are:

**•** VendorLine

**•** CompanyNumber

**•** LocalPresence

**•** CustomCallerId

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A separate phone number users can utilize as part of a call bridge.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the phone number owner.


### Standard Objects VoiceVendorInfo

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceUserPreferencesOwnerSharingRule**

Sharing rules are available for the object.

**VoiceUserPreferencesShare**

Sharing is available for the object.

### VoiceVendorInfo

Represents information about the Service Cloud Voice or Sales Dialer provider’s vendor.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
CorporateNumber

IsActive

LocalPresenceDefaultNumber

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The standard number that users can choose to display when making outgoing
calls.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the vendor is active or not.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects VoiceVendorLine

**Field Name** **Details**

**Description**
The default routing number that’s available for incoming local presence calls.

```
TenantConfigVersion

VendorAccountKey

VendorProviderName

VendorType

### VoiceVendorLine

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the Service Cloud Voice tenant configuration. Available in API
version 51.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The account key of the vendor.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the vendor.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The name of the telephony vendor.

Represents a user’s phone number reserved with the vendor.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects VoiceVendorLine

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
CallUsageInSecondsLastMonth

OwnerId

PhoneNumber

ShouldRecord

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
An org’s total call usage last month in seconds.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the phone number.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
phone

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique vendor phone number.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


Standard Objects VoiceVendorLine

**Field Name** **Details**

```
Status

UserId

VoiceVendorInfoId

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the number is currently active or released.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user using the phone number.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Dialer vendor.

This is a relationship field.

**Relationship Name**
VoiceVendorInfo

**Relationship Type**
Lookup

**Refers To**
VoiceVendorInfo

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceVendorLineOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects Vote

**VoiceVendorLineShare**

Sharing is available for the object.

### Vote

Represents a vote that a user has made on a Knowledge Article, Idea, or Reply.

Note: In API version 16.0 and earlier, SOQL queries on the Vote object only return votes for the Idea object. Starting in API version
17.0, SOQL queries return votes for both Idea and Reply.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Voting on Knowledge articles is available only when Knowledge is enabled.

Fields

**Field** **Details**

```
IsDeleted

LastModifiedById

LastModifiedDate

```

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
Defaulted on create, Filter, Group, Sort

**Description**
ID of the user most recently associated with this vote.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort


Standard Objects Vote

**Field** **Details**

**Description**
The datetime when this vote was last modified.

```
ParentId

Type

```

**Type**
reference

**Properties**
Group, Sort, Create, Filter

**Description**
ID of the Knowledge Article, Idea, or Reply associated with this vote.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Idea, IdeaComment, KnowledgeArticle, Solution

**Type**
picklist

**Properties**
Group, Sort, Create, Filter, Restricted picklist, Update

**Description**
Picklist that indicates the type of vote. The value `Up` indicates that the vote is a user's positive
endorsement of the associated idea or reply. The value `Down` indicates that the vote is a
user's negative endorsement of the associated idea or reply.

Note: If you are importing Vote data into Salesforce and need to set the value for an audit field, such as `CreatedDate`, contact
Salesforce. Audit fields are automatically updated during API operations unless you request to set these fields yourself..

Usage

For Knowledge Articles, one vote record is inserted per user per Knowledge Article. Voting for another article version overrides the vote
for the previous version.

In version 12.0 and later, use this object to track the votes that users made on ideas. For more information on ideas, see “Understand
and Work with Ideas” in the Salesforce Help .

In version 17.0 and later, you must filter using the following syntax when querying this object in a SOQL query: `ParentId =` _**`single`**_
_**`ID`**_, `Parent.Type =` _**`single Type`**_, `Id =` _**`single ID`**_, or `Id IN (` _**`list of IDs`**_ ). See Comparison Operators in the
[Salesforce SOQL and SOSL Reference Guide for a sample query.](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/)

A SOQL query must filter using one of the following Parent or Id clauses.

**•** `ParentId = [` _**`single ID`**_ `]`


### Standard Objects WarrantyTerm

**•** `Parent.Type = [` _**`single type`**_ `]`

**•** `Id = [` _**`single ID`**_ `]`

**•** `Id IN = [` _**`list of IDs`**_ `]`

SEE ALSO:

Idea

IdeaComment

### WarrantyTerm

Represents warranty terms defining the labor, parts, and expenses covered, along with any exchange options, provided to rectify issues
with products. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Code

Description

EffectiveStartDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A code or other identifier associated with this warranty term.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the warranty term.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date on which the warranty term became available for use.

Possible values are:


Standard Objects WarrantyTerm

**Field** **Details**

**•** `InstallDate`

**•** `ManufactureDate`

**•** `PurchaseDate`

```
ExchangeType

Exclusions

ExpensesCovered

ExpensesCoveredDuration

ExpensesCoveredUnitOfTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of exchange offered.

Possible values are:

**•** `AdvanceExchange`

**•** `Loaner`

**•** `ReturnExchange`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of any exclusions.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of expenses covered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The duration for which expenses are covered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects WarrantyTerm

**Field** **Details**

**Description**
The unit in which expenses covered duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

```
IsActive

IsTransferable

LaborCovered

LaborCoveredDuration

LaborCoveredUnitOfTime

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty term is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty can be transferred to a new owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of labor covered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The duration for which labor is covered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects WarrantyTerm

**Field** **Details**

**Description**
The unit in which labor covered duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

```
LastReferencedDate

LastViewedDate

OwnerId

PartsCovered

PartsCoveredDuration

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the warranty term was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the warranty term was last viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The warranty term’s assigned owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of parts covered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WarrantyTerm

**Field** **Details**

**Description**
The duration for which parts are covered.

```
PartsCoveredUnitOfTime

Pricebook2Id

WarrantyDuration

WarrantyTermName

WarrantyType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit in which parts covered duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the price book item associated with this warranty term.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the warranty offered by this term.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the warranty term.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects WaveAutoInstallRequest

**Field** **Details**

**Description**
The type of warranty.

Possible values are:

**•** `Repair`

**•** `Standard`

**•** `Supplier`

```
WarrantyUnitOfTime

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit in which the warranty duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WarrantyTermChangeEvent**

Change events are available for the object.

### WaveAutoInstallRequest

Provides access to the concrete object that represents a CRM Analytics auto-install request. The auto-install request tracks the progress
of CRM Analytics applications created from CRM Analytics templates by the automated process user. This object is available in API version
38.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

CRM Analytics must be enabled in your org. A user must have the Auto Install permission enabled.


Standard Objects WaveAutoInstallRequest

Fields

**Field** **Details**

```
Configuration

FailedReason

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
CRM Analytics application configuration for the auto-install request.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the CRM Analytics application fails to complete successfully, this value indicates why the
failure occurred. Values can be:

**•** `OrganizationIncompatible` : the org didn't pass the template compatibility
checks.

**•** `AppInstallationSkipped` : the org didn't pass the template compatibility checks
and was skipped.

**•** `RetriesExhausted` : the request exhausted the maximum number of retries.

**•** `RequestCancelled` : the user canceled the request.

**•** `AppCreateFailure` : the app or folder creation failed. Check the request log and
try again.

**•** `AppUpdateFailure` : the app or folder update failed. Check the request log and try
again.

**•** `AppConstructionFailure` : the app or folder construction failed. Check the
request log and try again.

**•** `WaveDisabled` : the org doesn't have the Wave org permission or preference enabled.
Check the licenses for CRM Analytics and try again.

**•** `CancelFailed` : canceling an in-progress app failed. Check the request log and try
again.

**•** `DeleteFailed` : deleting an app failed. Check the request log and try again.

**•** `DependencyFailure` : a dependent auto-install request failed. Check App Install
History and try again.

**•** `DependencyCancelled` : the user canceled a dependent auto-install request. Check
App Install History and try again.

**•** `FailedToEnqueue` : the request failed to enqueue. Check the request log and try
again.

**•** `FailedOther` : the request failed for another reason. Check the request log and try
again.


Standard Objects WaveAutoInstallRequest

**Field** **Details**

```
FolderId

IsLocked

MayEdit

Name

RequestLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the CRM Analytics application created by the auto-install request.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the auto-install request is locked or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the auto-install request can be edited or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the auto-install request, provided at creation by the user.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A log of the auto-install progress and completion results.


Standard Objects WaveAutoInstallRequest

**Field** **Details**

```
 RequestStatus

 RequestType

 TemplateApiName

 TemplateVersion

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the auto-install request. Values can be `New`, `Enqueued`, `Cancelled`, `In`
`Progress`, `AppInProgress`, `Failed`, and `Success` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of auto-install request. Values can be `WaveEnable`,
`OrgCompatibilityCheck`, `WaveAppCreate`, `WaveAppUpdate`,
`WaveAppDelete`, and `StartDataflow` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The API name of the CRM Analytics template to create the CRM Analytics app from.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The version of the CRM Analytics template to create the CRM Analytics app from.

Use this object to query and create auto-install requests for CRM Analytics applications in your org. This object is useful to troubleshoot
issues with templated applications that the automated process user creates.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WaveAutoInstallRequestChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects WebCart WebCart

Represents an online shopping cart for a store built with B2B Commerce or D2C Commerce, with total amounts for products, shipping
and handling, and taxes. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The WebCart object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AccountId

BillingAddress

BillingCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
### ID of the account that owns this WebCart . In API version 51.0 and later, if the WebCart

was created through Guest Browsing, this ID is the ID of the `GuestBuyerProfile` .

This field is a polymorphic relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
### The mailing address to which this WebCart is billed.

**Type**
string


Standard Objects WebCart

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the billing address.

```
BillingCountry

BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy rating of the geocode for the billing address. Possible values are:

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
The latitude of the geocode for the billing address.

**Type**
double


Standard Objects WebCart

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the geocode for the billing address.

```
BillingPostalCode

BillingState

BillingStreet

CurrencyIsoCode

GrandTotalAmount

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the billing address. Enter up to 255 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions with multi-currency enabled, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency


Standard Objects WebCart

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items’ `TotalAmount`, or `WebCart TotalAmount` plus `WebCart`
`TotalTaxAmount` . This value includes all taxes and adjustments.

```
GuestCompanyName

GuestEmailAddress

GuestFirstName

GuestLastName

GuestPhoneNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with a delivery for a guest customer. This field is available in API
version 59.0 and later.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name (or surname) of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
phone


Standard Objects WebCart

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number of a guest buyer.

This field is available in API version 52.0 and later.

```
GuestSecondName

InitialOrderReferenceNumber

InventoryReservationIdentifier

IsRepricingNeeded

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The second name of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier assigned to the WebCart at the beginning of the checkout process. Initially
populated when the checkout process is initiated, the
`InitialOrderReferenceNumber` is then associated with the order created when
the checkout is complete.

This field is available in API version 61.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

This field is available in API version 57.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the cart has changed since the last repricing. The default value is false.


Standard Objects WebCart

**Field** **Details**

```
IsSecondary

LastRepricingDate

Name

OwnerId

PaymentGroupId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the cart is a secondary cart or a primary cart.

This field is available in API version 52.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the last repricing was done.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `WebCart` record. `Name` can be up to 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this `WebCart` .

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


Standard Objects WebCart

**Field** **Details**

**Description**
The ID of the `WebCart` payment group.

This field is a relationship field.

**Relationship Name**
PaymentGroup

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

```
PaymentMethodId

PoNumber

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The method of payment for this `WebCart` .

This field is a polymorphic relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
AlternativePaymentMethod, CardPaymentMethod, DigitalWallet

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The purchase order number. Enter up to 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of this `WebCart` . Possible values are:

**•** `Active—` Cart is created and available for modifications, like adding or removing products
or promotions.

**•** `Checkout—` Cart is in checkout. If the customer modifies the cart, the current checkout
session is canceled.


Standard Objects WebCart

**Field** **Details**

**•** `Closed—` Checkout is complete and an order was created. The cart cannot be modified.

**•** `PendingClosed—` Cart is marked to be closed, but the request isn't completed yet.
The cart can’t be modified. This value is available in API version 57.0 and later.

**•** `PendingDelete—` Cart is marked for delete, but the request isn't completed yet. The
cart can’t be modified.

**•** `Processing—` Cart is processing. For example, taxes are being calculated. The cart
can’t be modified.

```
TaxLocaleType

TaxType

TotalAdjustmentAmount

TotalAmount

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax locale. Possible values are:

**•** `Net`

**•** `Gross`

This field is available in API versions 52.0 to 54.0.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax policy. Possible values are:

**•** `Automatic`

**•** `Net`

**•** `Gross`

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that reflects the total of all adjustments to the cart subtotal. Adjustments
include item, tier, and cart level discounts.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects WebCart

**Field** **Details**

**Description**
The sum of all cart items’ `TotalPrice`, or `TotalProductAmount` plus
`TotalChargeAmount` . If the store tax type is Gross, the sum includes taxes.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required and must have a value greater than or equal to zero](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
(0).

```
TotalAmountAfterAllAdjustments

TotalCartLevelAdjAmount

TotalChargeAmount

TotalChargeTaxAmount

TotalLineItemsWithErrors

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all cart items after all price adjustments are applied. Adjustments include various
types of discounts.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total cart level discount amount for the cart.

This field is available in API version 61.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all cart items’ `TotalPrice` for cart items of the type `Charge` .

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalTaxAmount` for cart items of the type `Charge` .

**Type**
int


Standard Objects WebCart

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
A calculated field that shows the total number of cart line items of type `Product` with
errors.

This field is available in API version 50.0 and later.

```
TotalListAmount

TotalProductAmount

TotalProductCount

TotalProductItemAdjAmount

TotalProductLineItemCount

```

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Sum of all the cart items’ `TotalListPrice` .

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalPrice` for cart items of the type `Product` .

**Type**
double

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A count of all the products in the `WebCart` .

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total item level discount amount for the cart.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects WebCart

**Field** **Details**

**Description**
A calculated field that shows the total number of cart line items of type `Product` .

This field is available in API version 60.0 and later.

```
TotalProductListAmount

TotalProductTaxAmount

TotalPromoAdjustmentAmount

TotalPromoAdjustmentTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalListAmount` for the `CartItem` type `Product` .

This field is available in API version 59.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalTaxAmount` for the `CartItem` type `Product` .

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The total of all item discounts related to product promotions.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The total tax adjustment for all item discounts related to product promotions.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects WebCart

**Field** **Details**

**Description**
The sum of all cart items’ `TotalTaxAmount`, or `TotalProductTaxAmount` plus
`TotalDeliveryTaxAmount` .

```
Type

UniqueProductCount

WebStoreId

```

Usage Notes

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `WebCart` type. Default value is `Cart` . Possible values are:

**•** `Cart`

**•** `PayNowReadOnly`

**•** `ReadOnly`

**•** `Template`

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The count of unique product SKUs in the `WebCart` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The store ID related to this `WebCart` .

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**•** In a B2B Commerce for Lightning store, customers who created custom components for adding items to carts noticed that, after
adding items, the cart badge didn’t refresh. A hard refresh causes the value to properly update.


### Standard Objects WebCartAdjustmentBasis

Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WebCartChangeEvent (API version 58.0)**
Change events are available for the object.

**WebCartHistory**

History is available for tracked fields of the object.

**WebCartOwnerSharingRule**

Sharing rules are available for the object.

**WebCartShare**

Sharing is available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

_Salesforce DX Developer Guide_ [: Get Started with Scratch Org](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_get_started.htm)

### WebCartAdjustmentBasis

Coupons that trigger promotions for the cart. When a customer tries to add a coupon to the cart, the store looks for promotions associated
with the coupon. If a promotion results in a price adjustment, a WebCartAdjusmentBasis record is created. This object is available in API
version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentBasisDetail

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon code for the coupon associated with the promotion.


Standard Objects WebCartAdjustmentBasis

**Field** **Details**

```
AdjustmentBasisReferenceId

CurrencyIsoCode

Name

WebCartId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key reference to the coupon.

This field is a relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code of the cart.

Possible values are:

**•** `EUR`

**•** `USD`

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the WebCartAdjustmentBasis record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cart.

This field is a relationship field.


### Standard Objects WebCartAdjustmentGroup

**Field** **Details**

**Relationship Name**
### WebCart

**Relationship Type**
Lookup

**Refers To**
### WebCart

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebCartAdjustmentBasisChangeEvent on page 68**
Change events are available for the object.

### WebCartAdjustmentGroup

Group of price adjustments for a cart. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The WebCartAdjustmentGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`


Standard Objects WebCartAdjustmentGroup

**Field** **Details**

**•** `System`

```
AdjustmentTargetType

AdjustmentType

AdjustmentValue

CartId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target for the price adjustment (the cart itself or individual items).

Possible values are:

**•** `Cart`

**•** `Item`

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
Create, Filter, Group, Sort

**Description**
ID of the cart to which the price adjustment belongs.

This is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup


Standard Objects WebCartAdjustmentGroup

**Field** **Details**

**Refers To**
WebCart

```
CurrencyIsoCode

Description

Name

PriceAdjustmentCauseId

```

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
Description of the adjustment group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the adjustment group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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


### Standard Objects WebCartHistory

**Field** **Details**

```
Priority

TaxAmount

TotalAmount

TotalAmountWithTax

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple price adjustments, sequence in which the price adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tax on the total adjusted price.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total adjusted price plus tax.

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WebCartAdjustmentGroupChangeEvent (API version 58.0)**
Change events are available for the object.

### WebCartHistory WebCartHistory represents the history of changes to the values in the fields of the WebCart object. For specific version information, see the documentation for WebCart .


Standard Objects WebCartHistory

Supported Calls

`describeSObjects()`, `query`, `replicate`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

For specific special access rules, if any, see the documentation for `WebCart` .

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

WebCartId

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
Name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Old value of the field that was changed.

**Type**
reference


### Standard Objects WebLink

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the `WebCart` .

### WebLink

Represents a custom link to a URL or Scontrol.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

**•** To create a custom link, the client application must be logged in with the “Customize Application” permission.

**•** Customer Portal users can’t access this object.

Fields

**Field Name** **Details**

```
Availability

Description

DisplayType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the custom link. Limit is 1,000 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects WebLink

**Field Name** **Details**

**Description**
Type of display: button, link, or mass-action button.

```
EncodingKey

HasMenubar

HasScrollbars

HasToolbar

Height

IsProtected

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Encoding of parameters on the URL link.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows a menu bar ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows scroll bars ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows browser toolbars ( `true` ) or not
( `false` ). Toolbars normally contain navigation buttons like Back, Forward, and
Print.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Height of the popup in pixels.

**Type**
boolean


Standard Objects WebLink

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is protected ( `true` ) or not ( `false` ). Protected
components that have been installed in other organizations can’t be linked to
or referenced by components created in the subscriber organization. A developer
can easily delete a protected component contained in a managed package in a
future release of the package without worrying about failing installations.
However, once a component is marked as unprotected and is released globally,
the developer can’t delete it.

```
IsResizable

LinkType

MasterLabel

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users are allowed to resize the popup window ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Type of link (S-control or URL).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Master label for the link. Limit is 240 characters. This display value is the internal
label that is not translated.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name to display on page.


Standard Objects WebLink

**Field Name** **Details**

```
NamespacePrefix

OpenType

PageOrSobjectType

Position

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
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. How the custom link opens when clicked in a browser—NewWindow,
Sidebar, or NoSidebar.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. For standard objects, the name of the page on which to display the
custom link. For custom objects, the name of the object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects WebLink

**Field Name** **Details**

**Description**
Location on the screen where the popup should open—TopLeft, FullScreen, or
None.

```
RequireRowSelection

ScontrolId

ShowsLocation

ShowsStatus

Url

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the custom link requires a row selection ( `true` ) or not
( `false` ).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the custom s-control object (Scontrol) to link to. Can include fields as tokens
within the custom s-control object. Label is **Custom S-Control ID** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows the browser’s address bar containing
the URL ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Show the status bar at the bottom of the browser.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Required. URL of the page to link to. Can include fields as tokens within the URL.
Limit: 1,024 KB.


### Standard Objects WebLinkLocalization

**Field Name** **Details**

```
Width

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Width of the popup in pixels.

Use this object to programmatically manage custom links, which allow client applications to integrate data with external URLs, an
organization’s intranet, or other back-end office systems. A custom link can point to:

**•** An external URL, such as `www.google.com` or your company's intranet.

**•** A custom s-control, such as a Java applet or Active-X control.

Custom links can include fields as tokens within the URL or custom s-control.

SEE ALSO:

Scontrol

### WebLinkLocalization

Represents the translated value of the field label for a custom link to a URL or s-control when the Translation Workbench is enabled for
your organization.

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
LanguageLocaleKey

```

**Type**
picklist


Standard Objects WebLinkLocalization

**Field** **Details**

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

```
Language

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

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


Standard Objects WebLinkLocalization

**Field** **Details**

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


Standard Objects WebLinkLocalization

**Field** **Details**

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


Standard Objects WebLinkLocalization

**Field** **Details**

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Icelandic: `is`

**•** Irish: `ga`

**•** Italian (Switzerland): `it_CH`

**•** Kannada: `kn`

**•** Kazakh: `kk`

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


Standard Objects WebLinkLocalization

**Field** **Details**

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

**•** Spanish (Venezuela): `es_VE`

**•** Swahili: `sw`

**•** Tagalog: `tl`

**•** Tamil: `ta`

**•** Te reo: `mi`

**•** Telugu: `te`

**•** Urdu: `ur`

**•** Welsh: `cy`

**•** Xhosa: `xh`

**•** Zulu: `zu`

The values in this field are not related to the default locale selection.

```
NamespacePrefix

```

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


### Standard Objects WebStore

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 Value

 WebLinkId

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual translated label of the custom link. Label is **Translation** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the WebLink that is being translated.

Use this object to translate your custom links to URLs or s-controls into the different languages supported by Salesforce. Users with the
Translation Workbench enabled can view custom link translations, but either the “Customize Application” or “Manage Translation”
permission is required to create or update custom link translations.

SEE ALSO:

CategoryNodeLocalization

ScontrolLocalization

### WebStore

Represents a B2B or D2C store. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete(),describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must:

**•** Have CRUD read permission to access this object


Standard Objects WebStore

**•** Be a Salesforce admin with CRUD create permission to create a new record in this object

Fields

**Field** **Details**

```
CheckoutTimeToLive

CheckoutValidAfterDate

Country

CurrencyIsoCode

DefaultLanguage

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Amount of time in minutes that a B2B checkout stays active and doesn’t expire. If you use a
`Null` value, your checkout never expires. If you use a `0` value, checkout is disabled. This
field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A timestamp in the default server timezone (GMT). All B2B checkouts that start before this
date are considered expired. A `Null` value means that all checkouts are valid. Example
format: 2020-07-14T14:27:00.000Z. This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Two-digit ISO code of the store's country. Purchases can be shipped only to the country
assigned to the store. This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
picklist


Standard Objects WebStore

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The primary supported language for your store.

Possible values include:

**•** `da`                   - Danish

**•** `de`                   - German

**•** `en_US`                   - English

**•** `es`                   - Spanish

**•** `en_MX`                   - Spanish (Mexico)

**•** `fi`                   - Finnish

**•** `fr`                   - French

**•** `it`                   - Italian

**•** `ja`                   - Japanese

**•** `ko`                   - Korean

**•** `nl_NL`                   - Dutch

**•** `no`                   - Norwegian

**•** `pt_BR`                   - Portuguese (Brazil)

**•** `ru`                   - Russian

**•** `sv`                   - Swedish

**•** `th`                   - Thai

**•** `zh_CN`                   - Chinese (Simplified)

**•** `zh_TW`                   - Chinese (Traditional)

```
DefaultTaxLocaleType

DefaultTaxPolicyId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Tax type of the store. This field is available in API version 55.0 and later.

Possible values include:

**•** `Gross`  - Prices include tax

**•** `Net`  - Prices don't include tax

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WebStore

**Field** **Details**

**Description**
The default tax policy for the store. This field is a relationship field. This field is available in
API version 56.0 and later.

**Relationship Name**
DefaultTaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

```
Description

ExternalReference

GuestBuyerProfileId

GuestCartTimeToLive

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the store.

**Type**
textarea

**Properties**
Nillable

**Description**
Identifies the instance of B2C Commerce. Format is `<<SiteId>>@<<InstanceId>>.`
This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the GuestBuyerProfile associated with the store. GuestBuyerProfile determines what
buyer groups are part of the profile. The guest buyer groups then determine the entitlements
and pricing of products for the guest buyer.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The time that a guest cart is to remain valid before it expires. The default value is 168 hours
(7 days), and the maximum value is 720 hours (30 days). This field is available in API version
52.0 and later.


Standard Objects WebStore

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationId

MaxValuesPerFacet

Name

OptionsAutoFacetingEnabled

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
record might only have been referenced and not viewed directly.

**Type**
reference

**Properties**
Filter, Group, Nillible, Sort

**Description**
The location associated with the address.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of values that can be added to a facet.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the catalog.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects WebStore

**Field** **Details**

**Description**
If enabled (True), the most relevant search facets are automatically returned, in addition to
the configured search facets, in the product search results. If disabled (False), only the
configured search facets are returned. The default is `False` [.See Add Product Search Filters](https://help.salesforce.com/s/articleView?id=commerce.comm_search_add_filters.htm&type=5&language=en_US)
[(Facets).for more information. This field is available in API version 50.0 or later.](https://help.salesforce.com/s/articleView?id=commerce.comm_search_add_filters.htm&type=5&language=en_US)

```
OptionsCartAsyncProcessingEnabled

OptionsCartCalculateEnabled

OptionsCartToOrderAutoCustomFieldMapping

OptionsDuplicateCartItemsEnabled

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether add-to-cart requests are processed asynchronously ( `True` ) or not ( `False` ).
The default value is `True` . This field is available in API version 59.0 or later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the cart calculate extension is enabled ( `True` ) or not ( `False` ). The default
value is `False` .

This field is available in API version 59.0 or later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether custom field mapping for cart and order objects is enabled ( `True` ) or not
( `False` ). The default value is `True` .

This field is available in API version 57.0 or later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether a cart can include multiple items with the same product ID (True) or not
(False). The default value is `False` .

This field is available in API version 59.0 or later.


Standard Objects WebStore

**Field** **Details**

```
OptionsGuestBrowsingEnabled

OptionsGuestCartEnabled

OptionsGuestCheckoutEnabled

OptionsPreserveGuestCartEnabled

OptionsSkipAdditionalEntitlementCheckForSearch

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest browsing is enabled for this store. Set the option to `True` to allow
guest buyers access to products in the store.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest cart access is enabled for a store created with an LWR template. Set
the option to `True` to allow guest buyers access to products in the store.

This field is available in API version 58.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest checkout access is enabled for a store created with an LWR template.
Set the option to `True` to allow guest buyers access to products in the store.

This field is available in API version 58.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether cart contents are preserved when a guest logs in to the store. Set the
option to `True` to preserve guest carts.

This field is available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects WebStore

**Field** **Details**

**Description**
By default, user entitlement checks are run as part of a search index rebuild and again when
product search results are returned. Skips the second check to promote faster search
performance. Set the option to `True` to skip additional entitlement checks on a search.
This field is available in API version 52.0 and later.

```
OrderActivationStatus

OrderLifeCycleType

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the order. This field is available in API version 55.0 and later.

Possible values are:

**•** `Activated`

**•** `Draft`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether order summaries are processed with Order Management features:

**•** `Managed`  

**•** `Unmanaged`  

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates the owner of the store. This field is available in API 53.0 or later.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects WebStore

**Field** **Details**

```
PaginationSize

PricingStrategy

ProductGrouping

SortByPriceBookId

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Dimensions of the page.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `LowestPrice`  - Best Price

**•** `Priority`  - Priority Price.

The default value is `LowestPrice` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether product variations are listed individually in search results or are
represented by the parent product, which links to its children. Possible values are:

**•** `NoGrouping` —Variations are listed individually in search results.

**•** `VariationParent` —The parent product is returned in search results with a link to
its children.

The default value is `VariationParent` .

This field is available in API version 52.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the price book used for the sorting rule. This field is available in API version 55.0
and later.

This is a relationship field.

**Relationship Name**
SortByPriceBook


Standard Objects WebStore

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
StrikethroughPricebookId

SupportedCurrencies

SupportedLanguages

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the strikethrough price book.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**
Currencies supported in the store.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**
Languages supported in the store.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Type of store that can be created.

Possible values are:

**•** `B2B`

**•** `B2C`

**•** `B2CE`

**•** `OMS`

The default value is `B2B` .


### Standard Objects WebstoreBuyerGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebStoreEvent (API version 55.0)**
Change events are available for the object.

SEE ALSO:

WebStoreNetwork

### WebstoreBuyerGroup

Associates a webstore with a buyer group. Supports dynamically changing locales when buyers shop in orgs that are enabled for multiple
languages and currencies. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BuyerGroupId

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the buyer group this record references.

This field is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects WebstoreBuyerGroup

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

Name

WebStoreId

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the webstore.

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore

This object can support a localized buyer experience by associating a Market-enabled webstore with a buyer group, allowing shoppers
to view their group entitlements, price books, and promotions in localized languages and currencies.


### Standard Objects WebStoreCatalog

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebstoreBuyerGroupChangeEvent on page 68**
Change events are available for the object.

**WebstoreBuyerGroupFeed on page 55**
Feed tracking is available for the object.

**WebstoreBuyerGroupHistory on page 63**
History is available for tracked fields of the object.

**WebstoreBuyerGroupOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WebstoreBuyerGroupShare on page 67**
Sharing is available for the object.

### WebStoreCatalog

Represents the collection of products associated with a store. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete(), describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access product media.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `GBP`  - British Pound

**•** `USD`  - U.S. Dollar

The default value is `USD` .


Standard Objects WebStoreCatalog

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

ProductCatalogId

SalesStoreId

```

Associated Objects

**WebStoreCatalogHistory**

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
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the catalog.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the catalog, containing products.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store that the catalog is associated with. This field is unique within your org.

History is available for tracked fields of the object.


### Standard Objects WebStoreInventorySource WebStoreInventorySource

Used to configure the inventory source for a webstore. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DoesAllowGuestInventoryLevel

InventoryCacheTtl

InventoryDimension

IsBopisEnabled

```

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates whether guest users can view a product’s inventory levels when guest checkout
is disabled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Amount of time in seconds before cache expires.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies which field within inventory levels to use to determine availability.

Possible values are `AvailableToFulfill,AvailableToOrder,OnHand` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the location supports buy online, pick up in store.

The default value is `false` .


Standard Objects WebStoreInventorySource

**Field** **Details**

```
IsChkInvOnActiveCartEnabled

IsDefault

IsEnabled

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the inventory is checked when a customer adds or edits an item in the
active cart.

If an admin wants to enable the inventory check feature for their store, they must set this
value to `true` .

The default value is `true` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default inventory source value ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the default inventory source is active.

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

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.


Standard Objects WebStoreInventorySource

**Field** **Details**

```
LocationSourceExtRef

LocationSourceId

Name

ReservationDurationInSeconds

ShowGuestInventoryLevel

```

**Type**
string

**Properties**
Group, Nillable

**Description**
The external reference identifier associated with the `LocationSourceId` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location ID or location group ID for this webstore.

This field is a polymorphic relationship field.

**Relationship Name**
LocationSource

**Relationship Type**
Lookup

**Refers To**
Location, LocationGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The source name for this entity.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time in seconds that a reservation stays active and doesn’t expire. Required
for implementations using Omnichannel Inventory.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects WebStoreMessageContent

**Field** **Details**

**Description**
Displays the inventory level to guest users, even when guest checkout is disabled.

The default value is `false` .

This field is available in API version 65.0 and later.

```
WebStoreId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique store ID related to this inventory source.

This field is a relationship field.

**Relationship Name**
### WebStore

**Relationship Type**
Lookup

**Refers To**
### WebStore

### WebStoreMessageContent

Represents the assocation of a managed content message record in CMS to a web store, along with other attributes that specify the
application and intent of the message content. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Special Access Rules

This object is available only if a B2B Commerce or D2C Commerce license is enabled.


Standard Objects WebStoreMessageContent

Fields

**Field** **Details**

```
IsActive

ManagedContentId

MessageApp

MessageUsage

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this message content is active (true) or not (false).

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the managed content in CMS.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Refers To**
ManagedContent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The application type that uses the message content.

Possible values are:

**•** `Email`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The usage type of the message content.

Possible values are:

**•** `AbandonedCart`

**•** `OrderConfirmation`


### Standard Objects WebStoreNetwork

**Field** **Details**

```
Name

WebStoreId

### WebStoreNetwork

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the message content.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the web store.

This field is a relationship field.

**Relationship Name**
### WebStore

**Relationship Type**
Master-detail

**Refers To**
WebStore (the master object)

Represents the relationship between a web store and an experience site. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

You must:

**•** Have CRUD read permission to access this object

**•** Be a Salesforce admin with CRUD create permission to create a new record in this object


Standard Objects WebStoreNetwork

Fields

**Field** **Details**

```
Name

NetworkId

WebStoreId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the web store network.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the experience site associated with the web store.

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the web store associated with the experience site.

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore


### Standard Objects WebStorePricebook

Usage

After you copy web store data between a sandbox and production, or between sandboxes, you can programmatically associate the
copy with a different site by updating the corresponding WebStoreNetwork record. You can even change the association while the store
is active. The site must use a template that’s compatible with the web store type, and the site can’t be associated with a store. Otherwise,
you can change the association only by editing the web store in the UI.

SEE ALSO:

Network

### WebStore WebStorePricebook

Represents a store price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
IsActive

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the WebStorePricebook is active ( `true` ) or not ( `false` ). Default value
is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects WebStorePricebook

**Field** **Details**

```
LastViewedDate

Name

Pricebook2Id

WebStoreId

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
The name of the store price book record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book assigned to the store.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store assigned to the price book.

Use the WebStorePricebook object to assign price books to a store. When you assign a price book to a web store, any buyer who has
access to the store can price products from the assigned price books. When a store or buyer has multiple price book assignments,
including prices to the same product, the price is determined by the pricing strategy of the store.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WebStorePricebookFeed**

Feed tracking is available for this object.


### Standard Objects WebStoreSearchProdSettings WebStoreSearchProdSettings

Search settings for a WebStore product search. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

You must have a B2B Commerce or D2C Commerce commerce license to create a web store.

Fields

**Field** **Details**

```
CurrencyIsoCode

IsExcludedFromSearch

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for the store’s currency.

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the product is excluded from searches.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the search settings for the WebStore product search.


### Standard Objects WebStoreShare

**Field** **Details**

```
ProductId

WebStoreId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product to search.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Webstore to search.

This field is a relationship field.

**Relationship Name**
### WebStore

**Relationship Type**
Lookup

**Refers To**
### WebStore

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebStoreSearchProdSettingsChangeEvent on page 68**
Change events are available for the object.

### WebStoreShare

Represents a sharing entry on a B2B or D2C store. This object is available in API version 45.0 and later.


Standard Objects WebStoreShare

Supported Calls

`create()`, `delete(),`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Your Salesforce admin can manage this object using standard Salesforce sharing rules and CRUD access for the WebStore.

Fields

**Field** **Details**

```
AccessLevel

ParentId

RowCause

```

**Type**

**picklist**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing allowed.

Possible values are:

**•** `All` —Owner

**•** `Edit` —Read/Write

**•** `Read` —Read Only

**Type**

**reference**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent folder for the record.

This field is a relationship field.

**Relationship Name**
Parent

**Refers To**
WebStore

**Type**

**picklist**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects WebStoreShare

**Field** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `ALMAssignmentSharing` —Actionable List Member Sharing Rule

**•** `CompliantDataSharing` —Compliant Data Sharing

**•** `GuestParentImplicit` —Associated guest user sharing

**•** `GuestPersonImplicit` —Associated Guest User Sharing

**•** `GuestRule` —Guest User Sharing Rule

**•** `ImplicitChild` —Account Sharing

**•** `ImplicitParent` —Associated record owner or sharing

**•** `ImplicitPerson` —Person Contact

**•** `LearningAssignment` —Learning Assignment Share

**•** `LearningAssignmentImplicit` —Learning Assignment Implicit Share

**•** `LearningItemAssignment` —Learning Item Assignment Share

**•** `Manual` —Manual Sharing

**•** `MfgTargetShare` —Manufacturing Target Sharing Rule

**•** `ObligationAssigneeShare` —Obligation Assignee Share

**•** `Owner`

**•** `Rule` —Sharing Rule

**•** `SharingRecordCollection` —Record Collection

**•** `SurveyShare` —Survey Sharing Rule

**•** `Team` —Sales Team

**•** `Territory` —Territory Assignment Rule

**•** `Territory2AssociationManual` —Territory Manual

**•** `Territory2Forecast` —Territory assignment for forecasting and reporting

**•** `Territory2SplitsForecast` —Territory Splits Share

**•** `TerritoryManual` —Territory Manual

**•** `TerritoryRule` —Territory Sharing Rule

```
UserOrGroupId

```

**Type**

**reference**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the User. This field can’t be updated.

This field is a polymorphic relationship field.


### Standard Objects Wishlist

**Field** **Details**

**Relationship Name**
UserOrGroup

**Refers To**
Group, User

### Wishlist Represents a buyer-created list of WishlistItem s in a store that’s built with B2B Commerce on Lightning. Available in API version

49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The Wishlist object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AccountId

CurrencyIsoCode

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
### The ID of the account that owns the Wishlist .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string


Standard Objects Wishlist

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `Wishlist` record. `Name` can be up to 255 characters.

```
OwnerId

WebStoreId

WishlistProductCount

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user or group that owns the `Wishlist` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the `WebStore` related to this `Wishlist` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The count of `WishlistItem` s on this `Wishlist` . `WishlistProductCount` is a
calculated field.

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WishlistOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WishlistShare on page 67**
Sharing is available for the object.

Usage Notes

**•** Wishlists aren’t included in any searches.

SEE ALSO:

WishlistItem


### Standard Objects WishlistItem WishlistItem Represents an item on a Wishlist in a store built with B2B Commerce for Lightning. Available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The WishListItem object is available only if the B2B Commerce for Lightning license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

Product2Id

WishlistId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is
`USD` .Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
### The name of this WishlistItem record. Name can be up to 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
### The ID of the product that is represented by the WishlistItem .

**Type**
reference


### Standard Objects WorkAccess

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent `Wishlist` of this `WishlistItem` .

SEE ALSO:

Wishlist

### WorkAccess

Used to grant or restrict user access to give badge definitions. Each badge definition record must have one WorkAccess record.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Additional Considerations and Related Objects

### WorkAccess is not available through Schema Builder and is not customizable. A WorkAccess record is required for users to Give

BadgeDefinitions. If a WorkAccess record is not created, BadgeDefinitions will not be available to users.

The sharing of WorkAccess records is through WorkAccessShare. For each WorkBadgeDefinition record, you must create both a WorkAccess
record (per WorkBadgeDefinition) and WorkAccessShare records for sharing to users or groups.

Fields

**Field Name** **Details**

```
AccessType

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Define the type of Access given to user (“Give”).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects WorkAccessShare

**Field Name** **Details**

**Description**
Salesforce unique ID for owner of Access record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ParentId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID for BadgeDefinition record associated with this Access record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
WorkBadgeDefinition

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkAccessChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkAccessOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

### **WorkAccessShare**

Sharing is available for the object.

### WorkAccessShare

Used to control Givers of WorkBadgeDefinition records.


Standard Objects WorkAccessShare

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Additional Considerations and Related Objects

[Related to WorkAccess Object. WorkAccess is the parent of WorkAccessShare.](https://docs.google.com/a/salesforce.com/document/d/11IkXSCNKBD_04YlyOPvWS94iyVeQ7zN98M03LdcW4eM/edit#bookmark=id.7idtv3rbjtcr)

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

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
CRUD Access Level (picklist values: Read Only, Read/Write, Owner).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID for WorkAccess record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
WorkAccess


### Standard Objects WorkBadge

**Field Name** **Details**

```
RowCause

UserOrGroupId

### WorkBadge

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

Values can include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the WorkAccess with them.

**•** `Owner` —The User is the owner of the WorkAccess or is in a role above the
WorkAccess owner in the role hierarchy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
User or Group ID for WorkAccess.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Represents information about who the badge was given to and which badge was given. A WorkBadge record is created for each recipient
of a WorkBadgeDefinition.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkBadge

Additional Considerations and Related Objects

WorkBadge is a lookup to WorkThanks. Each WorkBadge record must derive a SourceId from WorkThanks. There can be multiple
WorkBadge records tied to a single WorkThanks record.

Fields

**Field Name** **Details**

```
DefinitionId

Description

GiverId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Salesforce unique ID for the given WorkBadgeDefinition record given.

This is a relationship field.

**Relationship Name**
Definition

**Relationship Type**
Lookup

**Refers To**
WorkBadgeDefinition

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the WorkBadgeDefinition.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the badge giver. Can’t be the same as `RecipientId` .

This is a relationship field.

**Relationship Name**
Giver

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects WorkBadge

**Field Name** **Details**

```
ImageUrl

LastReferencedDate

LastViewedDate

Message

NetworkId

RecipientId

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the badge image.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkBadge.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this WorkBadge.
If this value is null, this record might have been only referenced
( `LastReferencedDate` ) and not viewed.

**Type**
textarea

**Properties**
Nillable

**Description**
The message accompanying the thanks badge.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the community that this WorkBadge is associated with. This field is
available only if digital experiences is enabled in your org.

**Type**
reference


Standard Objects WorkBadge

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Salesforce unique ID for User who is the Recipient of Badge. Can’t be
the same as `GiverId`

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
User

```
RewardId

SourceId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce unique ID for Reward given with badge (if Reward Badge)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce unique ID for Thanks record referenced to this badge.

This is a relationship field.

**Relationship Name**
Source

**Relationship Type**
Lookup

**Refers To**
WorkThanks

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkBadgeChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects WorkBadgeDefinition WorkBadgeDefinition

Represents the attributes of a badge including the badge name, description, and image. Each WorkBadge record must have a lookup
to a WorkBadgeDefinition since badge attributes (like badge name) are derived from the WorkBadgeDefinition object.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Additional Considerations and Related Objects

### WorkBadgeDefinition has a field called ImageUrl that references a DocumentID. This is a required field for creating a Badge.

To grant “giver” access to a WorkBadgeDefinition, you must also create the WorkAccess (and the related WorkAccessShare records.

Each WorkBadgeDefinition has an `ImageUrl` field that must be populated with a DocumentID of the Document record containing
the badge image.

Fields

**Field Name** **Details**

```
Description

GivenBadgeCount

ImageUrl

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. Limit: 4000 characters. The description of the badge and what it means
to receive this badge.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of badges given per user or across all users.

Note: This field can’t be added in a list view or referenced in a formula
field.

**Type**
url

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects WorkBadgeDefinition

**Field Name** **Details**

**Description**
Required. This is the badge image that will be displayed in the UI. Use DocumentID
or ImageURL.

```
IsActive

IsCompanyWide

IsLimitPerUser

IsRewardBadge

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents whether a WorkBadgeDefinition is active and available in the UI and
API.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents a special class of badges known as Company Badges. Company
badges are visible to the entire company and visible in specific list view filters.

Note: If this field is selected, everyone within the user’s network will be
able to give the badge automatically. If this field is not selected, people
with sharing must be added to the badge’s access list in order to give the
badge.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the badge limit is per user ( `true` ) or across all users ( `false` ).
The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the badge is a reward badge ( `true` ) or not ( `false` ).

**Type**
dateTime


Standard Objects WorkBadgeDefinition

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkBadgeDefinition.

```
LastViewedDate

LimitNumber

LimitStartDate

Name

NetworkId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkBadgeDefinition. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The badge limit per user or across all users.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the badge limit. The date can be reset to the current date.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the Badge. **Label:** Badge Title.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkBadgeDefinition

**Field Name** **Details**

**Description**
The ID of the community that this WorkBadgeDefinition is associated with. This
field is available only if digital experiences is enabled in your org.

```
OwnerId

RewardFundId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce User ID for User who is the Owner of the WorkBadgeDefinition record
(usually the creator of the record)

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
Salesforce unique ID for the WorkRewardFund that is associated with this
WorkBadgeDefinition. WorkBadgeDefinition records with a RewardFundID indicate
a Reward Badge.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkBadgeDefinitionChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkBadgeDefinitionFeed**

Feed tracking is available for the object.

**WorkBadgeDefinitionHistory**

History is available for tracked fields of the object.

**WorkBadgeDefinitionOwnerSharingRule**

Sharing rules are available for the object.

**WorkBadgeDefinitionShare**

Sharing is available for the object.


### Standard Objects WorkCapacityAvailability WorkCapacityAvailability

Represents the available work capacity for a specific time and service territory. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AvailCapacityHours

AvailCapacityMinutes

EndDate

LastReferencedDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of available capacity in hours in the time frame the user defined for a service
territory.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of available capacity in minutes in the time frame the user defined for a service
territory.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the total available capacity.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.


Standard Objects WorkCapacityAvailability

**Field** **Details**

```
LastViewedDate

OwnerId

ServiceTerritoryId

StartDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this object.

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
The ID of the service territory of the work capacity availability calculation.

This field is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects WorkCapacityLimit

**Field** **Details**

**Description**
The start date of the total available capacity.

```
TimePeriod

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period the user selected when creating the work capacity limit. The value is copied
from the `TimePeriod` field of the WorkCapacityLimit object.

Possible values are:

**•** `Day`

The default value is `Day` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityAvailabilityFeed on page 55**
Feed tracking is available for the object.

**WorkCapacityAvailabilityShare on page 67**
Sharing is available for the object.

### WorkCapacityLimit

Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This object
is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CapacityLimitRelaxation

```

**Type**
string


Standard Objects WorkCapacityLimit

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the relaxation behavior that determines the limit override policy for this limit if the
limit override policy is set per limit in Field Service Settings. If the limit override policy isn’t
set per limit, this value is ignored. Valid strings are:

**•** Empty value - no limit override

**•** 0 - limit override starts at midnight on the day of service

**•** Positive integer - limit override starts this number of hours after midnight. the maximum
value is 23.

**•** Negative integer - limit override starts this number of hours before midnight. The
maximum value is 336.

```
Description

EndDate

IsActive

IsFriday

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the work capacity limit.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
End date of the work capacity limit. If no `EndDate` is set this work capacity limit is without
an expiration date.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the work capacity limit is active or inactive. When creating a record, save
the record, and then activate it. You can't update fields in an active record.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects WorkCapacityLimit

**Field** **Details**

**Description**
Indicates whether the limitation is applied on Fridays.

The default value is `false` .

```
IsMonday

IsSaturday

IsSunday

IsSvcTerrOnlyLimit

IsThursday

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Mondays.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Saturdays.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Sundays.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Apply this work capacity limit to the entire service territory.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects WorkCapacityLimit

**Field** **Details**

**Description**
Indicates whether the limitation is applied on Thursdays.

The default value is `false` .

```
IsTuesday

IsWednesday

LastReferencedDate

LastViewedDate

LimitationUnits

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Tuesdays.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Wednesdays.

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
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects WorkCapacityLimit

**Field** **Details**

**Description**
Unit of the `LimitationValue` .

Possible values are:

**•** `Hours`

**•** `Percentage`

The default value is `Hours` .

```
LimitationValue

OwnerId

ServiceTerritoryId

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
If the `LimitationUnits` is `Hours`, `LimitationValue` is the threshold that
represents how many hours of total work capacity can be scheduled for a specific workstream
in a service territory. Enter the number of hours for the daily limitation as a whole number.

If the `LimitationUnits` is `Percentage` this threshold represents the percentage
of the total work capacity that can be scheduled for a specific workstream in a service territory.
Enter the percentage for the daily limitation as a whole number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of the work capacity limit.

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
ID of the service territory of the work capacity workstream for which the limit is defined.

This field is a relationship field.


Standard Objects WorkCapacityLimit

**Field** **Details**

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
StartDate

SvcApptField

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The start date of the Work Capacity Limit.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Work-specific criteria used to define the capacity limit for the workstream. The service
appointment field is set for the organization when the first work capacity limit instance is
created.

Possible values are:

**•** `ServiceAppointment.AccountId`

**•** `ServiceAppointment.ActualDuration` —Actual duration (in minutes)

**•** `ServiceAppointment.Duration` —Duration

**•** `ServiceAppointment.DurationInMinutes`

**•** `ServiceAppointment.FSL__Appointment_Grade__c` e

**•** `ServiceAppointment.FSL__Auto_Schedule__c`

**•** `ServiceAppointment.FSL__Duration_In_Minutes__c` —Scheduled
duration

**•** `ServiceAppointment.FSL__Emergency__c`

**•** `ServiceAppointment.FSL__GanttColor__c`

**•** `ServiceAppointment.FSL__GanttLabel__c`

**•** `ServiceAppointment.FSL__InJeopardyReason__c`

**•** `ServiceAppointment.FSL__InJeopardy__c`

**•** `ServiceAppointment.FSL__IsFillInCandidate__c`

**•** `ServiceAppointment.FSL__IsMultiDay__c`

**•** `ServiceAppointment.FSL__Last_Updated_Epoch__c`


Standard Objects WorkCapacityLimit

**Field** **Details**

**•** `ServiceAppointment.FSL__MDS_Calculated_length__c` —Multiday
work calculated length

**•** `ServiceAppointment.FSL__Pinned__c`

**•** `ServiceAppointment.FSL__Prevent_Geocoding_For_Chatter_Actions__c`

**•** `ServiceAppointment.FSL__Related_Service__c`

**•** `ServiceAppointment.FSL__Same_Day__c`

**•** `ServiceAppointment.FSL__Same_Resource__c`

**•** `ServiceAppointment.FSL__Schedule_Mode__c`

**•** `ServiceAppointment.FSL__Schedule_over_lower_priority_appointment__c`

**•** `ServiceAppointment.FSL__Scheduling_Policy_Used__c`

**•** `ServiceAppointment.FSL__Time_Dependency__c`

**•** `ServiceAppointment.FSL__UpdatedByOptimization__c`

**•** `ServiceAppointment.FSL__Use_Async_Logic__c`

**•** `ServiceAppointment.FSL__Virtual_Service_For_Chatter_Action__c`

**•** `ServiceAppointment.IsOffsiteAppointment`

**•** `ServiceAppointment.Subject`

**•** `ServiceAppointment.WorkTypeId` —Work Type ID

```
SvcApptFieldValDplyNm

SvcApptFieldValue

TimePeriod

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The workstream display name of `SvcApptFieldValue` . If `SvcApptField` is a lookup
to a service appointment, `SvcApptFieldValue` is an ID and the display name describes
the value for the user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of `SvcApptField`, the work-specific criteria of the capacity limit.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Duration for defining the capacity limitation on the workstream in the service territory.


### Standard Objects WorkCapacityUsage

**Field** **Details**

Possible values are:

**•** `Day`

The default value is `Day` .

```
WorkCapacityLimitNumber

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto populated, unique identifying number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityLimitChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkCapacityLimitFeed on page 55**
Feed tracking is available for the object.

**WorkCapacityLimitHistory on page 63**
History is available for tracked fields of the object.

**WorkCapacityLimitShare on page 67**
Sharing is available for the object.

### WorkCapacityUsage

Represents the capacity usage in a specific service territory for a workstream or for the whole service territory in a given period. This
object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AvailCapacityHours

```

**Type**
double


Standard Objects WorkCapacityUsage

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
This value is copied from the `AvailCapacityHours` of the WorkCapacityAvailability
object for the service territory on the same date.

```
CapacityLimitRelaxation

ConsumptionToLimitRatio

EndDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the relaxation behavior that determines the limit override policy for this limit if the
limit override policy is set per limit in Field Service Settings. If the limit override policy isn’t
set per limit, this value is ignored. Valid strings are:

**•** Empty value - no limit override

**•** 0 - limit override starts at midnight on the day of service

**•** Positive integer - limit override starts this number of hours after midnight. the maximum
value is 23.

**•** Negative integer - limit override starts this number of hours before midnight. The
maximum value is 336.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
(Time consumed in hours / Limit in hours) * 100

Note the following exceptions.

**•** If a limit isn’t defined (-1) the ratio is -1 (even if consumption is 0 or higher).

**•** If consumption is 0, and the limit is a number greater than 0, then the ration is 0.

**•** If consumption is 0 and the limit is 0, the ration is 100% hard-coded.

**•** If consumption is greater than 0 and the limit is 0, the ration is calculated as if the limit
= 0.99 in order to get a result that’s higher than 100%.

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
End date of the time period for which the capacity usage is accumulated.


Standard Objects WorkCapacityUsage

**Field** **Details**

```
IsSvcTerrOnlyLimit

LastReferencedDate

LastViewedDate

LimitationPercentage

LimitationUnits

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Applies this work capacity limit to the entire service territory.

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
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
If the `LimitationUnits` is `Percentage` this value is copied from the
`LimitationValue` field of the WorkCapacityLimit object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the limitation for the workstream in the service territory is in hours or as a
percentage of all the available hours for all the workstreams for which limitations exist in the
service territory on a specific day.

Possible values are:


Standard Objects WorkCapacityUsage

**Field** **Details**

**•** `Hours`

**•** `Percentage`

The default value is `Hours` .

```
LimitationValue

OriginalLimit

OwnerId

ServiceTerritoryId

```

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
The `LimitationValue` depends on the LimitationUnit. If the `LimitationUnit` is
Hours the value is copied from `LimitationValue` in the WorkCapacityLimit object. If
the `LimitationUnit` is Percentage, the percentage is calculated relative to the availability
in the WorkCapacityAvailability object.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
If the limit value is changed after the work capacity usage was created, this parameter is the
original value.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

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


Standard Objects WorkCapacityUsage

**Field** **Details**

**Description**
ID of the service territory of the work capacity workstream for which usage is accumulated.

This field is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
StartDate

SvcApptField

```

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
Start date of the time period for which the capacity usage is accumulated.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Work-specific criteria used to define the capacity limit for the workstream.

Possible values are:

**•** `ServiceAppointment.AccountId`

**•** `ServiceAppointment.ActualDuration` —Actual duration (in minutes)

**•** `ServiceAppointment.Duration` —Duration

**•** `ServiceAppointment.DurationInMinutes`

**•** `ServiceAppointment.FSL__Appointment_Grade__c` e

**•** `ServiceAppointment.FSL__Auto_Schedule__c`

**•** `ServiceAppointment.FSL__Duration_In_Minutes__c` —Scheduled
duration

**•** `ServiceAppointment.FSL__Emergency__c`

**•** `ServiceAppointment.FSL__GanttColor__c`

**•** `ServiceAppointment.FSL__GanttLabel__c`

**•** `ServiceAppointment.FSL__InJeopardyReason__c`

**•** `ServiceAppointment.FSL__InJeopardy__c`

**•** `ServiceAppointment.FSL__IsFillInCandidate__c`

**•** `ServiceAppointment.FSL__IsMultiDay__c`


Standard Objects WorkCapacityUsage

**Field** **Details**

**•** `ServiceAppointment.FSL__Last_Updated_Epoch__c`

**•** `ServiceAppointment.FSL__MDS_Calculated_length__c` —Multiday
work calculated length

**•** `ServiceAppointment.FSL__Pinned__c`

**•** `ServiceAppointment.FSL__Prevent_Geocoding_For_Chatter_Actions__c`

**•** `ServiceAppointment.FSL__Related_Service__c`

**•** `ServiceAppointment.FSL__Same_Day__c`

**•** `ServiceAppointment.FSL__Same_Resource__c`

**•** `ServiceAppointment.FSL__Schedule_Mode__c`

**•** `ServiceAppointment.FSL__Schedule_over_lower_priority_appointment__c`

**•** `ServiceAppointment.FSL__Scheduling_Policy_Used__c`

**•** `ServiceAppointment.FSL__Time_Dependency__c`

**•** `ServiceAppointment.FSL__UpdatedByOptimization__c`

**•** `ServiceAppointment.FSL__Use_Async_Logic__c`

**•** `ServiceAppointment.FSL__Virtual_Service_For_Chatter_Action__c`

**•** `ServiceAppointment.IsOffsiteAppointment`

**•** `ServiceAppointment.Subject`

**•** `ServiceAppointment.WorkTypeId` —Work Type ID

```
SvcApptFieldValDplyNm

SvcApptFieldValue

TimeConsumedInHours

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Workstream display name of `SvcApptFieldValue` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Value of `SvcApptField`, the work-specific criteria of the capacity limit.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Time consumed in hours by the workstream in the service territory for the defined period.
This value is calculated by dividing `TimeConsumedInMinutes` by 60.


Standard Objects WorkCapacityUsage

**Field** **Details**

```
TimeConsumedInMinutes

TimePeriod

WcuUniqueField1

WcuUniqueField2

WorkCapacityUsageNumber

```

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Time consumed in minutes by the workstream in the service territory for the defined period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Duration for defining the capacity limitation on the workstream in the service territory.

Possible values are:

**•** `Day`

The default value is `Day` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Read-only. Auto populated, unique identifying number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Read-only. Auto populated, unique identifying number.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto populated, unique identifying number.


### Standard Objects WorkCoaching

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityUsageFeed on page 55**
Feed tracking is available for the object.

**WorkCapacityUsageShare on page 67**
Sharing is available for the object.

### WorkCoaching

Represents a single coaching relationship between two users. One of the users is defined as the coach and the other is defined as a
coachee. WorkCoaching is feed-enabled so there is a private feed available to the coach and coachee.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CoachId

CoachedId

IsInactive

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

[Required] The coach in this 1:1 coaching relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

[Required] The user being coached in this 1:1 coaching relationship.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the coaching relationship is _`Inactive`_ ( `true` ) or not
( `false` ).


Standard Objects WorkCoaching

**Field Name** **Details**

```
LastReferencedDate

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
The time stamp that indicates when the current user last viewed a record that is
related to this coaching relationship.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this coaching
relationship. If this value is null, this record might have been only referenced
( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

[Required] The record’s name. Max length is 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the WorkCoaching record.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkCoachingFeed**

Feed tracking is available for the object.

**WorkCoachingHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)


### Standard Objects WorkDemographic

**WorkCoachingOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkCoachingShare**

Sharing is available for the object.

### WorkDemographic

Represents the field values used to specify slices in the workload forecasting and capacity planning. This object is available in API version
49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.

Fields

**Field** **Details**

```
Channel

CustomWorkType

GroupIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The channel value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Custom dimension value that the user can define other than the channel, region, and skill
dimensions.

**Type**
string


Standard Objects WorkDemographic

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The group or queue associated to a slice when creating an Omni-based workload.

```
JobProfileId

Region

ServiceChannelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the JobProfile object.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The region value.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the ServiceChannel object.

This is a relationship field.

**Relationship Name**
ServiceChannel

**Relationship Type**
Lookup

**Refers To**
ServiceChannel


### Standard Objects WorkFeedback

**Field** **Details**

```
ServiceTerritoryId

SkillSet

### WorkFeedback

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the ServiceTerritory object.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The skill value.

Represents the answer to a question that a person was asked via a feedback request. Also used to store offered feedback without linking
it to a particular question.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Additional Considerations and Related Objects

**•** Ownership is transferred to the requester on submit for certain types (ad-hoc feedback).

**•** The record is read-only after the request that it’s linked to is set to Submitted.

**•** You can’t link a feedback object to a request unless you are the recipient.

**•** The question that the feedback is linked to must be part of the same question set that the request is linked to.


Standard Objects WorkFeedback

Fields

**Field Name** **Details**

```
Feedback

Name

OwnerId

QuestionId

RequestId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains either the free-form text of the answer, or the choice selected by the
user. Max length is 65536.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the WorkFeedback record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedback record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The question this answer applies to. When this feedback is linked to a request of
an unsolicited type, the question ID is null.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the request this response belongs to, in case of offered feedback.


### Standard Objects WorkFeedbackQuestion

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackShare**

Sharing is available for the object.

### WorkFeedbackQuestion

Represents a free-form text type or multiple choice question within a set of questions.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Choices

Detail

IsConfidentialAnswer

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
New-line separated list of valid choices for multiple choice questions. Maximum
length is 1000 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Detailed instructions on how to answer the question.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects WorkFeedbackQuestion

**Field Name** **Details**

**Description**
Answers to questions marked confidential will not be shared with the subject of
the review. This field applies only to performance summaries.

```
IsOptional

Name

Number

OwnerId

QuestionSetId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If this option is selected, the question is optional and isn’t required to be answered.
This field applies only to performance summaries.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A short description of the question, which can be used as a header for reports
and Calibration.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order of the question that is displayed within the question set, such as
question number three in a question set that has five questions.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedbackQuestion.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The question set this question is a part of.


### Standard Objects WorkFeedbackQuestionSet

**Field Name** **Details**

```
Text

Type

```

Associated Objects

**Type**
textarea

**Properties**
Create, Update

**Description**
The body of the question. Max length is 16384 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows for either a free-form text answer or a multiple choice question defined
by new-line separate choices in the ‘Choices’ field. Valid picklist values are:

**•** MultipleChoice

**•** FreeText

**•** Rating

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackQuestionOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackQuestionShare**

Sharing is available for the object.

### WorkFeedbackQuestionSet

Represents a set of questions being asked. The question set is used to link all the individual requests where different recipients were
asked the same set of questions on the same subject.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

In the WDC performance application, a question set defines the type of summaries and their due dates that will accompany the deployment
of a specific performance summary cycle.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkFeedbackQuestionSet

Fields

**Field Name** **Details**

```
DueDate

FeedbackType

Name

OwnerId

PerformanceCycleId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date that this specific question set is expected to be submitted by the
recipient. This field applies only to performance summaries.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The description of the collection of questions that are written in context to the
type of recipient answering them, relative to the subject of the summary. This
field applies only to performance summaries.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the question set. Maximum length is 225 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedbackQuestionSet.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a question set is associated to a performance summary cycle, then that cycle
ID is referenced in this field. This field applies only to performance summaries.


### Standard Objects WorkFeedbackRequest

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackQuestionSetOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackQuestionSetShare**

Sharing is available for the object.

### WorkFeedbackRequest

Represents a single feedback request on a subject or topic (question) to a single recipient in the feedback application. In the case of
offered feedback, WorkFeedbackRequest represents feedback that is offered about a subject. In the performance application,
### WorkFeedbackRequest represents a request for feedback on a set of questions from a question set, on a subject—for the recipient to

complete and submit.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Additional Considerations and Related Objects

**•** After a request’s state is changed to Submitted, fields can’t be changed, except for LastSharedDate and IsUnreadByOwner.

**•** If LastRemindDate is updated, a reminder notification will be sent to the request’s recipient (only possible when request is in Draft
state).

**•** When a new request is created, a notification is sent to the recipient.

**•** When a recipient of a request submits their feedback (Draft->Submitted), a notification will be sent to requester (except for offered
feedback).

**•** Requester cannot modify the subject of the question set after a request is created.

**•** For offered feedback (to user, to manager, or both), the person who is offering feedback is both the creator of WorkFeedbackRequest
as well as the recipient.

Fields

**Field Name** **Details**

```
AdHocFeedback

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the feedback.


Standard Objects WorkFeedbackRequest

**Field Name** **Details**

```
AdHocQuestion

Description

FeedbackRequestState

FeedbackType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the feedback question.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the WorkFeedbackRequest.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current state of the feedback request. Allowed picklist values are:

**•** Draft

**•** Submitted

**•** Declined

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of request. Picklist values that are used for performance
summaries:

**•** Unspecified

**•** Peer Summary

**•** Self Summary

**•** Manager Summary

**•** Skip Level Summary

Picklist values that are used for feedback:

**•** Personal

**•** Unsolicited to User

**•** Unsolicited to Manager


Standard Objects WorkFeedbackRequest

**Field Name** **Details**

**•** Unsolicited to User and Manager

**•** On Topic

The type of the feedback determines the sharing and visibility rules that are
applied to answers.

```
IsDeployed

IsShareWithSubject

IsUnreadByOwner

IsUnsolicited

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the feedback is part of a deployed performance summary cycle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the feedback is shared with the summary subject.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the submitted request has not been seen by the requester.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the feedback request is unsolicited feedback offered to another user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkFeedbackRequest.


Standard Objects WorkFeedbackRequest

**Field Name** **Details**

```
LastRemindDate

LastSharedDate

LastViewedDate

Name

OwnerId

PerformanceCycleId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time a reminder was sent to the recipient of this draft request.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time this request was shared with another user or group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkFeedbackRequest. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkFeedbackRequest.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedbackRequest.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkFeedbackRequest

**Field Name** **Details**

**Description**
Used by performance summaries to link to a summary cycle. This field applies
only to performance summaries.

```
QuestionSetId

RecipientId

RelatedObjectId

SharingScope

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Question set associated with the current request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User asked to provide feedback on the subject.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Specifies a record in the system that this feedback request is related to. Used by
ad-hoc feedback to gather feedback in the context of an opportunity or WDC
goal.

Used by performance summaries to link to a summary cycle.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The users that see the feedback. `SharingScope` can have the following
values:

**•** Nobody

**•** Subject

**•** Manager

**•** SubjectAndManager


### Standard Objects WorkforceCapacity

**Field Name** **Details**

```
SubjectId

SubmitFeedbackToId

SubmittedDate

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user that this request (or offer) is about.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the person this performance summary feedback request (and its
respective answers) is shared with. It’s also the ID of the person who owns the
requested subject’s manager summary request. This field applies only to
performance summaries.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time (in case it was reopened by admin) this request was submitted by
the recipient. This field applies only to performance summaries.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackRequestFeed**

Feed tracking is available for the object.

**WorkFeedbackRequestOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackRequestShare**

Sharing is available for the object.

### WorkforceCapacity

Represents the time series for actual or forecasted workforce allocation. This object is available in API version 51.0 and later.


Standard Objects WorkforceCapacity

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Analyst permission set.

Fields

**Field** **Details**

```
Description

EndDateTime

IsOmni

Name

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the planning.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The end date and time of the planning.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from isOmni field on Workload object. Indicates that the workload is Omni-based.
If workload is null, the field value defaults to `false` .

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the plan.


Standard Objects WorkforceCapacity

**Field** **Details**

```
OwnerId

PlanType

StartDateTime

TimeZone

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the record.

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
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of capacity plan. Possible values are:

**•** `Intraday` —The plan shows intraday management.

**•** `LongTerm` —The plan predicts the required number of full-time employees (FTEs).

**•** `ShortTerm` —The plan predicts the required number of shifts.

This field is available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date and time of the planning.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone associated with the capacity plan. Possible values are the time zones supported
by Workforce Engagement.

This field is available in API version 56.0 and later.


### Standard Objects WorkforceCapacityUnit

**Field** **Details**

```
WorkloadId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The foreign key to the Workload object.

This is a relationship field.

**Relationship Name**
Workload

**Relationship Type**
Lookup

**Refers To**
Workload

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkforceCapacityOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WorkforceCapacityShare on page 67**
Sharing is available for the object.

### WorkforceCapacityUnit

Represents the number of resources allocated or needed for a specific set of work items at a timestamp within a specific duration. This
object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.


Standard Objects WorkforceCapacityUnit

Fields

**Field** **Details**

```
AssignedTotalCount

AvailableTotalCount

Capacity

DateTime

IsOmni

IsShiftTemplateNonStandard

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The number of shifts assigned at specific time period.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total number of shifts scheduled at a specific time period.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Staffing prediction for a capacity plan. This field is available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The timestamp of the data point.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from the isOmni field on WorkforceCapacity. Indicates that the workload is
Omni-based.

The default value is 'false'.

**Type**
boolean


Standard Objects WorkforceCapacityUnit

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift template that’s used at a specific time period is a non-standard
shift. This field is available in API version 53.0 and later.

The default value is `false` .

```
JobProfileName

MaxCount

MeasureUnit

OriginalTotalCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from the WorkDemographic SkillSet field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The max number of resources allocated or needed at a specific time period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time interval (in minutes) used in capacity plans.

Possible values are:

**•** `43200` —Monthly for long-term capacity plans. This value is available in API version
54.0 and later.

**•** `10080` —Weekly

**•** `1440` —Daily

**•** `60` —Hourly

**•** `30` —30 minutes. Reserved for future use.

**•** `15` —15 minutes. Reserved for future use.

The default value is '1440'.

**Type**
int


Standard Objects WorkforceCapacityUnit

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The original total number of resources allocated or needed at specific time period calculated
from the planning process.

```
ResourceGap

ServiceTerritoryName

ShiftTemplateDuration

ShiftTemplateDurationType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the resource gap between the available and required resources.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from the WorkDemographic Region field.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The duration of the shift template that’s used at a specific time period. This field is available
in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the duration of the shift template that’s used at a specific time period is
in minutes or hours. This field is available in API version 53.0 and later.

Possible values are:

**•** `H` —Hours

**•** `M` —Minutes

The default value is `H` .


Standard Objects WorkforceCapacityUnit

**Field** **Details**

```
ShiftTemplateId

ShiftTemplateJobProfile

ShiftTemplateName

ShiftTemplateStartTime

TotalCount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the shift template that’s used at a specific time period. This field is available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The job profile that relates to the shift template that’s used at a specific time period. This
field is available in API version 53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the shift template that’s used at a specific time period. This field is available in API
version 53.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start time of the shift template that’s used at a specific time period. This field is available
in API version 53.0 and later.

**Type**
int


### Standard Objects WorkGoal

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of resources allocated or needed at specific time period. It represents the
updated count after the adjustment. This value is the same as `OriginalTotalCount`
if no adjustments were made.

This is a calculated field.

```
WorkDemographicId

WorkforceCapacityId

### WorkGoal

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The foreign key to WorkDemographic object.

This is a relationship field.

**Relationship Name**
WorkDemographic

**Relationship Type**
Lookup

**Refers To**
WorkDemographic

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The foreign key to WorkCapacity object.

This is a relationship field.

**Relationship Name**
WorkforceCapacity

**Relationship Type**
Lookup

**Refers To**
WorkforceCapacity

Represents the components of a goal, such as its description and associated metrics. This object has been deprecated as of API version
35.0. Use the Goal object to query information about WDC goals.


Standard Objects WorkGoal

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Related

WorkGoalCollaborator, WorkGoalLink, WorkGoalFeed

Fields

**Field Name** **Details**

```
ActualValue

ActualValueExternalUrl

CompletionDate

Description

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual value of the WorkGoal metric. Applicable only to WorkGoal objects of
`Type` : Metric.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a URL that references WDC data synchronization for the actual value of
a metric. Applicable only to WorkGoal objects of `Type` : Metric.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the goal.

Note: Field-level security limits access to only administrators and owners
by default, and only they can complete a goal.

**Type**
textarea (max length 4000)


Standard Objects WorkGoal

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the goal.

```
DueDate

FlaggedAs

ImageUrl

InitialValue

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the WorkGoal object is due (optional). Applicable only to WorkGoal
objects of `Type` : Metric.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The progress of the WorkGoal object. Applicable only to WorkGoal objects of
`Type` : Metric.

Possible values:

**•** On Track: Progress on the metric is on track.

**•** Behind: Progress on the metric is behind schedule.

**•** Postponed: The metric is postponed.

**•** Critical: Progress on the metric is critical.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the goal image. The image must be stored in Documents and set as
externally available. Applicable only to WorkGoal objects of `Type` : Goal.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The initial value of the WorkGoal metric. Applicable only to WorkGoal objects of
`Type` : Metric and `MetricType` : Progress or Percent.


Standard Objects WorkGoal

**Field Name** **Details**

```
IsKeyCompanyGoal

LastReferencedDate

LastSyncDate

LastViewedDate

MetricType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Used to indicate if the goal is a key company goal. Used for the Company Goal
Showcase. Applicable only to WorkGoal objects of `Type` : Goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this goal.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time stamp that indicates when the actual value was last synced with the
associated metrics report.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this goal.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of metric that is represented. (See values in the following list). Applies
only to WorkGoal objects of `Type` : Metric.

Possible values:

**•** Progress: ActualValue / TargetValue as a percentage

**•** Percent: the metric as a percentage only


Standard Objects WorkGoal

**Field Name** **Details**

**•** YesNo: the completed / not completed metric as a milestone

**•** Absolute: Deprecated

```
MetricTypeDataSource

Name

OverallStatus

OwnerId

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies how the metric (ActualValue and CurrentValue) is updated. Applies only
to WorkGoal objects of `Type` : Goal and Metric.

Possible values:

**•** Manual: indicates that the actual and target value of the metric is updated
manually by the user

**•** Rollup: indicates that the actual and target value of a goal is rolled up
automatically by WDC Goals

**•** DataSyncActualOnly: indicates that the actual value of the metric is linked to
a Salesforce report

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkGoal object. (Maximum length is 255.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The overall calculated status of the WorkGoal based on `FlaggedAs` and
`CompletionDate` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the WorkGoal.

**Type**
reference


Standard Objects WorkGoal

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the structural parent of the WorkGoal. For example, a goal that has a
metric is represented by a WorkGoal of `Type` Metric, which has a parent of
WorkGoal of Type Goal.

Note: The root and the parent must be set to the parent goal for any
child metrics.

```
Progress

RootId

State

TargetValue

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read Only. The overall progress of the WorkGoal.

**Type**
reference to a WorkGoal object

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the structural root of the WorkGoal. For example, a goal that has a metric
is represented by a WorkGoal of `Type` Metric, which has a root of WorkGoal of
`Type` Goal.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the WorkGoal object. Applies only to WorkGoal objects of `Type` :
Metric.

Possible values:

**•** Draft: the draft state for the WorkGoal

**•** Published: published state for the WorkGoal

**•** Archived: archived state for the WorkGoal (for example, goals that no longer
apply)

**Type**
double


Standard Objects WorkGoal

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The target value of the WorkGoal. Applies only to WorkGoal objects of `Type` :
Metric.

```
Type

Weight

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the WorkGoal object, used to differentiate between the components
of a goal. (This field is used to represent components of a goal such as its
description and associated metrics.)

Possible values:

**•** Goal: a goal

**•** Metric: a metric (typically associated with goals)

**•** Objective: an objective

**•** KeyResult: a key result (typically associated with objectives

**•** V2Mom: a V2MOM (pilot feature)

**•** Vision: a vision (pilot feature — typically associated with V2MOM)

**•** Value: a value (pilot feature - typically associated with V2MOM)

**•** Method: a method (pilot feature - typically associated with V2MOM)

**•** Obstacle: an obstacle (pilot feature - typically associated with V2MOM)

**•** Measure: a measure (pilot feature - typically associated with a method)

Note: Administrators can rename goals and metrics to objectives and
key results, respectively. If this preference is enabled, use the `Type`
Objective or KeyResult. Otherwise, use the default `Type` Goal or KeyResult.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The weight of the goal or metric. The sum of the weights should equal 100%.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects WorkGoalCollaborator

**WorkGoalFeed (API verison 35.0)**
Feed tracking is available for the object.

**WorkGoalHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkGoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkGoalShare**

Sharing is available for the object.

### WorkGoalCollaborator

Represents collaborators on a WorkGoal object. This doesn’t include WorkGoal followers, which is handled by Chatter Feed Follow
functionality. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
InvitationDate

State

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date that a user was invited to become a collaborator (nill if the user was not
invited).

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the state of the collaborating user. Whether the user has not responded,
joined, or declined collaboration. The possible values are:


### Standard Objects WorkGoalCollaboratorHistory

**Field Name** **Details**

**•** PendingResponse: a user who was invited to collaborate but hasn’t joined
or declined

**•** Joined: a user who is collaborating on a goal (joined/commit)

**•** Declined: a user who declined to collaborate on a goal

```
UserId

WorkGoalId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The collaborating user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The WorkGoal object that this collaborator is a part of.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

### **WorkGoalCollaboratorHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

### WorkGoalCollaboratorHistory

Represents the history of changes to the values in the fields in a WorkGoalCollaborator object. Access is read-only.

Note: This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals in API
version 35.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects WorkGoalCollaboratorHistory

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

WorkGoalCollaboratorId

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

Name of the standard or custom field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

New value of the modified field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

Previous value of the modified field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the WorkGoalCollaborator object that is associated with this history entry.


### Standard Objects WorkGoalHistory WorkGoalHistory

Represents the history of changes to the values in the fields of a WorkGoal. Access is read-only. This object has been deprecated as of
API version 35.0. Use the GoalHistory object to query historical information for WDC goals.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
Field

NewValue

OldValue

WorkGoalId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The name of the field that was changed.

**Type**
Any Type

**Properties**
Nillable, Sort

**Description**

The new value of the field that was changed.

**Type**
Any Type

**Properties**
Nillable, Sort

**Description**

The latest value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects WorkGoalLink

**Field Name** **Details**

**Description**

ID of the Goal. Label is Goal ID.

### WorkGoalLink

Represents the relationship between two goals (many to many relationship). This object has been deprecated as of API version 35.0.
Use the GoalLink object to query information about the relationship between two WDC goals.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
IsActive

LinkType

Name

SourceGoalId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the WorkGoalLink is active ( `true` ) or not ( `false` )

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of link

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the goal link

**Type**
reference


### Standard Objects WorkGoalShare

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the source WorkGoal object

```
TargetGoalId

### WorkGoalShare

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the target WorkGoal object

Represents a sharing entry on a WorkGoal object. This object has been deprecated as of API version 35.0. Use the GoalShare object to
query information about sharing for WDC goals.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field Name** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The user’s or group’s level of access to the goal. The possible values are:

**•** Read


Standard Objects WorkGoalShare

**Field Name** **Details**

**•** Edit

**•** All: This value is not valid when you create, update, or delete records

This field must be set to an access level that is higher than the organization’s
default access level for goals.

```
ParentId

RowCause

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the WorkGoal object that is associated with this sharing entry.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Valid values include:

**•** `Owner` —The User is the owner of the WorkGoal or is in a user role above
the WorkGoal owner in the role hierarchy.

**•** `Manual` —The User or Group has access, because a user with “All” access
manually shared the WorkGoal with the user or group.

**•** `Rule` —The User or Group has access via a WorkGoal sharing rule.

**•** `GuestRule` —The User or Group has access via a WorkGoal guest user
sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the user or group that was given access to the goal. This field can’t be
updated.


### Standard Objects Workload Workload

Represents the time series for work item volume and average handle time from aggregation and forecasting processes. This object is
available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.

Fields

**Field** **Details**

```
Description

EndDateTime

IsOmni

Name

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the workload

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The end date and time of the time series represented by the Workload object.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the workload is Omni-based.

The default value is 'false'.

**Type**
string


Standard Objects Workload

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The workload name.

```
OwnerId

StartDateTime

TimeZone

WorkloadType

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the workload.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The start date and time of the time series represented by the Workload object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone associated with the workload. Possible values are the time zones supported
by Workforce Engagement.

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the workload.


### Standard Objects WorkloadUnit

**Field** **Details**

Possible values are:

**•** `F` —Forecasted

**•** `H` —Historical

**•** `IH` —Intraday History. This value is available in API version 55.0 and later.

The default value is 'H'.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkloadOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WorkloadShare on page 67**
Sharing is available for the object.

### WorkloadUnit

Represents the number of work items and average handle time in a specific time interval. This object is available in API version 49.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have a Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Analyst permission set.

Fields

**Field** **Details**

```
AverageHandleTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average handle time at a specific period of time.


Standard Objects WorkloadUnit

**Field** **Details**

```
Channel

CustomWorkType

DateTime

IsOmni

MeasureUnit

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The channel value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field of WorkDemographic.CustomWorkType for the custom dimension value.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The timestamp of the single data point in the time series of the workload.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from isOmni field in workload. Indicates that the workload is Omni-based

The default value is 'false'.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time interval (in minutes) used in the workload.

Possible values are:

**•** `43200` —Monthly. Reserved for future use.

**•** `10080` —Weekly

**•** `1440` —Daily

**•** `60` —Hourly


Standard Objects WorkloadUnit

**Field** **Details**

**•** `30` —30 minutes. Reserved for future use.

**•** `15` —15 minutes. Reserved for future use.

The default value is '1440'.

```
Region

SkillSet

TotalCount

WorkDemographicId

WorkloadId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from WorkDemographic.Region for the region value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from WorkDemographic.SkillSet for the skill value.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The total number work items at a specific period of time.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The foreign key to the WorkDemographic object.

This is a relationship field.

**Relationship Name**
WorkDemographic

**Relationship Type**
Lookup

**Refers To**
WorkDemographic

**Type**
reference


### Standard Objects WorkOrder

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The foreign key to the Workload object.

This is a relationship field.

**Relationship Name**
Workload

**Relationship Type**
Lookup

**Refers To**
Workload

```
WorkloadType

### WorkOrder

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The derived field from Workload.WorkloadType to indicate the type of workload, for example,
a history or forecast workload.

Possible values are:

**•** `F` —Forecasted

**•** `H` —Historical

The default value is 'H'.

Represents field service work to be performed for a customer. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Work orders or Field Service must be enabled.

**•** The following fields can’t be edited, regardless of your field-level security settings:

**–** Discount

**–** GrandTotal


Standard Objects WorkOrder

**–** IsGeneratedFromMaintenancePlan

**–** RootWorkOrderId

Fields

**Field Name** **Details**

```
AccountId

Address

AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the work order.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address where the work order is completed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the work order.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


Standard Objects WorkOrder

**Field Name** **Details**

```
AssetWarrantyId

BusinessHoursId

CaseId

City

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset warranty term associated with the work order. This field is available in
API version 50.0 and above.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business hours associated with the work order.

This is a relationship field.

**Relationship Name**
BusinessHours

**Relationship Type**
Lookup

**Refers To**
BusinessHours

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the work order.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The city where the work order is completed. Maximum length is 40 characters.

```
ContactId

Country

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the work order.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the work order is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization. The label in the user interface
is `Currency ISO Code` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work order. Try to include the steps needed to change the
work order’s status to Completed.


Standard Objects WorkOrder

**Field Name** **Details**

```
Discount

Duration

DurationInMinutes

DurationType

EndDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The weighted average of the discounts on all line items in the work
order. It can be any positive number up to 100.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated time required to complete the work order. Specify the duration
unit in the `Duration Type` field. If the `Duration` field on a Work Order
is null, it adopts the duration value from the Work Type object when the work
type is updated or inserted.

Work order duration and work order line item duration are independent of each
other. If you want work order duration to automatically show the sum of the
work order line items’ duration, replace the Duration field on work orders with a
custom roll-up summary field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The estimated duration in minutes. For internal use only.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The date when the work order is completed. This field is blank unless you set up
an Apex trigger or quick action to populate it. For example, you can create a quick
action that sets the `EndDate` to 365 days after the `StartDate` .

```
EntitlementId

GeocodeAccuracy

GrandTotal

IsClosed

IsGeneratedFromMaintenancePlan

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entitlement associated with the work order.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total price of the work order with tax added.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the work order is closed ( `true` ) or open ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
(Read Only) Indicates that the work order was generated from a maintenance
plan ( `true` ), rather than manually created ( `false` ).


Standard Objects WorkOrder

**Field Name** **Details**

```
IsStopped

LastReferencedDate

LastViewedDate

Latitude

LineItemCount

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a milestone is paused ( `true` ) or counting down ( `false` ).
This field is available only if **Enable stopped time and actual elapsed time** is
selected on the Entitlement Settings page.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of work order line items in the work order. Its label in the user
interface is `Line Items` .


Standard Objects WorkOrder

**Field Name** **Details**

```
LocationId

Longitude

MaintenancePlanId

MaintenanceWorkRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the work order. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order. When the work order is
auto-generated from a maintenance plan, this field automatically lists the related
plan.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this work order. This field is
available in API version 50.0 and above.


Standard Objects WorkOrder

**Field Name** **Details**

```
MilestoneStatus

MinimumCrewSize

OwnerId

ParentWorkOrderId

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the status of a milestone. This field is visible if an entitlement process
is applied to a work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the work order.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order’s minimum crew size requirement.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The work order’s assigned owner.

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
The work order’s parent work order, if it has one. Create a custom report to view
a work order’s child work orders.

This is a relationship field.


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Name**
ParentWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

PostWorkSummary

```
PostalCode

```

PreWorkBriefPromptTemplate

```
Pricebook2Id

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of a completed work order that’s either entered manually or created
by an AI agent.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the activated Pre-Work Brief prompt template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price book associated with the work order. Adding a price book to the work
order lets you assign different price book entries to the work order’s line items.
This is only available if Product2 is enabled.

This is a relationship field.

**Relationship Name**
Pricebook2


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
Priority

ProductServiceCampaignId

ProductServiceCampaignItemId

RecommendedCrewSize

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the work order. The picklist includes the following values, which
can be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the work
order. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.


Standard Objects WorkOrder

**Field Name** **Details**

```
ReturnOrderId

ReturnOrderLineItemId

RootWorkOrderId

ServiceAppointmentCount

ServiceContractId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level work order in a work order hierarchy. Depending on
where a work order lies in the hierarchy, its root could be the same as its parent.
View a work order’s child work order in the Child Work Orders related list.

This is a relationship field.

**Relationship Name**
RootWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The service contract associated with the work order.

```
ServiceDocumentTemplate

ServiceReportLanguage

ServiceReportTemplateId

ServiceTerritoryId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for all service reports and service report previews created for
the work order, its service appointments, and its work order line items and their
service appointments. If the field is blank, service reports are generated in the
default language in Salesforce of the person creating the report.

To appear as an option in the ServiceReportLanguage field, a language must be
[set up in Translation Workbench or be one of Salesforce’s 18 fully supported](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
[languages. Rich text fields and service report section names aren’t translated.](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template that the work order uses. If you don’t specify a service
report template on a work order, it uses the service report template listed on its
work type. If the work type doesn’t list a template or no work type is specified,
the work order uses the default service report template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the work order is taking place.

This is a relationship field.


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
SlaExitDate

SlaStartDate

StartDate

State

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the work order exits the entitlement process.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the work order enters the entitlement process. You can update or
reset the time if you have “Edit” permission on work orders.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the work order goes into effect. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the StartDate to the date when the Status changes to In
Progress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the work order is completed. Maximum length is 80 characters.

**Type**
picklist


Standard Objects WorkOrder

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the work order. The picklist includes the following values, which
can be customized:

**•** `New` —Work order was created, but there hasn’t yet been any activity.

**•** `In Progress` —Work has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

Changing a work order’s status does not affect the status of its work order line
items or associated service appointments.

```
StatusCategory

StopStartDate

Street

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field has eight default values: seven values which are identical to the default
`Status` values, and a `None` value for statuses without a status category.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Waiting for Response`_ value,
you may decide that it belongs in the _`On Hold`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the milestone was paused. The label in the user interface is
`Stopped Since` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The street number and name where the work order is completed.

```
Subject

Subtotal

SuggestedMaintenanceDate

Tax

TotalPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the work order. Try to describe the nature and purpose of the job
to be completed. For example, “Annual On-Site Well Maintenance.” Maximum
length is 255 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total of the work order line items’ subtotals before discounts and
taxes are applied.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The suggested date that the work order is completed. When the work order is
auto-generated from a maintenance plan, this field is automatically populated
based on the maintenance plan’s settings.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total tax on the work order. You can enter a number with or without the
currency symbol and use up to two decimal places. For example, in a work order
whose total price is $100, enter $10 to apply a 10% tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
Read only. The total of the work order line items’ prices. This value has discounts
applied but not tax.

```
WorkOrderNumber

WorkTypeId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An eight-digit, auto-generated number that identifies the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the work order. When a work type is selected, the
work order automatically inherits the work type’s `Duration`, `Duration`
`Type`, and required skills. If the `Duration` field for the work type is null, enter
the duration value.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderFeed**

Feed tracking is available for the object.

**WorkOrderHistory**

History is available for tracked fields of the object.

**WorkOrderOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects WorkOrderHistory

**WorkOrderShare**

Sharing is available for the object.

### WorkOrderHistory

Represents the history of changes made to tracked fields on a work order. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Work orders or Field Service must be enabled in your organization, and field tracking for work order fields must be configured.

Fields

**Field Name** **Details**

```
DataType

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


### Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

```
WorkOrderId

### WorkOrderLineItem

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the work order being tracked. The history is displayed on the detail page
for this record.

This is a relationship field.

**Relationship Name**
### WorkOrder

**Relationship Type**
Lookup

**Refers To**
### WorkOrder

Represents a subtask on a work order in field service. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Work orders or Field Service must be enabled.

Fields

**Field Name** **Details**

```
Address

```

**Type**
address


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable

**Description**
The compound form of the address where the line item is completed.

```
AssetId

AssetWarrantyId

City

Country

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the work order line item. The asset is not automatically
inherited from the parent work order.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset warranty term associated with the work order line item. This field is
available in API version 50.0 and above.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the line item is completed. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the line item is completed. Maximum length is 80 characters.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

```
CurrencyIsoCode

Description

Discount

Duration

DurationInMinutes

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization. The label in the user interface
is `Currency ISO Code` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work order line item. Try to describe the steps needed to
mark the line item Completed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percent discount to apply to the line item. You can enter a number with or
without the percent symbol, and you can use up to two decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated time required to complete the line item. Specify the duration unit
in the `Duration Type` field. If the `Duration` field on a Work Order is null,
it adopts the duration value from the Work Type object when the work type is
updated or inserted.

Note: Work order duration and work order line item duration are
independent of each other. If you want work order duration to
automatically show the sum of the work order line items’ duration, replace
the Duration field on work orders with a custom roll-up summary field.

**Type**
double


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The estimated duration in minutes. For internal use only.

```
DurationType

EndDate

GeocodeAccuracy

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the line item is completed. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the EndDate to 365 days after the StartDate.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

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


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**•** `Unknown`

**•** `Zip`

```
IsClosed

IsGeneratedFromMaintenancePlan

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the line item has been closed. Changing the line item’s status
to `Closed` causes this checkbox to be selected in the user interface (sets
`IsClosed` to `true` ).

Tip: Use this field to report on closed versus open work order line items.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Identifies whether the work order line item is generated from a maintenance
plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Used with `Longitude` to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

Note: This field is available in the API only.

```
LineItemNumber

ListPrice

LocationId

Longitude

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number that identifies the work order line item. Each work
order’s line items start at 1.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

The price of the line item (product) as listed in its corresponding price book entry.
If a price book entry isn’t specified, the list price defaults to zero.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A location associated with the work order line item. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Used with `Latitude` to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.

```
MaintenancePlanId

MaintenanceWorkRuleId

MinimumCrewSize

OrderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this line item. This field is available
in API version 50.0 and above.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the line item.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order line item’s minimum crew size
requirement.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order associated with the line item. For example, you may need to order
replacement parts before you can complete the line item.

This is a relationship field.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

```
ParentWorkOrderLineItemId

PostalCode

PricebookEntryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent work order line item, if it has one.

Tip: Create a custom report to view a line item’s child line items.

This is a relationship field.

**Relationship Name**
ParentWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the line item is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price book entry (product) associated with the line item. The label in the user
interface is `Product` . This field’s lookup search only returns products that are
included in the work order’s price book.

This is a relationship field.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

```
Priority

Product2Id

ProductServiceCampaignId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the line item. The picklist includes the following values, which can
be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Read only) The product associated with the price book entry. This field is not
available in the user interface. For best results, use the `PricebookEntryId`
field in any custom code or layouts.

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
Filter, Group, Nillable, Sort

**Description**
The product service campaign associated with the work order line item.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

```
ProductServiceCampaignItemId

Quantity

RecommendedCrewSize

ReturnOrderId

ReturnOrderLineItemId

RootWorkOrderLineItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Number of units of the line item included in the associated work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the line
item. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
(Read only) The top-level line item in a work order line item hierarchy. Depending
on where a line item lies in the hierarchy, its root could be the same as its parent.

Note: View a line item’s child line items in the Child Work Order Line
Items related list.

This is a relationship field.

**Relationship Name**
RootWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

```
ServiceAppointmentCount

ServiceDocumentTemplate

ServiceReportTemplateId

ServiceTerritoryId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order line item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template that the line item uses. If you don’t specify a service
report template on a work order line item, it uses the service report template
listed on its work type. If the work type doesn’t list a template or no work type is
specified, the line item uses the default service report template.

**Type**
reference


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the line item is completed.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
StartDate

State

Status

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the line item goes into effect. This field is blank unless you
set up an Apex trigger or quick action to populate it. For example, you can create
a quick action that sets the StartDate to the date when the Status changes to In
Progress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the line item is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the line item. The picklist includes the following values, which can
be customized:

**•** `New` —Line item was created, but there hasn’t yet been any activity.

**•** `In Progress` —Work has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

```
StatusCategory

Street

Subject

Subtotal

SuggestedMaintenanceDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field has eight default values: seven values which are identical to the default
`Status` values, and a `None` value for statuses without a status category.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Waiting for Response`_ value,
you may decide that it belongs in the _`On Hold`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the line item is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A word or phrase describing the line item.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

(Read only) The line item’s unit price multiplied by the quantity.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Date when maintenance work is planned.

```
TotalPrice

UnitPrice

WorkOrderId

WorkTypeId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The line item’s subtotal with discounts applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Initially, the unit price for a work order line item is the line item’s list price from
the price book, but you can change it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The line item’s parent work order. Because work order line items must be
associated with a work order, this is a required field.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the line item. When a work type is selected, the
line item automatically inherits the work type’s `Duration`, `Duration Type`,
and required skills. If the `Duration` field for the work type is null, enter the
duration value.


### Standard Objects WorkOrderLineItemHistory

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Usage

A work order line item is a child record of a work order. It represents a specific subtask on a work order.

For example, suppose a customer purchased a truck from you. The truck is represented as an asset in your Salesforce org. After some
time, the truck needs both headlight bulbs replaced. Here’s one way that you can use work orders and work order line items to track
the repair.

**1.** Create a work order named “Replace Headlight Bulbs” from the asset record detail page.

**2.** Add three work order line items to the work order: “Replace Left Headlight Bulb,” “Replace Right Headlight Bulb,” and “Test Headlights.”

**3.** Assign the work order to a technician via a queue.

**4.** As the technician completes each line item, he or she marks the item `Completed` .

**5.** When all the line items are complete, the technician marks the work order `Completed` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderLineItemFeed**

Feed tracking is available for the object.

### **WorkOrderLineItemHistory**

History is available for tracked fields of the object.

### WorkOrderLineItemHistory

Represents the history of changes made to tracked fields on a work order line item. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects WorkOrderLineItemHistory

Special Access Rules

Work orders or Field Service must be enabled in your organization, and field tracking for work order line item fields must be configured.

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

WorkOrderLineItemId

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
ID of the work order line item being tracked. The history is displayed on the detail
page for this record.


### Standard Objects WorkOrderLineItemStatus

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
### WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
### WorkOrderLineItem WorkOrderLineItemStatus

Represents a possible status of a work order line item in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ApiName

IsDefault

MasterLabel

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on work orders. Only one status
value can be the default.

**Type**
string


### Standard Objects WorkOrderShare

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value that appears in the UI.

```
SortOrder

StatusCode

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the drop-down list of values in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.

The Status field on work order line items comes with the following values:

**•** New—Line item was created, but there hasn’t yet been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The WorkOrderLineItemStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled By
Customer—creates a work order line item status record, and vice versa.

Note: Work order line items also come with a StatusCategory field whose values are identical to the default Status values. If you
create custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_
value, you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory,
[see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### WorkOrderShare

Represents a sharing entry on a work order. This object is available in API version 36.0 and later.


Standard Objects WorkOrderShare

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Work orders or Field Service must be enabled in your organization. External users can’t access this object.

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
Level of access that the user or group has to the work order. The possible values
are:

**•** _`Read`_

**•** _`Edit`_

**•** _`All`_ (This value isn’t valid for create or update calls.)

Set to an access level that is at least equal to the organization’s default work order
access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The work order associated with the sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


### Standard Objects WorkOrderStatus

**Field Name** **Details**

**Refers To**
### WorkOrder

```
RowCause

UserOrGroupId

### WorkOrderStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited. Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the work order.

**•** `Owner` —The User is the owner of the work order.

**•** `Rule` —The User or Group has access via a work order sharing rule.

**•** `GuestRule` —The User or Group has access via a work order guest user
sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Read Only) ID of the user or group that has access to the work order.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Represents a possible status of a work order in field service.


Standard Objects WorkOrderStatus

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ApiName

IsDefault

MasterLabel

SortOrder

StatusCode

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on work orders. Only one status
value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value that appears in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the drop-down list of values in the UI.

**Type**
picklist


### Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.

Usage

The Status field on work orders comes with the following values:

**•** New—Work order was created, but there hasn’t yet been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The WorkOrderStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled By
Customer—creates a work order status record, and vice versa.

Note: Work orders also come with a StatusCategory field whose values are identical to the default Status values. If you create
custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_ value,
you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory, see
[How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### WorkPerformanceCycle

Represents feedback that is gathered to assess the performance of a specific set of employees.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ActivityFrom

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Description**
The date that you want to start filtering the WDC objects to help requesters create
accurate summaries. The start of the evaluation period.

```
ActivityTo

CurrentTask

LastManagerRequestsSharedDate

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date that you want to stop filtering the WDC objects to help requesters create
accurate summaries. The end of the evaluation period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The current task that the performance summary cycle is engaged in, including
deploying and sharing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when all manager requests are set to be shared.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkPerformanceCycle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Description**
The time stamp that indicates when the current user last viewed this
WorkPerformanceCycle. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

State

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the performance summary cycle that employees will participate in.
This name is created by the administrator and is visible on all respective
notifications and in the UI.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkPerformanceCycle.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state that the performance summary cycle is in. Available pick list values:

**•** Setup: The summary is in draft.

**•** In Progress: The summary is deployed and people are answering the questions
that were created.

**•** Finished: The summary is no longer in progress.

**•** Error: The summary encountered an error.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkPerformanceCycleFeed**

Feed tracking is available for the object.

**WorkPerformanceCycleHistory**

History is available for tracked fields of the object.


### Standard Objects WorkPlan

**WorkPerformanceCycleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPerformanceCycleShare**

Sharing is available for the object.

### WorkPlan

Represents a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

ExecutionOrder

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the work plan is executed. Only positive values or null are supported.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:


Standard Objects WorkPlan

**Field** **Details**

```
LastViewedDate

Name

OwnerId

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the work plan.

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
The ID of the work order, work order line item, or change request that the work plan is
associated with. Available in API version 54.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup


Standard Objects WorkPlan

**Field** **Details**

**Refers To**
ChangeRequest, WorkOrder, WorkOrderLineItem

```
ParentRecordType

WorkOrderId

WorkOrderLineItemId

WorkPlanTemplateId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes whether the parent record is a work order, work order line item, or change request.
Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the work order.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work order line item.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects WorkPlanSelectionRule

**Field** **Details**

**Description**
The ID of the work plan template record. Available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
WorkPlanTemplate

**Relationship Type**
Lookup

**Refers To**
WorkPlanTemplate

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanChangeEvent on page 68**
Change events are available for the object. Available in API version 54.0 and later.

**WorkPlanFeed on page 55**
Feed tracking is available for the object.

**WorkPlanHistory on page 63**
History is available for tracked fields of the object.

**WorkPlanOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WorkPlanShare on page 67**
Sharing is available for the object.

### WorkPlanSelectionRule

Represents a rule that selects a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkPlanSelectionRule

Fields

**Field** **Details**

```
AssetId

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the selection rule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this selection rule is active ( `true` ) or not ( `false` ). Default is `false` .
Label is Active.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.


Standard Objects WorkPlanSelectionRule

**Field** **Details**

```
LocationId

OwnerId

Product2Id

ServiceTerritoryId

WorkPlanSelectionRuleNumber

WorkPlanTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the location.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product. Label is Product.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number of the work plan selection rule, for example, WPSR-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work plan template.


### Standard Objects WorkPlanTemplate

**Field** **Details**

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanSelectionRuleChangeEvent**

Change events are available for the object.

**WorkPlanSelectionRuleFeed**

Feed tracking is available for the object.

**WorkPlanSelectionRuleHistory**

History is available for tracked fields of the object.

**WorkPlanSelectionRuleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanSelectionRuleShare**

Sharing is available for the object.

### WorkPlanTemplate

Represents a template for a work plan. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects WorkPlanTemplate

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan template.

```
IsActive

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
Controls whether the specific template is available for application ( `true` ) or not ( `false` ).
Default is `false` . Label is Active.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects WorkPlanTemplateEntry

**Field** **Details**

**Description**
The ID of the owner who created the work plan template.

```
RelativeExecutionOrder

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The relative execution order for sorting the work plan when it’s applied to the work order or
work order line item. Only positive integers are supported.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateChangeEvent**

Change events are available for the object.

**WorkPlanTemplateFeed**

Feed tracking is available for the object.

**WorkPlanTemplateHistory**

History is available for tracked fields of the object.

**WorkPlanTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanTemplateShare**

Sharing is available for the object.

### WorkPlanTemplateEntry

Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkPlanTemplateEntry

Fields

**Field** **Details**

```
ExecutionOrder

LastReferencedDate

LastViewedDate

WorkPlanTemplateEntryNumber

WorkPlanTemplateId

WorkStepTemplateId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequence number of when this entry is executed. Only positive values are supported.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number of the work plan template entry, for example, WPTE-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the work plan template.

**Type**
reference


### Standard Objects WorkReward

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work step template.

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateEntryChangeEvent**

Change events are available for the object.

**WorkPlanTemplateEntryFeed**

Feed tracking is available for the object.

**WorkPlanTemplateEntryHistory**

History is available for tracked fields of the object.

### WorkReward

Used to store reward codes tied to a Reward Fund. Reward Funds must have at least one WorkReward record.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the Reward permission enabled in order to use the Rewards feature, including WorkRewardFund and WorkReward.

Additional Considerations and Related Objects

### WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record to be available for use. Each

WorkBadge record with a `RewardId` indicates a reward badge given to a Recipient.

Fields

**Field Name** **Details**

```
Code

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects WorkReward

**Field Name** **Details**

**Description**
Represents a singe reward code tied to a RewardFundId.

```
OwnerId

RecipientId

RedemptionDisclaimer

RedemptionInfo

RedemptionUrl

RewardFundId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the User ID of Owner of WorkReward record

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce User ID for User associated with this WorkReward record.

**Type**
textarea

**Properties**
Nillable

**Description**
The disclaimer information about the WorkReward.

**Type**
textarea

**Properties**
Nillable

**Description**
The instructions for redeeming the WorkReward.

**Type**
textarea

**Properties**
Nillable

**Description**
The URL for redeeming the WorkReward.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects WorkRewardFund

**Field Name** **Details**

**Description**
Salesforce unique ID for WorkRewardFund record that is associated with
WorkReward record.

```
RewardFundTypeId

Value

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType associated with the
WorkReward.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of the WorkReward.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardShare**

Sharing is available for the object.

### WorkRewardFund

Represents a Reward Fund and describes the Reward Fund attributes.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkRewardFund

Special Access Rules

To use the Rewards feature, including WorkRewardFund and WorkReward, you must have the Reward permission enabled. To create
Rewards, the user must have Create on WorkRewardFund, which is not a standard permission.

Additional Considerations and Related Objects

WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record available. Each
WorkBadgeDefinition with a RewardFundId is a “Reward Badge.”

Fields

**Field Name** **Details**

```
IsActive

LastReferencedDate

LastViewedDate

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the WorkRewardFund is active ( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFund.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFund. If this value is null, this record might have been only referenced
( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the Reward Fund.


Standard Objects WorkRewardFund

**Field Name** **Details**

```
OwnerId

RewardFundTypeId

TotalCodeCount

Type

UsedCodeCount

Value

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of User who is the Owner of the WorkRewardFund record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType that is associated with the
WorkRewardFund.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are available in the WorkRewardFund. Derived from
WorkReward records that are associated with the WorkRewardFund.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
RewardType of the WorkRewardFund. Default is Amazon.com.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are used in the WorkRewardFund. Derived from the total
assigned WorkReward records that are associated with the WorkRewardFund.

**Type**
currency

**Properties**
Create, Filter, Sort, Update


### Standard Objects WorkRewardFundType

**Field Name** **Details**

**Description**
Value of each of the reward codes in the WorkRewardFund.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundFeed**

Feed tracking is available for the object.

**WorkRewardFundHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundShare**

Sharing is available for the object.

### WorkRewardFundType

Represents the type of WorkRewardFund object.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CreditSystem

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects WorkRewardFundType

**Field Name** **Details**

**Description**
The credit system that is used by the WorkRewardFundType object (gift codes
or points). If points are selected, the reward message will not consider the
`CurrencyCode` field.

```
CurrencyCode

IsActive

IsPredefined

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency code of the WorkRewardFundType

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the WorkRewardFundType is active and available in the UI

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the WorkRewardFundType is predefined ( `true` ) or not ( `false` )

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFundType.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFundType. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.


Standard Objects WorkRewardFundType

**Field Name** **Details**

```
Name

OwnerId

RedemptionDisclaimer

RedemptionInfo

RedemptionUrl

UploadCodeColumn

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkRewardFundType

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the WorkRewardFundType owner

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The redemption disclaimer text for the WorkRewardFundType

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Redemption text for the WorkRewardFundType

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that’s linked to the redemption

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects WorkStep

**Field Name** **Details**

**Description**
The column where the reward code is contained in the CSV file. The upload uses
the second value by default.

```
UploadValueColumn

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The column where the reward value is contained in the CSV file. The upload uses
the third column by default.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundTypeFeed**

Feed tracking is available for the object.

**WorkRewardFundTypeHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeShare**

Sharing is available for the object.

### WorkStep

Represents a work step in a work plan. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkStep

Fields

**Field** **Details**

```
ActionDefinition

ActionType

Description

EndTime

ExecutionOrder

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org. To launch Lightning Web Components from
Work Steps, you must use `QuickAction` on the action definition.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step ends. The value must be greater than or equal to
`StartTime` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkStep

**Field** **Details**

**Description**
The order in which the work step is executed. Only positive integer values or null are
supported.

```
LastReferencedDate

LastViewedDate

Name

PausedFlowInterviewId

ProcessType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The user-defined name of the work step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated ID of the flow interview paused by a user.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow process type launched from the work step.

Possible values are:


Standard Objects WorkStep

**Field** **Details**

**•** `DataCaptureFlow` —Data Capture Flow

**•** `DiscoveryFrameworkFlow` —Discovery Framework Data Capture Flow (Beta)

**•** `FieldServiceMobileFlow` —Field Service Mobile Flow

The default value is `DataCaptureFlow` .

```
StartTime

Status

StatusCategory

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The customizable status of the work order. Every status must be mapped to a status category,
but there can be status categories not mapped to a status.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Not Applicable`

**•** `Paused`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each status value belongs to. Each default status category is mapped to
the corresponding default status. If you create a custom status, you must indicate which
[status category it belongs to. To learn which processes reference StatusCategory, see How](https://help.salesforce.com/articleView?id=service.fs_status_categories.htm&type=5&language=en_US)
[are Status Categories Used?.](https://help.salesforce.com/articleView?id=service.fs_status_categories.htm&type=5&language=en_US)

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`


Standard Objects WorkStep

**Field** **Details**

**•** `Paused`

```
WorkOrderId

WorkOrderLineItemId

WorkPlanExecutionOrder

WorkPlanId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the work order line item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the plan execution order.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work plan.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepChangeEvent**

Change events are available for the object.

**WorkStepFeed**

Feed tracking is available for the object.

**WorkStepHistory**

History is available for tracked fields of the object.


### Standard Objects WorkStepStatus WorkStepStatus

Represents a picklist for a status category on a work step. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

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
Required. The name of the work step status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Controls whether this status is the default value of the picklist of the corresponding status
category ( `true` ) or not ( `false` ). Default is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. The label of the work step status.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects WorkStepTemplate

**Field** **Details**

**Description**
Required. The order in which the work step statuses are displayed in the status category's
picklist.

```
StatusCode

### WorkStepTemplate

```

**Type**
picklist

**Properties**
Required. Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that this status belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`

**•** `Paused`

Represents a template for a work step. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ActionDefinition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects WorkStepTemplate

**Field** **Details**

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org.

```
ActionType

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step template.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this work step template is active `true` or not `false` . Default is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects WorkThanks

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

```
Name

OwnerId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work step template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner who created the work step template.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepTemplateChangeEvent**

Change events are available for the object.

**WorkStepTemplateFeed**

Feed tracking is available for the object.

**WorkStepTemplateHistory**

History is available for tracked fields of the object.

**WorkStepTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkStepTemplateShare**

Sharing is available for the object.

### WorkThanks

Represents the source and message of a thanks post.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkThanks

Additional Considerations and Related Objects

WorkBadge is a lookup to WorkThanks. Each WorkBadge record must derive a SourceId from WorkThanks.

Fields

**Field Name** **Details**

```
FeedItemId

GiverId

Message

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the FeedItem related to the thanks badge.

This is a relationship field.

**Relationship Name**
FeedItem

**Relationship Type**
Lookup

**Refers To**
FeedItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce user ID for the giver of the Thanks record.

This is a relationship field.

**Relationship Name**
Giver

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create

**Description**
Required. Message associated with the Thanks record.


### Standard Objects WorkType

**Field Name** **Details**

```
NetworkId

OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the community that this WorkThanks is associated with. This field is
available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce user ID for the owner of the badge record (typically the same user as
the giver of the record).

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkThanksChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkThanksOwnerSharingRule**

Sharing rules are available for the object.

**WorkThanksShare**

Sharing is available for the object.

### WorkType

Represents a type of work to be performed in Field Service and Lightning Scheduler. Work types are templates that can be applied to
work order or work order line items. This object is available in API version 38.0 and later.


Standard Objects WorkType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Description

DurationType

EstimatedDuration

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work type. Try to add details about the task or tasks that
this work type represents.

**Type**
picklist

**Properties**
Create, Filter, Group, Defaulted on create, Restricted picklist, Sort, Update

**Description**
The unit of the `Estimated Duration` : Minutes or Hours.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The estimated length of the work. The estimated duration is in minutes or hours
based on the value selected in the `Duration Type` field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work type was last modified. Its label in the user interface is
`Last Modified Date` .


Standard Objects WorkType

**Field Name** **Details**

```
LastViewedDate

MinimumCrewSize

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work type was last viewed by the current user.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the work. Work orders
and work order line items inherit their work type’s minimum crew size.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits the minimum crew size requirement.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work type. Try to use a name that helps users quickly understand
the type of work orders that can be created from the work type. For example,
“Annual Refrigerator Maintenance” or “Valve Replacement.”

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The work type’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects WorkType

**Field Name** **Details**

```
RecommendedCrewSize

SaDocumentTemplate

ServiceReportTemplateId

ShouldAutoCreateSvcAppt

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the work.
For example, you might have a Minimum Crew Size of 2 and a Recommended
Crew Size of 3. Work orders and work order line items inherit their work type’s
recommended crew size.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a service appointment.
The ID is 15 to 18 characters long.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template associated with the work type. When users create
service reports from a work order or work order line item that uses this work type,
the reports use this template.

**Type**
boolean

**Properties**
Create, Filter, Group, Defaulted on create, Sort, Update

**Description**
Select this option to have a service appointment automatically created on work
orders and work order line items that use the work type.

Note:

**•** By default, the Due Date on auto-created service appointments is
seven days after the created date. Admins can adjust this offset from
the Field Service Settings page in Setup.

**•** If a work type with the Auto-Create Service Appointment option
selected is added to an existing work order or work order line item, a


Standard Objects WorkType

**Field Name** **Details**

service appointment is only created for the work order or work order
line item if it doesn’t yet have one.

**•** If someone updates an existing work type by selecting the Auto-Create
Service Appointment option, service appointments aren’t created on
work orders and work order line items that were already using the
work type.

```
WoDocumentTemplate

WoliDocumentTemplate

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a work order. The ID is
15 to 18 characters long.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a work order line item.
The ID is 15 to 18 characters long.

Adding a work type to a work order or work order line item causes the record to inherit the work type’s duration values and required
skills and products.

Note:

**•** If needed, you can update the duration values and required skills and products on a work order or work order line item after
they’re inherited from the work type.

**•** If a work order or work order line item already has required skills or products, associating it with a work type doesn’t cause it
to inherit the work type’s requirements.

**•** If a work order or work order line item already has a duration value in its `Duration` field, associating it with a work type
doesn’t cause it to inherit the work type’s duration value.

**•** Customizations to required skills or products, such as validation rules or Apex triggers, are not carried over from work types to
work orders and work order line items.


### Standard Objects WorkTypeGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkTypeChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkTypeFeed**

Feed tracking is available for the object.

**WorkTypeHistory**

History is available for tracked fields of the object.

**WorkTypeOwnerSharingRule**

Sharing rules are available for the object.

**WorkTypeShare**

Sharing is available for the object.

### WorkTypeGroup

Represents a grouping of work types used to categorize types of appointments available in Lightning Scheduler, or to define scheduling
limits in Field Service. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdditionalInformation

Description

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Additional information about the types of appointments this work type group represents.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this work type group.


Standard Objects WorkTypeGroup

**Field** **Details**

```
GroupType

IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The category of this work type group. Possible values are:

**•** `Capacity` —A group of work types used to define a work capacity limit in Field Service.

**•** `Default` —A non-capacity group of work types used in Lightning Scheduler.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this work type group can be used for appointment scheduling or work
capacity limits. A work type can belong to only one active work type group of type Capacity.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this work type group.

**Type**
reference


### Standard Objects WorkTypeGroupMember

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupFeed**

Feed tracking is available for the object.

**WorkTypeGroupHistory**

History is available for tracked fields of the object.

**WorkTypeGroupOwnerSharingRule**

Sharing rules are available for the object.

**WorkTypeGroupShare**

Sharing is available for the object.

### WorkTypeGroupMember

Represents the relationship between a work type and the work type group it belongs to. This object is available in API version 45.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

```

**Type**
dateTime


Standard Objects WorkTypeGroupMember

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

```
LastViewedDate

Name

WorkTypeGroupId

WorkTypeId

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
Autogenerated number identifying the work type group membership. It uses the format
########.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type group that this record belongs to.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that this record corresponds to.

This is a relationship field.


Standard Objects WorkTypeGroupMember

**Field** **Details**

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupMemberFeed**

Feed tracking is available for the object.

**WorkTypeGroupMemberHistory**

History is available for tracked fields of the object.


## CHAPTER 7 Data Model

Entity relationship diagrams (ERDs) for standard Salesforce objects illustrate important relationships between objects. Salesforce ERDs
use crow’s foot notation.

[[other]: ERDs are hosted in the Data Model Gallery. The Salesforce Data Model Gallery is a curated collection of diagrams that](https://developer.salesforce.com/docs/platform/data-models/guide)
illustrate the underlying data models for Salesforce products, features, and clouds. It’s a resource designed to support customers,
developers, solution engineers, and data architects in understanding how data is structured across Salesforce — enabling better
solution design, integration planning, and implementation strategy.

The data model for your custom objects depends on what you create.


INDEX

A

AccountInsight object 289
AccountUserTerritory2View object 343
AnalyticsLicensedAsset object 546

B

Big Objects
Composite primary key 32
Custom Big Object 32
Defining 32
Deploying 32
# Index 32

Overview 31

C

ContactSuggestionInsight object 1457

D

Data access
standard objects 27
Delegated Account Objects 1852

E

Electronic_Media_Group_object 1915
Electronic_Media_Use_object 1917
External Account Hierarchy History Object 2497
External_Account_Hierarchy_object 2494
ExternalSocialAccount object 2514

F

FormulaFunction object 2810
FormulaFunctionCategory object 2813
Freeze users 5631

H

HealthCareDiagnosis object 2902
HealthCareProcedure object 2907

# I

IframeWhiteListUrl object 2933

L

LandingPage object 3061

M

Managed_Content 3375
Managed_Content_Channel 3377
Managed_Content_Channelobject 3377
Managed_Content_Info_object 3380
Managed_Content_object 3375
Managed_Content_Variant 3382
Managed_Content_Variant_object 3382
MarketingForm object 3385
MarketingLink object 3389

O

Object_name object 4803
ObjectPermissions object 3592
Objects
AccountInsight 289
AccountUserTerritory2View 343
AnalyticsLicensedAsset 546
ContactSuggestionInsight 1457
Electronic_Media_Group 1915
Electronic_Media_Use 1917
External_Account_Hierarchy 2494
ExternalSocialAccount 2514
FormulaFunction 2810
FormulaFunctionCategory 2813
HealthCareDiagnosis 2902
HealthCareProcedure 2907
IframeWhiteListUrl 2933
LandingPage 3061
LightningExperienceTheme 3158
Managed_Content_Info 3380
MarketingForm 3385
MarketingLink 3389
Object_name 4803
ObjectPermissions 3592
OmniSupervisorConfig 3605
OmniSupervisorConfigAction 3607
OmniSupervisorConfigGroup 3608
OmniSupervisorConfigProfile 3609
OmniSupervisorConfigUser 3614
OpportunityContactRoleSuggestionInsight 3651
OpportunityInsight 3658
PermissionSet 4139
PermissionSetGroup 4126, 4129
Product_Attribute 4326


**Index**

Objects _(continued)_
Product_Attribute_Set 4327
Product_Attribute_Set_Item 4329
Product_Attribute_Set_Product 4330
Product_Category 4334, 4337
Product_Media 4359
Prompt 4472, 4485
PromptAction 4463, 4467
PromptActionOwnerSharingRule 4469
PromptActionShare 4470, 4474
Recommendation 4616
Sales_Store_Catalog 4782
SocialPersona 5088
SocialPost 5094
SurveyQuestionScore 5160
UiFormulaCriterion 5456
UiFormulaRule 5457
VoiceCallQualityFeedback 5791
WebStore 5856, 5880
WebStoreCatalog 5868
OmniSupervisorConfig object 3605
OmniSupervisorConfigAction object 3607
OmniSupervisorConfigGroup object 3608
OmniSupervisorConfigProfile object 3609
OmniSupervisorConfigUser object 3614
OpportunityContactRoleSuggestionInsight object 3651
OpportunityInsight object 3658

P

PermissionSetGroup object 4126

PermissionSetGroupComponent object 4129
PermissionSetTabSetting object 4139
Product_Attribute_object 4326
Product_Attribute_Set_Item_object 4329
Product_Attribute_Set_object 4327
Product_Attribute_Set_Product_object 4330
Product_Category_object 4334, 4337
Product_Media_object 4359

R

Recommendation object 4616

S

Sales_Store_Catalog_object 4782
SocialPersona object 5088
SocialPost object 5094
Standard objects
data access 27
SurveyQuestionScore object 5160

U

UiFormulaCriterion object 5456
UiFormulaRule object 5457

V

VoiceCallQualityFeedback object 5791

W

WebStore object 5856, 5880
WebStoreCatalog_object 5868

