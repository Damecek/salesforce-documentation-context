The administrator-created custom email content sent when a policy is triggered. Used in
Real-Time Event Monitoring only. Maximum of 1333 characters. This field is null when the
Custom Email Content setting is selected in the UI but no message content is entered. This
field is available in API version 54.0 and later.

Custom messages aren’t translatable.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description entered for this policy.


Standard Objects TransactionSecurityPolicy

**Field** **Details**

```
DeveloperName

EventName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API, or program name, for this policy.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Real-Time Event Monitoring only. Indicates the name of the event the policy monitors.
Valid values are:

**•** `ApiEvent` —Tracks these user-initiated read-only API calls: `query()`,
`queryMore()`, and `count()` . Captures API requests through SOAP API and Bulk
API for the Enterprise and Partner WSDLs. Tooling API calls and API calls originating from
a Salesforce mobile app aren’t captured.

**•** `ApiAnomalyEventStore` —Tracks anomalies in how users make API calls.
ApiAnomalyEventStore is an object that stores the event data of `ApiAnomalyEvent` .
This object is available in API version 50.0 and later.

**•** `BulkApiResultEventStore` —Tracks when a user downloads the results of a
Bulk API request. `BulkApiResultEventStore` is a big object that stores the
event data of `BulkApiResultEvent` . This object is available in API version 50.0
and later.

**•** `CredentialStuffingEventStore` —Tracks when a user successfully logs into
Salesforce during an identified credential stuffing attack. Credential stuffing refers to
large-scale automated login requests using stolen user credentials.This value is available
in API 49.0 and later.

**•** `FileEventStore` —Tracks when a user downloads, previews, or uploads a file.
FileEventStore is a big object that stores the event data of FileEvent. This object is available
in API version 57.0 and later.

**•** `GuestUserAnomalyEventStore` —Tracks data access anomalies that are caused
by guest user permission misconfiguration. GuestUserAnomalyEventStore is an object
that stores the event data of GuestUserAnomalyEvent. This object is available in API
version 60.0 and later.

**•** `ListViewEvent` —Tracks when users access data with list views using Lightning
Experience, Salesforce Classic, or the API. It doesn’t track list views of Setup entities.

**•** `LoginAnomalyEventStore` —Stores the records of data access anomalies that
are caused by potentially malicious login actions.This object is available in API version
64.0 and later.


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**•** `LoginAsEvent` —Tracks the login activity of admins who log in to Salesforce as other
users.This object is available in API version 46.0 and later.

**•** `LoginEvent` —LoginEvent tracks the login activity of users who log in to Salesforce.

**•** `PermissionSetEventStore` —Tracks changes to permission sets and permission
set groups.

**•** `ReportAnomalyEventStore` —Tracks anomalies in how users run or export
reports, including unsaved reports. This value is available in API 49.0 and later.

**•** `ReportEvent` —Tracks when reports are run in your org.

**•** `SessionHijackingEventStore` —Tracks when unauthorized users gain
ownership of a Salesforce user’s session with a stolen session identifier. To detect such
an event, Salesforce evaluates how significantly a user’s current browser fingerprint
diverges from the previously known fingerprint using a probabilistically inferred
significance of change. This value is available in API 49.0 and later.

```
EventType

ExecutionUserId

MasterLabel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Legacy Transaction Security only. Indicates the type of event the policy monitors.
Valid values are:

**•** `AccessResource` —Notifies you when the selected resource has been accessed.

**•** `AuditTrail` —Reserved for future use.

**•** `DataExport` —Notifies you when any API query is made, such as from the Data Loader
API client, or when a Report export occurs.

**•** `Entity` —Notifies you on use of an object type such as an authentication provider or
chatter post.

**•** `Login` —Notifies you when a user logs in.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. The ID of an active user who is assigned the Modify
All Data and View Setup user permissions. As of Summer '20, Legacy Transaction Security is
a retired feature in all Salesforce orgs.

**Type**
string


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The policy’s name.

Important: Where possible, we changed noninclusive terms to align with our
company value of Equality. We maintained certain terms to avoid any effect on
customer implementations.

```
NamespacePrefix

ResourceName

State

```

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

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. A resource used to narrow down the conditions
under which the policy triggers. For example, with a `DataExport` event, you can select
a resource Lead to specifically monitor export activity occurring on your Lead entities. The
resources available depend on the `EventType` field.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Description**
Indicates whether the policy is active. Valid values are:

**•** `Disabled`

**•** `Enabled`

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of validation that the policy uses. The valid values are:

**•** `CustomApexPolicy`  - Created with Apex editor.

**•** `CustomConditionBuilderPolicy`  - Created with Condition Builder

.

### TransactionSecurityEventLog

Transaction Security event logs contain details about policy execution. Legacy transaction security policy details are supported in API
version 38.0 and later. Enhanced transaction security policy details are supported in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApexIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.


Standard Objects TransactionSecurityEventLog

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ClientIp

CpuTime

EvaluationTime

EventName

FlowIdentifier

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the event, which is `Transaction Security Event` .

**Type**
String


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

```
LoginKey

PlannerIdentifier

PolicyIdentifier

PolicyOutcome

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated. For example: `00530000009M943` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

Possible values are:

**•** `Error` —The policy caused an undefined error when it executed.

**•** `ExemptNoAction` —The user is exempt from transaction security policies, so the
policy didn’t trigger.

**•** `MeteringBlock` —The policy took longer than 3 seconds to process, so the user was
blocked from performing the operation.

**•** `MeteringNoAction` —The policy took longer than 3 seconds to process, but the
user isn't blocked from performing the operation.

**•** `NoAction` —The policy didn't trigger.


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**•** `Notified` —A notification was sent to the recipient.

```
PolicyType

RequestIdentifier

Result

RunTime

SendEmailNotification

SendInAppNotification

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique id for a given request. For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The outcome of evaluating the policy. For example: `NOT TRIGGERED` .

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
Boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to send an email notification. The default value is `false` .

**Type**
Boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Description**
Indicates whether to send an in-app notification. The default value is `false` .

```
SessionKey

Timestamp

TriggeredTimestamp

Uri

UserIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
DateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time at which the Transaction Security event was generated in ISO8601-compatible
format. For example: 2015-07-27T11:32:59.555Z.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who is using Salesforce services through the UI or the API.
For example: `00530000009M943` .


### Standard Objects Translation Translation

The Translation object represents the languages enabled for translation in your Salesforce org. This object is available in API version 47.0
and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** To view this object, you must have the “View Setup and Configuration” permission.

**•** To use the `create()`, `update()`, and `upsert()` calls, Translation Workbench must be enabled in your org.

**•** To manage translations, Translation Workbench must be enabled in your org. Specify translators for each language through the
### Translation Language Settings Setup page.

Fields

**Field** **Details**

```
CanManage

IsActive

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the language is available for translation ( `true` ) or not ( `false` ).

Specify translators for each language through the Translation Language Setup page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the translated values for this language display to users ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code. See the Salesforce Help for a full list of languages and their codes.


### Standard Objects TravelMode TravelMode

Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such as
Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is available
in API version 54.0 and later.

Fields

**Field** **Details**

```
CanUseTollRoads

IsLocked

IsTransportingHazmat

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is allowed to drive on toll roads.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is transporting hazardous materials.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects TravelMode

**Field** **Details**

```
LastViewedDate

MayEdit

Name

OwnerId

TransportType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` =)
but not viewed it.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the travel mode.

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
picklist


### Standard Objects TwoFactorInfo

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of transportation.

Possible values are:

**•** `Bicycle`

**•** `Car` -Default.

**•** `Heavy Truck`

**•** `Light Truck`

**•** `Walking`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TravelModeFeed**

Feed tracking is available for the object.

**TravelModeOwnerSharingRule**

Sharing rules are available for the object.

**TravelModeShare**

Sharing is available for the object.

### TwoFactorInfo

Stores a user’s secret for multi-factor operations. Use this object when customizing multi-factor authentication in your organization.
(Note that multi-factor authentication was formerly called two-factor authentication.) This object is available in API version 32.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You need the Manage Multi-Factor Authentication in API permission to create or update this object.


### Standard Objects TwoFactorMethodsInfo

Fields

**Field Name** **Details**

```
SharedKey

Type

UserId

### TwoFactorMethodsInfo

```

**Type**
string

**Properties**
Create, Group, Sort, Update

**Description**

This field is never read-enabled, though it is write-enabled. A request for this
value always returns `null` . The value must be a base32-encoded string of a
20-byte secret.

You can use the Apex method
`Auth.SessionManagement.getQrCode()` to get a value to write to
this field.

Note: If you write a secret to this field, in API version 37.0 and later the
user gets an email notification that a new identity verification method
was added to the user’s account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The multi-factor method.

**•** `TOTP` —The time-based one-time password.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the user who’s associated with the authentication secret.

Stores information about which identity verification methods a user has registered. This object is available in API version 37.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects TwoFactorMethodsInfo

Special Access Rules

You need the Manage MFA in API user permission to access this object. Note that multi-factor authentication (MFA) was formerly called
two-factor authentication.

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
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
ExternalId

HasBuiltInAuthenticator

HasSalesforceAuthenticator

HasSecurityKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique system-generated numerical identifier for the user.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a built-in authenticator on their device, such as
Touch ID or Windows Hello. The user can verify their identity by using the built-in
authenticator.

This field is available in API version 53.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has connected the Salesforce Authenticator mobile app. The
user can verify identity by approving a notification sent to the app. If the user
sets a trusted location in the app, Salesforce Authenticator verifies automatically
when the user is in the trusted location.

**Type**
boolean


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a WebAuthn-compatible security key. This field
includes all security keys registered or used after Summer ’22. The user can verify
their identity by inserting the security key into a USB port to generate credentials.

```
HasTempCode

HasTotp

HasU2F

HasUserVerifiedEmailAddress

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has a temporary verification code generated by a Salesforce
admin or user with Manage Multi-Factor Authentication in User Interface
permission.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has connected an authenticator app that generates verification
codes, also known as time-based one-time passwords (TOTP). The user can verify
identity by entering a code generated by the app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a U2F security key. The user can verify identity
by inserting the security key into a USB port to generate credentials.

Note: For U2F security keys registered or used after Summer ’22, use
HasSecurityKey instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user's email address is verified.

This parameter is available in API version 43.0 and later.


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

```
HasUserVerifiedMobileNumber

HasVerifiedMobileNumber

UserId

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has self-registered and verified a mobile phone number.
Salesforce can text a verification code to the user at that number.

This parameter is available in API version 43.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has a mobile phone number that was added by an administrator
or self-registered by the user. Salesforce can text a verification code to the user
at that number.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who’s associated with the identity verification methods.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `[query()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_query.htm)` call returns up to 500 rows.
A `[queryMore()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_querymore.htm)` call returns 500 more, up to 2,500 total. No more records are returned after 2,500.

To make sure that you don’t miss any records, issue a `COUNT()` query in a SELECT clause for TwoFactorMethodInfo. This query gives
you the total number of records. If there are more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
  SELECT <desired fields> FROM TwoFactorMethodsInfo LIMIT 2000 OFFSET 0

```


### Standard Objects TwoFactorTempCode

Then, run another query with an offset of 2,000.

```
     SELECT <desired fields> FROM TwoFactorMethodsInfo LIMIT 2000 OFFSET 2000

```

Continue to increase the offset by 2,000 until you have results for all records.

### TwoFactorTempCode

Stores information about a user’s temporary verification code for confirming their identity when logging in. This object is available in
API version 37.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You need the Manage Multi-Factor Authentication in API permission to access this object. (Note that multi-factor authentication was
formerly called two-factor authentication.)

Fields

**Field Name** **Details**

```
Expiration

Identifier

TempCode

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when the temporary verification code expires. The code expires
in 1 to 24 hours after it’s generated. Salesforce admins and non-admin users with
the Manage Multi-Factor Authentication in User Interface permission set the
expiration time when generating the code.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique identifier for the temporary code. This is a required field that can take
any value.

**Type**
encryptedstring


### Standard Objects UiAgentInteractionEventLog

**Field Name** **Details**

**Description**
A request for this value always returns `null` .

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the user who’s associated with the temporary verification code.

### UiAgentInteractionEventLog

This log tracks client side interactions and events with the Agentforce panel. It is limited to Salesforce Lightning Experience, Salesforce
Mobile, and Conversation Preview within Agentforce Builder. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AgentType

AppName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app this logline has executed.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

BrowserName

BrowserVersion

ButtonLabel

Channel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returned with every session (from bots runtime API). The session begins with co-pilot panel
is opened and ends when the user logs out of Salesforce, closes the browser tab or exits the
browser. For mobile, this id is present throughout the entire time the app is open, and only
changes upon cold start or logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Browser major.minor version. Some browseers may not provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the user interacts with a message by clicking a message-level button, this is the label
of the button the user selects.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the channel. For example, mobile, LEX, or Playground.

```
ClientGeolocation

ClientIdentifier

ClientIp

Components

ConnectionType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Client geographic location in format Country/State.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API client ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Client IP address.

**Type**
textarea

**Properties**
Nillable

**Description**
An array of strings that contain the names of the components, including the namespace and
the name of the component. This should include both input and output components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection. For example, WiFi.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
DeviceModel

DevicePlatform

DeviceSessionIdentifier

FeedbackIdentifier

HasToxicityWarning

IsAgentPanelExited

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The device model.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The application experience

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Auto-generated ID on the client-side that stays the same for the duration of the browser tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The turn ID from Agents V1 API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Flag to identify whether the message contains a toxicity warning.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Description**
A boolean field that is true if the user clicks on a button to navigate away from an agent
panel.

The default value is `false` .

```
LightningType

LightningTypeMessage

LoginKey

MessageIdentifier

MobileSdkAppType

MobileSdkVersion

```

**Type**
textarea

**Properties**
Nillable

**Description**
An array of strings that contains the name of the ES type(s).

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
This is the ES type message associated with the co-pilot response (i.e. “Inform” or “Inquire”)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the login id to allow tracking of all events from user login to logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returned with every message (from bots runtime API).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK version.

```
ObjectType

OperatingSystemName

OperatingSystemVersion

PageContext

PageObjectIdentifier

PageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object for ES Type recordInfo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the operating system.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the component hosting the main content of the page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object id, if any, of the record being displayed.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object type of the page being displayed.

```
PageUrl

RequestIdentifier

SdkAppVersion

SessionKey

TaskName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Raw url of the page log occurred on.

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
The SDK app version this logline has executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the session id to allow tracking of all events in a session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This will describe the nature of the event being logged.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
Timestamp

UiEventElapsedTime

UiEventTimestamp

UiRootActivityIdentifier

UserIdentifier

UserType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The elapsed time for the UI event.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time when the message was logged according to the client.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the root activity, if any, when this message was logged.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID of the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of user.


### Standard Objects UiFormulaCriterion

**Field** **Details**

```
VoiceOrText

### UiFormulaCriterion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Whether the input by the user was “voice” or “text”.

Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
LeftHandSide

OperatorId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the field that the filter is based on. For example, `AMOUNT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter operator. Valid values are:

**•** `CONTAINS`

**•** `EQUAL`

**•** `GE` —greater than or equal

**•** `GT` —greater than

**•** `LE` —less than or equal

**•** `LT` —less than

**•** `NE` —not equal


### Standard Objects UiFormulaRule

**Field** **Details**

This is a relationship field.

**Relationship Name**
Operator

**Relationship Type**
Lookup

**Refers To**
null

```
ParentKeyPrefix

RightHandSide

RuleId

### UiFormulaRule

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix of the parent ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the value used to evaluate the component’s visibility. For example, 1000000.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the formula rule ID.

This is a relationship field.

**Relationship Name**
Rule

**Relationship Type**
Lookup

**Refers To**
### UiFormulaRule

Represents a set of one or more filters that define the conditions under which a component displays on a Lightning page. This object is
available in API version 47.0 and later.


Standard Objects UiFormulaRule

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AssociatedElementId

BooleanFilter

DeveloperName

Formula

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a parent component that UiFormulaRule is associated with, such as PromptVersion.

This is a relationship field.

**Relationship Name**
AssociatedElement

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter logic applied to UiFormulaRule. References the UI formula rule stored
by UiFormulaCriterion based on the sortIndex, such as ((1 && 3) || 2).

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the API name of the UiFormulaRule.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
textarea

**Properties**
Nillable


### Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
Represents the formula source string of UiFormulaRule.

```
Language

MasterLabel

ParentKeyPrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the language of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. Represents the label of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix for AssociatedElementId.

### UiTelemetryNavTmEventLog

UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from the
[UI Telemetry Resource Timing Event on page 2413 and includes requests initiated with either the Fetch API or the XMLHttpRequest API.](https://fetch.spec.whatwg.org/)
This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects UiTelemetryNavTmEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as `Salesforce.com IP` .

```
ConnectEnd

ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
string


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

```
DevicePlatform

DeviceSessionIdentifier

DomComplete

DomContentLoadedEventEnd

DomContentLoadedEventStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the page’s `readyState` property is set to `complete` .
Indicates that the page and its subresources have finished loading.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler completes.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

**Type**
double


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler starts.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

```
DomInteractive

DomainLookupEnd

DomainLookupStart

Duration

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the page’s `readyState` is set to `interactive` . Indicates
that the page has finished loading, but subresources, such as images and scripts, are still
loading.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`LOAD_EVENT_END` time.

```
EncodedBodySize

FetchStart

FirstInterimResponseStart

InitiatorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTML element that initiates the resource load.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
LoadEventEnd

LoadEventStart

LoginKey

MobileSdkAppType

MobileSdkVersion

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `load` event handler completes.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `load` event handler begins.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile SDK version number.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
NavigationType

NextHopProtocol

OperatingSystemName

OperatingSystemVersion

PageContext

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of navigation timing data.

**Possible Values**

**•** `navigate` : a user interaction or a script initiated navigation.

**•** `reload` : a reload initiated navigation.

**•** back_forward: navigation traverses the browser’s history.

**•** `prerender` : a prerender hint initiated navigation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Application-Layer Protocol Negotiation (ALPN) Protocol ID that fetches the resource.

**Possible Values**
`http/0.9`, `http/1.0`, `h2`, `h2c`, `h3`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `USER_AGENT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
PageObjectIdentifier

PageObjectType

PageUrl

RedirectCount

RedirectEnd

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the top-level Lightning Experience page that the user opened. The page
can contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of redirects since the last non-redirect navigation in the current browsing
context.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
RedirectStart

RenderBlockingStatus

RequestIdentifier

RequestStart

ResponseEnd

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

```
ResponseStart

ResponseStatus

SdkAppVersion

SecureConnectionStart

ServerRequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The HTTP response status code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The request ID for the server request that’s used to find associated server logs.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
SessionKey

StartTime

Timestamp

TransferSize

UiEventElapsedTime

UiEventTimestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the resource, including the response header and the response payload
body.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The time at which this event occurs, measured in milliseconds.

```
UiRootActivityIdentifier

UiThreadResponseDelay

UnloadEventEnd

UnloadEventStart

Url

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the root activity when the event occurs.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `unload` event handler completes.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `unload` event handler starts.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The URL of the request.

```
UserIdentifier

UserType

WorkerStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
If a service worker is installed, the time in milliseconds when the active service worker receives
the `fetch` event.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

### UiTelemetryRsrcTmEventLog

UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 64.0 and later.](https://fetch.spec.whatwg.org/)

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects UiTelemetryRsrcTmEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP.”

```
ConnectEnd

ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

```
DevicePlatform

DeviceSessionIdentifier

DomainLookupEnd

DomainLookupStart

Duration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`RESPONSE_END` time.

```
EncodedBodySize

FetchStart

FirstInterimResponseStart

InitiatorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The HTML element that initiates the resource load.

```
LoginKey

MobileSdkAppType

MobileSdkVersion

NextHopProtocol

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile SDK version number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ALPN Protocol ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the operating system.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version number.

```
PageContext

PageObjectIdentifier

PageObjectType

PageUrl

RedirectEnd

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience page that the user opened. The page can
contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

```
RedirectStart

RenderBlockingStatus

RequestIdentifier

RequestStart

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
ResponseEnd

ResponseStart

ResponseStatus

SdkAppVersion

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The HTTP response status code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
SecureConnectionStart

ServerRequestIdentifier

SessionKey

StartTime

Timestamp

TransferSize

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The requestId for the server request that’s used to find associated server logs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The size in octets of the resource, including the response header and the response payload
body.

```
UiEventElapsedTime

UiEventTimestamp

UiRootActivityIdentifier

UiThreadResponseDelay

Url

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the message was logged and when the browser
tab started meaning

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the root activity when the event occurs.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the request.


### Standard Objects UndecidedEventRelation

**Field** **Details**

```
UserIdentifier

UserType

WorkerStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the active service worker receives the `fetch` event, if a
service worker is installed.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

### UndecidedEventRelation

Represents event participants (invitees or attendees) with the status `Not Responded` for a given event. This object is available in
API versions 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

```

**Type**
reference


Standard Objects UndecidedEventRelation

**Field Name** **Details**

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

```
RelationId

RespondedDate

Response

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
This field is always `null` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment` .


### Standard Objects UnifiedActivity

**Field Name** **Details**

```
Type

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.

**Query invitees who have not responded to an invitation to an event**

```
  SELECT eventId, type, response FROM UndecidedEventRelation WHERE

  eventid='00UTD000000ZH5LA'

```

SEE ALSO:

AcceptedEventRelation

DeclinedEventRelation

### UnifiedActivity

Represents an activity that is automatically captured from Einstein Activity Capture (EAC) or other activity data, such as calls, manually
logged tasks, and emails. This object consists of fields common to all types of activity-related objects such as Event, Task, EmailMessage,
VoiceCall, VideoCall, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime


Standard Objects UnifiedActivity

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible values are:

**•** `UnifiedActivity`

**•** `UnifiedEmail`

**•** `UnifiedMeeting`

**•** `UnifiedTask`

**•** `UnifiedVideoCall`

**•** `UnifiedVoiceCall`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a polymorphic relationship field.


### Standard Objects UnifiedActivityInsight

**Field** **Details**

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage, Event, Task, VideoCall, VoiceCall

```
InternalEventKey

IsInsightAvailable

Snippet

Subject

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the task or event.

### UnifiedActivityInsight

Represents an insight related to a unified activity. This object is available for reports and dashboards in the Winter ’24 release and later.


Standard Objects UnifiedActivityInsight

Supported Calls

`describeSObjects()`, `query()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

AggregatedKeywordOccurrences

InsightType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the unified activity that this insight is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of keyword occurrences that triggered this insight. This field is the sum of
occurrences for all the attached UnifiedActivityInsightKeyword objects.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Type of the insight.


### Standard Objects UnifiedActivityParticipant

**Field** **Details**

```
OwnerId

Scope

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. ID of the owner of the insight. Only user-scoped insights have owners
( `Scope` = `USER` ).

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The scope of the insight.

Possible values are:

**•** `ORG`

**•** `USER`

### UnifiedActivityParticipant

Represents a participant in an activity. For example, a participant in a voice call is someone who initiated the call or someone who
received the call.This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.


Standard Objects UnifiedActivityParticipant

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity that the person participated in.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The channel-specific address used to identify the participant in an external communication.
For example, an email address in an email or a phone number in a voice call. The value is
captured at the time of the communication; it doesn’t change if the contact’s email address
or phone number is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The role of the participant in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`


### Standard Objects UnifiedActivityRelation

**Field** **Details**

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

```
PersonId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person who participated in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

### UnifiedActivityRelation

Represents a relationship between an activity and a related record that’s a target or topic of the activity. For example, a related record
can be an opportunity, account, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)


### Standard Objects UnifiedActvtyInsightKeyword

Fields

**Field** **Details**

```
ActivityId

RelatedId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity. This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedVideoCall, UnifiedVoiceCall

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the related record. This field is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Contract, Lead, Opportunity, User

### UnifiedActvtyInsightKeyword

Represents a keyword in a communication that triggered the activity insight. This object is available for reports and dashboards in the
Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.


### Standard Objects UnifiedEmail

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
InsightId

Keyword

Occurrences

### UnifiedEmail

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity insight associated with the keyword.

This field is a relationship field.

**Relationship Name**
Insight

**Relationship Type**
Lookup

**Refers To**
UnifiedActivityInsight

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Keyword mentioned in the communication.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Number of times the keyword was mentioned in the communication.

Represents an email that was captured or synced from an EmailMessage or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.


Standard Objects UnifiedEmail

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

ActivitySubType

ActivityType

DetailId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the email in the Coordinated Universal Time (UTC) time zone.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedEmail` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UnifiedEmail

**Field** **Details**

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object. If the email was captured from Einstein Activity Capture,
this field returns a blank value.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
Direction

InternalEventKey

IsInsightAvailable

IsPrivate

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The direction in which the email was sent or received.

Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean


### Standard Objects UnifiedEmailParticipant

**Field** **Details**

**Properties**
Defaulted on create Filter

**Description**
Indicates whether the activity's sensitive fields ( `Subject` and `Snippet` ) are masked
( `true` ) or visible ( `false` ) for non-owners.

The default value is `false` .

```
Snippet

Subject

```

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the email content. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the email.

### UnifiedEmailParticipant

Represents a participant in an email. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedEmailParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedEmail

**Type**
string

**Properties**
Filter, Nillable

**Description**
Email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Participant’s role in the email.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedMeeting

**Field** **Details**

```
PersonId

### UnifiedMeeting

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the email.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a meeting that was captured or synced from an Event record. This object is available for reports and dashboards in the Winter
’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects UnifiedMeeting

**Field** **Details**

**Description**
The date and time of the meeting in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

InternalEventKey

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedMeeting` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.


### Standard Objects UnifiedMeetingParticipant

**Field** **Details**

```
IsInsightAvailable

Snippet

Subject

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the event description. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the meeting.

### UnifiedMeetingParticipant

Represents a participant in a meeting. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedMeetingParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the meeting that the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedMeeting

**Type**
string

**Properties**
Filter, Nillable

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the meeting.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedTask

**Field** **Details**

```
PersonId

### UnifiedTask

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact, lead, or user participating in the meeting.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a business activity such as a to-do item. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects UnifiedTask

**Field** **Details**

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

InternalEventKey

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedTask` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
Task

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.


### Standard Objects UnifiedTaskParticipant

**Field** **Details**

```
IsInsightAvailable

Snippet

Subject

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the task body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
The subject line of the task.

### UnifiedTaskParticipant

Represents a participant in a task. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedTaskParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedTask

**Type**
string

**Properties**
Filter, Nillable

**Description**
Username of the participant. The username is captured at the time of the communication;
it doesn’t change if the contact’s username is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedVideoCall

**Field** **Details**

```
PersonId

### UnifiedVideoCall

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact, lead, or user participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a video call that is captured or synced from the VideoCall or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.


Standard Objects UnifiedVideoCall

**Field** **Details**

```
ActivitySubType

ActivityType

CallDurationInSeconds

DetailId

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVideoCall` .

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the video call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup


### Standard Objects UnifiedVideoCallParticipant

**Field** **Details**

**Refers To**
VideoCall

```
InternalEventKey

IsInsightAvailable

Snippet

Subject

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it.

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the video call.

### UnifiedVideoCallParticipant

Represents a participant in a video call. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects UnifiedVideoCallParticipant

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ListenRatio

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the video call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedVideoCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the video call.

**Type**
picklist


### Standard Objects UnifiedVoiceCall

**Field** **Details**

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

```
PersonId

TalkRatio

### UnifiedVoiceCall

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was talking versus listening in the video call.

Represents a voice call that is captured or synced from a VoiceCall or Task record. This object is available for reports and dashboards in
the Winter ’24 release and later.


Standard Objects UnifiedVoiceCall

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

ActivitySubType

ActivityType

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVoiceCall` .


Standard Objects UnifiedVoiceCall

**Field** **Details**

```
CallDurationInSeconds

DetailId

InternalEventKey

IsInsightAvailable

Snippet

```

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the voice call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
VoiceCall

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string


### Standard Objects UnifiedVoiceCallParticipant

**Field** **Details**

**Properties**
Nillable

**Description**
An abbreviation of the voice call content. This field has a maximum length of 255 characters.

```
Subject

```

**Type**
string

**Properties**
None

**Description**
Contains the subject of the voice call.

### UnifiedVoiceCallParticipant

Represents a participant in a voice call. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the voice call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity


Standard Objects UnifiedVoiceCallParticipant

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
UnifiedVoiceCall

```
ChannelAddress

ListenRatio

ParticipantType

PersonId

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The phone number of the participant. The phone number is captured at the time of the
communication; it doesn’t change if the contact’s phone number is updated later.

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the voice call.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UnitOfMeasure

**Field** **Details**

**Description**
ID of the person participating in the voice call.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

```
TalkRatio

### UnitOfMeasure

```

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was talking versus listening in the voice call.

Defines the units and systems of units used to express and account for quantities. This object is available in API version 61.0 and later.

Examples of units of measure include Litre (for volume), Kilogram (for weight), and single units (such as Can, sachet, and packet).

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConversionFactor

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The factor or rate that's used to convert this unit of measurement to the base unit. For
example, for the Weight unit of measure class, the default unit of measure is pounds (lbs).
Then, all units of measure records with the Weight unit of measure class are converted to


Standard Objects UnitOfMeasure

**Field** **Details**

equate 1 unit to 1 pound. If the unit of measure is kilogram, the conversion factor is 2.2 as 1
pound consists of 2.2 kilograms.

```
Description

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
The description of this unit of measure.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the unit of measure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.


Standard Objects UnitOfMeasure

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
Group, User

```
Type

Sequence

Status

UnitCode

UnitOfMeasureClassId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The type of the unit of measure. For example, weight, distance, period.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequence number assigned to the unit of measure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the unit of measure.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Code for the unit of measure.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects UriEventLog

**Field** **Details**

**Description**
The class associated with the unit of measurement.

This field is a relationship field.

**Relationship Name**
UnitOfMeasureClass

**Refers To**
UnitOfMeasureClass

### UriEventLog

URI events contain details about user interaction with the web browser UI. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

```

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


Standard Objects UriEventLog

**Field** **Details**

```
DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

LoginKey

ReferrerUri

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how much activity is occurring in the database.

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
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The referring URI of the page that’s receiving the request.


Standard Objects UriEventLog

**Field** **Details**

```
RequestIdentifier

RequestStatus

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

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


Standard Objects UriEventLog

**Field** **Details**

```
Timestamp

Uri

UserIdentifier

UserType

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


### Standard Objects UsageImpactFactor

**Field** **Details**

customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### UsageImpactFactor

Represents a collection of fields to set up the Usage Impact Factors used across jurisdictions and programs.This object is available in API
version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
IsActive

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Factor is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Factor.


Standard Objects UsageImpactFactor

**Field** **Details**

```
ShortForm

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Factor.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Factor

Possible values are:

**•** `AdjustedGrossAnnual` —Adjusted Gross Annual

**•** `AdjustedGrossAnnualMMBTU` —Adjusted Gross Annual MMBTU

**•** `AdjustedGrossAnnualkW` —Adjusted Gross Annual kW

**•** `AdjustedGrossAnnualkWSummer` —Adjusted Gross Annual kW Summer

**•** `AdjustedGrossAnnualkWWinter` —Adjusted Gross Annual kW Winter

**•** `AdjustedGrossAnnualkWh` —Adjusted Gross Annual kWh

**•** `GrossAnnualMMBTU` —Gross Annual MMBTU

**•** `GrossAnnualkW` —Gross Annual kW

**•** `GrossAnnualkWh` —Gross Annual kWh

**•** `NetAnnual` —Net Annual

**•** `NetLifetime` —Net Lifetime

**•** `NetToGross` —Net To Gross

**•** `NetToGrossFR` —Net To Gross FR

**•** `UsefulLife` —Useful Life

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.


### Standard Objects UsageImpactGroup

**[UsageImpactFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactFactorShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroup

Represents a collection of fields to set up the Usage Impact Groups used across jurisdictions and programs. This object is available in
API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
Description

IsActive

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects UsageImpactGroupFactor

**Field** **Details**

**Description**
The name of the Usage Impact Group.

```
ShortForm

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Group.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Group.

Possible values are:

**•** `ForwardMarkets` —Forward Markets

**•** `Planning`

**•** `Production`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupFactor

Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0 and
later.


Standard Objects UsageImpactGroupFactor

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
FactorValue

IsActive

Name

UnitOfMeasureId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Defines the value of the Usage Impact Group Factor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group Factor is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Factor.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The UnitOfMeasure object associated with the Usage Impact Group Factor.

This field is a relationship field.


Standard Objects UsageImpactGroupFactor

**Field** **Details**

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

```
UsageImpactFactorId

UsageImpactGroupVersionId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Factor object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactFactor

**Relationship Type**
Lookup

**Refers To**
UsageImpactFactor

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroupVersion

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects UsageImpactGroupPgmMeasure

**[UsageImpactGroupFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupFactorShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupPgmMeasure

Represents a junction between the program, product, and Usage Impact Group version. This object is available in API version 58.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
Description

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Program Measure.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Program Measure.


Standard Objects UsageImpactGroupPgmMeasure

**Field** **Details**

```
Product2Id

ProgramId

UsageImpactGroupVersionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Usage Impact Group Program Measure.

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
Create, Filter, Group, Sort, Update

**Description**
The Program object associated with the Usage Impact Group Program Measure.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup

**Refers To**
Program

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version associated with the Energy Saving Group Association.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup


### Standard Objects UsageImpactGroupVersion

**Field** **Details**

**Refers To**
### UsageImpactGroupVersion

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupPgmMeasureChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupPgmMeasureFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupPgmMeasureHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupPgmMeasureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupPgmMeasureShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupVersion

Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
ApprovedMeasureExtlid

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The approved Measure Category ID assigned by a regulator.


Standard Objects UsageImpactGroupVersion

**Field** **Details**

```
Description

EndDate

IsActive

Name

StartDate

TechResourceManualCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Version.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group Version is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Version.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UsageImpactGroupVersion

**Field** **Details**

**Description**
The code and version of the Technical Reference Manual which is the source for the values
associated with this Usage Impact Group Version. This is necessary for regulatory reporting.

```
UsageImpactGroupId

Version

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group object associated with the Usage Impact Group Version.

This field is a relationship field.

**Relationship Name**
UsageImpactGroup

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroup

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the Usage Impact Group Version.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupVersionShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects User User

Represents a user in your organization.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

**•** To create or update a User record, you must have the Manage Internal Users permission. If the user is a Customer Portal user, you
must have the Manage Customer Users permission. If the user is a partner portal user, you must have the Manage External Users
permission. But the `describeSObjects` call always returns `createable` as `true` .

**•** If digital experiences is enabled, to create or update external users for Customer Portal, partner portal, or Experience Cloud sites, you
must also have the Manage External Users permission.

**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

But internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** When requested by portal users, queries that look up to the User object, such as `owner.name` or `owner.email` sometimes
don’t return values when the portal user making the request doesn’t have Read access to the User record being queried.

The behavior depends on the number of domains associated with the lookup field. If the object can look up to more than one
domain, `owner.name` returns a value, but other detail fields don’t. For example, Case owner can look up to the User or Queue
objects. In this case, portal users can see only the value of `owner.name` . Other User detail fields, such as `owner.email` or
`owner.phone` don’t return a value.

If the object can look up to only a single domain, such as Account owner, then no detail fields return values, including `owner.name` .

**•** To change ownership of a record by updating its `OwnerId` field, you must have both the Transfer Record permission and Read
access to the User record of the new record owner.

**•** To view the `NumberOfFailedLogins` field, you must have the Manage User permission.

Fields

**Field** **Details**

```
AboutMe

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
Information about the user, such as areas of interest or skills. This field is available even if
Chatter is disabled.

```
AccountId

```

`Address` (beta)

```
Alias

BadgeText

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Account associated with a Customer Portal user.

This field is null for Salesforce users.

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
The compound form of the address. Read-only. See Address Compound Fields for details on
compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user’s alias. For example, `jsmith` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Experience Cloud site role, displayed on the user profile page just below the user name.


Standard Objects User

**Field** **Details**

```
BannerPhotoUrl

CallCenterId

City

CommunityNickname

CompanyName

ContactId

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's banner photo. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If Salesforce CRM Call Center is enabled, represents the call center that this user is assigned
to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city associated with the user. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique name used to identify this user in the Experience Cloud site.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the user’s company.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
ID of the Contact associated with this account. The contact must have a value in the
`AccountId` field or an error occurs.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

```
Country

CountryCode

CurrentStatus

DefaultCurrencyIsoCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country associated with the user. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code associated with the user.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text that describes what the user is working on.

Note: If you update this field, the API automatically adds a post of type
`UserStatus` on the user’s profile in Chatter.

This field is deprecated in API version 25.0. To achieve similar behavior, post to the
user directly by creating a FeedItem with the user’s ParentId.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
The user's default currency setting for new records. For example, if a user in France sets
`DefaultCurrencyIsoCode` to euros, then that’s their default currency.

Only applicable for organizations that use multiple currencies.

```
DefaultDivision

DefaultGroupNotificationFrequency

DelegatedApproverId

Department

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the user's Chatter group email notifications
when the user joins groups. The valid values are:

**•** `P` —Email on every post

**•** `D` —Daily digests

**•** `W` —Weekly digests

**•** `N` —Never

The default value is `N` . For Professional, Enterprise, Unlimited, and Developer Edition
organizations that existed before API version 22.0, the default value remains `D` .

This field is available in API version 21.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable,Sort, Update

**Description**
Id of the user who is a delegated approver for this user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company department associated with the user.


Standard Objects User

**Field** **Details**

```
DigestFrequency

Division

Email

EmailEncodingKey

EmailPreferencesAutoBcc

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The send frequency of the user’s Chatter personal email digest. The valid values
are:

**•** `D` = Daily

**•** `W` = Weekly

**•** `N` = Never

The default value is `D` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The division associated with this user, similar to Department, and unrelated to
`DefaultDivision` .

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The user’s email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The email encoding for the user, such as `ISO-8859-1` or `UTF-8` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the user receives copies of sent emails. This option applies only if
compliance BCC emails aren’t enabled.


Standard Objects User

**Field** **Details**

```
EmployeeNumber

EndDay

Extension

Fax

FederationIdentifier

FirstName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s employee number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally stops working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s phone extension number.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s fax number.

**Type**
string

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Indicates the value that must be listed in the `Subject` element of a Security Assertion
Markup Language (SAML) _IDP certificate_ to authenticate the user for a client application using
single sign-on. This value must be specified if the `SAML User ID Type` is Assertion
contains Federation ID from the User record. Otherwise, this field can’t be edited.

**Type**
string


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s first name.

```
ForecastEnabled

FullPhotoUrl

GeocodeAccuracy

HasUserVerifiedEmail

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user is enabled for forecasts ( `true` ) or not ( `false` ). Forecast user
has access to the forecasts page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo. This field is available even if Chatter is disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's email is verified ( `true` ) or not ( `false` ). The default value is
`false` . This field is available in API version 63.0 and later.


Standard Objects User

**Field** **Details**

```
HasUserVerifiedPhone

IndividualId

IsActive

IsPartner

IsPortalEnabled

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's phone number is verified ( `true` ) or not ( `false` ). The default
value is false. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this user. This field is available if Data Protection
and Privacy is enabled.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user has access to log in ( `true` ) or not ( `false` ). You can modify a
User's active status from the user interface or via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is a partner who has access to the partner portal ( `true` ) or not
( `false` ). This field isn’t available for release 9.0 and later. Instead, use `UserType` with the
value `Partner` or `Power Partner` .

**Type**
boolean


Standard Objects User

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an active, external, user has access to Experience Cloud sites or portals
( `true` ) or not ( `false` ).

This field is only available if one of these conditions is true:

**•** Digital experiences is enabled and you have community or portal user licenses

**•** Portals are enabled

Note: Users with External Identity licenses can access Experience Cloud sites even
if the flag is false.

```
IsPortalSelfRegistered

IsPrmSuperUser

IsProfilePhotoActive

JigsawImportLimitOverride

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is a Customer Portal user who self-registered for your organization's
Customer Portal ( `true` ) or not ( `false` ). This field isn’t available for release 9.0 and earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Available for partner portal users only. Indicates whether the user has super user access in
the partner portal ( `true` ) or not ( `false` ).

This field is available in API version 24.0 and later.

Note: This field isn’t automatically enabled. Contact Salesforce to enable this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has a profile photo ( `true` ) or not ( `false` ). This field is available
in API version 36.0 and later.

**Type**
int


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data.com user’s monthly addition limit. The value must be between zero and the
organization’s monthly addition limit. Label is **Data.com Monthly Addition Limit** . This
field is available in API version 27.0 and later.

```
LanguageLocaleKey

LastLoginDate

LastName

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The user’s language, such as French or Chinese (Traditional). Label is **Language** .

Note: In API version 47.0 and later, when using the DescribeSObjectResult API to
return PicklistEntry values from this picklist, the `active` value indicates whether
the language is in the user’s **Displayed Languages** ( `true` ) or the user’s **Available**
**Languages** ( `false` ). All other languages aren’t in the returned `active` value
array.

In API version 46.0 and earlier, the PicklistEntry `active` values indicate whether the
language is in either the user’s **Displayed Languages** or **Available Languages** lists
( `true` ) or not in either list ( `false` ).

**Type**
dateTime

**Properties**
Filter, Sort, Nillable

**Description**
The date and time when the user last successfully logged in. This value is updated if 60
seconds elapses since the user’s last login.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user’s last name.

**Type**
datetime

**Properties**
Filter, Nillable, Sort


Standard Objects User

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Latitude

LocaleSidKey

Longitude

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) but not viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the geolocation of an address. Acceptable values are
numbers between –90 and 90 up to 15 decimal places. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. The value of the field affects formatting and
parsing of values, especially numeric values, in the user interface. It doesn’t affect the API.

The field values are named according to the language, and the country if necessary, using
two-letter ISO codes. The set of names is based on the ISO standard. You can also manually
set a user’s locale in the user interface, and then use that value for inserting or updating other
users via the API.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the geolocation of an address. Acceptable values are
numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.


Standard Objects User

**Field** **Details**

```
Manager

ManagerId

MediumBannerPhotoUrl

MiddleName

MobilePhone

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
User lookup field used to select the user's manager. This field establishes a hierarchical
relationship, preventing you from selecting a user that directly or indirectly reports to
themselves.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Id of the user who manages this user.

This is a relationship field.

**Relationship Name**
Manager

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the medium-sized user profile banner photo.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s middle name. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
phone


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s mobile device number.

```
Name

NumberOfFailedLogins

OfflineTrialExpirationDate

PasswordExpirationDate

Phone

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` . Limited to 203 characters, including
whitespaces.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of failed login attempts for the user’s account. When the maximum number of
failed login attempts is reached, the counter resets and the user’s account is locked. If there’s
a successful login before the maximum number of failed login attempts is reached, the
counter resets and the user’s account remains unlocked.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user’s Connect Offline trial expires.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user’s password expires. This field is available in API version 63.0
and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
The user’s phone number.

```
PortalRole

PostalCode

ProfileId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the user in the Customer Portal (either Executive, Manager, User, or PersonAcount).

In API version 15.0 and earlier, if you set this field to null, the system automatically included
a portal role. In API version 16.0 and above, when you set this field to null, a portal role is not
automatically created. When this field is null and a `ContactId` is provided, the user is
assigned to the User role.

The Update property is available in API version 43.0 and later.

The field is available if Customer Portal is enabled OR digital experiences is enabled and
Experience Cloud sites have available partner portal, Customer Portal, or High-Volume Portal
User licenses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s postal or ZIP code. Label is **Zip/Postal Code** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the user’s Profile. Use this value to cache metadata based on profile. In earlier
releases, this was `RoleId` .

If you change the user’s profile, the user’s license also changes, because every profile belongs
to exactly one user license type.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile


Standard Objects User

**Field** **Details**

```
ReceivesAdminInfoEmails

ReceivesInfoEmails

SenderEmail

SenderName

Signature

SmallBannerPhotoUrl

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives email for administrators from Salesforce ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives informational email from Salesforce ( `true` ) or not
( `false` ).

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address used as the From address when the user sends emails. This address is the
same value shown in Setup on the My Email Settings page.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name used as the email sender when the user sends emails. This name is the same value
shown in Setup on the My Email Settings page.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The signature text added to emails. This text is the same value shown in Setup on the My
Email Settings page.

**Type**
url


Standard Objects User

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the small user profile banner photo.

```
SmallPhotoUrl

StartDay

State

StateCode

Street

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo. This field is available even if Chatter is
disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally starts working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state associated with the User. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code associated with the user.

**Type**
textarea


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address associated with the User.

```
SuAccessExpirationDate

Suffix

TimeZoneSidKey

Title

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expiration date for allowing Salesforce Customer Support to log in as this user with Login
As functionality. After this date, the user must grant login access to Salesforce Customer
Support again. This field is available in API version 63.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s name suffix. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. A User time zone affects the offset used when
displaying or entering times in the user interface. But the API doesn’t use a User time zone
when querying or setting values.

Values for this field are named using region and key city, according to ISO standards. You
can also manually set one User time zone in the user interface, and then use that value for
creating or updating other User records via the API.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s business title, such as Vice President.


Standard Objects User

**Field** **Details**

```
Username

UserPermissionsCallCenterAutoLogin

UserPermissionsChatterAnswersUser

UserPermissionsInteractionUser

UserPermissionsJigsawProspectingUser

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Contains the name that a user enters to log in to the API or the user interface. The
value for this field must be in the form of an email address, using all lowercase characters. It
must also be unique across all organizations. If you try to create or update a User with a
duplicate value for this field, the operation is rejected.

Each inserted User also counts as a license. Every organization has a maximum number of
licenses. If you attempt to exceed the maximum number of licenses by inserting User records,
the create request is rejected.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if Salesforce CRM Call Center is enabled. Indicates whether the user is enabled to
use the auto login feature of the call center ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the portal user is enabled to use the Chatter Answers feature ( `true` ) or
not ( `false` ). This field defaults to `false` when a Customer Portal user is created from
the API.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user can run flows or not. Label is **Flow User** .

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
Indicates whether the user is allocated one Data.com user license ( `true` ) or not ( `false` ).
The Data.com user lets the user add Data.com contact and lead records to Salesforce in
supported editions. Label is **Data.com User** .

```
UserPermissionsKnowledgeUser

UserPermissionsLiveAgentUser

UserPermissionsMarketingUser

UserPermissionsOfflineUser

UserPermissionsSFContentUser

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Salesforce Knowledge ( `true` ) or not ( `false` ).
Label is **Knowledge User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Chat ( `true` ) or not ( `false` ). Label is **Live**
**Agent User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to manage campaigns in the user interface
( `true` ) or not ( `false` ). Label is **Marketing User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to use Offline Edition ( `true` ) or not ( `false` ).
Label is **Offline User** .

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
Indicates whether the user is allocated one Salesforce CRM Content User License ( `true` ) or
not ( `false` ). Label is **Salesforce CRM Content User** . The Salesforce CRM Content User
license grants the user access to the Salesforce CRM Content application.

```
UserPermissionsSiteforceContributorUser

UserPermissionsSiteforcePublisherUser

UserPermissionsSupportUser

UserPermissionsWirelessUser

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Contributor feature license ( `true` ) or
not ( `false` ). Label is **Site.com Contributor User** . The Site.com Contributor feature license
grants the user access to the Site.com application. Users with a Contributor license can use
Site.com Studio to edit site content only.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Publisher feature license ( `true` ) or not
( `false` ). Label is **Site.com Publisher User** . The Site.com Publisher feature license grants
the user access to the Site.com application. Users with a Publisher license can build and style
websites, control the layout and functionality of pages and page elements, and add and edit
content.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user can use the Salesforce console.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if the Wireless permission is enabled. Indicates whether the user is enabled to use
Wireless Edition ( `true` ) or not ( `false` ). Label is **Wireless User** .


Standard Objects User

**Field** **Details**

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.

```
UserPermissionsWorkDotComUserFeature

UserPreferencesActivityRemindersPopup

UserPreferencesAllowConversationReminders

UserPreferencesApexPagesDeveloperMode

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the WDC feature is enabled for the user ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder window automatically opens when an activity reminder is due.
Corresponds to the `Trigger alert when reminder comes due` checkbox at
the Reminders page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, voice and call reminders are displayed as notification cards in Lightning
Experience. Corresponds to the `Show conversation reminders in Lightning`
`Experience` checkbox in the Activity Reminders page in the personal settings in the user
interface.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, indicates that the user has enabled developer mode for editing Visualforce
pages and controllers.


Standard Objects User

**Field** **Details**

```
UserPreferencesAutoForwardCall

UserPreferencesContentEmailAsAndWhen

UserPreferencesContentNoEmail

UserPreferencesEnableAutoSubForFeeds

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user receives Dialer calls simultaneously in their browser and on their
forwarding number.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, a user with Salesforce CRM Content subscriptions receives a once-daily email
summary if activity occurs on the subscribed content, libraries, tags, or authors. To receive
email, the `UserPreferencesContentNoEmail` field must also be `false` .

The default value is `false` .

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, a user with Salesforce CRM Content subscriptions receives email notifications
if activity occurs on the subscribed content, libraries, tags, or authors. To receive real-time
email alerts, set this field to `false` and set the
`UserPreferencesContentEmailAsAndWhen` field to `true` .

The default value is `false` .

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user automatically subscribes to feeds for any objects that the user creates.
This field is available in API version 25.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesDisableAllFeedsEmail

UserPreferencesDisableAutoSubForFeeds

UserPreferencesDisableBookmarkEmail

UserPreferencesDisableChangeCommentEmail

UserPreferencesDisableEndorsementEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email for all updates to Chatter feeds, based
on the types of feed emails and digests the user has enabled. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically subscribes to feeds for any objects that the user creates.
This field is deprecated in API version 25.0 and later. Starting with API version 25.0, use
`UserPreferencesEnableAutoSubForFeeds` to enable or disable auto-follow
for objects a user creates.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
Chatter feed item after the user has bookmarked it. This field is available in API version 24.0
and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
change the user has made, such as an update to their profile. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the member automatically receives email every time someone endorses
them for a topic.

```
UserPreferencesDisableFileShareNotificationsForApi

UserPreferencesDisableFollowersEmail

UserPreferencesDisableLaterCommentEmail

UserPreferencesDisableLikeEmail

UserPreferencesDisableMentionsPostEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, email notifications are sent from the person who shared the file to the users
that the file is shared with. This field is available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone starts following
the user in Chatter. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
feed item after the user has commented on the feed item. This field is available in API version
24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone likes their post or
comment. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time they’re mentioned in posts.
This field is available in API version 24.0 and later.

```
UserPreferencesDisableProfilePostEmail

UserPreferencesDisableSharePostEmail

UserPreferencesDisableFeedbackEmail

UserPreferencesDisCommentAfterLikeEmail

UserPreferencesDisMentionsCommentEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone posts to the user’s
profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time their post is shared. This
field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives emails related to WDC feedback. The user
receives these emails when someone requests or offers feedback, shares feedback with the
user, or reminds the user to answer a feedback request.

This field isn’t visible as of API version 54.0.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
post that the user liked. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time the user is mentioned in
comments. This field is available in API version 24.0 and later.

```
UserPreferencesDisableMessageEmail

UserPreferencesDisableRewardEmail

UserPreferencesDisableWorkEmail

UserPreferencesDisProfPostCommentEmail

UserPreferencesEnableVoiceCallRecording

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email for Chatter messages sent to the user.
This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives emails related to WDC rewards. The user
receives these emails when someone gives a reward to the user.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user receives emails related to WDC feedback, goals, and coaching. The
user must also sign up for individual emails listed on the WDC email settings page. When
`true`, the user doesn’t receive any emails related to WDC feedback, goals, or coaching even
if they’re signed up for individual emails.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on
posts on the user’s profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `true`, voice call recording is enabled for the user.

```
UserPreferencesEnableVoiceLocalPresence

UserPreferencesEventRemindersCheckboxDefault

UserPreferencesHideBiggerPhotoCallout

UserPreferencesHideChatterOnboardingSplash

UserPreferencesHideCSNDesktopTask

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, local numbers are shown when the user calls customers with Sales Dialer.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder popup is automatically set on the user's events. Corresponds to
the `By default, set reminder on Events to...` checkbox on the
Reminders page in the user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, users can choose to hide the callout text below the large profile photo.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the initial Chatter onboarding prompts don’t appear.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Chatter recommendations panel never displays the recommendation to
install Chatter Desktop. This field is available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesHideCSNGetChatterMobileTask

UserPreferencesHideEndUserOnboardingAssistantModal

UserPreferencesHideLightningMigrationModal

UserPreferencesHideSecondChatterOnboardingSplash

UserPreferencesHideS1BrowserUI

UserPreferencesHideSfxWelcomeMat

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Chatter recommendations panel never displays the recommendation to
install Chatter Mobile. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the secondary Chatter onboarding prompts don’t appear.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls the interface that the user sees when logging in to Salesforce from a supported
mobile browser. If `false`, the user is automatically redirected to the Salesforce mobile
web. If `true`, the user sees the full Salesforce site. The default value is `false` . Label is
**Salesforce User** .

This field is available in API version 29.0 or later.

**Type**
boolean


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Controls whether a user sees the Lightning Experience new user message. That message
welcomes users to the new interface and provides step-by-step instructions that describe
how to return to Salesforce Classic.

```
UserPreferencesJigsawListUser

UserPreferencesLightningExperiencePreferred

UserPreferencesLiveAgentMiawSetupDeflection

UserPreferencesNativeEmailClient

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user is a Data.com List user so shares record additions from a pool.
UserPermissionsJigsawProspectingUser must also be set to `true` . Label is **Data.com List**
**User** . This field is available in API version 27.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, redirects the user to the Lightning Experience interface. Label is **Switch to**
**Lightning Experience** . This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, disables the pop-up to deflect users on Chat setup nodes to the Messaging
setup. The default value is `false` . This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Use this field to set a default email preference for the user’s native email client. This field is
available in API version 47.0 and later. The default value is `false`, corresponding to the
Salesforce docked email composer.


Standard Objects User

**Field** **Details**

```
UserPreferencesOptOutOfTouch

UserPreferencesOutboundBridge

UserPreferencesPathAssistantCollapsed

UserPreferencesProcessAssistantCollapsed

UserPreferencesReceiveNoNotificationsAsApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
This field is deprecated in API version 29.0. When `false`, the user automatically accesses
the Salesforce Touch app when logging in to Salesforce from an iPad. If `true`, automatic
access to the Salesforce Touch app is turned off and the user’s iPad is directed to the full
Salesforce site instead. The default value is `false` .

Note: Salesforce Touch must be enabled before this field is visible.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, outbound calls are made through the user’s phone.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, Sales Path appears collapsed or hidden to the user. This field is available in API
version 35.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, Sales Path appears collapsed or hidden to the user. This field is available in API
versions 33.0 and 34.0 only. In API versions 35.0 and later, use
`UserPreferencesPathAssistantCollapsed` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for _approvers_ .


Standard Objects User

**Field** **Details**

**•** If `true`, emails are _disabled_ .

**•** If `false`, emails are _enabled_ .

The default value is `false` .

Note: The `Receive Approval Request Emails` setting in the UI
controls this field and the

```
                     UserPreferencesReceiveNotificationsAsDelegatedApprover
```

field.

**•** Setting: **If I’m an approver or delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Only if I’m an approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: **Only if I’m a delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Never**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

```
UserPreferencesReceiveNotificationsAsDelegatedApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for _delegated approvers_ .

**•** If `true`, emails are _enabled_ .

**•** If `false`, emails are _disabled_ .

The default value is `false` .

Note: The `Receive Approval Request Emails` setting in the UI
controls this field and the
`UserPreferencesReceiveNoNotificationsAsApprover` field.

**•** Setting: **If I’m an approver or delegated approver**


Standard Objects User

**Field** **Details**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Only if I’m an approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: **Only if I’m a delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Never**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

```
UserPreferencesReminderSoundOff

UserPreferencesShowCityToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a sound automatically plays when an activity reminder is due. Corresponds to
the `Play a reminder sound` checkbox on the Reminders page in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. City is visible only to
internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

City is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowCityToGuestUsers` is `true`,
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

The default value is `false` . This field is available in API version 26.0 and later.

```
UserPreferencesShowCityToGuestUsers

UserPreferencesShowCountryToExternalUsers

UserPreferencesShowCountryToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. When `true`, city is
visible to guest users. Guest users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated with each site. When
`false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCityToExternalUsers`, making the user’s city visible
to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. Country is visible
only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Country is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowCountryToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. When `true`,
country is visible to guest users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site. When `false`, this field returns the value `#N/A` .


Standard Objects User

**Field** **Details**

When `true`, this field overrides the value `false` in
`UserPreferencesShowCountryToExternalUsers`, making the user’s country
visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

```
UserPreferencesShowEmailToExternalUsers

UserPreferencesShowEmailToGuestUsers

UserPreferencesShowFaxToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. Email
address is visible only to internal members of the user’s organization when this field is `false` .
Email address is visible to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. When
`true`, the email address is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowEmailToExternalUsers`, making the user’s email address
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. Fax number
is visible only to internal members of the user’s organization when this field is `false` . Fax
number is visible to external members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowFaxToGuestUsers

UserPreferencesShowManagerToExternalUsers

UserPreferencesShowManagerToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. When `true`,
the fax number field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowFaxToExternalUsers`, making the user’s fax number
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. Manager is
visible only to internal members of the user’s organization when this field is `false` . Manager
is visible to external members in an Experience Cloud site when this field is `true` . External
users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. When `true`,
the manager field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowManagerToExternalUsers`, making the user’s manager
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowMobilePhoneToExternalUsers

UserPreferencesShowMobilePhoneToGuestUsers

UserPreferencesShowPostalCodeToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile device number field in the user’s contact information.
The number is visible only to internal members of the user’s organization when this field is
`false` . The number is visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer Portal, or partner portal
licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile phone field in the user’s contact information. When
`true`, the mobile phone field is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowMobilePhoneToExternalUsers`, making the user’s
mobile phone visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. Postal
code is visible only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Postal code is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowPostalCodeToGuestUsers`
is `true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

The default value is `false` . This field is available in API version 26.0 and later.

```
UserPreferencesShowPostalCodeToGuestUsers

UserPreferencesShowProfilePicToGuestUsers

UserPreferencesShowStateToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. When
`true`, postal code is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowPostalCodeToExternalUsers`, making the user’s
postal code visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the user’s profile photo. When `true`, the photo is visible to guest
users in an Experience Cloud site. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site.

When `false`, this field returns the stock photo. The default value is `false` . This field is
available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. State is visible only
to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

State is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowStateToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

```
UserPreferencesShowStateToGuestUsers

UserPreferencesShowStreetAddressToExternalUsers

UserPreferencesShowStreetAddressToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. When `true`, state
is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowStateToExternalUsers, making the user’s state visible to external
members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. The address
is visible only to internal members of the user’s organization when this field is `false` . The
address is visible to external members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. When
`true`, the street address field is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowStreetAddressToExternalUsers`, making the user’s
street address visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowTitleToExternalUsers

UserPreferencesShowTitleToGuestUsers

UserPreferencesShowWorkPhoneToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. Title is visible
only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Title is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowTitleToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `true` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. When `true`,
title is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone number field in the user’s contact information. The
number is visible only to internal members of the user’s organization when this field is
`false` . The number is visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer Portal, or partner portal
licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowWorkPhoneToGuestUsers

UserPreferencesSortFeedByComment

UserPreferencesSuppressEventSFXReminders

UserPreferencesSuppressTaskSFXReminders

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone field in the user’s contact information. When `true`,
the work phone field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowWorkPhoneToExternalUsers`, making the user’s work
phone visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies the data value used in sorting a user’s feed. When `true`, the feed is sorted by most
recent comment activity. When `false`, the feed is sorted by post date.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, event reminders don’t appear. Corresponds to the **Show event reminders**
**in Lightning Experience** checkbox on the Activity Reminders page in the user interface.
This field is related to UserPreference and customizing activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, task reminders don’t appear. Corresponds to the **Show task reminders in**
**Lightning Experience** . checkbox on the Activity Reminders page in the user interface. This
field is related to UserPreference and customizing activity reminders.


Standard Objects User

**Field** **Details**

```
UserPreferencesTaskRemindersCheckboxDefault

UserPreferencesUserDebugModePref

UserRoleId

UserType

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder popup is automatically set on the user's tasks. Corresponds to the
`By default, set reminder on Tasks to...` checkbox on the Reminders
page in the user interface. This field is related to UserPreference and customizing activity
reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Lightning Component framework executes in debug mode for the user.
Corresponds to the `Debug Mode` checkbox on the Advanced User Details page of personal
settings in the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user’s UserRole. Label is **Role ID** .

This is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort, Restricted picklist

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and
later, valid values include:


Standard Objects User

**Field** **Details**

**•** Standard: user license. This user type also includes Salesforce Platform and Salesforce
Platform One user licenses. Label is **Standard** .

**•** PowerPartner: User whose access is limited because they’re a partner and typically access
the application through a partner portal or Experience Cloud site. Label is **Partner** .

**•** CspLitePortal: user whose access is limited because they’re an org's customer and access
the application through a Customer Portal or Experience Cloud site. Label is **High Volume**
**Portal** .

**•** CustomerSuccess: user whose access is limited because they’re an org's customer and
access the application through a Customer Portal. Label is **Customer Portal User** .

**•** PowerCustomerSuccess: user whose access is limited because they’re an org's customer
and access the application through a Customer Portal. Label is **Customer Portal**
**Manager** .

Users with this license type can view and edit data they directly own or data owned by
or shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is **Chatter Free** .

**•** Guest: user whose access is limited because they’re an unauthenticated user without
login credentials. Label is **Guest** .

```
WirelessEmail

```

Usage

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Wireless email address associated with this user. For use with Salesforce Wireless Edition.
This field is available only if the Wireless and Email permissions are enabled for your
organization.

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.

Use this object to query information about users and to provision and modify users in your organization. Unlike other objects, the records
in the User table represent actual users—not data owned by users. Any user can query or describe User records.


Standard Objects User

For example, the following SOQL code finds users with a particular user role.

```
   SELECT Id, Username

   FROM User

   WHERE UserRoleId='00ED0000000xicT'

```

Each portal user is associated with a portal account. A portal account can have a maximum of three portal roles (Executive, Manager,
and User). You can select the default number of roles to be created from the user interface. The role hierarchy is maintained when you
insert and delete portal roles, and roles are created bottom-up. Deleting the User role causes the Manager role to be renamed to User
role. Deleting both the Executive and User roles causes the Manager role to be renamed to User role. Before deleting a role, you must
assign users under that role to another role.

Deactivate Users

You can’t delete a user in the user interface or the API. You can deactivate a user in the user interface; and you can deactivate or disable
a Customer Portal or partner portal user in the user interface or the API. Because users can never be deleted, we recommend that you
exercise caution when creating them.

[Be aware of the expected behaviors when deactivating users. See Considerations for Deactivating Users. The user interface provides](https://help.salesforce.com/s/articleView?id=platform.users_deactivate_considerations.htm&type=5&language=en_US)
options to auto-remove a user from teams, but the removal isn’t supported in API.

If you deactivate a user, any EntitySubscription where the user is associated with the ParentId or SubscriberId field, meaning all subscriptions
both to and from the user, are soft deleted. If the user is reactivated, the subscriptions are restored. However, if you deactivate multiple
users at once and these users follow each other, their subscriptions are hard deleted. In this case, the user-to-user EntitySubscription is
deleted twice (double deleted). Such subscriptions can’t be restored upon user reactivation.

Passwords

For security reasons, you can’t query User passwords via the API or the user interface. But the API allows you to set and reset User
passwords using the `setPassword()` and `resetPassword()` calls. The password lockout status and the ability to reset the
User locked-out status isn’t available via the API. Check and reset the User password lockout status using the user interface.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserChangeEvent (API version 44.0)**
Change events are available for the object.

**UserFeed (API version 18.0)**
Feed tracking is available for the object.

**UserShare**

Sharing is available for the object.

SEE ALSO:

_SOAP API Developer Guide_ [: Frequently-Occurring Fields](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_objects_fequently_occurring_fields.htm)

UserRole

UserLicense


### Standard Objects UserAccessChange UserAccessChange

Represents a change related to user access. This object is available in API version 57.0 and later.

### UserAccessChange records are created through different access-related operations. For example, being assigned to or removed from a

permission set.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To access UserAccessChange records, users must have the View Setup and Configuration permission.

Fields

**Field** **Details**

```
Source

### UserAccessPolicy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
### The source of the user access change. For example, UserAccessPolicyId .

Represents a user access policy. This object is available in API version 57.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To create or modify user access policies, users must have the Manage User Access Policies permission.


Standard Objects UserAccessPolicy

Fields

**Field** **Details**

```
BooleanFilter

Description

DeveloperName

Language

MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logic that determines how your user criteria filters are applied in the user access policy.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name for the user access policy.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the user access policy. In the UI, this field is Label.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserAccessPolicy

**Field** **Details**

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

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

```
Order

Status

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the order for which active policy is applied when a user meets the criteria for
multiple policies. Must be an integer from 0 to 10,000. Only the active policy with the lowest
`Order` value is applied. This field is required only if the `Status` field is set to `Active` .

Available in API version 61.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user access policy.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Design`

**•** `Failed`

**•** `Migrate`

**•** `Testing`

**•** `Updating`

The default value is `Design` .


### Standard Objects UserAccountTeamMember

**Field** **Details**

```
TriggerType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of user record trigger for which this user access policy runs.

Possible values are:

**•** `Create` —The user access policy runs when a user who matches the policy criteria is
created.

**•** `CreateAndUpdate` —The user access policy runs when a user who matches the
policy criteria is either created or updated.

**•** `Update` —The user access policy runs when a user who matches the policy criteria is
updated.

[For more information, see User Access Policies in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.perm_user_access_policies.htm&type=5&language=en_US)

### UserAccountTeamMember

Represents a User on the default account team of another User.

See also OpportunityTeamMember, which represents a User on the opportunity team of an Opportunity

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal and Chatter Free users can't access this object.

Fields

**Field** **Details**

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


Standard Objects UserAccountTeamMember

**Field** **Details**

**Description**
Required. For Account records that the user has added to his or her default account
team, the level of access the account team member has. . The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for accounts.

```
CaseAccessLevel

ContactAccessLevel

OpportunityAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the account team member has to Case records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for cases.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. ForContact records related to the account, the level of access that the
account team member has. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for contacts. When `DefaultContactAccess` is set to
`Controlled by Parent`, you can’t create or update this field.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


Standard Objects UserAccountTeamMember

**Field** **Details**

**Description**
Required. Level of access that the team member has to Opportunity records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for opportunities.

```
 OwnerId

 TeamMemberRole

 UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default account team.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the user has added his
or her default account team. The valid values are set by the organization’s administrator
in the Account Team Roles picklist. Label is **Team Role** .

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default account team. This field
cannot be updated.

This object is available only in organizations that have enabled the account teams functionality, which can be done using the user
interface.

If you attempt to create a record that matches an existing record, the create call updates any modified fields and returns the existing
record.

You can set up a User record so the default account team includes the others who typically work with them on accounts.


### Standard Objects UserAppInfo UserAppInfo

Stores the last Lightning app logged in to. If the user hasn’t logged into Salesforce or if the user lost access to the last accessed app, the
### UserAppInfo object stores a Null value. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AppDefinitionId

FormFactor

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the last Lightning app that the user logged in to. This field is available
in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The relative size of the app as displayed. Values are:

**•** Small—suitable for a small device like a mobile phone

**•** Medium—suitable for a tablet

**•** Large—suitable for a large display device, like a monitor

It’s possible to have three versions of the app as the one last logged in to, where
each version has a different form factor.


### Standard Objects UserAppMenuCustomization

**Field Name** **Details**

```
UserId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that used this app.

This is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Lookup

**Refers To**
### User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserAppInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### UserAppMenuCustomization

Represents an individual user’s settings for items in the app menu or App Launcher. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ApplicationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15-character ID for the application associated with the menu item.


Standard Objects UserAppMenuCustomization

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
Application

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

```
OwnerId

SortOrder

```

Usage

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user for these specific settings.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.

See the AppMenuItem object for the organization-wide default settings This object contains the fields representing any changes the
user made to the menu.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects UserAppMenuItem

**UserAppMenuCustomizationOwnerSharingRule**

Sharing rules are available for the object.

**UserAppMenuCustomizationShare**

Sharing is available for the object.

### UserAppMenuItem

Represents the organization-wide settings for items in the app menu or App Launcher that the requesting user has access to in Setup.
This object is available in API version 35.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
AppMenuItemId

ApplicationId

Description

IconUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the application associated with the menu item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A description of this menu item.

**Type**
url


Standard Objects UserAppMenuItem

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon for the menu item’s application.

```
InfoUrl

IsUsingAdminAuthorization

IsVisible

Label

LogoUrl

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL for more information about the application.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the app is pre-authorized for certain users by the administrator.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the app is visible to the user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The app’s name.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The logo for the menu item’s application. The default is the initials of the `Label`
value.


Standard Objects UserAppMenuItem

**Field Name** **Details**

```
MobileStartUrl

Name

SortOrder

StartUrl

Type

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location mobile users are directed to after they’ve authenticated. This is only
used with connected apps.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The API name of the item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location users are directed to after they’ve authenticated. For a connected
app, this is the location specified by the `StartUrl` . Otherwise it’s the
application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of application represented by this item. The types are:

**•** ConnectedApplication


### Standard Objects UserAuthCertificate

**Field Name** **Details**

**•** Network

**•** ServiceProvider

**•** TabSet

```
UserSortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that represents where the user set this item in the menu (or App
Launcher). For example, an item with a sort order value of 5 will appear between
items with sort order values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both
values. For example, if you want the user-sorted items to appear first, followed
by the organization order for the rest, use:

```
  SELECT ApplicationId,SortOrder,UserSortOrder FROM

  AppMenuItem order by userSortOrder NULLS LAST,

  sortOrder NULLS LAST

```

See the AppMenuItem object for the organization-wide default settings This object contains the fields the requesting user has permission
to see.

### UserAuthCertificate

Represents a user authentication certificate in your org. A user certificate is a unique PEM-encoded X.509 digital certificate to authenticate
individual users to your org. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in orgs with `Let users authenticate with a certificate` enabled in Identity Verification.
Only users with the Manage Internal Users permission can access this object.


Standard Objects UserAuthCertificate

Fields

**Field** **Details**

```
CertificateChain

CertificateChainLength

DeveloperName

ExpirationDate

Fingerprint

```

**Type**
base64

**Properties**
Create, Update

**Description**
The uploaded PEM files can contain a single certificate or up to 10 certificates in a certificate
chain. Uploaded PEM files can’t be larger than 1 MB.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-generated length of the certificate or certificate chain in the uploaded PEM file.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, Salesforce generates one for each record,
which slows performance.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The expiration date of the uploaded certificate.

**Type**
string

**Properties**
Filter. Group, idLookup, Sort


Standard Objects UserAuthCertificate

**Field** **Details**

**Description**
The unique fingerprint of the uploaded certificate.

```
Language

MasterLabel

SerialNumber

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language in which to display the certificate.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexico)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazil)

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
A descriptive name for the certificate.

**Type**
string

**Properties**
Filter, Group, Sort


### Standard Objects UserConfigTransferButton

**Field** **Details**

**Description**
The serial number of the uploaded certificate.

```
UserID

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user associated with the certificate.

### UserConfigTransferButton

Represents the association between a Chat configuration and a live chat button. This association allows users associated with a specific
configuration to transfer chats to a button queue.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
LiveChatButtonId

LiveChatUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the live chat button that agents can transfer chats to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserConfigTransferSkill

**Field Name** **Details**

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId` .

### UserConfigTransferSkill

Represents the association between a Chat configuration and a skill. This association allows users associated with a specific configuration
to transfer chats to agents who have that skill.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

SkillId

### UserCustomBadge

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the skill group that agents can transfer chats to.

Represents a custom badge for a user. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects UserCustomBadgeLocalization

Fields

**Field Name** **Details**

```
BadgeType

CustomText

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of badge. Valid values are:

**•** `Customer`

**•** `Partner`

**•** `Employee`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Custom text for the badge.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site or org that the badge is in.

### UserCustomBadgeLocalization

Represents the translated version of a custom badge for a user. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Translation Workbench must be enabled for your org.

**•** Users with the “Customize Application” or “Manage Translation” permission can create or update UserCustomBadge translations.


Standard Objects UserCustomBadgeLocalization

Fields

**Field Name** **Details**

```
Language

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language the UserCustomBadge is translated into.

This picklist contains these fully supported languages.

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
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.


### Standard Objects UserDailyMetric

**Field Name** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
ParentId

Value

### UserDailyMetric

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the UserCustomBadge.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the UserCustomBadge. Label is **Translation Text** .

Represents the daily engagement metrics for a user. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

```

**Type**
int


Standard Objects UserDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Call Back Later.

```
AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Unqualified.

**Type**
int


Standard Objects UserDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this user in the day.

This is a calculated field.

```
AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsNotDeliveredCount

AllEmailsOutOfOfficeCount

AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this user in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of emails sent by this user in the day.

This is a calculated field.

```
AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

DailyCutOffTimeStamp

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls by this user with all call results in the day.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.


Standard Objects UserDailyMetric

**Field** **Details**

```
Date

DateInt

HardBounceTrackableSends

LinkClickTrackableSends

OpenTrackableSends

OutOfOfficeTrackableSends

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
The number of emails sent with hard bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 53.0 and later.


Standard Objects UserDailyMetric

**Field** **Details**

```
RecipientReplies

RecipientSends

ReplyTrackableRecipientSends

ReplyTrackableSends

SoftBounceTrackableSends

SomeEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who responded to an email. Available in API version 53.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who were sent an email. Available in API version 53.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with reply tracking. Available in API version
53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This is a calculated field.

```
SomeEmailsDeliveredRate

TrackableRecipientSendReplyRt

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This is a calculated field.


Standard Objects UserDailyMetric

**Field** **Details**

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of unique recipients who clicked a link in an email sent by the user on the day.

```
UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

UserId

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by the user on the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by the user on the day.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserDailyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserDailyMetricShare on page 67**
Sharing is available for the object.


### Standard Objects UserDailyMetricOwnerSharingRule UserDailyMetricOwnerSharingRule

Represents the rules for sharing the user daily metric with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines the level of access users have to records. Values are:

**•** `Read` (read only)

**•** `Edit` (read/write)

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the sharing rule. Maximum length is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a


### Standard Objects UserDefinedLabel

**Field** **Details**

letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

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
ID of the source group. Records that are owned by users in the source group trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the UI. Maximum length is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that you are granting access to.

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

UserDailyMetric

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### UserDefinedLabel

Represents a label created by a user to help organize, track, and find records. This object is available in API version 61.0 and later.


Standard Objects UserDefinedLabel

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Color

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Hexadecimal value of the color used to help organize the UserDefinedLabel records.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly. For example,
accessed through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.
For example, accessed through a list view or related record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the UserDefinedLabel record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects UserDefinedLabelAssignment

**Field** **Details**

**Description**
ID of the user or group that owns the label.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
TotalAssignments

Type

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Calculated field. Number of related UserDefinedLabelAssignment records. Available in API
version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of user-defined label.

Possible values are:

**•** `Starred`

**•** `Tag`

### • User

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserDefinedLabelShare on page 67**
Sharing is available for the object.

### UserDefinedLabelAssignment

Represents a relationship between a record label and the item the user assigned it to. This object is available in API version 61.0 and
later.


Standard Objects UserDefinedLabelAssignment

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EntityType

ItemId

LabelId

OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object label of the Item record derived from ItemId. Available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Item record added to the UserDefinedLabel record.

This field is a polymorphic relationship field.

**Relationship Name**
Item

**Refers To**
Account, ActionCadence, ActionCadenceStepTracker, CallTemplate, Case, Contact,
EmailTemplate, FlowOrchestrationWorkItem, Lead, Opportunity, Task

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the UserDefinedLabel record that the Item record is assigned to.

This field is a relationship field.

**Relationship Name**
Label

**Refers To**
UserDefinedLabel

**Type**
reference


### Standard Objects UserDevice

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
SortOrder

SubjectOrName

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Order of the assigned items for a given UserDefinedLabel record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Item record. If it's a task, the value is the subject of the Item record.

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelAssignmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserDefinedLabelAssignmentShare on page 67**
Sharing is available for the object.

### UserDevice

Represents information unique to a device. Available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects UserDevice

Special Access Rules

You must have View Devices enabled to see devices.

Fields

**Field Name** **Details**

```
BrowserType

DeviceNativeUid

DeviceType

IsVerified

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser used for login.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A unique string used to identify a mobile device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The device used to log in to Salesforce. The picklist options are:

**•** `Desktop`

**•** `Tablet`

**•** `iPad`

**•** `iPhone`

**•** `Phone`

**•** `Unknown`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


Standard Objects UserDevice

**Field Name** **Details**

```
LastLoginHistoryId

Name

PlatformType

PlatformVersion

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most recent LoginHistory associated with the device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and can’t be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operating system of the device. The picklist options are:

**•** iOS

**•** Android

**•** OSX

**•** Linux

**•** Phone

**•** Windows

**•** AppleApp

**•** Blackberry

**•** Other

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the operating system running on the device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects UserDeviceApplication

**Field Name** **Details**

**Description**
The activity status of the device. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

```
UserId

UserLastSeen

UserProvidedDeviceIdentifier

### UserDeviceApplication

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the user’s last access.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
An identifier for the user’s device such as the International Mobile Equipment
Identity (IMEI) number or the device serial number.

Note: This field isn’t automatically populated. The developer must provide
values.

Represents information on applications installed on a device that is accessing Salesforce. Available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects UserDeviceApplication

Special Access Rules

You must have View Devices enabled to see devices.

Fields

**Field Name** **Details**

```
ApplicationType

Name

Status

UserDeviceId

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application used to log in to Salesforce.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and cannot be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The activity status of the device application. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events.
`UserDeviceId` is a generated value that’s created when the mobile app is
initially run after installation.

**Type**
reference


### Standard Objects UserDeviceHistory

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.

### UserDeviceHistory

Represents tracking information on the UserDevice sObject. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data that has changed.

Possible values are:

**•** `Address`

**•** `AnyType`

**•** `AutoNumber`

**•** `Base64`

**•** `BitVector`

**•** `Boolean`

**•** `Content`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `DateOnly`

**•** `DateTime`

**•** `Division`

**•** `Double`


Standard Objects UserDeviceHistory

**Field** **Details**

**•** `DynamicEnum`

**•** `Email`

**•** `EncryptedBase64`

**•** `EncryptedText`

**•** `EntityId`

**•** `EnumOrId`

**•** `ExternalId`

**•** `Fax`

**•** `File`

**•** `HtmlMultiLineText`

**•** `HtmlStringPlusClob`

**•** `InetAddress`

**•** `Json`

**•** `Location`

**•** `MultiEnum`

**•** `MultiLineText`

**•** `Namespace`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Raw`

**•** `RecordType`

**•** `SfdcEncryptedText`

**•** `SimpleNamespace`

**•** `StringPlusClob`

**•** `Switchable_PersonName`

**•** `Text`

**•** `TimeOnly`

**•** `Url`

**•** `YearQuarter`

```
Field

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The field that has changed.

Possible values are:


Standard Objects UserDeviceHistory

**Field** **Details**

**•** `BrowserType` —Browser

**•** `DeviceNativeUid` —Device Native ID

**•** `DeviceType` —Device Type

**•** `HashedBrowserFingerPrint` —Hashed Browser Fingerprint

**•** `IsVerified` —Is Device Verified

**•** `LastLoginHistory` —Login History

**•** `Name`

**•** `PlatformType` —Platform or OS Type

**•** `PlatformVersion` —Platform or OS Version

**•** `RawBrowserFingerPrint` —Raw Browser Fingerprint Data

**•** `Status` —Device Status

**•** `User`

**•** `UserLastSeen` —Last time user was seen

**•** `UserProvidedDeviceIdentifier` —User provided device identifier

**•** `created` —Created.

**•** `feedEvent` —Feed event

**•** `individualMerged` —Individual Merged

**•** `locked` —Record locked.

**•** `ownerAccepted` —Owner (Accepted)

**•** `ownerAssignment` —Owner (Assignment)

**•** `unlocked` —Record unlocked.

```
NewValue

OldValue

UserDeviceId

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value after a change has occurred.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value before a change has occurred.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects UserEmailCalendarSync

**Field** **Details**

**Description**
The ID of the UserDevice object.

### UserEmailCalendarSync

Represents the user assignments of an Einstein Activity Capture configuration. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Einstein Activity Capture in your org.

Fields

**Field** **Details**

```
AssignedId

ConfigurationId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user or profile. Only Einstein Activity users can be added to a configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Einstein Activity Capture configuration. The configuration is created in Salesforce
Setup. After the configuration is created, the autogenerated ID is visible on the Configurations
tab. From Setup, in the Quick Find box, enter _`Einstein Activity Capture`_, and
then select **Settings** . Click the Configurations tab.

Use UserEmailCalendarSync to add and remove users to an Einstein Activity Capture configuration. You can add users to a configuration
via a user ID or a profile ID. You can add a profile to only one configuration and assign a profile to only one user.


### Standard Objects UserEmailPreferredPerson

This example adds two users to an Einstein Activity Capture configuration.

```
   // Create a list of UserEmailCalendarSync records

   List<UserEmailCalendarSync> usersToAdd = new ArrayList<>();

   // Populate the UserEmailCalendarSync record with the ID of

   // the user or profile, and with the ID of the Activity Capture configuration you are

   adding them to

   UserEmailCalendarSync user1 = new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',

    AssignedId = '005xxxxxxxxxxxx');

   UserEmailCalendarSync user2= new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',

    AssignedId = '005xxxxxxxxxxxx');

   // add the UserEmailCalendarSync users to your list

   usersToAdd.add(user1);

   usersToAdd.add(user2);

   // Insert the list of UserEmailCalendarSync into the database

   Database.SaveResult[] results = Database.insertImmediate(usersToAdd);

