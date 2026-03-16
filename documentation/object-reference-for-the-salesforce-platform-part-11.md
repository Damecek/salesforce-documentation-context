string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive name that makes the sender email address easier to identify.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique system ID of the domain associated with the sender email address.

This field is a relationship field.

**Relationship Name**
EmailDomainKey

**Refers To**
EmailDomainKey

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique identifier for the sender email address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique user ID of the user who owns the sender email address object.

This field is a polymorphic relationship field.


### Standard Objects ServiceAppointment

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
Group, User

```
Username

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The part of the email address that comes before the @ symbol.

### ServiceAppointment

Represents an appointment to complete work for a customer in Field Service, Lightning Scheduler,Intelligent Appointment Management,
and Virtual Care.This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The account associated with the appointment. If the parent record
is a work order or work order line item, this field’s value is inherited from the
parent. Otherwise, it remains blank.

This is a relationship field.

**Relationship Name**
Account


Standard Objects ServiceAppointment

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
ActualDuration

ActualEndTime

ActualStartTime

Address

AppointmentNumber

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that it took the resource to complete the appointment
after arriving at the address. When values are first added to the `Actual`
`Start` and `Actual End` fields, the `Actual Duration` is automatically
populated to list the difference between the `Actual Start` and `Actual`
`End` . If the `Actual Start` and `Actual End` fields are subsequently
updated, the `Actual Duration` field doesn’t re-update, but you can
manually update it.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual date and time the appointment ended.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual date and time the appointment started.

**Type**
address

**Properties**
Filter

**Description**
The address where the appointment is taking place. The address is inherited from
the parent record if the parent record is a work order or work order line item.

**Type**
string


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the appointment.

```
ArrivalWindowEndTime

ArrivalWindowStartTime

BundlePolicyId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the window of time in which the technician is scheduled to arrive at
the site. This window is typically larger than the Scheduled Start and End window
to allow time for delays and scheduling changes. You may choose to share the
Arrival Window Start and End with the customer, but keep the Scheduled Start
and End internal-only.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The beginning of the window of time in which the technician is scheduled to
arrive at the site. This window is typically larger than the Scheduled Start and
End window to allow time for delays and scheduling changes. You may choose
to share the Arrival Window Start and End with the customer, but keep the
Scheduled Start and End internal-only.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the bundle policy associated with this service appointment.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ServiceAppointment

**Field Name** **Details**

```
City

ContactId

Country

Description

DueDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the appointment is completed. Maximum length is 40 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the parent record. If needed, you can manually
update the service appointment contact.

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
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the appointment.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


Standard Objects ServiceAppointment

**Field Name** **Details**

**Description**
The date by which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

```
Duration

DurationType

EarliestStartTime

GeocodeAccuracy

IsAnonymousBooking

```

**Type**
double

**Properties**
Create, Nillable, Filter, Sort, Update

**Description**
The estimated length of the appointment. If the parent record is work order or
work order line item, the appointment inherits its parent’s duration, but it can
be manually updated. The duration is in minutes or hours based on the value
selected in the `Duration Type` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the Duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date after which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
boolean


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a service resource was automatically assigned to the
appointment. The default value is false.

This field is available in API version 49.0 and later.

```
IsBundle

IsBundleMember

IsManuallyBundled

IsOffsiteAppointment

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle service appointment. The default
value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle member service appointment.
The default value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this bundle was created manually. The default value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any type of work that can be done remotely.

This field is available in API version 58.0 and later.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Latitude

Longitude

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with `Longitude` to specify the precise geolocation of the address where
the service appointments is completed. Acceptable values are numbers between
–90 and 90 with up to 15 decimal places.

To integrate data from an external data source for latitude, map your data to the
`ServiceAppointment.Latitude` and not the

```
  ServiceAppointment.FSL__InternalSLRGeolocation__Latitude__s
```

field.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with `Latitude` to specify the precise geolocation of the address where
the service appointment is completed. Acceptable values are numbers between
–180 and 180 with up to 15 decimal places.

To integrate data from an external data source for longitude, map your data to
the `ServiceAppointment.Longitude` and not the

```
  ServiceAppointment.FSL__InternalSLRGeolocation__Longitude__s
```

field.


Standard Objects ServiceAppointment

**Field Name** **Details**

Note: This field is available in the API only.

```
OwnerId

ParentRecordId

ParentRecordStatusCategory

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service appointment.

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
The parent record associated with the appointment. The parent record can’t be
updated after the service appointment is created.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account, Asset, Lead, Opportunity, ServiceAppointmentGroup, WorkOrder,
WorkOrderLineItem

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read only) The `Status Category` of the parent record. If the parent record
is a work order or work order line item, this field is populated; otherwise, it remains
blank.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
ParentRecordType

PostalCode

RelatedBundleId

SchedEndTime

SchedStartTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of parent record: Account, Asset, Lead, Opportunity, Work
Order, or Work Order Line Item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bundle that this service appointment is a member of.

This is a relationship field.

**Relationship Name**
RelatedBundle

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to end. If you are using the Field
Service managed package with the scheduling optimizer, this field is populated
once the appointment is assigned to a resource. `Scheduled End`   `Scheduled Start` = `Estimated Duration` .

**Type**
dateTime


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to start. If you are using the
Field Service managed package with the scheduling optimizer, this field is
populated once the appointment is assigned to a resource.

```
ServiceDocumentTemplate

ServiceTerritoryId

State

Status

```

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
The service territory associated with the appointment. If the parent record is a
work order or work order line item, the appointment inherits its parent’s service
territory.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the service appointment is completed. Maximum length is 80
characters.

**Type**
picklist


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the appointment. The picklist includes the following values, which
can be customized:

**•** `None` —Default value.

**•** `Scheduled` —Appointment has been assigned to a service resource.

**•** `Dispatched` —Assigned service resource has been notified about their
assignment.

**•** `In Progress` —Work has begun.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.

**•** `Canceled` —Work is canceled, typically before any work began

While you can set the status to null via the API, setting the status to null returns
an error. To prevent errors, use one of the picklist values.

```
StatusCategory

Street

Subject

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field’s values are identical to the default `Status` values.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Customer Absent`_ value, you may
decide that it belongs in the _`Cannot Complete`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the service appointment is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short phrase describing the appointment.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
Transaction

WorkTypeId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last transaction ID of the scheduling and optimization request that updated
this object. The transaction ID is automatically generated and populated by the
Enhanced Scheduling and Optimization engine. Available in API version 63.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the service appointment. The work type is inherited
from the appointment’s parent record if the parent is a work order or work order
line item.

Note: If Lightning Scheduler is also in use, this field is editable. However,
users see an error if they update it to list a different work type than the
parent record’s work type.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Service appointments always have a parent record, which can be a work order, work order line item, opportunity, account, or asset. The
type of parent record tells you about the nature of the service appointment:

**•** Service appointments on _work orders_ and _work order line items_ offer a more detailed view of the work being performed. While work
orders and work order line items let you enter general information about a task, service appointments are where you add the details
about scheduling and ownership.

**•** Service appointments on _assets_ represent work being performed on the asset.

**•** Service appointments on _accounts_ represent work being performed for the account.

**•** Service appointments on _opportunities_ represent work that is related to the opportunity.

**•** Service appointments on _leads_ represent work that is related to lead—for example, a site visit to pursue a promising lead.


### Standard Objects ServiceAppointmentStatus

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceAppointmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceAppointmentFeed**

Feed tracking is available for the object.

**ServiceAppointmentHistory**

History is available for tracked fields of the object.

**ServiceAppointmentOwnerSharingRule**

Sharing rules are available for the object.

**ServiceAppointmentShare**

Sharing is available for the object.

### ServiceAppointmentStatus

Represents a possible status of a service appointment in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ApiName

IsDefault

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


Standard Objects ServiceAppointmentStatus

**Field Name** **Details**

**Description**
Indicates that the status value is the default status on service appointments. Only
one status value can be the default.

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
The label for the picklist value that appears in the UI.

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

The Status field on service appointments comes with the following values:

**•** None—Default value.

**•** Scheduled—Appointment has been assigned to a service resource.

**•** Dispatched—Assigned service resource has been notified about their assignment.

**•** In Progress—Work has begun.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Canceled—Work is canceled, typically before any work began

**•** CheckedIn—The customer has arrived for their scheduled appointment.

Important: While you can set the status to null via the API, setting the status to null returns an error. To prevent errors, use one
of the documented picklist values.


### Standard Objects ServiceChannel

The ServiceAppointmentStatus object corresponds to the Status field. Adding a value to the Status field—for example, Waiting—creates
a service appointment status record, and vice versa.

Note: Service appointments also come with a StatusCategory field whose values are identical to the default Status values. If you
create custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_
value, you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory,
[see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ServiceChannel

Represents a channel of work items that are received from your organization—for example, cases, chats, or leads. This object is available
in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AcwExtensionDuration

AfterConvoWorkMaxTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Specify a value from 10 through 3600.
Available only for service channels of type Messaging or Voice.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if `HasAfterConvoWorkTimer` is set
to `true` . Specify a value from 10 through 3600. Available only for service channels of type
Messaging or Voice.


Standard Objects ServiceChannel

**Field** **Details**

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type Messaging, this field is available in API version 56.0 and later.

```
CapacityModel

CustomSoundId

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, RestrictedPicklist, Sort, Update

**Description**
The method that determines when an agent's capacity for a work item is released. With the
Status-Based capacity routing model, work remains assigned and applied to an agent’s
capacity until the work is completed or reassigned to a different agent. In contrast, the
tab-based capacity model releases an agent’s capacity when a work tab is closed in the
service console. Possible values are StatusBased and TabBased.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  CustomSound

```

**Relationship Type**
Lookup

**Refers To**

```
  StaticResource

```

**Description**
The ID of the static resource for the custom sound selected to play for the
`PresenceUserConfig` object.

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

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.


Standard Objects ServiceChannel

**Field** **Details**

```
DoesCheckCapOnOwnerChange

DoesCheckCapOnStatusChange

DoesMinimizeWidgetOnAccept

DoesOverridePresenceAudio

HasAcwExtensionEnabled

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reassigned to a specific agent, you
can choose to override the capacity check and keep the work assigned to the agent. The
default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reopened, you can choose to
override the capacity check keep the work assigned to a specific agent. The default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Automatically minimizes the Omni-Channel widget when an agent accepts work. The default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Service channel settings override the audio settings for each agent’s presence configuration.
The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, agents can extend their After Conversation Work (ACW) time. Available only
if `HasAfterConvoWorkTimer` is set to `true` . If set to `true`, you must also set the


Standard Objects ServiceChannel

**Field** **Details**

`AcwExtensionDuration` and `MaxExtensions` fields. The default value is `false` .
Available only for service channels of type Messaging or Voice.

This field is available in API version 56.0 and later.

```
HasAfterConvoWorkTimer

HasAutoAcceptEnabled

Language

MasterLabel

MaxExtensions

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, After Conversation Work (ACW) time can be configured for the channel. If
set to `true`, you must also set the `AfterConvoWorkMaxTime` field. The default value
is `false` . Available only for service channels of type Messaging or Voice.

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type messaging, this field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Work items in a service channel open automatically in the agent’s workspace so that the
agent doesn’t have to manually accept them. The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the service channel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the service channel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ServiceChannel

**Field** **Details**

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Available only for service channels of
type Messaging or Voice.

This field is available in API version 56.0 and later.

```
RelatedEntity

RoutingConfigurationId

SecRoutingPriorityField

SoundLength

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of object that’s associated with this service channel. This field is unique within your
organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  RoutingConfiguration

```

**Refers To**

```
  QueueRoutingConfig

```

**Description**
The ID of the routing configuration. This field is a relationship field. This field is available in
API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The name of the standard field or the id of the custom field that is used for secondary routing
priority. This field is unique within your organization.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.


### Standard Objects ServiceChannelFieldPriority

**Field** **Details**

```
StatusField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The picklist field that you use to track work status in the Status-Based capacity routing model.
Use ServiceChannelStatusField to specify the values that indicate completed and in-progress
work-item status.

### ServiceChannelFieldPriority

Represents a secondary routing priority field-value mapping. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
Priority

ServiceChannelId

Value

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority number assigned to the mapped field value.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
string


### Standard Objects ServiceChannelStatus

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The value of the SecRoutingPriorityField field defined in parent ServiceChannel.

### ServiceChannelStatus

Represents the status that’s associated with a specific service channel. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
ServiceChannelId

ServicePresenceStatusId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s associated with the service channel that’s specified by
the `ServicePresenceChannelId` .


### Standard Objects ServiceChannelStatusField ServiceChannelStatusField

Represents the values that you use to indicate completed and in-progress work item status for the status field in the Status-Based Capacity
routing model. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel and Status-Based Capacity Model must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
ServiceChannelId

Type

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For the field that you use to track work status, specifies whether the values are for completed
or in-progress work.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Specifies the values that you use to indicate completed and in-progress work status. Valid
values are `Completed`, `InProgress`, and `Paused` .


### Standard Objects ServiceContract ServiceContract

Represents a customer support contract (business agreement). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

ActivationDate

AdditionalDiscount

ApprovalStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account associated with the service contract.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The initial day the service contract went into effect (whereas `StartDate` may include
a renewal date).

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Extra discount percentage for the service contract. Available in API version 55.0 and
later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Approval status of the service contract.


Standard Objects ServiceContract

**Field** **Details**

`BillingAddress` (beta)

```
BillingCity

BillingCountry

BillingCountryCode

BillingLatitude

BillingLongitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ServiceContract

**Field** **Details**

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

```
BillingPostalCode

BillingState

BillingStateCode

BillingStreet

ContactId

ContractNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
string

**Properties**
Group, Sort, Filter, Nillable

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s billing address.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Contact associated with the service contract. Must be a valid ID.

**Type**
string


Standard Objects ServiceContract

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Unique number automatically assigned to the service contract.

```
Description

Discount

EndDate

GrandTotal

IsDeleted

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the service contract.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

Discount percentage for the service contract.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last day the service contract is in effect.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the service contract plus shipping and taxes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .


Standard Objects ServiceContract

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LineItemCount

Name

OwnerId

ParentServiceContractId

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number of ContractLineItem records associated with the service contract.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the service contract.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns the service contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ServiceContract

**Field** **Details**

**Description**
The service contract’s parent service contract, if it has one.

```
Pricebook2Id

RootServiceContractId

```

`ShippingAddress` (beta)

```
ShippingCity

ShippingCountry

ShippingCountryCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Pricebook2 associated with the service contract. Must be a valid ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level service contract in a service contract hierarchy. Depending
on where a service contract lies in the hierarchy, its root could be the same as its parent.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Country maximum size is 40 characters.

**Type**
picklist


Standard Objects ServiceContract

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s shipping address.

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
Used with `ShippingLongitude` to specify the precise geolocation of a shipping
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

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
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. State maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s shipping address.


Standard Objects ServiceContract

**Field** **Details**

```
ShippingStreet

SpecialTerms

StartDate

Status

Subtotal

Tax

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The street address of the shipping address. Maximum of 255 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Any terms specifically agreed to and tracked in the service contract.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first day the service contract is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
The status of the service contract, such as Inactive.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Total of the service contract line items (products) before discounts, taxes, and shipping
are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update


### Standard Objects ServiceContractOwnerSharingRule

**Field** **Details**

**Description**
Total taxes for the service contract.

```
Term

TotalPrice

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
Number of months that the service contract is valid.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Total of the contract line items (products) after discounts and before taxes and shipping.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceContractChangeEvent (API version 44.0)**
Change events are available for the object.

**ServiceContractFeed (API version 23.0)**
Feed tracking is available for the object.

**ServiceContractHistory**

History is available for tracked fields of the object.

### **ServiceContractOwnerSharingRule**

Sharing rules are available for the object.

**ServiceContractShare**

Sharing is available for the object.

SEE ALSO:

### ServiceContractOwnerSharingRule ServiceContractOwnerSharingRule

Represents the rules for sharing a ServiceContract (customer service agreement) with users other than the owner. This object is available
in API version 18.0 and later.


Standard Objects ServiceContractOwnerSharingRule

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A value that represents the type of sharing allowed. The possible values are:

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

This field is available in API version 24.0 and later. When creating large sets of data,
always specify a unique `DeveloperName` for each record. If no


### Standard Objects ServiceCrew

**Field Name** **Details**

`DeveloperName` is specified, performance slows down while Salesforce generates
one for each record.

```
GroupId

Name

UserorGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
The ID representing the source group. Service contracts owned by users in the source
group trigger the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** in the user interface.

**Type**
reference

**Properties**
Create, Filter

**Description**
The ID representing the target user or group. Target users or groups are given access.

Use this object to manage the sharing rules for a service contract. General sharing and territory management-related sharing use this
object.

SEE ALSO:

ServiceContract

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### ServiceCrew

Represents a group of service resources who can be assigned to service appointments as a unit.

A service crew is a group of service resources whose combined skills and experience make them a good fit to work together on
appointments. For example, a wellhead repair crew might include a hydrologist, a mechanical engineer, and an electrician.


Standard Objects ServiceCrew

Service appointments can only be assigned to service resources. To assign a service crew to service appointments, you must create a
service resource with a resource type of Crew that represents the crew, then use the resource for assignment purposes.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
CrewSize

LastReferencedDate

LastViewedDate

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of members on the crew. This field is manual, so it doesn’t
auto-update when you add or remove members.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ServiceCrewMember

**Field Name** **Details**

**Description**
The name of the service crew. For example, Repair Crew.

```
OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The crew owner. By default, the owner is the person who created the service
crew.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceCrewChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceCrewFeed**

Feed tracking is available for the object.

**ServiceCrewHistory**

History is available for tracked fields of the object.

**ServiceCrewOwnerSharingRule**

Sharing rules are available for the object.

**ServiceCrewShare**

Sharing is available for the object.

### ServiceCrewMember

Represents a technician service resource that belongs to a service crew.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ServiceCrewMember

Fields

**Field Name** **Details**

```
EndDate

IsLeader

LastReferencedDate

LastViewedDate

ServiceCrewId

ServiceCrewMemberNumber

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last day that the service resource belongs to the crew. You can use this field
to track employment dates for contractors.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the member is the crew leader.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The crew that the service resource belongs to.

**Type**
string


### Standard Objects ServiceCrewOwnerSharingRule

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service crew member.

```
ServiceResourceId

StartDate

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that belongs to the crew. Only service resources whose
resource type is Technician can be added to service crews.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The day the service resource joins the crew. Service resources can
belong to multiple crews as long as their start and end dates don’t overlap.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceCrewMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceCrewMemberFeed**

Feed tracking is available for the object.

**ServiceCrewMemberHistory**

History is available for tracked fields of the object.

### ServiceCrewOwnerSharingRule

Represents the rules for sharing a service crew with user records other than the owner or anyone above the owner in the role hierarchy.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)


Standard Objects ServiceCrewOwnerSharingRule

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

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
A description of the sharing rule. Maximum size is 1000 characters.

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

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A service crew owned by a User in the source Group
triggers the rule to give access.

**Type**
string


### Standard Objects ServicePresenceStatus

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

```
ServiceResourceAccessLevel

UserOrGroupId

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
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### ServicePresenceStatus

Represents a presence status that can be assigned to a service channel. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects ServiceReport

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

### ServiceReport

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence status.

Represents a report that summarizes a work order, work order line item, or service appointment.

The fields that appear on a service report are determined by its service report template. Service reports can be signed by the customer
and shared as a PDF.


Standard Objects ServiceReport

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()update( )

```

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ContentVersionDocumentId

DocumentBody

DocumentContentType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the service report version, used for storage.

**Type**
base64

**Properties**
Create, Nillable

**Description**
The report output. `DocumentBody` can’t be retrieved via REST API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data used for the report output.. Possible values are:

**•** `audio/ogg`

**•** `text/calendar`

**•** `video/3gpp2`

**•** `video/3gpp`

**•** `image/avif`

**•** `text/calendar`

**•** `audio/x-caf`

**•** `image/webp`


Standard Objects ServiceReport

**Field Name** **Details**

```
DocumentLength

DocumentName

DocumentTemplate

IsSigned

ParentId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the report output.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the report output, always set to Service Report.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The template used to generate service documents for the Document Builder
feature.

Important: `DocumentTemplate` is different from `Template` . The
document template needs to reference a flexipage that is of type

`serviceDocument` and must target the object used to generate the
service document. For example, you can't use an Account flexipage for a
service report tied to a work order.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the service report contains one or more signatures. This field
isn’t supported for Document Builder.

Tip: Add this field to the Service Reports related list on work orders, work
order line items, and service appointments.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceReport

**Field Name** **Details**

**Description**
The ID of the service appointment, work order, or work order line item that the
service report summarizes. For example, if you click **Create Service Report** on
a service appointment, this field lists the service appointment’s record ID.

```
ServiceReportLanguage

ServiceReportNumber

Status

Template

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Restricted picklist

**Description**
The language used for the service report. The language is selected in the
`ServiceReportLanguage` field on the associated work order. If the work
order doesn’t specify a service report language, the report is translated in the
default language in Salesforce of the person generating the report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service report.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service report. Available in API version 53.0 and later.

Possible values are:

**•** `Completed`

**•** `Failed`

**•** `Generating`

**•** `In Progress`

**•** `None`

**•** `Queued`

The default value is `None` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects ServiceReportLayout

**Field Name** **Details**

**Description**
The service report template used to generate the service report.

Note: If the person creating the service report doesn’t have access to
certain objects or fields that are included in the service report template,
those fields aren’t visible in the report they create.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceReportChangeEvent on page 68**
Change events are available for the object. Available in API version 55.0 and later.

**ServiceReportHistory**

History is available for tracked fields of the object.

### ServiceReportLayout

Represents a service report template in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled. All users with Field Service Standard user permission can view the ServiceReportLayout object via the
API.

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
The developer name of the service report template.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


Standard Objects ServiceReportLayout

**Field Name** **Details**

```
Language

LastViewedDate

MasterLabel

TemplateType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the service report template uses.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the service report template was last viewed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the service report template. For example, Maintenance Report
Template.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the service report template. Available in API version 46.0 and later.

Possible values are:

**•** `DigitalForm`

**•** `ServiceReport`

The default value is `ServiceReport` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceReportLayoutChangeEvent on page 68**
Change events are available for the object. Available in API version 55.0 and later.


### Standard Objects ServiceRequest ServiceRequest

Represents a formal request from a user for something to be provided, such as access, information, hardware, or software. This object
manages the lifecycle of these tasks, which are typically low-risk, and can be fulfilled through a defined, repeatable process. For example,
a Service Request can be created for an employee requesting a new laptop or a student needing a transcript. This object is available in
API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssignedGroupId

AssignedUserId

BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user group assigned to the service request.

This field is a relationship field.

**Relationship Name**
AssignedGroup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user assigned to the service request.

This field is a relationship field.

**Relationship Name**
AssignedUser

**Refers To**
User

**Type**
reference


Standard Objects ServiceRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the business hours used to determine the SLA calculation.

This field is a relationship field.

**Relationship Name**
BusinessHours

**Refers To**
BusinessHours

```
ClosedDate

Description

IsClosed

IsPaused

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the service request was closed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A detailed description of the service request.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the service request is closed (true) or not (false). The default value is false.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the SLA timer is paused (true) or not (false). The default value is false.

The default value is `false` .


Standard Objects ServiceRequest

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MilestoneStatus

Name

OwnerId

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
The timestamp for when the current user last viewed this record

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Information about the milestone the service request reached.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the service request record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects ServiceRequest

**Field** **Details**

```
ParentServiceRequestId

Priority

ReportedById

ResolutionDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent request that this service request belongs to.

This field is a relationship field.

**Relationship Name**
ParentServiceRequest

**Refers To**
ServiceRequest

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of a service request.

Valid values are:

**•** `High`

**•** `Medium`

**•** `Low`

The default value is `Low` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the person who reported the service request.

This field is a polymorphic relationship field.

**Relationship Name**
ReportedBy

**Refers To**
Account, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ServiceRequest

**Field** **Details**

**Description**
The date and time when the service request was resolved.

```
ResolutionSummary

SlaEndDate

SlaPauseDate

SlaStartDate

Status

StatusCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Resolution summary for the service request.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the SLA timer ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the SLA timer was paused.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the SLA timer started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of a service request.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ServiceResource

**Field** **Details**

**Description**
The code that displays the status of the service request lifecycle.

Valid values are:

**•** `Closed`

**•** `Canceled`

**•** `InProgress`

**•** `New`

**•** `OnHold`

**•** `Resolved`

The default value is `New` .

```
Subject

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A short description of the service request.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceRequestFeed on page 55**
Feed tracking is available for the object.

**ServiceRequestHistory**

History is available for tracked fields of the object.

**ServiceRequestShare**

Sharing is available for the object.

### ServiceResource

Represents a service technician or service crew in Field Service and Salesforce Scheduler, or an agent in Workforce Engagement. This
object is available in API version 38.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`


Standard Objects ServiceResource

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
Description

IsActive

IsCapacityBased

IsOptimizationCapable

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the resource.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When selected, this option means that the resource can be assigned to work
orders. For service tracking purposes, resources can’t be deleted, so deactivating
a resource is the best way to send them into retirement.

Deactivating a user doesn’t deactivate the related service resource. You can’t
create a service resource that is linked to an inactive user.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Capacity-based resources are limited to a certain number of hours or
appointments in a specified time period.

Tip: The Capacities related list shows a resource’s capacity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is reserved for Field Service and the managed package. Create a custom
field instead of using this field to include a service resource in optimization.


Standard Objects ServiceResource

**Field Name** **Details**

```
LastKnownLatitude

LastKnownLongitude

LastKnownLocation

LastKnownLocationDate

LastReferencedDate

LastViewedDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the last known location.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the last known location.

**Type**
location

**Properties**
Nillable

**Description**
The service resource’s last known location. You can configure this field to display
data collected from a custom mobile app. This field isn’t visible in the user
interface, but you can expose it on service resource page layouts or set up field
tracking to be able to view a resource’s location history.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time of the last known location.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime


Standard Objects ServiceResource

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource was last viewed.

```
LocationId

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The location associated with the service resource. For example, a service vehicle
driven by the service resource.

LocationId is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The resource’s name, for example the name or title of the associated user or
service crew.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service resource.

OwnerId is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ServiceResource

**Field Name** **Details**

```
RelatedRecordId

ResourceType

ServiceCrewId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The associated user. Its label in the UI is `User` . If the service resource represents
a service crew rather than a user, leave the `User` field blank and select the
related crew in the `ServiceCrewId` field.

RelatedRecordId is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the resource is a Technician (T), Dispatcher (D), Crew (C), Asset
(S), Agent (A), or Planner (P). The default value is Technician (T). Resources who
are dispatchers can’t be capacity-based or included in scheduling optimization.
Only users with the Field Service Dispatcher permission-set license can be
dispatchers. You can’t add additional resource types.

To create a dependent lookup filter with ServiceResource.ResourceType, use only
the first letter of the picklist value, for example T for Technician.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The associated service crew. If the service resource represents a crew, select the
crew.

Note: This field is hidden for all users by default. To use it, update its
field-level security settings in Setup and add it to your service resource
page layouts.


### Standard Objects ServiceResourceCapacity

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceResourceChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceResourceFeed**

Feed tracking is available for the object.

**ServiceResourceHistory**

History is available for tracked fields of the object.

**ServiceResourceOwnerSharingRule**

Sharing rules are available for the object.

**ServiceResourceShare**

Sharing is available for the object.

### ServiceResourceCapacity

Represents the maximum number of scheduled hours or number of service appointments that a capacity-based service resource can
complete within a specific time period. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
CapacityInHours

CapacityInWorkItems

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of hours that the resource can work per time period. You must fill
out this field, the `CapacityInWorkItems` field, or both.

**Type**
int


Standard Objects ServiceResourceCapacity

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of service appointments that the resource can complete per
time period. You must fill out this field, the `CapacityInHours` field, or both.

```
CapacityNumber

EndDate

LastReferencedDate

LastViewedDate

ServiceResourceId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the capacity record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the capacity ends; for example, the end date of a contract.

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
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceResourceCapacity

**Field Name** **Details**

**Description**
The associated service resource. You can set multiple capacities for a resource as
long as their start and end dates do not overlap.

```
StartDate

TimePeriod

```

Usage

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The date the capacity goes into effect.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Days, Hours, or Months. For example, if a resource can work 80 hours per month,
the capacity’s `Time Period` would be _`Month`_ and `Hours per Time`
`Period` would be _`80`_ .

Service resources who are capacity-based can only work a certain number of hours or complete a certain number of service appointments
within a specified time period. Contractors tend to be capacity-based. To indicate that a service resource is capacity-based, select
**Capacity-Based** on the service resource record, then create a capacity record for the service resource.

You must fill out at least one of these fields: `CapacityInWorkItems` and `CapacityInHours` . If you’re using the Field Service
managed package and would like to measure capacity both in hours and in number of work items, enter a value for both. The resource
is considered to reach their capacity based on whichever term is met first—hours or number of work items.

Important: If you aren’t using the Field Service managed package, capacity serves more as a suggestion than a rule. Resources
can still be as scheduled beyond their capacity, and you aren’t notified when a resource exceeds their capacity.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceCapacityChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceCapacityFeed**

Feed tracking is available for the object.

**ServiceResourceCapacityHistory**

History is available for tracked fields of the object.


### Standard Objects ServiceResourceCapacityHistory ServiceResourceCapacityHistory

Represents the history of changes made to tracked fields on a service resource capacity record. This object is available in API version 38.0
and later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for service resource capacity fields must be configured.

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

**Properties**
Nillable, Sort


### Standard Objects ServiceResourceDataTranslation

**Field Name** **Details**

**Description**
The value of the field before it was changed.

```
ServiceResourceCapacityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the service resource capacity being tracked. The history is displayed on the
detail page for this record.

### ServiceResourceDataTranslation

Represents the translated values of the data stored within a ServiceResource record’s fields. This object is available in API version 54.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

Fields

**Field** **Details**

```
Description

IsOutOfDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The translated value for the ServiceResource description.

**Type**
boolean


### Standard Objects ServiceResourceOwnerSharingRule

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ServiceResource record is updated after the last translation was
filed.

```
Language

Name

ParentId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the ServiceResource record name. This field is required to translate
the text in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the ServiceResource associated with the data that is being translated.

Use this object to translate the data stored in a ServiceResource record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ServiceResource object, additional ServiceResourceDataTranslation fields exist for translating
the data contained within those fields.

You can’t use a custom external id field in an upsert call for a ServiceResourceDataTranslation object.

### ServiceResourceOwnerSharingRule

Represents the rules for sharing a service resource with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 38.0 and later.


Standard Objects ServiceResourceOwnerSharingRule

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
Description

DeveloperName

GroupId

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
Create, Defaulted on create, Filter, Group, Sort, Update

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
The ID representing the source group. A service resource owned by a User in the source
Group triggers the rule to give access.


### Standard Objects ServiceResourcePreference

**Field** **Details**

```
Name

ServiceResourceAccessLevel

UserOrGroupId

```

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
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### ServiceResourcePreference

Represents the service resource scheduling preferences that are considered as a business objective in the scheduling logic engine. This
object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Agent or Workforce Engagement Planner permission set.


Standard Objects ServiceResourcePreference

Fields

**Field** **Details**

```
EndDate

LastReferencedDate

LastViewedDate

Name

OperatingHoursId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date period that this preference is effective.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last modified. Its label in the user interface
is **Last Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The service resource preference record name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The operating hours associated with the service resource preference.

This is a relationship field.

**Relationship Name**
OperatingHours


Standard Objects ServiceResourcePreference

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
OperatingHours

```
OwnerId

ServiceResourceId

StartDate

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service resource preference.

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
The service resource associated with the service resource preference.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The start date period that this preference is effective.


### Standard Objects ServiceResourceSkill ServiceResourceSkill

Represents a skill that a service resource possesses in Field Service and Lightning Scheduler. This object is available in API version 38.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
EffectiveEndDate

EffectiveStartDate

LastReferencedDate

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the skill expires. For example, if a service resource needs to be
re-certified after six months, the end date would be the date their certification
expires.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource gains the skill. For example, if the skill
represents a certification, the start date would be the date of certification.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last modified. Its label in the user interface
is `Last Modified Date` .


Standard Objects ServiceResourceSkill

**Field Name** **Details**

```
LastViewedDate

ServiceResourceId

SkillId

SkillLevel

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service resource who possesses the skill.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill the service resource possesses.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The service resource’s skill level. Skill level can range from zero to 99.99.


### Standard Objects ServiceSetupProvisioning

**Field Name** **Details**

```
SkillNumber

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource skill assignment.

You can assign skills to all service resources in your org to indicate their certifications and areas of expertise, and specify each resource’s
skill level from 0 to 99.99. For example, you can assign Maria the “Welding” skill, level 50.

If you intend to use the skills feature, determine which skills you want to track and how skill level should be determined. For example,
you may want the skill level to reflect years of experience, certification levels, or license classes.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceSkillChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceSkillFeed**

Feed tracking is available for the object.

**ServiceResourceSkillHistory**

History is available for tracked fields of the object.

### ServiceSetupProvisioning

Represents a task completed by the Service Setup Assistant. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ServiceSetupProvisioning is accessible only if the Service Setup Assistant is turned on. Users need the Customize Application permission

to access it.


Standard Objects ServiceSetupProvisioning

Fields

**Field** **Details**

```
JobName

