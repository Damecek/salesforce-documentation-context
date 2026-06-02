For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

```
USER_ID_DERIVED

VIEW_MODE

WAVE_SESSION_ID

WAVE_TIMESTAMP

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Wave Performance Event Type

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The view mode for the CRM Analytics asset. Possible values
include `view`, `edit`, `present`, `json`, or `print` .

**Type**
String

**Description**
The ID of a particular session of CRM Analytics. Use this field
to determine which log lines originated from a particular
session.

**Type**
Number

**Description**
The time at which this log line was generated.

Wave Performance events help you track trends in your Analytics performance.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

CPU_TIME

EPT

EVENT_TYPE

IS_INITIAL

LOGIN_KEY

NAME

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
The experienced page time in milliseconds.

**Type**
String

**Description**
The type of event. The value is always `WavePerformance` .

**Type**
Boolean

**Description**
Indicates whether the event is for the initial load of dashboard
( `true` ) or not ( `false` ).

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
The asset title or query string.


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

QUERY_ID

RECORD_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TAB_ID

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
This field is deprecated in API version 50.0. The number of
queries can be determined using the Uri Event type logs,
referenced here on page 2426

**Type**
String

**Description**
The Salesforce ID of the CRM Analytics object.

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
The ID of the particular Analytics tab in the user interface.


Standard Objects EventLogFile Supported Event Types

**Example**
dashboard-0FKB0000000Ec64GDK

```
TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

URI_ID_DERIVED

USER_ID

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

**Type**
String

**Description**
The CRM Analytics object type. This field is scheduled for
deprecation in v59.0. Use the new `IS_INITIAL` field to
determine the log line type.

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


### Standard Objects EventRelation

```
USER_ID_DERIVED

VIEW_MODE

WAVE_SESSION_ID

WAVE_TIMESTAMP

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

### EventRelation

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The view mode for the CRM Analytics asset. Possible values
include `view`, `edit`, `present`, `json`, or `print` .

**Type**
String

**Description**
The ID of a particular session of CRM Analytics. Use this field
to determine which log lines originated from a particular
session.

**Type**
Number

**Description**
The time at which this log line was generated.

Represents a person (a user, lead, or contact) or a resource (such as a conference room) invited to an event. This object lets you add or
remove invitees from an event and use the API to manage invitees’ responses to invitations. If Shared Activities is enabled, EventRelation
can also represent other objects that are related to an event. EventRelation does not support triggers, workflow, or data validation rules.

### EventRelation allows a variable number of relationships and handles deleted events differently, depending on whether Shared Activities

is enabled.

A non-recurring event can have up to 1,000 invitees. A recurring event can have up to 100 invitees.

**If Shared Activities Isn’t Enabled**

### • EventRelation records only represent invitees (contacts, users, and resources).

**•** An event can be related to one contact or lead.


Standard Objects EventRelation

**If Shared Activities Is Enabled**

**•** EventRelation records can represent:

**–** Invitees ( `IsInvitee=` is set to `true` )

OR

**–** Related contacts or lead ( `IsParent` is set to `true` )

**•** An event can be related to up to 50 contacts or one lead. These people may or may not be invitees. The number of allowed
invitees is not affected by the number of related contacts. If a contact or lead is also an invitee, there is one EventRelation record
for that person with `IsInvitee` and `IsParent` are set to `true` .

**•** An event can be related to a lead, contact, resource, account, or opportunity.

**•** An event can be related to a custom object that has the `HasActivities` attribute set to `true` .

**•** If you delete an event, then relations between the event and any specified contacts, leads, and other records are also deleted.

**•** If you delete the EventRelation record representing a relation then the corresponding relation field may be cleared on the event.

**•** If you delete the EventRelation record representing the `WhoId` on an event, then another Who, if any, from the event’s
`EventWhoIds` field will be promoted to the `WhoId` .

**•** If you restore a deleted event, relations between the event and any specified contacts, leads, and records are also restored. The
`WhoId`, `WhatId`, and `AccountId` field values are recalculated using the field values on EventRelation.

Whether or not Shared Activities is enabled, an event can be related to one other kind of record, such as an account, an opportunity, or
a custom object.

Note:

**•** With API versions 26.0 and later, the EventRelation object replaces the EventAttendee object, and the EventAttendee object
is no longer visible. You can still query the EventAttendee object using packages that support API versions 25.0 and earlier, or
by using Apex.

**•** An EventRelation object can’t be created for a child event.

**•** EventRelation includes deactivated users.

**•** In API versions 25.0 and earlier, you can’t use `query()`, `delete()`, or `update()` with events related to more than one
contact.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EventRelation

**Field** **Details**

**Description**
Contains the Account ID of the relation. For information on IDs, see ID Field Type.
`AccountId` is visible when Shared Activities is enabled.

```
EventId

IsDeleted

IsInvitee

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Contains the ID of the event. This value can’t be changed after it’s been specified.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is `Deleted` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the relation is an invitee.

**•** `IsInvitee` is visible while Shared Activities is being enabled, after it has been
enabled, and while it is being disabled.

**•** `IsInvitee` defaults to `true` while Shared Activities is being enabled, after
it has been enabled, and while it is being disabled if `IsInvitee`, `IsParent`,
and `IsWhat` are not set. This configuration ensures compatibility when Shared
Activities isn’t enabled and EventRelation represents event invitees only.

**•** `IsInvitee` defaults to `false` when Shared Activities is enabled if
`IsParent` is set to `true` .


Standard Objects EventRelation

**Field** **Details**

```
IsParent

IsWhat

RelationId

RespondedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
`IsParent` is visible only when Shared Activities is enabled. When `false`, indicates
that the relation is an invitee (a contact, lead, or user). When `true`, indicates that
the relation is a Who or What, as determined by `IsWhat` field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
`IsWhat` is visible only when Shared Activities is enabled. The value is relevant only
if `IsParent` is `true` . When `IsWhat` is `true`, the relation specified by
`RelationId` is a What (an account, opportunity, custom object, etc.). When
`IsWhat` is `false`, the relation specified by `RelationId` is a Who (a contact,
lead, or user).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Contains the ID of the person (User, Contact, or Lead) or the resource invited to an
event. When Shared Activities is enabled, `RelationId` can also contain the ID of
an account, opportunity, or other object related to an event.

This value can’t be changed after it’s been specified.

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
Create, Filter, Nillable, Sort, Update


Standard Objects EventRelation

**Field** **Details**

**Description**
Indicates the most recent date and time when the invitee responded to an invitation
to an event.

```
Response

Status

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains optional text that the invitee can enter when responding to an invitation
to an event.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the invitee status with one of the following values:

**•** `New` : Invitee has received the invitation but hasn’t yet responded. This value is
the default.

**•** `Declined` : Invitee has declined the invitation.

**•** `Accepted` : Invitee has accepted the invitation.

Note: `Uninvited` and `Maybe` aren’t currently supported.

**•** Invitee related lists display slightly different content. In the Salesforce mobile app, the invitee related list includes invitees only,
whereas in the full site, it also includes the event owner. To reproduce the full site functionality in the Salesforce mobile app, use the
following API queries.

If you use Shared Activities in your Salesforce org, use this query:

```
  SELECT RelationId FROM EventRelation WHERE isInvitee = true AND eventId='[Event_Id]'

```

where _`Event_Id`_ is the child event’s ID.

If you don’t use Shared Activities, use this query:

```
  SELECT RelationId FROM EventRelation WHERE eventId='[Event_Id]'

```

These queries get the main event’s relations and display them for the given child event. To further filter the results, add a `WHERE`
clause.


Standard Objects EventRelation

**Assigning resource attendance status**
You can add a resource to an event only when the resource is available. The only attendance status that can be assigned to resources
is Accepted. Events can’t be saved when resources you’ve added aren’t available.

**Create an invitee if Shared Activities is enabled (or during the process of enabling it or rolling back)**
If the invitee is already a contact or lead, update `IsInvitee` to `true` .

If the invitee is not already a contact or lead, create an EventRelation object for the invitee with `IsInvitee` set to `true` .

**Create an invitee if Shared Activities is not enabled**
Create an EventRelation object for the invitee.

**Insert a contact or lead relation**

```
     EventRelation er = new EventRelation(EventId = '00UD0000005zijH',

       RelationId = '003D000000Q8aeV', isParent = true, isInvitee = false);

     insert er;

```

**Determine what events a given invitee is attending**
To determine all the events that a particular person is attending during a given time period (for example, next week), you can have
a client application query the Event object for a given date range, iterate through the results, and, for each event, query the
EventRelation object to determine whether the particular person ( `RelationId` ) has accepted an invitation to that event.

**Insert an invitee relation**

If `isParent`, `isWhat` and `IsInvitee` are not set, and `RelationId` is a contact, lead, user, or calendar, `IsInvitee`
defaults to `true` . This means if an EventRelation isn’t specifically inserted as a relation to a contact or lead, it’s treated as an Invitee
relation by default.

```
     EventRelation er = new EventRelation(EventId = '00UD0000005zijH',

       RelationId = '003D000000Q8adV');

     insert er;

```

**Query relations to a contact or a lead**

```
     List<EventRelation> whoRelations = [SELECT Id, Relation.Name FROM

       EventRelation WHERE EventId = '00UD0000005zijD' AND isParent = true AND isWhat =

     false];

```

**Query invitee relations**

```
     List<EventRelation> inviteeRelations = [SELECT Id, Relation.Name FROM

       EventRelation WHERE EventId = '00UD0000005zijD' AND isInvitee = true];

```

**Update an invitee relation to a contact or lead invitee relation**

```
     EventRelation er = [SELECT Id FROM EventRelation WHERE EventId =

       '00UD0000005zijD' AND isInvitee = true and isParent = false LIMIT 1];

     er.isParent = true;

     update er;

```

**Update a contact or lead relation to a contact or lead invitee relation**

```
     EventRelation er = [SELECT Id FROM EventRelation WHERE EventId =

       '00UD0000005zijD' AND isParent = true and isInvitee = false LIMIT 1];

     er.isInvitee = true;

     update er;

```


### Standard Objects EventBusSubscriber

**Reproduce invitee related list functionality in the Salesforce mobile app**
Invitee related lists display slightly different content in the Salesforce mobile app and the full site. In the app, the invitee related list
includes invitees only, whereas in the full site, it also includes the event owner.

If you use Shared Activities in your Salesforce org, use the following query to reproduce the full site functionality in the Salesforce
mobile app:

```
     SELECT RelationId FROM EventRelation WHERE isInvitee = true AND eventId='[Event_Id]'

```

where _`Event_Id`_ is the child event’s ID.

If you don’t use Shared Activities, use this query:

```
     SELECT RelationId FROM EventRelation WHERE eventId='[Event_Id]'

```

These queries get the main event’s relations and display them for the given child event. To further filter the results, add a `WHERE`
clause.

**Send email notifications**
To send email notifications for a given event, query EventRelation for the event, iterate through the list, examine the status, and send
email notifications to every person who accepted the invitation.

**Syncing Events with Lightning Sync**
Attendee statuses (Accepted or Maybe, Declined, or No Response) sync from Microsoft [®] Exchange or Google to Salesforce, but not
from Salesforce to Exchange or Google. Be wary of creating API flows that update attendee status in Salesforce for users set up to
sync both ways. Eventually the original Exchange or Google status overrides the update made in Salesforce.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EventRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

### Event

EventWhoRelation

Overview of Salesforce Objects and Fields

### EventBusSubscriber

Represents a trigger, process, or flow that’s subscribed to a platform event or a change data capture event. Doesn’t include CometD or
Pub/Sub API subscribers.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects EventBusSubscriber

Special Access Rules

EventBusSubscriber is read only and can only be queried. As of Summer ’20 and later, only your Salesforce org's internal users can access
this object.

Fields

**Field** **Details**

```
ExternalId

IsPartitioned

LastError

LastProcessed

LastPublished

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the subscriber. For example, the trigger ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the platform event Apex trigger is configured with parallel subscriptions
( `true` ) or not ( `false` ). The default value is `false` [. See Platform Event Processing at Scale](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_ps.htm)
[with Parallel Subscriptions for Apex Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_ps.htm) _Platform Events Developer Guide_ .

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message that the last thrown `EventBus.RetryableException` contains.
This field applies to Apex triggers only. Available in API version 43.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last event that the subscriber processed. This field replaces `Position`
as of API level 66.0.

**Type**
string


Standard Objects EventBusSubscriber

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last published event. This field replaces `Tip` as of API level 66.0.

Note: For high-volume platform events and change events, the value for Tip isn’t
available and is always -1.

```
Name

Position

Retries

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subscribed item, such as the trigger or process name. If the subscribed
item’s name is “Process”, at least one flow Pause element is subscribed to the event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last event that the subscriber processed. This field has been deprecated
as of API level 66.0 and should no longer be used. Use `LastProcessed` instead. This
field may not be properly represented if the value exceeds the maximum integer size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the trigger was retried due to throwing the
`EventBus.RetryableException` . This field applies to Apex triggers only. Available
in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the subscriber. Can be one of these values:

**•** `Error`  - The subscriber was disconnected and stopped receiving published events.
A trigger reaches this state when it exceeds the number of maximum retries with the
`EventBus.RetryableException` . Trigger assertion failures and unhandled


Standard Objects EventBusSubscriber

**Field** **Details**

exceptions don’t cause the error state. We recommend limiting the retries to fewer than
nine times to avoid reaching this state. When you fix and save the trigger, or for a
managed package trigger, if you redeploy the package, the trigger resumes automatically
from the tip, starting from new events. Also, you can resume a trigger subscription in
the subscription detail page that you access from the platform event page.

**•** `Repartitioning` —The system is in the process of modifying the trigger's parallel
subscription configuration.

**•** `Running` —The subscriber is actively listening to events. If you modify the subscriber,
the subscription continues to process events.

**•** `Suspended` —The subscriber is disconnected and can’t receive events because a
Salesforce admin suspended it or due to an internal error. You can resume a trigger
subscription in the subscription detail page that you access from the platform event
page. To resume a process, deactivate it and then reactivate it. If you modify the
subscriber, the subscription resumes automatically from the tip, starting from new events.

[For more information, see View and Manage an Event’s Subscribers on the Platform Event’s](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm)
[Detail Page in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm) _Platform Events Developer Guide_ .

```
Tip

Topic

Type

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last published event. This field has been deprecated as of API level 66.0
and should no longer be used. Use `LastPublished` instead. This field may not be
properly represented if the value exceeds the maximum integer size.

Note: For high-volume platform events and change events, the value for Tip isn’t
available and is always -1.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subscription channel that corresponds to a platform event or change event.
For a platform event, the topic name is the event name appended with `__e`, such as
`MyEvent__e` . For a change event, the topic is the name of the change event, such as
`AccountChangeEvent` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EventRelayConfig

**Field** **Details**

**Description**
The subscriber type ( `ApexTrigger` ). If the subscriber is a process or flow Pause element,
the type is blank.

Usage

Use EventBusSubscriber to query details about subscribers to a platform event. You can get all subscribers for a particular event by
filtering on the `Topic` field, as follows.

```
   SELECT ExternalId, Name, Position, Status, Tip, Type

   FROM EventBusSubscriber

   WHERE Topic='Low_Ink__e'

### EventRelayConfig

```

Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon
EventBridge. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** To retrieve or query this object, you must have the View Setup and Configuration permission.

**•** [This object is read-only. To configure an event relay, use EventRelayConfig in Tooling API or EventRelayConfig in Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_eventrelayconfig.htm)

Fields

**Field** **Details**

```
DestinationResourceName

DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the named credential, which stores the AWS account information.
The `destinationResourceName` value contains the `callout:` prefix. For example:

```
  callout:MyRelayNamedCredential

```

**Type**
string


Standard Objects EventRelayConfig

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Record Type Name** . This field is
automatically generated, but you can supply your own value if you create the record using
the API.

```
EventChannel

Language

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The full name of the event channel used in the event relay. For example:

```
  MyRelayChannel__chn

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the EventRelayConfig.

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


Standard Objects EventRelayConfig

**Field** **Details**

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

NamespacePrefix

RelayOption

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the EventRelayConfig. In the UI, this field is Event Relay Config.

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
textarea

**Properties**
Nillable

**Description**
A JSON-encoded string that contains an option for resuming an event relay after the system
recovers from an error. This option is used if the event relay can't resume after the last relayed
event. The options available are:

**•** `"{\"ReplayRecovery\":\"LATEST\"}"` —(Default) Start relaying events
from new events received in the event bus. Use this option if you aren’t interested in
missed events while the relay was down.


### Standard Objects EventRelayFeedback

**Field** **Details**

**•** `"{\"ReplayRecovery\":\"EARLIEST\"}"` —Resend all events stored in
the event bus and relay new events thereafter. The event bus stores events for up to
three days. Use this option if you want to reprocess all stored events and catch up on
missed events.

```
State

UsageType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The execution state of the event relay. Possible values are:

**•** `RUN` —The event relay is running and actively relaying event messages from Salesforce
to Amazon EventBridge.

**•** `PAUSE` —An administrator paused the event relay. No events are relayed to Amazon
EventBridge during this status. All current state information is saved.

**•** `STOP` —(Default) The event relay is stopped and no events are relayed to Amazon
EventBridge. All current state information is deleted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

### EventRelayFeedback

Represents execution state information about an event relay from Salesforce to Amazon EventBridge for platform events and change
data capture events. Query this object to get information such as the event relay status and any error message. This object is available
in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ErrorCode

```

**Type**
string


Standard Objects EventRelayFeedback

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code of the last error that occurred during the relay of event messages. For a list
of possible error codes and messages, see Error Codes.

```
ErrorIdentifier

ErrorMessage

ErrorTime

EventRelayConfigId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier of an unexpected system error that occurred during the relay of event messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The error message of the last error that occurred during the relay of event messages. For a
list of possible error codes and messages, see Error Codes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last error occurred during the relay of
event messages.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the event relay configuration that this feedback record is collecting the execution
information of.

This field is a relationship field.

**Relationship Name**
EventRelayConfig

**Relationship Type**
Lookup


Standard Objects EventRelayFeedback

**Field** **Details**

**Refers To**
EventRelayConfig

```
EventRelayNumber

LastRelayedEventTime

RemoteResource

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that identifies the EventRelayFeedback record. This field is of type Auto Number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last event was relayed to Amazon
EventBridge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the partner event source associated with the event relay. It is in the format
`aws.partner/salesforce.com/` _**`orgID`**_ `/` _**`channelID`**_ . For example:
`aws.partner/salesforce.com/00DRM000000Fxts2AC/0YLRM0000004Dfg4AE` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the event relay.

Possible values are:

**•** `ERROR`  - The event relay encountered an error while running or during a state change
that the administrator initiates. During the `ERROR` state, no events are relayed to Amazon
EventBridge. The system attempts periodically to recover from the error. If it succeeds,
the `Status` field value changes to `RUNNING` or to the new state that the administrator
selected. The event relay attempts to resume sending events from the event bus from
where it left off. In rare occasions, if it can't resume after the last relayed event, it uses
the error recovery option in the `relayOption` field of EventRelayConfig to determine
where to resume from.


### Standard Objects EventStagedInviteeEmail

**Field** **Details**

**•** `DELETED` —Reserved for future use.

**•** `PAUSED`                   - An administrator paused the event relay. No events are relayed to Amazon
EventBridge during this status. When an administrator resumes the event relay, events
are relayed from the last position in the event bus, as long as they're within the retention
window.

**•** `RUNNING`                   - The event relay is running and actively relaying events from Salesforce to
Amazon EventBridge.

**•** `STOPPED` —The event relay is stopped and no events are relayed to Amazon
EventBridge. Some state information stored in EventRelayFeedback fields is deleted, such
as `LastRelayedEventTime` and error fields. When the event relay is resumed,
only new events are relayed.

The default value is `STOPPED` .

```
UsageType

```

Error Codes

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

This table contains the error codes and messages that a query on EventRelayFeedback can return in the `ErrorCode` and
`ErrorMessage` fields.

### EventStagedInviteeEmail

Represents the relationship between an event and an email address invited to the event that doesn’t match to a user, contact, or lead
record. Data about the unmatched email address is represented in StagedInviteeEmail. This object represents event-related details, such
as the invitee's attendance response to the event. This object is available in API version 66.0 and later.


Standard Objects EventStagedInviteeEmail

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on.

Fields

**Field** **Details**

```
EventId

IsArchived

IsOrganizer

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related event record.

This field is a relationship field.

**Relationship Name**
Event

**Refers To**
Event

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is archived ( `true` ) or not ( `false` ). This value helps manage
high volumes of archived events, improving query performance.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the invitee is the event organizer ( `true` ) or not ( `false` ).


### Standard Objects EventTag

**Field** **Details**

The default value is `false` .

```
Name

StagedInviteeEmailId

Status

### EventTag

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The invited email address.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related invitee email address record.

This field is a relationship field.

**Relationship Name**
StagedInviteeEmail

**Relationship Type**
Master-detail

**Refers To**
StagedInviteeEmail

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The attendance response to the event from the invitee.

Possible values are:

**•** `Accepted`

**•** `Declined`

**•** `Maybe`

**•** `New`

**•** `Uninvited`

Associates a word or short phrase with an Event.


Standard Objects EventTag

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


### Standard Objects EventWhoRelation

Usage

EventTag stores the relationship between its parent TagDefinition and the Event being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### EventWhoRelation

Represents the relationship between an event and a lead or contacts. This derived object is a filtered version of the EventRelation on
page 2454 object; that is, IsParent is _`true`_ and IsWhat is _`false`_ . It doesn’t represent relationships to invitees or to accounts, opportunities,
or other objects. This object is available in API versions 29.0 and later.

### EventWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared

Activities for your organization.

Note: EventWhoRelation objects aren’t created for child events.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

RelationId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Expense

**Field Name** **Details**

**Description**
Indicates whether the person related to the event is a contact or lead.

Usage

**Apex example that queries relations to a contact or lead**

```
     List<EventWhoRelation> whoRelations = [SELECT Id, Relation.Name FROM

     EventWhoRelation WHERE EventId = '00UD0000005zijD'];

```

SEE ALSO:

Event

EventRelation

### Expense

Represents an expense linked to a work order. Service resource technicians can log expenses, such as tools or travel costs. This object is
available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

Amount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the account associated with the linked work order.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The amount of the expense.


Standard Objects Expense

**Field** **Details**

```
CurrencyIsoCode

Description

Discount

ExpenseEndDate

ExpenseNumber

ExpenseStartDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage deducted from the `Subtotal` price. Available in version 51.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the expense was incurred over multiple days, the Expense End Date is the last day that the
expense covers.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that uniquely identifies the expense.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Expense

**Field** **Details**

**Description**
If the expense was incurred over multiple days, the Expense Start Date is the first day that
the expense covers.

```
ExpenseType

LastReferencedDate

LastViewedDate

OwnerId

Quantity

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of expense. Possible values are:

**•** `Billable`

**•** `Non-Billable`

The default value is `Billable` .

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

**Description**
The ID of the user who owns the expense record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Expense

**Field** **Details**

**Description**
The number of items purchased in this record. Available in version 51.0 and later.

```
Subtotal

Title

TotalPrice

TransactionDate

UnitPrice

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The subtotal price calculated as the product of `Quantity` and `UnitPrice` . Available
in version 51.0 and later.

This is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price of the transaction which is equal to the discounted subtotal: `Subtotal`   ( `Discount`    - `Subtotal` ). Available in version 51.0 and later.

This is a calculated field.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The day that the expense was incurred, or the payment date for the expense.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects ExpenseReport

**Field** **Details**

**Description**
The price of one item on the record. Available in version 51.0 and later.

```
WorkOrderId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work order associated with the expense.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseChangeEvent (API version 55.0)**
Change events are available for the object.

**ExpenseFeed**

Feed tracking is available for the object.

**ExpenseHistory**

History is available for tracked fields of the object.

**ExpenseOwnerSharingRule**

Sharing rules are available for the object.

**ExpenseShare**

Sharing is available for the object.

### ExpenseReport

Represents a report that summarizes expenses. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist


Standard Objects ExpenseReport

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

```
Description

ExpenseReportNumber

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report.

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

**Description**
The ID of the user who owns the expense report record.


### Standard Objects ExpenseReportEntry

**Field** **Details**

```
Title

TotalExpenseAmount

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense report.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all expense entries in the report.

This is a calculated field.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportFeed**

Feed tracking is available for the object.

**ExpenseReportHistory**

History is available for tracked fields of the object.

**ExpenseReportShare**

Sharing is available for the object.

### ExpenseReportEntry

Represents an entry in an expense report. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Amount

```

**Type**
currency


Standard Objects ExpenseReportEntry

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the expense.

```
CurrencyIsoCode

ExpenseId

ExpenseReportEntryNumber

ExpenseReportId

ExpenseType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The expense that corresponds to the expense report entry.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The expense report that’s associated with the expense report entry.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The type of expense. Possible values are:

**•** `Billable`


Standard Objects ExpenseReportEntry

**Field** **Details**

**•** `Non-Billable`

The default value is `Billable` .

```
LastReferencedDate

LastViewedDate

Title

TransactionDate

```

Associated Objects

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
Filter, Group, Nillable, Sort

**Description**
A title that identifies the expense.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The day that the expense was incurred, or the payment date for the expense.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportEntryFeed**

Feed tracking is available for the object.

**ExpenseReportEntryHistory**

History is available for tracked fields of the object.


### Standard Objects ExpressionFilter ExpressionFilter

Represents a logical expression that’s used to control the execution of macro instructions. This object is available in API version 46.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContextId

FilterConditionLogic

FilterDescription

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the MacroInstruction object that contains the expression.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The filter conditions to use and the order in which to apply them. For example, ‘1
AND 2’ evaluates condition 1 and then condition 2.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. A description of the filter expression that helps to explain the logic to users. For
example, ‘Applies to New cases.’

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the expression.


### Standard Objects ExpressionFilterCriteria

Usage

The ExpressionFilter object is used with the `IF` and `ELSEIF` operations in a MacroInstruction. It lets you specify a logical expression
that determines whether macro instructions are executed. The object indicates whether any or all conditions must be true.

To represent the conditions that are evaluated, this object uses one or more ExpressionFilterCriteria child objects. The ExpressionFilter
to be used with each criteria is specified in the ExpressionFilterCriteria’s ExpressionFilterId field.

For example, to represent the following conditional statement, the ExpressionFilter object specifies the `FilterConditionLogic`
field as `1 AND 2`, where 1 and 2 are ExpressionFilterCriteria objects. In this example, condition 1 is `Case.Status EQUALS New`,
and condition 2 is `Case.Origin EQUALS Phone` .

```
   IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)

       Select Email QuickAction

       Set Subject…

       Set To…

       Set Body…

       Submit

   ENDIF

### ExpressionFilterCriteria

```

Represents a condition in an expression that’s used to control the execution of macro instructions. This object is available in API version
46.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ExpressionFilterId

FilterTarget

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the ExpressionFilter object that references this condition.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ExpressionFilterCriteria

**Field** **Details**

**Description**
Required. The target object or field used in the condition. For example, to create a condition
that applies to new cases, use `Case.Status` as the `FilterTarget` .

```
FilterTargetValue

Name

Operation

SortOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The value that’s compared to the value of the FilterTarget. For example, to create
a condition that applies to new cases, use `New` as the `FilterTargetValue` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the condition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the operator used to compare the target field and the target value. For
example, to create a condition that applies to new cases, use EQUALS for the `Operation`
field, as in `Case.Status EQUALS New` .

**•** `EQUALS`

**•** `NOTEQUALS`

**•** `CONTAINS`

**•** `NOTCONTAIN`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The order in which the criteria are evaluated.


### Standard Objects ExpressionSetConstraintObj

Usage

ExpressionFilterCriteria is a child object of the ExpressionFilter object. Use these objects with the `IF` and `ELSEIF` operations in a
MacroInstruction to control instruction execution. Each condition in a ExpressionFilterCriteria compares a target object or field to a value
using a condition operator; for example, `Case.Status EQUALS New` .

### ExpressionSetConstraintObj

Represents the association between a Product object and the constraint model tags defined in a given constraint model. This object is
available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.

Fields

**Field** **Details**

```
ConstraintModelTag

ConstraintModelTagType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The product tag that is defined in the constraint model, for example, `Laptop` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the product tag that is defined in the constraint model.

Possible values are:

**•** `Port`

**•** `Type`

The default value is `Type` .


Standard Objects ExpressionSetConstraintObj

**Field** **Details**

```
ExpressionSetId

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The expression set associated with the expression set constraint object.

This field is a relationship field.

**Relationship Name**
ExpressionSet

**Refers To**
ExpressionSet

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
the user accessed this record or list view (LastReferencedDate) but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the expression set constraint.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For internal use only.


### Standard Objects ExtConvParticipantIntegDef

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
ReferenceObjectId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The object associated with the expression set constraint object.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Refers To**
Product2, ProductClassification, ProductRelatedComponent

### ExtConvParticipantIntegDef

Represents the integration configuration for external conversation participants, used for communication between Salesforce and external
messaging platforms. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountKey

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Encrypted JSON format key for secure storage of authentication credentials for external bot
API calls.


Standard Objects ExtConvParticipantIntegDef

**Field** **Details**

```
BotProvider