```

This example removes a user from an Einstein Activity Capture configuration.

To remove a user, call `UserEmailCalendarSync()`, passing in `null` for `ConfigurationId` .

```
   UserEmailCalendarSync user2Remove= new UserEmailCalendarSync(ConfigurationId = "", AssignedId

    ='005xxxxxxxxxxxx');

   Database.SaveResult results =Database.insertImmediate(user2Remove);

### UserEmailPreferredPerson

```

Represents a mapping for a user’s preferred record for an email address when multiple records match an email field.This object is available
in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ‘20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
Email

```

**Type**
email


Standard Objects UserEmailPreferredPerson

**Field** **Details**

**Properties**
Create, Filter,Group, idLookup, Sort, Update

**Description**
Required. The unique email the mapping applies to. This field is unique for each user.

```
Name

OwnerId

PersonRecordId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto-generated field.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The userId that owns the record. Each record is only accessible to the owner.

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
Required. The recordId of a contact, lead, or user that represents the preferred record for the
email address. Use cascade delete for contact and lead, and delete if the personId is a
deactivated user record.

This is a polymorphic relationship field.

**Relationship Name**
PersonRecord

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


### Standard Objects UserEmailPreferredPersonShare

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserEmailPreferredPersonChangeEvent (API version 62.0)**
Change events are available for the object.

### **UserEmailPreferredPersonShare**

Sharing is available for the object.

### UserEmailPreferredPersonShare

Represents a sharing entry on a UserEmailPreferredPerson object. Sharing is not customizable for UserEmailPreferredPerson records.This
object is available in API version 44.0 and later.

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

ParentId

```