Name

Status

TaskAction

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of a group of tasks completed by the Service Setup Assistant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the task being completed by the Service Setup Assistant.

Possible values are:

**•** `

**•** `Completed` —The task completed successfully.

**•** `ExistingSetup` —The task couldn’t be completed due to conflicting configurations.

**•** `FailedFatalError` —The task couldn’t be completed.

**•** `InProgress` —The task is in progress.

**•** `PRE_CONDITION_NOT_MET` —The task couldn’t be completed because one or more
prerequisites weren’t met.

**•** `VALIDATION_NOT_MET` —The task is considered as completed but the condition
defined in the implementation was not true. No retry will be executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action taken by the task.

Possible values are:


### Standard Objects ServiceTerritory

**Field** **Details**

**•** `updatesOrgSettings`

**•** `updatesOrgValues`

**•** `sortApps`

**•** `setForecastingUserFeatureLicense`

**•** `recalculatePermissionSetGroup`

**•** `deploysMetadata`

**•** `createsSetupEntityAccess`

**•** `clearGuidanceCenterCache`

**•** `callsConnectApi`

**•** `assignsPermissionSets`

**•** `assignsPermissionSetGroups`

```
TaskActionContext

TaskContext

TaskName

### ServiceTerritory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional details about the `TaskAction` parameter, including how much of the action
has been processed.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the changes included in the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the task.

Represents a geographic or functional region in which work can be performed in Field Service, Salesforce Scheduler, or Workforce
Engagement. This object is available in API version 38.0 and later.


Standard Objects ServiceTerritory

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Address

AvgTravelTime

City

Country

```

**Type**
address

**Properties**
Filter

**Description**
An address to associate with the territory. For example, you can list the address
of the territory’s headquarters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The average travel time for this service territory. The value is added to the Work
Capacity Usage for each scheduled service appointment in the service territory.
Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the associated address. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to associate with the territory. Maximum length is 80 characters.


Standard Objects ServiceTerritory

**Field Name** **Details**

```
Description

GeocodeAccuracy

IsActive

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.This field is available in the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service territory is meant to be used. If a territory is inactive,
you can’t add members to it or link it to work orders, work order line items, or
service appointments.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last viewed.

**Type**
double


Standard Objects ServiceTerritory

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.This field is available in the API only.

```
Longitude

Name

OperatingHoursId

ParentTerritoryId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory’s operating hours, which indicate when service appointments within
the territory can occur. Service resources who are members of a territory
automatically inherit the territory’s operating hours unless different hours are
specified on the resource record.

This field is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference


Standard Objects ServiceTerritory

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The territory’s parent service territory, if it has one. For example, a _`Northern`_
_`California`_ territory can have a _`State of California`_ territory as
its parent. A service territory hierarchy can contain up to 10,000 territories.

This field is a relationship field.

**Relationship Name**
ParentTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
PostalCode

State

Street

TopLevelTerritoryId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the territory. Maximum length is
20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the territory. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the address associated with the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ServiceTerritory

**Field Name** **Details**

**Description**
(Read only) The top-level territory in a hierarchy of service territories. Depending
on where a territory lies in the hierarchy, its top-level territory can be the same
as its parent.

This field is a relationship field.

**Relationship Name**
TopLevelTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
TravelModeId

TravelTimeBuffer

TypicalInTerritoryTravelTime

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the TravelMode used for travel time calculations. The travel mode includes
information about the type of transportation, such as a car or walking, whether
a vehicle can take toll roads, and whether a vehicle is transporting hazardous
materials.

This field is a relationship field.

**Relationship Name**
TravelMode

**Relationship Type**
Lookup

**Refers To**
TravelMode

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Add additional time to driving time, such as time to find parking or to walk to
the site. This value overrides the Travel Time Buffer value defined in Field Service
Settings | Scheduling | Routing.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects ServiceTerritoryDataTranslation

**Field Name** **Details**

**Description**
Estimated number of minutes needed to travel from one location to another
within the service territory. You can use this field in Apex customization.

Usage

If you want to use service territories, determine which territories to create. Depending on how your business works, you can create
territories based on cities or counties, or on functional categories such as sales versus service. If you plan to build out a hierarchy of service
territories, create the highest-level territories first.

For example, you can create a hierarchy of territories to represent the areas where your team works in California. Include a top-level
territory named _`California`_, three child territories named _`Northern California`_, _`Central California`_, and
_`Southern California`_, and a series of third-level territories corresponding to California counties. Assign service resources to each
county territory to indicate who is available to work in that county.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**ServiceTerritoryChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryFeed**

Feed tracking is available for the object.

**ServiceTerritoryHistory**

History is available for tracked fields of the object.

**ServiceTerritoryOwnerSharingRule**

Sharing rules are available for the object.

**ServiceTerritoryShare**

Sharing is available for the object.

### ServiceTerritoryDataTranslation

Represents the translated values of the data stored within a ServiceTerritory record’s fields. This object is available in API version 54.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.


Standard Objects ServiceTerritoryDataTranslation

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

Fields

**Field** **Details**

```
Description

IsOutOfDate

Language

Name

ParentId

```

**Type**
textarea

**Properties**
Create, Nillable,Update

**Description**
The translated value for the ServiceTerritory description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ServiceTerritory record is updated after the last translation was
filed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the ServiceTerritory record name. This field is required to translate
the text in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the ServiceTerritory associated with the data that is being translated.


### Standard Objects ServiceTerritoryLocation

Usage

Use this object to translate the data stored in a ServiceTerritory record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ServiceTerritory object, additional ServiceTerritoryDataTranslation fields exist for translating
the data contained within those fields.

You can’t use a custom external id field in an upsert call for a ServiceTerritoryDataTranslation object.

### ServiceTerritoryLocation

Represents a location associated with a particular service territory in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LocationId

ServiceTerritoryId

### `ServiceTerritoryLocationNumber`

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location that is associated with the service territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read only) Auto-generated number identifying the service territory location.


### Standard Objects ServiceTerritoryMember

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryLocationChangeEvent (API version 55.0)**
Change events are available for the object.

**ServiceTerritoryLocationFeed**

Feed tracking is available for the object.

**ServiceTerritoryLocationHistory**

History is available for tracked fields of the object.

### ServiceTerritoryMember

Represents a service resource who can be assigned in a service territory in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
Address

City

```

**Type**
address

**Properties**
Filter

**Description**
The member’s address. You may want to list the related service resource’s address
in this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the member’s address. Maximum length is 40 characters.


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

```
Country

EffectiveEndDate

EffectiveStartDate

GeocodeAccuracy

LastReferencedDate

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the member’s address. Maximum length is 80 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the service resource is no longer a member of the territory. If the
resource will be working in the territory for the foreseeable future, leave this field
blank. This field is mainly useful for indicating when a temporary relocation ends.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource becomes a member of the service territory.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory member was last modified. Its label in the user
interface is `Last Modified Date` .


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

```
LastViewedDate

Latitude

Longitude

MemberNumber

OperatingHoursId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory member was last viewed.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the service territory member.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours assigned to the service territory member. If no operating
hours are specified, the member is assumed to use their parent service territory’s


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

operating hours. If a member needs special operating hours, create them in Setup
and select them in the `Operating Hours` lookup field on the member’s
detail page.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

```
PostalCode

ServiceResourceId

ServiceTerritoryId

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the member’s address. Maximum length is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource assigned to the service territory.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service territory that the service resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceTerritory


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
State

Street

TerritoryType

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the member’s address. Maximum length is 80 characters.

**Type**
textarea

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the member’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Primary, Secondary, or Relocation.

**•** The primary territory is typically the territory where the resource works most
often—for example, near their home base. Service resources can only have
one primary territory.

**•** Secondary territories are territories where the resource can be assigned to
appointments if needed. Service resources can have multiple secondary
territories.

**•** Relocation territories represent temporary moves for service resources. If
you’re using the Field Service managed packages with the scheduling
optimizer, resources with relocation territories are always assigned to services
within their relocation territories during the specified relocation dates; if they
don’t have a relocation territory, the primary territories are favored over the
secondary.

For example, a service resource might have the following territories:

**•** Primary territory: _`West Chicago`_

**•** Secondary territories:

**–** _`East Chicago`_


### Standard Objects ServiceTerritoryWorkType

**Field Name** **Details**

**–** _`South Chicago`_

**•** Relocation territory: _`Manhattan`_, for a three-month period

```
TravelModeId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the TravelMode used for travel time calculations. The travel mode includes
information about the type of transportation, such as a car or walking, whether
a vehicle can take toll roads, and whether a vehicle is transporting hazardous
materials.

This field is a relationship field.

**Relationship Name**
TravelMode

**Relationship Type**
Lookup

**Refers To**
TravelMode

If you delete a service territory with members, the service resources who were members no longer have any connection to the territory.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceTerritoryMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryMemberFeed**

Feed tracking is available for the object.

**ServiceTerritoryMemberHistory**

History is available for tracked fields of the object.

### ServiceTerritoryWorkType

Represents the relationship between a ServiceTerritory object and a WorkType object for Salesforce Scheduler appointments. This object
is available in API version 45.0 and later.


Standard Objects ServiceTerritoryWorkType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsSlotPublished

LastReferencedDate

LastViewedDate

Name

ServiceTerritoryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicate whether records in the Shift object are created for the selected Service Territory and
Work Type.

The default value is `false` .

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this service territory-work type relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceTerritoryWorkType

**Field** **Details**

**Description**
The ID of the service territory that’s related to the work type indicated in the `WorkTypeId`
field.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
TeamId

WorkTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the team associated with the service territory for a specific work type.

This field is a relationship field and is available in API version 58.0 and later.

**Relationship Name**
Team

**Relationship Type**
Lookup

**Refers To**
Team

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that’s related to the service territory indicated in the
`ServiceTerritoryId` field.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


### Standard Objects SessionPermSetActivation

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryWorkTypeFeed**

Feed tracking is available for the object.

**ServiceTerritoryWorkTypeHistory**

History is available for tracked fields of the object.

### SessionPermSetActivation

The SessionPermSetActivation object represents a permission set assignment activated during an individual user session. When a
### SessionPermSetActivation object is inserted into a permission set, an activation event fires, allowing the permission settings to apply to

the user’s specific session. This object is available in API versions 37.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Note: If you include session-based permission sets in a permission set group, the permissions in them do not require session-based
activation for users assigned to the group.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

Fields

**Field Name** **Details**

```
AuthSessionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The session ID related to this permission set assignment for its duration.

This is a relationship field.

**Relationship Name**
AuthSession

**Relationship Type**
Lookup

**Refers To**
AuthSession


Standard Objects SessionPermSetActivation

**Field Name** **Details**

```
Description

PermissionSetGroupId

PermissionSetId

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session details, such as device used and browser.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The permission set group ID related to this permission set group assignment and
user for its duration. This field is available in API version 53.0 and later.

This is a relationship field.

**Relationship Name**
PermissionSetGroup

**Relationship Type**
Lookup

**Refers To**
PermissionSetGroup

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The permission set ID related to this permission set assignment and user for its
duration.

This is a relationship field.

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects SessionPermSetActivation

**Field Name** **Details**

**Description**
The user ID of the user to whom this permission set assignment applies for its
duration.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Usage

Use SessionPermSetActivation to create a permission set available only for a specified session’s duration. For example, create permission
sets that provide access to specific applications only during authenticated sessions.

In the following Apex example, an identified session is activated after session information is submitted via a button. Successful activation
results in a confirmation message displayed to the user.

```
   public class SessionPermSetActivationController {

      // id of the session permission set to be activated

      private final String sessionPermSetId = '0PSxx00000004rJ';

      private final String sessionId;

      public SessionPermSetActivationController() {

        Map<String, String> sessionManagement = Auth.SessionManagement.getCurrentSession();

        String parentSessionId = sessionManagement.get('ParentId');

        String currentSessionId = sessionManagement.get('SessionId');

        sessionId = parentSessionId != null ? parentSessionId : currentSessionId;

      }

      public PageReference activate() {

        // activate the permission set

        SessionPermSetActivation activation = new SessionPermSetActivation();

        activation.AuthSessionId = sessionId;

        activation.PermissionSetId = sessionPermSetId;

        activation.Description = 'created by SessionPermSetActivationController';

        insert activation;

        return null;

      }

      public boolean getActivated() {

        Integer alreadyActivated = [SELECT count()

                              FROM SessionPermSetActivation

```


### Standard Objects SetupAssistantStep

```
                              WHERE AuthSessionId = :sessionId

                             And PermissionSetId = :sessionPermSetId LIMIT

    1];

        return alreadyActivated > 0;

      }

   }

   <apex:page controller="SessionPermSetActivationController">

       <apex:outputPanel rendered="{!!Activated}">

         <h3>Activate Session Permission Set</h3>

         <br />

         <apex:form >

             <apex:commandButton action="{!activate}" value="Activate"

   id="activateButton"/>

         </apex:form>

       </apex:outputPanel>

       <apex:outputPanel rendered="{!Activated}">

         <h3>Session Permission Set is already active.</h3>

       </apex:outputPanel>

   </apex:page>

### SetupAssistantStep

```

For internal use only.

### SetupAuditTrail

Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API version
15.0 and later.

Note: SetupAuditTrail is not a supported standard controller. Using SetupAuditTrail as a standard controller in a Visualforce page
results in an error.

Supported Calls

`query()`, `retrieve()`

Note: Aggregate queries aren’t supported on this object. For example, `SELECT count() FROM SetupAuditTrail`
works but `SELECT count(Id) FROM SetupAuditTrail` fails.

Fields

**Field** **Details**

```
Action

```

**Type**
string


Standard Objects SetupAuditTrail

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The category of the change made in Setup. For example, a value of _`PermSetCreate`_
indicates that an administrator created a permission set. The `Display` field contains more
specific information.

```
CreatedByContext

CreatedByIssuer

DelegateUser

Display

Section

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context under which the Setup change was made. For example, if Einstein uses
cloud-to-cloud services to make a change in Setup, the value of this field is _`Einstein`_ .
This field is available in API version 48.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Login-As user who executed the action in Setup. If a Login-As user didn’t perform the
action, this field is blank. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Nillable, Sort

**Description**
The full description of changes made in Setup. For example, if the `Action` field has a value
of _`PermSetCreate`_, the `Display` field has a value like “Created permission set MAD:
with user license Salesforce.”

**Type**
string


### Standard Objects SetupEntityAccess

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
The section in the Setup menu where the action occurred. For example, Manage Users or
Company Profile.

Note: You can use SOQL joins to get the information you need more quickly. For example, running `SELECT CreatedBy.Name`
`FROM SetupAuditTrail LIMIT 10` returns the first and last names of the last 10 people to make changes in Setup.

### SetupEntityAccess

Represents the enabled setup entity access settings (such as for Apex classes) for the parent PermissionSet. This object is available in
API version 25.0 and later.

To grant users access to an entity, associate the appropriate SetupEntityAccess record with a PermissionSet that’s assigned to a user.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with "View Setup and Configuration" permission can access this object.

Fields

**Field Name** **Details**

```
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet


Standard Objects SetupEntityAccess

**Field Name** **Details**

```
SetupEntityId

SetupEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity for which access is enabled, such as an Apex class or
Visualforce page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of setup entity for which access is enabled. Valid values are:

**•** `ApexClass` for Apex classes

**•** `ApexPage` for Visualforce pages

**•** In API version 64.0 and later, `BotDefinition` for agents

**•** In API version 28.0 and later, `ConnectedApplication` for OAuth
connected apps

**•** In API version 48.0 and later, `CustomEntityDefinition` for Custom
Settings and Custom Metadata Types

**•** In API version 31.0 and later, `CustomPermission` for custom permissions

**•** In API version 62.0 and later, `EmailRoutingAddress` for email routing
addresses.

**•** In API version 60.0 and later, `ExternalClientApplication` for
external client apps.

**•** In API version 58.0 and later, `ExternalCredentialParameter` for
external credential principals.

**•** In API version 58.0 and later, `FlowDefinition` for flows

**•** In API version 62.0 and later, `MessagingChannel` for messaging channels

**•** In API version 58.0 and later, `OrgWideEmailAddress` for
organization-wide email addresses

**•** In API version 28.0 and later, `ServiceProvider` for service providers

**•** In API version 60.0 and later, `StandardInvocableActionType` for
standard invocable actions.

**•** In API version 28.0 and later, `TabSet` for apps


Standard Objects SetupEntityAccess

Usage

Because SetupEntityAccess is a child of the PermissionSet object, the usage is similar to other PermissionSet child objects like
FieldPermissions and ObjectPermissions.

For example, the following code returns all permission sets that grant access to any setup entities for which access is enabled:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

```

The following code returns permission sets that grant access only to Apex classes:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE SetupEntityType='ApexClass'

```

The following code returns permission sets that grant access to any setup entities, and are not owned by a profile:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE ParentId

   IN (SELECT Id

     FROM PermissionSet

     WHERE isOwnedByProfile = false)

```

You may want to return only those permission sets that have access to a specific setup entity. To do this, query the parent object. For
example, this code returns all permission sets that grant access to the `helloWorld` Apex class:

```
   SELECT Id, Name,

     (SELECT Id, Parent.Name, Parent.Profile.Name

     FROM SetupEntityAccessItems)

   FROM ApexClass

   WHERE Name = 'helloWorld'

```

While it’s possible to return permission sets that have access to a `ConnectedApplication`, `ServiceProvider`, or `TabSet`
by `SetupEntityId`, it’s not possible to return permission sets that have access to these `SetupEntityType` fields by any other
AppMenuItem attribute, such as `Name` or `Description` . For example, to find out if a user has access to the Recruiting app, you’d
run two queries. First, query to get the AppMenuItem ID:

```
   SELECT Id, Name, Label

   FROM AppMenuItem

   WHERE Name = 'Recruiting'

```

Let’s say the previous query returned the AppMenuItem `ApplicationId` 02uD0000000GIiMIAW. Using this ID, you can now run a
query to find out if a user has access to the Recruiting app:

```
   SELECT Id, SetupEntityId, SetupEntityType

   FROM SetupEntityAccess

   WHERE ParentId

   IN

     (SELECT PermissionSetId

     FROM PermissionSetAssignment

```


### Standard Objects ShapeRepresentation

```
     WHERE AssigneeId = '005D0000001QOzF')

   AND (SetupEntityId = '02uD0000000GIiMIAW')

```

SEE ALSO:

PermissionSet

FieldPermissions

ObjectPermissions

ApexClass

ApexPage

### ShapeRepresentation

Contains information about the shape of an org. The shape of an org includes licenses and limits information. You can easily create
scratch orgs based on a source org’s shape. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A free-form text field for you to enter a description of this org shape. This field has a maximum
length of 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the org shape was last referenced. This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects SharingRecordCollection

**Field** **Details**

**Description**
Date when the org shape was last viewed. This field is read-only.

```
Name

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The alias for the org shape.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of this org shape. You can use an org shape when it’s Active. This field is read-only.

Possible values are:

**•** `Active`

**•** `Error`

**•** `InProgress`

**•** `Inactive`

**•** `New`

### SharingRecordCollection

Represents a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Record collections are limited to 100 items and 100 members for each record collection.

Fields

**Field** **Details**

```
Description

```

**Type**
string


Standard Objects SharingRecordCollection

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection.

```
GroupId

LastAdded

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The group ID of the record collection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when an item was last added to the record collection.

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
The name of the record collection.


### Standard Objects SharingRecordCollectionItem

**Field** **Details**

```
NumberOfRecords

OwnerId

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of records in the record collection. The limit is 100.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record collection owner.

### SharingRecordCollectionItem

Represents a single record in a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Record collections are limited to 100 items for each record collection.

Fields

**Field** **Details**

```
CollectionId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SharingRecordCollectionMember

**Field** **Details**

**Description**
The description of the record collection item.

```
ItemId

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record collection item.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection item.

### SharingRecordCollectionMember

Represents a user with access to a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Record collections are limited to 100 members for each record collection.

Fields

**Field** **Details**

```
AccessLevel

CollectionId

```

**Type**
picklist

**Properties**
Read, Edit

**Description**
The access level on the related record collection.

**Type**
reference


### Standard Objects Shift

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

```
UserOrGroupId

### Shift

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user or group with access to the record collection.

Represents a shift for service resource scheduling. Available in API versions 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `upsert()`

Special Access Rules

Field Service, Service Engagement, or Workforce Engagement must be enabled. For Field Service, users must have Field Service permissions.
For Service Engagement, users must have the Service Engagement Planner permission set. For Workforce Engagement, users must have
the Workforce Engagement Admin or Planner permission set.

Fields

**Field** **Details**

```
BackgroundColor

EndTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
dateTime


Standard Objects Shift

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift ends.

```
IsHolidayShift

IsNonStandard

JobProfileId

Label

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates a shift that overlaps with holiday hours. The default value is false. Available in API
version 55.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The job profile associated with the shift. Available in API versions 47.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label that a shift is given.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed a related record.


Standard Objects Shift

**Field** **Details**

```
LastViewedDate

OwnerId

RecordsetFilterCriteriaId

ServiceResourceId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift.

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
The ID of the recordset filter criteria selected for the shift. Available in API version 49.0 and
later.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shift

**Field** **Details**

**Description**
The ID of the service resource the shift belongs to. Available in API versions 47.0 and later.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
ServiceTerritoryId

ShiftNumber

ShiftTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory the shift belongs to. Available in API versions 47.0 and later.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number automatically given to the shift upon creation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The shift template ID, if the shift was created from a shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate


Standard Objects Shift

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

```
StartTime

Status

StatusCategory

TimeSlotType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift starts.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the status of the shift. Users can create custom values. Default values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. This field is derived from `Status` using
the mapping defined in setup.

Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of time slot for the shift. The same setup values as the `TimeSlot` field in the
OperatingHours object.


### Standard Objects ShiftHistory

**Field** **Details**

Possible values are:

**•** `Normal` (default value)

**•** `Extended`

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0, and is a pilot feature in API version
47.0.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftChangeEvent (API version 54.0)**
Change events are available for the object.

**ShiftFeed**

Feed tracking is available for the object.

### **ShiftHistory**

History is available for tracked fields of the object.

**ShiftOwnerSharingRule**

Sharing rules are available for the object.

**ShiftShare**

Sharing is available for the object.

### ShiftHistory

Represents the history of changes made to tracked fields on a time sheet. Available in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for shift fields must be configured.


Standard Objects ShiftHistory

Fields

**Field** **Details**

```
DataType

Field

NewValue

OldValue

ShiftId

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
ID of the shift being tracked. The history is displayed on the detail page for this record.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup


### Standard Objects ShiftOwnerSharingRule

**Field** **Details**

**Refers To**
### Shift

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftOwnerSharingRule

Represents the rules for sharing a shift with user records other than the owner or anyone above the owner in the role hierarchy. Available
in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not


Standard Objects ShiftOwnerSharingRule

**Field** **Details**

include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
GroupId

Name

ServiceResourceAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A time sheet owned by a User in the source Group
triggers the rule to give access.

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
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.


### Standard Objects ShiftPattern

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftPattern

Represents a pattern of templates for creating shifts. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled. Users must have Field Service permission.

Fields

**Field** **Details**

```
Description

IsActive

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A short description of the shift pattern to help users identify the pattern.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the shift pattern can be used to create shifts.

The default value is ‘false’.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last used.


Standard Objects ShiftPattern

**Field** **Details**

```
LastViewedDate

Name

OwnerId

PatternLength

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A short, descriptive name of the shift pattern.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the shift pattern. Default is the user who creates the shift pattern.

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
Create, Filter, Group, Sort, Update

**Description**
The duration in days of the shift pattern.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftPatternChangeEvent (API version 54.0)**
Change events are available for the object.


### Standard Objects ShiftPatternEntry

**ShiftPatternFeed on page 55**
Feed tracking is available for the object.

**ShiftPatternHistory on page 63**
History is available for tracked fields of the object.

**ShiftPatternShare on page 67**
Sharing is available for the object.

SEE ALSO:

### ShiftPatternEntry

[Shift Patterns](https://help.salesforce.com/articleView?id=fs_shift_patterns.htm&language=en_US)

### ShiftPatternEntry ShiftPatternEntry links a shift template to a shift pattern. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled. Users must have Field Service permission.

Fields

**Field** **Details**

```
DayOrder

LastReferencedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
`DayOrder` links the shift template to the specific day within the shift pattern duration that
the template. For example, if the DayOrder is 2 then a shift from the associated template is
created on the second day of the pattern.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last used.


Standard Objects ShiftPatternEntry

**Field** **Details**

```
LastViewedDate

Name

ShiftPatternId

ShiftTemplateId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated reference number for the shift pattern entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the shift pattern that the shift pattern entry is linked to.

This is a relationship field.

**Relationship Name**
ShiftPattern

**Relationship Type**
Lookup

**Refers To**
ShiftPattern

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the shift template that’s used to create shifts for this shift pattern entry.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate


### Standard Objects ShiftSegment

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftPatternEntryChangeEvent (API version 54.0)**
Change events are available for the object.

SEE ALSO:

ShiftPattern

### ShiftSegment

Represents a scheduled activity within a shift. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
EndTime

IsInAdherence

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the agent is in adherence ( `true` ) or not ( `false` ) for the scheduled
segment activity.

The default value is `true` .


Standard Objects ShiftSegment

**Field** **Details**

```
Name

SegmentTypeId

ShiftId

StartTime

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the shift segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the associated shift segment type.

This is a relationship field.

**Relationship Name**
SegmentType

**Relationship Type**
Lookup

**Refers To**
ShiftSegmentType

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the shift in which the segment is scheduled.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup

**Refers To**
Shift

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment starts.


### Standard Objects ShiftSegmentType ShiftSegmentType

Represents a type of activity scheduled within a shift. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
AdherenceThreshold

Category

Color

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A threshold, in minutes. If the agent starts the scheduled activity within this threshold, the
shift segment activity is in adherence.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A category for the type of shift segment.

Possible values are:

**•** `Break` —Break times, such as a coffee or lunch break.

**•** `NonWork` —Non-working activities, such as training or meetings.

**•** `Work` —Work activities, such as answering calls, responding to chats, or handling cases.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shift activities of this type are displayed in the UI. Use a 3- or
6-digit hexadecimal format, for example #FF00FF.


Standard Objects ShiftSegmentType

**Field** **Details**

```
Description

DeveloperName

IsActive

Language

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the shift segment type.

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
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the shift segment type is active ( `true` ) or not ( `false` ).

The default value is `true` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the shift segment type.

Possible values are the languages that Workforce Engagement supports.


### Standard Objects ShiftShare

**Field** **Details**

```
MasterLabel

ServicePresenceStatusId

### ShiftShare

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the shift segment type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the associated service presence status for segments of this type.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

Represents a sharing entry on a field service shift. Available in API versions 46.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ShiftShare

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
Level of access that the user or group has to the shift. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn’t valid for create or update calls.)

Set to an access level that is at least equal to the organization’s default shift access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The shift associated with the sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the shift record.

**•** `Owner` —The User is the owner of the shift.

**•** `Rule` —The User or Group has access via a shift sharing rule.


### Standard Objects ShiftStatus

**Field** **Details**

**•** `GuestRule` —The User or Group has access via a shift guest user sharing rule.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Read only) ID of the user or group that has access to the shift record.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftStatus

Represents a shift, such as Tentative, Published, or Confirmed. Available in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects ShiftStatus

**Field** **Details**

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

```
IsDefault

MasterLabel

SortOrder

StatusCode

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default shift status value ( `true` ) or not ( `false` ) in the picklist.
Only one value can be the default value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this shift status value. This display value is the internal label that does not
get translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the shift status picklist. These numbers are not guaranteed
to be sequential, as some previous shift status values might have been deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.


### Standard Objects ShiftTemplate ShiftTemplate

Represents a template for creating shifts. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled. For Field Service, users must have Field Service permission. For Workforce
Engagement, the user needs to have a Workforce Engagement Admin or Planner permission set.

Fields

**Field** **Details**

```
BackgroundColor

Description

Duration

IsActive

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the shift like number of breaks or activities.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
How long the shift lasts. The unit of measurement for this field is determined by
### ShiftTemplateDurationType .

**Type**
boolean


Standard Objects ShiftTemplate

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is active or inactive.

```
IsNonStandard

JobProfileId

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Job Profile record. This field is optional.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last modified. Its label in the user interface is **Last**
**Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last viewed.


Standard Objects ShiftTemplate

**Field** **Details**

```
Name

OwnerId

RecordsetFilterCriteriaId

ShiftTemplateDurationType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The shift template record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift template.

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
The ID of the recordset filter criteria selected for the shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects Shipment

**Field** **Details**

**Description**
The unit of measurement for the shift template duration.

Possible values are:

**•** `H` —Hours

**•** `M` —Minutes

The default value is `H` .

```
StartTime

TimeSlotType

```

Associated Objects

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time of day when the shift starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are:

**•** `Normal`

**•** `Extended`

You can use _`Extended`_ to represent overtime shifts. Available in API version 55.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftTemplateOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ShiftTemplateShare on page 67**
Sharing is available for the object.

**ShiftTemplateChangeEvent on page 68**
Change Data Capture events are available for the object. Available in API version 54.0 and later.

### Shipment

Represents the transport of inventory in field service or a shipment of order items in Order Management.


Standard Objects Shipment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution

Fields

**Field Name** **Details**

```
ActualDeliveryDate

DeliveredToId

DeliveryMethodId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product was delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person or entity the product was delivered to.

This is a polymorphic relationship field.

**Relationship Name**
DeliveredTo

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
The delivery method used for the shipment.

This field is available in API version 51.0 and later.

```
Description

DestinationLocationId

ExpectedDeliveryDate

FulfillmentOrderId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The place the product is to be delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The fulfillment order that the shipment belongs to.

This field is available in API version 51.0 and later.


Standard Objects Shipment

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

OrderSummaryId

OwnerId

Provider

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order summary associated with the shipment.

This field is available in API version 51.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shipment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company or person making the transfer.

```
ReturnOrderId

ShipFromAddress

ShipFromCity

ShipFromCountry

ShipFromGeocodeAccuracy

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For a return Shipment, the associated ReturnOrder.

This field is available in API version 53.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The place the product is coming from. The compound form of the ship to address.
Read-only. For details on compound address fields, see Address Compound
Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment originates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
Accuracy level of the geocode for the address where the shipment originates.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

```
ShipFromLatitude

ShipFromLongitude

ShipFromPostalCode

ShipFromState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
The state of the address where the shipment originates.

```
ShipFromStreet

ShipToAddress

ShipToCity

ShipToCountry

ShipToGeocodeAccuracy

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment originates.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the shipment is delivered. The compound form of
the ship to address. Read-only. For details on compound address fields, see
Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment is delivered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the shipment is delivered.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.


Standard Objects Shipment

**Field Name** **Details**

Note: This field is available in the API only.

```
ShipToLatitude

ShipToLongitude

ShipToName

ShipToPostalCode

ShipToState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The shipment recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment is delivered.

**Type**
string


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the shipment is delivered.

```
ShipToStreet

ShipmentNumber

SourceLocationId

Status

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment is delivered.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field service location where the shipment originates.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** _`Created`_ —Shipment has been created.


Standard Objects Shipment

**Field Name** **Details**

**•** _`Delivered`_ —Shipment has been delivered.

**•** _`In Transit`_ —Shipment is in transit.

**•** _`Shipped`_ —Order has been shipped.

**•** _`Voided`_ —Shipment has been cancelled.

```
TotalItemsQuantity

TrackingNumber

TrackingUrl

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total quantity of items included in the shipment. This value is calculated as
the sum of the quantities of the shipment items in the shipment.

This field is available in API version 51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Tracking number for the shipment.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL of website used for tracking the shipment.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShipmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ShipmentFeed**

Feed tracking is available for the object.

**ShipmentHistory**

History is available for tracked fields of the object.

**ShipmentOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects ShipmentItem

**ShipmentShare**

Sharing is available for the object.

SEE ALSO:

### ShipmentItem ShipmentItem

Represents an order item included in a shipment. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution

Fields

**Field** **Details**

```
Description

ExpectedDeliveryDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the shipment item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Expected delivery date of the shipment that contains the shipment item.


Standard Objects ShipmentItem

**Field** **Details**

```
FulfillmentOrderLineItemId

OrderItemSummaryId

Product2Id

Quantity

ReturnOrderLineItemId

```

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The FulfillmentOrderLineItem (fulfillment order product) corresponding to the shipment
item.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The OrderItemSummary (order product summary) corresponding to the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product represented by the shipment item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of products represented by the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ShipmentItem

**Field** **Details**

**Description**
For a return ShipmentItem, the associated ReturnOrderLineItem.

This field is available in API version 53.0 and later.

```
ShipmentId

ShipmentItemNumber

TrackingNumber

TrackingUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The shipment that contains the shipment item.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup

**Refers To**
Shipment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking number of the shipment that contains the shipment item.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking URL of the shipment that contains the shipment item.


### Standard Objects ShippingCarrier

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShipmentItemFeed**

Feed tracking is available for the object.