ChannelMode

ClientIdentifier

DeveloperName

Language

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Bot provider for integration of authentication and request and response logic.

Possible value:

**•** `Custom`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Possible values for the type of channel:

**•** `Messaging`

**•** `Voice`

The default value is `Messaging` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
API client ID of the bot provider.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique name of the object in the API.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the master label.


### Standard Objects ExtDataShare

**Field** **Details**

```
MasterLabel

NamespacePrefix

ProjectIdentifier

Status

### ExtDataShare

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the `ExtConvParticipantIntegDef` object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If it's part of a managed package, the namespace of the package that contains integration
definition for the external conversation participant.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the project in the provider framework to scope API calls and resource access.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the integration.

Possible values are:

**•** `Active`

**•** `Deleted`

**•** `Inactive`

The default value is `Active` .

Represents a data share, which is a collection of Data Cloud objects that can be shared with other Data Cloud orgs or third-party partners.
This object is available in API version 56.0 and later.


Standard Objects ExtDataShare

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataShareType

DataSpaceId

InboundDataShareName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data share, indicating the direction of data flow. If `Outbound`, the data share
was created on this Data Cloud org and is shared to third-party partners or with another
Data Cloud org. If `Inbound`, the data share comes from another Data Cloud org and is
shared to this Data Cloud org.

Possible values are:

**•** `Inbound`

**•** `Outbound`

The default value is `Outbound` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the data space under which the data share was created.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the data share in the source Data Cloud org.


Standard Objects ExtDataShare

**Field** **Details**

```
InboundDataShareOrgIdentifier

LastReferencedDate

LastViewedDate

Name

ObjectCount

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the source Data Cloud org that shared a data share with the target org.

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

The timestamp when the current user last viewed this record or list view.

If this value is null, and `LastReferenceDate` is not null, the user accessed this record
or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the data share.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of Data Cloud objects added to this data share.


### Standard Objects ExternalAccountHierarchy

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtDataShareChangeEvent on page 68**
Change events are available for the object.

**ExtDataShareFeed on page 55**
Feed tracking is available for the object.

**ExtDataShareHistory on page 63**
History is available for tracked fields of the object.

**ExtDataShareOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ExtDataShareShare on page 67**
Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Create a Data Stream](https://help.salesforce.com/s/articleView?id=data.c360_a_create_data_shares.htm&language=en_US)

### ExternalAccountHierarchy

Represents the external account hierarchy, which works like a role-based hierarchy. Use ExternalAccountHierarchy to allow partner and
customer users to share data with other external accounts in their hierarchy.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have a Partner or Customer Community Plus license.

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the account in the external account hierarchy.


Standard Objects ExternalAccountHierarchy

**Field** **Details**

CurrencyISOCode

```
Description

HierarchyType

IsAccessibleToParent

IsActive

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

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the external account hierarchy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `CustomerPortal`  - Customer

**•** `Partner`

The default value is `Partner` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows data to be shared with parent account in the account hierarchy. The default value is
`true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ExternalAccountHierarchy

**Field** **Details**

**Description**
When true, the hierarchy is turned on. The default value is `false` .

```
LastReferencedDate

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external account hierarchy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent account.


### Standard Objects ExternalAccountHierarchyHistory ExternalAccountHierarchyHistory

Represents the history of changes to values in the fields of an external account hierarchy. This object is available in API version 50.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

You must have a Partner or Customer Community Plus license.

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
Possible values are:

**•** Address

**•** AnyType

**•** AutoNumber

**•** Base64

**•** BitVector

**•** Boolean

**•** Content

**•** Currency

**•** DataCategoryGroupReference

**•** DateOnly

**•** DateTime

**•** Division

**•** Double

**•** DynamicEnum

**•** Email

**•** EncryptedBase64

**•** EncryptedText


Standard Objects ExternalAccountHierarchyHistory

**Field** **Details**

**•** EntityId

**•** EnumOrId

**•** ExternalId

**•** Fax

**•** File

**•** HtmlMultiLineText

**•** HtmlStringPlusClob

**•** InetAddress

**•** Json

**•** Location

**•** MultiEnum

**•** MultiLineText

**•** Namespace

**•** Percent

**•** PersonName

**•** Phone

**•** Raw

**•** RecordType

**•** SfdcEncryptedText

**•** SimpleNamespace

**•** StringPlusClob

**•** Switchable_PersonName

**•** Text

**•** TimeOnly

**•** Url

**•** YearQuarter

```
ExternalAccountHierarchyId

Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the external account hierarchy.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects ExternalClientApplication

**Field** **Details**

**Description**
Possible values are:

**•** Account

**•** HierarchyType - Hierarchy Type

**•** IsAccessibleToParent - Is Accessible to Parent

**•** IsActive - Is Hierarchy Active

**•** Name

**•** Owner

**•** Parent

**•** Created - Created.

**•** FeedEvent - Feed Event

**•** IndividualMerged - Individual Merged

**•** Locked - Record Locked

**•** OwnerAccepted - Owner (Accepted)

**•** OwnerAssignment - Owner (Assignment)

**•** Unlocked - Record unlocked

```
NewValue

OldValue

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

### ExternalClientApplication

For internal use only.

### ExternalDataSource

Represents an external data source, which defines connection details for integration with data and content that are stored outside the
Salesforce org. This object is available in API version 27.0 and later.


Standard Objects ExternalDataSource

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

From API version 48.0 onwards, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
AuthProviderId

CustomConfiguration

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce ID of the authentication provider, which defines the service that provides the login
process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders” permissions can
view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

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

**Description**
A JSON-encoded configuration string that defines parameters specific to the type of external
data source.


Standard Objects ExternalDataSource

**Field Name** **Details**

```
DeveloperName

Endpoint

isWritable

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
In managed packages, this field prevents naming conflicts on package installations. With this
field, a developer can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
textarea

**Properties**
Nillable

**Description**
The URL of the external system, or if that URL is defined in a named credential, the named
credential URL.

A named credential URL contains the scheme `callout:`, the name of the named credential,
and an optional path. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ .
You can append a query string to a named credential URL. Use a question mark (?) as the
separator between the named credential URL and the query string. For example:
`callout:` _`My_Named_Credential`_ `/` _`some_path`_ `?format=json` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Lets the Lightning Platform and users in this org create, update, and delete records for external
objects associated with the external data source. The external object data is stored outside
the org. By default, external objects are read only.

Available only for Salesforce Connect external data sources. Available in API version 35.0 and
later. However, with the cross-org adapter for Salesforce Connect, you can set this field to
`true` only in API version 39.0 and later.

**Type**
picklist


Standard Objects ExternalDataSource

**Field Name** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the `MasterLabel` .

```
MasterLabel

NamedCredentialId

NamespacePrefix

PrincipalType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the external data source. This internal label doesn’t get translated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the referenced named credential for an external data source. Required
for Salesforce Connect adapters for Amazon DynamoDB, Amazon Athena, GraphQL, and
OData 4.01. For connecting to other external data sources, the field must be null. This field is
available in API version 58.0 and later.

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
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

**Type**
picklist


Standard Objects ExternalDataSource

**Field Name** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether the org uses one set ( `NamedUser` ), multiple sets ( `PerUser` ), or no
( `Anonymous` ) credentials to access the external system. Each set of credentials corresponds
to a login account on the external system. Corresponds to `Identity Type` in the user
interface.

```
Protocol

Repository

Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether to use OAuth, password authentication, or no authentication to access the
external system.

Some types of external data sources support only one value.

**•** For cloud-based Files Connect external systems, select **Oauth 2.0** .

**•** For on-premises systems, select **Password Authentication** .

**•** For Simple URL data sources, select **No Authentication** .

Additional authentication protocols are supported for the Amazon DynamoDB, Amazon
Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used for SharePoint Online. An optional name of the repository in the data source. Not
applicable to all data source types.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the adapter that connects to the external system.


### Standard Objects ExternalDataUserAuth

Usage

Define an external data source to connect to data or content that’s stored outside the Salesforce org. Then create external objects, which
map to the external system’s data and behave similarly to custom objects.

Note: Some external data source fields rely on per-user authentication to connect with an external system. If an admin edits one
of these fields, then the previously authenticated credentials can get invalidated, requiring individual users to reauthenticate.

SEE ALSO:

### ExternalDataUserAuth

NamedCredential

### ExternalDataUserAuth

Stores authentication settings for a Salesforce user to access an external system. The external system must be defined in an external data
source or a named credential that’s configured to use per-user authentication. This object is available in API version 27.0 and later.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AuthProviderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the authentication provider, which defines the service that
provides the login process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders”
permissions can view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup


Standard Objects ExternalDataUserAuth

**Field Name** **Details**

**Refers To**
AuthProvider

```
ExternalDataSourceId

Password

Protocol

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce ID of the external data source or named credential that defines the
external system.

This is a polymorphic relationship field.

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Password portion of the credentials for the Salesforce user to access the external
system.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether to use OAuth, password authentication, or no authentication
when the user accesses the external system.

Additional authentication protocols are supported for the Amazon DynamoDB,
Amazon Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange


### Standard Objects ExternalEncryptionRootKey

**Field Name** **Details**

```
UserId

Username

```

Usage

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce user who’s accessing the external system.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Username portion of the credentials for the Salesforce user to access the external
system.

These authentication settings enable a Salesforce user to access an external system. The external system is defined in Salesforce as one
of the following.

**•** External data source—Provides access to external objects, whose data is stored outside the Salesforce organization.

**•** Named credential—Enables the user’s actions to trigger authenticated callouts to the endpoint that’s specified in the named
credential.

If you grant users access to the external data source or named credential via permission sets or profiles, those users can manage their
[own authentication settings. See Store Authentication Settings for External Systems in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.external_authentication.htm&type=5&language=en_US)

SEE ALSO:

ExternalDataSource

NamedCredential

### ExternalEncryptionRootKey

Represents metadata about root keys stored in third-party key stores that are used to generate and secure keys that encrypt Salesforce
data. This object is available in API version 58.0 and later.


Standard Objects ExternalEncryptionRootKey

Root keys are used to generate data encryption keys (DEKs) in Salesforce, which are in turn used to encrypt and decrypt data. Root keys
are also used as wrapping keys to secure DEKs in the Salesforce database.

Supported Calls

`describeSObjects()`, `query()`, `update()`

Special Access Rules

This object is available as part of the Shield and Salesforce Platform Encryption add-on subscriptions. Access to this object also requires
the Cache-Only Key Service add-on subscription.

Fields

**Field** **Details**

```
ActivatedDate

CreatedBy

Description

LastModifiedBy

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date the key was activated in Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who created the root key. For example,
`user@example.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The user-defined description of the root key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects ExternalEncryptionRootKey

**Field** **Details**

**Description**
The email address of the user who most recently modified the key. For example,
`user@example.com` .

```
Region

RootKeyIdentifier

RootKeyService

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The region for the customer managed key. For example, if the `RootKeyService` is `AWS`,
the region is an Amazon Web Services (AWS) region such as `us-east1` .

**Type**
string

**Properties**
Filter, Nillable, Sort, Update

**Description**
The unique key identifier from the external KMS, such as an AWS Amazon Resource Name
(ARN). For example,

```
  arn:aws:kms:us-west-2:123456789000:key/123ab456-7cd8-9012-3e4f-5gh678i901j2

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The external key management service connected to Salesforce. For example, `AWS` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The status of the key. This is the only value that can be changed using update(). You can
only change the status from Active to Inactive, or from Inactive to Active.

Possible values are:

**•** `Activation Pending` —Salesforce is waiting for confirmation of a valid key policy
in the external key store.

**•** `Active` —Can be used to encrypt new DEKs and decrypt existing DEKs.

**•** `Archived` —Can’t encrypt new DEKs. Can be used to decrypt previously created DEKs.

**•** `Canceled` —Root key activation canceled by a user.


Standard Objects ExternalEncryptionRootKey

**Field** **Details**

**•** `Inactive` —The root key, and the DEKs that it encrypts, are inaccessible. Inaccessible
DEKs can’t be used to decrypt data, which renders that data also inaccessible.

**•** `Unavailable` —The root key, and the DEKs that it encrypts, cannot be accessed. The
root key has been removed or deactivated by the managing KMS.

Usage

Three functions are available: `describeSObjects()`, `query()`, and `update()`

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives you starter information](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_encryption_rest_api_guide.meta/platform_encryption_rest_api_guide/api_rest_encryption.htm)
on using REST to work with Shield Platform Encryption.

**Describe an external root key with** **`describeSObjects()`**

To get information about the ExternalEncryptionRootKey sObject, use `describe` .

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

     ExternalEncryptionRootKey/describe'

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN'

```

On success, the response is the full JSON description of the ExternalEncryptionRootKey sObject.

**Get info on an external root key with** **`query()`**

To get information about a specific root key, use `query` on the `ExternalEncryptionRootKey` sObject. Use the Identifier
value as listed on the Key Management Page for the root key Id in the WHERE clause.

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/query?' \

     ?q=SELECT+FIELDS(ALL)+FROM+ExternalEncryptionRootKey+WHERE+Id='48q001t5ddzbucnAAA'+\

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN'

```

On success, the response is be similar to

```
     {

       "totalSize": 1,

       "done": true,

       "records": [

          {

            "attributes": {

               "type": "ExternalEncryptionRootKey",

               "url":

     "/services/data/v62.0/sobjects/ExternalEncryptionRootKey/48q001t5ddzbucnAAA"

            },

            "Id": "48q001t5ddzbucnAAA",

            "RootKeyIdentifier": "97ee8238-c5ac-4320-a2d0-a728aaefd567",

            "CreatedDate": "2024-08-05T17:32:11.841+0000",

            "CreatedBy": "charley.t.pulasky@wise-raccoon-od1ly6.com",

            "LastModifiedDate": "2025-02-12T18:36:11.063+0000",

            "LastModifiedBy": "charley.t.pulasky@wise-raccoon-od1ly6.com",

            "RootKeyService": "SF",

```


### Standard Objects ExternalEvent

```
            "Region": "KEY REGION",

            "Status": "Active",

            "Description": null,

            "ActivatedDate": null

          }

       ]

     }

```

**Update Status on an external root key with** **`update()`**

To update the status of an `ExternalEncryptionRootKey` from `Active` to `Inactive`, or from `Inactive` to `Active`,
use PATCH on the specific key object. Use the vaule for `Identifier` as listed on the Key Management Page for the root key
identifier.

```
     curl --location --request PATCH

     'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/ExternalEncryptionRootKey/ROOTKEYIDENTIFIER'

      \

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN'\

     --data '{

      "Status": "Active"

     }'

```

On success, the response is be similar to I SEE NO RESPONSE.

### ExternalEvent

Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
ExternalId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ExternalEvent

**Field** **Details**

**Description**
The ID of the external event.

```
Location

Name

Notes

Time

Title

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The site where the external event takes place.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the external event’s organizer.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Additional details about the external event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The time the external event is held.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the external event.


### Standard Objects ExternalEventMapping

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExternalEventChangeEvent on page 68**
Change events are available for the object.

### ExternalEventMapping

Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
EndDate

EventId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the external event ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Salesforce event created by the external event.

This field is a relationship field.

**Relationship Name**
Event

**Refers To**
Event


Standard Objects ExternalEventMapping

**Field** **Details**

```
ExternalId

IsLocked

IsRecurring

MayEdit

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the external event.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the external event is locked, or `false` if it’s not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the external event is recurring (true) or not (fales).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

Indicates whether the external event can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the external event’s organizer.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects ExternalSocialAccount

**Field** **Details**

**Description**
The ID of the creator of the external event.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
StartDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the external event begins.

### ExternalSocialAccount

Represents a managed social media account on a social network such as Facebook or Twitter. This object is available in API version 29.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
AuthorizedBy

DataSourceId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Radian6 user who added the social account to Radian6.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ExternalSocialAccount

**Field Name** **Details**

**Description**
ID of the Radian6 data source for the social account.

```
DefaultResponseAccountId

DeveloperName

ExternalAccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the managed social account to use by default when responding.

This is a relationship field.

**Relationship Name**
DefaultResponseAccount

**Relationship Type**
Lookup

**Refers To**
ExternalSocialAccount

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

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID of the social account on the social network.


Standard Objects ExternalSocialAccount

**Field Name** **Details**

```
ExternalPictureURL

IsActive

IsAuthenticated

IsCaseCreationEnabled

IsDataSourceActive

Language

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to the picture of the social account on the social network.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is active or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is authenticated or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether case creation for the social account is enabled or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the data source is active or not.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the language of the social account.


Standard Objects ExternalSocialAccount

**Field Name** **Details**

```
MasterLabel

ProfileUrl

Provider

ProviderUserId

RuleId

SocialPropertyId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the social account. This display value is the internal label and
does not get translated.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Social network, such as Facebook or Twitter, of the social account.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID for the social network of the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 rule for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ExtKnowledgeConnector

**Field Name** **Details**

**Description**
ID of the Radian6 social property for the account.

```
TopicId

UniqueName

Username

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the topic for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique name for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Username for the social account.

[Although available, many of the Radian6-related fields are no longer accurate or used. We recommend using Social Engagement](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm)
[Resources in](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm) _Connect REST API Developer Guide_ .

### ExtKnowledgeConnector

Represents a connector to a third-party knowledge source for Unified Knowledge. This object is available in API version 60.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Knowledge must be enabled in your org. Salesforce Knowledge users, unlike customer and partner users, must also be granted
the Knowledge User feature license.


Standard Objects ExtKnowledgeConnector

Fields

**Field** **Details**

```
IsLocked

LastSyncDate

LastSyncStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the connector last synced with the third-party knowledge source to import
articles into Salesforce.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the connector’s last sync of articles from the third-party knowledge
source into Salesforce.

Possible values are:

**•** `articleLimitExceeded` —Exceeded article or version limits

**•** `completed` —Completed

**•** `completedWithErrors` —Completed with errors

**•** `ended` —Ended

**•** `failed` —Failed

**•** `initiating` —Started

**•** `invalidCredentials` —Invalid credentials

**•** `polling` —Polling for Zoomin sync to complete

**•** `queued` —Queued

**•** `syncing` —Syncing

**•** `timedOut` —Timed Out

**•** `unavailable` —Zoomin unavailable


Standard Objects ExtKnowledgeConnector

**Field** **Details**

```
MayEdit

Name

NamedCredentialId

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated import article condition record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The connector’s label in Unified Knowledge setup.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce ID of the named credential that’s used for a request. The named credential identifies
the third-party system and the third-party authentication settings.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID of the owner of the connector.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects ExtlClntAppOauthPlcyCnfg

**Field** **Details**

**Refers To**
Group, User

```
PartnerConnectorIdentifier

ShouldOpenInSource

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether articles imported into Salesforce open in the third-party source from links
in Salesforce.

The default value is `false` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtKnowledgeConnectorOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ExtKnowledgeConnectorShare on page 67**
Sharing is available for the object.

### ExtlClntAppOauthPlcyCnfg

For internal use only.

### ExtlClntAppOauthSettings

For internal use only.

### ExtlClntAppPlcyCnfg

For internal use only.


### Standard Objects ExtlIntrIdMapping ExtlIntrIdMapping

Represents a mapping between a Salesforce record and its corresponding record in an external system, such as Workday. This object is
available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
ExternalIdentifier

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the external event.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the external event’s organizer.


### Standard Objects ExtlRecShrCnct

**Field** **Details**

```
OwnerId

RecordIdentifier

RelatedExternalIdentifier

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the creator of the external event.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Salesforce record that is linked to a record in an external system.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of an associated record from the external system that provides additional context for
the integration.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtlIntrIdMappingOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ExtlIntrIdMappingShare on page 67**
Sharing is available for the object.

### ExtlRecShrCnct

Represents authentication data to make outbound calls to and inbound calls from an external system to publish events for Partner
Connect. This object is available in API version 62.0 and later.


Standard Objects ExtlRecShrCnct

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
CnctName

CnctRole

CnctStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the connection.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
System’s role in the connection.

Possible values are:

**•** `Partner`

**•** `Vendor`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the connection.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**•** `Error`

**•** `Pending`

**•** `Unknown`


### Standard Objects ExtlRecShrCnctAccnt

**Field** **Details**

```
ExternalClientApplicationId

ExtlSystem

NamedCredentialId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of external client app representing your org’s connection to the external system.

This field is a relationship field.

**Relationship Name**
ExternalClientApplication

**Refers To**
ExternalClientApplication

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
ID of the external system.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the named credential.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Refers To**
NamedCredential

### ExtlRecShrCnctAccnt

Represents an association between an account and an external record share connection for Partner Connect. This object is available in
API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ExtlRecShrCnctAccnt

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
AccountId

ExtlRecShrCnctId

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the account.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ExtlRecShrCnct record.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.


### Standard Objects ExtlRecShrField ExtlRecShrField

Represents an imported, exported, or updated external record share field for Partner Connect. This object is available in API version 63.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrObjectId

FieldDefaultValue

FieldSetType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrObject record.

This field is a relationship field.

**Relationship Name**
ExtlRecShrObject

**Refers To**
ExtlRecShrObject

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default value of the field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Set of fields associated with this record.


Standard Objects ExtlRecShrField

**Field** **Details**

Possible values are:

**•** `ExportedFields`

**•** `ImportedFields`

**•** `InternalFields`

```
IsFieldNillable

SendFieldUpdates

SharedFieldDevName

SharedFieldLabel

SharedFieldLength

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this field can be set to null ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether updates are tracked for this field, sent to the connected org, and stored
in the ExtlRecShrLead or ExlRecShrOpportunity objects ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Developer name of the field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label of the field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ExtlRecShrFieldMap

**Field** **Details**

**Description**
Maximum length of the field.

```
SharedFieldType

### ExtlRecShrFieldMap

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Field type of the imported, exported, or updated field.

Possible values are:

**•** `Address`

**•** `Boolean`

**•** `Currency`

**•** `DateOnly`

**•** `DateTime`

**•** `Double`

**•** `DynamicEnum`

**•** `Email`

**•** `EntityId`

**•** `EnumOrId`

**•** `Fax`

**•** `Integer`

**•** `MultiLineText`

**•** `Percent`

**•** `Phone`

**•** `StaticEnum`

**•** `Text`

**•** `Url`

Represents the external record share field mapping between the sender and receiver for Partner Connect. This object is available in API
version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects ExtlRecShrLead

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ImportedFieldId

InternalFieldId

### ExtlRecShrLead

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrField record containing the field data sent from the external system.

This field is a relationship field.

**Relationship Name**
ImportedField

**Refers To**
ExtlRecShrField

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrField record containing the field data received on the internal system.

This field is a relationship field.

**Relationship Name**
InternalField

**Refers To**
ExtlRecShrField

Represents the Lead record of a vendor org if you’re a partner. If you’re a vendor for Partner Connect, this object represents a partner
org. This object is available in API version 62.0 and later.

In a related list, the label of this object is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Standard Objects ExtlRecShrLead

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrCnctId

LeadId

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the partner lead.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Master-detail