**Type**
picklist

**Properties**
Create, Filter,Group, Restricted picklist, Sort, Update

**Description**
Required. The level of access allowed. Values can be:

**•** `All`

**•** `Edit`

**•** `Read`

.

**Type**
reference

**Properties**
Create, Filter,Group, Sort,


Standard Objects UserEmailPreferredPersonShare

**Field** **Details**

**Description**
Id of the parent record, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
UserEmailPreferredPerson

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter,Group, Nillable, Restricted picklist, Sort,

**Description**
Required. Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` . All other
`RowCause` values are read-only. After the sharing entry is created, this field can’t be edited.
Valid values can include:

**•** `Manual` —The User or Group has access because a user with All access manually shared
the record with them.

**•** `Owner` —The User is the owner of the record or is in a role above the record owner in
the role hierarchy.

**Type**
reference

**Properties**
Create, Filter,Group, Sort,

**Description**
Required. ID of the user or group that has been given access to the
`UserEmailPreferredPerson` record. The `UserOrGroupID` is polymorphic. The
label is `User/Group Id` .

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects UserLicense UserLicense

Represents a user license in your organization. A user license entitles a user to specific functionality and determines the profiles and
permission sets available to the user.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
LicenseDefinitionKey

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A string that uniquely identifies a particular user license. Label is `License Def. ID` .
Values are:

**AUL** : corresponds to the Salesforce Platform user license

**AUL1** : corresponds to the Salesforce Platform One user license

**AUL_LIGHT** corresponds to the Salesforce Platform Light user license

**FDC_ONE** corresponds to the Lightning Platform - One App user license

**FDC_SUB** corresponds to the Lightning Platform App Subscription user license

**Overage_Platform_Portal_User** corresponds to the Overage Authenticated Website user
license

**PID_STRATEGIC_PRM** : corresponds to the Gold Partner user license

**PID_CHATTER** corresponds to the Chatter Only user license

**PID_CONTENT** corresponds to the Content Only user license

**PID_Customer_Portal_Basic** : corresponds to the Customer Portal Manager Standard user
license and the Customer Portal User license

**PID_Customer_Portal_Standard** : corresponds to the Customer Portal Manager Custom
user license

**PID_FDC_FREE** corresponds to the Lightning Platform Free user license

**PID_IDEAS** corresponds to the Ideas Only user license

**PID_Ideas_Only_Portal** corresponds to the Ideas Only Portal user license

**PID_Ideas_Only_Site** corresponds to the Ideas Only Site user license

**PID_KNOWLEDGE** corresponds to the Knowledge Only user license

**PID_Customer_Community** corresponds to the Customer Community license.


Standard Objects UserLicense

**Field** **Details**

**PID_Customer_Community_Login** corresponds to the Customer Community Login
license.

**PID_Partner_Community** corresponds to the Partner Community license.

**PID_Partner_Community_Login** corresponds to the Partner Community Login license.

**PID_Limited_Customer_Portal_Basic** : corresponds to the Limited Customer Portal
Manager Standard user license

**PID_Limited_Customer_Portal_Standard** : corresponds to the Limited Customer Portal
Manager Custom user license

**PID_Overage_Customer_Portal_Basic** : corresponds to the Overage Customer Portal
Manager Standard user license

**PID_Overage_High Volume Customer Portal** corresponds to the Overage High Volume
Customer Portal user license

**Platform_Portal_User** : corresponds to the Authenticated Website user license

**POWER_PRM** : corresponds to the Partner user license

**POWER_SSP** : corresponds to the Customer Portal Manager user license

**SFDC** : corresponds to the Full CRM user license

```
MasterLabel