**ShipmentItemHistory**

History is available for tracked fields of the object.

SEE ALSO:

Shipment

FulfillmentOrderLineItem

### ShippingCarrier

Shipping company or carrier responsible for transporting goods or packages. Examples include UPS, FedEx, and USPS. This object is
available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingCarrier object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ExternalReference

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the shipping carrier associated with the delivery. Can
be used for internal tracking or integration purposes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ShippingCarrier

**Field** **Details**

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

```
LastViewedDate

ManagedShippingCarrier

Name

ShipFromCountry

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-managed shipping carrier information that provides estimated transit times. This
field is available in API version 65.0 and later.

Possible values are:

**•** `FEDEX`

**•** `UPS`

**•** `USPS`

**Type**
text

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Country where the shipment originates. This field is available in API version 65.0 and later.

Possible values are:

**•** `AD` —Andorra

**•** `AE` —United Arab Emirates

**•** `AF` —Afghanistan


Standard Objects ShippingCarrier

**Field** **Details**

**•** `AG` —Antigua and Barbuda

**•** `AI` —Anguilla

**•** `AL` —Albania

**•** `AM` —Armenia

**•** `AO` —Angola

**•** `AQ` —Antarctica

**•** `AR` —Argentina

**•** `AS` —American Samoa

**•** `AT` —Austria

**•** `AU` —Australia

**•** `AW` —Aruba

**•** `AX` —Aland Islands

**•** `AZ` —Azerbaijan

**•** `BA` —Bosnia and Herzegovina

**•** `BB` —Barbados

**•** `BD` —Bangladesh

**•** `BE` —Belgium

**•** `BF` —Burkina Faso

**•** `BG` —Bulgaria

**•** `BH` —Bahrain

**•** `BI` —Burundi

**•** `BJ` —Benin

**•** `BL` —Saint Barthélemy

**•** `BM` —Bermuda

**•** `BN` —Brunei Darussalam

**•** `BO` —Bolivia, Plurinational State of

**•** `BQ` —Bonaire, Sint Eustatius and Saba

**•** `BR` —Brazil

**•** `BS` —Bahamas

**•** `BT` —Bhutan

**•** `BV` —Bouvet Island

**•** `BW` —Botswana

**•** `BY` —Belarus

**•** `BZ` —Belize

**•** `CA` —Canada

**•** `CC` —Cocos (Keeling) Islands

**•** `CD` —Congo, the Democratic Republic of the

**•** `CF` —Central African Republic


Standard Objects ShippingCarrier

**Field** **Details**

**•** `CG` —Congo

**•** `CH` —Switzerland

**•** `CI` —Cote d'Ivoire

**•** `CK` —Cook Islands

**•** `CL` —Chile

**•** `CM` —Cameroon

**•** `CN` —China

**•** `CO` —Colombia

**•** `CR` —Costa Rica

**•** `CU` —Cuba

**•** `CV` —Cape Verde

**•** `CW` —Curaçao

**•** `CX` —Christmas Island

**•** `CY` —Cyprus

**•** `CZ` —Czechia

**•** `DE` —Germany

**•** `DJ` —Djibouti

**•** `DK` —Denmark

**•** `DM` —Dominica

**•** `DO` —Dominican Republic

**•** `DZ` —Algeria

**•** `EC` —Ecuador

**•** `EE` —Estonia

**•** `EG` —Egypt

**•** `EH` —Western Sahara

**•** `ER` —Eritrea

**•** `ES` —Spain

**•** `ET` —Ethiopia

**•** `FI` —Finland

**•** `FJ` —Fiji

**•** `FK` —Falkland Islands (Malvinas)

**•** `FM` —Micronesia

**•** `FO` —Faroe Islands

**•** `FR` —France

**•** `GA` —Gabon

**•** `GB` —United Kingdom

**•** `GD` —Grenada

**•** `GE` —Georgia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `GF` —French Guiana

**•** `GG` —Guernsey

**•** `GH` —Ghana

**•** `GI` —Gibraltar

**•** `GL` —Greenland

**•** `GM` —Gambia

**•** `GN` —Guinea

**•** `GP` —Guadeloupe

**•** `GQ` —Equatorial Guinea

**•** `GR` —Greece

**•** `GS` —South Georgia and the South Sandwich Islands

**•** `GT` —Guatemala

**•** `GU` —Guam

**•** `GW` —Guinea-Bissau

**•** `GY` —Guyana

**•** `HK` —Hong Kong SAR China

**•** `HM` —Heard Island and McDonald Islands

**•** `HN` —Honduras

**•** `HR` —Croatia

**•** `HT` —Haiti

**•** `HU` —Hungary

**•** `ID` —Indonesia

**•** `IE` —Ireland

**•** `IL` —Israel

**•** `IM` —Isle of Man

**•** `IN` —India

**•** `IO` —British Indian Ocean Territory

**•** `IQ` —Iraq

**•** `IR` —Iran, Islamic Republic of

**•** `IS` —Iceland

**•** `IT` —Italy

**•** `JE` —Jersey

**•** `JM` —Jamaica

**•** `JO` —Jordan

**•** `JP` —Japan

**•** `KE` —Kenya

**•** `KG` —Kyrgyzstan

**•** `KH` —Cambodia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `KI` —Kiribati

**•** `KM` —Comoros

**•** `KN` —Saint Kitts and Nevis

**•** `KP` —Korea, Democratic People's Republic of

**•** `KR` —Korea, Republic of

**•** `KW` —Kuwait

**•** `KY` —Cayman Islands

**•** `KZ` —Kazakhstan

**•** `LA` —Lao People's Democratic Republic

**•** `LB` —Lebanon

**•** `LC` —Saint Lucia

**•** `LI` —Liechtenstein

**•** `LK` —Sri Lanka

**•** `LR` —Liberia

**•** `LS` —Lesotho

**•** `LT` —Lithuania

**•** `LU` —Luxembourg

**•** `LV` —Latvia

**•** `LY` —Libya

**•** `MA` —Morocco

**•** `MC` —Monaco

**•** `MD` —Moldova, Republic of

**•** `ME` —Montenegro

**•** `MF` —Saint Martin (French part)

**•** `MG` —Madagascar

**•** `MH` —Marshall Islands

**•** `MK` —North Macedonia

**•** `ML` —Mali

**•** `MM` —Myanmar

**•** `MN` —Mongolia

**•** `MO` —Macao

**•** `MP` —Northern Mariana Islands

**•** `MQ` —Martinique

**•** `MR` —Mauritania

**•** `MS` —Montserrat

**•** `MT` —Malta

**•** `MU` —Mauritius

**•** `MV` —Maldives


Standard Objects ShippingCarrier

**Field** **Details**

**•** `MW` —Malawi

**•** `MX` —Mexico

**•** `MY` —Malaysia

**•** `MZ` —Mozambique

**•** `NA` —Namibia

**•** `NC` —New Caledonia

**•** `NE` —Niger

**•** `NF` —Norfolk Island

**•** `NG` —Nigeria

**•** `NI` —Nicaragua

**•** `NL` —Netherlands

**•** `NO` —Norway

**•** `NP` —Nepal

**•** `NR` —Nauru

**•** `NU` —Niue

**•** `NZ` —New Zealand

**•** `OM` —Oman

**•** `PA` —Panama

**•** `PE` —Peru

**•** `PF` —French Polynesia

**•** `PG` —Papua New Guinea

**•** `PH` —Philippines

**•** `PK` —Pakistan

**•** `PL` —Poland

**•** `PM` —Saint Pierre and Miquelon

**•** `PN` —Pitcairn

**•** `PR` —Puerto Rico

**•** `PS` —Palestine

**•** `PT` —Portugal

**•** `PW` —Palau

**•** `PY` —Paraguay

**•** `QA` —Qatar

**•** `RE` —Reunion

**•** `RO` —Romania

**•** `RS` —Serbia

**•** `RU` —Russian Federation

**•** `RW` —Rwanda

**•** `SA` —Saudi Arabia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `SB` —Solomon Islands

**•** `SC` —Seychelles

**•** `SD` —Sudan

**•** `SE` —Sweden

**•** `SG` —Singapore

**•** `SH` —Saint Helena, Ascension and Tristan da Cunha

**•** `SI` —Slovenia

**•** `SJ` —Svalbard and Jan Mayen

**•** `SK` —Slovakia

**•** `SL` —Sierra Leone

**•** `SM` —San Marino

**•** `SN` —Senegal

**•** `SO` —Somalia

**•** `SR` —Suriname

**•** `SS` —South Sudan

**•** `ST` —Sao Tome and Principe

**•** `SV` —El Salvador

**•** `SX` —Sint Maarten (Dutch part)

**•** `SY` —Syrian Arab Republic

**•** `SZ` —Eswatini

**•** `TC` —Turks and Caicos Islands

**•** `TD` —Chad

**•** `TF` —French Southern Territories

**•** `TG` —Togo

**•** `TH` —Thailand

**•** `TJ` —Tajikistan

**•** `TK` —Tokelau

**•** `TL` —Timor-Leste

**•** `TM` —Turkmenistan

**•** `TN` —Tunisia

**•** `TO` —Tonga

**•** `TR` —Türkiye

**•** `TT` —Trinidad and Tobago

**•** `TV` —Tuvalu

**•** `TW` —Taiwan

**•** `TZ` —Tanzania, United Republic of

**•** `UA` —Ukraine

**•** `UG` —Uganda


### Standard Objects ShippingCarrierMethod

**Field** **Details**

**•** `UM` —U.S. Outlying Islands

**•** `US` —United States

**•** `UY` —Uruguay

**•** `UZ` —Uzbekistan

**•** `VA` —Holy See (Vatican City State)

**•** `VC` —Saint Vincent and the Grenadines

**•** `VE` —Venezuela, Bolivarian Republic of

**•** `VG` —Virgin Islands, British

**•** `VI` —U.S. Virgin Islands

**•** `VN` —Vietnam

**•** `VU` —Vanuatu

**•** `WF` —Wallis and Futuna

**•** `WS` —Samoa

**•** `YE` —Yemen

**•** `YT` —Mayotte

**•** `ZA` —South Africa

**•** `ZM` —Zambia

**•** `ZW` —Zimbabwe

```
OwnerId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrier object. Default value is the user logged
in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### ShippingCarrierMethod

Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of transit
times available for each carrier. This object is available in API version 61.0 and later.


Standard Objects ShippingCarrierMethod

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingCarrierMethodId object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ExternalReference

LastReferencedDate

LastViewedDate

ManagedShippingCarrierMethod

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the shipping carrier associated with the delivery. Can
be used for internal tracking or integration purposes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-managed shipping carrier method that provides estimated transit times. This field
is available in API version 65.0 and later.


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
MaxTransitTime

MinTransitTime

Name

OwnerId

```

**Type**
integer

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Maximum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the maximum transit time is set to 3, the carrier takes no more than 3 units
of the specified transit time unit to deliver the order.

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the minimum transit time is set to 1, the carrier takes at least 1 unit of the
specified transit time unit to deliver the order.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrierMethod object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
ShippingCarrierId

ShippingScope

TransitTimeUnit

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Id of the company or service responsible for transporting and delivering the order to the
customer.

This is a relationship field.

**Relationship Name**
ShippingCarrier

**Refers To**
ShippingCarrier

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of shipping carrier method. This field is available in API version 65.0 and later.

Possible values are:

**•** `Domestic`

**•** `DomesticAndInternational`

**•** `International`

The default value is `Domestic` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Unit of measurement used for transit time. Specifies the time interval in which the minimum
and maximum transit times are expressed.

The available options are:

**•** `Days`

**•** `Hours`

**•** `Weeks`


### Standard Objects ShippingConfigurationSet ShippingConfigurationSet

Shipping configuration for a set of products in a store. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingConfigurationSet object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
IsDefault

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shipping configuration is the default `(True)` or not `(False)` .

The default value is `False` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping configuration set.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the shipping configuration owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects ShippingConfigSetProduct

**Field** **Details**

**Refers To**
Group, User

```
ProcessTime

ProcessTimeUnit

TargetRecordId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time to process an order before it is ready to ship.

The default value is `1 Day` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time to process an order.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the target record.

This field is a relationship field.

**Relationship Name**
TargetRecord

**Relationship Type**
Lookup

**Refers To**
WebStore

### ShippingConfigSetProduct

Represents a product associated with a shipping configuration. This object is available in API version 64.0 and later.


Standard Objects ShippingConfigSetProduct

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingConfigSetProduct object is available only if you've a B2B Commerce or D2C Commerce license and the MultipleShippingProfile
org perm is enabled.

Fields

**Field** **Details**

```
Name

Product2Id

ShippingProfileId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping configuration set product record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Product2 record that is associated with shipping configuration set record.

This field is a relationship field.

**Relationship Name**
Product2

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile


### Standard Objects ShippingRateArea

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ShippingConfigurationSet (the master object)

### ShippingRateArea

A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateArea object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Countries

Name

Regions

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Countries in the shipping rate area.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate area.

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects ShippingRateGroup

**Field** **Details**

**Description**
Reserved for future use.

### `ShippingRateGroupId` ShippingRateGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping rate group

This field is a relationship field.

**Relationship Name**
### ShippingRateGroup

**Relationship Type**
Lookup

**Refers To**
### ShippingRateGroup

Available shipping rates based on shipping destination. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate group.


### Standard Objects SignupRequest

**Field** **Details**

```
ShippingProfileId

### SignupRequest

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile

**Relationship Type**
Lookup

**Refers To**
ShippingConfigurationSet

Represents a request for a new sign-up. SignupRequest isn’t supported in sandbox instances and will result in an error. This object is
available in API version 27.0 and later.

[Note: You’re limited to 20 sign-ups per day. To make additional sign-ups, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com)
For product, specify **Sales** . For topic, specify **AppExchange & Managed Packages** .

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Fields

**Field Name** **Details**

```
AuthCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A one-time authorization code that can be exchanged for an OAuth access token and refresh
token using standard Salesforce APIs. It’s used with `ConnectedAppCallbackUrl` and
`ConnectedAppConsumerKey` when the specified connected app hasn’t been configured
with an X.509 certificate. The system provides this read-only field after the sign-up request
has been processed. This field is available in API version 29.0 and later.


Standard Objects SignupRequest

**Field Name** **Details**

```
Company

ConnectedAppCallbackUrl

ConnectedAppConsumerKey

Country

CreatedOrgId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the company requesting the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with `ConnectedAppConsumerKey`, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with `ConnectedAppCallbackUrl`, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The default value is the country of the requesting org. To override the default, enter the
two-character, uppercase ISO-3166 country code (Alpha-2 code). A complete list of the codes
[is located at https://www.iso.org/obp/ui/#search. The language of the trial org is](https://www.iso.org/obp/ui/#search)
auto-determined based on the value of this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the trial org created. The system provides this read-only field after
the sign-up request has been processed.


Standard Objects SignupRequest

**Field Name** **Details**

```
CreatedOrgInstance

Edition

ErrorCode

FirstName

LastName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The server instance of the new trial org, for example, “na8.” This field is available in API version
29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The Salesforce template that is used to create the trial org. Possible values are `Partner`
`Group`, `Professional`, `Partner Professional`, `Sales Enterprise`,
`Professional TSO`, `Enterprise`, `Partner Enterprise`, `Service`
`Professional`, `Enterprise TSO`, `Developer`, and `Partner Developer` .
This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code if the sign-up request isn’t successful. The system provides this read-only field
for support purposes.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The first name of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The last name of the admin user for the trial sign-up.


Standard Objects SignupRequest

**Field Name** **Details**

```
PreferredLanguage

ResolvedTemplateId

ShouldConnectToEnvHub

SignupEmail

SignupSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the trial org being created. Specify the language using a language code listed
[under Fully Supported Languages in Supported Languages in Salesforce Help. For example,](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
use _`zh_CN`_ for simplified Chinese. The value you select overrides the language set by the
locale. If you specify an invalid language, the org defaults to the default language of the country.
Likewise, if you specify a language that isn’t supported by the Salesforce edition associated
with your trial template, the trial org defaults to the default language of the country. This field
is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Populated during the sign-up request and for internal use by Salesforce. This field is available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
When set to `true`, the trial org is connected to the Environment Hub. The sign-up must take
place in the hub main org or a spoke org. This field is available in API version 35.0 and later.

**Type**
email

**Properties**
Create, Filter, Group, Sort

**Description**
The email address of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects SignupRequest

**Field Name** **Details**

**Description**
A user-specified description of the trial sign-up, up to 60 characters. This field is available in
API version 36.0 and later.

```
Status

Subdomain

SuppressSignupEmails

TemplateId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the request. Possible values are `New`, `In Progress`, `Error`, or `Success` .
The default is `New` .

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The My Domain name for the new trial org used in the org’s login and application URLs. In
Developer Edition orgs, your name must contain at least 3 characters and no more than 27
characters. In all other editions, it must be at least 3 characters and no more than 34 characters.
It can include letters, numbers, and hyphens, but you can’t start the name with a hyphen.

If you don’t choose a My Domain during sign-up, Salesforce assigns one for you based on your
company name. If you don’t like the one we set, you can change it.

[For details, see My Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=domain_name_overview.htm&language=en_US)

**Type**
boolean

**Properties**
Filter, Group, Nillable, Sort

**Description**
When set to `true`, no sign-up emails are sent when the trial org is created. This field is used
for the Proxy Signup feature and is available in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Trialforce template that is the basis for the trial sign-up. Salesforce
must approve the template. If you don’t specify an edition, a template ID is required.


Standard Objects SignupRequest

**Field Name** **Details**

```
TrialDays

TrialSourceOrgId

Username

```

Usage

**Type**
anyType

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The duration of the trial sign-up in days. Must be equal to or less than the trial days for the
approved Trialforce template. If not provided, it defaults to the trial duration specified for the
Trialforce template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the Trialforce Source Organization (TSO) from which the Trialforce
template was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The username of the admin user for the trial sign-up. It must follow the address convention
[specified in RFC822: www.w3.org/Protocols/rfc822/#z10.](http://www.w3.org/Protocols/rfc822/#z10)

The Java class uses REST API to create a SignupRequest object. It authenticates to the Trialforce Management Organization (TMO) and
then posts a request to the SignupRequest object.

Here are the variables to specify in this example.

**•** SERVER—The name of the host server for the TMO, for example, _`yourInstance`_ .salesforce.com.

**•** USERNAME—The admin username for the TMO.

**•** PASSWORD—The concatenation of the admin password and the security token for the TMO. To get an email with the security token,
from your personal settings in Salesforce, select **Reset My Security Token** and click **Reset Security Token** .

**•** CLIENT_ID—From Setup in Salesforce, in the Quick Find box, enter _`Apps`_, and then select **Apps** . Under Connected Apps, click **New** .
Enter values for the required fields (Callback URL is required, but you can initially set it to any valid URL because it’s not used). Grant
full access for the OAuth scopes in the Selected OAuth Scopes selector, and click **Save** . Then copy the value of Consumer Key and
use it for this variable.

**•** CLIENT_SECRET—On the same page, click **Click to reveal** . Then copy the value of Consumer Secret and use it for this variable.

```
public class IsvSignupDriver {

   private static final String SERVER = server_name : port ;

```


Standard Objects SignupRequest

```
      private static final String USERNAME = tmo_username ;

      private static final String PASSWORD = tmo_passwordsecurity_token ;

      private static final String CLIENT_ID = consumer_key ;

      private static final String CLIENT_SECRET = consumer_secret ;

      private static SignupRequestInfo signupRequest = null;

      public static String createSignupRequest (SignupRequestInfo sr)

       throws JSONException, IOException {

        JSONObject createResponse = null;

        signupRequest = sr;

        JSONObject loginResponse = login(SERVER, USERNAME, PASSWORD);

        String instanceUrl = loginResponse.getString("instance_url");

        String accessToken = loginResponse.getString("access_token");

        createResponse = create(instanceUrl, accessToken);

        System.out.println("Created SignupRequest object: " + createResponse + "\n");

        return createResponse.toString();

      }

      /* Authenticates to the TMO using the required credentials */

      private static JSONObject login(String server, String username, String password)

       throws ClientProtocolException, IOException, JSONException {

        String authEndPoint = server + "/services/oauth2/token";

        HttpClient httpclient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(authEndPoint);

           List<NameValuePair> params = new ArrayList<NameValuePair>();

           params.add(new BasicNameValuePair("grant_type", "password"));

           params.add(new BasicNameValuePair("client_id", CLIENT_ID));

           params.add(new BasicNameValuePair("client_secret", CLIENT_SECRET));

           params.add(new BasicNameValuePair("username", username));

           params.add(new BasicNameValuePair("password", password));

           post.setEntity(new UrlEncodedFormEntity(params, Consts.UTF_8));

           BasicResponseHandler handler = new BasicResponseHandler();

           String response = httpclient.execute(post, handler);

           return new JSONObject(response);

        } finally {

           httpclient.getConnectionManager().shutdown();

        }

      }

      /* Posts a request to the SignupRequest object */

      private static JSONObject create(String instanceUrl, String accessToken)

       throws ClientProtocolException, IOException, JSONException {

        HttpClient httpClient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(instanceUrl +

            "/services/data/v27.0/sobjects/SignupRequest/");

             post.setHeader("Authorization", "Bearer " + accessToken);

             post.setHeader("Content-Type", "application/json");

```


Standard Objects SignupRequest

```
             JSONObject requestBody = new JSONObject();

             requestBody.put("TemplateId", signupRequest.getTemplateID());

             requestBody.put("SignupEmail", signupRequest.getEmail());

             requestBody.put("username", signupRequest.getUsername());

             requestBody.put("Country", "US");

             requestBody.put("Company", signupRequest.getCompanyName());

             requestBody.put("lastName", signupRequest.getLastName());

             StringEntity entity = new StringEntity(requestBody.toString());

             post.setEntity(entity);

             BasicResponseHandler handler = new BasicResponseHandler();

             String response = httpClient.execute(post, handler);

             return new JSONObject(response);

        } finally {

           httpClient.getConnectionManager().shutdown();

        }

      }

   }

```

Error Codes

If the sign-up fails, the system generates an error code that can help you identify the cause. This table shows the most important error
codes.


### Standard Objects Site

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**•** SignupRequestFeed–Feed tracking is available for the object.

**•** SignupRequestHistory–History is available for tracked fields of the object.

**•** SignupRequestOwnerSharingRule–Sharing rules are available for the object

**•** SignupRequestShare–Sharing is available for the object.

### Site

Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.


Standard Objects Site

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
AdminId

AnalyticsTrackingCode

ArchiveStatus

ArchivedById

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The site administrator designated as the contact for the site. This user receives
site-related communications from site visitors and from Salesforce.

This is a relationship field.

**Relationship Name**
Admin

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking code associated with your site. This code can be used by services
like Google Analytics to track page request data for your site.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The archived status of a site. Possible values are:

**•** `NotArchived`

**•** `TemporaritlyArchived`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Site

**Field** **Description**

**Description**
The user that archived the site.

**Relationship Name:**
ArchivedBy

**Relationship Type:**
Lookup

**Refers To:**
User

```
ArchivedDate

ClickjackProtectionLevel

DailyBandwidthLimit

DailyBandwidthUsed

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the site was archived.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sets the clickjack protection level. The options are:

**•** `AllowAllFraming` —Allow framing by any page (no protection)

**•** `SameOriginOnly` —Allow framing by the same origin only
(recommended)

**•** `NoFraming` —Don’t allow framing by any page (most protection)

This field is available in API version 30.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily bandwidth limit for the sites in your organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Site

**Field** **Description**

**Description**
The current rolling 24-hour daily bandwidth usage for the sites in your
organization.

```
DailyRequestTimeLimit

DailyRequestTimeUsed

Description

GuestRecordDefaultOwnerId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily service request time limit for the sites in your
organization. Service request time is calculated as the total server time in minutes
required to generate pages for the site.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily service request time for the sites in your
organization.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
An optional description of the site.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user in the Salesforce org that is the default owner of records created by
unauthenticated (guest) users.

This is a relationship field.

**Relationship Name**
GuestRecordDefaultOwner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects Site

**Field** **Description**

```
GuestUserId

MasterLabel

MonthlyPageViewsEntitlement

Name

OptionsAllowGuestPaymentsApi

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The site or Experience Cloud sites specific user that anonymous, unauthenticated
users run as when interacting with the site.

This is a relationship field.

**Relationship Name**
GuestUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the site as it appears in the user interface.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views allowed for the current calendar month for the sites
in your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name used when referencing the site in the API.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
Indicates whether unauthenticated guest users can access the Payments API
( `true` ) or not ( `false` ). The default is `false` . This field is available in API version
49.0 and later.

```
OptionsAllowGuestSupportApi

OptionsAllowHomePage

OptionsAllowStandardAnswersPages

OptionsAllowStandardIdeasPages

OptionsAllowStandardLookups

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable unauthenticated users to access the Support API.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard page associated with the Home tab
( `/home/home.jsp` ).

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an answers Experience
Cloud site. If you want to use default Answers pages (such as AnswersHome),
enable these pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an Ideas Experience Cloud
site. If you want to use default Ideas pages (such as IdeasHome), enable these
pages.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable the standard lookup pages. These are the windows
associated with lookup fields on Visualforce pages.

```
OptionsAllowStandardPortalPages

OptionsAllowStandardSearch

OptionsBrowserXssProtection

OptionsCachePublicVfPagesInProxies