**Refers To**
Lead (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects ExtlRecShrObject

**Field** **Details**

**Description**
For internal use only.

### ExtlRecShrObject

Represents a shared object for Partner Connect. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
DefaultRecordOwnerId

ExtlObjectType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the shared record owner. The owner can be a user or a queue, represented by a Group
ID.

This field is a polymorphic relationship field.

**Relationship Name**
DefaultRecordOwner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object type in the external org or system that is part of the object field mapping.

Possible values are:


Standard Objects ExtlRecShrObject

**Field** **Details**

**•** `ExtlRecShrLead`

**•** `ExtlRecShrOpportunity`

**•** `Lead`

**•** `Opportunity`

```
ExtlRecShrCnctId

FieldMapStatus

InternalObjectType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Exporter’s status of the field mapping.

Possible values are:

**•** `ActiveMapping`

**•** `Selected`

**•** `SystemOverride`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object type in your org or system used to group field selections and field mappings.

Possible values are:

**•** `ExtlRecShrLead`

**•** `ExtlRecShrOpportunity`

**•** `Lead`

**•** `Opportunity`


### Standard Objects ExtlRecShrOpportunity ExtlRecShrOpportunity

Represents the opportunity for Partner Connect in the vendor org if you’re a partner and the partner org if you’re the vendor. This object
is available in API version 62.0 and later.

The label of this object in the related list is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrCnctId

Name

OpportunityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference


### Standard Objects ExtlRecShrPcklstOptn

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the associated opportunity.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Master-detail

**Refers To**
Opportunity (the master object)

### ExtlRecShrPcklstOptn

Represents a picklist option of an external record share picklist field shared between a partner and vendor for Partner Connect. This
object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrFieldId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated external record share field of type picklist.

This field is a relationship field.

**Relationship Name**
ExtlRecShrField


### Standard Objects ExtlRecShrPicklistMap

**Field** **Details**

**Refers To**
ExtlRecShrField

```
IsDefaultOption

SharedOptionLabel

SharedOptionValue

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this picklist option is set as the default option ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the picklist option.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the picklist option.

### ExtlRecShrPicklistMap

Represents the external record share picklist field mapping between the partner and vendor system for Partner Connect. This object is
available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .


### Standard Objects ExtlRecShrRecordMap

Fields

**Field** **Details**

```
ImportedPcklstOptionId

InternalPcklstOptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the external system.

This field is a relationship field.

**Relationship Name**
ImportedPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the internal system.

This field is a relationship field.

**Relationship Name**
InternalPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

### ExtlRecShrRecordMap

Represents the lead or opportunity being mapped between a partner and vendor for Partner Connect. This object is available in API
version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ExtlRecShrRecordMap

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrCnctId

ExtlRecord

InboundStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead or opportunity record on the external system.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of imports and updates received.

Possible values are:

**•** `ImportSuccess`

**•** `ImportConctExtlRecError`

**•** `UpdateSuccess`

**•** `UpdateFieldMapError`

**•** `UpdateConctExtlRecError`

**•** `UpdateUnknownError`


Standard Objects ExtlRecShrRecordMap

**Field** **Details**

```
InternalRecordId

IsImported

LastModifiedSent

Name

OutboundStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the lead or opportunity record on the internal system.

This field is a polymorphic relationship field.

**Relationship Name**
InternalRecord

**Relationship Type**
Master-detail

**Refers To**
Lead, Opportunity (the master object)

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record originated on the internal system ( `true` ) or external system
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp of the last record update between the vendor and partner. This field doesn’t
capture when the result is received.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
picklist


Standard Objects ExtlRecShrRecordMap

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of exports, updates, and results received.

Possible values are:

**•** `ExportSuccess`

**•** `ExportInProgress`

**•** `ExportSuccessSkipped`

**•** `ExportSuccessPartial`

**•** `ExportPublishFieldMapError`

**•** `ExportSubscribeFieldMapError`

**•** `ExportPublishEventError`

**•** `ExportPublishUnknownError`

**•** `ExportSubscribeUnknownError`

**•** `ExportPublishConnectionError`

**•** `UpdateInProgress`

**•** `UpdateInProgressUpdateSuccess`

**•** `UpdatePublishFieldMapErrorUpdateSubscribeRecordNotFound`

**•** `UpdatePublishFieldMapError`

**•** `UpdateSubscribeFieldMapError`

**•** `UpdatePublishConnectionError`

**•** `UpdatePublishEventError`

**•** `UpdatePublishUnknownError`

**•** `UpdateSubscribeUnknownError`

```
UniqueRecordKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Record key used internally for indexing. If `IsImported` is `false`, then this field contains
the `InternalRecordId` value. If `IsImported` is `true`, this field contains the
`ExtlRecord` value.

This field is a calculated field.


### Standard Objects FeedAttachment FeedAttachment

Represents an attachment to a feed item, such as a file attachment or a link. Use FeedAttachment to add various attachments to one
feed item. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `idEnabled()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** You can read, create, update, or delete a FeedAttachment only if you have the corresponding access to the associated FeedItem.

**•** Inline images aren’t creatable, updatable, or deletable through SOAP API.

Fields

**Field Name** **Details**

```
FeedEntityId

RecordId

Title

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated feed entity that contains this attachment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that this feed attachment contains. For inline images,
`RecordId` is a ContentDocument ID. For content attachments, `RecordId`
is a ContentVersion ID, For feed items, `RecordId` is a FeedItem ID.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of this feed attachment. When `Type` is `Link`, `Title` value is the
label for the attachment link. Otherwise, `Title` value isn’t used.

**Type**
picklist


Standard Objects FeedAttachment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this feed attachment. Valid values are:

**•** 0 `Content` —A content attachment.

**•** 1 `InlineImage` —An inline image. The system creates an inline image
attachment when an image is added to the body of the associated FeedItem.
You can’t add an inline image directly using FeedAttachment.

**•** 2 `Link` —A link.

**•** 3 `FeedEntity` —A feed entity, for example, a post that is shared. Available
in API version 39 and later in Lightning Experience.

**•** 4 `ChatterExtension` —a Rich Publisher App that’s integrated with the
Chatter publisher.

**•** 5 `Record` —A record.

```
Value

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The string value of this FeedAttachment. This field is optional. If the feed
attachment is a Link FeedAttachment, the value is the link URL string.

**•** This Apex example shows how to add an attachment to a Lead using API version 36.0 and later. First, post a feed item.

```
  //create and insert post

  FeedItem post = new FeedItem();

  post.Body = 'HelloThere';

  post.ParentId = ' ID_OF_LEAD_ENTITY ';

  post.Title = ' FileName ';

  insert post;

```

Then insert the attachment.

```
  //create and associate a content attachment to the post

  FeedAttachment feedAttachment = new FeedAttachment();

  feedAttachment.FeedEntityId = post.Id;

  feedAttachment.RecordId = ' ID_OF_CONTENT_VERSION ';

  feedAttachment.Title = ' FileName ';

  feedAttachment.Type = 'CONTENT';

  insert feedAttachment;

```

**•** You can create only one link attachment ( `FeedAttachment` of type `Link` ) per feed item.


### Standard Objects FeedComment

**•** If the feed item type is one of the following, you can add content or link feed attachments to a FeedItem.

**–** `AdvancedTextPost`

**–** `TextPost`

**–** `ContentPost`

**–** `LinkPost`

**–** `QuestionPost`

**•** When a `FeedAttachment` is added or removed from a feed item, Salesforce updates the type of the feed item to its most
appropriate value, as follows.

**–** If all content feed attachments are removed from a feed item of type `ContentPost`, the type of this feed item is updated to
`TextPost` .

**–** Conversely, if a content feed attachment is added to a feed item of type `TextPost`, the type of this feed item is updated to
`ContentPost` .

**–** If all link feed attachments are removed from a feed item of type `LinkPost`, the type of this feed item is updated to `TextPost` .

**–** Conversely, if a link feed attachment is added to a feed item of type `TextPost`, the type of this feed item is updated to
`LinkPost` .

**–** The type of all other feed items, such as `QuestionPost` or `AdvancedTextPost` feed items, doesn’t change when any
feed attachments are added or removed.

**–** If a content feed attachment is added to a feed item of type `LinkPost`, the feed item type is updated to `ContentPost` .

**–** If all content attachments are removed from a feed item of type `ContentPost`, but there's also a link attachment, the feed
item type is updated to `LinkPost` .

**•** Users without administrator privileges can’t retrieve a FeedAttachment by its ID in a SOQL query. They can retrieve attachments by
specifying the associated `FeedEntityId`, as follows:

```
     SELECT Id FROM FeedAttachment WHERE FeedEntityId = ' some_feedItem_id '

```

**•** Alternatively, retrieve attachments by using a SOQL query on FeedItem with a subquery on the FeedAttachments child relationship,
as follows.

```
     SELECT Body, (SELECT RecordId, Title, Type, Value FROM FeedAttachments)

     FROM FeedItem

     WHERE Id = ' some_feedItem_id '

```

**•** FeedAttachment is not a triggerable object. You can access feed attachments in FeedItem _update_ triggers by retrieving them through
[a SOQL query. For a trigger example, and to learn about trigger considerations for FeedAttachment, see Triggers for Chatter Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_fields_not_updated_chatter.htm)
in the _Apex Developer Guide_ .

### FeedComment

Represents a comment added to a feed by a user. This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects FeedComment

Special Access Rules

Note the following when working with feed comments.

**•** You must have read access to the feed’s parent type to see a FeedComment record.

**•** You must be able to access the feed to add a comment.

**•** If the comment is related to a user record, the user can delete the comment. For example, if John Smith makes a comment on Sasha
Jones’ profile feed, Sasha can delete the comment.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**•** Modify All Data

**•** Modify All Records on the object associated with the feed and delete permission on the parent feed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

**•** Manage Unlisted Groups

Only users with this permission can delete items in unlisted groups.

Fields

**Field** **Details**

```
CommentBody

CommentType

```

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The text in the comment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of comment:

**•** `ContentComment` —an uploaded file on a comment

**•** `TextComment` —a direct text entry on a comment

Before API version 24.0, a text entry was required on a comment. As of version 24.0, a text
entry is optional if the `CommentType` is `ContentComment` .


Standard Objects FeedComment

**Field** **Details**

```
FeedItemId

HasEntityLinks

InsertedById

IsRichText

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the feed item containing the comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed `CommentBody` includes at least one link to a record.

Note: This field is available starting in API version 43.0.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed `CommentBody` contains rich text. If you post a rich text feed
comment using SOAP API, set `IsRichText` to `true` and escape HTML entities from
the body. Otherwise, the comment is rendered as plain text.

Rich text supports the following HTML tags:


Standard Objects FeedComment

**Field** **Details**

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: This attribute is available as of API version 38.0. In API version 38.0 and later,
the system replaces special characters in rich text with escaped HTML. In API version
37.0 and prior, all rich text appears as a plain-text representation.

```
IsVerified

LastEditById

LastEditDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a comment on a question is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed comment.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort


Standard Objects FeedComment

**Field** **Details**

**Description**
The date the feed comment was last edited.

```
ParentId

RelatedRecordId

Revision

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of a record associated with the feed comment. For example, if you are commenting on a
change to a field on Account, `ParentId` is set to the account ID.

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentComment` . This field is null for
all comments except `ContentComment` .

For example, set this field to an existing ContentVersion ID and set the `CommentType` to
`ContentComment` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of times the comment was revised.

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed comment is published and visible to all who can access the parent
feed item. To change a comment’s status, the comment’s parent feed item must be in a
published state. This field is available in API version 38.0 and later.

Possible values are:

**•** `Published` —The comment is visible to all who can access the parent feed item.

**•** `PendingReview` —The comment is visible to its author. Users see the parent feed
item and have View All Data or Can Approve Feed Post and Comment permission also
see the comment. The author can delete the comment as can users who see the comment
and have Can Approve Feed Post and Comment or Modify All Data permission. If the


Standard Objects FeedComment

**Field** **Details**

parent feed item is published, the author can edit the comment. Users who see the
comment and have Can Approve Feed Post and Comment or Modify All Data permission
can also edit the comment. Users with Can Approve Feed Post and Comment or Modify
All Data permission can change comment status from Published to PendingReview and
from PendingReview to Published.

Some actions are blocked when a feed comment is pending review:

**–** Select as Best—When a feed comment that is marked as best answer becomes
unpublished, it’s removed as the best answer. If the comment is published, its best
answer status is not restored.

**–** Like and unlike

**•** `Isolated` —The comment is visible only to admins. After an item is isolated, the author
no longer has view or edit access. The admin user can edit, view, and delete isolated
feed comments.

```
SystemModstamp

ThreadChildrenCount

ThreadLastUpdatedDate

```

**Type**
datetime

**Properties**
Defaulted on create, Filter

**Description**
Date and time when a user or automated process (such as a trigger) last modified this record.
In this context, "trigger" refers to Salesforce code that runs to implement standard
functionality, and not an Apex trigger. `SystemModstamp` [is a read-only system field,](http://www.salesforce.com/developer/docs/api/Content/system_fields.htm)
available in FeedComment as of API version 37.0.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The count of comments associated with this parent feed object. The feed object can be
either a Feed Item or a Feed Comment. The count shows how many comments are directly
subordinate to the parent. This field is available on the object when **Allow discussion**
**threads** is selected in the Administration Workspace. This field is available in API version
44.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time the thread on this comment was last updated. This field is available on
the object when **Allow discussion threads** is selected in the Administration Workspace.
This field is available in API version 44.0 and later.


Standard Objects FeedComment

**Field** **Details**

```
ThreadLevel

ThreadParentId

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier that shows the level of this Feed Comment in a thread. By default, there are a
maximum of three levels in a thread. The `ThreadLevel` value shows in which of the
three levels this comment falls. This field is available on the object when **Allow discussion**
**threads** is selected in the Administration Workspace. This field is available in API version
44.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier of the feed item that is the parent of this comment. This field is available on
the object when **Allow discussion threads** is selected in the Administration Workspace.
This field is available in API version 44.0 and later.

This is a relationship field.

**Relationship Name**
ThreadParent

**Relationship Type**
Lookup

**Refers To**
FeedComment

**•** As of API version 23.0 and later, if you have View All Data permission, you can query FeedComment records directly without an ID
filter. If you don’t have View All Data permission, you can’t query FeedComment records directly, with or without an ID filter.

For example, the following query returns general information about a feed:

```
  SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName,

         CreatedBy.LastName, ParentId, Parent.Name, Body

  FROM FeedItem

  WHERE CreatedDate > LAST_MONTH

  ORDER BY CreatedDate DESC, Id DESC

```

**•** You can search for text in comments using SOSL. For example, the following Java class uses `search()` to find the string “foo” in
any field of a record:

```
  public void searchSample() {

   try {

```


### Standard Objects FeedItem

```
       SearchResult sr = connection.search("find {foo} in all fields " +

          "returning feedcomment(Id, FeedItemId, CommentBody)");

       // Put the results into an array of SearchRecords

       SearchRecord[] records = sr.getSearchRecords();

       // Check the length of the returned array of records to see

       // if the search found anything

       if (records != null && records.length > 0) {

         System.out.println("Found " + records.length + " comments: ");

         // Display each comment

         for (SearchRecord record : records) {

          FeedComment comment = (FeedComment) record.getRecord();

          System.out.println(comment.getId() + ": " +

            comment.getCommentBody());

         }

       } else {

         System.out.println("No records were found for the search.");

       }

      } catch (ConnectionException ce) {

       ce.printStackTrace();

      }

     }

```

**•** If you use an Apex trigger to modify the `Body` of a FeedComment object, all mentions hyperlinks are converted to plain text. The
mentioned users don't get email notifications.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.

SEE ALSO:

Custom Object__Feed

### FeedItem FeedItem represents an entry in the feed, such as changes in a record feed, including text posts, link posts, and content posts. This object

is available in API version 21.0 and later. This object replaces FeedPost.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

**•** You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**–** Modify All Data

**–** Modify All Records on the feed item’s parent object, for example, Account for a feed item on an account feed

**–** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments that they can see.


Standard Objects FeedItem

Only users with this permission can delete items in unlisted groups.

**•** Guest users can’t insert system field values for Chatter feeds. Even if you try to assign the CanInsertFeedSystemFields permission to
a Guest User, the permission isn’t granted.

Only users with the Modify All Data permission can delete a feed item of `Type TrackedChange` .

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

Fields

**Field Name** **Details**

```
BestCommentId

Body

CommentCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

This is a relationship field.

**Relationship Name**
BestComment

**Relationship Type**
Lookup

**Refers To**
FeedComment

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
The body of the feed item. Required when `Type` is `TextPost` or
`AdvancedTextPost` . Optional when `Type` is `ContentPost` or
`LinkPost` .

Although a value for `Body` isn’t required for the `ContentPost` type, an
attachment is required. If an attachment isn’t present, the type changes to
`TextPost` or `AdvancedTextPost`, depending on the API version.
`TextPost` and `AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the
body of rich text posts.

**Type**
int


Standard Objects FeedItem

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

Tip: In a feed that supports pre-moderation, `CommentCount` isn’t updated
until a comment is published. For example, say that you comment on a post
that already has one published comment and your comment triggers
moderation. Now there are two comments on the post, but the count says
there's only one. In a moderated feed, comments aren’t counted until approved
by an admin or someone with Can Approve Feed Post and Comment or Modify
All Data.

Feed moderation has implications on how you retrieve feed comments. In a
moderated feed, rather than retrieving comments by looping through
`CommentCount`, go through pagination until the end of comments is
returned.

```
ConnectionId

ContentData

ContentDescription

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When a PartnerNetworkConnection modifies a record that is tracked, the
`CreatedBy` field contains the ID of the system administrator. The
`ConnectionId` contains the ID of the PartnerNetworkConnection. Available
if Salesforce to Salesforce is enabled for your org.

**Type**
base64

**Properties**
Create, Nillable

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is required if `Type` is `ContentPost` .
Encoded file data in any format, and can’t be 0 bytes. Setting this field
automatically sets `Type` to `ContentPost` .

**Type**
textarea

**Properties**
Create, Nillable, Sort


Standard Objects FeedItem

**Field Name** **Details**

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The description of the file specified in
`ContentData` .

```
ContentFileName

ContentSize

ContentType

FeedPostId

```

**Type**
string

**Properties**
Create, Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The name of the file uploaded to the feed. Setting
`ContentFileName` automatically sets `Type` to `ContentPost` .

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the size of the file (in bytes) uploaded
to the feed. This field is read-only and is automatically determined during insert.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the MIME type of the file uploaded to
the feed. This field is read-only and is automatically determined during insert.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field was removed in API version 22.0, and is available in earlier versions for
backward compatibility only.

ID of the associated FeedPost. A FeedPost represents the following types of
changes in a feed item: changes to tracked fields, text posts, link posts, and
content posts.


Standard Objects FeedItem

**Field Name** **Details**

```
HasContent

HasFeedEntity

HasLink

HasVerifiedComment

InsertedById

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has content.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a feed entity, for example, a post, as an
attachment. Available in API version 39 and later when sharing a feed entity in
Lightning Experience.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a link attached.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a question has an answer that is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application
migrates posts and comments from another application into a feed, the
`InsertedBy` value is set to the ID of the context user.

This is a polymorphic relationship field.


Standard Objects FeedItem

**Field Name** **Details**

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

```
IsClosed

IsDeleted

IsRichText

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
As of API version 43, a read-only field that indicates whether the feed item is
open or closed to new actions. A value of `true` places restrictions on the actions
a user can take on a feed item and its comments. For more information, see the
Usage section.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Standard system field. Indicates whether the record has been moved to the
Recycle Bin ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text
feed comment using SOAP API, set `IsRichText` to `true` and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use
`<p>&nbsp;</p>` to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`


Standard Objects FeedItem

**Field Name** **Details**

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`

```
                         src="sfdc://069B0000000omjh"></img>

```

Note: In API version 35.0 and later, the system replaces special characters
in rich text with escaped HTML. In API version 34.0 and prior, all rich text
appears as a plain-text representation.

```
LastEditById

LastEditDate

LikeCount

LinkUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed item.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date the feed item was last edited.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Create, Nillable, Sort

**Description**
The URL of a `LinkPost` .


Standard Objects FeedItem

**Field Name** **Details**

```
NetworkScope

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether this feed item is available in the default Experience Cloud site,
a specific Experience Cloud site, or all sites. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

`NetworkScope` can have the following values:

**•** `NetworkId` —The ID of the Experience Cloud site in which the FeedItem
is available. If left empty, the feed item is only available in the default
Experience Cloud site.

**•** `AllNetworks` —The feed item is available in all Experience Cloud sites.

Note the following exceptions for `NetworkScope` :

**•** Only feed items with a Group or User parent can set a `NetworkId` or a
null value for `NetworkScope` .

**•** For feed items with a record parent, users can set `NetworkScope` only
to `AllNetworks` .

**•** You can’t filter a feed item on the `NetworkScope` field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the object type to which the feed item is related. For example, set this field
to a `UserId` to post to someone’s profile feed, or an `AccountId` to post to
a specific account.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,


Standard Objects FeedItem

**Field Name** **Details**

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
ContactEncounterParticipant, ContentDocument, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, Event, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Identifier, Image, IndividualApplication, Invoice,
InvoiceLine, Lead, Location, MarketSegment, MarketSegmentActivation,
MemberPlan, MessagingSession, MktCalculatedInsight, OperatingHours,
Opportunity, Order, OrderItem, OtherComponentTask, PartyConsent,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, ProviderSearchSyncLog, PurchaserPlan, PurchaserPlanAssn,
ReceivedDocument, Report, ReportAnomalyEventStore, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderLineItem, ServiceAppointment,
ServiceResource, ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember,
ServiceTerritoryWorkType, SessionHijackingEventStore, Shift, Shipment,
ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

```
RelatedRecordId

```

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC
thanks posts, it’s the ID of the WorkThanks object associated with a
`RypplePost` . This field is typically null for all posts except `ContentPost`
and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed
with `Type` set to `ContentPost` .


Standard Objects FeedItem

**Field Name** **Details**

```
Revision

Status

Title

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is published and visible to all who can access
the feed. This field is available in API version 37.0 and later.

Possible values are:

**•** `Published` —The item’s visible to all with access to the feed.

**•** `PendingReview` —The item’s visible to its author and users who see the
item and have View All Data or Can Approve Feed Post and Comment
permission. Some people can delete and edit the item. They include the
author and users who see the item and have Can Approve Feed Post and
Comment or Modify All Data permission.

Note: These permissions don’t apply when you retrieve feed items
using SOQL. To filter out Pending Review feed items you must add an
explicit clause.

Some actions are blocked when a feed item is pending review:

**–** Comment

**–** Like and unlike

**–** Bookmark

**–** Share

**•** `Isolated` —The item is visible only to admins. After an item is isolated,
the author no longer has view or edit access. The admin user can edit, view,
and delete isolated feed items.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is
the URL and this field is the link name. The `Title` field can be updated on posts
of `Type QuestionPost` .


Standard Objects FeedItem

**Field Name** **Details**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`,
`QuestionPost`, and `TextPost`, all the FeedItem types listed here are
system-generated. In most situations, we recommend that you don't create
system-generated fields using Apex or our APIs. One exception is during Chatter
data migrations, which can require admins to migrate system-generated post
types.

**•** `ActivityEvent` —indirectly generated event when a user or the API
adds a Task associated with a feed-enabled parent record (excluding email
tasks on cases). Also occurs when a user or the API adds or updates a Task or
Event associated with a case record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the
series only. For a recurring Task with CaseFeed enabled, events are generated
for the series and each occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement
and, in Lightning Experience as of API version 39.0 and later, when a user
shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a
public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from
the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric
or gauge exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a
dashboard snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter
profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.


Standard Objects FeedItem

**Field Name** **Details**

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post.
Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply
only to CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an
article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through
the user interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment
for a case object.

**•** `ChangeStatusPost` —generated event when a user changes the status
of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved
to a case.

**•** `EmailMessageEvent` —generated event when an email related to a
case object is sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a
case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or
reaches violation status.

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData`
and `ContentFileName` .

```
Visibility

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is available to all users or internal users only. This
field is available in API version 26.0 and later, if digital experiences is enabled for
your org.

`Visibility` can have the following values:

**•** `AllUsers` —The feed item is available to all users who have permission
to see the feed item.

**•** `InternalUsers` —The feed item is available to internal users only.

Note the following exceptions for `Visibility` :


Standard Objects FeedItem

**Field Name** **Details**

**•** For record posts, `Visibility` is set to `InternalUsers` for all internal
users by default.

**•** External users can set `Visibility` only to `AllUsers` .

**•** `Visibility` can be updated on record posts.

**•** The `Update` property is supported only for feed items posted on records.

Usage

**•** When a feed item’s `IsClosed` field is set to true, some actions are blocked and others are blocked to most users. This table sets
out the actions that are blocked when a feed item is closed.


Standard Objects FeedItem

**•** This Apex example shows how to add a feed item with an attachment to a lead using API version 36.0 and later. First, post a feed
item.

```
     //create and insert post

     FeedItem post = new FeedItem();

     post.Body = 'HelloThere';

     post.ParentId = ' ID_OF_LEAD_ENTITY ';

     post.Title = ' FileName ';

     insert post;

```

Then insert the attachment.

```
     //create and associate a content attachment to the post

     FeedAttachment feedAttachment = new FeedAttachment();

     feedAttachment.FeedEntityId = post.Id;

     feedAttachment.RecordId = ' ID_OF_CONTENT_VERSION ';

     feedAttachment.Title = ' FileName ';

     feedAttachment.Type = 'CONTENT';

     insert feedAttachment;

```

**•** If you’re using API version 23.0 or later and have View All Data permission, you can directly query for a FeedItem. The following
example returns the 20 most recent feed items.

```
     SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName, CreatedBy.LastName, ParentId,

      Parent.Name, Body,

      (SELECT ID, FieldName, OldValue, NewValue FROM FeedTrackedChanges ORDER BY ID DESC)

     FROM FeedItem

     WHERE CreatedDate > LAST_MONTH

     ORDER BY CreatedDate DESC

```

**•** If you’re using an earlier API version than version 23.0, query FeedItem objects through a feed (such as AccountFeed or
OpportunityFeed). The following example returns all feed items for a given account, ordered by date descending:

```
     SELECT Id, Type, FeedItem.Body

     FROM AccountFeed

     WHERE ParentId = AccountId ORDER BY CreatedDate DESC

```

Note: Provide the `ParentId` for API version 22.0 and earlier.

**•** A feed item of type `UserStatus` is automatically created when a user adds a post to update the status. You can’t explicitly create
a feed item of type `UserStatus` .

**•** The FeedItem object doesn’t support aggregate functions in queries.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

**•** The size limit for an attachment on a feed is 2 GB.

**•** You can’t use the content fields to update or delete the content.

**•** You can’t filter or update the content fields.

**•** Deleting a feed item via the API also deletes the associated content. Likewise, undeleting a feed item restores associated content.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.


### Standard Objects FeedLike

**•** After uploading to a feed, it’s possible for an attachment or document to be deleted, marked private, or hidden by sharing rules. In
this case, all content fields in a FeedItem object appear as `null` in a SOQL query.

**•** You can’t explicitly create or delete a FeedTrackedChange record.

**•** Imagine that you insert a feed item or feed comment of `Type ContentPost` on a User or Group to create a file. Then the
`NetworkScope` field value of the feed item is passed to the file.

**•** If you use an Apex trigger to modify the `Body` of a FeedItem object, all mentions hyperlinks are converted to plain text. The mentioned
users don’t get email notifications.

**•** If you insert rich text into the feed item body, make sure that the case of the opening and closing HTML tags matches. For example,
`<b>This is bold text</B>` generates an error.

**•** To check file sharing with Apex triggers, write triggers on ContentDocumentLink instead of FeedItem. For an example, see
ContentDocumentLink.

**•** In API version 36.0 and later, use FeedAttachment to attach one or more content items to a feed item. As a result of support for
multiple attachments through FeedAttachment, all fields related to content attachments have been removed. These fields are:
`ContentData`, `ContentDescription`, `ContentFileName`, `ContentSize`, and `ContentType` .

**•** For all API versions of FeedItem, you can’t query a FeedItem object using the `System Modstamp` filter.

**•** When you use the FeedItem object to create a record-triggered flow, and the flow tries to update a field on the parent record, the
field may not update in the UI until the page is refreshed.

### FeedLike

Indicates that a user has liked a feed item. This object is available in API version 21.0 and later.

### FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API. A FeedLike is a

child object of an associated FeedItem, FeedTrackedChange, or object feed, such as AccountFeed.

Supported Calls

`create()`, `delete()`, `describeSObjects()`

Special Access Rules

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

Fields

**Field Name** **Details**

```
FeedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the feed item that the user liked.


### Standard Objects FeedPollChoice

**Field Name** **Details**

```
FeedEntityId

InsertedById

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of a feed item or feed comment the user liked.

If the user liked a comment, `FeedEntityId` is set to the ID of the comment. If the user
liked a feed item, `FeedEntityId` is set to the ID of the feed item.

This field is optional. The default value is the ID of the feed item.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

You can't query FeedLike records directly. They can only be queried via the entity feed, such as AccountFeed.

FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API.

### FeedPollChoice

Shows the choices for a poll posted in the feed. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects FeedPollChoice

Special Access Rules

To delete feed items they didn’t create, users must have one of these permissions:

**•** Modify All Data

**•** Modify All Records on the parent object, for example on Account for a poll on an AccountFeed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

Only users with this permission can delete items in unlisted groups.

Fields

**Field Name** **Details**

```
ChoiceBody

FeedItemId

Position

```

Usage

**Type**
textarea

**Properties**
Group

**Description**
A choice in the poll.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.

**Type**
int

**Properties**
Group, Sort

**Description**
Shows the position of the poll choice.

Use this object to query all of the choices associated with a particular poll. To view how people voted on the poll, see the FeedPollVote
object.


### Standard Objects FeedPollVote FeedPollVote

Shows how users voted on a poll posted in the feed. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ChoiceId

FeedItemId

```

Usage

**Type**
reference

**Properties**
Filter, Group

**Description**
Indicates which choice a user selected on a poll posted in a feed.

This is a relationship field.

**Relationship Name**
Choice

**Relationship Type**
Lookup

**Refers To**
FeedPollChoice

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.

Use this object to query how users voted on a particular poll.

### FeedPost FeedPost represents the following types of changes in a record feed, such as AccountFeed: text posts, link posts, and content posts. This

object is available in API version 18.0 through 21.0. FeedPost is no longer available in later versions. Starting with API version 21.0, use
FeedItem to represent text posts, link posts, and content posts in feeds.


Standard Objects FeedPost

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `search()`

Special Access Rules

You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**•** “Modify All Data”

**•** “Modify All Records” on the object associated with the feed and delete permission on the parent feed

**•** “Moderate Chatter”

Note: Users with the “Moderate Chatter” permission can delete only the feed items and comments they can see.

**•** Manage Unlisted Groups

Only users with this permission can delete items in unlisted groups.

Only users with the Modify All Data permission can delete a feed item of `Type TrackedChange` .

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

Fields

**Field** **Details**

```
Body

ContentData

ContentDescription

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the FeedPost. Required when `Type` is `TextPost` or
`AdvancedTextPost` . Optional when `Type` is `ContentPost` or `LinkPost` .

**Type**
base64

**Properties**
Create, Nillable

**Description**
This field is required if `Type` is `ContentPost` . Encoded file data in any format,
and can’t be 0 bytes. Setting this field automatically sets `Type` to `ContentPost` .

**Type**
string

**Properties**
Create, Nillable, Sort


Standard Objects FeedPost

**Field** **Details**

**Description**
The description of the file specified in `ContentData` .

```
ContentFileName

ContentSize

ContentType

FeedItemId

InsertedById

```

**Type**
string

**Properties**
Create, Group, Nillable, Sort

**Description**
This field is required if `Type` is `ContentPost` . The name of the file uploaded to
the feed. Setting `ContentFileName` automatically sets `Type` to
`ContentPost` .

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
This field is the size of the file (in bytes) uploaded to the feed. This field is read-only
and is automatically determined during insert.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
This field is the MIME type of the file uploaded to the feed. This field is read-only and
is automatically determined during insert.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed containing the FeedPost.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects FeedPost

**Field** **Details**

**Description**
ID of the user who added this item to the feed. For example, if an application migrates
posts and comments from another application into a feed, the `InsertedBy` value
is set to the ID of the context user.

```
IsDeleted

LinkUrl

ParentId

Title

Type

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not
( `false` ). This field is a standard system field.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort

**Description**
The URL of a `LinkPost` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the object type to which the FeedPost is related. For example, set this field to a
`UserId` to post to someone’s profile feed, or an `AccountId` to post to a specific
account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The title of the FeedPost. When the `Type` is `LinkPost`, the `Body` is the URL and
the `Title` is the label for the link.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects FeedRevision

**Field** **Details**

**Description**
The type of FeedPost:

**•** `UserStatus` —automatically generated when a user updates their status

**•** `TrackedChange` —ignore

**•** `TextPost` —a direct text entry on a feed

**•** `LinkPost` —a URL posting on a feed

**•** `ContentPost` —an uploaded file on a feed

Note: If you set `Type` to `ContentPost`, you must specify
`ContentData` and `ContentFileName` .

Usage

**•** You can’t directly query for a FeedPost. FeedPosts are always associated with a feed item, so you can query for them through the
feeds. The following example returns all feed items for a given account, ordered by date descending:

```
     SELECT Id, Type, FeedPost.Body

     FROM AccountFeed

     WHERE ParentId = AccountId ORDER BY CreatedDate DESC

```

**•** A FeedPost of type `UserStatus` is automatically created when a user adds a post to update the current status. You can’t explicitly
create a FeedPost of type `UserStatus` .

**•** The size limit for an attachment on a profile, news, or record feed is 2 GB.

**•** You can’t use the content fields to update or delete the content.

**•** You can’t filter or update the content fields.

**•** Deleting a FeedPost via the API also deletes the associated content and FeedPost objects. Likewise, undeleting a FeedPost restores
associated content and FeedPost objects.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.

**•** After uploading to a feed, it is possible for an attachment or document to be deleted, marked private, or hidden by sharing rules. In
this case, all content fields in FeedPost appear as `null` in a SOQL query.

**•** You can’t explicitly create or delete a FeedTrackedChange record.

### FeedRevision

Holds the revision history of a specific feed item or comment, including a list of attributes that changed for each revision. This object is
available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects FeedRevision

Fields

**Field Name** **Details**

```
Action

EditedAttribute

FeedEntityId

IsDeleted

IsValueRichText

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Holds the type of modification to the underlying feed item or comment attribute.
`Action` can have the value `Changed` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Identifies the part of the feed item or comment which was modified. A single
revision can have many edited attributes.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifies the modified feed item or comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not
( `false` ). This field is a standard system field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text
feed comment using SOAP API, set `IsRichText` to `true` and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:


Standard Objects FeedRevision

**Field Name** **Details**

**•** `<p>`

Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>` to
create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`

```
                         src="sfdc://069B0000000omjh"></img>

```

In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a
plain-text representation.

```
OriginNetworkId

Revision

Value

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site in which a user modified the feed item or
comment. This field is only available, if digital experiences is enabled for your
org.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item or comment.

**Type**
textarea

**Properties**
Nillable


### Standard Objects feedSignal

**Field Name** **Details**

**Description**
Identifies the value of the `EditedAttribute` field before the update.

Usage

This object tracks the changes made to a feed item or feed comment and stores a list of attributes that changed for each revision.

**•** To query the FeedRevision object, users need the View All Data permission or supply a WHERE clause on the `FeedEntityId` .

### feedSignal

Attach feed signals, like `UpDownVote`, `UserVerified`, and `Verified`, to a feed post or comment. This object is available in
API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`

Fields

**Field** **Details**

```
FeedEntityId

FeedItemId

InsertedById

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Feed entity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the feed post or comment.

Possible values are:

**•** `FeedItem`

**•** `FeedComment`

**Type**
reference


### Standard Objects FeedTrackedChange

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of user who inserted the signal.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

```
SignalType

SignalValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of signal.

Possible values are:

**•** `UpDownVote`

**•** `UserVerified`

**•** `Verified`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The value of the signal. For example, for `UpDownVote`, the value specifies whether the
signal is an upvote or a downvote.

### FeedTrackedChange

Represents an individual field change or set of field changes. A FeedTrackedChange is a child object of a record feed, such as AccountFeed.
This object is available in API version 18.0 and later.

Supported Calls

```
describeSObjects()

```


Standard Objects FeedTrackedChange

Fields

**Field** **Details**

```
CurrencyIsoCode

FeedItemId

FieldName

NewValue

OldCurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
currency code for the field, if `FieldName` is a currency field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent feed that tracks the field change.

**Type**
string

**Properties**
Group, Sort

**Description**
The name of the field that was changed.

Note: This field also tracks other events that are not related to an individual field for
a parent feed. These events occur as the parent record advances through its pipeline.
For example, a value of `leadConverted` indicates that a lead has been converted
to an opportunity. For a full list of values, see Tracking of Special Events.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
currency code for the `OldValue` field, if `FieldName` is a currency field.


Standard Objects FeedTrackedChange

**Field** **Details**

```
OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The last value of the field before it was changed.

A user can subscribe to a record or to another user. Changes to the record and updates from the users are displayed in the Chatter feed
on the user's home page, which is a useful way to stay up-to-date with other users and with changes made to records in Salesforce.
Feeds are available in API version 18.0 and later.

If you move a custom field to the Recycle Bin, all FeedTrackedChange records that track historical changes to the custom field are
automatically deleted and are not restored if the custom-field is undeleted.

The following sections outline the difference between standard feeds and custom feeds.

Standard Feeds

A standard feed is a record feed, such as AccountFeed. FeedTrackedChange records for standard feeds can only be queried via the parent
feed object.

Note the following when working with standard feed items:

**•** Feed items for standard feeds are read only in the API.

**•** A FeedTrackedChange record is visible when you have read access on the record feed, and when the field is visible in the field-level
security settings.

Custom Feeds

If you want more control over the information provided in a record feed, such as AccountFeed, you can create a custom feed. A custom
feed can replace or augment an existing record feed. For example, you might want to:

**•** Disable the standard account record feed and use an Apex trigger to generate FeedTrackedChange records for the events that you
want to track in the feed instead.

**•** Augment the standard contact record feed by writing an API client that inserts feed items for events that are not tracked in the
standard feed.

Tracking of Special Events

The `FieldName` field also tracks other events that are not related to an individual field for a parent feed. These events occur as the
parent record advances through its pipeline. For example, a value of `leadConverted` indicates that a lead has been converted to
an opportunity.

Valid values for the `FieldName` field for multiple objects:

**•** `created`


### Standard Objects FieldHistoryArchive

**•** `ownerAccepted`

**•** `ownerAssignment`

Additional valid values for the `FieldName` field for individual objects:

**Account**

**•** `accountCreatedFromLead`

**•** `accountMerged`

**•** `accountUpdatedByLead`

**•** `personAccountUpdatedByLead`

**Case**

**•** `closed`

**•** `ownerEscalated`

**Contact**

**•** `contactCreatedFromLead`

**•** `contactMerged`

**•** `contactUpdatedByLead`

**Contract**

**•** `contractActivation`

**•** `contractApproval`

**•** `contractConversion`

**•** `contractExpiration`

**•** `contractTermination`

**Lead**

**•** `leadConverted`

**•** `leadMerged`

**Opportunity**

**•** `opportunityCreatedFromLead`

SEE ALSO:

Custom Object__Feed

### FieldHistoryArchive Represents field history values for all objects that retain field history. FieldHistoryArchive is a big object, available only to users

with the “Retain Field History” permission. This object is available in API version 29.0 and later.

### Each instance of the FieldHistoryArchive object represents a single change in the value of a field. FieldHistoryArchive

stores history for both standard and custom fields.

### The Field field returns the name of the field unless the parent field or object is deleted, in which case it returns the field ID. You can

use the ID to retrieve the old field and object name from the `FieldNameAfterArchival` and `ParentNameAfterArchival`
fields, respectively.


Standard Objects FieldHistoryArchive

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
ArchiveFieldName

ArchiveParentName

ArchiveParentType

ArchiveTimestamp

CreatedById

```

**Type**
string

**Properties**
Nillable

**Description**
The name of the field at the time the data was archived. If the field name changed,
the name is sometimes not the same for all records related to a single field.

**Type**
string

**Properties**
Nillable

**Description**
The name of the parent object at the time the data was archived. If the object
name changed, the name is sometimes not the same for all records related to a
single field.

**Type**
string

**Properties**
Nillable

**Description**
The type of the field at the time the data was archived. If the field type changed,
the type is sometimes not the same for all records related to a single field.

**Type**
dateTime

**Properties**
Nillable

**Description**
The date and time at which the data was archived.

**Type**
reference

**Properties**
Nillable


Standard Objects FieldHistoryArchive

**Field Name** **Details**

**Description**
The user ID of the user who created the original record.

```
CreatedDate

Field

FieldHistoryType

```

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**
The date and time at which the original record was created.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The name of the field that was changed. If the field is deleted from the parent
object, the `Field` field contains the field ID instead.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The name of the object that contains the field history. Possible values are:

**•** `Account`

**•** `Article`

**•** `Asset`

**•** `AuthorizationFormConsent`  - Available in version 58.0 and later.

**•** `Case`

**•** `CommSubscriptionConsent`  - Available in version 58.0 and later.

**•** `Contact`

**•** `ContactPointConsent`  - Available in version 58.0 and later.

**•** `ContactPointTypeConsent`  - Available in version 58.0 and later.

**•** `Contract`

**•** `ContractLineItem`

**•** `Crisis`

**•** `Employee`

**•** `EmployeeCrisisAssessment`

**•** `Entitlement`

**•** `Individual`


Standard Objects FieldHistoryArchive

**Field Name** **Details**

**•** `InternalOrganizationUnit`

**•** `Knowledge`

**•** `Lead`

**•** `Opportunity`

**•** `Order`

**•** `OrderItem`

**•** `PartyConsent`                       - Available in version 58.0 and later.

**•** `Pricebook2`

**•** `PricebookEntry`

**•** `Product2`

**•** `ServiceAppointment`

**•** `ServiceContract`

**•** `Solution`

**•** `WorkOrder`

**•** `WorkOrderLineItem`

```
HistoryId

Id

NewValue

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the relevant history object (for example, AccountHistory). This field is
available in versions 42.0 and later.

**Type**
ID

**Properties**
Defaulted on create, Filter, idLookup

**Description**
The ID of the archived record. It’s useful to have a field’s ID for fields that you’ve
deleted. (Field names aren’t retained in history when you delete fields from
Salesforce.)

**Type**
anyType

**Properties**
Nillable

**Description**
The new value of the modified field.


### Standard Objects FieldChangeSnapshot

**Field Name** **Details**

```
OldValue

ParentId

```

Usage

When sorting fields, order them as follows:

**1.** `FieldHistoryType ASC`

**2.** `ParentID ASC`

**3.** `CreatedDate DESC`

SEE ALSO:

**Type**
anyType

**Properties**
Nillable

**Description**
The previous value of the modified field.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the object that contains the field (the parent object).

_Developer Guide:_ [Big Objects Implementation Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.bigobjects.meta/bigobjects/big_object.htm)

### FieldChangeSnapshot

Use this virtual object to learn which opportunities' close dates changed during the specified time period. This object is available in API
version 52.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To use FieldChangeSnapshot, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.


Standard Objects FieldChangeSnapshot

Fields

**Field** **Details**

```
CurrentValueDateOnly

FieldName

ParentId

ValidFrom

ValidTo

```

**Type**
date

**Properties**
Filter, Group, Nillable

**Description**
The current value of a date field on the opportunity.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the field to get the change history for. Possible values are:

**•** `CloseDate`

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity to get the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time that specifies the beginning of the time period.

**Type**
dateTime


### Standard Objects FieldPermissions **Field Details**

**Properties**
Filter

**Description**
The date and time that specifies the end of the time period.

Usage

Use FieldChangeSnapshot to learn about the first change made to the specified opportunity during the specified time period. Subsequent
changes are not returned.

Example: Suppose that last week you changed an opportunity's close date to June 1, 2021. Assuming the opportunity had the
ID '006R0000XXXXXXXXXX', the following query would return the `CurrentValueDateOnly` of June 1, 2021:

```
      Select CurrentValueDateOnly from FieldChangeSnapshot where ParentID =

      '006R0000XXXXXXXXXX' and FieldName = 'CloseDate' and ValidTo = LAST_WEEK AND ValidFrom

      = LAST_WEEK and CurrentValueDateOnly < 2021-07-01

### FieldPermissions

```

Represents the enabled field permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

To grant a user access to a field, associate a FieldPermissions record with a PermissionSet that’s assigned to a user. FieldPermissions
records are only supported in PermissionSet, not in Profile.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, only users with the View Setup and Configuration permission can access this object.

Fields

In API version 50.0 and later, for lookup field inserts and queries, you can leave off the Id in the field name or include it. The rows returned
always use the API name. For example:

```
   SELECT SobjectType, Field

   FROM FieldPermissions

   WHERE Field='Contact.Account'

```

and

```
   SELECT SobjectType, Field

   FROM FieldPermissions

   WHERE Field='Contact.Account Id '

```


Standard Objects FieldPermissions

both return

```
   Contact, Contact.AccountId

```

**Field Name** **Details**

```
Field

ParentId

PermissionsEdit

PermissionsRead

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field’s API name. This name must be prefixed with the `SobjectType` . For example,

```
  Merchandise__c.Description__c

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The `Id` of the field’s parent PermissionSet.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit this field. Requires
`PermissionsRead` for the same field to be `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view this field. A FieldPermissions
record must have at minimum `PermissionsRead` set to `true`, or it will be deleted.


Standard Objects FieldPermissions

**Field Name** **Details**

```
SobjectType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object’s API name. For example, `Merchandise__c` .

FieldPermissions work similarly to ObjectPermissions. However, FieldPermissions includes a `Field` attribute to return the name of the
field.

For example, the following query returns all FieldPermissions records that have at least the “Read” permission. The results include the
field, object, and permission set names.

```
SELECT SobjectType, Field, PermissionsRead, Parent.Name

FROM FieldPermissions

WHERE PermissionsRead = True

```

Include the field’s parent object when querying FieldPermissions. For example, to find all rows that match the Account object’s `Type`
field, create the following query:

```
SELECT Id, SobjectType, Field

FROM FieldPermissions

WHERE Field = 'Account.Type' AND SobjectType = 'Account'

```

To find which permission sets are backed by profiles with the Account object, you can use a query like the following example:

```
SELECT Id, ParentId, SobjectType, Field, PermissionsEdit, PermissionsRead, Parent.Name

FROM FieldPermissions

WHERE SobjectType = 'Account' and Parent.IsOwnedByProfile = true

ORDER BY SObjectType, Field

```

Both `SobjectType` and `Field` must be included in the `SELECT` line of the query. Provide the full API name of the field in the
form of `SobjectType.Field` when querying for a field.

Note: When using the FieldPermission object to download records, depending on the SOQL query you use, you might not receive
all expected records. Results can also appear incomplete. However, all records do download; fields that don't support field security
and rows for entities not visible to the org are hidden.

Special Properties for Field Permissions

The auto-number and formula fields have special rules for how field permissions work. Both have FieldPermissions records, but inserting
and updating is limited to `PermissionsRead` . `PermissionsEdit` isn’t allowed for either field type, since these fields must be
read-only for users.

The following field types don’t return a FieldPermissions record because they are assumed to always be readable.

**•** `Id`

**•** `CreatedById`


Standard Objects FieldPermissions

**•** `CreatedDate`

**•** `IsDeleted`

**•** `LastModifiedById`

**•** `LastModifiedDate`

**•** `SystemModStamp`

The following field types don’t return a FieldPermissions record because they are assumed to always be readable and writable.

**•** `OwnerId`

**•** Master-detail custom (relationship) fields

**•** Universally required custom fields

As a result, the following query returns no records, even though users do have some access to some of the fields.

```
   SELECT Field, SobjectType, PermissionsRead

   FROM FieldPermissions

   WHERE Field='Id'

```

To determine if a field can return a FieldPermissions record, you can call a `describeSObject()` on the field. For example,
`describeSObject('Merchandise__c')`, returns all the properties of the Merchandise custom object, including field properties.
If you use a field whose `permissionable` property is `false` (like the field types listed in this section), you can’t query, insert,
update, or delete field permissions records, because they don’t exist.

If the View All Fields object permission is enabled for an object in the permission set, the `PermissionsRead` field equals `true`
for all queried fields for that object.

Working with Custom Activity Fields

While tasks and events are considered separate objects, they share a common set of activity custom fields. As a result, when a custom
task field is created, a custom event field is also created, and vice versa. You can display the custom field on the event layout, task layout,
or both event and task layouts.

Although custom activity fields are shared between tasks and events, you see separate FieldPermissions records for the task and event.
However, changes made to one field permission record are automatically made to the other. For example, if you create a custom activity
field, assign field permissions to it in a permission set, and run the following query, the query returns two records with the same permission
value.

```
   SELECT Field, Id, ParentId, PermissionsEdit, PermissionsRead, SobjectType

   FROM FieldPermissions

   WHERE SobjectType = 'event' OR SobjectType ='task'

```

If you then update one of the records with another set of field permission values and run the query, the same permission values for both
records are returned.

Nesting Field Permissions

You can nest FieldPermissions in a PermissionSet query. For example, the following returns any permission sets where “Edit Read Only
Fields” is `true` . Also, the result set includes both the “Read” and “Edit” field permission on the Merchandise object. Get similar results
by nesting the SOQL with a field permission query using the relationship name for field permissions: `FieldPerms` .

```
   SELECT PermissionsEditReadonlyFields,

   (SELECT SobjectType, Field, PermissionsRead, PermissionsEdit

   FROM FieldPerms

```


Standard Objects FieldPermissions

```
   WHERE SobjectType = 'Merchandise__c')

   FROM PermissionSet

   WHERE PermissionsEditReadonlyFields = true

```

As a result, it’s possible to traverse the relationship between the PermissionSet and any child-related objects (in this case, FieldPermissions).
You can do this from the PermissionSet object by using the child relationship ( `ObjectPerms`, `FieldPerms`, and so on) or from
the child object by referencing the PermissionSet with `Parent.` _**`permission_set_attribute`**_ .

It’s important to consider when to use a conditional `WHERE` statement to restrict the result set. To query based on an attribute on the
permission set object, nest the SOQL with the child relationship. However, to query based on an attribute on the child object, you must
reference the permission set parent attribute in your query.

The following two queries return the same columns with different results, based on whether you use the child relationship or parent
notation.

```
   SELECT PermissionsEditReadonlyFields,

   (SELECT SobjectType, Field, PermissionsRead, PermissionsEdit

   FROM FieldPerms

   WHERE SobjectType = 'Merchandise__c')

   FROM PermissionSet

   WHERE PermissionsEditReadonlyFields = true

```

Versus:

```
   SELECT SobjectType, Field, PermissionsRead, PermissionsEdit, Parent.Name,

     Parent.PermissionsEditReadonlyFields

   FROM FieldPermissions

   WHERE SObjectType='Merchandise__c'

```

Muting Permissions

Field permissions with a parent muting permission set act differently than those enabled in a regular permission set. For a regular
permission set, if a FieldPermissions record grants full access to a field (for example, granting read and edit access), users have full access
to that field.

With muting permission sets, a FieldPermissions record defines the muting of access. So if a muting permission set is set for read and
edit, the read and edit access is muted.

For example, we have a permission set and a muting permission set that controls access to the Account object’s fields. Each permission
set has settings for the Website field.

Regular Permission Set

**Field** **PermissionsRead** **PermissionsEdit** **Result**

Account.Website `true` `false` The Account.Website field is
read only.

Account.Website `true` `true` The Account.Website field has
both read and edit permissions.

Muting Permission Set


### Standard Objects FieldSecurityClassification **Field PermissionsRead PermissionsEdit Result**

Account.Website `false` `true`

Account.Website `true` `true`

Edit permissions on the
Account.Website fields are
muted.

Read and edit permissions on
the Account.Website field are
muted.

Field permissions are aggregated by combining the permissions granted by the permission set and the permissions muted by the muting
permission set. For example, if you have a permission set that grants read and edit permissions for a field, and a muting permission that
mutes the same field’s edit permission, the result is that only the read permission is enabled.

SEE ALSO:

PermissionSet

ObjectPermissions

### FieldSecurityClassification

Represents a field’s data sensitivity value selected from the SecurityClassification picklist. This object is available in API version 46.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To view this object, you need the Customize Application or Modify Data Classification permission.

Fields

**Field Name** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential


Standard Objects FieldSecurityClassification

**Field Name** **Details**

**•** Restricted

**•** MissionCritical

```
Description

IsHighRiskLevel

MasterLabel

SortOrder

```

Usage

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the data sensitivity picklist value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your
company.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential

**•** Restricted

**•** MissionCritical

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the picklist.

Use this object to return information about data sensitivity values in the SecurityClassification picklist. This object is read-only, but you
[can update the SecurityClassification picklist using the StandardValueSet Metadata API type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_standardvalueset.htm)


### Standard Objects FieldServiceMobileSettings FieldServiceMobileSettings

Represents a configuration of settings that control the Field Service iOS and Android mobile app experience. This object is available in
API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AscAutomaticMode

```

AscCancellationTimerInSec

AscCompletedStatus

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes how status changes are handled. Possible values are:

**•** `Off` —No automatic status changes.

**•** `Manual` —The mobile worker can cancel or update the status change.

**•** `Timed` —The mobile worker has a time period to prevent the status change.
When the timer ends, the status changes.

**•** `Automated` —The mobile worker is notified that the status has changed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
For the Timed mode only. Time that the user has to cancel the appointment
status change.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
Status that indicates that a mobile worker completed a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

```
AscOnSiteStatus

AscRadiusInMeters

AscTimeLimitationInMin

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is at a service appointment. Possible
values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Service appointment radius that can trigger a status change.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
A time period when status changes can occur, before an appointment’s scheduled
start time and after the scheduled end time. The time is applied only if
IsAscTimeLimitEnabled is `true` .

```
AscTravelStatus

BgGeoLocationAccuracy

BgGeoLocationMinUpdateFreqMins

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is traveling to a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of geolocation tracking of services resources while the app is running
in the background. Lowering accuracy reduces battery consumption for mobile
devices. Available in API version 41.0 and later. Picklist options:

**•** `Medium` —Accurate to within about 100 meters.

**•** `Coarse` —Accurate to within about 1 kilometer.

**•** `Very Coarse` —Accurate to within about 3 kilometers.

The default value is `Coarse` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The frequency of geolocation poling of services resources while the app is running
in the background. Less frequent poling decreases battery consumption for


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

mobile devices. The label in the UI is **Minimum Update Frequency of Geo**
**Location in Minutes (Background)** . Available in API version 41.0 and later.

```
BrandInvertedColor

ContrastInvertedColor

ContrastPrimaryColor

ContrastQuaternaryColor

ContrastQuinaryColor

ContrastSecondaryColor

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of toasts and the contrast color of the floating action button.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary text.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary lines that delineate different areas of the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
The color of secondary text.

```
ContrastTertiaryColor

DaysBeforeCurrentServiceDate

DayAfterCurrentServiceDate

DefaultListViewDeveloperName

```

DestinationType

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the icons on the settings screen and of primary lines that delineate
different areas of the UI.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days before the current service date during which to prime service documents
for offline use.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days after the current service date during which to prime service documents for
offline use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the default service appointment list view on the schedule screen.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines if the mobile worker navigates to the destination based on the address
or based on the latitude and longitude. Possible values are:

**•** `Address`


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**•** `Latitude and Longitude`

The default value is `Address` .

```
DeveloperName

FeedbackPrimaryColor

FeedbackSecondaryColor

FeedbackSelectedColor

FutureDaysInDatePicker

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the set of field service mobile settings.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of error messages.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of success messages.

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The color indicating the user’s current selection.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the future that a user can select from the date picker
on the schedule screen.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
GeoLocationAccuracy

GeoLocationMinUpdateFreqMins

IsAscTimeLimitEnabled

IsAssignmentNotification

IsDefault

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of service resource geolocation tracking. Lowering accuracy reduces
battery consumption for mobile devices. Picklist values:

**•** `Fine` —Accurate to within 10 meters.

**•** `Medium` —Accurate to within 100 meters.

**•** `Coarse` —Accurate to within 1 kilometer.

The default value is `Medium` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to poll geolocation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether AscTimeLimitationInMin is applied. Default is `true`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is assigned the appointment. Default is `false` . This field is available
in API version 46.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
Indicates that the set of field service mobile settings is the default set that is
automatically assigned to users. You can’t make a different settings record the
default, but you can modify the default settings record. Default is `false` .
Available in API version 41.0 and later.

```
IsDispatchNotification

```

IsLimitedLocTrackingEnabled

IsOptimizedImageUploadEnabled

```
IsScheduleViewResourceAbsences

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is dispatched for the appointment. Default is `false` . This field is
available in API version 46.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When limited tracking for Appointment Assistant is enabled, the mobile worker’s
location is shown only on the way to a service appointment. The default value
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to configure the size of images uploaded by your mobile
workers. To optimize upload speeds, you can limit your file size to a defined
maximum size using the OptimizeImageSizeInMb field. Resizing your images
affects the resolution of your images. The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether resource absences appear in the Schedule tab of the mobile
app. This field is available in API version 55.0 and later.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
IsSendLocationHistory

IsShowEditFullRecord

IsTimeSheetEnabled

IsTimeZoneEnabled

IsUseSalesforceMobileActions

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether geolocation tracking of services resources is enabled. Default
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can edit records with the field service mobile app. Default
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can access time sheets on their mobile devices (Beta).
Default is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether the time zone of timesheet entries on the mobile app is
recorded. The current time zone is recorded in the `LocationTimeZone` field
of the TimeSheetEntry object. Default is `false` . Available in API version 50.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
Language

MasterLabel

MaxNumberOfServiceAppointments

MetadataCacheTimeDays

NavbarBackgroundColor

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The localization preference for a user. The format is a two letter language code
and, if there’s a dialect, followed by the two letter dialect, for example, `fr` for
French, and `fr_BE` for Belgian French

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label in the UI for the set of field service mobile settings. Available in API
version 41.0 and later.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Sets the maximum number of service appointments to use for offline priming
of service documents. If you don’t have dates on your service appointments, this
setting helps to optimize offline priming in place of
`DaysBeforeCurrentServiceDate` and
`DaysBeforeCurrentServiceDate` fields.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days that org metadata, such as layouts, is kept in the app’s local
cache of memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the top bar in the app.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
NavbarInvertedColor

```

OptimizeImageSizeInMb

```
PastDaysInDatePicker

PrimaryBrandColor

QuickStatusChangeFlowName

```

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The secondary color of the tap bar in the app.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Configure the size of images uploaded by your mobile workers. To optimize
upload speeds, you can limit your file size to a defined maximum size. Resizing
your images affects the resolution of your images. Enter 0.2 or higher. Used only
if IsOptimizedImageUploadEnabled is `true` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the past that a user can select from the date picker on
the schedule screen.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The main branding color used throughout the UI.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of an existing Field Service flow with a Quick Status Change action to
change the work order or service appointment status or both. This applies to
flows invoked on the mobile app only. This field is available in API version 51.0
and later.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
RecordDataCacheTimeMins

SecondaryBrandColor

TimeIntervalSetupMins

UpdateScheduleTimeMins

```

Usage

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of minutes that record data is kept in the app’s local cache of
memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of action buttons.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls the spacing of picklist options for time values such as when creating
resource absences.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to update a user’s
schedule.The user’s schedule might not refresh on this cadence if the user’s
device isn’t connected to a network or doesn’t have adequate battery life.

Field Service Mobile settings allow you to create sets of settings to apply to different field service mobile users. The settings apply to
both the Android and iOS versions of the app.

For example, suppose you want to accommodate workers that are color blind, or who work in dark or bright conditions. You can choose
different branding options for different workers to suit their needs, and assign them to their profiles.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects FieldServiceOrgSettings

**FieldServiceMobileSettingsChangeEvent (API version 55.0)**
Change events are available for the object.

### FieldServiceOrgSettings

Represents the org settings for Field Service, such as Appointment Assistant settings. If Field Service is enabled, the org contains one
read-only record of this object. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, Field Service must be enabled. For specified fields in the table, Appointment Assistant must also be enabled.

Fields

### **Field Details**

```
ApptAssistantExpiration

ApptAssistantInfoUrl

ApptAssistantRadiusUnit

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expiry time in minutes of when the customer stops seeing the mobile worker’s location.
Appointment Assistant must also be enabled to see this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The page URL that enables Appointment Assistant. Appointment Assistant must also be
enabled to see this field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of the radius of the service appointment that prompts the Last Mile event for
Appointment Assistant. Appointment Assistant must also be enabled to see this field.


Standard Objects FieldServiceOrgSettings

**Field** **Details**

Possible values are:

**•** `Kilometer`

**•** `Meter`

**•** `Mile`

**•** `Yard`

```
ApptAssistantRadiusValue

ApptAssistantStatus

CanPopulateGoogleAddress

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The radius of the service appointment that prompts the Last Mile event for Appointment
Assistant. Appointment Assistant must also be enabled to see this field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The value that prompts the En Route event for Appointment Assistant. Appointment Assistant
must also be enabled to see this field.

Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**•** `TestSharing`

The default value is 'None'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows desktop and mobile to send geolocation and map data to Google and Apple. Available
in API version 57.0 and later.

The default value is `true` .


Standard Objects FieldServiceOrgSettings

**Field** **Details**

```
CanSendAppCenterCrashReports

CanStoreMobileAnalytics

DeveloperName

DoesAvlCalcInclOvertime

DoesAvlCalcInclPrimOnly

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows Salesforce to send crash reports to Microsoft App Center. Available in API version 57.0
and later.

The default value is `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows third parties to store mobile analytics. Available in API version 57.0 and later.

The default value is `true` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether overtime is included in work capacity availability calculations. Available
in API version 59.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects FileSearchActivity

**Field** **Details**

**Description**
Specifies if primary members only are included in work capacity availability calculations. If
the value is `false` both primary and secondary members of the service territory are
included. Available in API version 59.0 and later.

The default value is `false` .

```
Language

MasterLabel

### FileSearchActivity

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the field service org settings.

The format for the values is a two-letter language code in small letters, for example, `fr` for
French. If the language has regional dialects, add the two-letter country code in capital
letters, for example, use `fr_BE` for Belgian French.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the field service org settings.

Represents search activity on a file. This object is available in API version 38.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AvgNumResults

```

**Type**
double

**Properties**
Filter, Sort


Standard Objects FileSearchActivity

**Field** **Details**

**Description**
The number of search results returned for the search term. If Period is also included, this
value is aggregated based on the time period specified.

```
ClickRank

CountQueries

CountUsers

Name

Period

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that the file appeared in the search results when users clicked it from the list of
results.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of searches for the period (day, month, or year).

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of individual users who clicked the file.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of search activity.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The time period that the search count is applied to. For example, a record where the Count
is 70 and the Period is Monthly indicates that 70 searches took place over the past month.
Totals are aggregated daily for the current month, monthly from the past full month through
the past full year, and yearly beyond that.


### Standard Objects FiscalYearSettings

**Field** **Details**

Possible values are:

**•** `DAY`

**•** `MONTH`

**•** `YEAR`

```
QueryDate

QueryLanguage

SearchTerm

### FiscalYearSettings

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date of the search.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language filter that’s applied to the user’s search.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first 100 characters of the search term that was used to search published files.

Settings to define a custom or standard fiscal year for your organization. This object has a parent-child relationship with the Period object.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only partner users and standard users can access this object.


Standard Objects FiscalYearSettings

Fields

**Field** **Details**

```
Description

EndDate

IsStandardYear

Name

PeriodId

PeriodLabelScheme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the setting.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the fiscal year.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fiscal year is a standard calendar year ( `true` ) or a custom fiscal year
( `false` ).

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A name for the fiscal year. Limit: 80 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated fiscal period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects FiscalYearSettings

**Field** **Details**

**Description**
The numbering scheme used for fiscal periods.

```
PeriodPrefix

QuarterLabelScheme

QuarterPrefix

StartDate

WeekLabelScheme

WeekStartDay

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal periods. For example, if `p` is the prefix, then the first period is “P1.”

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for fiscal quarters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal quarters. For example, if “Q” is the prefix, then the fourth quarter would
be “Q4.”

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**

Start date of the fiscal year.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for weeks.

**Type**
int


### Standard Objects FldSvcObjChg

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the day that starts the week, for example `Monday` or `Sunday`

```
YearType

```

SEE ALSO:

Period

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates one of two types of fiscal years, Standard or Custom. Standard denotes the standard
Gregorian calendar, while Custom means a fiscal year with a custom structure.

Overview of Salesforce Objects and Fields

### FldSvcObjChg

Represents a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Field Service must be enabled.

**•** The Field Service managed package must be installed.

**•** The **Track the lifecycle of service appointments** setting in **Setup** - **Field Service Settings** must be enabled.

**•** The Platform Integration User must have the Manage Service Appointment Lifecycle and the View Service Appointment Lifecycle
permissions.

**•** To view this object, users must have the View Service Appointment Lifecycle user permission.

Fields

**Field** **Details**

```
Activity

```

**Type**
picklist


Standard Objects FldSvcObjChg

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The available scheduling activities for the service appointment.

Possible values are:

**•** `AddedToBundle` —Currently not supported

**•** `BundleMemberAdded` —Currently not supported

**•** `BundleMemberRemoved` —Currently not supported

**•** `Created`

**•** `Deleted`

**•** `RemovedFromBundle` —Currently not supported

**•** `Rescheduled` —An appointment is considered rescheduled if a change is made to
its assigned service resource or to its scheduled start time.

**•** `Scheduled`

**•** `ServiceResourceAssigned`

**•** `StatusChanged` —The service appointment status was changed. The manual activities
of scheduling, rescheduling, and unscheduling are also reported as status changes
because they change the status of an appointment.

**•** `Unscheduled`

**•** `Updated` —Captures changes made to one or more of the tracked scheduling fields
that aren’t associated with another activity.

```
ActivityDetails

ActivityTimeStamp

IsPrimary

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Details about the scheduling activity such as the scheduling policy that was used and the
unscheduling reason (when applicable).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time of when the change to the service appointment was made.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FldSvcObjChg

**Field** **Details**

**Description**
Indicates whether the change was made directly to the service appointment or indirectly. If
the change was made directly to the appointment, it’s flagged as Primary. If it was made to
another appointment and affected this one, it’s flagged as Secondary.

```
OriginalSvcAppointment

ServiceAppointmentId

TimeZone

Transaction

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the service appointment that was changed. The field value isn’t deleted when the
Service Appointment object is deleted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the service appointment that was changed. Because this is a relationship field, the
field value is deleted when the Service Appointment object is deleted.

This field is a relationship field.

**Relationship Name**
ServiceAppointment

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone of the service appointment or the assigned resource.

**Type**
string

**Properties**
Filter, Nillable, Sort


### Standard Objects FldSvcObjChgDtl

**Field** **Details**

**Description**
The last transaction ID of the scheduling and optimization request that updated this object.
The transaction ID is automatically generated and populated by the Enhanced Scheduling
and Optimization engine.

```
UserId

```

SEE ALSO:

### FldSvcObjChgDtl FldSvcObjChgDtl

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who made the change to the service appointment. If an activity is a scheduled job,
it’s registered with the System Administrator user who configured it.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents the details of a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0 and
later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Field Service must be enabled.

**•** The Field Service managed package must be installed.

**•** The **Track the lifecycle of service appointments** setting in **Setup** - **Field Service Settings** must be enabled.

**•** The Platform Integration User must have the Manage Service Appointment Lifecycle and the View Service Appointment Lifecycle
permissions.

**•** To view this object, users must have the View Service Appointment Lifecycle user permission.


### Standard Objects FlexQueueItem

Fields

**Field** **Details**

```
FieldChangedName

FieldChangedValue

FldSvcObjChgId

```

SEE ALSO:

FldSvcObjChg

### FlexQueueItem

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the field that was changed.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The updated value of the field that was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The parent record associated with the details of the change. The parent record has multiple
detail records associated with it. Each record includes the name and the current value of the
tracked fields.

This field is a relationship field.

**Relationship Name**
FldSvcObjChg

**Relationship Type**
Lookup

**Refers To**
FldSvcObjChg

Represents an asynchronous Apex job in the Apex flex queue. Provides information about the job type and flex queue position of the
AsyncApexJob. This object is available in API version 36.0 and later.


Standard Objects FlexQueueItem

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
AsyncApexJobId

FlexQueueItemId

JobPosition

JobType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of an AsyncApexJob that’s waiting in the flex queue.

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary key for this FlexQueueItem.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The position in the flex queue of the waiting job. The highest-priority job in the
queue is at position 0.

**Type**
picklist


### Standard Objects FlowDefinitionView

**Field Name** **Description**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of the job. Valid values are:

**•** `ApexToken`

**•** `BatchApex`

**•** `BatchApexWorker`

**•** `Future`

**•** `Queueable`

**•** `ScheduledApex`

**•** `SharingRecalculation`

**•** `TestRequest`

**•** `TestWorker`

Currently, queries are supported only on `BatchApex` jobs.

Usage

To find the position of an AsyncApexJob in the flex queue, query `JobPosition` . For example:

```
   SELECT JobPosition FROM FlexQueueItem WHERE JobType = 'BatchApex' AND AsyncApexJobId =

   '707xx000000DABC'

```

To find the job at a given position, query `AsyncApexJobId` . For example:

```
   SELECT AsyncApexJobId FROM FlexQueueItem WHERE JobType = 'BatchApex' AND JobPosition = '2'

```

To find all batch jobs in the flex queue, query `JobType` . To get other information about the jobs, include AsyncApexJob in your query.
For example:

```
   SELECT JobType, JobPosition, AsyncApexJob.ApexClass.Name, AsyncApexJob.CreatedDate,

      AsyncApexJob.CreatedById FROM FlexQueueItem WHERE JobType='BatchApex' AND

      AsyncApexJob.ApexClass.Name LIKE '%BatchAJob%' ORDER BY JobPosition DESC

### FlowDefinitionView

```

Represents the description of a flow definition. This object is available in API version 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects FlowDefinitionView

Fields

**Field** **Details**

```
ActiveVersionId

ApiName

ApiVersion

AreMetricsLoggedToDataCloud

Builder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow definition.

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Possible values are:

**•** Cloud Flow Designer

**•** Flow Builder

**•** Swing Designer


Standard Objects FlowDefinitionView

**Field** **Details**

This field is available in API version 47.0 and later.

```
CapacityCategory

Description

DurableId

Environments

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow definition information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow definition.

**Type**
multipicklist

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default` —The flow can run from a Visualforce component, Lightning page,
flow action, or custom Aura component.

**•** `Offline` —The flow can run only offline. Flow types that support offline flows
must set this value. This value is available in API version 62.0 and later.

**•** `Slack` —The flow can run in Slack and the default environment. You specify
the Slack flow environment when you save the flow.

This field is available in API version 55.0 to 62.0. This field is deprecated in API version
63.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

```
HasAsyncAfterCommitPath

InstalledPackageName

IsActive

IsOutOfDate

IsOverridable

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the scheduled path runs asynchronously after a save. The default
value is false. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the installed package that includes this flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the latest version of the flow definition is the active flow version.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the active flow version is the latest version of the flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is overridable. The default value is false. This field is available
in API version 53.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

```
IsSwingFlow

IsTemplate

Label

LastModifiedBy

LatestVersionId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. The default value is `false` .
When installed from managed packages, subscribers can’t view or clone processes
or flows because of intellectual property (IP) protection. But when those processes
and flows are templates, subscribers can open them in a builder, clone them, and
customize the clones.

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who last updated this flow definition.

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the latest flow version, regardless of the flow’s status.


Standard Objects FlowDefinitionView

**Field** **Details**

```
ManageableState

NamespacePrefix

OverriddenById

OverriddenFlowId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the flow that is contained in a package. Possible
values are:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow definition.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The flow that’s overriding the current flow. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string


Standard Objects FlowDefinitionView

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The flow that the current flow is overriding. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

```
ProcessType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s executed when a
user completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This
value is available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API
version 44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for an approval process.
This value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request to be contacted
by customer support. This flow is used to create contact request records. This
value is available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate
survey questions with different stages in customer lifecycles. This value is available


Standard Objects FlowDefinitionView

**Field** **Details**

in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent` —A process that is invoked when it receives a platform event
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow`                     - In the UI, Data Capture flows configure the Form tab
in the Field Service mobile app. When the Data Capture flow is launched, its Flow
metadata is publicly available in JavaScript format. This value is available in API
version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `EvaluationFlow` —A flow for evaluating custom entry and exit conditions
in an orchestration. Uses the `isOrchestrationConditionMet` output
variable and discards values from any other output variables. This value is available
in API version 54.0 and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value
is available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more
screens or local actions, choices, or dynamic choices. In the UI and Salesforce
Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is
available in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration
and updates for single sign-on with the authentication provider framework.
Available in API version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow` —A flow that associates individuals
with interactions such as voice calls, messaging sessions, or case-related emails.
This value is available in API version 58.0 and later.

**•** `InvocableProcess` —A process that another process or the Invocable
Actions resource in REST API invokes. This value is available in API version 38.0
and later.

**•** `Journey` —An audience-driven flow for Marketing Cloud. This value is available
in API version 57.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

**•** `LoginFlow` —A flow for login. This value is available in API version 51.0 and
later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app that’s
invokable by loyalty program processes. This value is available in API version 54.0
and later.

**•** `Orchestrator` —An orchestration that organizes flows into groups of steps
contained in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder
and the flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy` —Build recommendations for your users. A
recommendation launches its assigned flow. This value is available in API version
[54.0 and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=platform.nba_building_flow_builder_strategy.htm&type=5&language=en_US)

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business
logic. This value is available in API version 52.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created
in Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper.
From the UI, this type of flow is created in the Survey Builder and requires an
associated survey flow type. This value is available in API version 49.0 or later and
only when the Customer Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In
the UI and Salesforce Help, it’s a record change process.

These values are reserved for future use:

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

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that


Standard Objects FlowDefinitionView

**Field** **Details**

the flow contains only the elements, resources, and functionality that the new flow type
supports.

```
RecordTriggerType

SourceTemplateId

SupportedEnvironments

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies what type of record changes can start the flow. Possible values are:

**•** `Create`

**•** `CreateAndUpdate`

**•** `Delete`

**•** `None`

**•** `Update`

Available only when `triggerType` is `RecordBeforeSave` . This field is
available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The template that the current flow was created from. This is a relationship field. This
field is available in API version 53.0 and later.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default` —The flow can run from a Visualforce component, Lightning page,
flow action, or custom Aura component.

**•** `Offline` —The flow can run only offline. Flow types that support offline flows
must set this value.


Standard Objects FlowDefinitionView

**Field** **Details**

**•** `Slack` —The flow can run in Slack and the default environment. You specify
the Slack flow environment when you save the flow.

This field is available in API version 63.0 and later.

```
TriggerObjectOrEventId

TriggerObjectOrEventLabel

TriggerOrder

TriggerType

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
ID of the object or platform event that triggers this flow. This field is available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
TriggerObjectOrEvent

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is available
in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
[The run order of a record-triggered flow, from 1 to 2,000. See "Guidelines for Defining](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
[the Run Order of Record-Triggered Flows for an Object" in Salesforce Help. Available](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
in API version 54.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects FlowDefinitionView

**Field** **Details**

**Description**
Specifies what causes the flow to run. If you exclude this field, the flow has no trigger
and starts only when a user or app launches the flow. Valid values are:

**•** `AutomationEvent` —The flow starts when an automation event such as an
SMS subscription occurs. This value is available in API version 62.0 and later.

**•** `CampaignMember` —t the scheduled time, the flow performs actions on or
sends messages to individuals from the selected campaign. This value is available
in API version 67.0 and later.

**•** `Capability` —The flow starts when the specified capability that the flow
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `CrmRecordQuery` —At the scheduled time, the flow performs actions on or
sends messages to individuals from the queried customer relationship
management record. This value is available in API version 67.0 and later.

**•** `DataCloudDataChange` —The flow starts when data model object (DMO)
or calculated insight object (CIO) conditions are met. This value is available in API
version 59.0 and later.

**•** `DataGraphDataChange` —The flow starts when conditions are met in the
specified data graph field. This value is available in API version 63.0 and later.

**•** `EnterpriseScaleExternalSystemChange` —The flow runs when
triggered by MuleSoft. This value is available in API version 67.0 and later.

**•** `EventDrivenJourney` —Reserved for internal use.

**•** `ExternalSystemChange` —The flow starts when an external system change
event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent` —The flow runs when a user submits data via a
webform. In Flow Builder, this value corresponds to `Form` . This value is available
in API version 60.0 and later.

**•** `IndivRelatedRecord` —The flow starts when an object or an object with
fields related to an individual is created or updated. This value is available in API
version 66.0 and later.

**•** `List` —At the scheduled time, the flow performs actions on or sends messages
to individuals from the selected list. This value is available in API version 67.0 and
later.

**•** `PlatformEvent` —The flow starts when a platform event message is received.
This value is available in API version 49.0 and later.

**•** `RecordAfterSave` —The flow starts after a record is saved. This value is
available in API version 49.0 and later.

**•** `RecordBeforeDelete` —Deleting a record triggers an autolaunched flow
before the record is deleted from the database. This value is available in API version
50.0 and later.

**•** `RecordBeforeSave` —Creating and/or updating a record triggers an
autolaunched flow to make additional updates to that record before it's saved to
the database. This value is available in API version 48.0 and later.


### Standard Objects FlowInterview

**Field** **Details**

**•** `Scheduled` —The flow starts at the scheduled time. This value is available in
API version 47.0 and later.

**•** `Segment`                     - At the scheduled time, the flow performs actions on or sends
messages to individuals from the selected segment. This value is available in API
version 56.0 and later.

Available only when `processType` is `AutoLaunchedFlow` or `PromptFlow` .
This field is available in API version 47.0 and later.

```
VersionNumber

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s version number. This field is available in API version 54.0 and later.

Use this object to query information about flow definitions.

### FlowInterview

Represents a flow interview. A _flow interview_ is a running instance of a flow. This object is available in API version 32.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To delete a flow interview, you must have the “Manage Flow” user permission. All other calls require the “Run Flows” user permission or
the `Flow User` field enabled on the user detail page. If **Override default behavior and restrict access to enabled profiles or**
**permission sets** is selected for an individual flow, access to that specific flow and its interviews is given to users by profile or permission
set.

Fields

**Field Name** **Details**

```
CurrentElement

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowInterview

**Field Name** **Details**

**Description**
The flow element at which the interview is paused.

```
CurrentFlowVersion

EngineType

Error

FlowVersionViewId

Guid

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The engine type used to run the flow interview.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The error message that explains why the flow interview failed. This field is available
in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
This field is a relationship field. This field is available in API version 51.0 and later.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

**Type**
string


Standard Objects FlowInterview

**Field Name** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Globally unique identifier for the interview.

```
InterviewLabel

InterviewStatus

MasterFlowVersion

Name

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the interview. This label helps users and administrators differentiate
interviews from the same flow.

In the user interface, this label appears in the Paused Flow Interviews component
on the user’s Home tab and in the list of paused flow interviews in Setup.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the interview. Valid values are:

**•** `Completed` —This flow is complete. There are no more records to process.

**•** `Error` —This flow has one or more errors. To resolve each error, check the
error code for instructions.

**•** `Paused` —This flow is paused. No new processes are added until the flow
is resumed.

**•** `Running` —This flow is running or is ready to run.

**•** `VersionPaused` —This flow version is paused. No more records are
processed until the flow is resumed. This value is available in API version 60.0
and later.

This field is available in API version 50.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
string


Standard Objects FlowInterview

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the interview.

```
OwnerId

PauseLabel

SerializedView

WasPausedFromScreen

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the interview. Only this user or an admin can resume
the interview.

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
Filter, Nillable, Sort

**Description**
Information about why the interview was paused. This string is entered by the
user who paused the flow interview. The label is **Why Paused** .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
For internal use only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects FlowInterviewLog

**Field Name** **Details**

**Description**
Whether the flow interview was paused by a user from a flow Screen element
( `true` ) or not ( `false` ). This field is available in API version 46.0 and later.

Associated Objects

This object has these associated objects. Unless noted, these objects are available in the same API version as this object.

**FlowInterviewOwnerSharingRule**

Sharing rules are available for the object.

**FlowInterviewShare**

Sharing is available for the object.

### FlowInterviewLog

Represents the logs of a screen flow interview. An _interview_ is an instance of a running or previously run flow.This object is available in
API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

By default, only users with the View All Data permission can access the logs for flows that are run by other users. To let users access other
### users’ flow logs, set up sharing settings with the FlowInterviewLogOwnerSharingRule object.

Fields

**Field Name** **Details**

```
FlowDeveloperName

FlowInterviewGuid

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow's API name.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects FlowInterviewLog

**Field Name** **Details**

**Description**
Globally unique identifier for the interview.

```
FlowLabel

FlowNamespace

FlowVersionNumber

InterviewDurationInMinutes

InterviewEndTimestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s label. Only shows up in API results when users query FlowInterviewLog, or when
they include this field in a report.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace of the flow interview logged in the FlowInterviewLog.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of the flow version for a flow definition. Flow versions are counted sequentially
from 1.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total number of minutes between InterviewStartTimestamp and InterviewEndTimestamp,
even if flow interview is paused.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the interview ended.


Standard Objects FlowInterviewLog

**Field Name** **Details**

```
InterviewStartTimestamp

InterviewStatus

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the interview started.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the interview. Valid values are:

**•** `Autosaved` —This value is available in API version 62.0 and later.

**•** `Completed`

**•** `Error`

**•** `Expired` —This value is available in API version 62.0 and later.

**•** `Paused`

**•** `Running`

**•** `VersionPaused` —This value is available in API version 60.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated name of the flow interview log record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user who owns the FlowInterviewLog record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects FlowInterviewLogEntry

**Field Name** **Details**

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**FlowInterviewOwnerSharingRule**

Sharing rules are available for the object.

### FlowInterviewLogEntry

Represents the log of a specific element that’s executed by a screen flow interview. An _interview_ is an instance of a running or previously
run flow. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

By default, only users with the View All Data permission can access the log entries for flows that are run by other users.

Fields

**Field Name** **Details**

```
DurationSinceStartInMinutes

ElementApiName

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of minutes that elapsed since the flow interview started, even if flow interview is
paused.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API name of the flow element.


Standard Objects FlowInterviewLogEntry

**Field Name** **Details**

```
ElementDurationInMinutes

ElementLabel

FlowInterviewLogId

LogEntryTimestamp

LogEntryType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of minutes that elapsed since the element executed. For example, if a screen element
takes users a long time to complete, consider simplifying the screen.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow element’s label.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
FlowInterviewLog

**Relationship Type**
Lookup

**Refers To**
FlowInterviewLog

**Type**
datetime

**Properties**
Filter, Sort

**Description**
Date and time when the flow element started to execute.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of screen flow user action triggered the log entry. Valid values are:


### Standard Objects FlowInterviewLogOwnerSharingRule

**Field Name** **Details**

**•** `Error`

**•** `FlowFinish-Finished Flow`

**•** `FlowPause-Paused Flow`

**•** `FlowResume-Resumed Flow`

**•** `FlowStart-Started Flow`

**•** `ScreenFinish-Clicked Finish`

**•** `ScreenNext-Clicked Next`

**•** `ScreenPrevious-Clicked Previous`

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated name of the flow interview log entry.

### FlowInterviewLogOwnerSharingRule

Represents the rules for sharing a FlowInterviewLog with users other than the owner.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

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
A value that represents the type of sharing being allowed.

Possible values are:

**•** `Edit` —Read/Write

**•** `Read` —Read Only


Standard Objects FlowInterviewLogOwnerSharingRule

**Field** **Details**

```
Description

DeveloperName

GroupId

Name

OptionsIncludeHVUOwnedRecords

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

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
boolean

**Properties**
Create, Filter, Update

**Description**


### Standard Objects FlowInterviewOwnerSharingRule

**Field** **Details**

```
OptionsIncludeRecordsOwnedByAll

UserOrGroupId

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group that’s given access.

Use this object to manage the sharing rules for FlowInterviewLog records. General sharing uses this object.

### FlowInterviewOwnerSharingRule

Represents the rules for sharing a FlowInterview with users other than the owner. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

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
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit` —In API version 42.0 and later, when **Let users resume shared flow**
**interviews** is enabled for your org, users can resume all flow interviews that they
have edit access to.


Standard Objects FlowInterviewOwnerSharingRule

**Field** **Details**

```
Description

DeveloperName

GroupId

Name

UserOrGroupId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

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
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects FlowInterviewShare

**Field** **Details**

**Description**
The ID representing the target user or group that’s given access.

Usage

Use this object to manage the sharing rules for FlowInterview records. General sharing uses this object.

In API version 42.0 and later, when **Let users resume shared flow interviews** is enabled for your org, users can resume all flow interviews
that they have edit access to. When that setting is disabled, only the owner or a flow admin can resume a flow interview. To disable this
setting, go to your org’s Process Automation Settings in Setup.

### FlowInterviewShare

Represents a sharing entry on a FlowInterview. This object is available in API version 33.0 and later.

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

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the FlowInterview. The possible values are:

**•** `Read`

**•** `Edit` —In API version 42.0 and later, when **Let users resume shared flow interviews**
is enabled for your org, users can resume all flow interviews that they have edit access
to.


Standard Objects FlowInterviewShare

**Field** **Details**

**•** `All` —This value is not valid for creating or deleting records.

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
ID of the FlowInterview associated with this sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the FlowInterview with them.

**•** `Owner` —The User is the owner of the FlowInterview.

**•** `Rule` —The User or Group has access via a FlowInterview sharing rule.

**•** `GuestRule` —The User or Group has access via a FlowInterview guest user sharing
rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the FlowInterview. This field can't be
updated.

This is a polymorphic relationship field.


### Standard Objects FlowNavMetricEventLog

**Field** **Details**

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object lets you determine which users and groups can view and edit flow interviews that are owned by other users.

In API version 42.0 and later, when **Let users resume shared flow interviews** is enabled for your org, users can resume all flow interviews
that they have edit access to. When that setting is disabled, only the owner or a flow admin can resume a flow interview. To disable this
setting, go to your org’s Process Automation Settings in Setup.

### FlowNavMetricEventLog

Flow Navigation Metric event logs contain metric data for flow interviews such as total execution time, number of interviews, and number
of errors. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the bot.


Standard Objects FlowNavMetricEventLog

**Field** **Details**

```
BotSessionIdentifier

ErrorCount

FlowLoadTime

FlowVersionIdentifier

InterviewCount

PlannerIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The bot session ID.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of errors for all flow interviews after the flow version was executed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds to load the flow’s metadata.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version that was executed.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of flow interviews that started after the flow version was executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.


Standard Objects FlowNavMetricEventLog

**Field** **Details**

```
ProcessType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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

**•** `DataCaptureFlow`  - In the UI, Data Capture flows configure the Form tab in the
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


Standard Objects FlowNavMetricEventLog

**Field** **Details**

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


Standard Objects FlowNavMetricEventLog

**Field** **Details**

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
RequestIdentifier

Timestamp

TotalExecutionTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`TID:000000000000c00fff` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the flow was executed in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in milliseconds to start and finish all flow interviews.


### Standard Objects FlowOrchestration

**Field** **Details**

```
UserIdentifier

### FlowOrchestration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who executed the flow through the UI or the API. For example:
`00530000009M943` .

Represents the details of an orchestration definition. This object is available in API version 62.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`

Fields

**Field** **Details**

```
ActiveVersionId

ApiName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active orchestration version. This field is a relationship field.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Refers To**
### FlowOrchestrationVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the the orchestration.


Standard Objects FlowOrchestration

**Field** **Details**

```
ApiVersion

AverageRunTime

CompletionRate

Description

FailedRunCount

InstalledPackageName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the active orchestration or the last saved orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The average duration of an orchestration run that has completed without error.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the total number of orchestration runs that have completed without error.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The description of the flow orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have failed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the installed package that the orchestration is a part of.


Standard Objects FlowOrchestration

**Field** **Details**

```
IsCitizenEnabled

IsOverridable

IsTemplate

LastReferencedDate

LastViewedDate

ManageableState

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration can be modified by non-admins. Valid value is False.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record is a template.

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
The timestamp for when the current user last viewed this record.

**Type**
picklist


Standard Objects FlowOrchestration

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the managable state of the orchestration that's contained in a package.

Valid values are:

**•** `beta` —Managed-Beta

**•** `deleted` —Managed-Proposed-Deleted

**•** `deprecated` —Managed-Proposed-Deprecated

**•** `deprecatedEditable` —SecondGen-Installed-Deprecated

**•** `installed` —Managed-Installed

**•** `installedEditable` —SecondGen-Installed-Editable

**•** `released` —Managed-Released

**•** `unmanaged` —Unmanaged

```
Name

NamespacePrefix

OrchestrationDefinition

OrchestrationLabel

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The label of the orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the orchestration record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the orchestration definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects FlowOrchestration

**Field** **Details**

**Description**
The label of the orchestration.

```
OrchestrationType

OverriddenById

OverriddenOrchestrationId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The orchestration's flow type. FlowType consolidates ProcessType and TriggerType into one
field. FlowType is used with permissions, so admins can control access to each flow type.

Valid values are:

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration: Launches when invoked
by Apex, REST API, custom buttons, or custom links. An orchestration lets you create a
multi-step, multi-user process.

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration: Launches
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch` —CMS Workflow Orchestration Autolaunched: Launches when
invoked from the Workflows component in a CMS workspace. This type of orchestration
lets you create a multi-step, multi-user process to create, edit, organize, and manage
digital content from a centralized location

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that's overriding the current orchestration.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Refers To**
FlowOrchestration

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.


Standard Objects FlowOrchestration

**Field** **Details**

**Relationship Name**
OverriddenOrchestration

**Refers To**
FlowOrchestration

```
RunCount

SourceTemplateId

Status

TriggerType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have been started across all orchestration versions.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template that the orchestration was created from.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the record.

Valid values are:

**•** `Active` —Active

**•** `Draft` —Inactive

**•** `InvalidDraft` —Draft

**•** `Obsolete` —Inactive

**•** `UnderReview` —Under Review

**Type**
picklist


### Standard Objects FlowOrchestrationInstance

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the trigger type for a record-triggered orchestration.

Valid values are:

**•** `RecordAfterSave` —Record—Run After Save

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationChangeEvent on page 68**
Change events are available for the object.

### FlowOrchestrationInstance

Represents a run-time instance of an orchestration. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationInstance, they determine access to specific orchestration run records. Or the user must
have the View All Data permission.

Fields

**Field** **Details**

```
AuxiliaryTriggeringRecord

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The related object ID or service appointment ID. This fields isn’t used by flow approval
processes or orchestrations. This field is available in API version 65.0 and later.


Standard Objects FlowOrchestrationInstance

**Field** **Details**

```
CurrentStage

Duration

FlowDefinitionVersionName

FlowType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage that was running when the orchestration run was paused or failed
because of an error in an action called by a step. This field is available in API version 62.0 and
later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the orchestration instance in seconds. Durations are incremented until the
orchestration is completed, canceled, or ends in an error. This field is available in API version
62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The fully qualified API name of the underlying orchestration.

Possible values are active flow approval processes and orchestrations in the org. This field is
available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow type of the orchestration that created the orchestration work item.

Valid values are:

**•** `ApprovalOrchAutolnch` —Autolaunched Flow Approval Process

**•** `ApprovalOrchRecTrigAftSave` —Record-Triggered After Save Flow Approval
Process

**•** `ExtSysChgFlowAppvl` —External System Change-Triggered Flow Approval Process

**•** `ExtSysChgOrch` —External System Change-Triggered Orchestration

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration


Standard Objects FlowOrchestrationInstance

**Field** **Details**

This field is available in API version 62.0 and later.

```
InterviewId

IsDebugRun

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The globally unique flow interview ID associated with the orchestration instance.

This field is a relationship field.

**Relationship Name**
Interview

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the instance was executed from a debug run. The default value is `false` .

This field is available in API version 65.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration run. This field is
available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration run. This field is available in API version
55.0 and later.


Standard Objects FlowOrchestrationInstance

**Field** **Details**

```
Name

OrchestrationDeveloperName

OrchestrationLabel

OwnerId

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the orchestration instance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name of the flow definition associated with the orchestration run. This field
is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the orchestration. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the orchestration run. Valid values are:


### Standard Objects FlowOrchestrationLog

**Field** **Details**

**•** `Canceled` —The orchestration instance was canceled.

**•** `Completed` —The orchestration instance completed.

**•** `Error` —The orchestration instance, or a stage or step within the orchestration instance,
encountered an error.

**•** `InProgress` —The orchestration instance is in progress.

**•** `Suspended` —The orchestration instance was suspended.

```
TriggeringRecord

TriggeringRecordType

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that triggered the record-triggered orchestration. This field is available
in API version 62.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Salesforce object configured to trigger the orchestration. This field is available
in API version 64.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object. This object is available in API version 56.0 and later.

**FlowOrchestrationInstanceShare on page 67**
Sharing is available for the object. This object is available in API version 56.0 and later.

### FlowOrchestrationLog

Represents logging data for a FlowOrchestrationInstance. This object is available in API version 54.0 and later.


Standard Objects FlowOrchestrationLog

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()update()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationInstance and the Inherit orchestration run sharing rules to control orchestration run log
record access setting is enabled, then orchestration run log record access is inherited from related orchestration run records. If the Inherit
orchestration run sharing rules to control orchestration run log record access setting isn’t enabled, a user must have the Manage Flow
permission. Or the user must have the View All Data permission.

Fields

**Field** **Details**

```
Actor

Assignee

AssigneeType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For an interactive step, the user that completed the work item.

For a background or MuleSoft step, the username of the user that the step ran as.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For an interactive step, the user, group, or queue assigned to a work item when the
FlowOrchestrationLog relates to an interactive FlowOrchestrationStep.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For an interactive step, the assignee type associated with an interactive step's work item.
Valid values are:

**•** `Group`

**•** `Invalid`

**•** `Queue`

**•** `User`


Standard Objects FlowOrchestrationLog

**Field** **Details**

```
Comments

Context

Duration

Kind

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string stored in an output variable with the API name of Comments from a flow called
by a completed orchestration step.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record where the assigned user completed the flow associated with an
interactive step in the Work Guide component.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
A long number that indicates the duration, in seconds, of the associated
FlowOrchestrationInstance, FlowOrchestrationStage, FlowOrchestrationStep, or
FlowOrchestrationWorkItem.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The milestone associated with the FlowOrchestrationLog. Valid values are:

**•** `CancelInstance` —The associated FlowOrchestrationInstance was canceled.

**•** `DiscontinueStage` —The associated FlowOrchestrationStage was discontinued.

**•** `DiscontinueStep` —The associated FlowOrchestrationStep was discontinued.

**•** `EndInstance` —The associated FlowOrchestrationInstance was completed
successfully.

**•** `EndStage` —The associated FlowOrchestrationStage was exited successfully.

**•** `EndStep` —The associated FlowOrchestrationStep was exited successfully.

**•** `EndWorkItem` —The associated FlowOrchestrationWorkItem was completed
successfully.

**•** `FailInstance` —The associated FlowOrchestrationInstance encountered an error.


Standard Objects FlowOrchestrationLog

**Field** **Details**

**•** `FailStage` —The associated FlowOrchestrationStage encountered an error.

**•** `FailStep` —The associated FlowOrchestrationStep encountered an error.

**•** `ResumeInstance` —A failed or paused orchestration instance was resumed.

**•** `ReassignWorkItem` —The associated FlowOrchestrationWorkItem was reassigned.

**•** `RunRecallPath` —The associated approval submission was recalled.

**•** `StartInstance` —The associated FlowOrchestrationInstance started.

**•** `StartStage` —The associated FlowOrchestrationStage started.

**•** `StartStep` —The associated FlowOrchestrationStep started.

**•** `StartWorkItem` —The associated FlowOrchestrationWorkItem started.

**•** `SuspendInstance` —The associated FlowOrchestrationInstance was suspended.

**•** `SuspendStage` —The associated FlowOrchestrationStage was suspended.

```
Name

OrchestationInstanceId

OrchestrationName

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name for the FlowOrchestrationLog record.

**Type**
reference

**Properties**
Filter, Sort, Group

**Description**
The FlowOrchestrationInstance associated with the FlowOrchestrationLog.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the orchestration.


Standard Objects FlowOrchestrationLog

**Field** **Details**

```
OrchestrationVersion

StageName

StepName

Timestamp

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
An integer for the FlowDefinitionVersion of the orchestration associated with the
FlowOrchestrationLog.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage in the associated orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the step in the associated orchestration.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when the FlowOrchestrationLog milestone occured.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationLogFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationLogHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationLogOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationLogShare on page 67**
Sharing is available for the object.


### Standard Objects FlowOrchestrationStageInstance FlowOrchestrationStageInstance

Represents a run-time instance of a stage in a run-time instance of an orchestration. This read-only object is available in API version 53.0
and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationStageInstance, they determine access to specific orchestration stage run records. Or
the user must have the View All Data permission.

Fields

**Field** **Details**

```
Label

Name

OrchestrationInstanceId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the flow orchestration stage instance. This label helps users and administrators
differentiate between step instances from the same orchestration.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The API name for the flow orchestration stage instance.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration stage instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance


Standard Objects FlowOrchestrationStageInstance

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

```
OrchestrationName

OwnerId

Position

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of flow orchestration stage instance. This field is available in API version 66.0
and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
For internal use only.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The run status of the orchestration stage instance. Valid values are:

**•** `Completed` —The stage instance completed.


### Standard Objects FlowOrchestrationStepInstance

**Field** **Details**

**•** `Discontinued` —The stage was in progress or completed when the orchestration
instance encountered an error.

**•** `Error` —The stage instance encountered an error, an instance of a background step
within the stage encountered and error, or an autolaunched flow called by a background
step within the stage encountered an error.

**•** `InProgress` —The stage instance is in progress.

**•** `Suspended` —The stage was in progress when the orchestration instance was manually
suspended.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStageInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationStageInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationStageInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationStageInstanceShare on page 67**
Sharing is available for the object.

### FlowOrchestrationStepInstance

Represents a run-time instance of a step in a run-time instance of a stage of a run-time instance of an orchestration. This read-only object
is available in API version 53.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationStepInstance, they determine access to specific orchestration step run records. Or the
user must have the View All Data permission.


Standard Objects FlowOrchestrationStepInstance

Fields

**Field** **Details**

```
Description

Label

Name

OrchestrationInstanceId

OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the step.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the step.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the step.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

**Type**
reference

**Properties**
Filter, Group, Sort, Update


Standard Objects FlowOrchestrationStepInstance

**Field** **Details**

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
StageInstanceId

Status

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationStageInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
StageInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationStageInstance

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the orchestration step instance. Valid values are:

**•** `Completed` —The step instance completed.

**•** `Discontinued` —The step instance was in progress or completed when it’s associated
stage instance completed, or the step was in progress or completed when the
orchestration instance encountered an error.

**•** `Error` —The step instance encountered an error or the autolaunched flow associated
with a step instance encountered an error.

**•** `InProgress` —The step instance is running, the step instance was in progress when
its associated stage encountered an error, or the screen flow associated with the step
instance encountered an error.

**•** `NotStarted` —The step instance was created, but hasn’t met its entry condition.


### Standard Objects FlowOrchestrationVersion

**Field** **Details**

```
StepType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of step. Valid values are:

**•** `InteractiveStep` —Interactive Step

**•** `BackgroundStep` —Background Step

**•** `AynchronousBackgroundStep` —Asynchronous Background Step

This value is available in API version 54.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStepInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationStepInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationStepInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationStepInstanceShare on page 67**
Sharing is available for the object.

### FlowOrchestrationVersion

Represents the version of an orchestration. This object is available in API version 62.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActivatedById

```

**Type**
reference


Standard Objects FlowOrchestrationVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that activated the orchestration.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Refers To**
User

```
ActivatedDate

ApiVersion

Description

FlowOrchestrationId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the orchestration was activated.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version of this orchestration record version.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow orchestration version.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent orchestration running this version.

This field is a relationship field.

**Relationship Name**
FlowOrchestration


Standard Objects FlowOrchestrationVersion

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
FlowOrchestration

```
IsOverridable

IsTemplate

LastReferencedDate

LastViewedDate

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record version is a template.

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
The timestamp for when the current user last viewed this record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the orchestration.


Standard Objects FlowOrchestrationVersion

**Field** **Details**

```
OrchestrationType

OverriddenById

OverriddenOrchestrationId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The orchestration's flow type. FlowType consolidates ProcessType and TriggerType into one
field. FlowType is used with permissions, so admins can control access to each flow type.

Valid values are:

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration: Launches when invoked
by Apex, REST API, custom buttons, or custom links. An orchestration lets you create a
multi-step, multi-user process.

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration: Launches
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch` —CMS Workflow Orchestration Autolaunched: Launches when
invoked from the Workflows component in a CMS workspace. This type of orchestration
lets you create a multi-step, multi-user process to create, edit, organize, and manage
digital content from a centralized location

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that's overriding the current orchestration.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Refers To**
FlowOrchestration

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.

**Relationship Name**
OverriddenOrchestration


Standard Objects FlowOrchestrationVersion

**Field** **Details**

**Refers To**
FlowOrchestration

```
RunInMode

SourceTemplateId

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the orchestration runs in.

Possible values are:

**•** `DefaultMode` —The orchestration version runs in system or user context, depending
on how the orchestration is launched.

**•** `SystemModeWithSharing` —The orchestration version always runs in system
mode with sharing. The orchestration respects org-wide default settings, role hierarchies,
sharing rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

**•** `SystemModeWithoutSharing` —The orchestration version can access all data.
In the UI, this value appears as System Context without Sharing—Access All Data.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The ID of the template that the orchestration was created from. This is a relationship
field.(Refers to Orchestration Record).

Possible values are:

**•** `Active` —Active

**•** `Draft` —Inactive

**•** `InvalidDraft` —Draft


### Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**•** `Obsolete` —Inactive

**•** `UnderReview` —Under Review

```
TriggerObjectOrEventLabel

VersionNumber

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the orchestration version.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationVersionChangeEvent on page 68**
Change events are available for the object.

### FlowOrchestrationWorkItem

Represents a work item associated with a run-time instance of an interactive step in a run-time instance of an orchestration. This object
is available in API version 54.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

An assignee can see all work item records assigned to them. If sharing rules are defined for FlowOrchestrationWorkItem, they determine
access to specific orchestration work item records for users other than the assignee. Or the user must have the View All Data permission.


Standard Objects FlowOrchestrationWorkItem

Fields

**Field** **Details**

```
AssigneeId

Description

ElapsedTimeSinceAsgntInSec

ElapsedTimeSinceCreationInSec

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user, group, or queue assigned to the orchestration work item.

This field is a polymorphic relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the orchestration work item.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
last assigned. When status is Completed, this value is null. This field is available in API version
63.0 and later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
created. When status is Completed, this value is null. This field is available in API version 63.0
and later.


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

```
FlowType

Label

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow type of the orchestration that created the orchestration work item.

Valid values are:

**•** `ApprovalOrchAutolnch` —Autolaunched Flow Approval Process

**•** `ApprovalOrchRecTrigAftSave` —Record-Triggered After Save Flow Approval
Process

**•** `ExtSysChgFlowAppvl` —External System Change-Triggered Flow Approval Process

**•** `ExtSysChgOrch` —External System Change-Triggered Orchestration

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label of the orchestration work item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration work item. This
field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration work item. This field is available in API
version 55.0 and later.

**Type**
string


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the orchestration work item.

```
OrchestrationName

OwnerId

ParentWorkItemId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the orchestration associated with the orchestration work item.

This field is avavilable in API version 56.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When the assignee is an internal user: the ID of the internal user

When the assignee is a credentialed Experience Cloud site visitor: the ID of the credentialed
Experience Cloud site visitor

When the assignee is a group or queue: the ID of the automated process user

This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent orchestration work item. When multiple group members receive child
work items, this field links each child to its parent.

This field is available in API version 67.0 and later.

**Relationship Name**
ParentWorkItem


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationWorkItem

```
RelatedRecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the context record, such as an account, case, or expense, that the orchestration
work item is related to. An assigned user completes the associated orchestration work item
on the page for this record.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
All objects except AccountContactRelation, AccountTeamMember, ActiveScratchOrg,
ActivityMetric, ActivityMetricRollup,CampaignMember, CartCheckoutSession,
CartDeliveryGroup, CartDeliveryGroupMethod, ChatterActivity,CollaborationGroupMember,
ContentDesignKit, ContentDesignKitVersion, ConversationBroadcastEntry,ConversationReason,
ConversationReasonExcerpt, ConversationReasonGroup,
CustomPersonDataTemplate,ElectronicMediaGroup, EngagementScore, Event, FeedItem,
FlowOrchestrationWorkItem, FtestDelPlatform1,FtestDelPlatform2,
FtestFormulaFieldRefSql,HighScaleSample, HighScaleSampleItem, LegalEntity, LocationWaitlist,
LocationWaitlistedParty,LocWaitlistMsgTemplate, ManagedContentVersion,
MessagingEndUser, MessagingSession, MLModel,MLModelFactor, MLModelFactorComponent,
NetworkMember, NetworkMemberChunk, OpportunityContactRole,OpportunityLineItem,
OpportunityScore, OpportunityTeamMember, OrgSnapshot,
PaymentTermItem,RequestsForAccessSIQ, ScoreIntelligence, ScratchOrgInfo,
SharingRecordCollection, SharingRecordCollectionItem,SharingRecordCollectionMember,
StreamActivityAccess, Survey, SurveyMessagingChannel, SurveyPage,SurveyQuestionChoice,
SurveyVersion, Task, TenantSecurityAlertRuleSelectedTenant,
TenantSecurityApiAnomaly,TenantSecurityConnectedApp, TenantSecurityCredentialStuffing,
TenantSecurityHealthCheckBaselineTrend,TenantSecurityHealthCheckDetail,
TenantSecurityHealthCheckTrend, TenantSecurityLogin,
TenantSecurityMetricDetail,TenantSecurityMetricDetailLink, TenantSecurityMobilePolicyTrend,
TenantSecurityMonitorMetric,TenantSecurityNotification, TenantSecurityNotificationRule,
TenantSecurityPackage, TenantSecurityPolicy,TenantSecurityPolicyChangeLog,
TenantSecurityPolicyDeployment,
TenantSecurityPolicySelectedTenant,TenantSecurityReportAnomaly,
TenantSecuritySessionHijacking, TenantSecurityTenantChangeLog,TenantSecurityTenantInfo,


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

TenantSecurityTrustedIpRangeTrend, TenantSecurityUserActivity,
TenantSecurityUserPerm,TenantSecurityWebsite, TopicAssignment, UserExternalCredential,
VoiceCall

```
ScreenFlow

ScreenFlowInputs

Status

StepInstanceId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The screen flow associated with the orchestration work item.

Possible values are screen flows in the org.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input parameters required by the screen flow.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the work item.

Valid values are:

**•** `Assigned`

**•** `Completed`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the flow orchestration step associated with the orchestration work item.

This field is a relationship field.

**Relationship Name**
StepInstance

**Relationship Type**
Lookup


### Standard Objects FlowRecord

**Field** **Details**

**Refers To**
FlowOrchestrationStepInstance

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationWorkItemFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationWorkItemHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationWorkItemOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationWorkItemShare on page 67**
Sharing is available for the object.

### FlowRecord

Represents the details of a flow. This object is available in API version 58.0 and later.

Supported Calls

`delete()`, `query()`, `update()`

Fields

**Field Name** **Details**

```
ActivationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the marketing segment activation. This field is available in API version
64.0 and later.

This field is a relationship field.

**Relationship Name**
Activation

**Relationship Type**
Lookup


Standard Objects FlowRecord

**Field Name** **Details**

**Refers To**
MarketSegmentActivation

```
ActiveVersionId

ApiVersion

AreMetricsLoggedToDataCloud

AssociatedRecordId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version. This field is available in API version 61.0 and
later.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Relationship Type**
Lookup

**Refers To**
FlowRecordVersion

**Type**
double

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow record. This field is available in API version 61.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value
is false. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record the flow is associated with.

This field is a polymorphic relationship field.


Standard Objects FlowRecord

**Field Name** **Details**

**Relationship Name**
AssociatedRecord

**Relationship Type**
Lookup

**Refers To**
Campaign

```
Builder

CapacityCategory

Description

```

ElementEntries

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Valid values are:

**•** `Cloud Flow Designer`

**•** `Flow Builder`

**•** `Swing Designer`

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the flow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the last flow occurrence activated an element. This field is
available in API version 67.0 and later.


Standard Objects FlowRecord

**Field Name** **Details**

ElementErrors

```
ErrorCode

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the last flow occurrence activated an element which caused
an error. This field is available in API version 67.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The error code if the flow element run encountered an error. Valid values are:

**•** `ACTIVATING_USER_ACCOUNT_DEACTIVATED` —We can't run this
flow because the user who activated it has a deactivated user record.

**•** `ACTIVATING_USER_LOST_PERMISSIONS` —We can't run this flow
because the user that activated it no longer has permission to it.

**•** `CANNOT_PUBLISH_SEGMENT` —We can't run this flow because we can't
publish the segment it's using. Contact Salesforce Customer Support and
ask for help with the error ID.

**•** `CANNOT_QUERY_SEGMENT_MEMBER_DATA` —We can't run this flow
because we can't query the segment membership data it's using. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_RUN_ACTIVATION_TRIGGERED_FLOW` —Something went
wrong with your automation. Contact Salesforce Customer Support and ask
for help with the error ID.

**•** `CANNOT_REFRESH_DATA_STREAM` —We can't run this flow because
we can't refresh your data stream metadata. Contact Salesforce Customer
Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_IDENTITY_RES_DATA` —We can't run this flow
because we can't refresh your identity resolution data. Contact Salesforce
Customer Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_IDENTITY_RES_METADATA` —We can't run this
flow because we can't refresh your identity resolution metadata. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_UPDATE_DATASTREAM_METADATA` —We can't run this flow
because we can't update your DataStream metadata. Contact Salesforce
Customer Support and ask for help with the error ID.

**•** `CREATE_EXPERIMENT_ERROR` —We can't run this flow because an
error occurred while executing the Path Experiment element. To try again,
save and activate a new version of the flow.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `DATA_ACTION_STATUS_ERROR` —We can’t run this flow because we
couldn’t create the data action. To try again, save and activate a new version
of the flow.

**•** `FLOW_FAILED_TO_START` —This flow failed to start. Contact Salesforce
Customer Support and ask for help with the error ID.

This field is available in API version 59.0 and later.

```
ErrorDetails

FlowCategory

FlowDefinition

FlowSubcategory

FlowType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error ID. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a category. Sharing rules assign permissions to view and edit
flows by category and subcategory. This field is available in API version 60.0 and
later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a subcategory. Sharing rules assign permissions to view and
edit flows by category and subcategory. This field is available in API version 60.0
and later.

**Type**
picklist


Standard Objects FlowRecord

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The label of a flow type. `FlowType` consolidates `ProcessType` and
`TriggerType` into one field. `FlowType` is used with permissions, so admins
can control access to each flow type. Valid values are:

**•** `Action Cadence Step Screen Flow` —Launches from a cadence
step. This type of flow collects or displays information and requires user
interaction.

**•** `Action Plan Autolaunched Flow` —Launches an action plan
task from an action plan when conditions in the associated action plan
template process are met. This type of flow runs in the background without
user interaction.

**•** `Activity-Object Matching No Trigger Flow` —Launches
when Einstein Activity Capture detects and captures a new activity, such as
an email. This type of flow runs in the background without user interaction.
Requires Sync Email as Salesforce Activity to be enabled.

**•** `Activation-Triggered Autolaunched Flow` —Launches
when an activation is published. This type of flow runs in the background
without user interaction.

**•** `Admin Automation Event-Triggered Flow` —Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction.

**•** `Autolaunched Approval Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An approval
orchestration lets you create a multi-step, multi-user approval process.

**•** `Autolaunched No Trigger Flow` —Launches when invoked by
processes or code such as Apex and REST API. This type of flow runs in the
background without user interaction.

**•** `Autolaunched No Trigger Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An orchestration
lets you create a multi-step, multi-user process.

**•** `Automation Event-Triggered Autolaunched`
`Flow` —Launches when invoked by Apex, processes, REST API, and more.
This type of flow runs in the background without user interaction.

**•** `Automation Event-Triggered Flow` —Launches when a user
performs an automation event, like subscribing to SMS messages. This type
of flow runs in the background without user interaction.

**•** `Automation Event-Triggered Flow v0` —Deprecated. Launches
when a user performs an automation event, like subscribing to SMS messages.
This type of flow runs in the background without user interaction.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Campaign Member` —Launches when scheduled to perform actions on
or send messages to individuals from the selected campaign member. This
value is available in API version 67.0 and later.

**•** `Cart Async Autolaunched Flow` —Launches when invoked by
a cart change, such as an Add to Cart. This type of flow runs in the background
without user interaction.

**•** `Checkout Screen Flow` —Create a screen flow that implements a
Commerce Cloud checkout process. This type of flow collects or displays
information and requires user interaction.

**•** `CMS Workflow Orchestration Autolaunched` —Launches
when invoked from the Workflows component in a CMS workspace. This
type of orchestration lets you create a multi-step, multi-user process to create,
edit, organize, and manage digital content from a centralized location.

**•** `Contact Request Screen Flow` —Launches when invoked by a
customer, allowing them to enter contact details into a self-service form. This
type of flow collects or displays information and requires user interaction.

**•** `Customer Lifecycle Record-Triggered After Save`
`Flow` —Launches after a customer lifecycle map is saved and changes
records related to the triggering record. This type of flow runs in the
background without user interaction.

**•** `Data Cloud Data Change Flow` —Launches when a record from
a Data Cloud data model object or a calculated insight object is changed and
meets the specified conditions. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Autolaunched Flow` —Launches
when invoked by Apex, processes, REST API, and more. This type of flow runs
in the background without user interaction.

**•** `Data Graph-Triggered Flow` —Launches when invoked by Apex,
processes, REST API, and more. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Flow v0` —Deprecated. Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction.

**•** `Digital Form Screen Flow` —Launches from app extensions. This
type of flow collects or displays information and requires user interaction.

**•** `Discovery Framework Data Capture Screen Flow`
`(Beta)` —Launches when invoked by a user on a mobile device and
presents assessment questions from Discovery Framework. This type of flow
collects or displays information and requires user interaction.

**•** `Employee Service Catalog Item Screen Flow` —Launches
when invoked by a user and allows them to browse and order items from
the Employee Service Catalog. This type of flow collects or displays information
and requires user interaction.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Enterprise Scale External System Change-Triggered`
`Flow` —Launches when invoked by MuleSoft. This value is available in API
version 67.0 and later.

**•** `Evaluation Autolaunched Flow` —Launches when invoked by
an orchestration to evaluate custom criteria for a stage or step. To indicate
that the criteria are met, set the output variable
`isOrchestrationConditionMet` to `true` . This type of flow runs
in the background without user interaction.

**•** `External System Change-Triggered Flow` —Launches when
an event is received from an external system. This type of flow runs in the
background without user interaction.

**•** `Event-Driven Flow` —Launches when an event is received. This type
of flow runs in the background without user interaction.

**•** `Field Service Mobile Screen Flow` —Launches when invoked
by a user in the Field Service mobile app. This type of flow collects or displays
information and requires user interaction.

**•** `Field Service Web Screen Flow` —Launches from the Field
Service app and lets users schedule, modify, or cancel an appointment in a
web browser. This type of flow requires user interaction.

**•** `Form-Triggered Autolaunched Flow` —Launches when a web
visitor submits a marketing form. This type of flow runs in the background
without user interaction.

**•** `Form-Triggered Flow` —Launches when a web visitor submits a
marketing form. This type of flow runs in the background without user
interaction.

**•** `Form-Triggered Flow v0` —Deprecated. Launches when a web
visitor submits a marketing form. This type of flow runs in the background
without user interaction.

**•** `Identity User Registration Flow` —Launches when a user
logs in via a single sign-on process that uses the authentication provider
framework. After the third-party identity provider authenticates the user, the
flow creates a user or updates an existing user. This type of flow runs in the
background without user interaction.

**•** `Indicator Result Screen Flow` —Launches a screen flow when
initiated by a user to calculate and create indicator results for a selected
indicator performance period.

**•** `Individual-Object Linking Screen Flow` —Launches when
invoked by an agent to link a record like a case or messaging session to a
contact, lead, person account, or employee. This type of flow collects or
displays information and requires user interaction.

**•** `List` —Launches when scheduled to perform actions on or send messages
to individuals from the selected list. This value is available in API version 67.0
and later.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Login Screen Flow` —Launches when a user tries to log in to
Salesforce. This type of flow extends Salesforce's default authentication
process by sending users with certain profiles through a flow when they log
in and requires user interaction.

**•** `Loyalty Management Autolaunched Flow` —Launches when
invoked by a loyalty program process, and contains Assignment, Decision,
and Action elements. The Action element in this type of flow supports Apex
and quick actions. This type of flow runs in the background without user
interaction.

**•** `Managed Content Autolaunched Flow` —Launches when
invoked by the ManagedContentRelease translator. This type of flow runs in
the background without user interaction.

**•** `Mortgage Lending Screen Flow` —Launches when invoked by
a user and allows them to provide Financial Service Cloud mortgage
application details. This type of flow requires user interaction.

**•** `Platform Event Triggered Flow` —Launches when a platform
event occurs. This type of flow runs in the background without user
interaction.

**•** `Process Builder Autolaunched Process` —Launched when
invoked from a Process Builder process. This type of flow runs in the
background without user interaction.

**•** `Process Builder Custom Event Process` —A process created
in Process Builder that launches when a custom event message is received.
This type of process runs in the background without user interaction.

**•** `Process Builder Workflow` —Launches when a record is created
or updated. This type of process runs in the background without user
interaction.

**•** `Prompt Template Capability-Triggered Flow` —Launches
from a prompt template. This type of flow adds prompt instructions to the
associated prompt template and runs in the background without user
interaction.

**•** `Recommendation Strategy Autolaunched Flow` —Build a
personalized list of recommendations. When a recommendation is selected,
it launches its assigned flow. Used by Einstein Next Best Action. Show
recommendations in Lightning App Builder with the Einstein Next Best Action
component and in Experience Builder with the Suggested Actions component.

**•** `Record-Triggered After Save Flow` —Launches after a record
is created or updated and has been saved. This type of flow can make changes
only to records related to the triggering record and runs in the background
without user interaction.

**•** `Record-Triggered After Save Approval`
`Orchestration` —Launches when a record is created or updated. An
approval orchestration lets you create a multi-step, multi-user approval
process.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered Before Delete Flow` —Launches when a
record is deleted. This type of flow runs in the background without user
interaction.

**•** `Record-Triggered Before Save Flow` —Launches after a record
is created or updated, but hasn't been saved. This type of flow can make
changes only to the triggering record and runs in the background without
user interaction.

**•** `Record Query` —Launches when scheduled to perform actions on or
send messages to individuals from the queried customer relationship
management record. This value is available in API version 67.0 and later.

**•** `Routing Autolaunched Flow` —Launches when a customer initiates
a chat, voice, or messaging conversation and routes the work item to a queue,
skill, agent, or bot. This type of flow runs in the background without user
interaction.

**•** `Schedule-Triggered Flow` —Launches at a specified time and
frequency for each record that meets the flow criteria. This type of flow runs
in the background without user interaction.

**•** `Scheduler Appointments Screen Flow` —Launches when
invoked by a user and lets them schedule appointments in Salesforce
Scheduler. This type of flow collects or displays information and requires user
interaction.

**•** `Screen Flow` —Launches from Lightning pages, Experience Cloud sites,
quick actions and more. This type of flow collects or displays information and
requires user interaction.

**•** `Segment-Triggered Autolaunched Flow` —Launches when
activated or when scheduled for qualified Data Cloud segment members.
This type of flow runs in the background without user interaction.

**•** `Segment-Triggered Flow` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction.

**•** `Segment-Triggered Flow v0` —Deprecated. Launches when
activated or when scheduled for qualified Data Cloud segment members.
This type of flow runs in the background without user interaction.

**•** `Stage Management Evaluation Autolaunched`
`Flow` —Launches when invoked by a stage transition in Stage Management
to evaluate custom criteria for a stage or step. To indicate that the criteria are
met, set the output variable isCriteriaMet to True.

**•** `Survey Enrich Autolaunched Flow` —Launches in the context
of a survey response and can't execute without a corresponding survey. Use
it to conditionally map a response to a record, create records, or send


Standard Objects FlowRecord

**Field Name** **Details**

notifications. This type of flow runs in the background without user
interaction.

**•** `Survey Screen Flow` —Launches when invoked by an internal or
external survey participant. This type of flow saves participant feedback as
survey response records and requires user interaction.

**•** `Transaction Security Autolaunched Flow` —Used by
Condition Builder to declaratively build customized security policies to protect
data. This type of flow runs in the background without user interaction.

**•** `User Provisioning Screen Flow` —Launches when invoked by
a user and allows them to create a user account and link it to a third-party
service or app. This type of flow requires user interaction.

This field is available in API version 60.0 and later.

```
Health

Id

IsLightningAppEnabled

IsOverridable

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The value of `ElementErrors` divided by `ElementEntries` multiplied
by 100. This field is available in API version 67.0 and later.

**Type**
text

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s flow type has been enabled in Lightning Experience
apps. The default value is `false` . This field is available in API version 61.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FlowRecord

**Field Name** **Details**

**Description**
Indicates whether the flow record version is overridable. The default value is
`false` . This field is available in API version 61.0 and later.

```
IsPaused

IsTemplate

LogsEnabledFlowVersion

Manageable State

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment-triggered flow is paused ( `true` ) or not ( `false` ).
When the value is `true`, no additional records are processed until the flow is
resumed. The default value is `false` . This field is available in API version 60.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is a template. Template flow record
versions are automatically shared with all users in your Salesforce org. The default
value is `false` . This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the flow that enabled persistent logging. This field is
available in API version 66.0 and later.

**Type**
boolean

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates the manageable state of the flow record that is contained in a package.
Valid values are:

**•** beta

**•** deleted

**•** deprecated

**•** deprecatedEditable


Standard Objects FlowRecord

**Field Name** **Details**

**•** installed

**•** installedEditable

**•** released

**•** unmanaged

This field is available in API version 60.0 and later.

```
Name

NamespacePrefix

OverriddenById

OverriddenFlowId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow record. This field is available in
API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that’s overriding the current flow. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowRecord

**Field Name** **Details**

**Description**
The ID of the flow that the current flow is overriding. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowRecord

```
OwnerId

ProgressStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user who owns the flow.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The progress status of the flow. Valid values are:

**•** `Canceled`  - Indicates a flow that has been deactivated by a user who
doesn’t process previously added records. No additional records are added
to this flow.

**•** `Completed`  - Indicates a flow that is complete. No additional records are
eligible to be processed in this flow.

**•** `Draft` —Indicates a flow that is under construction and isn’t active yet. This
status can be invalid because it needs additional information before it can
be activated by the user.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Error` —Indicates a flow that has been deactivated because it encountered
an error. When the error occurs, the error details are emailed to up to 5 users
with the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`                       - Indicates a flow that has been deactivated by a user, but is
finishing previously added records that are eligible to run to completion. No
additional records are added to this flow.

**•** `InProgress`                       - Indicates a flow that is running or ready to run.

**•** `PreparingData`                       - Indicates a flow that is preparing the necessary data
to run. This process can take up to 2 hours.

**•** `Scheduled`                       - Indicates a flow scheduled to start on the date and time
selected by the user.

**•** `UnderReview` —Indicates a flow that is under review before it is activated.
This value is available in API version 64.0 and later.

```
ScheduledStartDate

SegmentId

SourceTemplateId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow is scheduled to start.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the segment used in the flow.

This field is a relationship field.

**Relationship Name**
Segment

**Relationship Type**
Lookup

**Refers To**
MarketSegment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template from which the current flow was created. This field is
available in API version 61.0 and later.


Standard Objects FlowRecord

**Field Name** **Details**

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowRecord

```
TriggerObjectOrEventLabel

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is
available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The trigger type of the flow. Specifies what causes the flow to run. Valid values
are:

**•** `Activation` —The flow starts when an activation is published. This type
of flow runs in the background without user interaction. This value is available
in API version 64.0 and later.

**•** `AdminAutomationEvent` —The flow starts when an automation event
is received. This type of flow runs in the background without user interaction.
This value is available in API version 64.0 and later.

**•** `Automation Event` —The flow starts when an automation event such
as an SMS subscription occurs. This value is available in API version 62.0 and
later.

**•** `CampaignMember` —The flow starts at the scheduled time of a campaign
member. This value is available in API version 67.0 and later.

**•** `Capability` —The flow starts when the specified capability that the flow
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `DataCloudDataChange` —The flow starts when data model object
(DMO) or calculated insight object (CIO) conditions are met. This value is
available in API version 59.0 and later.

**•** `DataGraphDataChange` —The flow starts when conditions are met in
the specified data graph field. This value is available in API version 63.0 and
later.


### Standard Objects FlowRecordElement

**Field Name** **Details**

**•** `EnterpriseScaleExternalSystemChange` —The flow starts
when triggered by MuleSoft. This value is available in API version 67.0 and
later.

**•** `EventDrivenJourney` —Reserved for internal use.

**•** `ExternalSystemChange` —The flow starts when an external system
change event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent` —The flow runs when a user submits data via
a webform. In Flow Builder, this value corresponds to `Form` . This value is
available in API version 60.0 and later.

**•** `List` —The flow starts at the scheduled time of a list. This value is available
in API version 67.0 and later.

**•** `PlatformEvent` —The flow starts when a platform event message is
received. This value is available in API version 49.0 and later.

**•** `RecordAfterSave` —The flow starts after a record is saved. This value
is available in API version 49.0 and later.

**•** `RecordBeforeDelete` —Deleting a record triggers an autolaunched
flow before the record is deleted from the database. This value is available
in API version 50.0 and later.

**•** `RecordBeforeSave` —Creating and/or updating a record triggers an
autolaunched flow to make additional updates to that record before it's saved
to the database. This value is available in API version 48.0 and later.

**•** `RecordQuery` —The flow starts at the scheduled time of a queried
customer relationship management record. This value is available in API
version 67.0 and later.

**•** `Scheduled` —The flow starts at the scheduled time. This value is available
in API version 47.0 and later.

**•** `Segment` —The flow runs at the scheduled time of a segment.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**FlowRecordChangeEvent (API version 62.0)**
Change events are available for the object.

**FlowRecordOwnerSharingRule**

Sharing rules are available for the object.

**FlowRecordShare**

Sharing is available for the object.

### FlowRecordElement

Represents a single element within a flow version. This object is available in API version 58.0 and later.


Standard Objects FlowRecordElement

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DataSpaceId

ElementName

FlowRecordVersionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the data space for this flow record element. This field is available in API
version 66.0 and later.

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
The API name of the flow element.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow version the flow element is part of.

This field is a relationship field.

**Relationship Name**
FlowRecordVersion

**Relationship Type**
Master-detail

**Refers To**
FlowRecordVersion (the master object)


### Standard Objects FlowRecordElementOccurrence

**Field Name** **Details**

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
The date and time that the flow element was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow element was last viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the flow element.

**FlowRecordElementChangeEvent (API version 62.0)**
Change events are available for the object.

### FlowRecordElementOccurrence

Represents the execution metrics for a single element within a flow version. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist


Standard Objects FlowRecordElementOccurrence

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency associated with the flow.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
Entries

Errors

Exits

FlowRecordElementId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was initiated in all flow interviews after the flow version
was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of errors for the element in all flow interviews after the flow version was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was executed to completion in all flow interviews after
the flow version was executed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow element.

This field is a relationship field.

**Relationship Name**
FlowRecordElement


Standard Objects FlowRecordElementOccurrence

**Field** **Details**

**Refers To**
FlowRecordElement

```
FlowRecordId

FlowRecordVersionId

FlowRecordVersionOccurrenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow.

This field is a relationship field.

**Relationship Name**
FlowRecord

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version.

This field is a relationship field.

**Relationship Name**
FlowRecordVersion

**Refers To**
FlowRecordVersion

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow occurrence.

This field is a relationship field.

**Relationship Name**
FlowRecordVersionOccurrence

**Relationship Type**
Master-detail

**Refers To**
FlowRecordVersionOccurrence (the master object)


### Standard Objects FlowRecordRelation

**Field** **Details**

```
Name

Stopped

TotalDuration

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the flow element.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times execution of the element was stopped in all flow interviews after the
flow version was executed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total time in milliseconds spent executing the element in all flow interviews.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowRecordElementOccurrenceChangeEvent on page 68**
Change events are available for the object.

**FlowRecordElementOccurrenceFeed on page 55**
Feed tracking is available for the object.

**FlowRecordElementOccurrenceHistory on page 63**
History is available for tracked fields of the object.

**FlowRecordElementOccurrenceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowRecordElementOccurrenceShare on page 67**
Sharing is available for the object.

### FlowRecordRelation

Represents a relationship between a record and a flow interview. When a flow interview is paused, Salesforce uses the $Flow.CurrentRecord
global variable in the flow to associate the interview with a record. Available in API version 42.0 and later.


Standard Objects FlowRecordRelation

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

ParentId

RelatedRecordId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that the flow interview is related to. Make sure that this field contains
only one ID, and that the ID is for a valid object.

Custom objects and most standard objects are supported.

This is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup


Standard Objects FlowRecordRelation

**Field Name** **Details**

**Refers To**
Account, AccountContactRole, AccountPartner, Accreditation, ActivationTarget,
ActivationTrgtIntOrgAccess, Address, AlternativePaymentMethod, Announcement,
ApexTestQueueItem, AppAnalyticsQueryRequest, AppUsageAssignment,
AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, AssociatedLocation, AsyncApexJob, Attachment,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BackgroundOperation, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, CalendarView, Campaign,
CampaignMember, CardPaymentMethod, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth,
CarePreauthItem, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct,
CareProgramProvider, CareProgramTeamMember, CareProviderAdverseAction,
CareProviderFacilitySpecialty, CareProviderSearchableField, CareRegisteredDevice,
CareRequest, CareRequestDrug, CareRequestExtension, CareRequestItem,
CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CaseContactRole,
CaseSolution, CodeSet, CodeSetBundle, CollaborationGroup,
CollaborationGroupMember, CollaborationGroupMemberRequest,
CollaborationGroupRecord, CollaborationInvitation, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConferenceNumber, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, ContactRequest,
ContentDistribution, ContentDocument, ContentDocumentLink,
ContentDocumentSubscription, ContentFolder, ContentFolderLink,
ContentFolderMember, ContentNotification, ContentVersion,
ContentVersionComment, ContentVersionRating, ContentWorkspaceDoc,
Contract, ContractContactRole, ConversationEntry, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, Dashboard,
DashboardComponent, DataAssessmentFieldMetric, DataAssessmentMetric,
DataAssessmentValueMetric, DataStream, DataUseLegalBasis, DataUsePurpose,
DelegatedAccount, DeleteEvent, DialerCallUsage, DigitalSignature, DigitalWallet,
Document, DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet,
EmailMessage, EmailMessageRelation, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, EntitySubscription, Event,
EventRelation, ExternalEvent, ExternalEventMapping, FeedAttachment,
FeedComment, FeedItem, FeedPollChoice, FeedPollVote, FeedRevision,
FileSearchActivity, FlowInterviewLog, FlowInterviewLogEntry, FlowStageRelation,
HealthCareDiagnosis, HealthCareProcedure, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,


### Standard Objects FlowRecordVersion

**Field Name** **Details**

HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument, Image, Individual,
IndividualApplication, InstalledMobileApp, Invoice, InvoiceLine, Lead, ListEmail,
ListEmailIndividualRecipient, ListEmailRecipientSource, Location,
LocationTrustMeasure, MarketSegment, MarketSegmentActivation,
MatchingInformation, MemberPlan, MessagingDeliveryError, MessagingEndUser,
MktCalculatedInsight, MktSgmntActvtnAudAttribute,
MktSgmntActvtnContactPoint, Note, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, OpportunityPartner, Order,
OrderItem, OrgMetric, OrgMetricScanResult, OrgMetricScanSummary,
OtherComponentTask, Partner, PartyConsent, Payment, PaymentAuthAdjustment,
PaymentAuthorization, PaymentGateway, PaymentGatewayLog, PaymentGroup,
PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry,
ProcessException, ProcessInstance, ProcessInstanceNode, Product2,
ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, PromptAction, ProviderSearchSyncLog, PurchaserPlan,
PurchaserPlanAssn, PushTopic, QuickText, QuickTextUsage, ReceivedDocument,
Recommendation, RecordAction, Refund, RefundLinePayment, ReplyText, Report,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, SearchPromotionRule,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SetupAssistantStep,
SharingRecordCollection, SharingRecordCollectionItem,
SharingRecordCollectionMember, Shift, Shipment, ShipmentItem,
SkillRequirement, SocialPersona, SocialPost, Solution, StreamingChannel, Task,
ThreatDetectionFeedback, TimeSlot, TodayGoal, Topic, TopicAssignment,
UnitOfMeasure, UserAppInfo, UserAppMenuCustomization,
UserEmailPreferredPerson, UserProvAccount, UserProvAccountStaging,
UserProvMockTarget, UserProvisioningLog, UserProvisioningRequest, VideoCall,
VideoCallParticipant, VideoCallRecording, Visit, VisitedParty, Visitor, VoiceCall,
VoiceCallRecording, VoiceVendorLine, VolunteerProject, WaveAutoInstallRequest,
WaveCompatibilityCheckItem, WorkAccess, WorkBadge, WorkBadgeDefinition,
WorkOrder, WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup,
WorkTypeGroupMember

### FlowRecordVersion

Represents the version of a flow. This object is available in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`


Standard Objects FlowRecordVersion

Fields

**Field Name** **Details**

`AccessType` Reserved for future use.

```
ActivatedById

ActivatedDate

ApiVersion

AreMetricsLoggedToDataCloud

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that activated the flow. This field is available in API version 60.0
and later.

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
Filter, Nillable, Sort

**Description**
The date and time when the flow was activated. This field is available in API
version 60.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version of the flow record version. This field is available in API version
61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value
is false. This field is available in API version 63.0 and later.


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
Builder

CapacityCategory

DataSpaceId

Description

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Valid values are:

**•** `Cloud Flow Designer`

**•** `Flow Builder`

**•** `Swing Designer`

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the data space for this flow record version. This field is available in API
version 65.0 and later.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow record version. This field is available in API version
61.0 and later.


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
Entries

Errors

Exits

FlowRecordId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of entries in this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of errors in this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of exits from this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent flow running this version.

This field is a relationship field.

**Relationship Name**
FlowRecord

**Relationship Type**
Lookup

**Refers To**
FlowRecord


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
FlowType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The label of a flow type. `FlowType` consolidates `ProcessType` and
`TriggerType` into one field. `FlowType` is used with permissions, so admins
can control access to each flow type. Valid values are:

**•** `Action Cadence Step Screen Flow` —Launches from a cadence
step. This type of flow collects or displays information and requires user
interaction.

**•** `Activation-Triggered Autolaunched Flow` —Launches
when an activation is published. This type of flow runs in the background
without user interaction. This value is available in API version 64.0 and later.

**•** `Action Plan Autolaunched Flow` —Launches an action plan
task from an action plan when conditions in the associated action plan
template process are met. This type of flow runs in the background without
user interaction.

**•** `Admin Automation Event-Triggered Flow` —Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction. This value is available in API version
64.0 and later.

**•** `Agentic Guided Experience Background Flow` —Creates,
retrieves, updates, or deletes records. This autolaunched flow runs in the
background. This value is available in API version 65.0 and later.

**•** `Agentic Guided Experience Orchestration`
`Flow` —Launches when a mobile worker invokes it from the Field Service
mobile app. With Agentic Guided Experience, configure the mobile experience
to follow a tailored work completion process. This value is available in API
version 65.0 and later.

**•** `Agentic Guided Experience Screen Data Flow` —Retrieve
records for use throughout AGX Screen and AGX Orchestration flows. This
autolaunched flow runs in the background. This value is available in API
version 65.0 and later.

**•** `Agentic Guided Experience Screen Flow` —A screen flow
that can launch from an interactive step on an AGX orchestration flow. This
value is available in API version 65.0 and later.

**•** `Autolaunched Approval Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An approval
orchestration lets you create a multi-step, multi-user approval process.

**•** `Autolaunched No Trigger Flow` —Launches when invoked by
processes or code such as Apex and REST API. This type of flow runs in the
background without user interaction.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Autolaunched No Trigger Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An orchestration
lets you create a multi-step, multi-user process.

**•** `Automation Event-Triggered Flow` —Launches when invoked
by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction. This value is available in API version
64.0 and later.

**•** `Automation Event-Triggered Flow` —Launches when an
automation event is received. This type of flow runs in the background
without user interaction.

**•** `Broadcast Flow` —Launches when referenced by Apex, REST API, or
subflow element. This value is available in API version 65.0 and later.

**•** `Cart Async Autolaunched Flow` —Launches when invoked by
a cart change, such as an Add to Cart. This type of flow runs in the background
without user interaction.

**•** `Checkout Screen Flow` —Create a screen flow that implements a
Commerce Cloud checkout process. This type of flow collects or displays
information and requires user interaction.

**•** `CMS Workflow Orchestration Autolaunched` —Launches
when invoked from the Workflows component in a CMS workspace. This
type of orchestration lets you create a multi-step, multi-user process to create,
edit, organize, and manage digital content from a centralized location.

**•** `Contact Request Screen Flow` —Launches when invoked by a
customer, allowing them to enter contact details into a self-service form. This
type of flow collects or displays information and requires user interaction.

**•** `Customer Lifecycle Record-Triggered After Save`
`Flow` —Launches after a customer lifecycle map is saved and changes
records related to the triggering record. This type of flow runs in the
background without user interaction.

**•** `Data Cloud Data Change Flow` —Launches when a record from
a Data Cloud data model object or a calculated insight object is changed and
meets the specified conditions. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Flow` —Launches when conditions are
met in the specified data graph field. This type of flow runs in the background
without user interaction. This value is available in API version 64.0 and later.

**•** `Data Graph-Triggered Flow v0` —Launches when conditions
are met in the specified data graph field. This type of flow runs in the
background without user interaction.

**•** `Digital Form Screen Flow` —Launches from app extensions. This
type of flow collects or displays information and requires user interaction.

**•** `Discovery Framework Data Capture Screen Flow`
`(Beta)` —Launches when invoked by a user on a mobile device and


Standard Objects FlowRecordVersion

**Field Name** **Details**

presents assessment questions from Discovery Framework. This type of flow
collects or displays information and requires user interaction.

**•** `Employee Service Catalog Item Screen Flow` —Launches
when invoked by a user and allows them to browse and order items from
the Employee Service Catalog. This type of flow collects or displays information
and requires user interaction.

**•** `Evaluation Autolaunched Flow` —Launches when invoked by
an orchestration to evaluate custom criteria for a stage or step. To indicate
that the criteria are met, set the output variable
`isOrchestrationConditionMet` to `true` . This type of flow runs
in the background without user interaction.

**•** `External System Change-Triggered Flow Approval`
`Process` —Launches when data changes in a supported external system.
A flow approval process lets you create a multi-step, multi-user approval
process. This value is available in API version 65.0 and later.

**•** `External System Change-Triggered`
`Orchestration` —Launches when data changes in a supported external
system. An orchestration lets you create a multi-step, multi-user process. This
value is available in API version 65.0 and later.

**•** `External System Change-Triggered Flow` —Launches when
an event is received from an external system. This type of flow runs in the
background without user interaction.

**•** `Event-Driven Flow` —Launches when an event is received. This type
of flow runs in the background without user interaction.

**•** `Field Service Mobile Screen Flow` —Launches when invoked
by a user in the Field Service mobile app. This type of flow collects or displays
information and requires user interaction.

**•** `Field Service Web Screen Flow` —Launches from the Field
Service app and lets users schedule, modify, or cancel an appointment in a
web browser. This type of flow requires user interaction.

**•** `Form-Triggered Flow` —Launches when a web visitor submits a
marketing form. This type of flow runs in the background without user
interaction. This value is available in API version 64.0 and later.

**•** `Form-Triggered Flow v0` —Launches when a web visitor submits
a marketing form. This type of flow runs in the background without user
interaction.

**•** `Identity User Registration Autolaunched`
`Flow` —Launches when a user logs in via a single sign-on process that uses
the authentication provider framework. After the third-party identity provider
authenticates the user, the flow creates a user or updates an existing user.
This type of flow runs in the background without user interaction. This value
is available in API version 64.0 and later.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Indicator Result Screen Flow` —Launches a screen flow when
initiated by a user to calculate and create indicator results for a selected
indicator performance period.

**•** `Individual-Object Linking Screen Flow` —Launches when
invoked by an agent to link a record like a case or messaging session to a
contact, lead, person account, or employee. This type of flow collects or
displays information and requires user interaction.

**•** `Login Screen Flow` —Launches when a user tries to log in to
Salesforce. This type of flow extends Salesforce's default authentication
process by sending users with certain profiles through a flow when they log
in and requires user interaction.

**•** `Loyalty Management Autolaunched Flow` —Launches when
invoked by a loyalty program process, and contains Assignment, Decision,
and Action elements. The Action element in this type of flow supports Apex
and quick actions. This type of flow runs in the background without user
interaction.

**•** `Managed Content Autolaunched Flow` —Launches when
invoked by the ManagedContentRelease translator. This type of flow runs in
the background without user interaction.

**•** `Mortgage Lending Screen Flow` —Launches when invoked by
a user and allows them to provide Financial Service Cloud mortgage
application details. This type of flow requires user interaction.

**•** `On-Demand Flow` —Launches when referenced by the REST API. This
autolaunched flow runs asynchronously in the background. This value is
available in API version 65.0 and later.

**•** `Platform Event Triggered Flow` —Launches when a platform
event occurs. This type of flow runs in the background without user
interaction.

**•** `Process Builder Autolaunched Process` —Launched when
invoked from a Process Builder process. This type of flow runs in the
background without user interaction.

**•** `Process Builder Custom Event Process` —A process created
in Process Builder that launches when a custom event message is received.
This type of process runs in the background without user interaction.

**•** `Process Builder Workflow` —Launches when a record is created
or updated. This type of process runs in the background without user
interaction.

**•** `Prompt Template Capability-Triggered Flow` —Launches
from a prompt template. This type of flow adds prompt instructions to the
associated prompt template and runs in the background without user
interaction.

**•** `Recommendation Strategy Autolaunched Flow` —Build a
personalized list of recommendations. When a recommendation is selected,
it launches its assigned flow. Used by Einstein Next Best Action. Show


Standard Objects FlowRecordVersion

**Field Name** **Details**

recommendations in Lightning App Builder with the Einstein Next Best Action
component and in Experience Builder with the Suggested Actions component.

**•** `Record-Triggered After Save Flow` —Launches after a record
is created or updated and has been saved. This type of flow can make changes
only to records related to the triggering record and runs in the background
without user interaction.

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered Before Delete Flow` —Launches when a
record is deleted. This type of flow runs in the background without user
interaction.

**•** `Record-Triggered Before Save Flow` —Launches after a record
is created or updated, but hasn't been saved. This type of flow can make
changes only to the triggering record and runs in the background without
user interaction.

**•** `Routing Autolaunched Flow` —Launches when a customer initiates
a chat, voice, or messaging conversation and routes the work item to a queue,
skill, agent, or bot. This type of flow runs in the background without user
interaction.

**•** `Schedule-Triggered Flow` —Launches at a specified time and
frequency for each record that meets the flow criteria. This type of flow runs
in the background without user interaction.

**•** `Scheduler Appointments Screen Flow` —Launches when
invoked by a user and lets them schedule appointments in Salesforce
Scheduler. This type of flow collects or displays information and requires user
interaction.

**•** `Screen Flow` —Launches from Lightning pages, Experience Cloud sites,
quick actions and more. This type of flow collects or displays information and
requires user interaction.

**•** `Segment-Triggered Flow` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction. This value is available in API
version 64.0 and later.

**•** `Segment-Triggered Flow v0` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction.

**•** `Survey Enrich Autolaunched Flow` —Launches in the context
of a survey response and can't execute without a corresponding survey. Use


Standard Objects FlowRecordVersion

**Field Name** **Details**

it to conditionally map a response to a record, create records, or send
notifications. This type of flow runs in the background without user
interaction.

**•** `Survey Screen Flow` —Launches when invoked by an internal or
external survey participant. This type of flow saves participant feedback as
survey response records and requires user interaction.

**•** `Transaction Security Autolaunched Flow` —Used by
Condition Builder to declaratively build customized security policies to protect
data. This type of flow runs in the background without user interaction.

**•** `User Provisioning Screen Flow` —Launches when invoked by
a user and allows them to create a user account and link it to a third-party
service or app. This type of flow requires user interaction.

This field is available in API version 60.0 and later.

```
Id

IsOverridable

IsPaused

IsTemplate

```

**Type**
text

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow version.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is overridable. The default value is
`false` . This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment-triggered flow is paused ( `true` ) or not ( `false` ).
When the value is `true`, no additional records are processed until the flow is
resumed. The default value is `false` . This field is available in API version 60.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Description**
Indicates whether the flow record version is a template. Template flow record
versions are automatically shared with all users in your Salesforce org. The default
value is `false` . This field is available in API version 61.0 and later.

```
OverriddenById

OverriddenFlowId

PausedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that’s overriding the current flow. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
text

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that the current flow is overriding. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Description**
The date and time the segment-triggered flow was paused. This field is available
in API version 60.0 and later.

```
PausingUserId

ProgressStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who paused the segment-triggered flow. This field is available
in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
PausingUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The running status of the flow. Valid values are:

**•** `Canceled`  - Specifies a flow that was deactivated by a user. The flow
doesn’t process previously added records and no additional records are added
to this flow.

**•** `Completed`  - Indicates a flow that is complete. No additional records are
eligible to be processed in this flow.

**•** `Draft`  - Indicates a flow that is under construction and isn’t active yet.
This status can be invalid because it needs additional information before a
user can activate it.

**•** `Error`  - Indicates a flow that has been deactivated because it encountered
an error. When the error occurs, the error details are emailed to up to 5 users
with the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`  - Indicates a flow that was deactivated by a user, but is
finishing records previously added that are eligible to run to completion. No
additional records are added to this flow.

**•** `InProgress`  - Indicates a flow that is running or ready to run.

**•** `PreparingData`  - Indicates a flow that is preparing the resources it
requires to run. This process can take up to 2 hours.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Scheduled`                       - Indicates a flow scheduled to start on the date and time
selected by the user.

```
ReasonPaused

ResumedDate

ResumingUserId

RunInMode

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason the segment-triggered flow was paused. This field is available in API
version 60.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the segment-triggered flow resumed. This field is available in
API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who resumed the segment-triggered flow. This field is available
in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ResumingUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the flow runs in. Valid values are:

**•** `DefaultMode` —The flow record version runs in system or user context,
depending on how the flow is launched.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `SystemModeWithSharing` —The flow record version always runs in
system mode with sharing. The flow respects org-wide default settings, role
hierarchies, sharing rules, manual sharing, teams, and territories. But it doesn’t
respect object permissions, field-level access, or other permissions of the
running user.

**•** `SystemModeWithoutSharing` —The flow record version can access
all data. In the UI, this value appears as System Context without
Sharing—Access All Data. This value is available in API version 49.0 and later.

This field is available in API version 61.0 and later.

```
ScheduledStartDate

SourceTemplateId

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the flow started. This field is available in API version 60.0 and
later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template from which the current flow was created. This field is
available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The flow’s status. Valid values are:

**•** `Active`

**•** `Draft`

**•** `InvalidDraft`


### Standard Objects FlowRecordVersionOccurrence

**Field Name** **Details**

**•** `Obsolete`

**•** `UnderReview`                       - This value is available in API version 64.0 and later.

This field is available in API version 61.0 and later.

```
TriggerObjectOrEventLabel

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is
available in API version 61.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the flow version.

### FlowRecordVersionOccurrence

Represents an instance of a recurring flow that runs on a schedule. For example, a flow that runs weekly on Wednesdays creates an
occurrence each time it runs. This object is available in API version 60.0 and later.

Supported Calls

`describe()`, `read()`

Fields

**Field** **Details**

```
DataSpaceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the data space for this occurence. This field is available in API version 65.0
and later.

This field is a relationship field.


Standard Objects FlowRecordVersionOccurrence

**Field** **Details**

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Entries

Errors

ErrorDetail

Exits

FlowRecordId

FlowRecordVersionId

```

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of entries for this occurrence.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of errors for this occurrence.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the error. This field is available in API version 63.0 and later.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of exits for this occurrence.

**Type**
string

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated flow record.

**Type**
string


Standard Objects FlowRecordVersionOccurrence

**Field** **Details**

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated version of the flow record.

```
ProgressStatus

ScheduledDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The running status of the flow interview.

Valid values are:

**•** `Canceled`

Specifies a flow interview that was deactivated by a user. The flow doesn’t process
previously added records and no additional records are added to this flow.

**•** `Completed`

Indicates a flow interview that is complete. No additional records are eligible to
be processed in this flow.

**•** `Error`

Indicates a flow interview that has been deactivated because it encountered an
error. When the error occurs, the error details are emailed to up to 5 users with
the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`

Indicates a flow interview that was deactivated by a user, but is finishing records
previously added that are eligible to run to completion. No additional records are
added to this flow.

**•** `InProgress`

Indicates a flow interview that is running or ready to run.

**•** `PreparingData`

Indicates a flow interview that is preparing the resources it requires to run. This
process can take up to 2 hours.

**Type**
dateTime

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The scheduled time and date of the occurrence.


### Standard Objects FlowTestResult

**Field** **Details**

```
Stopped

### FlowTestResult

```

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of flows that were stopped for this occurrence.

Represents the results for a flow test associated with a flow version. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To view test run details, you must have the View All Data user permission. You can view flow tests and test results without the View All
Data permission.

Fields

**Field** **Details**

`Error` Reserved for future use.

`FailedAssertions` Reserved for future use.

```
FlowDefinitionViewId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView


Standard Objects FlowTestResult

**Field** **Details**

```
FlowTestViewId

FlowVersionNumber

FlowVersionViewId

Name

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow test associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowTestView

**Relationship Type**
Lookup

**Refers To**
FlowTestView

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number for the flow.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow version associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the flow test result.


Standard Objects FlowTestResult

**Field** **Details**

```
OwnerId

Result

TestEndDateTime

TestStartDateTime

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns this test result.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the flow test result.

Possible values are:

**•** `Error`

**•** `Fail`

**•** `Pass`

**•** `Skip` —The test run was skipped because the test doesn’t exist for that flow version.
This value appears only when you trigger tests by using Salesforce CLI. This value is
available in API version 66.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test started.


### Standard Objects FlowTestView

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowTestResultShare**

Sharing is available for the object.

### FlowTestView

Represents the description of a flow test associated with a flow definition. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
Description

DurableId

FlowDefinitionViewId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow test associated with the flow test view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow test associated with this flow test view.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test view.

This is a relationship field.

**Relationship Name**
FlowDefinitionView


### Standard Objects FlowStageRelation

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

```
FlowTestApiName

FlowTestLabel

### FlowStageRelation

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow test associated with the flow test view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow test associated with the flow test view.

Represents a relationship between a paused flow interview and its stages. When a flow interview is paused, Salesforce creates a
### FlowStageRelation record for each stage that’s set to the $Flow.CurrentStage or $Flow.ActiveStages global variable.

Available in API version 43.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.


Standard Objects FlowStageRelation

**Field** **Details**

```
ParentId

StageLabel

StageOrder

StageType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the stage. If the stage is translated, the label respects the language of the user who
is querying the label.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The order of this stage when the flow interview was paused. This order may differ from the
order in the stage definition.

**•** If the type is Active, the order corresponds to the order of the stage in
`$Flow.ActiveStages` .

**•** If the type is Current and corresponds to an active stage, the order matches the order of
the active stage.

**•** If the type is Current and doesn't correspond to an active stage, the order is 0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of stage. The valid values are:


### Standard Objects FlowVariableView

**Field** **Details**

**•** Current: Identifies that the stage is set to `$Flow.CurrentStage` .

**•** Active: Identifies that the stage is set to `$Flow.ActiveStages` .

Usage

You can use the FlowStageRelation records to represent the paused interview and its active and current stages visually.

For example, an Online Purchasing flow interview starts with several stages in $Flow.ActiveStages. If the interview is paused, Salesforce
creates a FlowStageRelation record for each stage in `$Flow.ActiveStages` or `$Flow.CurrentStage` .

### FlowVariableView

Represents a variable within the flow version. This object is available in API version 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApiName

DataType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow variable.

**Type**
string


Standard Objects FlowVariableView

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data type of the flow variable. Valid values are:

**•** `Apex` —This value is available in API version 46.0 and later.

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —This value is available in API version 30.0 and later.

**•** `Number`

**•** `Multipicklist` —This value is available in API version 34.0 and later.

**•** `Picklist` —This value is available in API version 34.0 and later.

**•** `String`

**•** `sObject`

```
Description

DurableId

FlowVersionViewId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow variable information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Id of the flow variable.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Id of the flow version.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup


### Standard Objects FlowVersionView

**Field** **Details**

**Refers To**
### FlowVersionView

```
IsCollection

IsInput

IsOutput

ObjectType

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is a collection of values.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicated whether or not the flow variable is available for input.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is available for output.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the data type is sObject, this field indicates which object.

### Use this object to query information about flow variables. A query must be filtered by FlowVersionViewId to get results. Only

variables with IsInput or IsOutput marked as true are visible.

### FlowVersionView

Represents the version of a flow definition. This object is available in API version 46.0 and later.


Standard Objects FlowVersionView

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApiVersion

ApiVersionRuntime

AreMetricsLoggedToDataCloud

CapabilityType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for the flow definition. Every flow version has an API version specified
at creation.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for running the flow. This value determines which versioned run-time
behavior improvements are adopted by the flow version.

If not specified when the flow or flow version is created, the latest available API version
is used as the API version for running the flow. When an existing flow is saved as a
new flow or flow version, the existing flow’s run-time API version is used in the new
flow or flow version.

This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowVersionView

**Field** **Details**

**Description**
The capability that integrates with the flow. An example value is
`PromptTemplateType://SalesEmail` .

```
CapacityCategory

Description

DurableId

FlowDefinitionViewId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow version information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition.

This field s a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView


Standard Objects FlowVersionView

**Field** **Details**

```
IsSwingFlow

IsTemplate

Label

ProcessType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

Default: false

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. When installed from managed
packages, processes and flows can’t be viewed or cloned by subscribers because of
intellectual property (IP) protection. But when those processes and flows are templates,
subscribers can open them in a builder, clone them, and customize the clones.
Available in API version 46.0 and later.

Default: false

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow executed when a user
completes a cadence step. This value is available in API version 56.0 and later.


Standard Objects FlowVersionView

**Field** **Details**

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This
value is available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API
version 44.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 63.0 and later.

**•** `ApprovalWorkflow` —An orchestration for approvals. This value is available
in API version 62.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request that customer
support get back to them. This flow is used to create contact request records.
This value is available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate
survey questions with different stages in customer lifecycles. This value is available
in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent` —A process that is invoked when it receives a platform event
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow` —A flow that configures the Form tab on Work Order
Overview or the related list for a service appointment or a work order line item.
This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value
is available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more
screens or local actions, choices, or dynamic choices. In the UI and Salesforce
Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.


Standard Objects FlowVersionView

**Field** **Details**

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is
available in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration
and updates for single sign-on with the authentication provider framework.
Available in API version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow` —A screen flow that helps search for
contacts, leads, person accounts, and employees and links them to support
interactions. This value is available in API version 58.0 and later.

**•** `InvocableProcess` —A process that can be invoked by another process or
the Invocable Actions resource in REST API. This value is available in API version
38.0 and later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app and
can be invoked by loyalty program processes. This value is available in API version
54.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder
and the flow. This value is available in API version 60.0 and later.

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business
logic. This value is available in API version 52.0 and later.

**•** `StageManagementEvaluationFlow` —A flow for evaluating custom
criteria for a stage or step in Stage Management. This value is available in API
version 63.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created
in Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper.
From the UI, this type of flow is created in the Survey Builder and requires an
associated survey flow type. This value is available in API version 49.0 or later and
only when the Customer Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In
the UI and Salesforce Help, it’s a record change process.

These values are reserved for future use.

**•** `ActionCadenceFlow`

**•** `ActionPlan`

**•** `ActivitySmartMatchingFlow`

**•** `AppProcess`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `Journey`

**•** `JourneyBuilderIntegration`


Standard Objects FlowVersionView

**Field** **Details**

**•** `LoginFlow`

**•** `ManagedContentFlow`

**•** `OrchestrationFlow`

**•** `RecommendationStrategy`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that
the flow contains only elements, resources, and functionality that the new flow type
supports.

```
RunInMode

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the flow runs in. Valid values are:

**•** DefaultMode — The flow version runs in system or user context, depending on
how the flow is launched.

**•** SystemModeWithSharing — The flow version always runs in system mode with
sharing. The flow respects org-wide default settings, role hierarchies, sharing
rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The flow’s status.

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**•** `UnderReview`


### Standard Objects Folder

**Field** **Details**

```
VersionNumber

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s version number.

Use this object to query information about flow versions. A query must be filtered by `DurableId` or `FlowDefinitionViewId`
to get results.

### Folder

Represents a repository for a Dashboard, Document, EmailTemplate, Macro, QuickText, or Report. Only one type of item can be contained
in a folder.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

**•** You must have the “Modify All Data” permission to create, update, or delete document folders and email template folders.

**•** Guest and Customer Portal users can’t access this object.

**•** To query this object, no special permissions are needed.

**•** As of API version 35.0, when a folder is shared with a role, it is only visible to users in that role. Superior roles in the role hierarchy
don’t gain visibility.

**•** If analytics folder sharing is turned on, then users need these permissions to create and manage report folders and dashboard folders:

**–** “ `Create Dashboard Folders` ”

**–** “ `Create Report Folders` ”

**•** To use folders for macros and quick text, enable folders for these objects in Setup on the Macro Settings and Quick Text Settings
pages.


Standard Objects Folder

Fields

**Field** **Details**

```
AccessType

DeveloperName

IsReadonly

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Indicates who can access the Folder. Available values include:

**•** `Hidden` —Folder is hidden from everyone.

**•** `Public` —Folder is accessible by all users.

**•** `Shared` —Folder is accessible only by a User in a particular Group or UserRole. The API
doesn’t allow you to view, insert, or update which group or Role the Folder is shared
with.

Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Folder Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this Folder is read-only ( `true` ) or editable ( `false` ). Label is _`Read`_
_`Only`_ .

Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.


Standard Objects Folder

**Field** **Details**

```
Name

NamespacePrefix

ParentId

Type

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the folder as it appears in the user interface. Label is **Document Folder Label** .

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

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the parent object, if any.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of objects contained in the Folder. This field can’t be updated. Available values
include:

**•** `Dashboard`

**•** `Document`


### Standard Objects FolderedContentDocument

**Field** **Details**

**•** `Email` (for Salesforce Classic email templates)

**•** `EmailTemplate` (for Lightning email templates)

**•** `Macro`

**•** `QuickText`

**•** `Report`

Usage

Only one type of item can be contained in a folder, either Dashboard, Document, EmailTemplate, Macro, QuickText, or Report.

SEE ALSO:

Overview of Salesforce Objects and Fields

### FolderedContentDocument

Represents the relationship between a parent and child ContentFolderItem in a ContentWorkspace.

Supported Calls

```
   describeSObjects()

```

Fields

**Field Name** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the ContentDocument that can be in a folder.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument


Standard Objects FolderedContentDocument

**Field Name** **Details**

```
ContentSize

ContentSizeLong

FileExtension

FileType

IsFolder

ParentContentFolderId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for files smaller than 2 GB.

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the ContentDocument.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File type of the ContentDocument.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the FolderedContentDocument is a folder, rather than a file.

**Type**
reference


### Standard Objects ForecastingAdjustment

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the ContentFoldr the ContentDocument resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

```
Title

### ForecastingAdjustment

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Name of the file or folder in a ContentFolder.

This object represents an individual forecast manager’s adjustment for a subordinate’s or child territory’s forecast via a ForecastingItem.
Available in API versions 26.0 and later. This object is different from the ForecastingOwnerAdjustment object, which represents forecast
users’ adjustments of their _own_ forecasts, including territory forecasts they own.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.


Standard Objects ForecastingAdjustment

Fields

**Field Name** **Details**

```
AdjustedAmount

AdjustedQuantity

AdjustmentNote

CurrencyIsoCode

ForecastCategoryName

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment. This
field is available in API version 28.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field doesn’t appear in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the user’s personal
currency.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category within the sales cycle that an opportunity is assigned to based on
its opportunity stage. The standard forecast categories are Pipeline, Best Case,


Standard Objects ForecastingAdjustment

**Field Name** **Details**

Commit, Omitted, and Closed. You can add a Most Likely category and can
customize forecast category names in single category rollups. The forecast
categories display information for that specific category; for example, Best Case
only reflects amounts in the Best Case category.

```
ForecastingGroupItemId

ForecastingItemCategory

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the manager adjustment belongs to. This field is a relationship field. Available in
API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly` —Rollup from Pipeline opportunities only.

**•** `BestCaseOnly` —Rollup from Best Case opportunities only. The value
in this category is adjustable.

**•** `MostLikelyOnly` —Rollup from Most Likely opportunities only. The
value in this category is adjustable.

**•** `CommitOnly` —Rollup from Commit opportunities only. The value in
this category is adjustable.

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline` —Rollup from Pipeline, Best Case, Most Likely, and
Commit opportunities.

**•** `BestCaseForecast` —Rollup from Best Case, Most Likely, Commit,
and Closed opportunities. The value in this category is adjustable.

**•** `MostLikelyForecast` —Rollup from Most Likely, Commit, and
Closed opportunities. The value in this category is adjustable.


Standard Objects ForecastingAdjustment

**Field Name** **Details**

**•** `CommitForecast` —Rollup from Commit and Closed opportunities.
The value in this category is adjustable.

**For either cumulative or individual forecast category rollups, the possible**
**values are:**

**•** `ClosedOnly` —Rollup from Closed opportunities only.

```
ForecastingItemId

ForecastingTypeId

IsAmount

IsQuantity

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` . This field is available in API version 28.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` . This field is available in API version 28.0 and later.

**Type**
reference

**Properties**
Create,Defaulted on create, Filter, Group, Sort


Standard Objects ForecastingAdjustment

**Field Name** **Details**

**Description**

The ID of the forecast owner.

```
PeriodId

ProductFamily

StartDate

Territory2Id

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the adjustment. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only. This field is available in API
version 29.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to obtain a manager’s adjustment detail for a specified ForecastingItem. The ForecastingAdjustment object is visible to
all users, but only forecast managers and users above them in the forecast hierarchy can read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType


### Standard Objects ForecastingColumnDefinition

object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

The `ForecastingItemCategory` field differs from the `ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category of the _underlying opportunities_ rolling up to forecast
amounts. In organizations using cumulative forecast rollups, the `ForecastCategoryName` field can be null because the
cumulative forecast amounts include opportunities from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of rollup_ a forecast amount or adjustment is from. In
organizations using individual forecast category columns, it contains the individual forecast rollup categories. In organizations using
cumulative forecast rollups, it contains the cumulative rollup categories.

When inserting manager adjustments, the values you insert for `ForecastCategoryName` and `ForecastingItemCategory`
must be compatible with each other. In organizations using cumulative forecast rollups, the `ForecastCategoryName` is nillable.
The following pairs are valid.

**For individual forecast category rollups:**

**•** `ForecastCategoryName` : `BestCase`, `ForecastingItemCategory` : `BestCaseOnly`

**•** `ForecastCategoryName` : `MostLikely`, `ForecastingItemCategory` : `MostLikelyOnly`

**•** `ForecastCategoryName` : `Commit`, `ForecastingItemCategory` : `CommitOnly`

**For cumulative forecast category rollups:**

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `BestCaseForecast`

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `MostLikelyForecast`

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `CommitForecast`

SEE ALSO:

ForecastingFact

ForecastingItem

ForecastingQuota

### ForecastingColumnDefinition

Represents a custom calculated column or a custom reference data column in a forecast type. This object is available in API version 56.0
and later.

For a custom calculated column, a `Formula` field value is required. For a custom reference data column, a `ReferenceField` field
value is required.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ForecastingColumnDefinition

Fields

**Field** **Details**

```
DeveloperName

ForecastingTypeId

Formula

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer (API) name of the custom calculated column or custom reference data column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for custom calculated columns. The formula for the custom calculated column.
Use API column names in your formula (such as ForecastAmount0), not column header
names (such as Closed or Closed Only). For details on API column names, operators, and
functions to use in formulas, see ForecastingColumnDefinition Formula Field Details.

**Example**
The following formula calculates the gap to quota: `ForecastingQuotaAmount -`

```
  ForecastAmount0

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the custom calculated column or custom reference data column.


Standard Objects ForecastingColumnDefinition

**Field** **Details**

```
MasterLabel

ReferenceField

ResultField

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object, which displays in Setup and in the column header on the forecasts
page. The label is in the default language locale for the organization. If there’s no default
language locale, the label is in en_US.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required for custom reference data columns. The number or currency custom field from the
ForecastingCustomData object. For example,
`ForecastingCustomData.Realized_Revenue__c` . Data from this field appears
in a column in the forecasts summary. This field is available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The field name to represent the custom calculated column or custom reference data column
result. Possible values are:

**Custom Calculated Column Result**

**•** CalculatedAmount0 or CalculatedQuantity0

**•** CalculatedAmount1 or CalculatedQuantity1

**•** CalculatedAmount2 or CalculatedQuantity2

**•** CalculatedAmount3 or CalculatedQuantity3

**•** CalculatedAmount4 or CalculatedQuantity4

If the formula’s result is null or invalid, “-” is the value. For example, if the formula divided by
0. If you want to show “-” for 0 or negative values in your forecast, use the IF function in your
formula to detect 0 or negative numbers.

**Custom Reference Data Column Result** Use the appropriate field based on whether your
column output is of Currency or Number type.

**•** ExtensionCurrency0 or ExtensionNumber0

**•** ExtensionCurrency1 or ExtensionNumber1

**•** ExtensionCurrency2 or ExtensionNumber2

**•** ExtensionCurrency3 or ExtensionNumber3


#### Standard Objects ForecastingColumnDefinition Formula Field Details

**Field** **Details**

**•** ExtensionCurrency4 or ExtensionNumber4

Usage

Each forecast type can include any combination of custom calculated columns and reference data columns, as long as they don’t exceed
five in number. For example, a forecast type can have two custom calculated columns and three custom reference data columns.

Custom calculated columns can’t be adjusted and aren’t included in rollups. In the UI, custom calculated columns can’t indicate changes
in the last 7 days.

If you have at least one custom calculated column in an active or inactive forecast type, you can’t do the following until you’ve removed
the column.

**•** Switch from single category to cumulative rollups in Forecast Settings

**•** Enable the Most Likely category

**•** Disable Show Quotas (only if your custom calculated column’s formula refers to a quota value)

#### ForecastingColumnDefinition Formula Field Details

Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

#### ForecastingColumnDefinition Formula Field Details

Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

**API Column Names – General**

**•** ForecastingQuotaAmount – Quota (currency)

**•** ForecastingQuotaQuantity – Quota quantity (double)

**•** _`DeveloperName`_ of any custom calculated column or custom reference data column shown in the forecasts page

**API Column Names for Forecast Category Columns**

If the Most Likely category isn’t enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Best Case

**•** ForecastAmount3 or ForecastQuantity3 – Pipeline

If the Most Likely category is enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – Best Case


Standard Objects ForecastingColumnDefinition Formula Field Details

**•** ForecastAmount4 or ForecastQuantity4 – Pipeline

**API Column Names for Adjustment Columns – Original Forecast Value Without Adjustments**

If your org shows adjustments in columns, use these API column names for the original forecast value without adjustments. Adjustment
columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Most Likely

**•** AmountWithoutAdjustments3 or QuantityWithoutAdjustments3 – Best Case

**API Column Names for Adjustment Columns – Team Adjustment Value**

If your org shows adjustments in columns, use these API column names for the team’s adjusted value that includes a subordinate’s
owner and manager adjustments, but not a forecast manager’s owner and manager adjustments. These adjustment columns are
available in API version 61.0 and later.

If the Most Likely category isn’t enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Best Case

If the Most Likely category is enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Most Likely

**•** SubordinateOverrideAmount3 or SubordinateOverrideQuantity3 - Best Case

Use these API column names for the team’s adjusted value that includes owner adjustments without manager adjustments. The
adjustment value includes a subordinate’s manager adjustments that they made. These adjustment columns are available in API
version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Most Likely

**•** AmountWithoutManagerAdjustment3 or QuantityWithoutManagerAdjustment3 – Best Case

**API Column Names for Adjustment Columns – My Adjusted Value**

The column that represents the adjusted value from the forecast user viewing the page is the same as the API column name for the
standard forecast category. Adjustment columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Best Case

If the Most Likely category is enabled:


### Standard Objects ForecastingColumnDefinitionLocalization

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – My Best Case

**API Column Names for Custom Reference Data**

Use the appropriate field based on whether the custom reference data is of Currency or Number type.

**•** ExtensionCurrency0

**•** ExtensionCurrency1

**•** ExtensionCurrency2

**•** ExtensionCurrency3

**•** ExtensionCurrency4

**•** ExtensionNumber0

**•** ExtensionNumber1

**•** ExtensionNumber2

**•** ExtensionNumber3

**•** ExtensionNumber4

**Supported Math Operators**

**•** + (Add) – Calculates the sum of two values.

**•**     - (Subtract) – Calculates the difference of two values.

**•**     - (Multiply) – Multiplies its values.

**•** / (Divide) – Divides its values.

**•** () (Open Parenthesis and Closed Parenthesis) – Specifies that the expressions within the open parenthesis and close parenthesis
are evaluated first. All other expressions are evaluated using standard operator precedence.

**Supported Logical Operators**

**•** = and == (Equal) – Evaluates if two values are equivalent. The = and == operators are interchangeable.

**•** <> and != (Not Equal) – Evaluates if two values aren’t equivalent.

**•** < (Less Than) – Evaluates if a value is less than the value that follows this symbol.

**•**     - (Greater Than) – Evaluates if a value is greater than the value that follows this symbol.

**•** <= (Less Than or Equal) – Evaluates if a value is less than or equal to the value that follows this symbol.

**•** >= (Greater Than or Equal) – Evaluates if a value is greater than or equal to the value that follows this symbol.

**Supported Functions**

**•** IF – Determines if expressions are true or false. Returns a given value if true and another value if false.

**•** NULL can be used as a constant. For example, `IF((expression) < 0, NULL, (expression)).`

### ForecastingColumnDefinitionLocalization

Represents the translated value of a custom calculated column or custom reference data column label when the Translation Workbench
is enabled for your organization. This object is available in API version 56.0 and later.


Standard Objects ForecastingColumnDefinitionLocalization

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Translation Workbench must be enabled for your org.

Fields

**Field** **Details**

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language of the translated label.

Possible values are:

**•** `af` —Afrikaans

**•** `am` —Amharic

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)

**•** `ar_EG` —Arabic (Egypt)

**•** `ar_IQ` —Arabic (Iraq)

**•** `ar_JO` —Arabic (Jordan)

**•** `ar_KW` —Arabic (Kuwait)

**•** `ar_LB` —Arabic (Lebanon)

**•** `ar_LY` —Arabic (Libya)

**•** `ar_MA` —Arabic (Morocco)

**•** `ar_OM` —Arabic (Oman)

**•** `ar_QA` —Arabic (Qatar)

**•** `ar_SA` —Arabic (Saudi Arabia)

**•** `ar_SD` —Arabic (Sudan)

**•** `ar_SY` —Arabic (Syria)

**•** `ar_TN` —Arabic (Tunisia)

**•** `ar_YE` —Arabic (Yemen)

**•** `bg` —Bulgarian


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh

**•** `da` —Danish

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `el_CY` —Greek (Cyprus)

**•** `en_AE` —English (United Arab Emirates)

**•** `en_AU` —English (Australian)

**•** `en_BE` —English (Belgium)

**•** `en_CA` —English (Canadian)

**•** `en_CY` —English (Cyprus)

**•** `en_DE` —English (Germany)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IL` —English (Israel)

**•** `en_IN` —English (Indian)

**•** `en_MT` —English (Malta)

**•** `en_MY` —English (Malaysian)

**•** `en_NL` —English (Netherlands)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `eo` —Esperanto (Pseudo)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `es_CR` —Spanish (Costa Rica)

**•** `es_DO` —Spanish (Dominican Republic)

**•** `es_EC` —Spanish (Ecuador)

**•** `es_GT` —Spanish (Guatemala)

**•** `es_HN` —Spanish (Honduras)

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)

**•** `es_PA` —Spanish (Panama)

**•** `es_PE` —Spanish (Peru)

**•** `es_PR` —Spanish (Puerto Rico)

**•** `es_PY` —Spanish (Paraguay)

**•** `es_SV` —Spanish (El Salvador)

**•** `es_US` —Spanish (United States)

**•** `es_UY` —Spanish (Uruguay)

**•** `es_VE` —Spanish (Venezuela)

**•** `et` —Estonian

**•** `eu` —Basque

**•** `fa` —Farsi

**•** `fi` —Finnish

**•** `fr` —French

**•** `fr_BE` —French (Belgium)

**•** `fr_CA` —French (Canadian)

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `fr_MA` —French (Morocco)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `haw` —Hawaiian

**•** `hi` —Hindi

**•** `hmn` —Hmong

**•** `hr` —Croatian

**•** `ht` —Haitian Creole

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `iw` —Hebrew

**•** `iw_EO` —Esperanto RTL (Pseudo)

**•** `ja` —Japanese

**•** `ji` —Yiddish

**•** `ka` —Georgian

**•** `kk` —Kazakh

**•** `kl` —Greenlandic

**•** `km` —Khmer

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo

**•** `mk` —Macedonian

**•** `ml` —Malayalam

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pa` —Punjabi

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `ru_AM` —Russian (Armenia)

**•** `ru_BY` —Russian (Belarus)

**•** `ru_KG` —Russian (Kyrgyzstan)

**•** `ru_KZ` —Russian (Kazakhstan)

**•** `ru_LT` —Russian (Lithuania)

**•** `ru_MD` —Russian (Moldova)

**•** `ru_PL` —Russian (Poland)


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `ru_UA` —Russian (Ukraine)

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sm` —Samoan

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_MY` —Chinese (Malaysia)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
NamespacePrefix

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


### Standard Objects ForecastingCustomCategory

**Field** **Details**

field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
ParentId

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related custom column definition. This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ForecastingColumnDefinition

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The translated label of the custom calculated column or custom reference data column.

### ForecastingCustomCategory

Represents a custom forecasting category used for forecast rollups. This object is available in API version 62.0 and later.

In API version 62.0, this object is available for rollup of Manager Judgments only.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects ForecastingCustomCategory

Fields

**Field** **Details**

```
CanHaveQuotas

Description

DeveloperName

DisplayPosition

ForecastingSourceDefinitionId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecasts in the custom category can have quotas. The default value is
`false` . Available in API version 63.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user-defined description of the custom category.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the custom category.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the placement of the custom category column among the other columns on the
forecasts page.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the forecasting source definition.

This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition


Standard Objects ForecastingCustomCategory

**Field** **Details**

**Refers To**
ForecastingSourceDefinition

```
ForecastingTypeId

IsAdjustable

IsAmount

IsHidden

IsOwnerAdjustable

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ForecastingType.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecast managers can adjust forecasts in the custom category. The default
value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, then `IsQuantity`
must be `true` . The default value is `false` . Available in API version 63.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom category is hidden. The default value is `false` . Available in
API version 63.0 and later.

**Type**
boolean


Standard Objects ForecastingCustomCategory

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether all forecast users can adjust their own forecasts in the custom category,
including the territory forecasts that they own. The default value is `false` .

```
IsQuantity

Language

MasterLabel

MeasureFieldOverride

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then `IsAmount`
must be `true` . The default value is `false` . Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom category.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for this column. The label is in the default language locale for the organization. If
there’s no default language locale, the label is in en_US.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The measure that this custom category supports.

Possible values are:

**•** `Opportunity.Amount`

**•** `Opportunity.AmountCustom__c`

**•** `Opportunity.AmountRSF__c`

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.Quantity`


### Standard Objects ForecastingCustomData

**Field** **Details**

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItem.oliCustomAmount__c`

**•** `OpportunityLineItemSplit.SplitAmount`

**•** `OpportunitySplit.SplitAmount`

**•** `OpportunitySplit.customAmount__c`

```
UnitOfMeasure

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unit of measure for the specified custom category measure. Available in API version 63.0
and later.

### ForecastingCustomData

Represents forecast data from external sources to display in the forecasts page. For example, risk or last year’s revenue. This object is
available in API version 58.0 and later.

This object doesn’t support forecast rollups or adjustments. Number and currency columns are supported only.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Available in Enterprise Edition and above, and in Professional Edition with an add-on license. Access to this object requires the Manage
Forecasts Custom Data user permission.

Fields

**Field** **Details**

```
ForecastOwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast owner. This field is a relationship field.


Standard Objects ForecastingCustomData

**Field** **Details**

**Relationship Name**
ForecastOwner

**Relationship Type**
Lookup

**Refers To**
User

```
ForecastingGroupItemId

ForecastingTypeId

PeriodId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that the custom
data belongs to. This field is a relationship field. Available in API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Period ID for the custom data. This field is a relationship field.


### Standard Objects ForecastingDisplayedFamily

**Field** **Details**

**Relationship Name**
Period

**Relationship Type**
Lookup

**Refers To**
Period

```
ProductFamily

StartDate

Territory2Id

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The user-defined product family available to forecast on. Each product family is unique.
Possible values are:

**•** _`[user-defined]`_ –For example, `Electronics` or `Appliances` .

**•** `None`

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The start of the custom data, expressed as month and year. The date can include any day in
a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.

Each record displays as a custom column on the forecasts summary page.

### ForecastingDisplayedFamily

Represents the table in Forecasts Settings where an admin selects the product families that users can forecast on in Lightning Experience.
This object is available in API version 40.0 and later.


### Standard Objects ForecastingFact

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
DisplayPosition

ProductFamily

### ForecastingFact

```

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