MonthlyLoginsEntitlement

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user license label.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum number of customer or partner portal logins allowed per month. A `null`
value in this field means the user license is charged according to the number of users rather
than the number of logins.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission


Standard Objects UserLicense

**Field** **Details**

```
MonthlyLoginsUsed

Name

Status

TotalLicenses

UsedLicenses

```

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
The number of successful logins for all users associated with a customer or partner portal
user license. This field has a non- `null` value if `MonthlyLoginsEntitlement` has
a non- `null` value.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The internal name of the user license.

Note: Your organization may also include custom user licenses.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current status of the user license. Valid values for this field are `Active` and `Disabled` .

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of user licenses in the organization.

This field is available in API version 32.0 and later.

**Type**
int


### Standard Objects UserListView

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The number of user licenses that are assigned to active users in the organization.

This field is available in API version 32.0 and later.

This field isn’t filterable in API version 64.0 or later when using it in a WHERE clause in a SOQL
query. Instead, you have to process the data after fetching all the records.

UsedLicensesLastUpdated

Usage

**Type**
dateTime

**Properties**
aggregate, Filter, Sort

**Description**
The timestamp of the query. If your license count exceeds your org’s allotted threshold, the
count timestamp reflects the previous day, otherwise the timestamp reflects the current day
and time.