OptionsContentSniffingProtection

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable authenticated users to access the standard Salesforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard search pages. To allow public users to perform
standard searches, enable these pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the browser's cross-site scripting protection.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether proxy servers cache this site’s publicly available pages only for
unauthenticated guest users ( `true` ) or not ( `false` ). When this field is `false`,
this site’s cache-enabled Visualforce pages are cached in the web browser for
both authenticated and unauthenticated users. The default is `true` . See
[Configure Site Caching in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable content-sniffing protection.

```
OptionsCookieConsent

OptionsCspUpgradeInsecureRequests

OptionsEnableFeeds

OptionsHasStoredPathPrefix

OptionsRedirectToCustomDomain

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether only required Salesforce-supplied cookies are allowed within
the site ( `true` ) or all cookies types are allowed: required, functional, and
advertising ( `false` ). The default is `false` . This field is available in API version
52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
boolean

**Properties**
Filter

**Description**
The option that displays the Syndication Feeds related list, where you can create
and manage syndication feeds for users on your public sites. This field is visible
only if you have the feature enabled for your organization.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether this Experience Cloud site has a customized urlPathPrefix
( `true` ) or instead uses the Experience Cloud site's `UrlPathPrefix` plus `/s`
( `false` ). The default is `false` . In other sites, this field has no effect. This field
is available in API version 50.0 and later.

**Type**
boolean


Standard Objects Site

**Field** **Description**

**Properties**
Filter

**Description**
Indicates whether requests to this site’s system-managed URLs are redirected to
the HTTPS custom domain serving this site ( `true` ) or not ( `false` ).
System-managed site URLs end in `*.my.salesforce-sites.com` or
`*.my.site.com` . In Experience Cloud sites, the default is `false` . In Salesforce
Sites, the default is `true` .

If multiple custom domains serve this site and this field is set to true, requests
are routed to the site’s primary custom URL only if it’s an HTTPS custom domain.
Otherwise, requests are redirected to the first HTTPS custom domain associated
with this site, in alphanumeric order. If no HTTPS custom domain serves this site,
this option has no effect.

This field is available in API version 52.0 and later.

```
OptionsReferrerPolicyOriginWhenCrossOrigin

OptionsRequireHttps

SiteType

Status

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable referrer policy (origin-when-cross-origin).

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Identifies whether the site is a Visualforce (Salesforce Sites) or a Site.com site.
`SiteType` is available in API version 21.0 and later. In API version 26.0 and
later, if Experience Cloud sites are enabled for your Salesforce org, the site could
also be a Network Visualforce or Network Site.com site.

**Type**
picklist


Standard Objects Site

**Field** **Description**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status for the site. For example, `Active` or `In Maintenance` .

```
Subdomain

TopLevelDomain

UrlPathPrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If you enabled Salesforce Sites or Digital Experiences before you enabled enhanced
domains on your My Domain, this field returns this site’s previous subdomain.
For example, if your domain was `mycompany.force.com`, then
`mycompany` is the subdomain.

If you enabled Salesforce Sites or Digital Experiences after you enabled enhanced
domains, this field returns a null value.

**Type**
url

**Properties**
Filter, Nillable

**Description**
The optional branded custom Web address that you registered with a third-party
domain name registrar. The custom Web address acts as an alias to your Salesforce
address.

Beginning with API version 21.0, `TopLevelDomain` is no longer available.
Instead, use the Domain and DomainSite objects.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique Salesforce URL that the public uses to access this site.

Use this read-only object to query or retrieve information on your site.


### Standard Objects SiteDetail

Associated Objects

This object has the following associated objects. Unless noted, these associated objects are available in the same API version as this
object.

**SiteFeed**

Feed tracking is available for the object.

**SiteHistory**

History is available for tracked fields of the object.

### SiteDetail

Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
   GET

```

Fields

**Field** **Details**

```
DurableId

IsRegistrationEnabled

SecureUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Site object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the site allows users to sign up.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SiteDomain

**Field** **Details**

**Description**
The URL of the website.

Note: SiteDetail fields are exposed in SOAP API version 45.0 and later. You can use Tooling API to query for SiteDetail fields in
guest user mode in API version 44.0 and earlier. In API version 45.0 and later, use SOAP API to get this data in guest user mode.
SiteDetail is still exposed in Tooling API to User Profiles with the ViewSetup permission.

### SiteDomain SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API version

21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects instead.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
Domain

SiteId

```

**Type**
url

**Properties**
Filter, Sort

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects SiteEventLog

**Field** **Description**

**Description**
The ID of the associated Site.

```
DomainType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS. This field is available in
version 24.0 of the API.

Use this read-only object to query the domains that are associated with each site in your organization.

### SiteEventLog SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version 62.0

and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects SiteEventLog

**Field** **Details**

```
CpuTime

DatabaseTotalTime

HttpHeaders

HttpMethod

IsApi

IsError

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
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DB_CPU_TIME. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP headers that were sent in the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: GET, POST, PUT, and so on.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

The default value is `false` .

**Type**
boolean


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was an error page.

The default value is `false` .

```
IsFirstRequest

IsGuest

IsSecure

LoginKey

PageName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page is the first Visualforce transaction in the request.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was a guest (unauthenticated) request.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this request is secure.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
GeJCsym5eyvtEK2I.

**Type**
string


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Visualforce page that was requested.

```
QueryString

RequestIdentifier

RequestStatus

RequestType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query, if one was performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action. This field can have a blank
value.

For example:

**•** `S`  - Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F`  - Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U`  - Undefined.

**•** `A` —Authorization error.

**•** `R`  - Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

**Type**
String


Standard Objects SiteEventLog

**Field** **Details**

**Description**
The request type.

Possible values are:

**•** `page` —a normal request for a page

**•** `content_UI` —a content request for a page that originated in the user interface

**•** `content_apex` —a content request initiated by an Apex call

**•** `PDF_UI` —a request for a page in PDF format through the user interface

**•** `PDF_apex` —a request for PDF format by an Apex call (usually a Web Service call)

```
RunTime

SessionKey

SiteIdentifier

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
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Site.com site.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: `20130715233322.670` .

**Type**
string


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `home/home.jsp` .

```
UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943YAS` .

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

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.


### Standard Objects SiteHistory SiteHistory

Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.

To access this object, Salesforce Sites must be enabled for your organization.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer Portal users can't access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

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


### Standard Objects SiteIframeWhitelistUrl

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
The last value of the field before it was changed.

```
SiteId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

### SiteIframeWhitelistUrl

Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is available
in API version 44.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.


### Standard Objects SiteRedirectMapping

Fields

**Field Name** **Details**

```
SiteId

Url

### SiteRedirectMapping

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the site to include in the inline frame.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain allowed to frame your Salesforce site or Experience Cloud site page.
Accepts these formats: example, example.com, *example.com, and
https://example.com.

Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only if Digital Experiences is enabled for your org and Create and Set Up Experiences is enabled.


Standard Objects SiteRedirectMapping

Fields

**Field** **Details**

```
Action

IsActive

IsDynamic

SiteId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the redirect.

Possible values are:

**•** `Permanent`

**•** `Temporary`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the redirect is enabled.

Default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a redirect rule is dynamic.

Default value is `false` . This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the site for the redirect.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup


### Standard Objects Skill

**Field** **Details**

**Refers To**
Site

```
Source

Target

```

Usage

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the site you want to redirect.

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the Experience Cloud site you want to users to visit.

If you build a new site on Experience Cloud but you also have an old site on a different platform, ensure that users visit the new site. Use
SiteRedirectMapping to redirect users from the external site to the Experience Cloud site.

### Skill

Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available in
API version 24.0 and later.

Note: For information about WDC skills on a user's profile, see the ProfileSkill topic.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects Skill

**Field Name** **Details**

**Description**
The description of the skill.

```
DeveloperName

Language

LastViewedDate

MasterLabel

```

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
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the skill.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the skill.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the skill.


### Standard Objects SkillLevelDefinition

**Field Name** **Details**

```
TypeId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The skill type associated with the skill.

This field is a relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
Type

**Refers To**
SkillType

**Chat**
Use this object to assign Chat users to groups based on their abilities. The skills associated with a LiveChatButton determine which
agents receive chat requests that come in through that button.

**Field Service**
Use this object to track certifications and areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page. When you assign a skill to a service resource,
you can specify their skill level and the duration of the skill.

**•** Add it as a required skill via the Skill Requirements related list on any work type, work order, or work order line item. When you
add a required skill to a work record, you can specify the skill level.

**Workforce Engagement**
Use this object to specify areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page.

**•** Add it as a required skill via the Skill Requirements related list on a job profile.

### SkillLevelDefinition

Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version
51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SkillLevelDefinition

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
Description

IsAutoApproved

LearningContent

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Describes the mapping.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this mapping auto-approves.

The default value is 'false'.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The titles of the Trailhead modules associated to this mapping.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the Skill Level Definition.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects SkillLevelProgress

**Field** **Details**

**Refers To**
Group, User

```
SkillId

### `SkillLevel`

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill that this mapping is for.

This is a relationship field.

**Relationship Name**
### Skill

**Relationship Type**
Lookup

**Refers To**
### Skill

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The level to assign for the skill.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelDefinitionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelDefinitionShare on page 67**
Sharing is available for the object.

### SkillLevelProgress

Represents training progress for a given user. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SkillLevelProgress

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
CompletedCount

CompletedDate

OwnerId

ServiceResourceId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of modules that have been completed towards this Skill Mapping.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this progress was completed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of skill level progress.

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
Create, Filter, Group, Sort, Update


Standard Objects SkillLevelProgress

**Field** **Details**

**Description**
The Service Resource that will be granted a service resource skill when the progress is
complete.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
SkillLevelDefinitionId

SkillMasterLabel

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The corresponding skill mapping for this progress.

This is a relationship field.

**Relationship Name**
SkillLevelDefinition

**Relationship Type**
Lookup

**Refers To**
SkillLevelDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The master label of the Skill associated with the associated SkillLevelDefinition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the progress.

Possible values are:

**•** `A` —Approved


### Standard Objects SkillProfile

**Field** **Details**

**•** `R` —Review

### • S —Started

The default value is 'S'.

```
TotalCount

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total number of modules that need to be completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelProgressOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelProgressShare on page 67**
Sharing is available for the object.

### SkillProfile

Represents a join between Skill and Profile. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the profile.


### Standard Objects SkillRequirement

**Field Name** **Details**

```
SkillId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

Use this object to assign specific skills to specific profiles.

### SkillRequirement

Represents a skill that is required to complete a particular task in Field Service, Omni-Channel, Salesforce Scheduler, or Workforce
Engagement. Skill requirements can be added to pending service routing objects in Omni-Channel. They can be added to work types,
work orders, and work order line items in Field Service and Lightning Scheduler. And they can be added to job profiles in Workforce
Engagement. This object is available in API version 38.0 and later. You also can add skill requirements to work items in Omni-Channel
skills-based routing using API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

If you want to use SkillRequirement for Field Service use cases, then Field Service must be enabled.

If you want to use SkillRequirement only for Omni-Channel skills-based routing use cases, then you don't need Field Service to be enabled.

If you want to use SkillRequirement for Workforce Engagement use cases, then Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
IsAdditionalSkill

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects SkillRequirement

**Field Name** **Details**

**Description**
Indicates that a skill is additional. After a designated timeout period, a skill marked
as additional is dropped from Omni-Channel routing. The case is then routed to
the best-matched agent even if they don’t have all the skills.

```
LastReferencedDate

LastViewedDate

RelatedRecordId

SkillId

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
The timestamp when the current user last viewed this record. If this value is null,
this record might only have been referenced ( `LastReferencedDate` ) and
not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the skill is required for. The related record can be a work order,
work order line item, work type, or pending service routing record.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
WorkOrder, WorkOrderLineItem, WorkType

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SkillRequirement

**Field Name** **Details**

**Description**
The skill that is required.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

```
SkillLevel

SkillNumber

SkillPriority

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The level of the skill required. Skill levels can range from zero to 99.99. Depending
on your business needs, you can have the skill level to reflect years of experience,
certification levels, or license classes.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the skill requirement.

**Type**
int

**Properties**
Aggregatable, Create, Filter, Group, Nillable, Sort, Update

**Description**
For additional skills, specify the order in which skills are dropped if after the
specified timeout no agent with that skill is available. Higher priority-value skills
are dropped first. Lower priority-value skills, for example 0, are dropped last. Skills
with the same priority value are dropped as a group. You can set skill priority
using skills-based routing rules or Apex code.


### Standard Objects SkillUser

Usage

**Field Service**
Skill requirements help dispatchers assign work orders to service resources with the proper expertise. You can still assign a work order,
work order line item, or related service appointment to a service resource that does _not_ have the specified skills, so skill requirements
serve more as a suggestion than a rule.

Note: If you’re using the Field Service managed package, use matching rules to ensure that appointments are only assigned to
service resources who possess the skills listed on the parent work order.

If many of your work orders require the same skills, add skill requirements to work types to save time and keep your processes consistent.
When you add a skill requirement to a work type, work orders and work order line items that use that type automatically inherit the skill
requirement. For example, if all annual maintenance visits for your Classic Refrigerator product require a Refrigerator Maintenance skill
level of at least 50, add that skill requirement to the Annual Maintenance Visit work type. When you create a work order for a customer’s
annual fridge maintenance, applying that work type adds the skill requirement as well.

**Omni-Channel**

We recommend that you use Omni-Channel flow or skills-based routing rules to create skills-based routing requests. When you do so,
work items are routed by creating a PendingServiceRouting object. The PendingServiceRouting object can have multiple SkillRequirements
objects associated with it. When a work item requires multiple skills, it’s routed to an agent who has all of the required skills. The
PendingServiceRouting object adds attributes to the work item that represent the skill (skill id), priority, skill proficiency, and timestamp.

**Workforce Engagement**

Workforce Engagement uses skill requirements to assign shifts to agents who have the right skills. You can still assign shifts to service
resources if they don’t have those skills.

In a non-Omni workflow, create a scheduling rule that matches agents to shifts based on their skills and the job profile's skill requirements.
Shift scheduling tools can then assign agents with the right skills.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**SkillRequirementChangeEvent (API version 54.0)**
Change events are available for the object.

**SkillRequirementFeed**

Feed tracking is available for the object.

**SkillRequirementHistory**

History is available for tracked fields of the object.

### SkillUser

Represents a join between Skill and User. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`


### Standard Objects SlackChannelRelatedRecord

Fields

**Field Name** **Details**

```
SkillId

UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the user.

Use this object to assign specific skills to specific users.

### SlackChannelRelatedRecord

Represents the related record mapping between a Slack channel and a Salesforce record that’s made when you create a Salesforce
channel. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the related record mapping.


### Standard Objects SlaProcess

**Field** **Details**

```
RelatedRecord

SlackChannel

TopLevelTeam

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The Salesforce record ID associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack channel ID of the Salesforce channel associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack Enterprise org ID associated with the Salesforce channel.

Use this object to retrieve and query the related record mapping between a Slack channel and a Salesforce record. You can select this
object in Salesforce Flow Builder and Slack Workflow Builder to trigger actions when a Salesforce channel is created.

This object is read only. You can’t create, modify, or delete the related record mappings between Slack channels and Salesforce records
using this object.

### SlaProcess

Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.

An entitlement process is a timeline that includes all the steps (MilestoneType records) that your support team must complete to resolve
cases. Each process includes the logic necessary to determine how to enforce the correct service level for your customers.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`, `describeLayout()`


Standard Objects SlaProcess

Special Access Rules

As of Summer ’20 and later, only Salesforce admin users, users with access to the Case, Entitlement, or Work Order objects, and users
with the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
BusinessHoursId

Description

IsActive

IsVersionDefault

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
textarea

**Properties**
Filter, Nillable

**Description**
A description of the entitlement process.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the entitlement process is active ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the entitlement process is the default version ( `true` ) or not
( `false` ).

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
dateTime


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the SlaProcess was last viewed.

```
Name

NameNorm

SObjectType

StartDateField

```

**Type**
string

**Properties**
Filter, idLookup

**Description**
The name of the entitlement process.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The read-only value for the unique name of the entitlement process or the entitlement
process version. If entitlement versioning is enabled, this value is automatically
generated for each version of an entitlement process in this form: _`process`_
_`name`_ +_v + _`x`_, where _`x`_ is the version number (for example, “gold_support_v2”).

If entitlement versioning isn’t enabled, this value is the same as `Name` .

This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Restricted picklist, Filter, Group, Sort

**Description**
The type of records that the entitlement process can run on. Its values are:

**•** _`Case`_

**•** _`Work Order`_

An entitlement process runs only on records that match its type. For example, a Case
entitlement process that’s applied to an entitlement runs only on cases associated
with the entitlement, not on work orders. As a best practice, therefore, manage
customers’ work orders and cases on separate entitlements.

The field label in the user interface is Entitlement Process Type.

**Type**
picklist


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Restricted picklist

**Description**
The criteria for cases to enter the entitlement process. Cases can enter the process
based on:

**•** The creation date on a case

**•** A custom date/time field on a case

```
VersionMaster

VersionNotes

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence of versions to which this entitlement process belongs. This
field’s contents can be any value as long as it is identical among all versions of the
entitlement process.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the entitlement process version.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the entitlement process. Must be 1 or greater.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.


### Standard Objects Snippet

Usage

Use this object to query entitlement processes on entitlements.

SEE ALSO:

Entitlement

MilestoneType

CaseMilestone

### Snippet

Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates. This
object is available in API version 47.0 and later.

Supported Calls

`create(),delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
Description

DeveloperName

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the snippet. Limited to 32 KB.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This field value is unique to your org and is required for a Snippet to be resolved
in marketing content. Label is **API Name** .

**Type**
dateTime


Standard Objects Snippet

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

Type

Value

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
Required. The name of the snippet.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of content a snippet includes. Allowable values are: Date, Image, Link, Text. This
field is for organizational purposes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body content of a snippet. This field can contain plain or rich text. The value of a snippet
is resolved when a marketing email is sent. The field does not support emojis, HTML, or image
files.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects SnippetAssignment

**SnippetFeed**

Feed tracking is available for the object.

### SnippetAssignment

Represents a relationship between a snippet and a campaign. Assignments are required to use snippet content in Account Engagement
emails and email templates. A snippet can be assigned to more than one campaign. This object is available in API version 47.0 and later.

Supported Calls

create( ), delete( ), describeLayout( ), describeSObjects( ), getDeleted( ), getUpdated( ), query( ), retrieve( )

Special Access Rules

Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
ParentId

SnippetId

### SoapApiEventLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related snippet record

SOAP API events contain details about your org's SOAP API request activity. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects SoapApiEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiType

ClientIp

ClientName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The name of the client that’s using Salesforce services. This field is an optional parameter
that can be passed in API calls. If blank, the caller didn't specify a client in the CallOptions
header.

```
CpuTime

DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

ExceptionMessage

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
that adding indexes or filters on your queries would benefit performance.

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

```
LoginKey

MethodName

ObjectName

RequestIdentifier

RequestSize

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
Filter, Group, Nillable, Sort

**Description**
The name of the calling Apex method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request. For example: `Account`,
`Opportunity`, `Contact`, and so on.

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The size of the callout request body, in bytes.

```
RequestStatus

ResponseSize

RowsProcessed

RunTime

```

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
The size of the callout response, in bytes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the request. For example: `150` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.


Standard Objects SoapApiEventLog

**Field** **Details**

```
SessionKey

Timestamp

Uri

UserIdentifier

UserType

```

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


### Standard Objects SocialPersona

**Field** **Details**

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

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### SocialPersona

Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version 22.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AreWeFollowing

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a Salesforce social account is following the social persona or
not.


Standard Objects SocialPersona

**Field Name** **Details**

```
AuthorLabels

AvatarUrl

Bio

ExternalId

ExternalPictureURL

Followers

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Comma-separated list of author type tags.

**Type**
string

**Properties**
Nillable

**Description**
Retrieves the user's social network avatar. It's a read-only field and you can't
specify or update its value.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Biography of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona on the social network.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL to the picture of the social persona on the social network.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPersona

**Field Name** **Details**

**Description**
Number of followers that the social persona has.

```
Following

InfluencerScore

IsBlacklisted

IsDefault

IsFollowingUs

IsVerified

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of people that the social persona is following.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 score describing the influence of the social persona. No longer used.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is blacklisted or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona supplies the default avatar image that’s
displayed on the contact or account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is following a Salesforce social account or
not.

**Type**
boolean


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is verified or not.

```
LastReferencedDate

LastViewedDate

ListedCount

MediaProvider

MediaType

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network type of the social persona.

**Type**
string


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social persona.

```
NumberOfFriends

NumberOfTweets

ParentId

ProfileType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of friends that the social persona has.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of tweets made by the social persona.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact parent record for the social persona.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead, SocialPost

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of profile. Values are:

**•** `Person`

**•** `Page`


Standard Objects SocialPersona

**Field Name** **Details**

```
ProfileUrl

Provider

R6SourceId

RealName

SourceApp

TopicType

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Social network, such as Facebook or Twitter, of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Real name of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Salesforce product that created the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of topic, such as keyword or managed.


### Standard Objects SocialPost

Usage

The fields on a SocialPersona object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected a post from the social persona. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SocialPersonaHistory (API version 26.0)**
History is available for tracked fields of the object.

### SocialPost

Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AnalyzerScore

AssignedTo

AttachmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Score set on the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
User in Social Studio that the social post is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the first attachment on the social post. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `APPLICATION`

**•** `AUDIO`

**•** `IMAGE`

**•** `LINK`

**•** `TEXT`

**•** `UNKNOWN`

**•** `VIDEO`

```
AttachmentUrl

Classification

CommentCount

Content

DeletedById

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the first attachment on the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Classification for the social post, such as inquiry or customer case.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of comments on the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
If the social post is deleted, ID of the person who deleted the social post.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

```
EngagementLevel

ExternalPostId

Handle

HarvestDate

Headline

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Engagement level of the social post, such as reviewed or resolved.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social post in its social network.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Handle of the person who posted the social post.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when Social Studio collected the social post.

**Type**
string


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Headline of the social post.

```
HiddenById

InboundLinkCount

IsOutbound

KeywordGroupName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the social post is hidden, ID of the person who hid it.

This is a relationship field.

**Relationship Name**
HiddenBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of links on the inbound social post.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social post is outbound or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field that is no longer used.


Standard Objects SocialPost

**Field Name** **Details**

```
Language

LastReferencedDate

LastViewedDate

LikedBy

LikesAndVotes

MediaProvider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Language of the social post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the managed social account in the social network that liked the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 number of likes and votes on the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social post.


Standard Objects SocialPost

**Field Name** **Details**

```
MediaType

MessageType

Name

Notes

OutboundSocialAccountId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of social network of the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of message. Values are:

**•** `Comment` —Facebook comment

**•** `Direct` —Twitter direct message

**•** `Post` —Facebook post

**•** `Private` —Facebook private message

**•** `Reply` —Twitter or Facebook reply

**•** `Retweet` —Twitter retweet

**•** `Tweet` —Twitter tweet

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes added by Social Hub actions for the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the social account used for outbound social posts.


Standard Objects SocialPost

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
OutboundSocialAccount

**Relationship Type**
Lookup

**Refers To**
ExternalSocialAccount

```
OwnerId

ParentId

PersonaId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the social post.

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
ID of the parent record of the social post, for example, the ID of a case.

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


Standard Objects SocialPost

**Field Name** **Details**

**Description**
ID of the social persona who made the post.

This is a relationship field.

**Relationship Name**
Persona

**Relationship Type**
Lookup

**Refers To**
SocialPersona

```
PostPriority

PostTags

PostUrl

Posted

Provider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of the social post set in Social Studio.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of tags on the social post.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the social post.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Sort, Update

**Description**
Date and time when the social post was made.

**Type**
picklist


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Social network of the social post.

```
R6PostId

R6SourceId

R6TopicId

Recipient

RecipientType

ReplyToId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique ID of the post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the author in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for either the topic profile or the managed account in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recipient of the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the recipient of the social post, such as a person.

**Type**
reference


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Dynamically generated from replyToExternalPostId in Social Studio.

This is a relationship field.

**Relationship Name**
ReplyTo

**Relationship Type**
Lookup

**Refers To**
SocialPost

```
ResponseContextExternalId

ReviewScale

ReviewScore

ReviewedStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External ID, such as a conversation ID, author ID, or post ID, for the item you’re
responding to.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review scale for the social post.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review score for the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the social post review.


Standard Objects SocialPost

**Field Name** **Details**

```
Sentiment

Shares

SourceTags

SpamRating

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Sentiment of the social post. Values are:

**•** `Negative`

**•** `Neutral`

**•** `Positive`

**•** `SomewhatNegative`

**•** `SomewhatPositive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post has been shared.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of author type tags.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Spam rating of the social post. Values are:

**•** `NotSpam`

**•** `Spam`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
Status of the social post. Values are:

**•** `DELETED`

**•** `FAILED`

**•** `HIDDEN`

**•** `PENDING`

**•** `PENDING_APPROVAL`

**•** `RECALL_APPROVAL`

**•** `REJECTED_APPROVAL`

**•** `REPLIED`

**•** `SENT`

**•** `UNKNOWN`

```
StatusMessage

ThreadSize

TopicProfileName

TopicType

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status message for the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the topic profile for the social post in Social Studio.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of topic. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `Keyword`

**•** `Managed`

```
TruncatedContent

UniqueCommentors

ViewCount

WhoId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Truncated content of the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of unique people who commented on the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post was viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Polymorphic ID of a person such as a lead or a contact.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead


### Standard Objects Solution

Usage

The fields on a SocialPost object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected the post from the social network. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SocialPostChangeEvent (API version 48.0)**
Change events are available for the object.

**SocialPostFeed (API version 26.0)**
Feed tracking is available for the object.

**SocialPostHistory (API version 26.0)**
History is available for tracked fields of the object.

**SocialPostOwnerSharingRule**

Sharing rules are available for the object.

**SocialPostShare**

Sharing is available for the object.

### Solution

Represents a detailed description of a customer issue and the resolution of that issue.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsDeleted

IsHtml

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


Standard Objects Solution

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution is an HTML solution ( `true` ) or not ( `false` ).

```
IsOutOfDate

IsPublished

IsPublishedInPublicKb

IsReviewed

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Read-only field that indicates whether a solution master has been updated since the translated
version was created ( `true` ) or not ( `false` ). Note that this field does not appear in the page
layout of master solutions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published ( `true` ) or not ( `false` ). A solution’s
published state does not affect how it can be used, or whether you can query, update, or
delete it. Label is **Public** . Prior to Spring ‘14, the label was **Visible in Self-Service Portal**

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published as a Public Solution ( `true` ) or not
( `false` ). Label is **Visible in Public Knowledge Base** .

This field only applies to solutions, not articles in the public knowledge base.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution has been reviewed ( `true` ) or not ( `false` ). This flag can
only be set indirectly via the `Status` picklist. Each predefined `Status` value implies an
`IsReviewed` value. Label is **Reviewed** .


Standard Objects Solution

**Field** **Details**

```
LastReferencedDate

LastViewedDate

OwnerId

ParentId

RecordTypeId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the Solution.

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
Create, Defaulted on create, Filter, Update

**Description**
ID of the master solution, if this is the translation of a master solution.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects Solution

**Field** **Details**

**Description**
ID of the RecordType to which the Solution is associated.

```
SolutionLanguage

SolutionName

SolutionNote

SolutionNumber

Status

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
The language that the solution is written in, such as `French` or `Chinese`
`(Traditional)` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. If a client application creates a new Solution and a value for this field is unspecified,
a hyphen (-), the default value for this field, is used. Limit: 255 characters. Label is **Title** .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the Solution record. Limit: 32,000 characters. Label is **Solution Details** . If you
have HTML Solutions enabled, any HTML tags used in this field are verified before the object
is created or updated. If invalid HTML is entered, an error is thrown. Any JavaScript used in
this field is removed before the object is created or updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An identifying number that is assigned automatically when a solution is created. It can’t be
set directly, and it can’t be modified.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects SolutionStatus

**Field** **Details**

**Description**
Required. The status of the solution. Directly controls the `IsReviewed` value. To obtain
the status values in the picklist, a client application can query the SolutionStatus.

```
TimesUsed

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times this solution has been used. Label is **Num Related Case** .

Use this object to manage your organization’s solutions. Client applications can create, update, delete, and query Attachment records
associated with a solution.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SolutionFeed (API version 18.0)**
Feed tracking is available for the object.

**SolutionHistory**

History is available for tracked fields of the object.

SEE ALSO:

CategoryData

CategoryNode

### SolutionStatus

Represents the status of a Solution, such as Draft, Reviewed, and so on.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects SolutionStatus

Fields

**Field** **Details**

```
ApiName

IsDefault

IsReviewed

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
Indicates whether this is the default solution status value ( `true` ) or not ( `false` ) in the
picklist. Only one value can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this solution status value represents a reviewed Solution ( `true` ) or not
( `false` ). Multiple solution status values can represent a reviewed Solution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this solution status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the solution status picklist. These numbers are not
guaranteed to be sequential, as some previous solution status values might have been
deleted.


### Standard Objects SolutionTag

Usage

This object represents a value in the solution status picklist. The solution status picklist provides additional information about the status
of a Solution, such as whether a given status value represents a reviewed or unreviewed solution. Your client application can query this
object to retrieve the set of values in the solution status picklist, and then use that information while processing Solution objects to
determine more information about a given solution. For example, the application could test whether a given case has been reviewed
or not based on its `Status` value and the value of the `IsReviewed` property in the associated SolutionStatus record.

SEE ALSO:

### Solution SolutionTag

Associates a word or short phrase with a Solution.

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


### Standard Objects SOSDeployment

**Field Name** **Details**

**Description**
ID of the parent TagDefinition object that owns the tag.

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

SolutionTag stores the relationship between its parent TagDefinition and the Solution being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### SOSDeployment

Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API
version 34.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SOSDeployment

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
Language

MasterLabel

OptionsIsBackwardFacingCameraEnabled

OptionsIsEnabled

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the deployment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether customers can use the backwards-facing camera on their
mobile devices to talk to SOS agents.

**Type**
boolean

**Properties**
Create, Filter, Update


### Standard Objects SOSSession

**Field Name** **Details**

**Description**
Determines whether the deployment is enabled for customers to request new
SOS video calls.

```
OptionsIsVoiceOnlyMode

QueueId

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether video functionality is disabled for customers, making it so
customers can only talk to SOS agents using only audio.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the queue that’s associated with the SOS deployment.

Use this object to query and manage SOS deployments.

### SOSSession

This object is automatically created for each SOS session and stores information about the session. This object is available in API versions
34.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AppVersion

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The version of the customer’s mobile application in which SOS is implemented.

```
CaseId

ContactId

DeploymentId

EndTime

IpAddress

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the SOS deployment that the SOS session originated from.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session ended.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
To protect the customer’s privacy, this field is now blank.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The date and time that the session record was last referenced by a user.

```
LastViewedDate

Name

OpentokSession

OwnerId

SessionDuration

SessionRecordingUrl

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the session.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The ID of the OpenTok session that’s associated with the SOS video call.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the session record’s owner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time that the SOS session lasted.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The URL where the SOS session recording is stored.

```
SosVersion

StartTime

SystemInfo

WaitDuration

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of SOS that was used in your organization’s mobile application when
this session occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session began.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the customer’s mobile device from which the SOS call
originated, such as the device’s operating system.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time the customer waited before an agent accepted the SOS
session and the call began.

Use this object to query and manage SOS session records.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects SOSSessionActivity

**SOSSessionFeed**

Feed tracking is available for the object.

**SOSSessionHistory**

History is available for tracked fields of the object.

**SOSSessionOwnerSharingRule**

Sharing rules are available for the object.

**SOSSessionShare**

Sharing is available for the object.

### SOSSessionActivity

Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object is
available in API version 34.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ActivityTime

Name

SessionId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the activity occurred.

**Type**
string

**Properties**
Autonumber, Defaulted on create, idLookup, Filter, Sort

**Description**
The name of the activity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the SOS session that’s associated with the event.


### Standard Objects StagedEmail

**Field Name** **Details**

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of activity that occurred.

Use this object to query and manage SOS session activities.

### StagedEmail

For internal use only.

### StagedInviteeEmail

Represents an email address that is included on a calendar event but that doesn’t match an existing user, contact, or lead record. This
object is available in API version 66.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on.

Fields

**Field** **Details**

```
Name

OwnerId

```

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The invited email address.

**Type**
reference


### Standard Objects StagedUnmtchdEmailAddr

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the record owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### StagedUnmtchdEmailAddr

Represents data about an email address identified by Einstein Activity Capture that doesn’t match to an existing user, contact, or lead
record. These addresses are only stored temporarily. Related to StagedUnmtchdEmailAddrRela, which represents data about the email
message or calendar event activity associated with an unmatched email. This object is available in API version 66.0 and later.

These addresses are only stored temporarily. An unmatched email address is automatically deleted from StagedUnmtchdEmailAddr if
it converts into a contact record. To convert, a user saves it from their Suggested Contacts list or the address crosses a threshold in the
automatic contact creation setting. An unmatched email address is also deleted after 30 days from the initial appearance without
subsequent activity.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.

Fields

**Field** **Details**

```
CreatedContactOrLeadId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the contact or lead record created from a suggestion. Read only.


Standard Objects StagedUnmtchdEmailAddr

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
CreatedContactOrLead

**Refers To**
Contact, Lead

```
EmailAddress

FirstName

IgnoreSuggestionEndDate

LastInteractionDate

LastName

```

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address of the suggested contact. This address doesn’t match any existing user,
contact, or lead. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
First name of the suggested contact.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If a user dismisses a suggestion, it isn't suggested again until this date.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the user last interacted with the unmatched email address through email or a
scheduled calendar event. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Last name of the suggested contact.


### Standard Objects StagedUnmtchdEmailAddrRela

**Field** **Details**

```
OccurrenceCount

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of times the user and the unmatched email address occur together. (Read
only.)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the user associated with the unknown email address. (Read only.)

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

### StagedUnmtchdEmailAddrRela

Represents data about the message or event activity associated with an email address that Einstein Activity Capture can’t match with
an existing user, contact, or lead record. Related to StagedUnmtchdEmailAddr, which represents data about the unmatched email
address. This object is available in API version 66.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.


Standard Objects StagedUnmtchdEmailAddrRela

Fields

**Field** **Details**

```
RelatedActivityId

SourceActivity

StagedUnmatchedEmailAddressId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related activity record, such as an email message or calendar event.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedActivity

**Refers To**
EmailMessage, Event, StagedEmail

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The activity type. Possible values are:

**•** `Event`

**•** `StagedEmail`

**•** `EmailAddress`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related unmatched email address record.

This field is a relationship field.

**Relationship Name**
StagedUnmatchedEmailAddress

**Relationship Type**
Master-detail

**Refers To**
StagedUnmtchdEmailAddr


### Standard Objects Stamp Stamp

Represents a User Specialty. This object is available in API version 39.0 and later.

Create User Specialty labels. Specialties can be any term you want, up to 50 characters, including spaces and underscores.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Description**

```
Description

MasterLabel

ParentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Use this field to describe what the user specialty means and how it applies to a
user. You have a 255 character maximum including spaces and underscores.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The User Specialty label that appears under the user’s profile picture. You can
create any label you want as long as it’s within the 50 character maximum,
including spaces and underscores.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id of the org or network.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Organization


### Standard Objects StampAssignment StampAssignment

Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.

Assign a User Specialty to users. This label appears beneath their profile photo.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
StampId

SubjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique id generated when creating a user specialty.

This is a relationship field.

**Relationship Name**
### Stamp

**Relationship Type**
Lookup

**Refers To**
### Stamp

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id for the user getting the User Specialty label.

This is a relationship field.

**Relationship Name**
Subject

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects StandardInvocableActionType StandardInvocableActionType

Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This object
is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Marketing Cloud Growth edition and the Manage Flow user permission or View Flows user permission are required.

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

Namespace

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name and namespace combination of the invocable action. This combination
must be unique.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code of the invocable action. For a full list of supported languages and their
[codes, see Supported Languages. This field is available in API version 60.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the invocable action. This display value is the internal label that doesn’t get
translated. This field is available in API version 60.0 and later.

**Type**
string


### Standard Objects StandardShippingRate

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the invocable action. Enter a value only if you’re using the invocable action
in Flow Builder or with Apex.

### StandardShippingRate

Standard shipping rate for a store. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The StandardShippingRate object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ConditionFactor

ConditionRangeMax

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Conditions that affect the shipping rate.

Possible values are:

**•** `OrderPriceFactor` —Condition based on the order price value.

**•** `OrderWeightFactor` —Condition based on delivery weight. This value is available
in API version 62.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum value of the shipping rate condition.


Standard Objects StandardShippingRate

**Field** **Details**

```
ConditionRangeMin

CurrencyIsoCode

Name

Price

ShippingCarrierMethodId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Minimum value of the shipping rate condition. This value can't be negative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the standard shipping rate.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Price of standard shipping.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shipping service carrier method. This field is available in API version 61.0 and later.

This field is a relationship field.


Standard Objects StandardShippingRate

**Field** **Details**

**Relationship Name**
ShippingCarrierMethod

**Relationship Type**
Lookup

**Refers To**
ShippingCarrierMethod

```
ShippingZoneId

TransitTimeMax

TransitTimeMin

TransitTimeUnit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping zone.

This field is a relationship field.

**Relationship Name**
ShippingZone

**Relationship Type**
Parent-detail

**Refers To**
ShippingRateArea (the master object)

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum value of the shipping transit time. This field is available in API version 61.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum value of the shipping transit time. This value can't be negative. This field is available
in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects StaticResource

**Field** **Details**

**Description**
Unit of value for shipping transit time. This field is available in API version 61.0 and later.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

```
WeightUnit

### StaticResource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of measurement for the weight of the cart items. This field is available in API version
62.0 and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

Represents a static resource that can be used in Visualforce markup.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Body

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Required. Encoded file data.


Standard Objects StaticResource

**Field** **Details**

```
BodyLength

CacheControl

ContentType

Description

Name

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the file (in bytes).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The sharing policy for the static resource when cached. The cache control can have one of
these values:

**•** `Private` specifies that the static resource is accessible to all authenticated users. The
static resource is stored on the Salesforce server in a user’s individual cache for the
duration of the session.

**•** `Public` specifies that the static resource is accessible after caching to all internet traffic,
including unauthenticated users. The resource is stored on the Salesforce server in a
shared cache, which results in faster load times.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Type of content. Label is **Mime Type** . Limit: 120 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the static resource. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the static resource.


Standard Objects StaticResource

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

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

Use static resources to upload content that you can reference in Visualforce markup, including archives (such as .zip and .jar files), images,
stylesheets, JavaScript, and other files. Using a static resource is preferable to uploading a file to the Documents tab because:

**•** You can package a collection of related files into a directory hierarchy and upload that hierarchy as a .zip or .jar archive.

**•** You can reference a static resource in page markup by name using the `$Resource` global variable instead of hard-coding
document IDs.

Encoded Data

The API sends and receives the binary file data encoded as a base64 data type. Prior to creating a record, clients must encode the binary
file data as base64. Upon receiving an API response, clients must decode the base64 data to binary. The SOAP client usually handles this
conversion.


### Standard Objects StoreIntegratedService

Maximum Static Resource Size

You can create or update static resources to a maximum size of 5 MB. An organization can have up to 250 MB of static resources, total.

SEE ALSO:

ApexComponent

ApexPage

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

### StoreIntegratedService

Represents an association between an integration and a store. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The StoreIntegratedService object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Integration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The integration ID.

Possible values are:

**•** If the integration is a RegisteredExternalService:

**–** The ID of the RegisteredExternalService OR

**–** [ServiceProviderType]__[DeveloperName]

**•** ServiceProviderType: Price, Inventory, Tax, or Shipment

**•** DeveloperName of RegisteredExternalService

**•** If the integration is a PaymentGateway:

**–** The ID of the PaymentGateway

**•** If the integration is a Flow:


### Standard Objects StreamingChannel

**Field** **Details**

**–** [ServiceProviderType]__[NamespacePrefix]__[ApiName]

**–** If NamespacePrefix is null, it’s [ServiceProviderType]__[ApiName]

**•** ServiceProviderType: Flow

**•** ApiName and NamespacePrefix of FlowDefinitionView

**•** If the integration is the Salesforce Standard pricing:

**–** [ServiceProviderType]__B2B_STOREFRONT__StandardPricing

**•** ServiceProviderType: Price

```
ServiceProviderType

StoreId

### StreamingChannel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The type of integration service provider.

Possible values are:

**•** `Flow`

**•** `Inventory`

**•** `Payment`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique ID for the store.

Represents a channel that is the basis for notifying listeners of generic Streaming API events. This object is available in API version 29.0
and later.


Standard Objects StreamingChannel

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** You can create a permission set and grant users read and create access to all streaming channels in the org. This access isn’t for a
specific channel, like with user sharing.

**•** You can apply user sharing to StreamingChannel. You can restrict access to receiving or sending events on a channel by sharing
channels with specific users or groups. Channels shared with public read-only or read-write access send events only to clients
subscribed to the channel that also are using a user session associated with the set of shared users or groups. Only users with
read-write access to a shared channel can generate events on the channel, or modify the actual StreamingChannel record.

Fields

**Field** **Details**

```
Description

IsDynamic

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the StreamingChannel. Limit: 255 characters.

**Label:** Description

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the channel gets dynamically created on subscribe if necessary, `false` otherwise.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:


Standard Objects StreamingChannel

**Field** **Details**

```
LastViewedDate

Name

OwnerId

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
Required. Descriptive name of the streaming channel. Limit: 80 characters, alphanumeric
and “_”, “/” characters only. Must start with “/u/”. This value identifies the channel and must
be unique.

**Label:** Streaming Channel Name

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the streaming channel.

**Label:** Owner Name

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Dynamic Streaming Channel

Streaming API generic streaming supports dynamic streaming channel creation, which creates a StreamingChannel when a client first
subscribes to the channel. To enable dynamic streaming channels in your org, from Setup, enter _`User Interface`_ in the Quick


### Standard Objects Salesforce Surveys Object Model

Find box, then select **User Interface** . Enable **Enable Dynamic Streaming Channel Creation** . You can also enable dynamic channel
creation in Metadata API using EventSettings.

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/intro_stream.htm)_