This field is available in API version 41.0 and later.

Users with the “View Setup and Configuration” permission can use the UserLicense object to view the set of currently defined user
licenses in your organization.

The UserLicense object is currently used by bulk user creation to determine the user license to which each profile and permission set
belongs. For example, if you use the API to create portal users and you want to know which profile belongs to each portal user license,
you can query this object for each profile and check the `LicenseDefinitionKey` to identify the associated user license.

SEE ALSO:

Profile

PermissionSet

### UserListView

Represents the customizations a user made to a list view. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects UserListView

Fields

**Name** **Details**

```
LastViewedChart

ListViewId

SobjectType

UserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The last chart a user viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the list view.

This is a relationship field.

**Relationship Name**
ListView

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The API name of the sObject for the user list view.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects UserListViewCriterion

**Name** **Details**

**Refers To**
### User UserListViewCriterion

Represents the criterion for a user’s customized list view. The criterion consists of the filters or sort order a user added to a list view for
the Salesforce Mobile app. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Name** **Details**

```
ColumnName

Operation

SortOrder

UserListViewId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the column in the user list view.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which the list view is evaluated compared to other UserListViewCriterion objects
for the given UserListView.

**Type**
reference


### Standard Objects UserLocationAssignment

**Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user list view.

This is a relationship field.

**Relationship Name**
UserListView

**Relationship Type**
Lookup

**Refers To**
UserListView

```
Value

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field values used to filter the list view. For example, a value of `94105` if the Field is
`Billing Zip/Postal Code` shows only rows that have a billing ZIP code of 94105.

### UserLocationAssignment

Represents the assignment between a location and a user. This object is available in API version 57.0 and later.

Supported Calls:

create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(), undelete(), update(),
upsert()

Special Access Rules:

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

### `UserLocationAssignmentNumber`

**Type**
text


Standard Objects UserLocationAssignment

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for the association

```
AssignedTo

Location

Username

IsActive