### Salesforce Surveys Object Model

Learn about how Salesforce Surveys objects relate to one another in Salesforce.

[This diagram represents the object model for Salesforce Surveys. For more details and a larger image, visit the Data Model Gallery.](https://developer.salesforce.com/docs/platform/data-models/guide/salesforce-surveys.html)

### Survey

Represents a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the Survey object using the Object Manager.

Fields

**Field Name** **Details**

```
ActiveVersionID

```

**Type**
reference


Standard Objects Survey

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the survey version currently activated.

```
Description

DeveloperName

IsPartialSaveEnabled

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Nillable

**Description**
The description of the survey. This field isn’t visible in the UI.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The survey’s unique API name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to save the partial responses for the survey ( `true` ) or not
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey.


Standard Objects Survey

**Field Name** **Details**

```
LatestVersionId

Name

NamespacePrefix

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the most recent version of this survey.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the survey that appears in the UI. This field is read-only from API
version 50.0.

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
Filter, Group, Sort

**Description**
The ID of the user who created the survey.


### Standard Objects SurveyEmailBranding

**Field Name** **Details**

```
SurveyType

TotalVersionsCount

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of the survey. The default value is Survey.

Possible values are:

**•** `ASSESSMENT`  - Survey type for sales enablement teams. Available from
API version 58.0 and later.

**•** `BASIC`  - Survey with a question page with like or dislike, long text, multiple
selection, NPS, rating, short text, and single selection questions, and without
inserted participant responses, display logic, and page branching logic.

**•** `SURVEY`  - Survey with all the available features.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of versions of the survey.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyChangeEvent on page 68**
Change events are available for the object.

**SurveyFeed (API version 42.0)**
Feed tracking is available for the object.

**SurveyOwnerSharingRule**

Sharing rules are available for the object.

**SurveyShare**

Sharing is available for the object.

### SurveyEmailBranding

Represents the configuration settings for invitation emails sent to survey participants for a particular survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects SurveyEmailBranding

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Note: You can’t define custom fields for the SurveyEmailBranding object using the Object Manager.

Fields

**Field Name** **Details**

```
Body

DeveloperName

FooterImageId

FromEmailAddress

HeaderImageId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The body text of the invitation email.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique API name of the email branding configuration.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the footer of the invitation email.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address that appears in the “From” field when the invitation is sent to
participants.

**Type**
reference


Standard Objects SurveyEmailBranding

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the header of the invitation email.

```
Language

MasterLabel

Subject

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the emails. Available languages include:

**•** Chinese (Simplified)

**•** Chinese (Traditional)

**•** Danish

**•** Dutch

**•** English

**•** Finnish

**•** French

**•** German

**•** Italian

**•** Japanese

**•** Korean

**•** Norwegian

**•** Portuguese (Brazilian)

**•** Russian

**•** Spanish

**•** Spanish (Mexican)

**•** Swedish

**•** Thai

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for these email configuration settings.

**Type**
string


### Standard Objects SurveyEngagementContext

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The subject of the invitation email.

### SurveyEngagementContext

Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API
version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Note: You can’t define custom fields for the SurveyEngagementContext object using the Object Manager.

Fields

**Field** **Details**

```
ContextType

ContextValue

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context type based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects SurveyInvitation

**Field** **Details**

**Description**
Name of the record.

```
OwnerId

### `SurveyInvitationId`

SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the record's owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey response.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyEngagementContextShare**

Sharing is available for the object.

### SurveyInvitation

Represents the invitation sent to a participant to complete the survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SurveyInvitation

Fields

**Field Name** **Details**

```
CommunityId

ContactId

EmailBrandingId

InvitationLink

InviteExpiryDateTime

IsDefault

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that you want to send the survey to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact who received the invitation. This field is available in API v49.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the survey email branding object that’s associated with this invitation.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL to the survey that is sent to participants. To query on this field, you need
access to the associated Survey record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the survey invitation expires.

**Type**
boolean


Standard Objects SurveyInvitation

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether this is the default survey invitation to use when the survey
is sent to participants.

```
LastReferencedDate

LastViewedDate

LeadId

Name

OptionsAllowGuestUserResponse

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
survey invitation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead who received the invitation. This field is available in API v49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the survey invitation that appears in the UI.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects SurveyInvitation

**Field Name** **Details**

**Description**
Determines whether participants who don’t have a Salesforce account can
complete the survey.

```
OptionsAllowParticipantAccessTheirResponse

OptionsCollectAnonymousResponse

OwnerId

ParticipantId

ResponseStatus

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can access a copy of their responses after they
complete the survey.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can complete the survey anonymously.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the participant if the participant is a Salesforce contact, user, or lead.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a participant’s response to the survey that’s associated with the
survey invitation. Possible values include:

**•** `NotStarted`  - For an invitation with a `ParticipantID`, it means
that the recipient hasn’t opened the survey. For an invitation without the


Standard Objects SurveyInvitation

**Field Name** **Details**

`ParticipantID`, it means that none of the recipients have opened the
survey.

**•** `Started`                       - For an invitation with a `ParticipantID`, it means that
the recipient opened the survey. For an invitation without the
`ParticipantID`, it means that the survey has been opened by at least
one recipient.

**•** `Paused`                       - For an invitation with a `ParticipantID`, it means that the
recipient has paused the survey. For an invitation without the
`ParticipantID`, it means that the survey has been paused by any one
of the recipients. Paused isn't available for invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.

**•** `PartiallyCompleted`                       - For an invitation with a `ParticipantID`
field, it means that the recipient has partially completed the survey. For an
invitation without the `ParticipantID` field, it means that at least one
recipient has partially completed the survey. Available in API version 63.0
and later.

**•** `Completed`                       - For an invitation with a `ParticipantID`, it means that
the recipient has submitted the survey. For an invitation without the
`ParticipantID`, it means that the invitation has been submitted by at
least one recipient.

```
SurveyId

UUID

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the survey that’s sent in the invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique user ID that's added to a survey invitation generated for a contact,
lead,or user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SurveyPage

**Field Name** **Details**

**Description**
ID of the user who received the invitation. This field is available in API v49.0 and
later.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyInvitationChangeEvent (API version 62.0)**
Change events are available for the object.

**SurveyInvitationOwnerSharingRule**

Sharing rules are available for the object.

**SurveyInvitationShare**

Sharing is available for the object.

### SurveyPage

Represents a page, such as the title page or a question page, in a survey.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyPage object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of this SurveyPage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the survey page that appears in the UI.


### Standard Objects SurveyQuestion

**Field** **Details**

```
SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The version of the survey that the page belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyPageChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestion

Represents a question in a survey.

Supported Calls

`describeLayout()describeSObjects()getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestion object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

IsDeprecated

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the SurveyQuestion. The API name must be unique within a particular
version of the survey.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects SurveyQuestion

**Field** **Details**

**Description**
Indicates whether the question was deleted from the survey.

```
Name

PageDisplayOrder

PageName

QuestionChoiceCount

QuestionName

QuestionOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the page is displayed. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the page. This field is available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of choices for the question. This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
The label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SurveyQuestion

**Field** **Details**

**Description**
The order in which the question is displayed.

The label for the page. This field is available in API version 52.0 and later.

```
QuestionType

RelatedQuestionId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of question. Possible values include:

**•** `Boolean` —This value is available in API v49.0 and later.

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `FreeText`

**•** `Image`

**•** `Matrix` —This value is available in API v55.0 and later.

**•** `MultipleChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `RadioButton`

**•** `StackRank`

**•** `Rating`

**•** `ShortText` —This value is available in API v49.0 and later.

**•** `Slider`

**•** `Toggle`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent question. This field is blank when the question itself is the parent question.
This field is available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.


Standard Objects SurveyQuestion

**Field** **Details**

```
SubQuestionDisplayOrder

 SurveyPageId

 SurveyVersionId

ValidationType

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed within the parent question. This field is available
in API v55.0 and later, with Feedback Management - Starter and Feedback Management Growth licenses.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Lookup to the SurveyPage that contains the question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the question belongs to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The validations available for the short-text question. Possible values include:

**•** Custom - Cu

**•** Number - Nu

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChangeEvent on page 68**
Change events are available for the object.


### Standard Objects SurveyQuestionChoice SurveyQuestionChoice

Represents an answer choice that a participant can select for a survey question.

Supported Calls

`describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionChoice object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

DisplayOrder

IsDeprecated

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of the SurveyQuestionChoice object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question choice is displayed within the parent question. This field is
available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a question choice was deleted from the survey.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A label for the question choice that appears in the UI.


### Standard Objects SurveyQuestionResponse

**Field** **Details**

```
QuestionId

SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyQuestion object that this choice belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the survey that this question choice belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChoiceChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionResponse

Represents a participant’s answer to a specific question.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionResponse object using the Object Manager.

Fields

**Field** **Details**

```
ChoiceValue

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for the following question types:


Standard Objects SurveyQuestionResponse

**Field** **Details**

**•** Multiple choice

**•** Picklist

**•** Radio

**•** Ranking

```
Datatype

DateTimeValue

DateValue

InvitationId

IsTrueOrFalse

```

**Type**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type of the question response. Possible values are:

**•** `Boolean` This value is available in API v49.0 and later.

**•** `Date`

**•** `Double`

**•** `Int`

**•** `Number`

**•** `String`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date time.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyInvitation that was sent to the survey participant.

**Type**
boolean


Standard Objects SurveyQuestionResponse

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Response provided by a participant for a question type which has only two possible values:
True and False.

```
NumberValue

QuestionChoiceId

QuestionId

Rank

ResponseId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Net Promoter Score (NPS)

**•** Rating

**•** Score

**•** Slider

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of SurveyQuestionChoice that a participant chose in response to a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyQuestion that a participant provided an answer for.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank provided by a participant for an answer choice for the ranking question type.

**Type**
reference


### Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyResponse that is the parent of this SurveyQuestionResponse.

```
 ResponseShortText

 ResponseValue

 SurveyVersionId

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the response provided by a participant for a text type question.

**Type**
textarea

**Properties**
Nillable

**Description**
Response provided by a participant for a question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the response belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionResponseChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionScore

Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring,
[slider, and Net Promoter Score](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/product-specific-terms/net-promoter-and-nps.pdf) [®] (NPS [®] ).

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`


Standard Objects SurveyQuestionScore

Note: You can’t define custom fields for the SurveyQuestionScore object using the Object Manager.

Fields

**Field** **Details**

```
CumulativeScore

DateResponse

Name

QuestionChoiceId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the responses provided by all the participants for a question of the following types:
rating, scoring, and slider. For a question of the type ranking, sum of the weights provided
by all the participants for each item.

Note: This field is only applicable for the overall score type.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date selected by one or more participants for a question of the type date.

Note: This field is only applicable for the individual score type.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
For an overall score type record:

**•** Name of a question.

**•** Name of an item in a question of the type ranking.

For an individual score type record:

**•** Name of an item in a question of the type ranking.

**•** Name of a question of the type date.

**•** Response provided by one or more participants for questions of the following types:
picklist, multiple choice, rating, ranking, score, slider, NPS.

**Type**
reference


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the answer choice selected by one or more participants. For an individual
score type record, this field is applicable for questions of the following types: picklist, radio,
multi choice, ranking and rating. For an overall score type record, this field is applicable for
questions of the type ranking.

```
QuestionDeveloperName

QuestionId

QuestionName

QuestionSkippedCount

ResponseCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the question for which response is recorded. The API name must be unique
within a particular version of the survey.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the question for which response is recorded.

**Type**
textarea

**Properties**
Nillable

**Description**
Name of the question for which response is recorded.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of participants who didn’t respond to the question.

Note: This field is only applicable for the overall score type.

**Type**
int


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
For an overall score type record, number of participants who responded to the question. For
an individual score type record, number of participants who selected a particular answer
choice.

```
ResponseValue

Score

ScoreType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Answer choice selected by one or more participants for a question of the following types:
rating, slider, score, NPS. Rank provided by the participant for an item in a question of the
type ranking.

Note: This field is only applicable for the individual score type.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For an individual score type record, percentage of participants who selected a particular
answer choice.

Note: For questions of the type ranking, the percentage of participants who have
provided the same rank to an item.

For overall score type record:

**•** Average score of questions of the following question types: rating, scoring, and slider.

**•** Score of an NPS type question.

**•** Average weight provided by all participants for each item in question of the type ranking.

**•** Number of participants who responded to the question for the following question types:
date, radio, multi choice, and picklist.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the score calculated for a record. Possible values are:

**•** `Individual`


### Standard Objects SurveyResponse

**Field** **Details**

**•** `Overall`

```
 SurveyId

 SurveyInvitationId

 SurveyVersionId

### SurveyResponse

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey that contains the question for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey version for which scores are calculated.

Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and
when the survey was completed.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```

Note: You can’t define custom fields for the SurveyResponse object using the Object Manager.

Fields

**Field Name** **Details**

```
CompletionDateTime

```

**Type**
dateTime


Standard Objects SurveyResponse

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the participant completed the survey.

```
DataMapperExecutionStatus

InterviewGuid

InterviewId

InvitationId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of all the survey data maps after a response is received. This field is available
in API v49.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

Possible values are:

**•** `Pending`

**•** `InProgress`

**•** `Success`

**•** `Error`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable

**Description**
An automatically-generated, unique ID for a saved survey response.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FlowInterview object that’s associated with this response.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyInvitation object that’s associated with this response.


Standard Objects SurveyResponse

**Field Name** **Details**

```
IpAddress

Language

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the device the participant used to take the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language that the participant used to complete the survey.

Possible values are:

**•** `af` —Afrikaans

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

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `da` —Danish

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `en_AU` —English (Australian)

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

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


Standard Objects SurveyResponse

**Field Name** **Details**

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

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

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


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

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

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that another Salesforce object last referenced this
SurveyResponse object.


Standard Objects SurveyResponse

**Field Name** **Details**

```
LastViewedDate

Latitude

Location

Longitude

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that someone last viewed this SurveyResponse object.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude of the participant’s location.

**Type**
location

**Properties**
Nillable

**Description**
The latitude and longitude coordinates of the participant’s location.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude of the participant’s location.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the participant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:


Standard Objects SurveyResponse

**Field Name** **Details**

**•** NotStarted — The participant hasn't opened the survey.

**•** Started — The participant has opened the survey.

**•** Paused — The participant has paused the survey. Paused isn't available for
invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.

**•** PartiallyCompleted — The participant has partially completed the survey.
Available in API version 63.0 and later.

**•** Completed — The participant has completed the survey.

```
SubmitterId

SurveyId

SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user, contact, or lead who completed the survey.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey that the participant completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the version of the survey that the participant completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects SurveySubject

**SurveyResponseChangeEvent on page 68**
Change events are available for the object.

### SurveySubject

Represents a relationship between a survey and another object, such as an account or a case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

ParentId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the SurveySubject record was last referenced by another
object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the SurveySubject record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the SurveySubject record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects SurveySubject

**Field Name** **Details**

**Description**
Unique identifier of the SurveyInvitation object or SurveyResponse object that is
associated with this survey-object relationship.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
SurveyInvitation, SurveyResponse

```
SubjectEntityType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object that the survey is associated with. Possible values include:

**•** _`Account`_

**•** _`Asset`_

**•** _`Banker`_

**•** _`BranchUnit`_

**•** _`BranchUnitBusinessMember`_

**•** _`BranchUnitCustomer`_

**•** _`BusinessLicenseApplication`_

**•** _`BusinessMilestone`_

**•** _`Campaign`_

**•** _`CareProgram`_

**•** _`Case`_

**•** _`Claim`_

**•** _`ClaimParticipant`_

**•** _`Contact`_

**•** _`Employee`_

**•** _`Event`_

**•** _`Incident`_

**•** _`IndividualApplication`_

**•** _`InsurancePolicy`_

**•** _`InsurancePolicyParticipant`_

**•** _`Lead`_

**•** _`LearningItemSubmission`_ —Available in API version 58.0 and later.

**•** _`LiveChatTranscript`_


Standard Objects SurveySubject

**Field Name** **Details**

**•** _`LoyaltyProgram`_

**•** _`LoyaltyProgramMember`_

**•** _`LoyaltyProgramPartner`_

**•** _`MaterialityStakeholder`_

**•** _`MessagingSession`_

**•** _`Opportunity`_

**•** _`Order`_

**•** _`PersonalLifeEvent`_

**•** _`Producer`_

**•** _`Product2`_

**•** _`Promotion`_

**•** _`RebateProgram`_

**•** _`RetailStore`_

**•** _`ServiceAppointment`_

**•** _`ServiceResource`_

**•** _`Solution`_

**•** _`Task`_

**•** _`TransactionJournal`_

**•** _`User`_

**•** _`VideoCall`_

**•** _`Visit`_

**•** _`VoiceCall`_

**•** _`VolunteerProject`_

**•** _`WorkOrder`_

**•** Custom Objects

```
SubjectId

SurveyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the object that’s associated with the survey.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects SurveyVersion

**Field Name** **Details**

**Description**
Unique identifier of the survey that’s associated with the record that’s represented
by `SubjectId` .

```
SurveyInvitationId

SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation that's associated with another object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey response that's associated with another object.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveySubjectChangeEvent (API version 62.0)**
Change events are available for the object.

### SurveyVersion

Represents a version of a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the SurveyVersion object using the Object Manager.

Fields

**Field Name** **Details**

```
BrandingSetId

```

**Type**
reference


Standard Objects SurveyVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the branding set associated with the survey version.

```
Description

IsTemplate

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of this survey version.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the survey version is a template. Template surveys are
automatically shared with all users in your Salesforce org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey
version.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey version.

**Type**
string

**Properties**
Filter, Group, Sort

Filter, Group, Sort

Filter, Group, idLookup, Sort


### Standard Objects SurveyVersionAddlInfo

**Field Name** **Details**

**Description**
The name of the survey that appears in the UI.

```
SurveyId

SurveyStatus

VersionNumber

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey associated with the survey version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The version number of the survey.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyVersionChangeEvent on page 68**
Change events are available for the object.

### SurveyVersionAddlInfo

Represents additional information about a survey version. This information defines the default settings of a survey version. This object
is available in API version 49.0 and later.


Standard Objects SurveyVersionAddlInfo

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
EmailSender

EmailTemplateId

EngagementContextMetadata

InvitationSharingRole

Language

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The organization-wide email address used to send a survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email template that's used to send an automated survey invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom metadata created to get the engagement context from the participants.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the users that share edit access to a survey invitation.

Possible values are:

**•** `InvitationRecordCreator`  - Owner of the record that's associated with a
survey invitation.

**•** `SurveyOwner`

**Type**
picklist


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Language used to create the survey.

Possible values are:

**•** `af` —Afrikaans

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

**•** `en_AU` —English (Australian)


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

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


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

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

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

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

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
Name

SurveyQuestionId

SurveyVersionId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the survey question embedded in the email template used to send automated survey
invitations.

**Type**
reference


### Standard Objects SvcCatalogCategory

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the survey version. This field is unique within your organization

### SvcCatalogCategory

Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
DeveloperName

ImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique developer name for the catalog item category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Allows a builder to pick an image displayed in the catalog.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup


Standard Objects SvcCatalogCategory

**Field** **Details**

**Refers To**
ContentAsset

```
IsActive

Language

ParentCategoryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows service catalog builders to deprecate categories or create in-draft categories.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
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
reference


### Standard Objects SvcCatalogCategoryItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Parent category of this category. Allows categories to be grouped up to a max depth of 3.

This field is a relationship field.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
### SvcCatalogCategory

```
SortOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the order that the category is displayed to the end user.

### SvcCatalogCategoryItem

Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This
object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
IsPrimaryCategory

```

**Type**
boolean


Standard Objects SvcCatalogCategoryItem

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the category is the primary category for a catalog item.

The default value is `false` .

```
SortOrder

SvcCatalogCategoryId

SvcCatalogItemDefId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the order in which catalog items appear by default when you're viewing all items
in a single category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the category for which the service category item belongs.

This field is a relationship field.

**Relationship Name**
SvcCatalogCategory

**Relationship Type**
Lookup

**Refers To**
SvcCatalogCategory

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service category item definition.

This field is a relationship field.

**Relationship Name**
SvcCatalogItemDef

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef


### Standard Objects SvcCatalogFilterCriteria SvcCatalogFilterCriteria

Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API version
60.0 and later.

Supported SOAP API Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Supported REST API Methods

```
   DELETE, GET, HEAD, PATCH, POST, Query

```

Special Access Rules

To access this object, get the Service Catalog Access permission set license.

Fields

**Field** **Details**

```
CriteriaRelation

Description

DeveloperName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Possible values are:

**•** `AllConditionsAreMet`

**•** `AnyConditionIsMet`

**Type**
textarea

**Properties**
Nillable

**Description**
A description that states the restriction placed on a user’s access to a catalog items eligibility.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:


Standard Objects SvcCatalogFilterCriteria

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

```
FullName

IsActive

Language

```

**Type**
string

**Properties**
Create, Group, Nillable

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies if the eligibility rule is active.

The default value is `false` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Supported languages for eligibility rules

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


Standard Objects SvcCatalogFilterCriteria

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
ManageableState

MasterLabel

Metadata

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the manageable state of a catalog item that is contained in a package.

Possible values are:

**•** `beta` —Managed-Beta

**•** `deleted` —Managed-Proposed-Deleted

**•** `deprecated` —Managed-Proposed-Deprecated

**•** `deprecatedEditable` —SecondGen-Installed-Deprecated

**•** `installed` —Managed-Installed

**•** `installedEditable` —SecondGen-Installed-Editable

**•** `released` —Managed-Released

**•** `unmanaged` —Unmanaged

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the eligibility rule record.

**Type**
complexvalue

**Properties**
Create, Nillable, Update

**Description**
The metadata type associated with the SvcCatalogFilterCriteria object.


### Standard Objects SvcCatalogItemDef

**Field** **Details**

```
NamespacePrefix

NumOfRelatedItems

### SvcCatalogItemDef

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of catalog items that has the eligibility rule.

Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The definition of the catalog item. This field is visible on the Service Catalog page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Description**
The unique developer name for the catalog item.

```
FlowName

FulfillmentFlowId

ImageId

ImageReference

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow called when the user navigates to the request page for the catalog item. Available
in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the fulfillment flow. Available in API version 56.0 and later.

This field is a relationship field.

**Relationship Name**
FulfillmentFlow

**Relationship Type**
Lookup

**Refers To**
SvcCatalogFulfillmentFlow

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The image ID used for the catalog item.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
string


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Derived field from `ImageId` to expose `ContentAssetId` on item definitions. Available
in API version 61.0 and later.

```
InternalNotes

IsActive

IsAvailableToAllCustomers

IsFeatured

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A place for the Service Catalog Builder to leave internal notes about the catalog item.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived field from `Status` to indicate whether the service catalog item is active.

The default value is `false` .

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Udpate

**Description**
Indicates whether the Service Catalog item is available to all customers. The default value is
`false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a catalog item is marked as a favorite for the org. Favorites display as a
featured item on the Service Catalog home page.

The default value is `false` .


Standard Objects SvcCatalogItemDef

**Field** **Details**

```
IsGuestAccessible

IsOutOfSync

Language

Product

ShortDescription

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Service Catalog item can be accessed by guest users. The default value
is `false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fulfillment flow that the Service Catalog item is based on has been
updated. Available in API version 58.0 and later.

The default value is `false` . If value is `true`, try updating and saving the service catalog
item again.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Supported languages for catalog items.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The product associated with the Service Catalog item. The value is derived from `UsageType` .
Available in API version 59.0 and later.

Possible values are:

**•** `FinancialServices`

**•** `ServiceCatalog` —Default

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
The short description of the catalog item.

```
Status

UsageType

### SvcCatalogRequest

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows the Service Catalog Builder to control whether the flow is displayed to users within
the Service Catalog.

Possible values are:

**•** `Deprecated`

**•** `Draft` —Default

**•** `PendingChanges`

**•** `Published`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business type for which the Service Catalog is used. Available in API version 57.0 and
later.

Possible values are:

**•** `CustomerService`

**•** `Employee` —Default

**•** `FinancialServices`

**•** `Industry`

Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects SvcCatalogRequest

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
CatalogItemDescription

CatalogItemName

CatalogItemVersion

ClosedDate

CurrencyIsoCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description for the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Version for the catalog item.

This is a calculated field. Available in API version 58.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was closed. This field is automatically populated when
`IsClosed` is 'true'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
ISO code of the currency. Must be one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as USD, GBP, or JPY. Must be unique within your
organization. Default value is `USD` -U.S. Dollar.

```
FlowInterviewGuid

IsClosed

ItemFlowVersion

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique GUID associated with the automation that was executed as part of the catalog item.
Available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the request has been resolved. This field is automatically checked when
`ClosedDate` is populated.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Version for the item flow.

This is a calculated field.

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


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
Name

OwnerId

Status

SubmitterId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Service Catalog request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID for the owner record.

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
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service catalog request. Available in API version 60.0 and later.

Possible values are:

**•** `CompletedExecution` —Default

**•** `CreatedRequest`

**•** `StartedExecution`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
ID for the submitter record.

This is a relationship field.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
User

```
SvcCatalogItemDefinitionId

TargetCustomerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The catalog item that was used to create this request.

This is a relationship field.

**Relationship Name**
SvcCatalogItemDefinition

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer ID that the request was submitted for. For example, when an agent runs a
catalog item for a given contact, the contact is represented by the `TargetCustomerId` .
Available in API version 61.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
TargetCustomer

**Relationship Type**
Lookup

**Refers To**
Contact, User


### Standard Objects SvcCatalogReqRelatedItem SvcCatalogReqRelatedItem

Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Name

RelatedExternalId

RelatedInternalRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the related item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text containing an ID from any external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce record related to this request. This reference must be for an object that has
the following characteristics.

**•** It's a standard object.

**•** It must allow custom fields.

**•** It's referencable (that is, it can be the target of a lookup).

**•** It can be the target of a custom lookup field.


### Standard Objects Swarm

**Field** **Details**

**•** It contains a Name field.

**•** It isn't dependent on a junction object.

**•** It isn't a virtual object or a setup object.

This is a polymorphic relationship field.

**Relationship Name**
RelatedInternalRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssociatedLocation, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, BusinessBrand, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, Contract, ContractLineItem, Customer, DataUseLegalBasis,
DataUsePurpose, Employee, EngagementChannelType, Entitlement, Idea, Individual,
InternalOrganizationUnit, Lead, Location, MessagingEndUser, Opportunity, Order, OrderItem,
PartyConsent, Pricebook2, ProcessException, Product2, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, QuickText, Recommendation, Seller, ServiceContract, SocialPersona, SocialPost,
Solution, SurveyInvitation, SurveySubject, UserProvisioningRequest, VoiceCall

```
SvcCatalogRequestId

### Swarm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The SvcCatalogRequest record.

This is a relationship field.

**Relationship Name**
SvcCatalogRequest

**Relationship Type**
Lookup

**Refers To**
SvcCatalogRequest

Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem
can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.


Standard Objects Swarm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
CollaborationRoomId

CollaborationTool

CollaborationUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the collaboration room.

This field is a relationship field.

**Relationship Name**
CollaborationRoom

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tool used for swarming.

Possible values are:

**•** `None`

**•** `Slack`

The default value is `None` .

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Swarm

**Field** **Details**

**Description**
URL of the Slack channel or thread.

```
EndedDateTime

HelpNeeded

IsDedicatedChannel

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm ended.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the swarm is happening in a dedicated channel ( `true` ) or in an existing channel
( `false` ).

The default value is `false` .

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


Standard Objects Swarm

**Field** **Details**

```
MessageKey

Name

OwnerId

RelatedRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Slack thread or message.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the swarm owner.

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
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup


Standard Objects Swarm

**Field** **Details**

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

```
StartedDateTime

Status

UsageType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm started.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

**•** `Waiting (Custom)`

The default value is `New` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of swarm.

Possible values are:

**•** `CareMgmt` —Care Coordination

**•** `DealRoom` —Sales Channel

**•** `PartnerChannel` —Partner Account Channel

**•** `Swarming`

The default value is `Swarming` .


### Standard Objects SwarmMember

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmFeed on page 55**
Feed tracking is available for the object.

**SwarmHistory on page 63**
History is available for tracked fields of the object.

**SwarmOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmShare on page 67**
Sharing is available for the object.

### SwarmMember

Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
AssignedDateTime

CompletedDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member is added to the swarm.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member exits the swarm or the swarm closes.


Standard Objects SwarmMember

**Field** **Details**

```
HelpNeeded

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
Short description of the problem that the swarm is trying to solve.

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
Name of the swarm or record number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce user assigned to a swarm.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


Standard Objects SwarmMember

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RelatedRecordId

Status

SwarmId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm member or swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

The default value is `New` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the swarm the member belongs to.

This field is a relationship field.


### Standard Objects TabDefinition

**Field** **Details**

**Relationship Name**
Swarm

**Relationship Type**
Lookup

**Refers To**
Swarm

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmMemberFeed on page 55**
Feed tracking is available for the object.

**SwarmMemberHistory on page 63**
History is available for tracked fields of the object.

**SwarmMemberOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmMemberShare on page 67**
Sharing is available for the object.

### TabDefinition

Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Unique identifier for the tab. Always retrieve this value before using it, because
the value isn’t guaranteed to stay the same from one release to the next. Simplify
queries by using this field instead of making multiple queries.


Standard Objects TabDefinition

**Field Name** **Details**

```
IsAvailableInAloha

IsAvailableInDesktop

IsAvailableInLightning

IsAvailableInMobile

IsCustom

Label

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available on desktop.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Lightning Experience.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in the Salesforce mobile app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is a custom tab created by admins in the org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects TagDefinition

**Field Name** **Details**

**Description**

The localized label corresponding to the `MasterLabel` field in the Tooling
API object.

```
MobileUrl

Name

SobjectName

Url

### TagDefinition

```

Defines the attributes of child Tag objects.

Supported Calls

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab in the Salesforce mobile app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The developer name of the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of the sObject corresponding to the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab on desktop.

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`


Standard Objects TagDefinition

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Detail**

```
Name

Type

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
Identifies the tag word or phrase.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Defines the visibility of a tag. Possible value are:

**•** **Public** : The tag can be viewed and manipulated between all users in an organization.

**•** **Personal** : The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

When you create a tag for a record, an association is created with to a corresponding TagDefinition:

**•** If the value in the tag's `Name` field is new, a new TagDefinition record is automatically created and becomes the parent of the tag.

**•** If the value in the tag's `Name` field already exists in a TagDefinition, that TagDefinition automatically becomes the parent of the tag.

Each TagDefinition record has a one-to-many relationship with its child tag records.

The following standard objects represent tags for records:

**•** AccountTag

**•** AssetTag

**•** CampaignTag

**•** CaseTag

**•** ContactTag

**•** ContractTag

**•** DocumentTag

**•** EventTag

**•** LeadTag


### Standard Objects Task

**•** NoteTag

**•** OpportunityTag

**•** SolutionTag

### • TaskTag

Custom objects may also be tagged. Tags for custom objects are identified by a suffix of two underscores immediately followed by the
word `tag` . For example, a custom object named `Meeting` has a corresponding tag named Meeting__tag in that organization’s
WSDL. Meeting__tag is only valid for `Meeting` objects.

TagDefinition is useful for mass operations on any tag record. For instance, if you want to rename existing tags, you can search for the
appropriate TagDefinition object, update it, and the child tag's `Name` values are also changed. The following Java example replaces all
`WC` tags with the phrase `West Coast` :

```
   public void tagDefinitionSample() {

     String soqlQuery = "SELECT Id, Name FROM TagDefinition " +

       "WHERE Name = 'WC'";

     QueryResult qResult = null;

     try {

       qResult = connection.query(soqlQuery);

      TagDefinition tagDef = (TagDefinition) qResult.getRecords()[0];

      tagDef.setName("West Coast");

      connection.update(new SObject[]{tagDef});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### Task

Represents a business activity such as making a phone call or other to-do items. In the user interface, Task and Event records are collectively
referred to as activities.

Note: Task fields related to calls are exclusive to Salesforce CRM Call Center. Also, `query()`, `delete()`, and `update()`
aren't allowed with tasks related to more than one contact in API versions 23.0 and earlier.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Field Type**

```
AccountId

```

**Type**
reference


Standard Objects Task

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the related Account. The `AccountId` is determined as follows.

If the value of `WhatId` is any of these objects, Salesforce uses that object's `AccountId` .

**•** Account

**•** Opportunity

**•** Contract

**•** Custom object that is a child of Account

If the value of the `WhatId` field is any other object, and the value of the `WhoId` field is a
Contact object, then Salesforce uses that contact’s `AccountId` . (If your organization uses
Shared Activities, then Salesforce uses the `AccountId` of the primary contact.)

Otherwise, Salesforce sets the value of the `AccountId` field to `null` .

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

CallDisposition

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the due date of the task. This field has a timestamp that is always set to midnight
in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant; do not
attempt to alter it to accommodate time zone differences. Label is **Due Date** .

This field can’t be set or updated for a recurring task ( `IsRecurrence` is `true` ).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.


Standard Objects Task

**Field** **Field Type**

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

```
CallDurationInSeconds

CallObject

CallType

CompletedDateTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Duration of the call in seconds.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of a call center. Limit is 255 characters.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The type of call being answered. Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

When working with PushTopic, the `CallType` values display as `1` for `Inbound`, `0` for
`Internal`, and `2` for `Outbound` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.


Standard Objects Task

**Field** **Field Type**

**•** For insert, if the task is saved with a Closed status the field is set. If the task is saved with
an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is no change
to the field.

The status is a dynamic enum. If the Closed mapping is changed it won’t cause an update
of existing tasks. Only new insert/update operations are affected.

```
ConnectionReceivedId

ConnectionSentId

Description

IsArchived

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
if Salesforce to Salesforce is enabled. This field is supported in API versions 14.0 and earlier.
In API version 15.0 and later, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains a text description of the task. The text provided in the Description field shows in
the Comments field on the task record detail page.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event has been archived. The default value of this field is `false` .


Standard Objects Task

**Field** **Field Type**

```
IsClosed

IsHighPriority

IsRecurrence

IsReminderSet

IsVisibleInSelfService

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task has been completed ( `true` ) or not ( `false` ). The default value
of this field is `false` . Is only set indirectly via the `Status` picklist. Label is **Closed** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. This field is derived from the `Priority` field. The default
value of this field is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task is scheduled to repeat itself ( `true` ) or only occurs once ( `false` ).
The default value of this field is `false` . This field is read-only on update, but not on create.
If this field value is `true`, then `RecurrenceStartDateOnly`,
`RecurrenceEndDateOnly`, `RecurrenceType`, and any recurrence fields associated
with the given recurrence type must be populated. See Usage section.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a popup reminder has been set for the task ( `true` ) or not ( `false` ). The
default value of this field is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a task associated with an object can be viewed in the Customer Portal
( `true` ) or not ( `false` ).


Standard Objects Task

**Field** **Field Type**

If your organization has digital experiences enabled, tasks marked
`IsVisibleInSelfService` are visible to any external user in the Experience Cloud
site, as long as the user has access to the record the task was created on.

```
OwnerId

Priority

RecurrenceActivityId

RecurrenceDayOfMonth

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group who owns the record. Label is **Assigned To ID** . This field accepts
Groups of type Queue only.

In the user interface, Group IDs correspond with the queue’s list view names. To create or
update tasks assigned to Group, use v48.0 or later.

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
Required. Indicates the importance or urgency of a task, such as high or low. The default
value of this field is `Normal` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Not required on create. ID of the main record of the recurring task. Subsequent
occurrences have the same value in this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Task

**Field** **Field Type**

**Description**
The day of the month in which the task repeats.

```
RecurrenceDayOfWeekMask

RecurrenceEndDateOnly

RecurrenceInstance

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the task repeats. This field contains a bitmask. The
values are as follows:

**•** `Sunday = 1`

**•** `Monday = 2`

**•** `Tuesday = 4`

**•** `Wednesday = 8`

**•** `Thursday = 16`

**•** `Friday = 32`

**•** `Saturday = 64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the task repeats. This field has a timestamp that is always set to
midnight in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant;
do not attempt to alter it to accommodate time zone differences.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring task.

Possible values are:

**•** `First` —1st

**•** `Fourth` —4th

**•** `Last` —last

**•** `Second` —2nd


Standard Objects Task

**Field** **Field Type**

**•** `Third` —3rd

```
RecurrenceInterval

RecurrenceMonthOfYear

RecurrenceRegeneratedType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring tasks.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year in which the task repeats.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents what triggers a repeating task to repeat. Add this field to a page layout together
with the `RecurrenceInterval` field, which determines the number of days between
the triggering date (due date or close date) and the due date of the next repeating task in
the series.

Label is **Repeat This Task** . This field has the following picklist values:

**•** **None** : The task doesn’t repeat.

**•** **After due date** : The next repeating task will be due the specified number of days after
the current task’s due date.

**•** **After the task is closed** : The next repeating task will be due the specified number of
days after the current task is closed.

**•** **(Task closed)** : This task, now closed, was opened as part of a repeating series.

When tasks in a series are set to repeat after their due date, Salesforce doesn’t create
recurrences that would have been due in the past. Instead, Salesforce keeps adding the
interval until a repeated task has a due date in the future.

For example, suppose that someone sets a task to repeat three days after it’s due. But, that
person doesn’t complete the task (mark it Closed) until five days after it’s due. Instead of
creating a task that’s already overdue, Salesforce gives the new task a due date of tomorrow.
This due date is equivalent to 6 days after the due date; two intervals of three days each.

If that person completes the repeating task (marks it Closed) before the due date, the next
task is still due three days after the due date.


Standard Objects Task

**Field** **Field Type**

```
RecurrenceStartDateOnly

RecurrenceTimeZoneSidKey

RecurrenceType

ReminderDateTime

Status

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the recurring task begins. Must be a date and time before
`RecurrenceEndDateOnly` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone associated with the recurring task. For example, “UTC-8:00” for Pacific Standard
Time.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the task repeats. For example, daily, weekly, or every nth month (where
“nth” is defined in `RecurrenceInstance` ).

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates the status of the task. The default value of this field is `Not Started` .
Each predefined `Status` field implies a value for the `IsClosed` flag. To obtain picklist
values, query the TaskStatus object.


Standard Objects Task

**Field** **Field Type**

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

This field can’t be updated for recurring tasks ( `IsRecurrence` is `true` ).

```
Subject

TaskSubtype

TaskWhoIds

```

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the task, such as “Call” or “Send Quote.” Limit: 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific task subtypes.
This field can't be updated.

`TaskSubtype` values:

**•** `Task`

**•** `Email`

**•** `LinkedIn` —Available in API version 56.0 and later.

**•** `ListEmail`

**•** `Cadence`

**•** `Call`

The `Cadence` subtype is an internal value used by Sales Engagement, and can’t be set
manually.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs related to this task. This `JunctionIdList` field is
linked to the `TaskWhoRelations` child relationship. `TaskWhoIds` is only available
when the shared activities setting is enabled. The first contact or lead ID in the list becomes


Standard Objects Task

**Field** **Field Type**

the primary `WhoId` if you don’t specify a primary `WhoId` . If you set the `EventWhoIds`
field to null, all entries in the list are deleted and the value of `WhoId` is added as the first
entry.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

```
Type

WhatCount

WhatId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of task, such as Call or Meeting.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Count of related TaskRelations
pertaining to `WhatId` . Count of the `WhatId` must be _`1`_ or less.

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


Standard Objects Task

**Field** **Field Type**

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
WhoCount

WhoId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Count of related TaskRelations
pertaining to `WhoId` .

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

Beginning in API version 37.0, if the contact or lead ID in the `WhoId` field is not in the
`TaskWhoIds` list, no error occurs and the ID is added to the `TaskWhoIds` as the primary
`WhoId` . If `WhoId` is set to null, an arbitrary ID from the existing `TaskWhoIds` list is
promoted to the primary position.

This is a polymorphic relationship field.


Standard Objects Task

**Field** **Field Type**

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

**Recurring Tasks**

**•** Recurring tasks are available in API version 16.0 and later.

**•** After a task is created, it can’t be changed from recurring to nonrecurring or vice versa.

**•** When a user creates a series of recurring tasks, Salesforce creates a main record and subsequent occurrences. For the main record,
`IsRecurrence` is set to `true` and other fields that define the recurrence pattern are populated. The ID of the main record of
the recurring task is saved in the subsequent occurrences, in the `RecurrenceActivityId` field.

**•** When you delete a recurring task series through the API, all open and closed task occurrences in the series are removed. However,
when you delete a recurring task series through the user interface, only open tasks occurrences ( `IsClosed` is `false` ) in the
series are removed.

**•** If `IsRecurrence` is `true`, then `RecurrenceStartDateOnly`, `RecurrenceEndDateOnly`, `RecurrenceType`,
and any properties associated with the given recurrence type (see the following table) must be populated.

**•** When you change the `RecurrenceStartDateOnly` field or the recurrence pattern, all open tasks occurrences in the series
are deleted and new open task occurrences are created based on the new recurrence pattern. The following fields determine the
recurrence pattern: `RecurrenceType`, `RecurrenceTimeZoneSidKey`, `RecurrenceInterval`,
`RecurrenceDayOfWeekMask`, `RecurrenceDayOfMonth`, `RecurrenceInstance`, and
`RecurrenceMonthOfYear` .

**•** When you change the value of `RecurrenceEndDateOnly` to an earlier date (for example, from January 20 to January 10), all
open task occurrences in the series with the `ActivityDate` value greater than the new end date value are deleted. Other open
and closed task occurrences in the series are not affected.

**•** When you change the value of `RecurrenceEndDateOnly` to a later date (for example, from January 10 to January 20), new
task occurrences are created up to the new end date. Existing open and closed tasks in the series are not affected.

This table describes the usage of recurrence fields for Salesforce Classic recurring events. Each recurrence type must have all of its
properties set. All unused properties must be set to null.

**RecurrenceType Value** **Properties** **Example Pattern**

RecursDaily RecurrenceInterval Every second day

RecursEveryWeekday RecurrenceDayOfWeekMask Every weekday - can’t be Saturday or Sunday

RecursMonthly RecurrenceDayOfMonth Every second month, on the third day of the month
RecurrenceInterval

RecursMonthlyNth RecurrenceInterval RecurrenceInstance Every second month, on the last Friday of the month
RecurrenceDayOfWeekMask


Standard Objects Task

**RecurrenceType Value** **Properties** **Example Pattern**

RecursWeekly RecurrenceInterval Every three weeks on Wednesday and Friday
RecurrenceDayOfWeekMask

RecursYearly RecurrenceDayOfMonth Every March on the 26th day of the month
RecurrenceMonthOfYear

RecursYearlyNth RecurrenceDayOfWeekMask The first Saturday in every October
RecurrenceInstanceRecurrenceMonthOfYear

**JunctionIdList**

The `JunctionIdList` field is now implemented in the Event and Task objects. With a single API call, it’s easy to create
many-to-many relationships between the Event or Task object with contacts, leads, or users.

To create a Task with related Contacts without `JunctionIdList`, you first have to create the task, then use the returned task
ID to create the `TaskRelation` records. If the `TaskRelation` save call fails, error handling is your responsibility because the
task has already been committed to the database.

```
     public void createTasksOld(Contact[] contacts) {

      Task task = new Task();

      task.setSubject("New Task");

      SaveResult[] results = null;

      try {

      results = connection.create(new Task[] {

       task

      });

      if (results[0].isSuccess()) {

       TaskRelation[] relations = new TaskRelation[contacts.size()];

       for (int i = 0; i < contacts.length; i++) {

       relations[i] = new TaskRelation();

       relations[i].setTaskId(results[0].getID());

       relations[i].setRelationId(contacts[i].getID());

       }

       results = connection.create(relations);

      }

      } catch (ConnectionException ce) {

      ce.printStackTrace();

      }

     }

```

To create a task using `JuncionIdList`, IDs are pulled from the related contacts and both the task and the `TaskRelation`
records are created in one API call. If the `TaskRelation` fails, the task is rolled back because it’s all done in a single API call.

```
     public void createTaskNew(Contact[] contacts) {

      String[] contactIds = new String[contacts.size()];

      for (int i = 0; i < contacts.size(); i++) {

      contactIds[i] = contacts[i].getID();

      }

      Task task = new Task();

      task.setSubject("New Task");

      task.setTaskWhoIds(contactIds);

      SaveResult[] results = null;

      try {

```


### Standard Objects TaskPriority

```
      results = connection.create(new Task[] {

       task

      });

      } catch (ConnectionException ce) {

      ce.printStackTrace();

      }

     }

```

**Shared Field-Level Security for Event and Task Objects**

Metadata deployments for the Task object should always include the field-level security for the Event object. Shared field-level security
prevents each object from changing the field-level security of the associated object.

Metadata deployments that include field-level security for only one of either the Event or Task objects can cause field-level security
changes to the other object that aren't reflected in the metadata.

**•** If field-level security is enabled for one object, then field-level security is enabled for both objects.

**•** If field-level security is disabled for one object, then it's disabled for both objects.

Note: A missing entry in the metadata is treated as field-level security being disabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaskChangeEvent (API version 44.0)**
Change events are available for the object.

**TaskFeed (API version 20.0)**
Feed tracking is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskPriority

Represents the importance or urgency of a task, such as High, Normal, or Low.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer and Partner Portal users can’t access this object.


Standard Objects TaskPriority

Fields

**Field** **Details**

```
ApiName

IsDefault

IsHighPriority

MasterLabel

SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task priority value ( `true` ) or not ( `false` ) in the
picklist. Only one value in the picklist can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task priority value represents a high priority task ( `true` ) or not
( `false` ). Multiple task priority values can represent a high-priority task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task priority value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number used to sort this value in the task priority picklist. These numbers aren’t guaranteed
to be sequential, as some previous task priority values might have been deleted.


### Standard Objects TaskRelation

Usage

This object represents a value in the task priority picklist. The task priority picklist provides additional information about the importance
of a task, such as whether a given priority value represents a high priority. Your client application can query on this object to retrieve
the set of values in the task priority picklist, and then use that information while processing task objects to determine more information
about a given task. For example, the application could test whether a given task is high priority based on its `Priority` value and the
value of the `IsHighPriority` field in the associated TaskPriority object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskRelation

Represents the relationship between a task and a lead, contacts, and other objects related to the task. If Shared Activities is enabled, this
object doesn’t support triggers, workflow, or data validation rules. This object is available in API version 24.0 and later.

### TaskRelation is only available if you’ve enabled Shared Activities in your organization. TaskRelation allows the following relationships:

**•** A task can be related to one lead or up to 50 contacts.

**•** A task can also be related to one account, asset, campaign, case, contract, opportunity, product, solution, or custom object.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `queryAll()`,

```
   retrieve()

```

Fields

**Field Name** **Details**

```
AccountId

IsWhat

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects TaskRelation

**Field Name** **Details**

**Description**
Indicates whether the relation is an Account, Opportunity, Campaign, Case, other
standard object, or a custom object. Value is `false` if `RelationId` is a
contact or lead and `true` otherwise.

```
RelationId

TaskId

```

Usage

**See contacts associated with a task**

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Indicates the `WhatId` or `WhoId` in the relationship. For more information, see
`Task` .

For information on IDs, see ID Field Type.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the ID of the associated Task.

For information on IDs, see ID Field Type.

```
  public void queryWhosOfTaskSample() {

     String soqlQuery = "SELECT Id, Subject, (SELECT RelationId, Relation.Name, IsWhat

   from TaskRelations WHERE isWhat = false) FROM Task WHERE Id = '00T x0000005OKEN'";

    QueryResult qResult = null;

    try {

       qResult = connection.query(soqlQuery);

       TaskRelation relation1 =

  (TaskRelation)qResult.getRecords()[0].getTaskRelations().getRecords()[0];

    }catch (ConnectionException ce) {

       ce.printStackTrace();

     }

   }

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects TaskStatus

**TaskRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

### Task

TaskWhoRelation

### TaskStatus

Represents the status of a task, such as Not Started, Completed, or Closed.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ApiName

IsClosed

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task status value represents a closed task ( `true` ) or not ( `false` ).
Multiple task status values can represent a closed task.

**Type**
boolean


### Standard Objects TaskTag

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task status value ( `true` ) or not ( `false` ) in the
picklist.

```
 MasterLabel

 SortOrder

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task status value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the task status picklist. These numbers aren’t guaranteed
to be sequential, as some previous task status values might have been deleted.

This object represents a value in the task status picklist. The task status picklist provides additional information about the status of a task
, such as whether a given status value represents an open or closed task. Your client application can query this object to retrieve the set
of values in the task status picklist, and then use that information while processing task records to determine more information about
a given task. For example, the application could test whether a given task is open or closed based on the task `Status` value and the
value of the `IsClosed` property in the associated TaskStatus record.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskTag

Associates a word or short phrase with a task .

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects TaskTag

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

TaskTag stores the relationship between its parent TagDefinition and the task being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.


### Standard Objects TaskWhoRelation

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### TaskWhoRelation

Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.

### TaskWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared

Activities for your organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
AccountId

RelationId

TaskId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the task.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects TaxEngine

**Field Name** **Details**

**Description**
Indicates whether the person related to the task is a lead or contact.

Usage

Here's a Java example that queries contacts associated with a task.

```
   public void queryWhosOfTaskSample() {

      String soqlQuery = "SELECT Id, Subject, (SELECT RelationId, Relation.Name, IsWhat from

    TaskWhoRelations) FROM Task WHERE Id = '00Tx0000005OKEN'";

      QueryResult qResult = null;

      try {

        qResult = connection.query(soqlQuery);

        TaskWhoRelation relation1 =

   (TaskWhoRelation)qResult.getRecords()[0].getTaskWhoRelations().getRecords()[0];

      } catch (ConnectionException ce) {

        ce.printStackTrace();

      }

   }

```

SEE ALSO:

Task

TaskRelation

### TaxEngine

A tax engine represents both an instance of a tax engine provider as well as the merchant credentials for that specific instance. When
Subscription Management calculates tax on an order item, it sends a request through Subscription Management Tax Calculation API to
an external tax engine. The Salesforce tax engine record contains information passed to the external tax engine, such as This object is
available in API version 55.0 and later.

The merchant credentials are stored in a named credential record in Salesforce. The named credential record is referenced in the tax
engine object’s Merchant Credentials field.

The tax adapter Apex class ID is stored in the tax engine provider. When a user calls Calculate Tax API, Subscription Management interacts
with the external tax provider using the adapter class and the named credentials.

The tax engine address and seller code from the TaxEngine record are also used in the interaction.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects TaxEngine

Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. If your org has Subscription Management
and Commerce Subscriptions enabled, then Subscription Management takes precedence.

Special Access Rules

This object is available with Subscription Management, Commerce Subscriptions, and Billing (Revenue Cloud). If your org has Subscription
Management and Commerce Subscriptions enabled, then Subscription Management takes precedence.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)

Fields

**Field** **Details**

```
Description

ExternalReference

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider and merchant credential.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Shows information about the external platform used for the tax engine.

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


Standard Objects TaxEngine

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
MerchantCredentialId

SellerCode

Status

TaxEngineAddress

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Looks up to the merchant credential setup entity in Salesforce. CommerceTax Tax Calculation
API sends this information to the external tax engine for use in the tax calculation process.

This field is a relationship field.

**Relationship Name**
MerchantCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Seller code of the transaction for which the tax engine integration log was captured.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows the status of the tax engine.

Possible values are:

**•** `Active` —This tax engine is available for use.

**•** `Inactive` —This tax engine isn't available for use.

**Type**
address

**Properties**
Filter


Standard Objects TaxEngine

**Field** **Details**

**Description**
[The compound form of the tax engine address. Read-only. See Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
for details on compound address fields.

```
TaxEngineCity

TaxEngineCountry

TaxEngineGeocodeAccuracy

TaxEngineLatitude

TaxEngineLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
[Accuracy level of the geocode for the tax engine address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLongitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects TaxEngine

**Field** **Details**

**Description**
Used with TaxEngineLatitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

```
TaxEngineName

TaxEnginePostalCode

TaxEngineProviderId

TaxEngineState

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the tax engine.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Postal code maximum size is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Id of the tax engine provider.

This field is a relationship field.

**Relationship Name**
TaxEngineProvider

**Relationship Type**
Lookup

**Refers To**
TaxEngineProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. State maximum size is 80 characters.


### Standard Objects TaxEngineInteractionLog

**Field** **Details**

```
TaxEngineStreet

TaxPrvdAccountIdentifier

Type

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the external tax provider’s account. This field is only available if
Commerce Subscriptions is enabled for your org. Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the tax engine used to calculate tax. This field is only available if Commerce
Subscriptions is enabled for your org. Available in API version 63.0 and later.

Possible values are:

**•** `CommerceTaxExtension` —Commerce Tax Extension

**•** `RevenueCloudTaxExtension` —Revenue Cloud Tax Extension

**•** `StandardTaxEngine` —Standard Tax Extension

**•** `StripeNative` —Stripe Native

### TaxEngineInteractionLog

A record of a communication with an external tax engine following a tax calculation request. This object is available in API version 55.0
and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```


Standard Objects TaxEngineInteractionLog

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)

Fields

**Field** **Details**

```
Description

DocumentCode

EffectiveDate

InteractionHttpStatusCode

InteractionType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined description for providing more information about the tax engine
interaction log.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Document code of the transaction for which the tax engine integration log was captured.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the tax engine request takes effect. This date is available for reference and
bookkeeping only and doesn’t have any impact on tax calculation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HHTP result code of the external callout made to a third-party tax engine provider. Refer
to your third-party tax engine provider’s documentation for details about the specific codes
returned.

**Type**
picklist


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of request made to the tax engine. In Subscription Management Summer
‘22, only `CalculateTax` is supported.

Possible values are:

**•** `CalculateTax`

```
LastReferencedDate

LastViewedDate

ReferenceEntity

RequestBody

RequestContentType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record on which tax was calculated.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API request.

**Type**
picklist


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of data passed in the request. For example, `application/html` or
`text/csv` .

```
RequestLength

RequestName

ResponseBody

ResponseContentType

ResponseLength

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the request body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the request.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API response.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the method used to deliver the tax calculation API response, such as
`application/html` or `text/vnd.salesforce.quip-template` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the response body.


Standard Objects TaxEngineInteractionLog

**Field** **Details**

```
ResponseName

ResultCode

TaxEngineId

TaxEngineInteractionLogNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the response from the tax engine.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The code describing the result of the request.

Possible values are:

**•** `AdapterException` —The Apex adapter interface for the tax provider threw an
exception.

**•** `Success` —The request was successful.

**•** `TaxEngineError` —An error occurred while processing the request. See the log for
details.

**•** `ValidationError` —A validation error occurred. Check that the request is complete
and valid.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax engine used in the tax calculation process.

This field is a relationship field.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects TaxEngineProvider

**Field** **Details**

**Description**
A system-generated number for a log entry.

### TaxEngineProvider

Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce,
and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine record
represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API version
55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)

Fields

**Field** **Details**

```
ApexAdapterId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Id of the Apex adapter used by this tax provider. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
ApexAdapter

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
textarea


### Standard Objects TaxGeoConfig

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider.

```
DeveloperName

Language

MasterLabel

NamespacePrefix

### TaxGeoConfig

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used by this tax engine provider. Values appear based on their language codes
in Salesforce, such as `da` for Danish or `th` for Thai.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label used for the tax engine’s API in Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Apex namespace prefix of the API used for the tax engine. In a packaging context, a
namespace prefix is a one to 15-character alphanumeric identifier that distinguishes your
package and its contents from packages of other developers on AppExchange.

Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.


Standard Objects TaxGeoConfig

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxGeoConfig object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
GeoCountryId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The GeoCountry associated with the TaxGeoConfig.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.


Standard Objects TaxGeoConfig

**Field** **Details**

```
Name

OwnerId

RoundingStrategyType

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the TaxGeoConfig.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the TaxGeoConfig record. By default, the asset owner is the user who created
the record.

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
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the tax rounding strategy associated with the TaxGeoConfig.

Possible values are:

**•** `Rounding Down`

**•** `Rounding Off`

**•** `Rounding Up`

The default value is `Rounding Off` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects TaxPolicy

**TaxGeoConfigShare on page 67**
Sharing is available for the object.

SEE ALSO:

GeoCountry

### TaxPolicy

A tax policy contains a group of tax treatments, where each treatment represents parameters to determine how a particular product is
taxed for a transaction line item. Tax policies are related to products, which pass the policy on to the resulting order items. When you
activate an order, Subscription Management assigns a tax treatment to each order item based on the tax policy's DefaultTaxTreatmentId,
then uses the tax treatment to calculate tax. This object is available in API version 55.0 and later.

Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)

Fields

**Field** **Details**

```
DefaultTaxTreatmentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When you order a product, the order product receives this tax treatment.

This field is a relationship field.

**Relationship Name**
DefaultTaxTreatment

**Relationship Type**
Lookup


Standard Objects TaxPolicy

**Field** **Details**

**Refers To**
TaxTreatment

```
Description

LastReferencedDate

LastViewedDate

Name

Status

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for providing more information about the tax policy.

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
Optional user-defined name for the tax policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
To calculate tax for order products, products must have an active tax policy. Tax policies are
created with a Draft status before being assigned to a product or order product. After
activating a tax policy, you can't edit certain policy fields.


### Standard Objects TaxRate

**Field** **Details**

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

```
TreatmentSelection

### TaxRate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management chooses a tax treatment to assign to order products
related to this tax policy. In API version 55.0, only `Default` is supported.

Possible values are:

**•** `Default` —The order product receives the tax treatment defined in the tax policy's
`DefaultTreatmentId` field.

**•** `LegalEntity` —Assigns a tax treatment based on matching legal entities between
the order product and tax treatment.

**•** `Manual` —Order products don't receive tax treatments based on the tax policy; users
must provide the treatment on their own instead.

Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxRate object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
GeoCountryId

```

**Type**
reference


Standard Objects TaxRate

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the GeoCountry for which the tax rate applies. You can define only one tax rate per
GeoCountry and tax code combination.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

```
LastReferencedDate

LastViewedDate

Name

OwnerId

```

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
it's possible the user accessed data in this record or list view but didn't viewed it directly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique ID of the tax rate.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects TaxRate

**Field** **Details**

**Description**
The TaxRate record owner. By default, the record owner is the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Priority

Rate

TaxCode

```

Associated Objects

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The tax percentage rate that will be applied to orders.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The code used to calculate the tax rate for the invoice line.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaxRateChangeEvent on page 68**
Change events are available for the object.

**TaxRateFeed on page 55**
Feed tracking is available for the object.

**TaxRateHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects TaxTreatment

**TaxRateOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TaxRateShare on page 67**
Sharing is available for the object.

### TaxTreatment

A tax treatment contains details about how Salesforce and external engines calculate taxes, and the tax engine to use for tax calculation.
The IsTaxable field determines whether tax is calculated for the product in the transaction. The tax code, tax engine, and product code
are sent via API to the external tax calculation service. When you invoice an order item that has a tax treatment, the invoice line inherits
the tax treatment from the order item’s related billing schedule. The invoice line’s TaxCode field is populated based on the code that
the tax engine used for calculation. This object is available in API version 55.0 and later.

Each product requires a tax policy to determine whether to apply tax. The tax treatments determine how taxable products are taxed.
Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)

Fields

**Field** **Details**

```
Description

IsTaxable

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for providing more information about the tax treatment.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects TaxTreatment

**Field** **Details**

**Description**
Determines whether Subscription Management calculates tax for order items covered by
the tax treatment. When this value is True, Subscription Management calls the CalculateTax
API for the order item during order item creation.

The default value is 'False'.

This field is available when Subscription Management is enabled.

```
LastReferencedDate

LastViewedDate

Name

ProductCode

Status

```

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
Optional user-defined name for the tax treatment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Code of the product that the tax treatment applies to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects TaxTreatment

**Field** **Details**

**Description**
Status of the tax treatment.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

```
TaxCode

TaxEngineId

TaxPolicyId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference code used when tax is calculated in an external tax engine.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax engine for the tax treatment. A tax engine represents both an instance of a tax engine
provider as well as the merchant credentials for that specific instance. When Subscription
Management begins the tax calculation process for an order item, it uses the tax engine
from the order item’s tax treatment.

If the tax treatment’s `IsTaxable` value is True, the treatment requires a tax engine.

This field is a relationship field.

This field is available when Subscription Management is enabled.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax treatment’s parent tax policy. A tax policy is a group of tax treatments, where each
treatment represents a rule for how to invoice a customer for an order item. Tax policies are
related to products, which pass the policy on to the resulting order items. When you activate


### Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

an order, Subscription Management assigns a tax treatment to each order item based on
the tax policy's DefaultTaxTreatmentId, then uses the tax treatment to calculate tax.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

### TenantScrAIPrmptInjection

Stores generative AI prompt injection data. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

InputSource

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin of this prompt.


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

```
Language

MaskedPrompt

MaskedResponse

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Language of the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
Masked prompt or input text.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response from the LLM. If masking is enabled, this may contain placeholder
text.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

**Description**
The name of the metric for which data is being collected.

```
PlannerLlm

Prompt

PromptTimestamp

PromptTokens

Response

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The LLM being used by the Planner.

**Type**
textarea

**Properties**
Nillable

**Description**
The hydrated version of prompt text before data masking is applied. The actual prompt sent
to the LLM will mask sensitive data if data masking is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when this prompt injection happened.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of tokens used in the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response after unmasking.

**Type**
string


### Standard Objects TenantSecret

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this triggered Transaction Security Policy event.

```
TenantName

### TenantSecret

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

This object stores an encrypted organization-specific key fragment that’s used with the primary secret (KDF seed) to produce org-specific
data encryption keys. This object is available in API version 34.0 and later.

You can rotate tenant secrets of the `Data` type once every four hours in a sandbox org or every 24 hours in production orgs. You can
rotate tenant secrets of the `SearchIndex` type one time every seven days.

Note: This information is about Shield Platform Encryption and not Classic Encryption.

Supported Calls

`create()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Description

KeyDerivationMode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The description of the tenant secret.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The key derivation mode applied to customer-supplied key material. Modes are:

**PBKDF2**
The customer-supplied key material is used by the Shield KMS to create a
derived data encryption key.

**NONE**
The customer-supplied key material is used by the Shield KMS as the final
data encryption key to directly encrypt and decrypt data.

Available in API version 43.0 and later.

```
RemoteKeyCertificate

RemoteKeyIdentifier

RemoteKeyServiceID

SecretValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the certificate whose public key is used to encrypt the
`SecretValue` during a remote key callout.

Available in API version 45.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique key identifier for key material fetched from a remote key service.

Available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The named credential used to fetch remote key material from a remote key
service.

Available in API version 45.0 and later.

**Type**
base64

**Properties**
Create, Nillable, Update


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The encrypted 256-bit secret value encoded in base64.

```
SecretValueCertificate

SecretValueHash

Source

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The certificate needed to upload a customer-supplied tenant secret. Each
certificate has a unique name.

**Type**
base64

**Properties**
Create

**Description**

The matching tenant secret hash for an uploaded customer-supplied tenant
secret.

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the encryption key material. Values are:

**HSM**
A Salesforce-generated tenant secret.

**Uploaded**
A customer-supplied tenant secret or data encryption key.

**Remote**
A tenant secret or data encryption key fetched from a key service outside of
Salesforce. Available in API version 44.0 and later.Tenant secrets with a
`Source` value of Remote are listed as Fetched on the Key Management
page in Setup.

Available in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The status of the tenant secret. Values are:

**Active**
Can be used to encrypt and decrypt new or existing data.

**Archived**
Can’t encrypt new data. Can be used to decrypt data previously encrypted
with this key when it was active.

**Destroyed**
Can’t encrypt or decrypt data. Data encrypted with this key when it was active
can no longer be decrypted. Files and attachments encrypted with this key
can no longer be downloaded.

You can update the `Status` field through the API in versions 44.0 or later.

```
Type

Version

```

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of tenant secret. The `Type` field is available in API version 39.0 and
later. The following values appear in the `Type` picklist:

**•** `Analytics` —CRM Analytics data (available in API version 39.0 and later).

**•** `Data` —data stored in the Salesforce database. Includes data in encrypted
fields, files, and attachments but not search index files. Tenant secrets created
in API version 34.0 and later default to the `Data` type.

**•** `Database` —transactional database including standard and custom fields,
metadata, and Apex (available in API version 62.0 and later).

**•** `DeterministicData` —data stored in the Salesforce database. Includes
data in encrypted fields, files, and attachments, but not search index files
(available in API version 39.0 and later).

**•** `EventBus` —Change Data Capture event data (available in API version 43.0
and later).

**•** `SearchIndex` —search index files (available in API version 39.0 and later).

For Hyperforce orgs on API version 63.0 and later, create secrets of type
`SearchIndex` with the DataEncryptionKey object. For Hyperforce orgs
on API version 62.0 and earlier, and for all non-Hyperforce orgs, create secrets
of type `SearchIndex` with the TenantSecret object.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The version number of this secret. The version number is unique within your org.