```

Usage:

**Type**
foreignkey (user)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
User being associated with the location

**Type**
foreignkey (location)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Location being associated to the User

**Type**
string (derived)

**Properties**
Filter, Sort

**Description**
Username of the User that is associated to the Location

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Whether the location is active or not

The UserLocationAssignment object associates a user to specified work locations. To assign a user to multiple locations, create Multiple
UserLocationAssignment objects. Use the isActive field to indicates the user's current active location.


### Standard Objects UserLogin UserLogin

Represents the settings that affect a user’s ability to log into an organization. To access this object, you need the
`UserPermissions.ManageUsers` permission. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
IsFrozen

IsPasswordLocked

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true` [, the user account associated with this object is frozen. If a user's account](https://help.salesforce.com/s/articleView?id=platform.users_freeze.htm&language=en_US)
is frozen, they can't log in, but their account isn't deactivated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the user account associated with this object is locked because of too
many login failures. From the API, you can set this field to `false`, but not `true` .

Note: If the Lockout effective period is set to Forever (must be reset by
admin) in your org’s Password Policies Setup page, this field isn’t set to
`false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated user account. This field can’t be updated.


### Standard Objects UserMembershipSharingRule

Usage

To query for all frozen users in your organization:

```
   SELECT Id, UserId

   FROM UserLogin

   WHERE IsFrozen = true

```

[To freeze or unfreeze multiple users, use Data Loader.](https://help.salesforce.com/s/articleView?id=000387522&type=1&language=en_US)

### UserMembershipSharingRule

Represents the rules for sharing user records from a source group to a target group. A user record contains details about a user. Users
who are members of the source group can be shared with members of the target group. The source and target groups can be based
on roles, portal roles, public groups, or territories. This object is available in API version 26.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts


Standard Objects UserMembershipSharingRule

**Field** **Details**

on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
GroupId

Name

UserAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

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
The ID representing the target group being given access.


### Standard Objects UserMonthlyMetric

Usage

Use this object to manage sharing rules for user records. Source and target groups can include internal users, portal users, Chatter or
Chatter External users.

### UserMonthlyMetric

Represents the monthly engagement metrics for a user. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

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
The number of calls in the month for this user with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Meaningful Connect.

**Type**
int


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Not Interested.

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails sent by this user in the month.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent by this user in the month.

This is a calculated field.

```
AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

DeliveredRecipientCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user that soft bounced in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls with all call results for this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received an email. Available in API version 53.0
and later.

This is a calculated field.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
DeliveredRecipientRate

HardBounceTrackableSends

HrdBncTrackableRecipientSends

LinkClickTrackableSends

LinkClkTrackableRecipientSends

Month

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients who successfully received an email. Available in API
version 53.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with hard bounce tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with link click tracking. Available in API
version 53.0 and later.

**Type**
date


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

```
MonthInt

OooTrackableRecipientSends

OpenTrackableRecipientSends

OpenTrackableSends

OutOfOfficeTrackableSends

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
The number of recipients who were sent an email with out-of-office tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with open tracking. Available in API version
53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 53.0 and later.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
RecipientReplies

RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

RecipientsSoftBounce

ReplyTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who responded to an email. Available in API version 53.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who were sent an email. Available in API version 53.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of email recipients who were sent an email that hard bounced. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who responded with an out-of-office reply. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email that soft bounced. Available in API version
54.0 and later.

**Type**
int


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with reply tracking. Available in API version
53.0 and later.

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
The number of emails sent with reply tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with soft bounce tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This field is a calculated field.

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
The percentage of unique recipients who hard bounced an email with hard bounce tracking.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that resulted in out-of-office replies
from unique recipients. This field is a calculated field. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that soft
bounced.

This field is a calculated field. Available in API version 54.0 and later.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This field is a calculated field.

```
TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

UserId

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who clicked a link in an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by this user in the month.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.


### Standard Objects UserMonthlyMetricOwnerSharingRule

**Field** **Details**

This is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Lookup

**Refers To**
### User

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

### **UserMonthlyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserMonthlyMetricShare on page 67**
Sharing is available for the object.

### UserMonthlyMetricOwnerSharingRule

Represents the rules for sharing the user monthly metric with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects UserMonthlyMetricOwnerSharingRule

**Field** **Details**

**Description**
Determines the level of access users have to records. Values are:

**•** `Read` (read only)

**•** `Edit` (read/write)

```
Description

DeveloperName

GroupId

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the sharing rule. Maximum length is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the source group. Records that are owned by users in the source group trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the UI. Maximum length is 80 characters.


### Standard Objects UserPackageLicense

**Field** **Details**

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that you are granting access to.

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

UserMonthlyMetric

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### UserPackageLicense

Represents a license for an installed managed package, assigned to a specific user. This object is available in API version 31.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve() update()`

Fields

**Field Name** **Details**

```
IsRevoked

LastCreatedByChangeId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Reserved for internal use. This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserPackageLicense

**Field Name** **Details**

**Description**
ID of the user access change record related to this managed package license assignment. This
field is available only if user access policies are enabled. This field is available in API version 58.0
and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

```
LastDeletedByChangeId

PackageLicenseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user access change record related to this managed package license assignment being
revoked. This field is available only if user access policies are enabled. This field is available in API
version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The 18-character Globally Unique ID (GUID) that identifies the package license

This is a relationship field.

**Relationship Name**
PackageLicense

**Relationship Type**
Lookup

**Refers To**
PackageLicense


### Standard Objects UserPermissionAccess

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The User ID of the user licensed to use this package

Use this object, in conjunction with PackageLicense, to provide users access to a managed package installed in your organization.

### UserPermissionAccess

Represents the permissions accessibility for a current user. Available in API version 41.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
LastCacheUpdate

Permissions<PermissionName>

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of either the user info or org info, whichever is later.

**Type**
boolean

**Properties**
Filter

**Description**
The name of the permission, such as `PermissionsActivateContract` or
`PermissionsAuthorApex` and whether it’s available to the user ( `true` ) or not
( `false` ).


### Standard Objects UserPrioritizedRecord

Usage

API users without `PermissionsViewSetup` can use this object to check if their own sessions have access to a feature.

SEE ALSO:

Profile

PermissionSet

### UserPrioritizedRecord

Represents records that Pipeline Inspection, Account Intelligence, Contact Intelligence, and Lead Intelligence users flag as important for
tracking in pipeline and intelligence views and filters. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To use UserPrioritizedRecord in Pipeline Inspection and the Account Intelligence, Contact Intelligence, and Lead Intelligence views,
enable the Pipeline Inspection user permission and the Pipeline Inspection setting.

Fields

**Field** **Details**

```
OwnerId

TargetId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who marked this record as important.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


### Standard Objects UserPreference

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the target object that is marked as important. Supported objects include:

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

```
TargetKeyPrefix

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The key prefix of the target object that is marked as important.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserPrioritizedRecordOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserPrioritizedRecordShare on page 67**
Sharing is available for the object.

### UserPreference

Represents a functional preference for a specific user in your organization.


Standard Objects UserPreference

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can't access this object.

Only users with the View All Data or Manage Users permission can access UserPreference records of other users but all users can access
their own UserPreference record.

Note: This behavior does not affect other types of user access such as Create or Edit.

Fields

**Field** **Details**

```
Preference

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the user preference. Supported values are:

**•** `57` (Event Reminder Default Lead Time)

**•** `58` (Task Reminder Default Time)

**•** `91` (Prevent Logs on Load)

**•** `92` (Autocomplete Apex After Key Press)

**•** `93` (Visualforce Viewstate Inspector)

**•** `94` (Forecasting Displayed Type)

**•** `96` (Editor Theme)

**•** `97` (Editor Font Size)

**•** `98` (Pinned Folders)

**•** `99` (Enable Query Plan)

**•** `100` (Enable New Open Dialog)

**•** `101` (Email Transport Type)

**•** `102` (Pinned Wave Folders)

**•** `108` (Density)

**•** `109` (Lightning Flow Builder)

**•** `111` (Format with Tabs)

**•** `112` (Format Tab Width)

**•** `113` (Format Print Width)

**•** `114` (Record Page Activities Display)

**•** `118` (Lightning Flow Explorer)


Standard Objects UserPreference

**Field** **Details**

**•** `119` (For internal use only)

**•** `120` (Simple Auth Option)

**•** `122` (Sales Alert Notifications Snooze Time)

**•** `131` (Color Scheme)

`Event Reminder Default Lead Time` and `Task Reminder Default`
`Time` are related to these fields on the User object:

**•** `UserPreferencesEventRemindersCheckboxDefault`

**•** `UserPreferencesTaskRemindersCheckboxDefault`

**•** `UserPreferencesSuppressEventSFXReminders`

**•** `UserPreferencesSuppressTaskSFXReminders`

`Enable New Open Dialog` is reserved for future use.

When creating SOQL queries, `tolabel` is required to return accurate results. For example,

```
                   select Id, tolabel(Preference), Value, UserId from
```

`UserPreference` .

`108` (Density) is available in API v44.0 and later.

```
UserId

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user associated with this role. The corresponding field label is **User ID** .

Admin users can create and edit preferences for other users.

Standard users can delete their own preferences only. For a standard user, the value of the
`UserId` field must be their own UserId.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The value of the user preference. For `Event Reminder Default Lead Time`, the
values are increasing intervals of time from 0 minutes to 2 days. For `Task Reminder`
`Default Time`, the values are half-hours from 12:00 AM to 11:30 PM. To view the
respective sets of values, access the Reminders in your personal settings in the online
application.


### Standard Objects UserProfile

Usage

Use this object to query the set of currently configured user preferences in your organization. In your client application, you can query
the User object to obtain valid User IDs to access the UserPreference object.

All users can invoke the supported calls with this object. Standard users can invoke these calls, but only on their own preferences.

### UserProfile

Represents a Chatter user profile.

Note: This object has been deprecated as of API version 32.0. Use the User object to query information about a user in API version
32.0 and later.

Supported Calls

`describeLayout()`, `query()`, `retrieve()`

Special Access Rules

**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** Any fields that have been restricted in visibility will be returned empty, whether or not they are, and will not be removed from the
field listing.

Fields

**Field** **Details**

```
AboutMe

```

`Address` (beta)

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Information about the user, such as areas of interest or skills.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects UserProfile

**Field** **Details**

**Description**
The compound form of the address. Read-only. See Address
Compound Fields for details on compound address fields.

```
City

CompanyName

Country

Email

Fax

FirstName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country associated with the user profile.

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address associated with the user profile.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The fax number associated with the user profile.

**Type**
string


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s first name.

```
FullPhotoUrl

IsActive

IsBadged

LastName

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo if Chatter is enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has access to log in ( `true` ) or not
( `false` ). You can modify a User's active status from the user interface
or via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is visually badged ( `true` ) or not ( `false` ).
Users of the same Chatter user type (internal, external) are badged.
Different user types are not badged.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s last name.


Standard Objects UserProfile

**Field** **Details**

`Latitude` (beta)

`Longitude` (beta)

```
ManagerId

MobilePhone

Name

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who manages this user.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s mobile or cellular phone number.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` .


Standard Objects UserProfile

**Field** **Details**

```
Phone

PostalCode

SmallPhotoUrl

State

Street

Title

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s phone number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s postal or ZIP code. Label is **Zip/Postal Code** .

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo if Chatter is
enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state associated with the user profile.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address associated with the user profile.

**Type**
string


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s business title, such as “Vice President.”

```
UserPreferencesActivityRemindersPopup

UserPreferencesApexPagesDeveloperMode

UserPreferencesDisableAllFeedsEmail

UserPreferencesDisableBookmarkEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder window automatically opens when an
activity reminder is due. Corresponds to the `Trigger alert`
`when reminder comes due` checkbox at the Reminders
page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, indicates that the user has enabled developer mode
for editing Visualforce pages and controllers.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email for all updates
to Chatter feeds, based on the types of feed emails and digests the
user has enabled.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a Chatter feed item after the user has
bookmarked it.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableChangeCommentEmail

UserPreferencesDisableEndorsementEmail

UserPreferencesDisableFeedbackEmail

UserPreferencesDisableFileShareNotificationsForApi

UserPreferencesDisableFollowersEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a change the user has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the member automatically receives email every time
someone endorses them for a topic.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives emails related to WDC
feedback. This includes when someone requests or offers feedback,
shares feedback with the user, or reminds the user to answer a
feedback request.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, email notifications are sent from the person who
shared the file to the users that the file is shared with.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone starts following the user in Chatter.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableLaterCommentEmail

UserPreferencesDisableLikeEmail

UserPreferencesDisableMentionsPostEmail

UserPreferencesDisableMessageEmail

UserPreferencesDisableProfilePostEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a feed item after the user has commented
on the feed item.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone likes their post or comment.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
they’re mentioned in posts.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email for Chatter
messages sent to the user.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone posts to the user’s profile.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableRewardEmail

UserPreferencesDisableSharePostEmail

UserPreferencesDisableWorkEmail

UserPreferencesDisCommentAfterLikeEmail

UserPreferencesDisMentionsCommentEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives emails related to WDC
rewards. This includes when someone someone gives a reward to
the user.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time their
post is shared.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user receives emails related to WDC feedback,
goals, and coaching. The user must also sign up for individual emails
listed on the WDC email settings page. When `true`, the user will
not receive any emails related to WDC feedback, goals, or coaching
even if they are signed up for individual emails.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a post that the user liked.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time the
user is mentioned in comments.

```
UserPreferencesDisProfPostCommentEmail

UserPreferencesEnableAutoSubForFeeds

UserPreferencesEventRemindersCheckboxDefault

UserPreferencesHideChatterOnboardingSplash

UserPreferencesHideCSNDesktopTask

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on posts on the user’s profile.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the user automatically subscribes to feeds for any
objects that the user creates.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder popup is automatically set on the user's
events. Corresponds to the `By default, set reminder`
`on Events to...` checkbox on the Reminders page in the
user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the initial Chatter onboarding prompts do not appear.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
When `true`, the Chatter recommendations panel never displays
the recommendation to install Chatter Desktop.

```
UserPreferencesHideCSNGetChatterMobileTask

UserPreferencesHideS1BrowserUI

UserPreferencesHideSecondChatterOnboardingSplash

UserPreferencesReminderSoundOff

UserPreferencesShowCityToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the Chatter recommendations panel never displays
the recommendation to install Chatter Mobile.

**Type**
boolean

**Properties**
Filter

**Description**
Controls the interface that the user sees when logging in to Salesforce
from a supported mobile browser. If `false`, the user is automatically
redirected to the Salesforce mobile web. If `true`, the user sees the
full Salesforce site. The default value is `false` . Label is **Salesforce**
**User** .This field is available in API version 29.0 or later.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the secondary Chatter onboarding prompts do not
appear.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a sound automatically plays when an activity reminder
is due. Corresponds to the `Play a reminder sound`
checkbox on the Reminders page in the user interface.

**Type**
boolean


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
City is visible only to internal members of the user’s organization
when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

City is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowCityToGuestUsers` is `true`,
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

```
UserPreferencesShowCityToGuestUsers

UserPreferencesShowCountryToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
When `true`, city is visible to guest users. Guest users can access
public Site.com and Salesforce sites, and public pages in Experience
Cloud sites, via the Guest User license associated with each site. When
`false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCityToExternalUsers`, making
the user’s city visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. Country is visible only to internal members of the user’s
organization when:


Standard Objects UserProfile

**Field** **Details**

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Country is visible to external members in an Experience Cloud site
when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowCountryToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

```
UserPreferencesShowCountryToGuestUsers

UserPreferencesShowEmailToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. When `true`, country is visible to guest users. Guest
users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated
with each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCountryToExternalUsers`,
making the user’s country visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the email address field in the user’s contact
information. Email address is visible only to internal members of the
user’s organization when this field is `false` . Email address is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesShowFaxToExternalUsers

UserPreferencesShowManagerToExternalUsers

UserPreferencesShowMobilePhoneToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the fax number field in the user’s contact
information. Fax number is visible only to internal members of the
user’s organization when this field is `false` . Fax number is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the manager field in the user’s contact
information. Manager is visible only to internal members of the user’s
organization when this field is `false` . Manager is visible to external
members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner
portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the mobile device number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false` . The number is
visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer
Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesShowPostalCodeToExternalUsers

UserPreferencesShowPostalCodeToGuestUsers

UserPreferencesShowProfilePicToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. Postal code is visible only to internal members
of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Postal code is visible to external members in an Experience Cloud
site when:

**•** This field is `true`, or

**•** This field is `false` but

```
   UserPreferencesShowPostalCodeToGuestUsers
```

is `true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. When `true`, postal code is visible to guest
users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license
associated with each site. When `false`, this field returns the value
`#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowPostalCodeToExternalUsers`,
making the user’s postal code visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
Indicates the visibility of the user’s profile photo. When `true`, the
photo is visible to guest users in an Experience Cloud site. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site.

When `false`, this field returns the stock photo. The default value
is `false` . This field is available in API version 28.0 and later.

```
UserPreferencesShowStateToExternalUsers

UserPreferencesShowStateToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. State is visible only to internal members of the user’s
organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

State is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowStateToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. When `true`, state is visible to guest users. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowStateToExternalUsers, making the user’s state
visible to external members.


Standard Objects UserProfile

**Field** **Details**

The default value is `false` . This field is available in API version 28.0
and later.

```
UserPreferencesShowStreetAddressToExternalUsers

UserPreferencesShowTitleToExternalUsers

UserPreferencesShowTitleToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the street address field in the user’s contact
information. The address is visible only to internal members of the
user’s organization when this field is `false` . The address is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the business title field in the user’s contact
information. Title is visible only to internal members of the user’s
organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Title is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowTitleToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `true` . This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
Indicates the visibility of the business title field in the user’s contact
information. When `true`, title is visible to guest users. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title
visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

```
UserPreferencesShowWorkPhoneToExternalUsers

UserPreferencesTaskRemindersCheckboxDefault

```

Usage

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the work phone number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false` . The number is
visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer
Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder popup is automatically set on the user's
tasks. Corresponds to the `By default, set reminder on`
`Tasks to...` checkbox on the Reminders page in the user
interface. This field is related to UserPreference and customizing
activity reminders.

Use this object to query Chatter—related information about the user. While the User object contains all the information about a user
and is historically tied to user management, UserProfile is a read-only entity that contains the information that is relevant in a Chatter
context.


### Standard Objects UserProvAccount

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserProfileFeed (API version 18.0–26.0)**
Feed tracking is available for the object.

### UserProvAccount

Represents information that links a Salesforce user account with an account in a third-party (target) system, such as Google, for users of
connected apps with Salesforce user provisioning enabled. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConnectedAppId

DeletedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The 15 character application ID.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the associated user account in the target system was deleted. This
value is automatically updated during the provisioning and reconciling processes.


Standard Objects UserProvAccount

**Field** **Details**

```
ExternalEmail

ExternalFirstName

ExternalLastName

ExternalUserId

ExternalUsername

IsKnownLink

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The username as stored in the target system for the associated user account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects UserProvAccount

**Field** **Details**

**Description**
Setting the `IsKnownLink` value to `true` implies the administrator or another user is
managing the relationship between the Salesforce user account and the third-party user
account, manually. This field helps Salesforce coordinate updates between the
UserProvAccountStaging object and the UserProvAccount object while committing staged
accounts. Typically, for a matching user account (the same `ExternalUserId` for both
objects), Salesforce copies the values from the UserProvAccountStaging object to the
UserProvAccount object.

However, if Salesforce encounters a UserProvAccountStaging object with a matching
`ExternalUserId` but different `LinkState` and `SalesforceUserId` values
during this process, Salesforce checks the UserProvAccount `IsKnownLink` value. If the
`IsKnownLink` value is `true`, Salesforce doesn’t copy the `LinkState` and
`SalesforceUserId` values from the UserProvAccountStaging object to the
UserProvAccount object (all other values are copied).

The default is `false`, meaning Salesforce manages the account relationship.

```
LinkState

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce organization
and the associated user account in the target system. The valid values are:

**•** `linked`  - changes to the account in the Salesforce organization are queued to be
updated for the associated user account in the target system.

**•** `duplicate`  - an associated account in the target system exists.

**•** `orphaned` —no associated account exists in the target system.

**•** `ignored`  - changes to the account in the Salesforce organization have no effect on
the associated user account in the target system.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Namepointing, Sort, Update


### Standard Objects UserProvAccountStaging

**Field** **Details**

**Description**
The user ID of the owner of this object—typically a Salesforce administrator.

```
SalesforceUserId

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID for the user account in the Salesforce organization that is associated with the
user account in the target system.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
### User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the account in the target system. The valid values are:

**•** `Active`

**•** `Deactivated`

**•** `Deleted`

### UserProvAccountStaging

Temporarily stores user account information while a user completes the User Provisioning Wizard. This information that is stored in the
UserProvAccount object when you click the button to collect and analyze accounts on the target system.

User provisioning links a Salesforce user account with an account in a third-party (target) system. To configure user provisioning, you
use a User Provisioning Wizard that guides you through the setup process. As you enter values about account details in the wizard, these
values are stored in this object until you click the button to collect and analyze accounts on the target system. The general user provisioning
configuration details are stored in the UserProvisioningConfig object.


Standard Objects UserProvAccountStaging

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ConnectedAppId

ExternalEmail

ExternalFirstName

ExternalLastName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15 character connected app ID.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvAccountStaging

**Field Name** **Details**

**Description**

The last name as stored in the target system for the associated user account.

```
ExternalUserId

ExternalUsername

LinkState

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce
organization and the associated user account in the target system. The valid
values are:

**•** `linked`  - a user account matches one in the target system.

**•** `duplicate`  - an associated account in the target system exists.

**•** `orphaned` —no associated account exists in the target system.

**•** `ignored`  - changes to the account in the Salesforce organization have
no effect on the associated user account in the target system.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The unique name for this object.

**Type**
reference


Standard Objects UserProvAccountStaging

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.

```
SalesforceUserId

Status

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user ID for the user account in the Salesforce organization that is associated
with the user account in the target system.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the account in the target system. The valid values are:

**•** `Active`

**•** `Deactivated`

**•** `Deleted`

When committing fields from a UserProvAccountStaging to a UserProvAccount object, Salesforce looks up the UserProvAccount record
where `UserProvAccountStaging.ExternalUserId = UserProvAccount.ExternalUserId` .

**•** If an `ExternalUserId` doesn't match an existing account, Salesforce creates a UserProvAccount record based on the
UserProvAccountStaging record.

**•** If an `ExternalUserId` matches, then Salesforce checks the `UserProvAccount.isKnownLink` value, and does the
following.

**–** If `UserProvAccount.IsKnownLink = true`, Salesforce copies the UserProvAccountStaging values to the
UserProvAccount object, except for the `ExternalUserId` and `LinkState` values.


### Standard Objects UserProvMockTarget

**–** If `UserProvAccount.IsKnownLink = false`, Salesforce copies all of the UserProvAccountStaging values to the
UserProvAccount object.

### UserProvMockTarget

Represents an entity for testing user data before committing the data to a third-party system for user provisioning.

During the user provisioning process, user account information is sent to a third-party system to create, update or delete a user account
on that system. While configuring user provisioning for your organization using a flow or Apex action, you can use this object to confirm
the associated flow or Apex code is sending the desired data. After confirming the correct fields and values, you can update the flow or
Apex action to send the data to the target system.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ExternalEmail

ExternalFirstName

ExternalLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The last name as stored in the target system for the associated user account.


### Standard Objects UserProvisioningConfig

**Field Name** **Details**

```
ExternalUserId

ExternalUsername

Name

OwnerId

### UserProvisioningConfig

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.

Represents information for a flow to use during a user provisioning request process, such as the attributes for an update. This object is
available in API version 34.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects UserProvisioningConfig

Fields

**Field Name** **Details**

```
ApprovalRequired

ConnectedAppId

DeveloperName

Enabled

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Denotes whether approvals are required for provisioning users for the associated
connected app. If the value is null, no approval is required.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 18-digit application ID for the connected app.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

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
object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean


Standard Objects UserProvisioningConfig

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether user provisioning is enabled for the associated connected app
( `true` ) or not ( `false` ).

```
EnabledOperations

Language

LastReconDateTime

MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the operations, as comma-separated values, that create a
UserProvisioningRequest object for the associated connected app. Allowed values
are:

**•** `Create`

**•** `Update`

**•** `EnableAndDisable` (activation and deactivation)

**•** `SuspendAndRestore` (freeze and unfreeze)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The two- to five-character code that represents the language and locale ISO. This
code controls the language for labels displayed in an application.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The date and time when user accounts were last reconciled between Salesforce
and the target system.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects UserProvisioningConfig

**Field Name** **Details**

**Description**

The primary label for this object. This value is the internal label that doesn’t get
translated.

```
NamedCredentialId

NamespacePrefix

Notes

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the named credential that’s used for a request. The named
credential identifies the third-party system and the third-party authentication
settings.

This is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

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
textarea


### Standard Objects UserProvisioningLog

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**

A utility field for administrators to add any additional information about the
configuration. This field is for internal reference only, and is not used by any
process.

```
OnUpdateAttributes

ReconFilter

UserAccountMapping

### UserProvisioningLog

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the user attributes, as comma-separated values, that generate a
UserProvisioningRequest object during an update.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When collecting and analyzing users on a third-party system, the plug-in uses
this filter to limit the scope of the collection.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Stores the attributes used to link the Salesforce user to the account on the
third-party system, in JSON format.

For example:

```
  {"linkingSalesforceUserAttribute":"Username",

  "linkingTargetUserAttribute":"Email"}

```

Represents messages generated during the process of provisioning users for third-party applications. This object is available in API version
33.0 and later.


Standard Objects UserProvisioningLog

Some messages for this object are generated automatically by Salesforce, and others are created by the developers of the user provisioning
plugin. Developers can use this object to log messages from the flow associated with the user provisioning process or the Apex plugin
that calls the target system. Administrators can use this object as a log of all user provisioning activity and as a troubleshooting tool if
desired behavior is missing. This object is available as a custom report type.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Details

ExternalUserId

ExternalUsername

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value of this field depends on the log entry. For example, if the target system returns an
error, the error message may be recorded in this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username set in the target system for the associated user account.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.

**Type**
reference


Standard Objects UserProvisioningLog

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce ID of the Group or User who owns this object.

```
Status

UserId

UserProvisioningRequestId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the user provisioning request. Based on the context of the log, it can contain
different values, such as an HttpStatusCode.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the user making the request.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the user provisioning request.

This is a relationship field.

**Relationship Name**
UserProvisioningRequest

**Relationship Type**
Lookup

**Refers To**
UserProvisioningRequest


### Standard Objects UserProvisioningRequest UserProvisioningRequest

Represents an individual provisioning request to create, update, or delete a single user account in a third-party service system (or another
Salesforce organization). This object is available in API version 33.0 and later.

A UserProvisioningRequest (UPR) record is created for each provisioning action for each user, and for each connected app available to
the user. For example, if a user has two connected apps, and a provisioning request is sent to two different services to create an account
for the user, Salesforce creates two UPR objects. Provisioning actions include creating, updating, or deleting a user account.

Supported Calls

`create()`, `delete()`,
`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppName

ApprovalStatus

ConnectedAppId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique name of the connected app associated with the service provider.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the approval for the current request. If the user provisioning setup for the
connected app does not have an approval process enabled, the status is `Not Required` .
If an approval process is enabled, supported values are:

**•** `Required`  - An approval process is enabled in the user provisioning setup for the
associated connected app, but there is no response to the request yet.

**•** `Not Required`  - An approval process is not enabled in the user provisioning setup
for the associated connected app.

**•** `Approved`

**•** `Denied`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvisioningRequest

**Field** **Details**

**Description**

The 18-digit application ID for the connected app.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

```
ExternalUserId

ManagerId

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user in the target system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Salesforce ID of the user who manages the user specified in the `SalesforceUserId`
field. If an approval process is configured for the user provisioning request. this value allows
the manager to approve the request. Available in API version 34.0 and later.

This is a relationship field.

**Relationship Name**
Manager

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.


Standard Objects UserProvisioningRequest

**Field** **Details**

```
Operation

OwnerId

ParentID

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The Apex method called by the trigger associated with the provisioning request (typically a
change to the User object). Supported values are:

**•** `Create`

**•** `Read`

**•** `Update`

**•** `Deactivate`

**•** `Activate`

**•** `Freeze`

**•** `Unfreeze`

**•** `Reconcile`

**•** `Linking`

For example, when the User object field `isActive` is set to `false`, the UPR object
`Operation` field value is set to `Deactivate` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce ID of the Group or User who owns this object.

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
When a retry event is created, the failed UPR is cloned and resubmitted. This field contains
a lookup to the failed UPR that was cloned to create the current record.


Standard Objects UserProvisioningRequest

**Field** **Details**

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
UserProvisioningRequest

```
Retry Count

SalesforceUserId

ScheduleDate

State

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of retry attempts performed on a UPR. Retry Count enables custom business logic
such as “Retry 5 times then stop and notify your admin.”

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the user making the request.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
When to send this request to the service provider.

Note: Scheduling is not implemented yet. Currently, provisioning changes are queued
immediately to be sent to the service provider.

**Type**
picklist


Standard Objects UserProvisioningRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of this request. Supported values are:

**•** `New`

**•** `Requested`

**•** `Completed`

**•** `Failed`

**•** `Collecting`

**•** `Collected`

**•** `Analyzing`

**•** `Analyzed`

**•** `Committing`

**•** `Retried`

**•** `Manually Completed`

The `State` goes from `New` to `Requested` to `Completed` or `Failed`, unless a
reconciliation process is occurring. For details about the reconciliation process `State` value
changes, see Usage.

The `State` goes from `Failed` to `Retried` or `Manually Completed` when
troubleshooting UPR failures. For details about handling failures, see State Values for Managing
Provisioning Failures.

```
UserProvAccountId

UserProvConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID value of the associated UserProvAccount object.

This is a relationship field.

**Relationship Name**
UserProvAccount

**Relationship Type**
Lookup

**Refers To**
UserProvAccount

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvisioningRequest

**Field** **Details**

**Description**

The ID value of the associated UserProvisioningConfig object. Available in API version 34.0
and later.

This is a relationship field.

**Relationship Name**
UserProvConfig

**Relationship Type**
Lookup

**Refers To**
UserProvisioningConfig

Usage

The `State` value changes during a reconciliation process ( `Operation = Reconcile` ) to gather and compare users on the
third-party system to Salesforce users. Typically, when a UPR entry is first created, it has a `State` value of `New` . When a collection
process is triggered, the `State` transitions to `Collecting` until that process is finished and the `State` is `Collected` . When
an analyze process is triggered, the `State` transitions to `Analyzing` until that process is finished and the `State` is `Analyzed` .
If a process commits the request, the `State` then transitions to `Committing`, and the properties move from the
UserProvAccountStaging object to the UserProvAccount object. When those properties are saved in the UserProvAccount object, the
`State` transitions to `Completed` .

However, the `State` does not necessarily start at `New` . For example, UserProvAccountStaging entries can be inserted programmatically.
If a process is initiated that triggers linking these rows to accounts on the third-party service, a UPR entry could start with the `Analyzing`
`State` .

Also, the `State` cannot go backwards from an active task. For example, a successful `AnalyzingState` must progress to `Analyzed` ;
unless the active process fails, and then the `State` must change to `Failed` . Certain `State` transitions cannot be made
programmatically and must be triggered by Salesforce.

The following table shows the `State` transitions that can occur for each `State` value. Each row corresponds to a current `State`
value and each column corresponds to a new `State` after a potential transition.

**•**   - the transition to this value is not allowed.

**•**   - the transition to this value is allowed.

**•**   - only Salesforce can transition the `State` to this value.


### Standard Objects UserRecordAccess

State Values for Managing Provisioning Failures

The `state` value changes to `Failed` for several reasons, such as network outages, session timeouts, permissions issues, and record
locks. The `Failed` state can transition to either `Retried` or `Manually Completed` to indicate what action was taken to
address the failure. Actions can include correcting the root cause of the failure and requesting that the provisioning engine retry the
UPR. Or, it can be completing the action against the target manually. Each UPR is an independent transaction and it’s possible the retry
causes a failure with a different root cause. So it’s hard to distinguish failed events that you addressed from the ones that require more
action.

If you tried to correct the cause of the failure and requested the provisioning engine to retry the UPR, you can mark the failed UPR
`Retried` . Or, if the action against the target was completed manually, you can mark it `Manually Completed` .

When a retry event is created, the failed UPR is cloned, and resubmitted. The `ParentID` field contains a lookup to the failed UPR to
use to clone the new UPR. The `Retry Count` field contains the number of retry attempts that were performed on a UPR. With the
`Retry Count` field, you can add custom business logic like "Retry 5 times then stop and notify your admin."

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserProvisioningRequestOwnerSharingRule (API version 34.0)**
Sharing rules are available for the object.

**UserProvisioningRequestShare (API version 34.0)**
Sharing is available for the object.

### UserRecordAccess

Represents a user’s access to a set of records. This object is read only and is available in API version 24.0 and later. This object doesn’t
consider whether a user’s access is blocked by a restriction rule.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects UserRecordAccess

Fields

**Field** **Details**

```
HasAllAccess

HasDeleteAccess

HasEditAccess

HasTransferAccess

HasReadAccess

MaxAccessLevel

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user can share the record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has delete access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has edit access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has transfer access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has read access to the record ( `true` ) or not ( `false` ).

**Type**
picklist

**Properties**
Group, Nillable, Restricted picklist, Sort


Standard Objects UserRecordAccess

**Field** **Details**

**Description**
Indicates a user’s maximum level of access to a record.

Valid values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `Delete`

**•** `Transfer`

**•** `All`

```
RecordId

UserId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
ID of the record.

**Type**
reference

**Properties**
Filter, Group

**Description**
ID of the user.

Use this object to query a user’s access to records. You can only query records of objects listed on the Sharing Settings Setup page. You
can’t create, delete, or update any records using this object.

[Note: UserRecordAccess doesn’t consider whether a user’s access is blocked due to a restriction rule. If a user’s access is blocked](https://developer.salesforce.com/docs/atlas.en-us.260.0.restriction_rules.meta/restriction_rules/restriction_rules_about.htm)
even though query results state that they should have access, check to see if a restriction rule on the object prevents the user’s
access.

Up to 200 record IDs can be queried. You can include an `ORDER BY` clause for any field that is being selected in the query.

The following sample query returns the records, whether the queried user has read and transfer access to each record, and the user’s
maximum access level to each record.

```
SELECT RecordId, HasReadAccess, HasTransferAccess, MaxAccessLevel

   FROM UserRecordAccess

   WHERE UserId = [single ID]

   AND RecordId = [single ID] //or Record IN [list of IDs]

```


### Standard Objects UserRelatedRecordContent

The following query returns the records to which a queried user has read access.

```
   SELECT RecordId

      FROM UserRecordAccess

      WHERE UserId = [single ID]

      AND RecordId = [single ID] //or Record IN [list of IDs]

      AND HasReadAccess = true

```

Using API version 30.0 and later, UserRecordAccess is a foreign key on the records. You can’t filter by or provide the `UserId` or
`RecordId` fields when using this object as a lookup or foreign key. The previous sample queries can be run as:

```
   SELECT Id, Name, UserRecordAccess.HasReadAccess, UserRecordAccess.HasTransferAccess,

   UserRecordAccess.MaxAccessLevel

       FROM Account

   SELECT Id, Name, UserRecordAccess.HasReadAccess

       FROM Account

```

SOQL restrictions:

**•** When the running user is querying a user's access to a set of records, records that the running user doesn’t have read access to are
filtered out of the results.

**•** When filtering by `UserId` and `RecordId` only, you must use `SELECT RecordId` and optionally one or more of the access
level fields: `HasReadAccess`, `HasEditAccess`, `HasDeleteAccess`, `HasTransferAccess`, and `HasAllAccess` .
You can include `MaxAccessLevel` .

**•** When filtering by `UserId`, `RecordId`, and an access level field, you must use `SELECT RecordId` only.

SEE ALSO:

_Developer Guide_ [: Restriction Rules](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

### UserRelatedRecordContent

Represents the link between a managed content record, an account, event, or opportunity record, and a user record. This object is
reserved for future use.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContentOwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserRole

**Field** **Details**

**Description**
The user who owns the managed content record associated with the given account, event,
or opportunity record.

This field is a relationship field.

**Relationship Name**
ContentOwner

**Refers To**
### User

```
ManagedContentId

RelatedRecordId

### UserRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the managed content record created for the associated Salesforce record. One
unique managed content record is created per account, event, or opportunity record per
user.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Refers To**
ManagedContent

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Salesforce record (e.g., account, opportunity, or event) associated with the
managed content record.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Refers To**
Account, Event, Opportunity

Represents a user role in your organization.


Standard Objects UserRole

Note: This object was called “Role” in previous versions of the API documentation.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with the View Roles and Role Hierarchy permission can access this object, and only users with
the Manage Roles permission can edit this object.

Fields

**Field** **Details**

```
CaseAccessForAccountOwner

ContactAccessForAccountOwner

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The case access level for the account owner.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The contact access level for the account owner.

Note: When `DefaultContactAccess` is set to `Controlled`
`by Parent`, you can’t create or update this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org.
It must begin with a letter, not include spaces, not end with an underscore,
and not contain two consecutive underscores. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the


Standard Objects UserRole

**Field** **Details**

changes are reflected in a subscriber’s organization. Corresponds to **Role**
**Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one
for each record.

```
ForecastUserId

IsPartner

MayForecastManagerShare

Name

OpportunityAccessForAccountOwner

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the forecast manager associated with this role. Label is **User ID** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user role is a partner who has access to the partner
portal ( `true` ) or not ( `false` ). This field is not available for release 9.0 and
later. Instead, use `PortalType` with the value `Partner` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecast manager can manually share their own
forecast.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the role. Corresponds to **Label** on the user interface.

**Type**
picklist


Standard Objects UserRole

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The opportunity access level for the account owner. Note that you
can’t set a user role with an opportunity access less than that specified in
organization-wide defaults.

```
ParentRoleId

PortalAccountId

PortalAccountOwnerId

PortalRole

PortalType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent role.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account. This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account’s owner. This field is read-only.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The portal role: Executive, Manager, User, or PersonAccount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This value indicates the type of portal for the role:


### Standard Objects UserServicePresence

**Field** **Details**

**•** None: Salesforce application role.

**•** CustomerPortal: Customer portal role.

**•** Partner: partner portal role. The field `IsPartner` used in release 8.0
will map to this value.

This field replaces `IsPartner` beginning with release 9.0.

```
 RollupDescription

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the forecast rollup. Label is **Description** .

Use this object to query the set of currently configured user roles in your organization. Use it in your client application to obtain valid
UserRole IDs to use when querying or modifying a User record.

Users with the View Roles and Role Hierarchy permission can query or describe this object. If your client application logs in with the
“Manage Users” permission, it can query, create, update, or delete UserRole records.

Note: You can’t update any field for a portal role.

For example, the following code finds all roles that are not assigned to any users.

```
SELECT Id, Name, DeveloperName

FROM UserRole

WHERE Id NOT IN (SELECT UserRoleId

           FROM User

           WHERE UserRoleId !='000000000000000')

```

SEE ALSO:

Overview of Salesforce Objects and Fields

### UserServicePresence

Represents a presence user’s real-time presence status. This object is available in API version 32.0 and later.

Supported Calls

`delete()`, `query()`, `getDeleted()`, `getUpdated()`, `retrieve()`, `undelete()`


Standard Objects UserServicePresence

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AtCapacityDuration

AverageCapacity

ConfiguredCapacity

ConfiguredInterruptCapacity

IdleDuration

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is at full capacity. This field is updated when the agent’s capacity
changes, such as when the agent is assigned, declines, or closes a work item. Available in
API versions 34.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The user’s average capacity. This field is updated when the agent’s capacity changes, such
as when the agent is assigned, declines, or closes a work item. Available in API versions 34.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured primary capacity.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured interruptible capacity. Available in version 57.0 and later when
the Interruptible Capacity feature is enabled.

**Type**
int


Standard Objects UserServicePresence

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is idle. This field is updated when the agent’s capacity changes,
such as when the agent is assigned, declines, or closes a work item. Available in API versions
34.0 and later.

```
IsAway

IsCurrentState

Name

OwnerId

ServicePresenceStatusId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user’s status is `Away` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a presence status is the user’s current state. If `true`, the agent is in that
presence status. Available in API versions 34.0 and later.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the `UserServicePresence` entity. For external routing, allows
the entity to be used in the Streaming API to listen to events whenever a
`UserServicePresence` record is created, modified, or deleted.

**Type**
reference


Standard Objects UserServicePresence

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The ID of the presence status that’s associated with the presence user that’s specified by the
`UserId` .

```
StatusDuration

StatusEndDate

StatusStartDate

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

This field is a calculated field: StatusEndDate - StatusStartDate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date of the user service presence status. Available in API versions 34.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Omni-Channel user.


### Standard Objects UserSetupEntityAccess

Usage

Apex triggers aren’t supported with `UserServicePresence` .

In API version 41.0 or later, `UserServicePresence` records can be deleted programmatically. The Customize Application permission
is required.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserServicePresenceChangeEvent (API version 62.0)**
Change events are available for the object.

**UserServicePresenceOwnerSharingRule**

Sharing rules are available for the object.

**UserServicePresenceShare**

Sharing is available for the object.

### UserSetupEntityAccess

Represents the enabled custom permissions of the running user. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DeveloperName

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the custom permission in the API.

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserSetupEntityAccess

**Field** **Details**

**Description**
This field isn't used.

```
KeyPrefix

LastCacheUpdate

NamespacePrefix

SetupEntityId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first 3 characters of the `SetupEntityId` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of the running user's info.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that’s associated with the custom permission. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the custom permission assigned to the user.


### Standard Objects UserShare

Usage

API users without the View Setup and Configuration permission can use this object to check their assigned custom permissions.

### UserShare

Represents a sharing entry on a user record. This object is available in API version 26.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only standard users or users with the Customize Application permission can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
IsActive

RowCause

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the User has access to log in ( `true` ) or not ( `false` ).
You can modify a User's active status from the user interface or via the API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .


Standard Objects UserShare

**Field** **Details**

All other `RowCause` values are read-only. After the sharing entry is created, this
field can’t be edited.

Possible values include:

**•** `Manual` —The User or Group has access to the user record because a User with
“All” access manually shared the User with them.

**•** `Rule` —The User or Group has access to the user record via a User sharing rule.

**•** `GuestRule` —The User or Group has access via a User guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

```
UserAccessLevel

UserId

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the specified user. The specified user is
denoted by the `UserId` . The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s
default `UserAccessLevel` .

`UserAccessLevel` can be updated only if `RowCause` is set to `Manual`
`Sharing` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User being shared.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


### Standard Objects UserSharedFeature

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the User. This field can’t be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit User records owned by other users.

### UserSharedFeature

For internal use only.

### UserTeamMember

Represents a single User on the default opportunity team of another User.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** This object is available only in organizations that have enabled the team selling functionality.

**•** Customer Portal users can’t access this object.


Standard Objects UserTeamMember

Fields

**Field** **Details**

```
OpportunityAccessLevel

OwnerId

TeamMemberRole

UserId

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the team member has to opportunities for which the user has
added his or her default opportunity team. The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default access
level for opportunities.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default opportunity team. This field can’t be updated.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the User has added his or her
default opportunity team. The valid values are set by the organization’s administrator in the
Opportunity Team Roles picklist. Label is **Team Role** .

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default opportunity team. This field can’t
be updated.


### Standard Objects UserTerritory

Usage

If you attempt to create a record that matches an existing record, the create request updates any modified fields and returns the existing
record.

Users can set up their default opportunity team to include other users that typically work with them on opportunities.

SEE ALSO:

OpportunityTeamMember

### UserTerritory

Represents a User who has been assigned to a Territory.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** Only available if territory management has been enabled for your organization.

**•** As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with
the Manage Territories permission can edit this object.

Fields

**Field** **Details**

```
IsActive

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is active in the given territory ( `true` ), or inactive in the
given territory ( `false` ):

**•** Users who are active in a territory are explicitly assigned to the territory and can
have open opportunities, closed opportunities, or no opportunities associated
with that territory.

**•** Users who are inactive in a territory are not explicitly assigned to the territory, but
own an open or closed opportunity that is associated with the territory. For
example, a user may have been transferred out of a territory, but still own
opportunities in his or her old territory.

Until a user is deleted from a territory (not simply removed from the territory), the
record is not returned in a `getDeleted()` call.


### Standard Objects UniqueQueryEventLog

**Field** **Details**

```
 IsDeleted

TerritoryId

UserId

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the Territory to which the user has been assigned. This field is required when
creating a record in API version 20.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the user. This field is required when creating a record.

If a user is inactive in a territory, and the opportunities they own that are associated with the territory are all closed, the user is not returned
in the Territories related list on the User page in Setup. Regardless of whether the user is inactive or the opportunities are closed, the
user is returned in the Quotas related list.

SEE ALSO:

Territory

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem

### UniqueQueryEventLog

Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This object is available in API version 65.0 and later.


Standard Objects UniqueQueryEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

LoginKey

PlannerIdentifier

QueryIdentifier

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

The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string


Standard Objects UniqueQueryEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The text of the SOQL query run or the Id of the report or list view run.

```
QueryType

RequestIdentifier

SessionKey

SqlIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The input type to the optimizer that was translated.

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
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier generated for the database query. (Its SQL Id in the ELF);

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.


### Standard Objects UserTerritory2Association UserTerritory2Association

Represents an association (by assignment) between a territory and a user record. Available only if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users based on your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

Note: UserTerritory2Association doesn’t support adding custom fields.

**Field Name** **Details**

```
IsActive

RoleInTerritory2

Territory2Id

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is active ( `true` ) or inactive ( `false` ) in the given
territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The role of the user in a territory. Possible values are: Owner, Administrator, Sales
Rep. Label is `Role in Territory` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the user is assigned to.


### Standard Objects UserTerritory2AssocLog

**Field Name** **Details**

```
UserId

### UserTerritory2AssocLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user who is assigned to the territory.

Represents a log of when a user is assigned and unassigned from a territory. This object is available in API version 57.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

To see this object, enable Sales Territory and User Tracking on the Territory Settings page. Activate a territory model to start the tracking.

Fields

**Field** **Details**

```
CurrencyIsoCode

EndDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of currency.

Possible values are:

**•** `EUR` —Euro

**•** `INR` —Indian Rupee

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects UserTerritory2AssocLog

**Field** **Details**

**Description**
Date when the user is unassigned from a territory. If the end date is empty, the user is still
assigned.

```
Name

RoleInTerritory2

StartDate

Territory2Id

Territory2ModelId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Auto-generated unique name of the log.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s role in the territory between the start and end date. The picklist is, by default, empty.
Add values to this field using Object Manager.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the user is assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the territory associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

**Type**
reference


### Standard Objects UserUIPreference

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory model associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model

```
UserId

### UserUIPreference

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user associated with the log.

This field is a relationship field.

**Relationship Name**
### User

**Refers To**
### User

Represents user preferences for Salesforce components. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
AsyncOperationTrackers

```

**Type**
textarea


Standard Objects UserUIPreference

**Field** **Details**

**Properties**
Create, Update

**Description**
Stores a JSON object that maps each quote ID to its asynchronous sales transaction request
details, which includes a tracker ID and the start date. This field is available with Revenue
Cloud in API version 66.0 and later.

```
Name

ObjectScope

PreferenceAttribute

SourceScope

UserId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-generated number for the user preferences. Read-only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the object that the preference applies to. For example, the preference
applies to the Quote object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type of preference.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the component, feature, or product that the preference is for. For example, a
preference for column widths that's associated with the Transaction Line Table component
in Revenue Cloud.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserWorkList

**Field** **Details**

**Description**
The user associated with the user preferences.

This field is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Master-detail

**Refers To**
User (the master object)

```
Value

### UserWorkList

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The JSON for the user's preferences.

Represents a list of work items in the My List tab for Sales Engagement users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsActive

ListType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the work list is active or not.

**Type**
picklist


### Standard Objects UserWorkListItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of list, such as a call or email.

```
 Name

 OwnerId

### UserWorkListItem

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work list.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the list.

Represents an individual work item in the My List tab for Sales Engagement users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
PriorityOrder

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order of the item in the list.


### Standard Objects VendorCallCenterStatusMap

**Field** **Details**

```
RelatedRecordId

UserWorkListId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the related record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related work list.

### VendorCallCenterStatusMap

Stores a mapping between a call center vendor agent status and a Salesforce presence status for an associated call center. This object
is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Omni-Channel and Service Cloud Voice must be enabled.

Fields

**Field** **Details**

```
CallCenterId

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


### Standard Objects VerificationHistory

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CallCenter

```
ExternalStatus

ServicePresenceStatusId

### VerificationHistory

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Status value to set for the call center vendor agent.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a presence status that can be assigned to a service channel.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

Represents the past six months of your org users’ attempts to verify their identity. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Only users with Manage Users permission can access this object.


Standard Objects VerificationHistory

Fields

**Field Name** **Details**

```
Activity

EventGroup

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action the user attempted that requires identity verification. The label is User
Activity. Available values are:

**•** `AccessReports` —The user attempted to access reports or dashboards.

**•** `Apex` —The user attempted to access a Salesforce resource with a verification
Apex method.

**•** `ChangeEmail` —The user attempted to change an email address.

**•** `ConnectSms` —The user attempted to connect a phone number.

**•** `ConnectToopher` —The user attempted to connect Salesforce
Authenticator.

**•** `ConnectTotp` —The user attempted to connect a one-time password
generator.

**•** `ConnectU2F` —The user attempted to register a U2F security key.

**•** `ConnectWebAuth` —The user attempted to register a built-in
authenticator.

**•** `ConnectedApp` —The user attempted to access a connected app.

**•** `EnableLL` —The user attempted to enroll in Lightning Login.

**•** `ExportPrintReports` —The user attempted to export or print reports
or dashboards.

**•** `ExternalClientApp`  - The user attempted to access an external client
app.

**•** `ExtraVerification` —Reserved for future use.

**•** `ListView` —The user attempted to access a list view.

**•** `Login` —The user attempted to log in.

**•** `Registration` —Reserved for future use.

**•** `TempCode` —The user attempted to generate a temporary verification code.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
ID of the verification attempt. Verification can involve several attempts and use
different verification methods. For example, in a user’s session, a user enters an
invalid verification code (first attempt). The user then enters the correct code and


Standard Objects VerificationHistory

**Field Name** **Details**

successfully verifies identity (second attempt). Both attempts are part of a single
verification and, therefore, have the same ID. The label is Verification Attempt.

```
LoginGeoId

LoginHistoryId

Policy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
successful or unsuccessful identity verification attempt. Due to the nature of
geolocation technology, the accuracy of geolocation fields (for example, country,
city, postal code) can vary.

This is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

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