Usage

Use this object to create or update an org-specific tenant secret or customer-supplied key material.

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, the video How To Use Salesforce APIs Collection With Postman by Sudipta Deb provides step](https://www.youtube.com/watch?v=DJ7_iW2B5tA)
by step instructions on getting started using REST with Salesforce.

Example 1:

Build an automated tenant secret creation and activation solution similar to the following.

**1.** Start by creating an Apex class to create the tenant secret. Specify the value of the tenant secret to encrypt data of a particular type.

```
     global class CreateNewSecret implements Schedulable {

       global void execute(SchedulableContext SC) {

         TenantSecret secret = new TenantSecret ();

         secret.description = 'Created new secret from scheduled job';

         secret.type= 'Database';

         insert secret;

       }

     }

```

Note: `Type` is available in API version 39.0 and later. `Type` is optional; all tenant secrets default to the `Data` type.

**2.** Schedule the Apex class to run at the specified interval.

This Apex code only needs to be run a single time to schedule the job. This code runs the job every 90 days.

```
     CreateNewSecret secret = new CreateNewSecret();

     String schedule = '0 0 0 1 JAN,APR,JUL,OCT ?';

     String jobID = system.schedule('Automated secret creation and activation', schedule,

     secret);

```

**3.** Validate that the job is scheduled.

**4.** Validate that tenant secrets are created after the job is run.

Example 2

Upload a customer-supplied tenant secret.

**1.** [Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)
Help.


Standard Objects TenantSecret

**2.** Then upload your matching key material and key material hash. Include the unique name of the compatible certificate. The key
material is uploaded in encrypted form.

```
         TenantSecret secret = new TenantSecret ();

         secret.description = 'New uploaded secret';

         secret.type= 'Data';

         secret.SecretValue = ...

         EncodingUtil.base64Decode('...');;

         secret.SecretValueCertificate = ...;

         secret.SecretValueHash = ...

         EncodingUtil.base64Decode('...');

         insert secret;

```

[You can use this script to generate a customer-supplied tenant secret and tenant secret hash.](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok_script.htm&type=5&language=en_US)

**3.** Validate that the key material is uploaded.

Example 3

Opt out of key derivation on a key-by-key basis when you upload key material. When you upload your key material, specify
`'Source':Uploaded` and `'KeyDerivationMode':'NONE'`, and set non-null values for the SecretValueCertificate,
SecretValue, and SecretValueHash.

Example 4

Import a tenant secret of the `Data` type.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.SecretValue = "<previously_exported_secret_as_a_String>";

   update secret;

```

Example 5

Export a tenant secret by writing the `secret.SecretValue` to a file. Here’s an example that uses a tenant secret of the `Data`
type.

```
   TenantSecret secret = [SELECT SecretValue FROM TenantSecret WHERE Type = 'Data' AND Version

    = 2];

   secret.SecretValue =...;

   update secret;

```

Example 6

Destroy a tenant secret of the `Data` type.

Warning: Your tenant secret is unique to your organization and to the specific data to which it applies. When you destroy a
tenant secret, related data isn’t accessible unless you previously exported the key and then import the key back into Salesforce.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.SecretValue = NULL;

```


### Standard Objects TenantSecurityAIGtwyUsage

```
   secret.Status = Destroyed;

   update secret;

```

Example 7

Change the `Status` of a tenant secret from Archived to Destroyed. Include the SecretValue and new tenant secret Status.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.Status = Destroyed;

   update secret;

```

Cache-Only Key Service customers can change the Status of cache-only key tenant secrets. For example, reactivate a cache-only key by
changing its Status from Destroyed to Active.

Example 8

Create a callout connection that fetches a cache-only key tenant secret from a key service outside of Salesforce.

**1.** Make sure that your org has at least one active Data in Salesforce key, either Salesforce-generated or customer-supplied. Then turn
on Allow Cache-Only Keys with BYOK from the Advanced Settings page in Setup.

**2.** [Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)
Help.

**3.** [Create and assemble your key material.](https://help.salesforce.com/articleView?id=security_pe_byok_cache_create.htm&language=en_US)

**4.** Create a named credential to serve as your authenticated callout mechanism. You can define your named credential through Setup
[or directly with Apex. Specify a BYOK-compatible certificate and an HTTPS endpoint.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

**5.** Configure the connection to your remote key service. This connection uses a named credential and its associated certificate to fetch
a specified cache-only key tenant secret.

```
     remote_params = { 'Source': 'Remote',

     'RemoteKeyIdentifier': ...,

     'RemoteKeyServiceId': ...,

     'RemoteKeyCertificate': ...}

     sf.TenantSecret.create(remote_params)

```

SEE ALSO:

System Fields

### TenantSecurityAIGtwyUsage

Stores Einstein generative AI gateway usage data. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityAIGtwyUsage

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Cloud

DetailIdentifier

Feature

MaskedPrompt

MaskedResponse

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Cost cloud ID.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The AI feature for which the gateway request was made.

**Type**
textarea

**Properties**
Nillable

**Description**
Masked prompt or input text.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response from the LLM. If masking is enabled, this may contain placeholder
text.


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

```
MetricIdentifier

MetricsType

Model

Name

ObjectName

Prompt

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the model to which the request was sent.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Name of the Salesforce object is referenced in the prompt.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

**Description**
The hydrated version of prompt text before data masking is applied. The actual prompt sent
to the LLM will mask sensitive data if data masking is enabled.

```
PromptTemplateDevName

PromptTemplateVersionNo

PromptTokens

Response

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the prompt template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the prompt template.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of tokens used in the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response after unmasking.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant of this AI gateway usage event.

**Type**
string


### Standard Objects TenantSecurityAlertRuleSelectedTenant

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant of this AI gateway usage event.

### TenantSecurityAlertRuleSelectedTenant

Stores information about a Security Center alert rule for tenants. This object is available for Security Center subscribers in API version
55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Name

NotificationRuleIdentifier

### `Tenant`

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the corresponding TenantSecurityNotificationRule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Description**
The ID of the tenant (org) that this record is for.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityAlertRuleSelectedTenantChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityAlertRuleSelectedTenantFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityAlertRuleSelectedTenantHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityAlertRuleSelectedTenantOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityAlertRuleSelectedTenantShare on page 67**
Sharing is available for the object.

### TenantSecurityApiAnomaly

[Stores detected anomalies in how users typically make API calls. Fore more information, see Threat Detection. This object is available to](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
Security Center subscribers in API version 53.0 and later.

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Description**
The ID of the individual detail record. This field is unique within your org.

```
EventDate

EventIdentifier

EventName

MetricIdentifier

MetricsType

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Api Anomaly.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

```
Operation

QueriedEntities

RequestIdentifier

RowsProcessed

Score

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API call that generated the event. For example, Query.

**Type**
textarea

**Properties**
Nillable

**Description**
The type of entities associated with the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total row count for the current operation.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
A number from 0 through 100 that represents the anomaly score for the API execution or
export tracked by this event. The anomaly score shows how the current API activity differs
from the user’s typical activity. A low score indicates that the user’s current API activity is
similar to the usual activity, and a high score indicates that it’s different.


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

```
SecurityEventData

Summary

Tenant

TenantName

Uri

```

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the API activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows how much as a percentage that the feature contributed to triggering this anomaly
event. The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the API anomaly that caused this event.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .


### Standard Objects TenantSecurityCertificate

**Field** **Details**

```
UserAgent

UserIdentifier

Username

```

Associated Objects

**Type**
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityApiAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityApiAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityApiAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityApiAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityApiAnomalyShare on page 67**
Sharing is available for the object.

### TenantSecurityCertificate

Stores metric details related to public key certificate information. The certificate binds the public key to the identity of an entity. This
object is available in API version 63.0 and later.


Standard Objects TenantSecurityCertificate

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

CertCreatedDate

```

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on this certificate. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action was taken.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate was created.


Standard Objects TenantSecurityCertificate

**Field** **Details**

```
DetailIdentifier

ExpirationDate

IsActive

IsCaSigned

IsPlatformEncrypted

IsPrivateKeyExportable

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate expires.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is active.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is signed by the issuer (true) or not (false).

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Whether this certificate is encrypted with Platform Encryption.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate’s private key is exportable.


Standard Objects TenantSecurityCertificate

**Field** **Details**

```
KeySize

MetricIdentfier

MetricsType

Name

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the public key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user-friendly name for the certificate.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this certificate.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant with this certificate.


### Standard Objects TenantSecurityConnectedApp TenantSecurityConnectedApp

Stores the details for a connected app that was added to or removed from a Security Center tenant. This object is available to Security
Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the connected app within a tenant.

Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who performed the action on the connected app.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the action was taken.


Standard Objects TenantSecurityConnectedApp

**Field** **Details**

```
AppName

AuthorizedBy

AuthorizedDate

DetailIdentifier

LastUsedDate

MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected app.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who authorized the connected app to be installed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the connected app was authorized for installation.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date that the connected app was used for authentication.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.


Standard Objects TenantSecurityConnectedApp

**Field** **Details**

```
MetricsType

Name

Publisher

Scope

Tenant

TenantName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents if the relevant tenant is the original publisher of the connected app for all
connected tenants in the org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The scope or scopes assigned to the connected app. A scope defines the type of protected
resource that the connected app can access.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the relevant tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


### Standard Objects TenantSecurityConfigAgent

**Field** **Details**

**Description**
The name of the tenant that the connected app is connected to.

```
Version

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the connected app.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityConnectedAppChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityConnectedAppFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityConnectedAppHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityConnectedAppOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityConnectedAppShare on page 67**
Sharing is available for the object.

### TenantSecurityConfigAgent

Stores metric details related to implemented Agentforce Agents This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.


Standard Objects TenantSecurityConfigAgent

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

AgentName

AgentType

AssignedTopics

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action taken on the configured agent within a tenant.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action was taken.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the configured agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of agent.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityConfigAgent

**Field** **Details**

**Description**
The list of agent topics.

```
DetailIdentifier

MetricIdentifier

MetricsType

Name

Status

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status, active or inactive, of the agent version.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
The ID of the tenant.

```
TenantName

Version

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tenant.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number.

### TenantSecurityCredentialStuffing

[Stores when a user successfully logs in to Salesforce during an identified credential stuffing attack. For more information, see Threat](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
[Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
AcceptLanguage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
List of HTTP headers that specify the natural language, such as English, that the client
understands.

```
DetailIdentifier

EventDate

EventIdentifier

EventName

LoginType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Credential Stuffing.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. For the list of possible values, see the LoginType
[field of LoginHistory in the Object Reference.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

```
LoginUrl

MetricIdentifier

MetricsType

Name

Score

Summary

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the login page. For example, `login.salesforce.com` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Indicates that a user successfully logged in to Salesforce during an identified credential
stuffing attack. The value of this field is always 1.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
A summary of the threat that caused this event to be created.

```
Tenant

TenantName

UserAgent

UserIdentifier

Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time the event was created.


### Standard Objects TenantSecurityCustomMetricSetup

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityCredentialStuffingChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityCredentialStuffingFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityCredentialStuffingHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityCredentialStuffingOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityCredentialStuffingShare on page 67**
Sharing is available for the object.

### TenantSecurityCustomMetricSetup

Represents the configuration for a custom metric within Security Center. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomMetricIdentifier

CustomObjectIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for the custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the custom object for this custom metric.


Standard Objects TenantSecurityCustomMetricSetup

**Field** **Details**

```
CustomObjectName

DiffFieldIdentifierList

DisplayFieldIdentifierList

Description

MetricDisplayType

MetricGroup

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the custom object for this custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for `Diff` display.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for display.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The display type for this metric. For example, `diff` or `non-diff.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects TenantSecurityCustomMetricDetail

**Field** **Details**

**Description**
The category of the custom metric. Some category examples include
`Authentication` and `Configuration` .

```
MetricName

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The `MetricName` and `Name` fields have the same value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The `MetricName` and `Name` fields have the same value.

### TenantSecurityCustomMetricDetail

Stores TenantSecurityCustomMetricStat drill down details. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Whether the metric detail record was added, updated, or removed.


Standard Objects TenantSecurityCustomMetricDetail

**Field** **Details**

```
ActionBy

ActionDate

CustomObjectIdentifier

DiffFieldValueListHash

FieldValueListHash

MetricStatIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user who performs the action.

**Type**
dateTime

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
When this change was made.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to a Custom Object in which the metric details are stored.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The hash of custom metric `diff` fields value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The hash of custom metric fields value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to TenantSecurityCustomMetricStat.


### Standard Objects TenantSecurityCustomMetricStat

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Custom Object Api Name associates to the custom metric.

### TenantSecurityCustomMetricStat

Represents custom metric data within Security Center. This object is available in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
ChangeCount

CustomMetricIdentifier

EndProcessTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this metric was changed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the custom metric.

**Type**
dateTime


Standard Objects TenantSecurityCustomMetricStat

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The end time of the metric being processed.

```
MetricCount

MetricIdentifier

MetricName

Name

PreviousMetricIdentifier

StartProcessTime

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of times this metric was recorded.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the custom metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous unique identifier of this metric.

**Type**
dateTime


### Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The start time of the metric being processed.

### `Tenant`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant with the custom metric.

### TenantSecurityEncryptedField

Represents fields encrypted under your Shield Platform Encryption policy. This object is available in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the encryption policy within a tenant. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
string


Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
This field is reserved for future use.

```
ActionDate

DetailIdentifier

EncryptionType

FieldName

FieldType

MetricIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of encryption for the field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the encrypted field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of field being encrypted.

**Type**
string


Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

```
MetricsType

Name

ObjectName

Tenant

TenantName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of encryption policy collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object for this encrypted field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with Shield Encryption.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tenant that this record is for.


### Standard Objects TenantSecurityGuestUserAnomaly TenantSecurityGuestUserAnomaly

Represents metric details for guest user anomaly events detected by Threat Detection. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

EventDate

EventIdentifier

EventName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects TenantSecurityGuestUserAnomaly

**Field** **Details**

**Description**
The name of the event.

```
MetricIdentifier

MetricsType

Name

RequestedObjects

Score

SoqlCommands

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The objects requested by the customers.

**Type**
double

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Specifies how significantly the guest user behavior deviates from the other guest users. It is
formatted as a number between 0 and 1.

**Type**
textarea


Standard Objects TenantSecurityGuestUserAnomaly

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
SOQL commands run by the guest user.

```
Summary

Tenant

TenantName

TotalControllerEvents

UserAgent

UserIdentifier

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text summary of the anomaly that caused this event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of times controllers were triggered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User Agent for this event.

**Type**
string


### Standard Objects TenantSecurityEncryptionPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID.

```
UserType

Username

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of user of this event. For example, a guest user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the event was
created.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityGuestUserAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityGuestUserAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityGuestUserAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityGuestUserAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityGuestUserAnomalyShare on page 67**
Sharing is available for the object.

### TenantSecurityEncryptionPolicy

Stores tenant encryption policy status. This object is available in API version 58.0 and later.


Standard Objects TenantSecurityEncryptionPolicy

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

DetailIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the encryption policy within a tenant. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.


Standard Objects TenantSecurityEncryptionPolicy

**Field** **Details**

```
MetricIdentifier

MetricsType

Name

PolicyName

PolicyStatus

Tenant

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of encryption policy collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the policy.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Status of the policy. Possible values are:

**•** `-1` —No license.

**•** `0` —Not Enabled.

**•** `-1` —Enabled

**Type**
string


### Standard Objects TenantSecurityFeature

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with Shield Encryption.

```
TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that this record is for.

### TenantSecurityFeature

Stores org features across all tenants in Security Center. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

FeatureDescription

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityFeature

**Field** **Details**

**Description**
The description of the feature.

```
FeatureName

IsEnabled

MetricIdentifier

MetricsType

Name

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the feature.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feature is enabled or disabled.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of feature collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the feature for which data is being collected.

**Type**
string


### Standard Objects TenantSecurityHealthCheckBaselineTrend

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant where the feature was applied.

```
TenantName

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the connected tenant where the feature was enabled or disabled.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityFeatureChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityFeatureFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityFeatureHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityFeatureOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityFeatureShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckBaselineTrend

Stores metric details related to Health Check baseline settings. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get details about which metrics are collected and for which tenants, and
changes made to the Health Check baseline. This object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.


Standard Objects TenantSecurityHealthCheckBaselineTrend

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

ApiName

BaselineDescription

BaselineIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of action. For example, added, updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user or admin that made the change.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the change.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the metric used by the API and managed packages.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For custom baselines, the name of the custom baseline file.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects TenantSecurityHealthCheckBaselineTrend

**Field** **Details**

**Description**
The ID of the baseline.

```
BaselineName

DetailIdentifier

IsDefault

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the baseline.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the baseline is default or custom. The default is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the type of metric collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of data collected. For example, SecurityHealthCheckBaselineMetric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects TenantSecurityHealthCheckDetail

**Field** **Details**

**Description**
The name of the metric for the data collected.

### `Tenant`

```
TenantName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was scored by the Security Health Check.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was scored by the Security Health Check.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckBaselineTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityHealthCheckBaselineTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckBaselineTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckBaselineTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckBaselineTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckDetail

Stores the details of Health Check scores for a connected tenant. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get settings and risks per tenant on a selected date. This object is available
to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityHealthCheckDetail

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
HealthCheckSettingIdentifier

HealthCheckTrendKey

Name

OrgValue

RiskType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check setting. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Health Check trend related to the Health Check detail records.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org’s value for the security setting.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security setting value.

Possible values are:


Standard Objects TenantSecurityHealthCheckDetail

**Field** **Details**

**•** `HIGH_RISK`

**•** `MEDIUM_RISK`

**•** `MEETS_STANDARD`

```
Setting

SettingGroup

SettingRiskCategory

StandardValue

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting. For example, Minimum Password Length.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting group in Setup that this setting is in. For example, Password
Policies.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security settings.

Possible values are:

**•** `HIGH_RISK`

**•** `INFORMATIONAL`

**•** `LOW_RISK`

**•** `MEDIUM_RISK`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended standard value for the security setting.

**Type**
string


### Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckDetailChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityHealthCheckDetailFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckDetailHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckDetailOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckDetailShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckTrend

Stores the history of Security Health Check scores for a connected tenant within Security Center. Health Check in Security Center displays
Health Check scores and the average risk settings for all your tenants in one place. This object belongs to the parent tenant and stores
Health Check data pushed from child tenants. This object is available for Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Baseline

```

**Type**
string


Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The definition of an org’s security settings standards.

```
HighRisk

Informational

LowRisk

MediumRisk

Name

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data that isn't sensitive for your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data with low sensitivity for your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data with moderate sensitivity for your
company.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.


Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

```
ProcessedTime

Score

ScoreDelta

Tenant

TenantOriginalIdentifier

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the Health Check score was calculated.

**Type**
double

**Properties**
Filter, Sort

**Description**
The summary score that shows how your org measures against a security baseline.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The percentage amount that the Health Check score changed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check Trend record for a tenant. This field is unique within your org.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckTrendChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityLicense

**TenantSecurityHealthCheckTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityLicense

Stores license usage information within Security Center. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Action

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of change made to the license. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when this change was made.


Standard Objects TenantSecurityLicense

**Field** **Details**

```
DetailIdentifier

ExpirationDate

MetricIdentifier

MetricsType

Name

Status

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which this license expires.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of license collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the license.


Standard Objects TenantSecurityLicense

**Field** **Details**

```
Tenant

TenantName

TotalLicenses

UsedLicenses

UsedLicensesLastUpdated

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant with this license.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The total number of licenses.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of used licenses.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the used licenses were last updated for this tenant.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLicenseChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityLogin

**TenantSecurityLicenseFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLicenseHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLicenseOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLicenseShare on page 67**
Sharing is available for the object.

### TenantSecurityLogin

Stores the login details of a single user to a tenant, grouped by date and type. You can query this object to find out how many times the
user logged in to a specific tenant using a specific login type (for example, username/password or SSO). This object is available to Security
Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

LastLoginDate

LoginCount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last time the user logged in.

**Type**
int


Standard Objects TenantSecurityLogin

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of times the user has logged in to the tenant.

```
MetricIdentifier

MetricsType

Name

Tenant

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

The supported metric types are:

**•** LOGIN_PWLESS

**•** LOGIN_PWLESS2FA

**•** LOGIN_UNPW

**•** LOGIN_UNPW2FA

**•** LOGIN_SSO

**•** LOGIN_SSO2FA

**•** LOGIN_OAUTH

**•** LOGIN_OAUTH2FA

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityLogin

**Field** **Details**

**Description**
The ID of the tenant that was scored.

```
TenantName

UserEmail

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityLoginChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityLoginFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLoginHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLoginOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLoginShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityLoginIpRangeTrend TenantSecurityLoginIpRangeTrend

Stores details of changes related to login IP ranges in Security Center. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

Description

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of change made to the login IP range. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when this change was made.

**Type**
string


Standard Objects TenantSecurityLoginIpRangeTrend

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The description of the login IP range record.

```
DetailIdentifier

IpEndAddress

IpRangeIdentifier

IpStartAddress

MetricIdentifier

MetricsType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The end IP address of the login IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of the login IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string


Standard Objects TenantSecurityLoginIpRangeTrend

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of metric for the data collected.

```
Name

ProfileIdentifier

ProfileName

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the profile that is assigned to this login IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile that is assigned to this login IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.


### Standard Objects TenantSecurityMobilePolicyTrend

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLoginIpRangeTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityLoginIpRangeTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLoginIpRangeTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLoginIpRangeTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLoginIpRangeTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityMobilePolicyTrend

Stores metrics related to changes in mobile security policies across all tenants in Security Center. This object is available to Security Center
subscribers in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The change made to the mobile security policy. For example, a new policy was added,
updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Description**
The user who made the change.

```
ActionDate

ConnectedApp

DetailIdentifier

EffectiveDate

IsEnabled

MetricIdentifier

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the mobile security policy change.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app that is associated with the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

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
A value indicating whether the mobile security policy is enabled. The default is `false`,
which means policies are disabled.

**Type**
string


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The foreign key of the metric.

```
MetricsType

MobilePlatform

Name

PolicyType

RuleValue

RuleValueType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of mobile security policy data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The mobile operating system of the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for which data is collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of mobile security policy. For example, Block Calendar.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The value of the security notification rule.

**Type**
string


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of rule value. For example, boolean or text.

```
SeverityLevel

Tenant

TenantName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The severity level of the security threat. For example, `CRITICAL` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPackageChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPackageFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPackageHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPackageOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPackageShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityMonitorMetric TenantSecurityMonitorMetric

Stores the daily count and daily count change for a metric within Security Center. This object is available to Security Center subscribers
in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
ChangeCount

Count

EndProcessTime

MetricIdentifier

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
How much the relevant metric changed.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The current metric count.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process ended.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects TenantSecurityMonitorMetric

**Field** **Details**

**Description**
The ID of the type of metric counted. This field is unique within your organization.

```
MetricsType

Name

PreviousMetricIdentifier

StartProcessTime

Tenant

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous ID of the type of metric that was counted. This field is unique within your
organization.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was scored.


### Standard Objects TenantSecurityNotification

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityMonitorMetricChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityMonitorMetricFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityMonitorMetricHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityMonitorMetricOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityMonitorMetricShare on page 67**
Sharing is available for the object.

### TenantSecurityNotification

Stores information about notifications that were triggered in Security Center as a function of the Alerts feature. For more information,
[see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 54.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
MetricCount

MetricIdentifier

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The metric count that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects TenantSecurityNotification

**Field** **Details**

**Description**
The ID of the type of metric that was counted.

```
MetricsType

Name

NotificationDate

NotificationType

Operator

RecipientEmails

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The metric for which the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the triggered notification rule.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The type of notification sent. For example, a Chatter feed or push notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The quantity of metrics used to measure.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects TenantSecurityNotification

**Field** **Details**

**Description**
The email addresses of the recipients who receive security notifications.

```
RuleName

Tenant

TenantName

Threshold

TriggerType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the notification rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant for which the notification was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The org name of the tenant for which the notification was triggered.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The threshold value that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger that set off the notification. For example, a security change was made.


### Standard Objects TenantSecurityNotificationRule

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityNotificationFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityNotificationHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityNotificationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityNotificationShare on page 67**
Sharing is available for the object.

### TenantSecurityNotificationRule

Stores an alert configured in the Security Center Alerts feature to notify recipients of changes made to security settings. For more
[information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
MetricsType

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of data being collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects TenantSecurityNotificationRule

**Field** **Details**

**Description**
The name of the metric for which data is being collected.

```
NotificationRuleIdentifier

NotificationType

Operator

RecipientEmails

RuleName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the alert that was triggered. This field is unique within your organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of notification used for the alert. The options are:

**•** `Email`

**•** `In-App`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operator for the change that triggered the alert. For example, greater than.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The email addresses for the recipients of the alert details.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom alert that triggered the notification. This field is unique within your
organization.


Standard Objects TenantSecurityNotificationRule

**Field** **Details**

```
Status

Threshold

TriggerType

Version

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The status of the alert setting. The options are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The threshold value that triggered the alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger used for the alert. The values are:

**•** `Always`

**•** `On Change`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the custom alert.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationRuleChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityMetricDetailLink

**TenantSecurityNotificationRuleFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityNotificationRuleHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityNotificationRuleOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityNotificationRuleShare on page 67**
Sharing is available for the object.

### TenantSecurityMetricDetailLink

Represents the link between the metric count and metric drill down. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

MetricIdentifier

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
string


### Standard Objects TenantSecurityPackage

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

### `Tenant`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

### TenantSecurityPackage

Stores details about managed and unmanaged packages that are added, updated, or removed from a tenant in Security Center. Use this
object to identify whether new packages are installed, upgraded, or uninstalled from your connected tenants. This object is available to
Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on a package within a tenant. The options are:

**•** `Added`

**•** `Removed`


Standard Objects TenantSecurityPackage

**Field** **Details**

```
ActionDate

AppExchangeReady

DetailIdentifier

InstalledBy

MetricIdentifier

MetricsType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the action was taken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the package has passed AppExchange review.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user that installed the package.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.


Standard Objects TenantSecurityPackage

**Field** **Details**

```
Name

NamespacePrefix

PackageName

Publisher

ReleaseStatus

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the package.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the package being added to or removed from the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the publisher that created the package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The release status of the package. The options are:

**•** `Beta`

**•** `Released`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityPolicy

**Field** **Details**

**Description**
The ID of the tenant that the package was added to or removed from.

```
TenantName

Version

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that the package was added to or removed from.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the package.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPackageChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPackageFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPackageHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPackageOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPackageShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicy

[Stores security policies created and deployed in Security Center. For more information, see Define and Deploy Security Policies. This](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects TenantSecurityPolicy

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
ApiName

Description

Name

PolicyData

PolicyIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The API name of the policy.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the policy.

**Type**
textarea

**Properties**
Create, Update

**Description**
The policy details contained in JSON format.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of this policy. Contains a unique virtual key from child to parent.


Standard Objects TenantSecurityPolicy

**Field** **Details**

```
PolicyType

SourceRowIdentifier

Status

Version

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The type of policy. For example, Health Check Baseline.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy that is applied to the tenant. This value is specific to the org that owns
this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the policy. For example, the policy is active or inactive.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The version of the policy.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects TenantSecurityPolicyDeployment

**TenantSecurityPolicyShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicyDeployment

[Stores the status of deployments of a Security Center policy on a tenant. For more information, see Define and Deploy Security Policies.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
This object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
DeploymentDate

DeploymentStatus

Description

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date the deployment was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the deployment. For example, Not Deployed, Processing, Deployed, or Failed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the deployment status.


Standard Objects TenantSecurityPolicyDeployment

**Field** **Details**

```
Name

PolicyIdentifier

StatusDate

Tenant

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the TenantSecurityPolicy entity.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date that the status of the deployment was provided.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant for which the policy was deployed.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyDeploymentChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyDeploymentFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyDeploymentHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyDeploymentOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects TenantSecurityPolicySelectedTenant

**TenantSecurityPolicyDeploymentShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicySelectedTenant

[Stores the list of tenants selected for a Security Center policy. For more information, see Define and Deploy Security Policies. This object](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
Name

PolicyIdentifier

### `Tenant`

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the policy for the selected tenant.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.


### Standard Objects TenantSecurityReportAnomaly

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicySelectedTenantChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicySelectedTenantFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicySelectedTenantHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicySelectedTenantOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPolicySelectedTenantShare on page 67**
Sharing is available for the object.

### TenantSecurityReportAnomaly

Stores anomalies in how users run or export reports, including unsaved reports, as detected by Threat Detection. For more information,
[see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

EventDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the detail record. This field is unique within your org.

**Type**
dateTime


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
The most granular setting is milliseconds.

```
EventIdentifier

EventName

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Report Anomaly.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

```
Report

Score

SecurityEventData

Summary

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the report for which this anomaly event was detected. If the anomaly resulted
from a user executing an unsaved report, the value of this field is null.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
A number from 0 through 100 that represents the anomaly score for the report execution
or export tracked by this event. The anomaly score indicates how the user’s current report
activity differs from their typical activity. A low score indicates that the current report activity
is similar to the user’s usual activity. A high score indicates that it’s different.

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the report activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time, but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows as a percentage how much a particular feature contributed to this anomaly event.
The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the report anomaly that caused this event.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

**Description**
The ID of the tenant that was targeted in the event.

```
TenantName

UserIdentifier

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time the event was created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityReportAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityReportAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityReportAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityReportAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityReportAnomalyShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecuritySessionHijacking TenantSecuritySessionHijacking

Stores information about session hijacking events as detected by Threat Detection within connected tenants in Security Center. For
[more information, see Threat Detection. This object is available for Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
CurrentIp

CurrentPlatform

CurrentScreen

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the IP address didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousIp` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the platform didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousPlatform` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Description**
The screen of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the screen didn’t contribute to the observed fingerprint deviation, the
value of this field is the same as the `PreviousScreen` field.

```
CurrentUserAgent

CurrentWindow

DetailIdentifier

EventDate

EventIdentifier

```

**Type**
textarea

**Properties**
Nillable

**Description**
The user agent of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the user agent didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousUserAgent` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the observed fingerprint that deviates from the previous fingerprint.
The difference between the current and previous values is one indicator that a session
hijacking attack has occurred. If the window didn’t contribute to the observed fingerprint
deviation, the value of this field is the same as the `PreviousWindow` field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
The most granular setting is milliseconds.

**Type**
string


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

```
EventName

MetricIdentifier

MetricsType

Name

PreviousIp

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Session Hijacking.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the `CurrentIp`
field for the newly observed IP address.


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

```
PreviousPlatform

PreviousScreen

PreviousUserAgent

PreviousWindow

Score

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentPlatform` field for the newly observed platform.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The screen of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentScreen` field for the newly observed screen.

**Type**
textarea

**Properties**
Nillable

**Description**
The user agent of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentUserAgent` field for the newly observed user agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the previous fingerprint. The difference between the current and
previous values is one indicator that a session hijacking attack has occurred. See the
`CurrentWindow` field for the newly observed window.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Description**
Specifies how much the new fingerprint deviates from the previous one. The score is from
6.0 through 21.0. The event exposes five field pairs (such as `CurrentIp` and
`PreviousIp` ) to view the before and after data for browser features that contributed to
this anomaly. See the `SecurityEventData` field for all contributing features in JSON
format. A large deviation score (6.0 or more) between two intra-session fingerprints indicates
that two different browsers are active in the same session. The presence of two active browsers
usually means that session hijacking has occurred.

```
SecurityEventData

Summary

Tenant

TenantName

```

**Type**
textarea

**Properties**
Nillable

**Description**
[The set of browser fingerprint features that triggered this event. See the Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
[documentation for the possible features. For example, a user’s current browser fingerprint](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
diverges from the previously known fingerprint. If Salesforce concludes the user’s session
was hijacked, it fires this event, and the contributing features are captured in this field in
JSON format. Each feature describes a browser fingerprint property, such as the browser user
agent, window, or platform. The data includes the current and previous values for each
feature.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the threat that caused this event. The summary lists the browser fingerprint
features that most contributed to the threat detection, along with their contribution to the
total score.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


### Standard Objects TenantSecurityTenantInfo

**Field** **Details**

**Description**
The name of the tenant that was targeted in the event.

```
UserIdentifier

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecuritySessionHijackingChangeEvent on page 68**
Change events are available for the object.

**TenantSecuritySessionHijackingFeed on page 55**
Feed tracking is available for the object.

**TenantSecuritySessionHijackingHistory on page 63**
History is available for tracked fields of the object.

**TenantSecuritySessionHijackingOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecuritySessionHijackingShare on page 67**
Sharing is available for the object.

### TenantSecurityTenantInfo

Stores information on changes related to the tenant history. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityTenantInfo

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
DetailIdentifier

Instance

MyDomainName

Name

SandboxAlias

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier for this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The instance that the tenant is being hosted on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the domain for this tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which the data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias specified by the user when the user creates a Sandbox.


Standard Objects TenantSecurityTenantInfo

**Field** **Details**

```
SandboxType

Status

Tenant

TenantName

TenantType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type specified by the user when the user creates a Sandbox.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the tenant. For example, active or inactive.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The type of tenant in this org.


### Standard Objects TenantSecurityTransactionPolicyTrend

Usage

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTenantInfoChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityTenantInfoFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityTenantInfoHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityTenantInfoOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityTenantInfoShare on page 67**
Sharing is available for the object.

### TenantSecurityTransactionPolicyTrend

Stores changes to the count of Transaction Security Policies for a connected tenant within Security Center. This object is available for
Security Center subscribers in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`


Standard Objects TenantSecurityTransactionPolicyTrend

**Field** **Details**

**•** `UPDATED`

```
ActionBy

ActionConfig

ActionDate

DetailIdentifier

EventName

MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a JSON description for how a user is alerted to an action on the policy. For example:

**•** `In-app`

**•** `Email`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this change was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event of the corresponding Transaction Security Policy.

**Type**
string


Standard Objects TenantSecurityTransactionPolicyTrend

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

```
MetricsType

Name

Tenant

TenantName

TransactionPolicyState

TransactionPolicyType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The state of the transaction security policy. The possible states are `ENABLED` or `DISABLED` .

**Type**
string


### Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of policy configured. The available types are standard policy or a custom Apex
policy.

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPolicyShare on page 67**
Sharing is available for the object.

### TenantSecurityTrigTransactionSecurityPol

Stores metric details related to Transaction Security Policy triggering events. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
ApexClass

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Description**
The name of the Apex class used to evaluate the policy.

```
ApexIdentifier

ClientIp

DetailIdentifier

FlowIdentifier

FlowName

LoginKey

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Flow used to evaluate the policy.

**Type**
String


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

```
MetricIdentfier

MetricsType

Name

Policy Identifier

PolicyName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy being evaluated.


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

```
PolicyOutcome

PolicyType

RequestIdentifier

RowVersion

SessionKey

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Description**
The ID of the tenant of this triggered the Transaction Security Policy event.

```
TenantName

Timestamp

Triggered Timestamp

Uri

UserIdentifier

Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The access time of Salesforce services in GMT. Milliseconds are the most granular setting.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The time at which the Transaction Security event was generated.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

**Description**
The username of the user who’s using Salesforce services through the UI or the API.

### TenantSecurityTrustedIpRangeTrend

Stores details of changes related to trusted IP ranges in Security Center.This object is available for Security Center subscribers in API
version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime


Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
When this change was made.

```
Description

DetailIdentifier

IpEndAddress

IpRangeIdentifier

IpStartAddress

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A description of the trusted IP range. For example, "Trusting the IP addresses from NA-West
region".

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The end IP address of a trusted IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of a trusted IP range. For example, `10.0.0.0 – 10.255.255.255` .


Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

```
MetricIdentifier

MetricsType

Name

Tenant

TenantName

UsageOptions

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.


### Standard Objects TenantSecurityUserActivity

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTrustedIpRangeTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityTrustedIpRangeTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityTrustedIpRangeTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityTrustedIpRangeTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityTrustedIpRangeTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityUserActivity

Stores details related to how a user interacts with a tenant. Use this object to determine whether to reevaluate a user’s access to your
org for security purposes. You can check whether a user has never logged in, hasn’t been active for 90 days, has a frozen account, or
isn’t using multi-factor authentication. This object is available to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
DetailIdentifier

LastLoginDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TenantSecurityUserActivity

**Field** **Details**

**Description**
The last time the user logged in.

```
MetricIdentifier

MetricsType

Name

Tenant

TenantName

UserCreatedDate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where the user activity happened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TenantSecurityUserActivity

**Field** **Details**

**Description**
The date that the user was created.

```
UserEmail

UserLicense

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserActivityChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityUserActivityFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityUserActivityHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityUserActivityOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityUserActivityShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityUserPerm TenantSecurityUserPerm

Stores information on permissions assigned to a user. Use this object to see which tenants a user is assigned to. This object is available
to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

Context

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken regarding the user’s permission. The options are:

**•** `Added`

**•** `Removed`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the permission action was taken.

**Type**
string


Standard Objects TenantSecurityUserPerm

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile or permission set assigned to the user.

```
ContextType

DetailIdentifier

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Indicates the method through which the permission was granted. The options are:

**•** `Permission Set`

**•** `Profile`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of metric that the assigned permission represents.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.


Standard Objects TenantSecurityUserPerm

**Field** **Details**

```
Tenant

TenantName

UserEmail

UserLicense

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s email address.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserPermChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantUsageEntitlement

**TenantSecurityUserPermFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityUserPermHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityUserPermOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityUserPermShare on page 67**
Sharing is available for the object.

### TenantUsageEntitlement

Represents a data structure that contains information about the features or functionalities that a Salesforce org has access to. This object
is available in API version 28.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AmountUsed

CurrentAmountAllowed

EndDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The quantity of an entitlement that has been used.

**Type**
double

**Properties**
Filter, Sort

**Description**
The amount of an entitlement that a tenant is allowed to use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The end date of the setting, based on license end dates that entitle the org to that setting.


Standard Objects TenantUsageEntitlement

**Field** **Details**

```
Frequency

HasRollover

IsPersistentResource

MasterLabel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How often the tenant's entitlement data is automatically reviewed to see how much of the
entitlement has been used.

Possible values are:

**•** `Daily`

**•** `Fortnightly`

**•** `Monthly`

**•** `Once`

**•** `Quarterly`

**•** `Weekly`

**•** `Yearly`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that a certain amount of a customer's unused entitlements from a set time period
can be added to the next set time period. This field is reserved for future use.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the data that will be saved and available for future use even after closing a
session.

The default value is `false` .

**Type**
string

**Properties**
Group, Nillable


Standard Objects TenantUsageEntitlement

**Field** **Details**

**Description**
The overarching name of an element in your organization. A MasterLabel is visible to
customers.

```
OverageGrace

ResourceGroupKey

Setting

StartDate

UsageDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the Allowed Amount that a customer can use without incurring an
additional charge. The default value is 100% (no overage grace). This field is reserved for
future use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Tracks resource usage across different segments for the same setting. For example, a Messages
entitlement that tracks email messages and SMS messages separately could have one
ResourceGroupKey of SMS and another ResourceGroupKey of Email. In most cases though,
TenantUsageEntitlements are configured for the org and not by segment.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A rule or attribute that can be used to configure the appearance or actions in an organization.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
This date is the earliest start date of any license contributing to the provisioning aggregation
output.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects Territory

**Field** **Details**

**Description**
The date an event occurred that deducted from the tenant's entitlement.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantUsageEntitlementChangeEvent on page 68**
Change events are available for the object.

**TenantUsageEntitlementFeed on page 55**
Feed tracking is available for the object.

**TenantUsageEntitlementHistory on page 63**
History is available for tracked fields of the object.

**TenantUsageEntitlementOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantUsageEntitlementShare on page 67**
Sharing is available for the object.

### Territory

Represents a flexible collection of accounts and users where the users have at least read access to the accounts, regardless of who owns
the accounts. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Standard and partner users can access this object. Users assigned to the Manage Territories permission set can edit this object.

Fields

**Field** **Details**

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects Territory

**Field** **Details**

**Description**
Account access level granted to users assigned to this territory.

```
CaseAccessLevel

ContactAccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Case access level granted to users assigned to this territory.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
A value that represents the type of access granted to the target Group, UserRole, or
User for any associated contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: When `DefaultContactAccess` is set to “Controlled by Parent,”
you can’t create or update this field.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the territory that is 1,000 characters or less.

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
Corresponds to **Territory Name** in the user interface.


Standard Objects Territory

**Field** **Details**

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
ForecastUserId

MayForecastManagerShare

Name

OpportunityAccessLevel

ParentTerritoryID

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Forecast Manager, who is the user to whom forecasts from this territory’s
child territories roll up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecast manager can manually share their own forecast.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A name for the territory. Limit is 80 characters. Corresponds to **Label** on the user
interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Opportunity access level granted to users assigned to this territory.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Territory immediately above this territory in the territory hierarchy. Label is **Parent**
**Territory ID** .


### Standard Objects TerritoryMgmtObjectConfig

**Field** **Details**

```
RestrictOppTransfer

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the opportunities associated with this territory are kept within the
bounds of this territory and this territory’s children when account assignment rules
are run ( `true` ), or if opportunities associated with this territory can be assigned to
other nodes of the territory hierarchy when account assignment rules are run ( `false` ).
Label is **Confine Opportunity Assignment** .

Use the Territory object to query your organization’s territory hierarchy. Use it to obtain valid territory IDs when querying or modifying
records associated with territories.

SEE ALSO:

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem

UserTerritory

### TerritoryMgmtObjectConfig

Represents territory management settings and defaults for a particular object. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only standard and partner users can access this object.

Fields

**Field** **Details**

```
DefaultAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects TerritoryMgmtObjectConfig

**Field** **Details**

**Description**
The default access level of the defined object for all territories.

```
DeveloperName

Language

MasterLabel

Object

State

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org where the territory model was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The readable label for this entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The name of the Enterprise Territory Management object.

Possible values are:

**•** `Lead`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the supported object.


### Standard Objects Territory2 Territory2

Represents a sales territory. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
AccountAccessLevel

CaseAccessLevel

ContactAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default account record access levels for users that are assigned
to the territory. Values are:

**•** `Read Only`

**•** `Read/Write`

**•** `Owner`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default case record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
picklist


Standard Objects Territory2

**Field Name** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the default contact record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

```
Description

DeveloperName

ForecastUserId

Name

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the territory. The field label in the user interface is `Territory`
`Description` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of a territory’s forecast manager. To select a
`ForecastUserId`, select someone in the list of users assigned to the territory.

**Type**
string


Standard Objects Territory2

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the territory. The field label in the user interface is `Territory`
`Label` .

```
OpportunityAccessLevel

ParentTerritory2Id

Territory2ModelId

Territory2TypeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default opportunity record access levels for users that are assigned
to the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory’s parent territory (if any). If the territory has no parent
territory, this value is `null` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory model that the territory belongs to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the territory type that the territory belongs to.


### Standard Objects Territory2AlignmentLog Territory2AlignmentLog

Represents the start and end status of a territory assignment rule run job. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users can’t view territory models in other states (such as `Planning`
or `Archived` ).

Fields

**Field** **Details**

```
EndTime

Filter

RunAsId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the assignment rule run job finished.

**Type**
textarea

**Properties**
Nillable

**Description**
Criteria to filter the rule jobs. For example, {RULE_LAST_MOD_DATE_FORM=2021-08-31,
RULE_LAST_MOD_DATE_TO=2021-09-15}.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Salesforce user who started the assignment rule run job.

This is a relationship field.


Standard Objects Territory2AlignmentLog

**Field** **Details**

**Relationship Name**
RunAs

**Relationship Type**
Lookup

**Refers To**
User

```
StartTime

Status

Territory2Id

Territory2ModelId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user started the assignment rule run job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the assignment rule run job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory for which the assignment rule run was performed. If the assignment
rule run was for the territory model, this value is null.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects Territory2Model

**Field** **Details**

**Description**
The ID of the territory model for which the assignment rule run was performed.

This is a relationship field.

**Relationship Name**
### Territory2Model

**Relationship Type**
Lookup

**Refers To**
### Territory2Model

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**Territory2AlignmentLogChangeEvent**

Change events are available for the object.

### Territory2Model

Represents a territory model. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
ActivatedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Territory2Model

**Field Name** **Details**

**Description**
The date when the territory model was activated.

```
DeactivatedDate

Description

DeveloperName

LastOppTerrAssignEndDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory model was archived.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory model.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Model Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. The date when the opportunity territory assignment filter was last
run. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15
/ API version 33).


### Standard Objects Territory2ModelHistory

**Field Name** **Details**

```
LastRunRulesEndDate

Name

State

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the last rules run was completed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory model name. The field label in the user interface is `Label` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The state of the territory model. Values are: `Planning`, `Activating`,
`Activation Failed`, `Active`, `Archiving`, `Archiving Failed`,
`Archived`, `Deleting`, and `Deletion Failed` .

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**Territory2ModelChangeEvent (API version 62.0)**
Change events are available for the object.

**Territory2ModelFeed**

Feed tracking is available for the object.

### **Territory2ModelHistory**

History is available for tracked fields of the object.

### Territory2ModelHistory

Represents the history of changes to the values in the fields on a territory model. Available if Sales Territories has been enabled.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects Territory2ModelHistory

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

Territory2ModelId

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
The name of the field whose value was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the territory model whose history is tracked.


### Standard Objects Territory2ObjectExclusion

Usage

This object is automatically generated whenever any field value changes on a territory model record. Use this object it to identify those
changes.

### Territory2ObjectExclusion

Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This object
is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your org’s sharing settings. Users can’t view territory models in other states (such as `Planning`
or `Archived` ).

Fields

**Field** **Details**

```
Note

ObjectId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Account object to exclude from the territory assignment rule.

This is a polymorphic relationship field.

**Relationship Name**
Object

**Relationship Type**
Lookup


### Standard Objects Territory2ObjSharingConfig

**Field** **Details**

**Refers To**
Account

```
Territory2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory to exclude from the territory model assignment rule.

This is a relationship field.

**Relationship Name**
### Territory2

**Relationship Type**
Lookup

**Refers To**
### Territory2

### Territory2ObjSharingConfig

Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

Only standard and partner users can access this object. Any standard or partner user can view object sharing configuration records in
an active model. Users without the Manage Territories permission can’t view territory records in the `Planning` or `Archived` state.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The access level of the object for the particular territory.


### Standard Objects Territory2Type

**Field** **Details**

```
Territory2Id

TerritoryMgmtObjectConfigId

### Territory2Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The territory on which the access level is defined.

This field is a relationship field.

**Relationship Name**
### Territory2

**Relationship Type**
Lookup

**Refers To**
### Territory2

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The object configuration record the territory access level is related to.

This field is a relationship field.

**Relationship Name**
TerritoryMgmtObjectConfig

**Relationship Type**
Lookup

**Refers To**
TerritoryMgmtObjectConfig

Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has been
enabled for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object.


Standard Objects Territory2Type

Fields

**Field Name** **Details**

```
Description

DeveloperName

Language

MasterLabel

Priority

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Type Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the label in the user interface.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required The user interface label for the territory type.

**Type**
int


### Standard Objects TerritoryAdminAssignment

**Field Name** **Details**

**Properties**
Create, Filter, Group, SortUpdate

**Description**
Required. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring
’15 / API version 33). Lets you specify a priority for a territory type. For opportunity
assignments, the filter examines all territories assigned to the account that the
opportunity is assigned to. The account-assigned territory whose territory type
priority is highest is then assigned to the opportunity. The `priority` field
value on each territory type must be unique. Further, if there are multiple territories
with the same territory type (and therefore the same priority) assigned to the
account, no territory is assigned to the opportunity.

### TerritoryAdminAssignment

Represents designated team members who can administer specific territories and their descendants. This object is available in API version
63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To designate team members, assign them the Administer Territory Operations permission.

Fields

**Field** **Details**

```
CanManageHierarchy

CanManageMembers

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user update and delete the territory and its descendants, and create descendants.

The default value is `false` .

**Type**
boolean


Standard Objects TerritoryAdminAssignment

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user assign other team members to the territory and its descendants. Also lets the
user update the user territory association log.

The default value is `false` .

```
CanManageRecordAssociations

Territory2Id

Territory2ModelId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user add and remove assignments for records, author rules, and assign and run rules
for the territory and its descendants.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory you’re letting the user administer. The user can also administer this
territory’s descendants.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory model that includes the territory you’re letting the user administer.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model


### Standard Objects TestSuiteMembership

**Field** **Details**

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the user you’re letting administer the territory and its descendants. Requires that
the user is assigned the Administer Territory Operations permission set.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Refers To**
Group, User

### TestSuiteMembership

Associates an Apex class with an ApexTestSuite. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
ApexClassId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The Apex class whose tests are to be executed.

This is a relationship field.

**Relationship Name**
ApexClass


### Standard Objects ThirdPartyAccountLink

**Field Name** **Description**

**Relationship Type**
Lookup

**Refers To**
ApexClass

```
ApexTestSuiteId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The test suite to which the Apex class is assigned.

This is a relationship field.

**Relationship Name**
ApexTestSuite

**Relationship Type**
Lookup

**Refers To**
ApexTestSuite

Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.

The following SOQL query returns the membership object that relates this Apex class to this test suite.

```
SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'

   AND ApexTestSuiteId = '05FD00000004CDBMA2'

```

SEE ALSO:

ApexTestSuite

### ThirdPartyAccountLink

Represents the list of external users who authenticated using an authentication provider. This object is available in API version 32.0 and
later.

A list of third-party account links is generated when users of an organization authenticate using an external authentication provider. Use
this object to list and revoke a given user's social sign-on connections (such as Facebook [©] ).


Standard Objects ThirdPartyAccountLink

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

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
Handle

IsNotSsoUsable

Provider

RemoteIdentifier

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The username in the third-party system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Sort

**Description**
Support for single sign-on.

If _`true`_, the link can't be used for a single sign-on flow. It's only available OAuth
access and refresh tokens.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The third-party account provider name.

**Type**
string


Standard Objects ThirdPartyAccountLink

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The unique ID for the user in the third-party system.

```
SsoProvider

SsoProviderId

SsoProviderName

ThirdPartyAccountLinkKey

```

**Type**
AuthProvider

**Properties**
Filter, Nillable, Sort

**Description**
The foreign key to the AuthProvider on page 883 of the third-party system.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The ID associated with the `SsoProvider` value.

This is a relationship field.

**Relationship Name**
SsoProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name associated with the AuthProvider of the third-party system, in case
the user has no access to the provider foreign key (the `SsoProvider` value).

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A concatenated string including the organization ID, the `SsoProviderId`
value, the `SsoProvider` value, and the `RemoteIdentifier` value.


Standard Objects ThirdPartyAccountLink

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The Salesforce user associated with this third-party account link.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Admins (with the Manage Users permission) querying this object can see all the links for all users in the organization. Without the Manage
Users permission, users can only retrieve their own links. Users sometimes don't have access to the `SsoProvider` value (the foreign
key). In this case, use the `SsoProviderName` to render the name of the provider for the associated link.

Use the Apex method `Auth.AuthToken.revokeAccess()` to revoke a link. To use this method, the `IsNotSsoUsable`
field must be `false` .

To make the ThirdPartyAccountLink standard object writable for Salesforce admins, contact Salesforce Customer Support. With this
feature, you can easily add or delete third-party account links using the API, but you can’t update existing account links.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `query()` call returns up to 500 rows.
A queryMore() call returns 500 more, up to 2,500 total. No more records are returned after 2,500. To make sure that you don’t miss any
records, issue a `COUNT()` query in a SELECT clause for ThirdPartyAccountLink. This query gives you the total number of records. If there
are more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2000 OFFSET 0

```

Then, run another query with an offset of 2,000.

```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2000 OFFSET 2000

```

Continue to increase the offset by 2,000 until you have results for all records.


### Standard Objects ThreatDetectionFeedback ThreatDetectionFeedback

Represents feedback provided by a user about a Threat Detection event that occurred in your org. The feedback specifies whether the
event was malicious, suspicious, not a threat, or unknown. Each ThreatDetectionFeedback object is associated with one of these Threat
Detection storage events: ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore, or SessionHijackingEventStore.
This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Response

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
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the severity of the threat.

Possible values are:

**•** `Malicious`

**•** `Not a Threat`

**•** `Suspicious`

**•** `Unknown`


Standard Objects ThreatDetectionFeedback

**Field** **Details**

```
ThreatDetectionEventId

ThreatDetectionFeedbackNumber

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the unique ID of one of these associated Threat Detection storage events:

**•** [ApiAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_apianomalyeventstore.htm)

**•** [CredentialStuffingEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_credentialstuffingeventstore.htm)

**•** [ReportAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_reportanomalyeventstore.htm)

**•** [SessionHijackingEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_sessionhijackingeventstore.htm)

For example, `0fjRM000000005p` .

This is a polymorphic relationship field.

**Relationship Name**
ThreatDetectionEvent

**Relationship Type**
Lookup

**Refers To**
ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore,
SessionHijackingEventStore

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number used as the unique name for this object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID. For example, `005000000000123` .

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects TimeSheet

**Field** **Details**

```
Username

```

Associated Object

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the object was
created.

This object has the following associated object. It’s available in the same API version as this object.

**ThreatDetectionFeedbackFeed**

Feed tracking is available for the object.

SEE ALSO:

_Salesforce Help_ [: Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_detection.htm&type=5&language=en_US)

### TimeSheet

Represents a schedule of a service resource’s time in Field Service or Workforce Engagement. This object is available in API v47.0 and
later.

Time sheets are composed of time sheet entries, which typically track individual tasks like travel or asset repair.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects TimeSheet

**Field Name** **Details**

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
`Currency ISO Code` .

```
EndDate

LastReferencedDate

LastViewedDate

OwnerId

ServiceResourceId

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The last day the time sheet covers.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the time sheet.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource whose time is being tracked with the time sheet.


Standard Objects TimeSheet

**Field Name** **Details**

```
StartDate

Status

TimeSheetEntryCount

TimeSheetNumber

TotalDurationInHours

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the time sheet covers.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet. The picklist includes the following values, which
can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The number of related time sheet entries.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the time sheet.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in hours.


### Standard Objects TimeSheetEntry

**Field Name** **Details**

```
TotalDurationInMinutes

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in minutes.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetFeed**

Feed tracking is available for the object.

**TimeSheetHistory**

History is available for tracked fields of the object.

**TimeSheetOwnerSharingRule**

Sharing rules are available for the object.

**TimeSheetShare**

Sharing is available for the object.

### TimeSheetEntry

Represents a span of time that a service resource spends on a field service task. This object is available in API version 47.0 and later.

Time sheets are composed of time sheet entries. Time sheet entries typically track individual tasks like travel or asset repair.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects TimeSheetEntry

Fields

**Field Name** **Details**

```
CurrencyIsoCode

Description

DurationInMinutes

EndTime

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
`Currency ISO Code` .

Time sheet entries inherit their time sheet’s currency code. Updates to a time
sheet’s currency code aren’t reflected in existing time sheet entries’ currency
code.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes on how the time was spent. For example, “This service took longer than
normal because the machine was jammed.”

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Minutes recorded on the time sheet entry.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TimeSheetEntry

**Field Name** **Details**

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

```
LastViewedDate

LocationTimeZone

StartTime

Status

Subject

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the location where the activity occurred.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity began.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet entry. The picklist includes the following values,
which can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
string


Standard Objects TimeSheetEntry

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Activity performed; for example, repair, lunch, or travel.

```
TimeSheetEntryNumber

TimeSheetId

Type

WorkOrderId

WorkOrderLineItemId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the time sheet entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The time sheet associated with the time sheet entry.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of work performed. The picklist includes the following values, which
can be customized:

**•** Direct

**•** Indirect

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order related to the time sheet entry. Work orders are searchable by
their content.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects TimeSlot

**Field Name** **Details**

**Description**
The work order line item related to the time sheet entry. Work order line items
are searchable by their content.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetEntryChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetEntryFeed**

Feed tracking is available for the object.

**TimeSheetEntryHistory**

History is available for tracked fields of the object.

### TimeSlot

Represents a period of time on a specified day of the week during which work can be performed in Field Service, Salesforce Scheduler,
or Workforce Engagement. Operating hours consist of one or more time slots. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DayOfWeek

EndTime

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The day of the week when the time slot takes place.

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot ends.


Standard Objects TimeSlot

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

MaxAppointments

OperatingHoursId

StartTime

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
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of appointments for a single time slot. Available in API version
47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The operating hours that the time slot belongs to. An operating hours’ time slots
appear in the Operating Hours related list.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
time


Standard Objects TimeSlot

**Field Name** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot starts.

```
RecordSetFilterCriteriaId

TimeSlotNumber

Type

WorkTypeGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria selected for the time slot.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the time slot. The name is auto-populated to a day and time
format—for example, `Monday 9:00 AM - 10:00 PM` —but you can
manually update it if you wish.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are _`Normal`_ and _`Extended`_ . You may
choose to use _`Extended`_ to represent overtime shifts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects TimeSlotHistory

**Field Name** **Details**

**Description**
Work type group assigned to the time slot. Available in API version 47.0 and later.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

Usage

Operating hours are composed of time slots, which indicate the hours of operation for a particular day. After you create operating hours,
create time slots for each day. For example, if the operating hours should be 8 AM to 5 PM Monday through Friday, create five time slots,
one per day. To reflect breaks such as lunch hours, create multiple time slots in a day: for example, _`Monday 8:00 AM – 12:00`_
_`PM`_ and _`Monday 1:00 PM – 5:00 PM`_ .

Tip: Time slots don’t come with any built-in rules, but you can create Apex triggers that limit time slot settings in your org. For
example, you may want to restrict the start and end times on time slots to half-hour increments, or to prohibit end times later
than 8 PM.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[TimeSlotChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **TimeSlotHistory (API version 62.0)**

History is available for tracked fields of the object.

### TimeSlotHistory

Represents the history of changes made to tracked fields on a time slot. This object is available in API version 38.0 and later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for time slot fields must be configured.


### Standard Objects TodayGoal

Fields

**Field Name** **Details**

```
Field

NewValue

OldValue

TimeSlotId

### TodayGoal

```

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
ID of the time slot being tracked. The history is displayed on the detail page for
this record.

Sets the quarterly sales goal on the performance chart. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects TodayGoal

Fields

**Field** **Details**

```
IsLocked

MayEdit

Name

OwnerId

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the goal is locked, or `false` if it’s not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the goal can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the goal.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the creator of the goal.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects Topic

**Field** **Details**

**Description**
The ID of the user of the goal.

This field is unique within your organization.

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

```
Value

```

Usage

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The customizable sales goal for the quarter.

This object is specific to the performance chart and has no impact on forecast quotas or any other type of goal. The performance chart
is available on the home page when Seller Home is not enabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TodayGoalChangeEvent on page 68**
Change events are available for the object.

**TodayGoalShare on page 67**
Sharing is available for the object.

### Topic

Represents a topic on a Chatter post or record. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`


Standard Objects Topic

Fields

**Field Name** **Details**

```
Description

ManagedTopicType

Name

NetworkId

TalkingAbout

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of managed topic. Values are:

**•** `Content`

**•** `Featured`

**•** `Navigational`

This field is available in API version 44.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

Note: You can change only the spacing and capitalization of a topic
name with the update property.

**Description**
Name of the topic.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort

**Description**
Identifier of the Experience Cloud site to which the topic belongs. This field is
available only if digital experiences is enabled in your org.

**Type**
int

**Properties**
Filter, Group, Sort


### Standard Objects TopicAssignment

**Field Name** **Details**

**Description**
Number of people talking about the topic over the last two months, based on
factors such as topic additions and comments on posts with the topic.

Usage

Use this object to query a specific topic or to get a list of all topics, even those used solely in private groups and on records, and the
number of people talking about them.

Use this object to create, edit, or delete topics. To create a topic, you must have the Create Topics permission. To edit a topic, you must
have the Edit Topics permission. To delete a topic, you must have the Delete Topics or Modify All Data permission.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TopicFeed (API version 29.0)**
Feed tracking is available for the object.

### TopicAssignment

Represents the assignment of a topic to a specific feed item, record, or file. This object is available in API version 28.0 and later.

Administrators must enable topics for objects before users can add topics to records of that object type. Topics for most objects are
available in API version 30.0 and later. Topics for ContentDocument are available in API version 37.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `delete()`, `getDeleted()`, `getUpdate()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EntityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the feed item, record, or file.

This is a polymorphic relationship field.

**Relationship Name**
Entity


Standard Objects TopicAssignment

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Asset, Campaign, Case, Contact, ContentDocument, Contract, Event,
FeedItem, Lead, Opportunity, Order, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shift, Shipment, Solution, Task, WorkOrder,
WorkOrderLineItem

```
EntityKeyPrefix

EntityType

NetworkId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The first three digits of the `EntityID` field, which identify the object type
(account, opportunity, etc). This read-only field is available in API version 32.0
and later.

Interface label is “Record Key Prefix,” which appears only in reports.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The standard name for the object type (account, opportunity, etc). This read-only
field is available in API version 33.0 and later.

Note: Querying topic assignments for the ManagedContentVersion entity
type isn’t supported.

Interface label is “Object Type,” which appears only in reports.

Tip: In most cases, you should use this field rather than
`EntityKeyPrefix`, which exists primarily to support older reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the TopicAssignment belongs. This field is
available only if digital experiences is enabled in your org.


### Standard Objects TopicLocalization

**Field Name** **Details**

```
TopicId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the topic.

This is a relationship field.

**Relationship Name**
### Topic

**Relationship Type**
Lookup

**Refers To**
### Topic

Use this object to query the assignments of topics to feed items, records, or files. To assign or remove topics, you must have the “Assign
Topics” permission.

In SOQL `SELECT` syntax, this object supports nested semi-joins, allowing queries on Knowledge articles assigned to specific topics.
For example:

```
SELECT parentId FROM KnowledgeArticleViewStat

   WHERE parentId in (SELECT KnowledgeArticleId FROM KnowledgeArticleVersion

   WHERE publishStatus = 'Online' AND language = 'en_US'

   AND Id in (select EntityId from TopicAssignment where TopicId ='0T0xx0000000xxx'))

```

There is no SOQL limit if the logged-in user has the “View All Data” permission. If they do have that permission, do one of the following:

**•** Specify a LIMIT clause of 1,100 records or fewer.

**•** Filter on `Id` or `Entity` when using a `WHERE` clause with "=".

Important: Deleting this object's records removes all its data. This action is irreversible.

Note: When you create a report type on the TopicAssignment object, all queries are generated in SQL, which does not enforce
the 1,100 record limit clause.

SEE ALSO:

### Topic

FeedItem

### TopicLocalization

Represents the translated version of a topic name. Topic localization applies only to navigational and featured topics in Experience Cloud
sites. This object is available in API version 33.0 and later.


Standard Objects TopicLocalization

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Users with the Translation Workbench enabled can view topic translations, but the Customize Application, Manage Translation, or
Manage Categories permission is required to create or update them.

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
The combined language and locale ISO code, which controls the language for
labels displayed in an application. (The values in this field are not related to the
default locale selection.)

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


Standard Objects TopicLocalization

**Field Name** **Details**

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

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


Standard Objects TopicLocalization

**Field Name** **Details**

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


Standard Objects TopicLocalization

**Field Name** **Details**

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


Standard Objects TopicLocalization

**Field Name** **Details**

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

```
NamespacePrefix

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


### Standard Objects TopicUserEvent

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

### TopicUserEvent

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID that identifies the topic. After a TopicLocalization record is created, this ID can’t
be modified.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the topic name. Label is **Topic Name Translation** .

Represents an action (such as comment, post, like, or share) made by a user on a topic. This object is available in API version 42.0 and
later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with the Modify All Data permission can view and delete these data.


Standard Objects TopicUserEvent

Fields

**Field** **Details**

```
ActionEnum

NetworkId

TopicId

UserId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action taken by a user on a topic. The possible values are:

**•** LIKE

**•** COMMENT

**•** POST

**•** ASSIGN

**•** SHARE

**•** FAVORITE

**•** UNFAVORITE

**•** AT_MENTION

**•** BANG_MENTION

**•** COMMENT_LIKE

**•** USER_ENDORSEMENT

**•** SKILL_PEER_ENDORSEMENT

**•** SKILL_SELF_ENDORSEMENT

**•** BEST_ANSWER

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site where the action was performed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifier of the topic.

**Type**
reference


### Standard Objects TopInsight

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Unique Salesforce user ID.

Usage

Use the TopicUserEvent object to delete topic-related activities by Experience Cloud site users who would like all their topic-related
activities to be removed from a site.

### TopInsight

For internal use only.

### TransactionSecurityPolicy

Represents a transaction security policy definition.

This object is available in API version 42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionConfig

ApexPolicyId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Describes the action to take when the matching Transaction Security policy is triggered. Also
indicates the type of notifications selected and the ID of the intended recipient. The recipient
must be active and assigned the Modify All Data and View Setup user permissions. Multiple
actions can be taken. The actions available depend on the `Event Type` field.

**Type**
reference


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Apex `TxnSecurity.PolicyCondition` or
`TxnSecurity.EventCondition` interface for this policy.

```
BlockMessage

CustomEmailContent

Description

```

**Type**
string

**Properties**
Create,Filter, Nillable, Sort, Update

**Description**
The custom message sent to a user when a policy blocks their action. Used in Real-Time
Event Monitoring only. Maximum of 1000 characters. This field is null when the default
message option is selected in the UI. Available only when `EventName` is set to `ApiEvent`,
`ListViewEvent`, `BulkApiResultEventStore`, or `ReportEvent` . Available
in API version 49.0 and later.

Include org- or policy-specific information in your custom message, such as the name of the
responsible administrator or the business unit. Be careful about what you include. Too much
information on how the policy was designed. can aid a malicious user.

Two-factor authentication (2FA) isn’t supported in Lightning Experience, so events like
`ListView` and `ReportEvent` are upgraded to Block in Lightning.

Custom messages aren’t translatable.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
