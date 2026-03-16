BundleAggregationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ApptBundleAggrDurDnscale

**Field** **Details**

**Description**
The ID of the parent appointment bundle aggregation policy.

This is a relationship field.

**Relationship Name**
BundleAggregationPolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundleAggrPolicy

```
FromBundleMemberNumber

LastReferencedDate

LastViewedDate

MaxReduction

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the first bundle member to which the downscale is applied.

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
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum reduction that can be applied to a bundle member.


### Standard Objects ApptBundleAggrPolicy

**Field** **Details**

```
Name

PercentageOfReduction

ToBundleMemberNumber

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle aggregation downscale policy.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The percentage of duration reduction.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the last bundle member to which the downscale is applied.

### ApptBundleAggrPolicy

Policy that defines how the property values of the bundle members are aggregated and assigned to the bundle. This object is available
in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.


Standard Objects ApptBundleAggrPolicy

Fields

**Field** **Details**

```
AggregationAction

AggregationFieldType

AggregationOrder

BundleFieldName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The aggregation action to be performed.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The target field type in the bundle to which the aggregation is directed.

Possible values are:

**•** `Boolean`

**•** `Date`

**•** `Numeric`

**•** `Picklist`

**•** `Picklist-Multi`

**•** `Skills`

**•** `String`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order the aggregation is triggered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle where the value is taken from the bundle member.

Possible values are: All default and custom Service Appointment fields.


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

```
BundleMemberAddiFieldName

BundleMemberFieldName

BundlePolicyId

ConstantValue

DateValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of an additional source field that is connected to the initial source field in the bundle
member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value that is used in the aggregation.

**Type**
picklist


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value will be determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

```
DoesAllowDuplicateStrings

DownscaleSortDirection

FilterCriteriaId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to allow the same string to appear more than once when using the
'Sum based on Bundle Members' action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Applies only if the Set Downscaled Duration action is set. The downscaling sorting direction
of the bundle member service appointments, according to their duration.

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for aggregating the bundle members.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

**Refers To**
RecordsetFilterCriteria

```
LastReferencedDate

LastViewedDate

MaxBundleDuration

Name

ShouldUpdateOnCreationOnly

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
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum bundle duration that can be accumulated from the bundle members (after
downscaling).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle aggregation policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to update the field in the bundle only when it is created.


### Standard Objects ApptBundleConfig ApptBundleConfig

Represents the general parameters that define the behavior of the bundle. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
AddToBundleStatuses

BundleStatusesToPropagate

```

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointment that are allowed to be bundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update


Standard Objects ApptBundleConfig

**Field** **Details**

**Description**
The bundle statuses that when updated are inherited by the bundle members.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
CriteriaForAutoUnbundlingId

DoesAddTravelTime

DoesDeleteEmptyBundles

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The criteria that causes a bundle service appointment to be unbundled.

This is a relationship field.

**Relationship Name**
CriteriaForAutoUnbundling

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If the bundle members aren’t in the same location, add travel time between them to the
bundle’s duration according to their sort order. The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ApptBundleConfig

**Field** **Details**

**Description**
If the bundle has no remaining bundle members, the bundle is deleted.

```
EmptyBundleStatus

LastReferencedDate

LastViewedDate

MemberStatusesNotToPropagate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status from the Canceled category that a bundle service appointment changes to if it
has no remaining bundle members, but still appears in the appointment list.

Possible values are determined by the org’s statuses.

The default value is None.

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
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The bundle member statuses that aren’t overridden when the bundle's status is updated.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`


Standard Objects ApptBundleConfig

**Field** **Details**

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
Name

OwnerId

RemoveFromBundleStatuses

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Appointment Bundle Config.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointments that are allowed to be removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`


Standard Objects ApptBundleConfig

**Field** **Details**

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
StatusOnRemovalFromBundle

StatusesNotToUpdateOnUnbundle

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status that a service appointment is given when it’s removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses that aren’t updated when a bundle is unbundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`


### Standard Objects ApptBundlePolicy

**Field** **Details**

**•** `Scheduled`

The default value is None.

### ApptBundlePolicy

Policy that defines how the bundling of service appointments should be handled. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundleEndTimeFieldName

BundleStartTimeFieldName

CanAllowSchleDepndInBundle

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the end time of the bundle.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the start time of the bundle.

**Type**
boolean


Standard Objects ApptBundlePolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is reserved for future use.

```
ConstantTimeValue

FilterCriteriaId

IsAutomaticBundling

IsManualBundling

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the total time of the bundle
as a preset constant value.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for the bundle members. Only service appointments
that meet the criteria can be bundled.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for automatic bundling.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for manual bundling.


Standard Objects ApptBundlePolicy

**Field** **Details**

The default value is ‘false’.

```
IsTimeCalcByBundleDurationFld

LastReferencedDate

LastViewedDate

LimitAmountOfBundleMembers

LimitDurationOfBundle

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the bundle’s duration is validated. If true, the bundle’s start time is subtracted
from the bundle’s end time. If the result is a negative value, it uses ConstantTimeValue as
the bundle’s duration.

The default value is ‘false’.

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
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of bundle members that can be included in a bundle.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum duration of a bundle.


### Standard Objects ApptBundlePolicySvcTerr

**Field** **Details**

```
Name

OwnerId

Priority

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the bundle policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
The priority level that this bundle policy should be given when the bundle policies are
analyzed using the automatic mode.

### ApptBundlePolicySvcTerr

Represents a link between the BundlePolicy and the ServiceTerritory. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ApptBundlePolicySvcTerr

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

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
string


### Standard Objects ApptBundlePropagatePolicy

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle service territory.

```
ServiceTerritoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

### ApptBundlePropagatePolicy

Policy that defines which property values are inherited from the bundle to the bundle members or are assigned as constant values in
the bundle members. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.


Standard Objects ApptBundlePropagatePolicy

Fields

**Field** **Details**

```
AdditionalConstantValue

BundleFieldName

BundleMemberFieldName

BundlePolicyId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The additional constant value that is connected to the initial constant value to be added to
the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle member where the value is inherited from the bundle.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This field is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ApptBundlePropagatePolicy

**Field** **Details**

```
ConstantValue

DateValue

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value to be added to the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value is determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects ApptBundleRestrictPolicy

**Field** **Details**

**Description**
The name of the appointment bundle propagation policy.

```
ShouldAddConstantValue

ShouldUpdateOnAdd

ShouldUpdateOnRemove

ShouldUpdateOnUnbundle

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable adding a constant value to the bundle members.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
added to the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
removed from the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when performing
the Unbundle action.

### ApptBundleRestrictPolicy

Policy that defines the restrictions that are considered while forming a bundle. This object is available in API version 54.0 and later.


Standard Objects ApptBundleRestrictPolicy

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

DoesAllowEmpty

DoesRestrictAutomaticMode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows a bundle member service appointment with an empty Restriction Field Name to be
bundled.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the automatic mode.


Standard Objects ApptBundleRestrictPolicy

**Field** **Details**

```
DoesRestrictManualMode

IsRestrictByDateOnly

LastReferencedDate

LastViewedDate

Name

RestrictionFieldName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the manual mode.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want the bundle to be restricted according to the calendar date only, ignoring
the time of day.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle restriction policy.

**Type**
picklist


### Standard Objects ApptBundleSortPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for applying the restriction.

Possible values are: All default and custom Service Appointment fields.

### ApptBundleSortPolicy

Policy that defines the properties by which the bundle members are sorted within the bundle. Can also be used in the automatic mode
for determining the order of the automatic selection of bundle members. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ApptBundleSortPolicy

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

SortDirection

SortFieldName

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
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the appointment bundle sort policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The order of the appointments in a bundle

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for sorting the bundle members.

Possible values are: All default and custom Service Appointment fields.


### Standard Objects AppUsageAssignment

**Field** **Details**

```
SortOrder

SortType

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order of fields used for sorting the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The applied sort type for arranging the bundle. Sort for Automatic Bundling defines the order
that automated bundling uses to examine the candidate service appointments to be bundled.
Sort Within a Bundle defines the order of bundle members. It’s also used when you unbundle
to define the order that the service appointments are scheduled on the Gantt.

Possible values are:

**•** `SortForAutomaticBundling` —Sort For Automatic Bundling

**•** `SortWithinaBundle` —Sort Within a Bundle

### AppUsageAssignment

Provides application context for a record. A record can have different allowed actions or different related objects when it’s created for
different applications. For example, a Revenue Lifecycle Management order has a related `RevenueLifecycleManagement`
### AppUsageAssignment, so Salesforce knows it can create assets for that order. Available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppUsageType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort


### Standard Objects ArchiveActivity

**Field** **Details**

**Description**
The application context for the record. Allowed values are determined by the available
licenses. For example, the `RevenueLifecycleManagement` and `BuyNow`
AppUsageTypes are available with the Subscription Management license.

```
Name

RecordId

### ArchiveActivity

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Autogenerated name for the AppUsageAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the AppUsageAssignment provides context for. For example, the order
record.

This is a relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**

**•** Order in API version 58.0 and later

**•** Asset, Contract, Quote in API version 59.0 and later

**•** WebCart in API version 60.0 and later

**•** OrderSummary in API version 61.0 and later

Represents metadata retrieved for a single Archive process initiated by an action. Retrieved metadata can include status tracking, start
and end times, record counts, and monitoring and auditing outcomes. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ArchiveActivity

Special Access Rules

This object is Read-Only and can't be deleted. Storage consumed by this object doesn't count toward your org's data storage limits.

Fields

**Field** **Details**

```
ArchivePolicyId

AttemptedRootRecordsCount

EndTime

FailedCount

FailureReason

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated policy that triggered the process. Links each execution back to its
configuration.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of root records that the action tried to process. Excludes records that were
filtered out before processing began.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the process executed successfully, or was terminated due to error.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of records that failed to process due to errors such as validation failures, missing
references, or system exceptions.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ArchiveActivity

**Field** **Details**

**Description**
Description of why process failed or only partially completed. Can include system error
messages or policy-level failures.

```
Name

ProgressPercentage

RecordsSizeInMb

SkippedRootRecordsCount

StartTime

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The autogenerated name of the action instance.

**Type**
double

**Properties**
Filter, Sort

**Description**
The percentage of records that were successfully processed.

**Type**
double

**Properties**
Filter, Sort

**Description**
Estimated total size, in megabytes (MB), of the records processed during an action, including
metadata and payload.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of root records skipped due to validation errors, exclusion filters, or data
protection thresholds.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the action started.


Standard Objects ArchiveActivity

**Field** **Details**

```
Status

SucceededCount

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Status of the current activity.

Valid values are:

**•** `Aborted` —Policy manually aborted during policy run.

**•** `Aborting` - `Aborted` process has started.

**•** `Archive Timeout` —Process automatically stopped because it took too long to execute
a specific task, or the entire run.

**•** `Completed` —Process completed successfully, and all records were processed.

**•** `Ended with Delete Failures` —Process finished its run, but failed to delete one
or more designated items.

**•** `Ended With Errors` —Process finished successfully, but some records weren't
processed. A CSV of the failed records can be downloaded from the Execution Details page.

**•** `Failed` —Process failed, and no records were archived. A CSV of the failed records is
available on the Activities tab.

**•** `No Records` —Process ran successfully but found no records matching the policy criteria.

**•** `Pending` —Process is in a queue waiting to be executed.

**•** `Process Exceeds 23h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run daily, this status indicates partial success before exceeding
the time limit.

**•** `Process Exceeds 120h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run one time in a five-day period, this status indicates partial
success before exceeding the time limit.

**•** `Process Exceeds 168h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run weekly, this status indicates partial success before exceeding
the time limit.

**•** `Query Timeout` —Process stopped because database query took too long to execute.

**•** `Running` —Process is actively executing its tasks.

**•** `Started` —Process has been initiated and is currently in progress.

**•** `Too Many Failures` —Process was abandoned after too many records failed to read
or delete.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of records processed successfully.


Standard Objects ArchiveActivity

**Field** **Details**

```
TotalRecordCount

Type

```

**Type**
int

**Properties**
Filter, Sort

**Description**
The total number of records initially selected for processing, including successful, failed, and
skipped records.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Specifies the type of archive process to be executed. This static enum categorizes the purpose
or mode of the run.

Valid values are:

**•** `Analyzer`

**•** `Archive`

**•** `Archive-fail-to-delete`

**•** `Estimate`

**•** `Export`

**•** `Export-and-download`

**•** `Export-to-external-bucket`

**•** `Import-data-archive`

**•** `Import-data-load`

**•** `Index-request`

**•** `None`

**•** `Purge`

**•** `Purge-by-retention`

**•** `Purge-estimation`

**•** `RTBF-SDK`

**•** `Unarchive`

**•** `Unarchive-retry`

**•** `Unarchive-sdk`


### Standard Objects ArchivePolicyDefinition ArchivePolicyDefinition

Represents a data lifecycle policy that, in each row, defines the scope, frequency, and rules for automated archiving or purging of records
from a root entity, such as Contact or Lead. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Create, Update, and Delete operations are restricted to the Archive Admin profile. All other profiles have Read-Only access.

Fields

**Field** **Details**

```
DataProtectionThreshold

Description

IsActive

Name

```

**Type**
int

**Properties**
Create, Filter, Sort, Update

**Description**
Specifies a retention buffer, in days, during which recently updated or sensitive records must
not be archived or deleted. Enforces data protection compliance.

**Type**
textarea

**Properties**
Create, Update

**Description**
The purpose or scope of the policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the policy is active and eligible for execution. Only active policies can be
executed by scheduled or manual processes.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ArchivePolicyDefinition

**Field** **Details**

**Description**
The unique name assigned to the policy.

```
Type

Query

QueryLimit

RootEntityName

RunFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Process type that the policy executes.

Valid values are:

**•** `Archive`

**•** `Import`

**•** `Purge`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A complete SOQL or custom query defining the set of records to archive or purge, based on
policy rules. Determines which records are eligible for processing.

**Type**
int

**Properties**
Create, Filter, Sort, Update

**Description**
The maximum number of root records this policy can process in a single run. Used to throttle
execution for scalability and control.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the Salesforce object targeted by the policy. Determines which object’s
records are queried and processed.

**Type**
picklist


### Standard Objects Article Type __DataCategorySelection

__DataCategorySelection

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies how often the policy is executed—manually or on a regular interval. Enables
automation for recurring data lifecycle operations.

Valid values are:

**•** `None`

This option is specifically for manual policy runs.

**•** `Daily`

**•** `Weekly`

**•** `Monthly`

### Article Type __DataCategorySelection __DataCategorySelection

A data category selection represents a data category that classifies an article. This object is available in API version 19.0 and later.

This object can be used to associate an article with data categories from a data category group or to query the category selections for
an article.

### The object name is variable and has a syntax of Article Type __DataCategorySelection, where Article Type is the Object

`Name` for the article type associated with the article. For example, `Offer__DataCategorySelection` represents the association
between the `Offer` article type and its data categories. Every article is associated with an article type.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `getDeleted()`, `retrieve()`

Special Access Rules

Knowledge must be enabled in your org. Not available in Lightning Knowledge. Users can only access, create or delete data category
selection visible to their role, permission set, or profile. If a user has partial visibility on an article's categorization, only the visible categories
are returned.

Fields

**Field Name** **Details**

```
DataCategoryGroupName

```

**Type**

DataCategoryGroupReference

**Properties**
Create


Standard Objects Article Type __DataCategorySelection
__DataCategorySelection

**Field Name** **Details**

**Description**
Unique name of the data category group which has categories associated with the article.

```
DataCategoryName

ParentId

```

Usage

**Type**

DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the article associated with the data category selection.

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use the _`Article Type`_ __DataCategorySelection object to query and manage article categorization in
your org. Client applications can create a categorization for an article with a Draft status. They can also delete and query article
categorizations.

Note: When using _`Article Type`_ __DataCategorySelection to classify an article, you can't select both a category (for example
USA) and one of its descendants (California) or ascendant categories (North America). In this case, only the first category is selected.

Answers zones use QuestionDataCategorySelection to classify questions.

SOQL Sample

The following SOQL query returns the data category selections used to classify the article whose ID is `ka0D000000005ApIAI` .

```
SELECT Id,DataCategoryName, ParentId

     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```

This clause only returns category unique names. To retrieve category labels use the following clause:

```
SELECT Id,toLabel(DataCategoryName), ParentId

     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```

Tip: You can also use relationship queries to retrieve categorizations from an article type.

SEE ALSO:

QuestionDataCategorySelection


### Standard Objects Asset Asset

Represents an item of commercial value, such as a product sold by your company or a competitor, that a customer has purchased.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

Address

### `AssetLevel`

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Required) ID of the Account associated with this asset. Must be a valid account ID. Required
if `ContactId` isn’t specified.

This field is a relationship field.

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
Represents the physical address or geolocation of the asset.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset’s position in an asset hierarchy. If the asset has no parent or child assets, its level
is 1. Assets that belong to a hierarchy have a level of 1 for the root asset, 2 for the child assets
of the root asset, 3 for their children, and so forth. On assets created before the introduction


Standard Objects Asset

**Field** **Details**

of this field, the asset level defaults to –1. After the asset record is updated, the asset level is
calculated and automatically updated.

```
AssetProvidedById

AssetServicedById

AssetTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account that provided the asset, typically a manufacturer.

This field is a relationship field.

**Relationship Name**
AssetProvidedBy

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account in charge of servicing the asset.

This field is a relationship field.

**Relationship Name**
AssetServicedBy

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset type associated with the asset.

This field is a relationship field.

This field is available in API version 62.0 and later for users with the Health Cloud Appointment
Management permission set.


Standard Objects Asset

**Field** **Details**

**Relationship Name**
AssetType

**Relationship Type**
Lookup

**Refers To**
AssetType

```
Availability

AveragetimetoRepair

AveragetimeBetweenFailure

AverageUptimePerDay

City

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of expected uptime where the asset was available for use.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the number of hours it typically takes to repair an asset after a failure.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the number of hours that typically elapses before the asset is likely to fail again.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The average number of hours per day the asset is expected to be available for use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city detail for the address.


Standard Objects Asset

**Field** **Details**

```
ConsequenceOfFailure

ContactId

Country

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business impact associated with the asset’s failure. Using this field, you can address the
[asset’s health and take action using Flows. To enable this field, use Object Manager to update](https://help.salesforce.com/s/articleView?id=platform.flow.htm&type=5&language=en_US)
the field availability. Make sure that the field is visible for field-level security and for page
[layout. To learn more, see What Determines Field Access. The picklist values aren’t predefined](https://help.salesforce.com/s/articleView?id=platform.customize_fieldaccess.htm&type=5&language=en_US)
in orgs created before Winter ’22 that aren’t Field Service enabled. This field is available in
API version 53.0 and later.

Possible values are:

**•** `Insignificant`

**•** `Minor`

**•** `Moderate`

**•** `Major`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if `AccountId` isn’t specified. ID of the Contact associated with this asset. Must
be a valid contact ID that has an account parent (but doesn’t need to match the asset’s
`AccountId` ).

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country detail for the address.


Standard Objects Asset

**Field** **Details**

```
CurrencyIsoCode

CurrentAmount

CurrentLifecycleEndDate

CurrentMrr

CurrentQuantity

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the invoice. The default value is USD.

This field is available in API version 55.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for future use.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the end of the period shown as current. System-populated field inherited from
the end date of the current asset state period. If that field is empty, as with an evergreen
subscription, the Current Lifecycle End Date field is also empty.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The asset’s monthly recurring revenue during the current asset state period. System-populated
field inherited from the monthly recurring revenue on the current asset state period. If no
asset state period is current, the value is `0` . Label is Current Monthly Recurring Revenue.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
double


Standard Objects Asset

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The asset’s quantity during the current asset state period. System-populated field inherited
from the quantity on the current asset state period. If no asset state period is current, the
value is `0` .

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

```
Description

DigitalAssetStatus

ExternalIdentifier

GeocodeAccuracy

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the asset.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of digital tracking of the asset. The default picklist includes the following values:

**•** `On`

**•** `Off`

**•** `Warning`

**•** `Error`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the matching record in an external system. This field is available in API version 49.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address.


Standard Objects Asset

**Field** **Details**

```
HasLifecycleManagement

InstallDate

IsCompetitorProduct

IsInternal

LastReferencedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this asset is a lifecycle-managed asset, otherwise false. You can’t switch an asset to a
lifecycle-managed asset or the reverse. This field is system populated.

The default value is _`false`_ .

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the asset was installed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this Asset represents a product sold by a competitor ( `true` ) or not
( `false` ). The default value is `false` . Its UI label is Competitor Asset.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the asset is produced or used internally ( `true` ) or not ( `false` ). The default
value is `false` . Its UI label is Internal Asset.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. Its UI label is Last Modified Date.


Standard Objects Asset

**Field** **Details**

```
LastViewedDate

Latitude

LifecycleEndDate

LifecycleStartDate

LocationId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
double

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the end of the asset’s lifecycle. System-populated field inherited from the end
date of the final asset state period. If that field is empty, as with an evergreen subscription,
the lifecycle has no end date. This field is available in API version 50.0 and later. This field is
available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the beginning of the asset’s lifecycle. System-populated field inherited from the
start date of the earliest asset state period. This field can’t be edited. When a new asset action
affects the start date of an asset state period, the period is deleted and a new one is generated.
This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset’s location. Typically, this location is the place where the asset is stored, such as a
warehouse or van.


Standard Objects Asset

**Field** **Details**

If you have access to the location entity, it doesn’t necessarily mean you can access the
location id field. To access the location, you must have `userHasLocation` user access.

```
Longitude

ManufactureDate

Name

OwnerId

ParentId

```

**Type**
double

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the asset was manufactured. This field is available from API version 49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
(Required) Name of the asset. Label is Asset Name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The asset’s owner. By default, the asset owner is the user who created the asset record. Its
UI label is Asset Owner.

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


Standard Objects Asset

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset’s parent asset. Its UI label is Parent Asset.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Asset

```
PostalCode

Price

PricingSource

Product2Id

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the address.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Price paid for this asset.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Pricing source to use when amending or renewing an asset.

Valid values are:

**•** `LastTransaction` —Last Transaction

**•** `PriceBookListPrice` —Price Book or List Price

Available in API version 60.0 and later.

**Type**
reference


Standard Objects Asset

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Optional) ID of the Product2 associated with this asset. Must be a valid Product2 ID. Its UI
label is Product.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductCode

ProductDescription

ProductFamily

PurchaseDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product code of the related product.

**Type**
string

**Properties**
Filter, Sort, Nillable

**Description**
The product description of the related product.

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The product family of the related product.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date on which this asset was purchased.


Standard Objects Asset

**Field** **Details**

```
Quantity

QuantityIncreasePricingType

RecordTypeId

Reliability

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity purchased or installed. The Quantity field value isn’t set by Customer Asset Lifecycle
Management. Instead, you can populate the field as you need.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specify which pricing type to use when the quantity of this asset is increased. Its UI label is
Pricing Type for Quantity Increase. This field is available in API version 56.0 and later. This
field is available when Revenue Cloud is enabled.

Possible values are:

**•** `LastNegotiatedPrice` —Available in API version 58.0 and later.

**•** `ListPrice`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier for the asset.

This field is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of expected uptime where the asset wasn’t subject to unplanned downtime.


Standard Objects Asset

**Field** **Details**

```
RenewalPricingType

RenewalTerm

RenewalTermUnit

RootAssetId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The price used when renewing a subscription. Its UI label is Pricing Type for Renewal. This
field is available in API version 55.0 and later. This field is available when Revenue Cloud is
enabled.

Possible values are:

**•** `LastNegotiatedPrice`

**•** `ListPrice`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
With Renewal Term Unit, defines the default subscription term for renewal quotes. This field
is available in API version 55.0 and later. This field is available when Revenue Cloud is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time for a subscription term. This field is available in API version 55.0 and later.
This field is available when Revenue Cloud is enabled.

Possible values are:

**•** `Annual` —Available in API version 58.0 and later. —UI label is `Years` .

**•** `Months`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level asset in an asset hierarchy. Depending on where an asset lies in
the hierarchy, its root could be the same as its parent. Its UI label is Root Asset.

This field is a relationship field.

**Relationship Name**
RootAsset


Standard Objects Asset

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Asset

```
SalesStoreId

SerialNumber

State

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the RetailStore or WebStore associated with this Asset.

This field is a polymorphic relationship field.

To access this field, your org must have a Salesforce Order Management license or a B2B
Commerce License.

This field is available in API v60.0 and later.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
RetailStore, WebStore

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Serial number for this asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state detail for the address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Asset

**Field** **Details**

**Description**
Customizable picklist of values. The default picklist includes the following values:

**•** `Purchased`

**•** `Shipped`

**•** `Installed`

**•** `Registered`

**•** `Obsolete`

```
StatusReason

StockKeepingUnit

Street

SumDowntime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The explanation of the device status. This field is available from API version 49.0 and later.

Possible values are:

**•** `Not Ready`

**•** `Off`

**•** `Offline`

**•** `Online`

**•** `Paused`

**•** `Standby`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SKU assigned to the related product.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street detail for the address.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects Asset

**Field** **Details**

**Description**
Accumulated downtime (planned and unplanned), determined as follows:

**•** When only `UptimeRecordStart` is set, the sum of all downtime from

```
                     UptimeRecordStart

```

**•** When `UptimeRecordStart` and `UptimeRecordEnd` are set, the sum of all
downtime from `UptimeRecordStart` to `UptimeRecordEnd`

Otherwise, downtime isn’t accumulated.

```
SumUnplannedDowntime

TotalLifecycleAmount

UptimeRecordEnd

UptimeRecordStart

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Accumulated unplanned downtime, determined as follows:

**•** When only `UptimeRecordStart` is set, the sum of all unplanned downtime from

```
   UptimeRecordStart

```

**•** When `UptimeRecordStart` and `UptimeRecordEnd` are set, the sum of all
unplanned downtime from `UptimeRecordStart` to `UptimeRecordEnd`

Otherwise, unplanned downtime isn’t accumulated.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of revenue for the asset, including revenue from each stage in the asset
lifecycle. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date until which `SumDowntime` and `SumUnplannedDowntime` are accumulated.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date from which `SumDowntime` and `SumUnplannedDowntime` are accumulated.


Standard Objects Asset

**Field** **Details**

```
UsageEndDate

Uuid

```

Usage

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when usage for this asset ends or expires.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID for the asset. This field is available in API version 49.0 and later.

Use this object to track products sold to customers. With asset tracking, a client application can quickly determine which products were
previously sold or are currently installed at a specific account. You can also create hierarchies of up to 10,000 assets.

For example, suppose that your company wants to renew and upsell opportunities on products sold in the past. Similarly, your company
can track competitive products in a customer environment where products can be replaced or swapped out.

Asset tracking is also useful for product support, providing detailed information to assist with product-specific support issues. For example,
the `PurchaseDate` or `SerialNumber` can indicate whether a given product has certain maintenance requirements, including
product recalls. Similarly, the `UsageEndDate` can indicate when the asset was removed from service or when a license or warranty
expires.

If an application creates an Asset record, it must specify a `Name` and either an `AccountId`, `ContactId`, or both.

With REST API, use the `getRelatedListInfo` function to get information about related lists on the asset. Note that when requesting
information about _`PrimaryAssets`_, the response is labeled `Related Assets`, and the response for _`RelatedAssets`_ is
labeled `Primary Assets` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, those objects are available in the same API versions as
this object. Otherwise, they’re available in the specified API version and later.

**[AssetChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AssetFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**AssetOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects AssetAction

**AssetShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### AssetAction

Represents a change made to a lifecycle-managed asset. The fields can’t be edited. This object is available in API version 50.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
ActionDate

ActualTaxChange

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date when an asset action change is recorded. This date can differ from the start date
of the related asset state period. For example, suppose that a customer cancels a subscription
in June, and the subscription expires in October. The date the customer cancels the
subscription (June) is the action date of the asset action. The cancellation's effective date
(October) is the start date of the asset state period.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of actual tax from all asset action sources. This field is populated by the system.
Label is **Change in Actual Tax** .

This field is a calculated field.


Standard Objects AssetAction

**Field** **Details**

```
AdjustmentAmountChange

Amount

AssetActionNumber

AssetId

CanRollBack

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of adjustment amount from all asset action sources. This field is populated by the
system. Label is **Change in Adjustment Amount** .

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The delta in the total asset amount resulting from an asset action.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action. Label is **Name** .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lifecycle-managed asset. Label is **Asset** .

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AssetAction

**Field** **Details**

**Description**
Indicates whether the last asset action can be rolled back ( `true` ). If this property is set to
`false`, the asset and the last asset action can’t be rolled back.

The default value is `false` . This field is available in API version 65.0 and later.

```
CategoryEnum

EstimatedTaxChange

MrrChange

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The business category of the asset action, for use in reporting. Asset action totals are broken
out by the picklist values on this required field, and those totals are in turn reflected on assets.
These categories are available and aren’t customizable. Label is **Business Category** .

Possible values are:

**•** `Cancellations`

**•** `Cross-Sells`

**•** `Downgrades` Indicates a transition to a lower-level version or tier of an asset.

**•** `Downsells` Indicates a negative quantity amendment or a decreased Line Item total
price with no change in quantity.

**•** `Initial Sale` Indicates that the asset is initially purchased by an account.

**•** `Other`

**•** `Renewals`

**•** `Swaps` Indicates the exchange of one asset for another. Applies to both swapped-out
and swapped-in actions.

**•** `Terms And Conditions Changes`

**•** `Transfers` Indicates that an asset is transferred from one account to another.

**•** `Upgrades` Indicates a transition to a higher-level version or tier of an asset.

**•** `Upsells` Indicates a positive quantity amendment or an increased Line Item total
price with no change in quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of estimated tax from all asset action sources. This field is populated by the system.
Label is **Change in Estimated Tax** .

This field is a calculated field.

**Type**
currency


Standard Objects AssetAction

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The delta in the asset’s monthly recurring revenue resulting from an asset action. For example,
suppose that the MRR during an asset state period is $200 and the next asset action adds
$100. Then this field’s value is $100. Label is **Change in Monthly Recurring Revenue** .

```
ProductAmountChange

QuantityChange

```

RolledbackAssetAction

```
SubtotalChange

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of product amount from all asset action sources. This field is populated by the
system. Label is **Change in Product Amount** .

This field is a calculated field.

**Type**
double

**Properties**
Filter, Sort

**Description**
The delta in the asset quantity resulting from an asset action. For example, suppose that the
asset quantity during an asset state period is 20 and the next asset action adds 10. Then this
field’s value is 10. Label is **Change in Quantity** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last asset action rolled back in the current rollback transaction. This field is available in
API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of subtotal from all asset action sources. This field is populated by the system.
Label is **Change in Subtotal** .

This field is a calculated field.


Standard Objects AssetAction

**Field** **Details**

```
Subtype

TotalAmount

TotalCancellationsAmount

TotalCrossSellsAmount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The subtype of the action on the asset.

Valid values are:

**•** `DowngradeFrom` —Available in API version 66.0 and later.

**•** `DowngradeTo` —Available in API version 66.0 and later.

**•** `FieldAmendment`

**•** `Rollback`

**•** `StartDateAdjustment`

**•** `SwapIn` —Available in API version 66.0 and later.

**•** `SwapOut` —Available in API version 66.0 and later.

**•** `TransferFrom`

**•** `TransferTo`

**•** `UpgradeFrom` —Available in API version 66.0 and later.

**•** `UpgradeTo` —Available in API version 66.0 and later.

This field is available in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the current and previous asset action amount. This field is populated by the
system.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Cancellations` .
This field is populated by the system.

**Type**
currency


Standard Objects AssetAction

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Cross-Sells` . This
field is populated by the system.

```
TotalDowngradesAmount

TotalDownsellsAmount

TotalInitialSaleAmount

TotalMrr

TotalOtherAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Downgrades` . This
field is populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Downsells` . This
field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Initial Sale` .
This field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the monthly recurring revenue for the current and previous asset action. This
field is populated by the system. Label is **Total Monthly Recurring Revenue** .

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects AssetAction

**Field** **Details**

**Description**
The sum of current and previous asset action amounts categorized as `Other` . This field is
populated by the system.

```
TotalQuantity

TotalRenewalsAmount

TotalSwapsAmount

TotalTermsAndConditionsAmount

TotalTransfersAmount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the changes in quantity for the current and previous asset action. This field is
populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Renewals` . This field
is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Swaps` . This field is
populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Terms and`
`Conditions Changes` . This field is populated by the system. Label is **Total Terms**
**and Conditions Changes Amount** .

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects AssetActionSource

**Field** **Details**

**Description**
The sum of current and previous asset action amounts categorized as `Transfers` . This
field is populated by the system.

```
TotalUpgradesAmount

TotalUpsellsAmount

Type

### AssetActionSource

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Upgrades` . This field
is populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Upsells` . This field
is populated by the system.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The REST API used to generate the asset action. This field is populated by the system.

Valid values are:

**•** `Cancel`

**•** `Change`

**•** `Convert`

**•** `Generate`

Represents an optional way to record what transactions caused changes to lifecycle-managed assets. Use it to trace financial and other
information about asset actions. This object supports Salesforce order products and work order line items, and transaction IDs from other
systems. The fields can’t be edited. This object is available in API version 50.0 and later.


Standard Objects AssetActionSource

Supported Calls

`createable()`, `deletable()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`,
`query()`, `retrieve()`, `search()`, `undeletable()`, `updateable()` .

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
ActualTax

AdjustmentAmount

AssetActionId

```

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The region-specific tax amount determined at time of the order.

This field is not used for price and tax calculations.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
An adjustment to the product amount, such as a discount.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort

**Description**
The related asset action, that is, the change caused by an asset action source transaction.

This field is a relationship field.

**Relationship Name**
AssetAction

**Relationship Type**
Lookup

**Refers To**
AssetAction


Standard Objects AssetActionSource

**Field** **Details**

```
AssetActionSourceNumber

BillingReference

Discount

DiscountAmount

EffectiveGrantDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action source. Label is **Name** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the OrderItem or OrderItemDetail record that this AssetActionSource record is
created for.

**Type**
percent

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The discount, expressed as a percentage, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The discount, expressed as currency, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The date when the resources associated with the asset were granted.

This field is available in orgs that have Revenue Cloud when Rate Management is enabled.

This field is available in API version 62.0 and later.


Standard Objects AssetActionSource

**Field** **Details**

```
EndDate

EstimatedTax

ExternalReference

ExternalReferenceDataSource

LegalEntityId

```

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The end date of the service or change.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The estimate of the region-specific tax amount made at time of the transaction.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of an asset action source transaction originating in a system outside of Salesforce.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
A system outside of Salesforce that contains asset action source transactions.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the legal entity record associated with the asset action source transaction.

This field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup


Standard Objects AssetActionSource

**Field** **Details**

**Refers To**
LegalEntity

```
ListPrice

NetUnitPrice

ObligatedAmount

OriginalLineNumber

```

**Type**
currency

**Properties**
Creatable, Filter, Nillable, Sort, Updateable

**Description**
List price for the order product. Value is inherited from the associated PriceBookEntry upon
order product creation.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The final adjusted unit price, inclusive of all adjustments, but exclusive of tax. The unit price
after all price adjustments are applied.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
When a line amount is prorated, this amount shows the service amount that’s been consumed.

**Type**
int

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The number of the original order item detail line. Salesforce uses this information to create
a record to amend, renew, or cancel an order. This field is available in API version 64.0 and
later.

**Relationship Name**
OrderItemDetail

**Relationship Type**
Lookup

**Refers To**
LineNumber


Standard Objects AssetActionSource

**Field** **Details**

```
PeriodBoundary

PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
picklist

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Boundary delimiters for periods. It determines when a period starts and/or ends.

Valid values are:

**•** `AlignToCalendar`

**•** `Anniversary`

**•** `DayOfPeriod`

**•** `LastDayOfPeriod`

**Type**
int

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The number specifying the day number when Period Boundary is a specific day in a
week/month/year. It only applies when PeriodBoundary is set to "day of period.”

**Type**
picklist

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency2 is Annual or by manual user entry. Possible values are:

1-January

2-February

3-March

4-April

5-May

6-June

7-July

8-August

9-September

10-October

11-November

12-December


Standard Objects AssetActionSource

**Field** **Details**

```
PricebookEntryId

PricingTermCount

ProductAmount

ProductSellingModelId

ProrationPolicyId

Quantity

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
PricebookEntry is used as a lookup for price information in order to pre-populate OrderItem's
ListPrice and UnitPrice.

**Type**
double

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Number of pricing terms is this subscription product.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The product amount after the asset action source transaction.

**Type**
reference

**Properties**
Creatable, Filter, Group, Nillable, Sort, Updateable

**Description**
Specifies the product selling model type. Foreignkey to ProductSellingModel entity.

**Type**
reference

**Properties**
Creatable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the ProrationPolicy used for pricing.

**Type**
double

**Properties**
Creatable, Filter, Nillable, Sort, Updateable


Standard Objects AssetActionSource

**Field** **Details**

**Description**
The product quantity or the change in product quantity after the asset action source
transaction.

```
ReferenceEntityItemId

SegmentIdentifier

StartDate

Subtotal

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of an asset action source transaction originating in Salesforce. The transaction can be
an order product or a work order line item.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, WorkOrderLineItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ramp segment associated with the asset action source transaction.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The start date of the service or change.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the product amount and the adjustment amount.

This field is a calculated field.


Standard Objects AssetActionSource

**Field** **Details**

```
TaxTreatmentId

TotalLineAmount

TotalPrice

TransactionDate

UnitPrice

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
Lookup to Tax Treatment entity. It's used to calculate tax.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The price of the line before any price adjustments were applied. SalesTransactionItem:
ProratedStartingTotal / StartingPriceTotal. Note: TotalPrice is computed using the UnitPrice,
which includes discounts (price adjustments), while TotalLineAmount doesn’t include price
adjustments.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Calculated by the pricing engine for ARC. Summation of TotalAdjustmentAmount plus
TotalLineAmount for this item.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The date of a source transaction, such as an order date.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The unit price of the item before any discounts or tax calculation.


### Standard Objects AssetAttribute AssetAttribute

Stores asset attributes to track and analyze asset conditions to improve their uptime. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `update()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
AssetId

AttributeDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset.

This field is a relationship field.

**Relationship Name**
### Asset

**Relationship Type**
Lookup

**Refers To**
### Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the attribute definition for this asset attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup


Standard Objects AssetAttribute

**Field** **Details**

**Refers To**
AttributeDefinition

```
AttributeName

AttributePicklistValueId

AttributeValue

ExternalId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name given to the asset attribute in the UI by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the attribute picklist value if the attribute is a picklist type.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**
AttributePicklistValue

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores the value of an asset attribute, for example 5-TB storage .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An auto-generated ID of the attribute record saved in an external system (for example an
HBase database). This field is reserved and used for internal purpose.


### Standard Objects AssetContractRelationship

Usage

Add asset descriptors to the AssetAttribute object instead of creating multiple custom attributes on an asset. This helps scale to a high
asset volume in the system.

SEE ALSO:

AttributeDefinition

AttributePicklist

AttributePicklistValue

RecordsetFltrCritMonitor

### AssetContractRelationship

Represents a relationship between an asset and a contract. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud.

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the asset related to the contract.

This field is a relationship field.

**Relationship Name**
### Asset

**Relationship Type**
Lookup

**Refers To**
### Asset


Standard Objects AssetContractRelationship

**Field** **Details**

```
ContractId

EndDate

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the contract related to the asset.

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The end date and time of the relationship between contract and asset.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. The associated UI label is **Last Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user accessed this record or list view ( `LastReferencedDate` ) but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects AssetDowntimePeriod

**Field** **Details**

**Description**
The auto-generated number assigned to AssetContractRelationship. (Read Only)

```
StartDate

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date and time of the relationship between contract and asset.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetContractRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetContractRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

### AssetDowntimePeriod

Represents a period during which an asset is not able to perform as expected. Downtime periods include planned activities, such as
maintenance, and unplanned events, such as mechanical breakdown. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `AssetDowntimePeriodNumber`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number of this asset downtime period record.


Standard Objects AssetDowntimePeriod

**Field** **Details**

```
AssetId

Description

DowntimeType

EndTime

IsExcluded

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset this asset downtime period record is for.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of this asset downtime period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of this asset downtime period. Possible values are:

**•** `Planned`

**•** `Unplanned`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The time this asset downtime period ended.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether this asset downtime period is excluded from the calculation of accumulated
downtime and accumulated unplanned downtime, and therefore not included in availability
and reliability calculations.

**Type**
dateTime


### Standard Objects AssetOwnerSharingRule

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The time this asset downtime period started.

### AssetOwnerSharingRule

Represents the rules for sharing an Asset with users other than the owner. This object is available in API version 33.0 and later.

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


Standard Objects AssetOwnerSharingRule

Fields

**Field** **Details**

```
AssetAccessLevel

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
A description of the sharing rule. Maximum size is 1000 characters.

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

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Cases owned by users in the source group
trigger the rule to give access.


### Standard Objects AssetRateAdjustment

**Field** **Details**

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

Use this object to manage the sharing rules for assets. General sharing uses this object.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### AssetRateAdjustment

Stores the tier rate adjustments for the asset rate card entries. This object is available in API version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.


Standard Objects AssetRateAdjustment

Fields

**Field** **Details**

```
AdjustmentType

AdjustmentValue

AssetRateCardEntryId

LowerBound

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of rate adjustment.

Valid values are:

**•** `Amount` —Adjusts rate by using a specific amount.

**•** `Override` —Adjusts rate by using the override rate.

**•** `Percentage` —Adjusts rate by using a percentage.

**Type**
double

**Properties**
Filter, Sort

**Description**
The value of the adjustment.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent asset rate card entry record associated with the asset rate adjustment.

This field is a relationship field.

**Relationship Name**
AssetRateCardEntry

**Relationship Type**
Master-detail

**Refers To**
AssetRateCardEntry (the master object)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The minimum quantity for the adjustment to be applicable.


### Standard Objects AssetRateCardEntry

**Field** **Details**

```
Name

UpperBound

### AssetRateCardEntry

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the asset rate adjustment.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The maximum quantity for the adjustment to be applicable.

Stores the negotiated rate card entries that are associated with an asset in Revenue Cloud. This object is available in API version 62.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the asset rate card entry record.

This field is a relationship field.


Standard Objects AssetRateCardEntry

**Field** **Details**

**Relationship Name**
Asset

**Relationship Type**
Master-detail

**Refers To**
Asset (the master object)

```
BindingObjectFormula

BindingObjectId

BindingObjectRateOrder

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The formula that returns the ID of the associated binding object, if specified. If binding object
isn't added, the formula returns the asset ID of the asset related to this asset rate card entry.
This field is read-only. Available in API version 65.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the binding object associated with the asset rate card entry. Available in API version
65.0 and later.

This field is a relationship field.

**Relationship Name**
BindingObject

**Refers To**
Asset

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that determines the applicable binding object rate when multiple rates are defined
for an Anchor binding object within a effective period. Available in API version 65.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects AssetRateCardEntry

**Field** **Details**

**Description**
The ID of the binding object associated with the asset rate card entry.

Possible values are:

**•** AED - UAE Dirham

**•** AUD - Australian Dollar

**•** BRL - Brazilian Real

**•** CAD - Canadian Dollar

**•** EUR - Euro

**•** GBP - British Pound

**•** INR - Indian Rupee

**•** JPY - Japanese Yen

**•** SEK - Swedish Krona

**•** USD - U.S. Dollar

The default value is USD. Available in API version 65.0 and later.

```
EndDate

Name

NegotiatedRate

RateCardEntryId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the rate card's time period becomes inactive. The rate card becomes inactive
at 11:59:00 PM on the end date.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number assigned to the asset rate card entry. Read-only.

**Type**
double

**Properties**
Filter, Sort

**Description**
The base negotiated rate used to charge overage consumption.

**Type**
reference


Standard Objects AssetRateCardEntry

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card entry record containing the catalog rates that's associated with the
asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCardEntry

**Refers To**
RateCardEntry

```
RateCardId

RateUnitOfMeasureId

StartDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCard

**Refers To**
RateCard

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the unit of measure record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateUnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
dateTime

**Properties**
Filter, Sort


### Standard Objects AssetRelationship

**Field** **Details**

**Description**
The date when the rate card's time period becomes active. The rate card becomes active at
12:00:00 AM on the start date.

```
UsageResourceId

### AssetRelationship

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the usage resource record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
UsageResource

**Refers To**
UsageResource

Represents a non-hierarchical relationship between assets due to an asset modification; for example, a replacement, upgrade, or other
circumstance. In Revenue Lifecycle Management, this object represents an asset or assets grouped in a bundle or set. This object is
available in API version 41.0 and later.

Asset relationships appear in the Primary Assets and Related Assets related lists on asset records in the UI.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Some fields are available only in Revenue Cloud. Field availability is noted in the field detail column.

Fields

**Field Name** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects AssetRelationship

**Field Name** **Details**

**Description**
The unique identifier of the new asset, which is the asset that is taking the place
of the existing asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

```
AssetRelationshipNumber

AssetRole

CurrencyIsoCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the asset relationship.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the main asset relative to the other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

Possible values are:

**•** `Add-on` —The main asset is an add-on.

**•** `Bundle` —The main asset is the bundle parent.

**•** `Set` —The asset is the main asset in the set.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the asset. The default value
is USD.


Standard Objects AssetRelationship

**Field Name** **Details**

```
FromDate

GroupingKey

ProductRelationshipTypeId

ProductRelatedComponent

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the new asset was installed.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Read-only field used to indicate the bundle that an asset belongs to. For example,
if two assets have the same GroupingKey value, then it means that the assets are
bundled together.

This field is available in API v.60.0 and later. This field is available in orgs with
Revenue Cloud.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the record that describes the relationship between the
main and associated assets.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

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
Filter, Group, Nillable, Sort

**Description**
The product related component that’s associated with the asset relationship.


Standard Objects AssetRelationship

**Field Name** **Details**

This field is a relationship field.

This field is available in API 60.0 and later in Revenue Cloud.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup

**Refers To**
ProductRelatedComponent

```
RelatedAssetId

RelatedAssetPricing

RelatedAssetQtyScaleMethod

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The existing asset that is being modified.

This field is a relationship field.

**Relationship Name**
RelatedAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the price of the related asset is included in the bundle price.
Valid values are:

**•** `IncludedInBundlePrice`

**•** `NotIncludedInBundlePrice`

This field is available in API version 59.0 and later in Revenue Cloud.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies how the quantity of the related asset changes relative to the quantity
of the parent asset. Valid values are:


Standard Objects AssetRelationship

**Field Name** **Details**

**•** `Constant`

**•** `Proportional`

This field is available in API version 59.0 and later in Revenue Cloud.

```
RelatedAssetRole

RelationshipType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated asset relative to other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

Valid values are:

**•** `Add-on` —The main asset is an add-on.

**•** `Bundle` —The main asset is the bundle parent.

**•** `Set` —The asset is the main asset in the set.

**•** `Simple` —The asset is purchased individually and isn’t associated with
variations.

**•** `Variation Parent` ——The main asset is the variation parent.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of relationship between the existing asset and the new asset. This field
comes with three values—Replacement, Upgrade, and Crossgrade—, but you
can create more values in Setup.

Possible values are:

**•** `Crossgrade` —The new asset is a crossgrade of an existing asset. For
example, changing a subscription to a plan with the same service, but that
runs for a longer amount of time.

**•** `Replacement` —The new asset is replacing an existing asset. For example,
a customer’s faulty widget that was under warranty is being replaced with
a new one.

**•** `Upgrade` —The new asset is an upgrade of an existing asset. For example,
upgrading a customer’s existing subscription plan to a new plan with more
services.

The default value is `Replacement` .


### Standard Objects AssetShare

**Field Name** **Details**

```
ToDate

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the modified asset is uninstalled.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetRelationshipChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AssetRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AssetRelationshipOwnerSharingRule (API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**
Sharing rules are available for the object.

**[AssetRelationshipShare (API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**
Sharing is available for the object.

### AssetShare

Represents a sharing entry on an Asset. This object is available in API version 33.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can’t access this object.


Standard Objects AssetShare

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
AssetAccessLevel

AssetId

IsDeleted

RowCause

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to the Asset. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid for creating or deleting records.

This field must be set to an access level that is higher than the organization’s default access
level for cases.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Asset associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist


### Standard Objects AssetStatePeriod

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Asset with them.

**•** `Owner` —The User is the owner of the Asset.

**•** `Rule` —The User or Group has access via an Asset sharing rule.

**•** `GuestRule` —The User or Group has access via an Asset guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Asset. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view and edit Asset records owned by other users.

If you attempt to create a new record that matches an existing record, request updates any modified fields and returns the existing
record.

### AssetStatePeriod

Represents a time span when an asset has the same quantity, amount, and monthly recurring revenue (MRR). An asset has as many asset
state periods as there are changes to it (asset actions) during its lifecycle. The dashboard and related pages show the current asset state
period. The fields can’t be edited. This object is available in API version 50.0 and later.


Standard Objects AssetStatePeriod

Supported Calls

`createable()`, `deletable()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`,
`query()`, `retrieve()`, `search()`, `updateable()` .

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
Amount

AssetId

AssetStatePeriodNumber

```

**Type**
currency

**Properties**
Createable, Filter, Sort, Updateable

**Description**
An asset’s total amount during an asset state period. Revenue Cloud doesn't set or use this
field's value currently.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort

**Description**
The asset related to an asset state period. Label is **Asset** .

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset state period. Label is **Name** .


Standard Objects AssetStatePeriod

**Field** **Details**

```
BillingFrequency

BindingInstanceTargetId

Discount

DiscountAmount

```

**Type**
picklist

**Properties**
Createable, Filter, Group, Nillable, Restricted picklist, Sort, Updateable

**Description**
The time period that indicates how often the line item is billed.

Possible values are:

**•** `Annual`

**•** `Monthly`

**•** `Quarterly`

**•** `Semi-Annual`

Available in API version 65.0 and later.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of a custom product target for a usage-based quote line item, order Item, or asset
allocation.

This field is a polymorphic relationship field.

**Relationship Name**
BindingInstanceTarget

**Refers To**
Account, Asset, BindingObjectCustomExt, Contract

**Type**
percent

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Editable number from 0 to 100. Available in API version 65.0 and later.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The fixed amount discount to apply to the line item. Available in API version 65.0 and later.


Standard Objects AssetStatePeriod

**Field** **Details**

```
EndDate

LegalEntityId

Mrr

PriceRevisionPolicy

```

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The end date and time of an asset state period. On an asset that is an evergreen subscription,
the last asset state period has no end date.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the related legal entity.

This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Createable, Filter, Sort, Updateable

**Description**
An asset’s monthly recurring revenue during an asset state period.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort, Updateable

**Description**
Specifies the price uplift policy associated with this asset state period.

This field is a relationship field.

This field is available in API version 65.0 and later.

**Relationship Name**
Price Revision Policy

**Relationship Type**
Lookup

**Refers To**
PriceRevisionPolicy


Standard Objects AssetStatePeriod

**Field** **Details**

```
Quantity

RampIdentifier

SegmentIdentifier

SegmentName

SegmentType

```

**Type**
double

**Properties**
Createable, Filter, Sort, Updateable

**Description**
The total quantity of an asset during an asset state period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp record used to group order item segments for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The name of the order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Updateable

**Description**
The period for the order item segment for this asset state period. Valid values are:


### Standard Objects AssetStatePeriodAttribute

**Field** **Details**

**•** `Custom`

**•** `Free Trial`

**•** `Yearly`

The default value is `Yearly` .

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

```
StartDate

UnitPrice

UnitPriceUplift

```

**Type**
dateTime

**Properties**
Createable, Filter, Sort, Updateable

**Description**
The start date and time of an asset state period.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The price per unit for the line item. Available in API version 65.0 and later. Revenue Cloud
won't populate this field in API version 66.0 and later.

**Type**
percent

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Indicates the percentage increase of a line item's unit price. Available in API version 65.0 and
later.

### AssetStatePeriodAttribute

Represents a virtual object that holds the key-value pair of the asset attribute in a specified asset state period. This object is a child object
of AssetStatePeriod. This object is available in API version 60.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects AssetStatePeriodAttribute

Special Access Rules

[This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud with the Access Lifecycle-Managed Assets](https://help.salesforce.com/s/articleView?id=ind.rev_cloud_asset_migration_permission.htm&language=en_US)
[user permission. This object is editable only through API and not the UI.](https://help.salesforce.com/s/articleView?id=ind.rev_cloud_asset_migration_permission.htm&language=en_US)

Fields

**Field** **Details**

```
AssetStatePeriodId

AttributeDefinitionId

AttributeName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The asset state period that's associated with the asset attribute.

This field is a relationship field.

**Relationship Name**
AssetStatePeriod

**Relationship Type**
Master-detail

**Refers To**
AssetStatePeriod (the master object)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The attribute definition that's associated with the asset state period attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup

**Refers To**
AttributeDefinition

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the asset attribute.


### Standard Objects AssetTag

**Field** **Details**

```
AttributePicklistValueId

AttributeValue

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value specified in the picklist type field that corresponds to the attribute in the
AttributePicklistValue object.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**
AttributePicklistValue

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the asset state period attribute. For example, a shirt can have the value of `blue`,
which indicates the shirt's color, or it can have the value of `small`, which indicates the
shirt's size.

You can use this field to filter records only if the DataType value in the related
`AttributeDefinitionId` record is `Text` . If the DataType value is `Picklist`, use
the value in the `AttributePicklistValueId` field for filtering. You can’t use this
field to filter records if the DataType value is `Checkbox`, `Currency`, `Date`, `Datetime`,
`Multipicklist`, `Number`, or `Percent` .

This object doesn’t support custom fields, validation rules, or triggers. In SOQL queries, you can filter records by using `Id` and
`AttributeDefinition` . You can’t use `AttributeValue` in the `WHERE` clause.

### AssetTag

Associates a word or short phrase with an Asset.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects AssetTag

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

AssetTag stores the relationship between its parent TagDefinition and the Asset being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects AssetTokenEvent

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### AssetTokenEvent

[The documentation has moved to AssetTokenEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_assettokenevent.htm) _Platform Events Developer Guide_ .

### AssetWarranty

Defines the warranty terms applicable to an asset along with any exclusions and extensions. This object is available in API version 50.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

### `AssetWarrantyNumber`

EndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset this warranty term applies to.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier of the asset warranty record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which this warranty term expires.


Standard Objects AssetWarranty

**Field** **Details**

```
ExchangeType

Exclusions

ExpensesCovered

ExpensesCoveredEndDate

IsTransferable

LaborCovered

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of exchange offered by this warranty term.

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
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for expenses ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty term can be transferred to a new owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of labor covered.


Standard Objects AssetWarranty

**Field** **Details**

```
LaborCoveredEndDate

LastReferencedDate

LastViewedDate

PartsCovered

PartsCoveredEndDate

Pricebook2Id

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for labor ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last viewed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of parts covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for parts ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects AssignedResource

**Field** **Details**

**Description**
The ID of the price book item associated with this asset warranty term.

```
StartDate

WarrantyTermId

WarrantyType

```

Associated Objects

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date on which cover under this warranty term starts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the warranty term this asset warranty term extends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of the warranty.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetWarrantyChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

### AssignedResource

Represents a service resource who is assigned to a service appointment in Field Service and Lightning Scheduler. Assigned resources
appear in the Assigned Resources related list on service appointments. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects AssignedResource

Fields

**Field Name** **Details**

```
ActualTravelTime

ApptAssistantInfoUrl

AssignedResourceNumber

EstimatedTravelTime

LocationStatus

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that the service resource needs to travel to the assigned
service appointment. You can enter a value with up to two decimal places.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that contains the status of the mobile worker approaching the service
appointment, the Community URL, and the expiry of the URL. Available in version
51.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource assignment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated number of minutes needed for the service resource to travel to
the service appointment they’re assigned to. You can enter a value with up to
two decimal places.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the mobile worker approaching the service appointment. When
the location status changes to one of these values, a status update containing


Standard Objects AssignedResource

**Field Name** **Details**

`ApptAssistantInfoUrl` is sent to the customer. Available in version 51.0
and later.

Possible values are:

**•** `EnRoute`

**•** `LastMile`

```
IsPrimaryResource

ServiceAppointmentId

ServiceCrewId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service resource is a primary resource or not. The default
value is false. Available in API version 47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service appointment that the resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceAppointment

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort, Nillable

**Description**
The service crew that the resource is assigned to.

Note: Since service resources can represent crews or individuals,
appointments are typically assigned to crews in the following way:

**1.** Create a service resource of the Crew type that represent the crew.

**2.** Create an assigned resource on the service appointment and select
the crew resource in the `ServiceResourceId` field.


Standard Objects AssignedResource

**Field Name** **Details**

As an alternative, you can assign appointments to crew members
separately. This lets you track each member’s travel time and see a list of
the crew members in the Assigned Resources related list. To take this
approach, create an assigned resource for each crew member. List the
crew member in the `ServiceResourceId` field and the crew they
belong to in the `ServiceCrewId` field.

```
ServiceResourceId

Transaction

```

Usage

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort

**Description**
The resource who is assigned to the service appointment.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last transaction ID of the scheduling and optimization request that updated
this object. The transaction ID is automatically generated and populated by the
Enhanced Scheduling and Optimization engine. Available in API version 63.0 and
later.

You can assign multiple service resources to a service appointment. Service resources who are assigned to service appointments cannot
be deactivated until they are removed from the appointments.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AssignedResourceChangeEvent (API version 48.0)**
Change events are available for the object.


### Standard Objects AssignmentRule

**AssignedResourceHistory on page 63(API version 61.0)**
History is available for tracked fields of the object.

**AssignedResourceFeed**

Feed tracking is available for the object.

### AssignmentRule

Represents an assignment rule associated with a Case or Lead.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

**•** This object is read only. Assignment rules are created, configured, and deleted in the user interface.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Active

Name

SobjectType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this assignment rule is active ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this assignment rule.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of assignment rule—Case or Lead.


### Standard Objects AssociatedLocation

Usage

Before creating or updating a new Case or Lead, a client application can query (by name) the AssignmentRule to obtain the ID of the
assignment rule to use, and then assign that ID to the `assignmentRuleId` field of the AssignmentRuleHeader. The
AssignmentRuleHeader can be set using either SOAP API or REST API.

Assignment rules can also be specified when creating or upserting Case or Lead objects via the Bulk API or the Bulk 2.0 API.

SEE ALSO:

Overview of Salesforce Objects and Fields

### AssociatedLocation

Represents a link between an account and a location in Field Service. You can associate multiple accounts with one location. For example,
a shopping center location may have multiple customer accounts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ActiveFrom

ActiveTo

### `AssociatedLocationNumber`

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location is active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location stops being active.

**Type**
string


Standard Objects AssociatedLocation

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number identifying the associated location.

```
LastReferencedDate

LastViewedDate

LocationId

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date the associated location was last modified.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the associated location was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location associated with the address.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account associated with the location.

This is a relationship field.


### Standard Objects AsyncApexJob

**Field Name** **Details**

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Bill To

**•** Ship To

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AssociatedLocationChangeEvent (API version 62.0)**
Change events are available for the object.

**AssociatedLocationHistory**

History is available for tracked fields of the object.

### AsyncApexJob

Represents an individual Apex sharing recalculation job, a batch Apex job, a method with the `future` annotation, or a job that
implements `Queueable` or `Schedulable` . Use this object to query Apex batch jobs in your organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

If Apex isn’t running in system mode, users must have the View Setup and Configuration permission to access this object and to enqueue
asynchronous Apex jobs.


Standard Objects AsyncApexJob

Fields

**Field Name** **Details**

```
ApexClassId

CompletedDate

CronTriggerId

ExtendedStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex class executing the job. Label is `Class ID` .

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job was completed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronTrigger for the AsyncApexJob. This field only applies to ScheduledApex
job type. This field is available in API version 53.0 and later. For scheduled jobs created before
version 53.0, this field is populated on subsequent execution.

This is a relationship field.

**Relationship Name**
CronTrigger

**Relationship Type**
Lookup

**Refers To**
CronTrigger

**Type**
string


Standard Objects AsyncApexJob

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
If one or more errors occurred during the batch processing, this field contains a short
description of the first error. A more detailed description of that error, along with any
subsequent errors, is emailed to the last user who modified the batch class. This field is
available in API version 19.0 and later.

```
JobItemsProcessed

JobType

LastProcessed

LastProcessedOffset

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of job items processed. Label is `Batches Processed` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job being processed. Valid values are:

**•** `ApexToken`

**•** `[BatchApex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)`

**•** `BatchApexWorker`

**•** `[Future](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_invoking_future_methods.htm)`

**•** `[Queueable](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)`

**•** `[ScheduledApex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_scheduler.htm)`

**•** `[SharingRecalculation](https://help.salesforce.com/s/articleView?id=platform.security_apex_sharing_recalc.htm&type=5&language=en_US)`

**•** `TestRequest`

**•** `TestWorker`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Last ID that was processed and committed.

**Type**
int


Standard Objects AsyncApexJob

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Offset of the last ID that was processed and committed.

```
MethodName

NumberOfErrors

ParentJobId

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Apex method being executed. Label is `Apex Method` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of batches with a failure. A batch is considered transactional, so any unhandled
exceptions constitute an entire failure of the batch. Label is `Failures` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For batch Apex jobs that run using chunking implementation, multiple child jobs of type
`BatchApexWorker` are created. Each of these child job records contains the job Id of
the parent Apex job that started their execution. For batch Apex jobs that run using a
non-chunking implementation, child jobs aren’t created.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the job. Valid values are:

**•** `Aborted`

**•** `Completed`

**•** `Failed`

**•** `Holding` [1]

**•** `Preparing`


### Standard Objects AsyncOperationLog

**Field Name** **Details**

**•** `Processing`

**•** `Queued`

1 This status applies to batch jobs in the Apex flex queue.

```
TotalJobItems

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of batches processed. Each batch contains a set of records. Label is `Total`
`Batches` .

Use this object to query Apex batch jobs in your organization.

### AsyncOperationLog

Represents an async operations log containing progress and status information about external synchronizations to the Omnichannel
Inventory service. This object is available in API version 51.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.

Fields

**Field** **Details**

```
AsyncOperationNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number assigned to the operation.


Standard Objects AsyncOperationLog

**Field** **Details**

```
Description

Error

ExternalReference

FinishedAt

LastStatusUpdateAt

RelatedRecordId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique external reference ID per type.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the status of the operation was last updated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The related record ID for the async request. This field is available in API version 60.0 and later.


Standard Objects AsyncOperationLog

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Asset, OrderItemSummary

```
Request

Response

StartedAt

Status

```

**Type**
textarea

**Properties**
Nillable

**Description**
The request sent to the external service.

**Type**
textarea

**Properties**
Nillable

**Description**
The full response from the external service.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation started.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the operation.

Possible values are:

**•** `Completed`

**•** `Error`

**•** `In Progress`

**•** `New`


### Standard Objects AsyncOperationTracker

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of operation that is being tracked.

Possible values are:

**•** `CancelAsset` —This value is available in API version 60.0 and later.

**•** `CreateAsset` —This value is available in API version 60.0 and later.

**•** `CancelOrderItemSummaries`

**•** `ImportInventory`

**•** `LocationManagement`

**•** `OrderSummaryAdjustmentAggregate`

### AsyncOperationTracker

Represents the status of an asynchronous request initiated from the Quote, Order, and CreditMemo entities. This object is available in
API version 61.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AsyncOperationNumber

CorrelationIdentifier

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A string that identifies the operation being tracked in AsyncOperationTracker.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AsyncOperationTracker

**Field** **Details**

**Description**
A string that identifies an operation across services.

```
ExpiresAt

FailedJobItems

FinishedAt

JobType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items within the job that have failed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job.

Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion` —Automated Negative
Invoice Line Conversion

**•** `AutomaticRefunds` —Automatic Refunds

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`


Standard Objects AsyncOperationTracker

**Field** **Details**

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PearAmendQtyAssets` —Initiate Amend Quantity

**•** `PearCancelAssets` —Initiate Cancellation

**•** `PearRenewAssets` —Initiate Renewal

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote` —Place Quote

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment` —Price Rule Deployment

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom` —Create Material Lines

```
LastReferencedDate

LastViewedDate

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


Standard Objects AsyncOperationTracker

**Field** **Details**

```
OwnerId

ParentOperationId

ReferenceEntityId

StartedAt

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is a relationship field.

**Relationship Name**
ParentOperation

**Refers To**
AsyncOperationTracker

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Refers To**
CreditMemo, InvoiceBatchRun, Order, Product2, Quote

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AsyncOperationTracker

**Field** **Details**

**Description**
The timestamp indicating when Salesforce started the asynchronous process.

```
Status

StepName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the asynchronous request.

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures` —Completed With Failures

**•** `Failure`

**•** `InProgress` —In Progress

**•** `Submitted`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion` —Automated Negative
Invoice Line Conversion

**•** `AutomaticRefunds` —Automatic Refunds

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PSTCommonSyncStep`

**•** `PSTConfigAndPersist`

**•** `PSTOrderTaxAsync`

**•** `PSTPriceAndPersist`


Standard Objects AsyncOperationTracker

**Field** **Details**

**•** `PSTQuoteTaxAsync`

**•** `PearAmendQtyAssets` —Initiate Amend Quantity

**•** `PearCancelAssets` —Initiate Cancellation

**•** `PearRenewAssets` —Initiate Renewal

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote` —Place Quote

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment` —Price Rule Deployment

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom` —Create Material Lines

```
SubmittedAt

SuccessfulJobItems

TotalJobItems

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successful items in this job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of items in this job.


### Standard Objects AsyncOpSyndicationFeedFile AsyncOpSyndicationFeedFile

Represents the sync status of file-related information shared with external channels such as Facebook and Instagram. This object is
available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

### `AsyncOpSyndicationFeedFileNumber`

```
AsyncOperationTrackerId

FeedContentBody

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID assigned to each syndication feed file record, and used for tracking and reference purposes.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID assigned to the Async Operation Tracker record, which monitors and manages the lifecycle
of the syndication process.

This field is a relationship field.

**Relationship Name**
AsyncOperationTracker

**Refers To**
AsyncOperationTracker

**Type**
base64

**Properties**
Nillable

**Description**
The content of the feed file that is syndicated to the external platform.


Standard Objects AsyncOpSyndicationFeedFile

**Field** **Details**

```
FeedContentContentType

FeedContentLength

FeedContentName

FeedScope

LastReferencedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the format of the feed file to ensure proper processing. For example, CSV, JSON, or
XML files.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the feed file in bytes, which is used for validation and processing requirements.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the feed file, which includes identifiers like timestamp or sequence number.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Defines the scope or category of the feed. For example, if the feed applies to main,
country-specific, or language-specific catalog segments.

Possible values are:

**•** `CountryFeed`

**•** `LanguageFeed`

**•** `MainFeed`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
For internal use only.


### Standard Objects AttachedContentDocument

**Field** **Details**

```
LastViewedDate

PlatformConnections

SyncMode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
For internal use only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The external channel or destination for syndication.

Possible values are:

**•** `Meta`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of sync being performed.

Possible values are:

**•** `FullSync`

### AttachedContentDocument

This read-only object contains all `ContentDocument` objects associated with an object.

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


Standard Objects AttachedContentDocument

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the attached `ContentDocument` .

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

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

The size of the document in bytes for notes smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for notes smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes up to 10 GB.

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


Standard Objects AttachedContentDocument

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the external data source in which the document is stored. This field is
set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

```
ExternalDataSourceType

FileExtension

FileType

LinkedEntityId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in APIAPI version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentDocument` .

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentDocument` is attached to.

This is a relationship field.

**Relationship Name**
LinkedEntity


Standard Objects AttachedContentDocument

**Field Name** **Details**

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
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingSession,
MktCalculatedInsight, OperatingHours, Opportunity, Order, OrderItem,
Organization, OtherComponentTask, PartyConsent, PersonEducation,
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


### Standard Objects AttachedContentNote

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
Controls whether or not sharing is frozen for a file. Only administrators and file
owners with Collaborator access to the file can modify this field. Default is
`Allowed`, which means that new shares are allowed. When set to
`Restricted`, new shares are prevented without affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Title of the attached `ContentDocument` .

Use this object to list all `ContentDocument` objects attached to an object via a feed post.

To retrieve `ContentDocument` objects, issue a describe call on an object, which returns a query result for each activity since the
record was created. You can’t directly query this object.

### AttachedContentNote

This read-only object contains all ContentNote objects associated with an object.This object is available in API version 35.0 and later.

Supported Calls

```
describeSObjects()

```

Special Access Rules

**•** Notes must be enabled.

**•** Chatter must be enabled.


Standard Objects AttachedContentNote

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentSize

ContentSizeLong

FileExtension

FileType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the attached `ContentNote`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the note in bytes for notes smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for notes smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentNote` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of file for the note. All notes have a file type of `SNOTE` .


### Standard Objects Attachment

**Field Name** **Details**

```
LinkedEntityId

TextPreview

Title

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentNote` is attached to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A preview of the note, up to 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

Title of the note.

Use this object to list all `ContentNote` objects attached to an object.

To retrieve `ContentNote` objects, issue a describe call on an object, which returns a describe result for each note created or attached.
You can’t directly query this object.

### Attachment

Represents a file that a User has uploaded and attached to a parent object.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`


Standard Objects Attachment

Fields

**Field** **Details**

```
Body

BodyLength

ConnectionReceivedId

ConnectionSentId

ContentType

```

**Type**
base64

**Properties**
Create, Update

**Description**
Required. Encoded file data.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Size of the file (in bytes).

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
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The content type of the attachment.

If the `Don't allow HTML uploads as attachments or document`
`records` security setting is enabled for your organization, you cannot upload files with


Standard Objects Attachment

**Field** **Details**

the following file extensions: `.htm`, `.html`, `.htt`, `.htx`, `.mhtm`, `.mhtml`, `.shtm`,
`.shtml`, `.acgi`, `.svg` .

When you insert a document or attachment through the API, make sure that this field is set
to the appropriate MIME type.

```
Description

IsEncrypted

IsPartnerShared

IsPrivate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the attachment. Maximum size is 500 characters. This field is available in API
version 18.0 and later.

This information is about Shield Platform Encryption and not Classic Encryption.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the attachment is encrypted using Shield Platform Encryption ( `true` ) or
not ( `false` ). This field is available in API version 34.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is shared with a connection using Salesforce to Salesforce.
Label is `Is Shared With Partner` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is viewable only by the owner and administrators ( `true` ) or
viewable by all otherwise-allowed users ( `false` ). During a create or update call, it is possible
to mark an Attachment record as private even if you are not the owner. This can result in a
situation in which you can no longer access the record that you just inserted or updated.
Label is **Private** .

Attachments on tasks or events can't be marked private.


Standard Objects Attachment

**Field** **Details**

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
Required. Name of the attached file. Maximum size is 255 characters. Label is **File Name** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the attachment. This field isn’t required for API version 9.0 or later.

The owner of an attachment on a task or event must be the same as the owner of the task
or event.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the parent object of the attachment. The following objects are supported as
parents of attachments:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contact

**•** Contract

**•** Custom objects

**•** EmailMessage

**•** EmailTemplate

**•** Event


Standard Objects Attachment

**Field** **Details**

**•** Lead

**•** Opportunity

**•** Product2

**•** Solution

**•** Task

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, Campaign,
CareBarrier, CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EmailMessage, EmailTemplate,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
Lead, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PersonEducation,
PersonLifeEvent, Product2, ProductRequest, ProductRequestLineItem, PurchaserPlan,
ReceivedDocument, ServiceAppointment, ServiceResource, Shift, SocialPost, Solution, Task,
Visit, VisitedParty, Visitor, VolunteerProject, WorkOrder, WorkOrderLineItem

Note: If you are importing Attachment data and want to set the value for an audit field, such as `CreatedDate`, contact
Salesforce. For example, for compliance reasons, you may prefer to set the `CreatedDate` to the date the record was originally
created in your system, rather than the date it was imported into Salesforce. Audit fields are automatically updated during API
operations unless you request to set these fields yourself.

Usage

The API sends and receives the binary file attachment data encoded as a base64Binary data type. Before creating a record, client
applications must encode the binary attachment data as base64. Upon receiving a response, client applications must decode the base64
data to binary (this conversion is usually handled for you by the SOAP client).


### Standard Objects AttachmentEventLog

The create call restricts these files to a maximum size of 25 MB. For a file attached to a Solution, the limit is 1.5 MB. The maximum email
attachment size is 3 MB.

The API supports attachments on email in create, delete, or update calls. The query call does not return attachments parented by email,
unless the user performing the query has the “Modify All Data” permission.

Note:

**•** Attachment records are not searched during text searches.

**•** When issued by an administrator, the query results include Attachment records from the Recycle Bin.

**•** When issued by a non-administrator, the `queryAll()` call results do not include Attachment records from the Recycle Bin.

Access to fields depends on the method being used:

**•** All of the fields are accessible using the `describeSObjects()` and `query()` calls. With the `create()` call, you can insert
the `Name`, `ParentId`, `Body`, `IsPrivate`, and `OwnerId` fields.

**•** To modify existing records, the `update()` call gives you access to change the `Name`, `Body`, `IsPrivate`, and `OwnerId`
fields.

**•** You can access all of the fields using a `query()` call. However, you can't receive the `Body` field for multiple records in a single
`query()` call. If your query returns the `Body` field, your client application must ensure that only one row with one Attachment
is returned; otherwise, an error occurs. A more effective approach is to return IDs (but not Attachment records in the `Body` field)
from a `query()` call and then pass them into `retrieve()` calls that return the `Body` field.

**•** For information about accessing the attachments of archived activities, see Archived Activities.

SEE ALSO:

Note

### AttachmentEventLog

Attachment event logs contain information about attachments. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AttachmentIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AttachmentEventLog

**Field** **Details**

**Description**
The ID of the attachment.

```
ContentType

IsPrivateOn

OperationType

ParentIdentifier

RequestIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the attachment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the attachment is flagged as private or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation type of the attachment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent object of the attachment. For example, `a07EE00001LgsUH`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
dateTime


### Standard Objects AttribModel

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
UserIdentifier

### AttribModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

Represents an attribution model used with Personalization, Attribution, and Campaign Influence, including model weights and touch
type. This object is available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

### `AttribModelStatus`

```
AttributionModelType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates a model’s current status. The default value is `Draft`, and accepted values are

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
picklist


Standard Objects AttribModel

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of attribution model, which determines which touchpoints to evaluate.
The default value is `LastTouch`, and accepted values are

**•** `First touch`

**•** `LastTouch`

```
CurrencyIsoCode

DataSpaceId

Description

DeveloperName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where a model's resources originate. This is a
required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the attribution model. Optional.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AttribModel

**Field** **Details**

**Description**
Auto-generated or user-generated API name for the attribution model. This is a required
field.

```
Error Code

GlobalAttributionWindowDays

IdentityResolutionMode

IsZeroDayLoadRequired

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the issue that’s causing an error. The default value is `None`, and accepted values
are

**•** `ConfigurationMissingError` indicates that a required configuration setting
is missing.

**•** `DpcJobError` indicates a problem during processing.

**•** `InternalError` indicates an internal error during processing.

**•** `ModelValidationError` indicates that the model is invalid.

**•** None

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Defines a timeframe for tracking attribution-related engagement. This is a required field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Defines which identity resolution method to use when tracking engagement activities.
Default value is `Individual`, and acceptable values are

**•** `Individual`

**•** `Unified`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AttribModel

**Field** **Details**

**Description**
Defines whether to sync data before the attribution window begins. The default value is
`false` .

```
LastReferencedDate

LastRefresh

LastSuccessfulRefresh

LastViewedDate

LatestRefreshedStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the model was referenced by another resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates the last time engagement data was refreshed and evaluated
by the model.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates the last time the model was successfully refreshed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the model.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the status of last refresh process. The default value is `None`, and
accepted values are

**•** `Canceled`

**•** `Complete`


Standard Objects AttribModel

**Field** **Details**

**•** `Failure`

**•** `None`

**•** `Processing`

```
ModelContext

ModelRevision

Name

Partner

ProfileDataGraphId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the app or feature in which the attribution model is used. The default value is
`Personalization`, and accepted values are

**•** `Attribution` : indicates the use with Attribution in Salesforce Personalization.

**•** `CampaignInfluence` : indicates the use with Campaign Influence in Unified
Marketing Analytics.

**•** `Personalization` : indicates the use with Personalization in Salesforce
Personalization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A version number that indicates the latest save of the model.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the attribution model. This is a required field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates who's using the model. This field is required if the value of `ModelContext` is
`Attribution` .

**Type**
reference


Standard Objects AttribModel

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the profile data graph that’s used with the model.

**Relationship Name**
ProfileDataGraph

**Refers To**
DataGraph

```
ScheduledFrequencyMins

SyncStatus

Tags

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The scheduled frequency (in minutes) at which the attribution model is processed.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the current status of the attribution model while an action is being performed. The
default value is `Processing`, and acceptable values are:

**•** `Active`

**•** `CreateError`

**•** `DeleteError`

**•** `Deleting`

**•** `EditError`

**•** `Processing`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
User-generated strings that can be used to organize attribution models.


### Standard Objects AttribModelStage

Usage

Use this object to get information about attribution models that are in use with personalization and influence features. For example,
you can:

**•** Retrieve status and error details.

**•** Identify model settings such as type (first-touch, last-touch).

**•** Find out when the model was last used, refreshed, or synced.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AttribModelChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### AttribModelStage

Represents a funnel stage that’s used in a predefined or custom attribution configuration. Available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
AttribModelId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the attribution configuration that uses this stage. This is a
required field.


Standard Objects AttribModelStage

**Field** **Details**

**Relationship Name**
AttribModel

**Relationship Type**
Master-detail

**Refers To**
AttribModel (the master object)

```
CurrencyIsoCode

EngagementSignalEnum

IsContentMatchRequired

Name

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the engagement signal that’s selected for an attribution stage.
This value represents a step in a customer journey.

The accepted values are the engagement signals that are configured in the selected data
space.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether to link item attribution from one funnel stage to the next. The default
value is `false`, meaning not required. If you set this value to `true`, only engagement
with the same item from the previous stage is linkable.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the attribution model stage. This is a required field.


Standard Objects AttribModelStage

**Field** **Details**

```
Sequence

StageUnionGroupName

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**

Indicates the position of a stage in its journey sequence, reflecting funnel engagement from
start to finish. The funnel requires a minimum of two stages, with a maximum of four stages.
Accepted values are `1`, `2`, `3`, or `4` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of a certain group of stages. It can be used to reference individual, consecutive stages
as a combined group with a common name.

Use this object to create attribution funnel stages. The funnel mirrors key touchpoints of an individual’s personalization journey, which
you define by selecting an engagement signal and any relevant metrics. The order that you create stages in describes funnel engagement
from start to finish.

For example, view a product, click the product, add it to cart, and submit the order. The funnel requires a minimum of two stages, with
a maximum of four stages in a journey.

Associated Objects

This object has the these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AttribModelStageChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelStageFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelStageHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelStageOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelStageShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects AttribModelStageMetric AttribModelStageMetric

Represents the engagement signal metrics that you select when you configure a funnel stage for an attribution configuration. Available
in API version 63.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
Alias

AttribModelStageId

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

Indicates the name of the output data metric. This name appears as the column name for
the metric on the attribution output table.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

Unique identifier that refers to the attribution configuration stage that uses this metric.

**Relationship Name**
### AttribModelStage

**Relationship Type**
Primary-detail

**Refers To**
AttribModelStage (the primary object)

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.


Standard Objects AttribModelStageMetric

**Field** **Details**

```
EngagementSignalMetricId

Name

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the engagement signal that defines this stage.

**Relationship Name**
EngagementSignalMetric

**Refers To**
EngagementSignalMetric

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the attribution model stage metric.

An engagement signal metric is an aggregation of an engagement signal data field. These metrics are reported in the attribution model
dashboard. For example, sum of clicks on a link, number of products added to a cart, email sends, or distinct article downloads.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AttribModelStageMetricChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelStageMetricFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelStageMetricHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelStageMetricOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelStageMetricShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects AttributeDefinition AttributeDefinition

Represents a product, asset, or object attribute, for example, a hardward specification or software detail. This object is available in API
version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
DataType

DefaultValue

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The data type of the attribute definition.

Possible values are:

**•** `Checkbox`

**•** `Date`

**•** `Datetime`

**•** `Number`

**•** `Picklist`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value for this attribute.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects AttributeDefinition

**Field** **Details**

**Description**
Description of this attribute.

```
DeveloperName

IsActive

IsRequired

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the attribute definition record.

This name must begin with a letter and use only alphanumeric characters and underscores.
It can't include spaces, end with an underscore, or have two consecutive underscores.

The developer name is used for internal purpose and must be unique for all records (including
deleted records). If the system doesn't find the name unique, it automatically overrides the
user input and creates a unique name. For external use, the developer name need not be
fixed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the attribute definition is active. Active attributes definitions can be selected
for assets.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the attribute definition is required for an asset.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
[The label for the attribute. Displays a friendly name for the attribute, for example, threshold](https://help.salesforce.com/s/articleView?id=service.fs_asset_attrib_manage_monit_filter.htm&type=5&language=en_US)
[monitor lightning component and recordset filter criteria rule.](https://help.salesforce.com/s/articleView?id=service.fs_asset_attrib_manage_monit_filter.htm&type=5&language=en_US)


Standard Objects AttributeDefinition

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

PicklistId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute definition was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute definition was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the attribute definition.

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
The ID of the attribute picklist with the valid values for this attribute.


Standard Objects AttributeDefinition

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Picklist

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

```
SourceSystemIdentifier

UnitOfMeasureId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the attribute definition in an external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the measurement unit for this attribute.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

Add asset descriptors to the Asset object instead of creating multiple custom attributes on an asset. This helps scale to a high volume
of various assets in the system. When you create the AttributeDefinition, you can provide a unique API name. If the API name is not
unique, the system appends a number to the end of the API name. The value of this number depends on how many times the same
name has been used.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects AttributePicklist

**AttributeDefinitionHistory on page 63**
History is available for tracked fields of the object.

**AttributeDefinitionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AttributeDefinitionShare on page 67**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

### AttributePicklist AttributePicklistValue

RecordsetFltrCritMonitor

### AttributePicklist

Represents a custom picklist for an asset attribute. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this picklist.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Datetime`

**•** `Number`


Standard Objects AttributePicklist

**Field** **Details**

**•** `Percent`

**•** `Text`

The default value is `Boolean` .

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
A description of the picklist. Maximum size is 32000 alphanumeric characters. Can include
the following special characters: @! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the picklist. Names must be unique.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the attribute picklist record.

This field is a polymorphic relationship field.


Standard Objects AttributePicklist

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Status

UnitOfMeasureId

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the unit of measure associated with the product.

This field is a relationship field.

This field is available when Revenue Cloud is enabled.

This field is available in API version 63.0 and later.

**Relationship Name**
UnitOfMeasure

**Refers To**
UnitOfMeasure

The AttributePicklist object is the parent object and the AttributePicklistValue object contains the picklist values. Let’s say you need an
asset attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for
the T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate
them with the parent record.


### Standard Objects AttributePicklistValue

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributePicklistHistory on page 63**
History is available for tracked fields of the object.

**AttributePicklistOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AttributePicklistShare on page 67**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

### AttributePicklistValue

RecordsetFltrCritMonitor

### AttributePicklistValue

Represents the values of an asset attribute picklist. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Abbreviation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short name of the picklist value that's displayed at run time. Use up to 255 alphanumeric
characters. Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $
”.


Standard Objects AttributePicklistValue

**Field** **Details**

```
Code

DisplayValue

IsDefault

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A picklist value code unique to the picklist. Maximum size is 80 alphanumeric characters.
Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The displayed picklist value if it’s different from the Name field. For example, the Name ‘5’
could have a DisplayValue ‘Five’.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the picklist value is the default for the associated picklist. Only one value
can be the default for a picklist.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last viewed.

**Type**
string


Standard Objects AttributePicklistValue

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute picklist value.

```
PicklistId

Sequence

Status

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the picklist that the value is associated with.

This field is a relationship field.

**Relationship Name**
Picklist

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The order in which the picklist value appears in the picklist.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist value.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft` .

**Type**
string


### Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text value for a picklist item if the picklist data type is text. This value must be unique
within a picklist. Maximum size is 255 alphanumeric characters. Can include the following
special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

Usage

The AttributePicklistValue object is the child object and the AttributePicklist object contains the picklist. Let’s say you need an asset
attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for the
T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate them
with the parent record..

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributePicklistValueHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

RecordsetFltrCritMonitor

### AsyncReportRunEventLog

Async Report Run Event Log is used for reporting scheduled requests. This category includes dashboard refreshes, asynchronous reports,
schedule reports, and analytics snapshots. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects AsyncReportRunEventLog

Fields

**Field** **Details**

```
AverageRowSize

BucketCount

ClientIp

ColumnCount

CpuTime

DashboardIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average row size (in bytes) of all rows in the Asynchronous Report Run event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of buckets used in the report.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of columns in the report.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dashboard that was run.

```
DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

DisplayType

ExceptionFilterCount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
How much activity is occurring in the database.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time (in milliseconds) to complete the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total time spent in OracleJdbc calls, counting the Jdbc driver, Network, and Oracle time for
execs, fetches, and get-connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Possible values are:

**•** D—Dashboard

**•** S—Show Details

**•** H—Hide Details

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Description**
The number of exception filters used in the report.

```
IsPreview

LoginKey

ObjectName

Origin

RenderingType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is reserved for future use.

The default value is `false` .

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
The name of the object affected by the trigger.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Where the report is being executed, such as from a UI (Classic, Lightning, Mobile), through
an API (synchronous, asynchronous, Apex), or through a dashboard.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the format of the report output in Salesforce Classic. If the report was exported in
Lightning Experience, this field is blank.


Standard Objects AsyncReportRunEventLog

**Field** **Details**

```
ReportIdentifier

RequestIdentifier

RequestStatus

RowCount

RunTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The report’s ID.

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the Asynchronous Report Run event.

**Type**
double


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

```
SessionKey

SortOrder

Timestamp

Uri

UserIdentifier

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The sort column and order that was used in the report.

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


### Standard Objects Audience

**Field** **Details**

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

```
UserType

### Audience

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license. Possible values are:

**•** CsnOnly—Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** CspLitePortal—CSP Lite Portal license. Users whose access is limited because they’re
organization customers and access the application through a customer portal or an
Experience Cloud site.

**•** CustomerSuccess—Customer Success license. Users whose access is limited because
they’re organization customers and access the application through a customer portal

**•** Guest—Users whose access is limited so that your customers can view and interact with
your site without logging in.

**•** PowerCustomerSuccess—Power Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal. Users with this license type can view and edit data they directly own or data
owned by or shared with users below them in the customer portal role hierarchy.

**•** PowerPartner—Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** SelfService—Users whose access is limited because they’re organization customers and
access the application through a self-service portal.

**•** Standard—Standard user license. This user type also includes Salesforce Platform and
Salesforce Platform One user licenses, and admins for this org.

Represents an audience that is defined by criteria and can be assigned and used for targeting in an Experience Cloud site. This object is
available in API version 44.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects Audience

Fields

**Field** **Details**

```
AudienceName

ContainerId

Description

DeveloperName

FormulaFilterType

```

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Name of the audience.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the site or org that contains the audience. ContainerId is nillable in API versions 47.0
and earlier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the audience.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The unique name of the audience in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated, but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist


Standard Objects Audience

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Formula filter for the criteria used to define the audience. Valid values are:

**•** `AllCriteriaMatch` —Matching all the conditions (AND).

**•** `AnyCriterionMatches` —Matching at least one condition (OR).

**•** `CustomLogicMatches` —Matching condition logic (AND and OR) and numbered
criteria groups. This value is available in API version 45.0 and later.

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the audience. Valid values are:

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

**Type**
string

**Properties**
Filter, Group, Sort, Update


### Standard Objects AuraDefinition

**Field** **Details**

**Description**
Master label for the audience. This internal name doesn’t get translated.

### AuraDefinition

Represents an Aura component definition, such as component markup, a client-side controller, or an event. This object is available in
API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

### `AuraDefinitionBundleId`

```
DefType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the bundle containing the definition. A bundle contains a Lightning
definition and all its related resources.

This is a relationship field.

**Relationship Name**
### AuraDefinitionBundle

**Relationship Type**
Lookup

**Refers To**
### AuraDefinitionBundle

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AuraDefinition

**Field Name** **Details**

**Description**

The definition type. Valid values are:

**•** `APPLICATION`                       - Lightning Aura Components app

**•** `CONTROLLER`                       - client-side controller

**•** `COMPONENT`                       - component markup

**•** `EVENT`                       - event definition

**•** `HELPER`                       - client-side helper

**•** `INTERFACE`                       - interface definition

**•** `RENDERER`                       - client-side renderer

**•** `STYLE`                       - style (CSS) resource

**•** `PROVIDER`                       - reserved for future use

**•** `MODEL`                       - deprecated, do not use

**•** `TESTSUITE`                       - reserved for future use

**•** `DOCUMENTATION`                       - documentation markup

**•** `TOKENS`                       - tokens collection

**•** `DESIGN`                       - design definition

**•** `SVG`                       - SVG graphic resource

**•** `MODULE`                       - reserved for future use

```
Format

Source

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The format of the definition. Valid values are:

**•** `XML` for component markup

**•** `JS` for JavaScript code

**•** `CSS` for styles

**•** `TEMPLATE_CSS` reserved for future use

**•** `SVG` for an SVG graphic

**Type**
textarea

**Properties**
Create, Update

**Description**
The contents of the definition. This is all the markup or code for the definition.


### Standard Objects AuraDefinitionBundle

Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/)

### AuraDefinitionBundle

Represents a Lightning Aura component definition bundle, such as a component or application bundle. A bundle contains a Lightning
Aura component definition and all its related resources. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ApiVersion

Description

DeveloperName

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this bundle. Every bundle has an API version specified at
creation.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text description of the bundle. Maximum size of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.


Standard Objects AuraDefinitionBundle

**Field Name** **Details**

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

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
The language of the `MasterLabel` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for the Lightning bundle. This internal label doesn’t get translated.

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


### Standard Objects AuraDefinitionBundleInfo

Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/)

### AuraDefinitionBundleInfo

For internal use only.

### AuraDefinitionInfo

For internal use only.

### AuraRequestEventLog

Aura Request Event Log contains details of requests to Apex methods from Aura and Lightning web components. This object is available
in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ActionMessage

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action (Apex method) names and times for all the actions in the request in the format.
For example: `action1Name=action1Time;action2Name=action2Time...`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AuraRequestEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

```
CpuTime

DatabaseTotalTime

LoginKey

RequestIdentifier

RequestMethod

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
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime`
to determine whether performance issues are occurring in the database layer or in your own
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
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string


Standard Objects AuraRequestEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request, such as `GET` or `POST` .

```
RequestStatus

RunTime

SessionKey

Timestamp

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


Standard Objects AuraRequestEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Uri

UserAgent

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
The numeric code for the type of client used to make the request (for example, the browser,
application, or API) as a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

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


### Standard Objects AuthConfig

**Field** **Details**

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

### AuthConfig

Represents authentication options for My Domain and Experience Cloud site login pages. This object is available in API version 32.0 and
later.

The fields for this object control the options that display on the login page of an org. By default, you have a My Domain and corresponding
login page. If you use Digital Experiences, you can also set up a login page for each of your Experience Cloud sites.

**•** Logging in with a username and password

**•** Using SAML for single sign-on

**•** Authentication provider logins from a third-party service, such as Facebook or Twitter

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have “View Setup and Configuration” permission to view the settings.

Fields

**Field Name** **Details**

```
AuthOptionsAuthProvider

```

**Type**
boolean

**Properties**
Filter


Standard Objects AuthConfig

**Field Name** **Details**

**Description**

If `true`, at least one Auth. Provider is selected to show up on the login page,
and this object has child AuthConfigProvider objects for each provider.

```
AuthOptionsCertificate

AuthOptionsSaml

AuthOptionsUsernamePassword

DeveloperName

```

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, certificate-based login displays on the My Domain login page.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, at least one SAML configuration is selected to show up on the login
page. If the organization has only one SAML configuration, this value indicates
whether that configuration is selected to show up on the login page. If the
organization has multiple SAML configurations, see the child AuthConfigProvider
objects for each configuration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, the login option for a username and password appears on the login
page.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the domain created using My Domain or, for an Experience Cloud
site, a concatenated string of _`site name`_ _ _`site prefix`_ .

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


Standard Objects AuthConfig

**Field Name** **Details**

```
IsActive

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Whether this configuration is in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text that’s used to identify the Visualforce page in Setup.

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


### Standard Objects AuthConfigProviders

**Field Name** **Details**

```
Type

Url

### AuthConfigProviders

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The organization type for this object.

**•** `Org` (includes custom domains)

**•** `Community`

**•** `Site`

**•** Portal

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The login URL of the organization for this AuthConfig object. Each URL has only
one associated AuthConfig object.

Represents an authentication provider that’s configured in an organization. AuthConfigProviders is a child of the AuthConfig object. This
object is available in API version 32.0 and later.

This object links the authentication configuration for an organization to the Auth Provider through the `AuthOptionsAuthProvider`
[field of the AuthConfig object. The login page of a My Domain or Experience Cloud site can allow multiple SAML configurations and](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authconfig.htm)
multiple authentication providers. These configurations can be set to show up as buttons on the login page. Each configuration has an
AuthConfigProvider object. For more information about how to display these configurations on the login page, see these resources in
Salesforce Help.

**•** [My Domain: Add Identity Providers to the My Domain Login Page](https://help.salesforce.com/s/articleView?id=products.domain_name_login_id_prov.htm&type=5&language=en_US)

**•** [Experience Cloud: Configure Your Login Page](https://help.salesforce.com/s/articleView?id=xcloud.external_identity_login_pages_configure.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have “View Setup and Configuration” permission to view the settings.


### Standard Objects AuthorizationForm

Fields

**Field Name** **Details**

```
AuthConfigId

AuthProviderId

### AuthorizationForm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID for this configuration.

This is a relationship field.

**Relationship Name**
AuthConfig

**Relationship Type**
Lookup

**Refers To**
AuthConfig

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Auth. Provider or SAML configuration.

This is a polymorphic relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig

Represents the specific version and effective dates of a form that is associated with consent, such as a privacy policy or terms and
conditions. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects AuthorizationForm

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
DefaultAuthFormTextId

EffectiveFromDate

EffectiveToDate

IsSignatureRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the default authorization form text to use if text isn’t available
for a specific language.

This is a relationship field.

**Relationship Name**
DefaultAuthFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form takes effect.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form is no longer in effect.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the authorization form requires a signature.


Standard Objects AuthorizationForm

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

RevisionNumber

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
Required. The name of the authorization form.

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


### Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The revision number of the authorization form. For example, "rev1.21."

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormHistory**

History is available for tracked fields of the object.

**AuthorizationFormOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormShare**

Sharing is available for the object.

### AuthorizationFormConsent

Represents the date and way in which a user consented to an authorization form. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormTextId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The authorization form text that the Individual consented to.


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
AuthorizationFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

```
ConsentCapturedDateTime

ConsentCapturedSource

ConsentCapturedSourceType

ConsentGiverId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The date and time that consent was given.

**Type**
string

**Properties**
Create, Filter, Group, Nillable Sort, Update

**Description**
Required. The source through which consent was captured. For example,
user@example.com, www.example.com.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The source type through which consent was captured. For example,
phone, email, or website.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the person consenting to the authorization form.

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, CareProgramEnrollee, Contact, Individual, User

```
DocumentVersionId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the document version for which consent is given.

This is a relationship field.

**Relationship Name**
DocumentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

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


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Description**

Required. The name of the authorization form consent.

```
OwnerId

RelatedRecordId

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The ID of the owner of the account associated with this customer.

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

The ID of a record showing consent of an authorization form.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Visit

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the authorization form.

Possible values are:

**•** `Rejected`

**•** `Seen`


### Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**•** `Signed`

```
PartyId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field was removed in API version 47.0. Use `ConsentGiverId` instead.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AuthorizationFormConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**AuthorizationFormConsentHistory**

History is available for tracked fields of the object.

**AuthorizationFormConsentOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormConsentShare**

Sharing is available for the object.

### AuthorizationFormDataUse

Represents the data use consented to in an authorization form. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormId

```

**Type**
reference


Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
AuthorizationForm

```
DataUsePurposeId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Identifies the data use purpose record associated with the authorization
form.

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
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

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
Required. The name of the authorization form data use.

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

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormDataUseChangeEvent (API version 62.0)**
Change events are available for the object.

**AuthorizationFormDataUseHistory**

History is available for tracked fields of the object.

**AuthorizationFormDataUseOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormDataUseShare**

Sharing is available for the object.


### Standard Objects AuthorizationFormText AuthorizationFormText

Represents an authorization form’s text and language settings. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormId

ContentDocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
### AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
### AuthorizationForm

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentDocument that provides the authorization form’s text.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup


Standard Objects AuthorizationFormText

**Field Name** **Details**

**Refers To**
ContentDocument

```
DetailAuthorizationFormText

FullAuthorizationFormUrl

LastReferencedDate

LastViewedDate

Locale

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A detailed version of the authorization form.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL where the full text of the authorization form is located.

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

picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. `Locale` and `LocaleSelection` have the same
function.


### Standard Objects AuthProvider

**Field Name** **Details**

Note: `Locale` can contain custom values not included in the picklist
if added before version 47.0.

```
LocaleSelection

Name

SummaryAuthFormText

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. `Locale` and `LocaleSelection` have the same
function.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form text.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A shortened version of the authorization form that is displayed to the user.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormTextChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormTextHistory**

History is available for tracked fields of the object.

### AuthProvider

Represents an authentication provider (auth provider). An auth provider lets users log in to your Salesforce org from an external service
provider, such as Facebook, Google, or GitHub. This object is available in API version 27.0 and later.


Standard Objects AuthProvider

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with Customize Application and Manage AuthProviders permissions can access this object.

Fields

**Field Name** **Details**

```
AppleTeam

AuthorizeUrl

ConsumerKey

ConsumerSecret

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. A
10-character team ID, obtained from an Apple developer account. Available in
API version 48.0 and later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required when creating an OpenID Connect authentication provider. The OAuth
authorization endpoint URL. Available in API version 29.0 and later. In API version
33.0 and later, for Salesforce-managed auth providers, leave the field blank to let
Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The app’s key that is registered at the third-party (external) authentication
provider. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Nillable


Standard Objects AuthProvider

**Field Name** **Details**

**Description**

The consumer secret of the authentication provider that is registered at the
third-party SSO provider. It’s used by the consumer for identification to Salesforce.
In API version 33.0 and later, for Salesforce-managed auth providers, leave the
field blank to let Salesforce supply and manage the value. You can create your
own consumer secret on `create()` . However, after you set it, you can’t change
the value.

```
CustomMetadataTypeRecord

DefaultScopes

DeveloperName

EcKey

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when creating a custom authentication provider plug-in. The API name
of the custom authentication provider. Available in API version 36.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

For OpenID Connect authentication providers, the scopes to send with the
authorization request, if not specified when a flow starts. Available in API version
29.0 and later. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Required. Used when referring to the authentication provider from a program.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. Available
in API version 48.0 and later.


Standard Objects AuthProvider

**Field Name** **Details**

```
ErrorUrl

ExecutionUserId

FlowDefaultAccountId

FlowDefaultProfileId

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

A custom error URL for the authentication provider to use to report errors.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Required to specify a registration handler. The username of the Salesforce admin
or system user who runs the Apex handler or flow. The execution user provides
the context in which the registration handler runs. For example, if the handler
creates a contact, the creation can be easily traced back to the registration process.
In production, use a system user. The user must have the Manage Users
permission. Available in API version 27.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For authentication providers that use a flow registration handler, the default
account that new external users are assigned to. If you include this field, Salesforce
automatically uses it for the `defaultAccountId` variable in the
Authentication Provider User Registration standard flow.

A default account is required to use a flow registration handler for external users.
You can specify a default account here or in the flow itself. If you use both, the
default account that's configured in the flow takes precedent.

Available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For authentication providers that use a flow registration handler, the default
profile that new users are assigned to. If you include this field, Salesforce
automatically uses it for the `defaultProfileId` variable in the
Authentication Provider User Registration standard flow.


Standard Objects AuthProvider

**Field Name** **Details**

A default profile is required to use a flow registration handler. You can specify a
default profile here or in the flow itself. If you use both, the default profile that's
configured in the flow takes precedent.

Available in API version 64.0 and later.

```
FriendlyName

IconUrl

IdTokenIssuer

LinkKickoffUrl

LogoutUrl

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Required. A user-friendly name for the authentication provider.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The path to an icon to use as a button on the login page. Users click the button
to log in with the associated authentication provider, such as Twitter or Facebook.
Available in API version 32.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The source of the authentication token in `https:` URI format. This field is
available when configuring an OpenID Connect or Microsoft authentication
provider. If provided, Salesforce validates the returned `id_token` value. OpenID
Connect requires returning an `id_token` value with the `access_token`
value. Available in API version 30.0 and later.

**Type**
url

**Properties**
Nillable

**Description**
The URL for linking existing Salesforce users to a third-party account. This field is
read-only. Available in API version 43.0 and later.

**Type**
url


Standard Objects AuthProvider

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The destination for users after they log out if they authenticated using single
sign-on. The URL must be fully qualified with an http or https prefix, such as
`https://acme.my.salesforce.com` . Available in API version 33.0 and
later.

```
OauthKickoffUrl

OptionsIncludeOrgIdInId

OptionsIsPkceEnabled

```

**Type**
url

**Properties**
Nillable

**Description**
The URL for obtaining OAuth access tokens for a third party. This field is read-only.
Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Used to differentiate between users with the same user ID from two sources
(such as two sandboxes). If enabled ( `true` ), Salesforce stores the org ID of the
third-party identity in addition to the user ID. After you enable this setting, you
can’t disable it. Applies only to a Salesforce-managed auth provider. Available in
API version 32.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If set to `true`, the authentication provider uses the OAuth 2.0 Proof Key for Code
Exchange (PKCE) extension, which improves the security of the provider’s
authorization flow. This field applies only to these `providerType` values:

**•** `Custom`

**•** `Facebook`

**•** `Google`

**•** `Microsoft`

**•** `OpenIdConnect`

**•** `Salesforce` .


Standard Objects AuthProvider

**Field Name** **Details**

This field is available in API version 59.0 and later.

```
OptionsRequireMfa

OptionsSendAccessTokenInHeader

OptionsSendClientCredentialsInHeader

OptionsSendSecretInApis

```

**Type**
boolean

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this auth
provider based on the MFA status of each user. For this setting to trigger MFA,
you must apply MFA directly to users via one of two methods. 1) Assign the user
permission Multi-Factor Authentication for User Interface Logins. 2) Enable the
org setting Require multi-factor authentication (MFA) for all direct UI logins to
your Salesforce org.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

If enabled ( `true` ), the access token is sent to the `UserInfoUrl` in a header
instead of a query string. Available in API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Required when creating an OpenID Connect authentication provider. If enabled
( `true` ), the client credentials are sent in a header to the `tokenUrl` instead
of a query string. The credentials are in the standard OpenID Connect Basic
Credentials header format, which is `Basic <token>`, where `<token>` is
the base64-encoded string `"clientkey:clientsecret"` . Available in
API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Determines whether the encrypted consumer secret appears in API responses.
If enabled (default), the secret appears in the response. If disabled ( `false` ),


Standard Objects AuthProvider

**Field Name** **Details**

responses don’t include the consumer secret. For security, you can disable the
setting. However, keep in mind that:

**•** By disabling this setting, the consumer secret is excluded from API responses
in all API versions.

**•** Change sets and other metadata deployments break because both the
consumer key and secret are expected. To fix this problem, insert the
consumer key manually during deployment.

Available in API version 47.0 and later.

```
PluginId

ProviderType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An existing Apex class that extends the
`Auth.AuthProviderPluginClass` abstract class. Available in API version
39.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Required. The third-party authentication provider to use. Valid values include:

**•** `Apple` . Available in API version 48.0 and later.

**•** `Bitbucket` —Provides authentication for a `Bitbucket` provider. Enables
you to connect to Bitbucket from a Lightning Platform application. When
logged in to Bitbucket, the app can makes calls to Bitbucket APIs. The
`Bitbucket` provider isn’t available as an SSO provider, so users can’t log
in to a Salesforce org using their Bitbucket login credentials. Available in API
version 61.0 and higher.

**•** `Custom` —A provider configured with a custom authentication provider
plug-in. Available in API version 36.0 and later.

**•** `Facebook` .

**•** `GitHub` —Provides authentication for a `GitHub` provider. Used to log in
users of your Lightning Platform app to GitHub using OAuth. When logged
in to GitHub, your app can make calls to GitHub APIs. The `GitHub` provider
isn’t available as an SSO provider, so users can’t log in to your Salesforce org
using their GitHub login credentials. Available in API version 35.0 and later.

**•** `Google` .

**•** `Janrain` .

**•** `LinkedIn` . Available in API version 32.0 and later.


Standard Objects AuthProvider

**Field Name** **Details**

**•** `Microsoft` . Provides authentication for all services that can be accessed
via Microsoft Azure Active Directory. Available in API version 55.0 and later.

**•** `MicrosoftACS` —Microsoft Access Control Service provides authentication
for a Microsoft Office 365 service, like SharePoint Online. The
`MicrosoftACS` provider doesn't support SSO. Available in API version
31.0 and later.

**•** `OpenIdConnect` . Available in API version 29.0 and later.

**•** `Salesforce` .

**•** `Slack` . Available in API version 54.0 and later.

**•** `Twitter` . Available in API version 32.0 and later.

```
RegistrationHandlerId

SsoKickoffUrl

TokenUrl

UserInfoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An existing Apex class that implements the `Auth.RegistrationHandler`
interface.

**Type**
url

**Properties**
Nillable

**Description**
The URL for performing SSO into Salesforce from a third party by using its
third-party credentials. This field is read-only. Available in API version 43.0 and
later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The OAuth token endpoint URL of an OpenID Connect authentication provider.
Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers for sandbox use cases only, leave the field
blank to let Salesforce supply and manage the value.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects AuthProvParamFwdAllowlist

**Field Name** **Details**

**Description**

The OpenID Connect endpoint URL of the OpenID Connect authentication
provider. Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers, leave the field blank to let Salesforce supply
and manage the value.

### AuthProvParamFwdAllowlist

Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization
URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales` parameter and use
it to send a user's language preference from Salesforce to the third-party provider's login page. This object is available in API version
62..0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AuthProviderId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the authentication provider associated with the allowlist.

This field is a relationship field.

**Relationship Name**
AuthProvider

**Refers To**
AuthProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description for the allowlisted URL parameter.


### Standard Objects AuthSession

**Field** **Details**

```
Param

### AuthSession

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the parameter, such as `ui_locales` or `login_hint` .

The AuthSession object represents an individual user session in your organization. This object is available in versions 29.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
CreatedDate

Id

IsAssociatedWithJwtAccessToken

```

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was created. This field is a standard system field.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, ID Lookup, Sort

**Description**
The current session’s ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the session is associated with a JSON Web Token (JWT)-based access
token. This field is available in API version 64.0 and later.


Standard Objects AuthSession

**Field Name** **Details**

```
IsCurrent

LastModifiedDate

LoginGeoId

LoginHistoryId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the session is a member of the user’s current session family. This field
is available in API version 37.0 and later.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was last updated. A session expires when the
current date and time equals `LastModifiedDate` + `NumSecondsValid` .
This field is a standard system field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
login event. Due to the nature of geolocation technology, the accuracy of
geolocation fields (for example, country, city, postal code) can vary. This field is
available in API version 34.0 and later.

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
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for a successful login event. When a session is reused,
Salesforce updates the `LoginHistoryId` with the value from the most
recent login. This field is available in API version 33.0 and later.


Standard Objects AuthSession

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
LoginHistory

**Relationship Type**
Lookup

**Refers To**
LoginHistory

```
LoginType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** `AJAX Toolkit`

**•** `Apex Office Toolkit`

**•** `AppExchange`

**•** `Application`

**•** `AppStore`

**•** `Certificate-based login`

**•** `Chatter Communities External User`

**•** `Chatter Communities External User Third Party SSO`

**•** `Community`

**•** `Customer Service Portal Third-Party SSO`

**•** `Customer Service Portal`

**•** `DataJunction`

**•** `DB Replication`

**•** `Employee Login to Community`

**•** `Excel Integration`

**•** `Help and Training`

**•** `HOTP YubiKey`

**•** `Lightning Login`

**•** `Networks Portal API Only`

**•** `Offline Client`

**•** `Order Center`

**•** `Other Apex API`

**•** `Outlook Integration`

**•** `Partner Portal Third-Party SSO`

**•** `Partner Portal`


Standard Objects AuthSession

**Field Name** **Details**

**•** `Partner Product`

**•** `Passwordless Login`

**•** `Remote Access 2.0`

**•** `Remote Access Client`

**•** `Sales Anywhere`

**•** `Salesforce Outlook Integration`

**•** `Salesforce.com Website`

**•** `SAML Chatter Communities External User SSO`

**•** `SAML Customer Service Portal SSO`

**•** `SAML Idp Initiated SSO`

**•** `SAML Partner Portal SSO`

**•** `SAML Sfdc Initiated SSO`

**•** `SAML Site SSO`

**•** `Self-Service`

**•** `Signup`

**•** `Sync`

**•** `SysAdmin Switch`

**•** `Third Party SSO`

**•** `Unknown`

**•** `Validate`

```
LogoutUrl

NumSecondsValid

ParentId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The page or view to display after users log out of an Experience Cloud site, or an
org if they authenticated using SAML. This field is available in API version 32.0
and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of seconds before the session expires, starting from the last update
time.

**Type**
reference


Standard Objects AuthSession

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the parent session, if one exists (for example, if the current
session is for a canvas app). If the current session doesn’t have a parent, this value
is the current session’s own ID.

```
SessionSecurityLevel

SessionType

SourceIp

UserType

UsersId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Standard or High, depending upon the authentication method used.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of session. Common ones are UI, Content, API, and Visualforce.

[For more information, see User Session Types in the](https://help.salesforce.com/s/articleView?id=xcloud.security_session_types.htm&type=5&language=en_US) _Object Reference Guide_ .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
IP address of the end user’s device from which the session started. This address
can be an IPv4 or IPv6 address.

The `SourceIp` field doesn't support the `LIKE` [comparison operator.](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_comparisonoperators.htm)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The kind of user for this session. Types include Standard, Partner, Customer Portal
Manager, High Volume Portal, and CSN Only.

**Type**
reference


### Standard Objects AutomatedAction

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s Salesforce user ID.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

Usage

The AuthSession object exposes session data and enables read and delete operations on that data. For example, use this object to see
who is signed in to your org. Or you can use this object to create a tool to delete a session, ending that user’s session. For a user, only
their own sessions are available, while administrators can see all sessions.

You can’t change user sessions with this object. You can only read and delete them.

### AutomatedAction

Represents the configuration of an automated action, such as a workflow rule. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. API version to use for executing the automated action.


Standard Objects AutomatedAction

**Field** **Details**

```
Description

ErrorDetail

ErrorMessage

EvalType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the error encountered when executing the automated action.

Possible values are:

**•** `invalidCondition`

**•** `invalidConditionReference`

**•** `invalidConditionValue`

**•** `invalidInvocableAction`

**•** `invalidInvocableActionParam`

**•** `invalidReferenceEntity`

**•** `unknownError`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the error encountered when executing the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
When the automated action runs.

Possible values are:

**•** `OnCreate`

**•** `OnCreateAndUpdate`


Standard Objects AutomatedAction

**Field** **Details**

```
ExecutionType

ExtraFilterExpression

ExtraFilterType

FilterExpression

FilterType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Whether the action runs automatically or generates a reminder.

Possible values are:

**•** `Automatic`

**•** `Reminder`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional condition logic for cross-object filters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Additional criteria for cross-object filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If `FilterType` is `Advanced`, this field contains the condition logic.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AutomatedAction

**Field** **Details**

**Description**
Criteria for filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`

```
InvocationName

IsLocked

LastEditedDateTime

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Invocable action to execute.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record is locked or not.

The default value is `false` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the automated action had a change that impacted rule evaluation.

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


Standard Objects AutomatedAction

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record was likely referenced ( `LastReferencedDate` ) and not viewed.

```
MayEdit

Name

ReferenceEntity

RuleType

State

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the automated action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Entity on which the automated action operates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of workflow rule.

Possible values are:

**•** `ManagerAssigned`

**•** `ManagerSubscribed`

**•** `Personal`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects AutomatedActionCondition

**Field** **Details**

**Description**
The status of the alert.

Possible values are:

**•** `Active`

**•** `Error`

**•** `Inactive`

```
SubscriptionState

Summary

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
For users who don’t have an override, the default value of the subscription.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A human-readable explanation of the automated action, its conditions, and its parameters.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionShare on page 67**
Sharing is available for the object.

### AutomatedActionCondition

Represents the logical operator details for evaluating conditions in an automated action. This object is available in API version 57.0 and
later.


Standard Objects AutomatedActionCondition

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutomatedActionId

ConditionNumber

IsLocked

MayEdit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference number of the condition containing advanced filter logic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AutomatedActionCondition

**Field** **Details**

**Description**
Indicates whether the automated action condition record can be edited or not.

The default value is `false` .

```
Operator

ReferenceField

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The logical operator for this condition.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `IsChanged`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `StartsWith`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to use for this condition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of condition.

Possible values are:

**•** `ExtraFilterCondition`

**•** `PrimaryFilterCondition`


### Standard Objects AutomatedActionOverride

**Field** **Details**

```
Value

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to compare to the `ReferenceField` .

### AutomatedActionOverride

Represents a modified attribute of a shared automated action. For example, the modified attribute can contain customizations for your
business. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
FieldName

IsLocked

IsRelatedRecordOverridable

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the field to override.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AutomatedActionOverride

**Field** **Details**

**Description**
Indicates whether the parent automated action record can be overridden.

The default value is `false` .

```
MayEdit

Name

RelatedRecordApiName

RelatedRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the automated action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object name of the `RelatedRecordId` .

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the automated action.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
AutomatedAction, FtestUser


### Standard Objects AutomatedActionParameter

**Field** **Details**

```
Value

```

Associated Objects

**Type**
textarea

**Properties**
Create, Update

**Description**
The overridden value used for `FieldName` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionOverrideOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionOverrideShare on page 67**
Sharing is available for the object.

### AutomatedActionParameter

Represents the values or field references evaluated by the automated action. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutomatedActionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
### AutomatedAction

**Relationship Type**
Lookup


Standard Objects AutomatedActionParameter

**Field** **Details**

**Refers To**
AutomatedAction

```
DataType

IsLocked

MayEdit

ParameterName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the value or field reference value.

Possible values are:

**•** `Boolean`

**•** `Double`

**•** `Int`

**•** `None`

**•** `String`

**•** `ValueList`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the invocable action parameter the value maps to.


### Standard Objects AutomatedActionReminder

**Field** **Details**

```
ReferenceField

Value

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reference to the field that’s resolved at runtime. For example, LeadID. If `Value` has a
value, this field is null.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to be passed to the invocable action parameter at runtime. If `ReferenceField`
has a value, this field is null.

### AutomatedActionReminder

Represents a reminder to the end user to take an action in the future. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionTakenDateTime

AutomatedActionId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Timestamp of when the user took the action suggested by the reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AutomatedActionReminder

**Field** **Details**

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

```
IsLocked

IsValidForUser

MayEdit

ReferenceRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action is active and accessible to the user who owns the
record ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record can be edited or not.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AutomatedActionReminder

**Field** **Details**

**Description**
The record that triggered the reminder. For example, when a rule is set to Case, the value of
this field is `CaseId` .

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact, Invoice, Lead, Opportunity

```
StartDateTime

State

Type

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time this reminder is scheduled to be displayed to the user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the reminder.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Disabled`

**•** `Dismissed`

**•** `Expired`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of automated action reminder.

Possible values are:

**•** `Reminder`


### Standard Objects BackgroundOperation

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionReminderOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionReminderShare on page 67**
Sharing is available for the object.

### BackgroundOperation

Represents a background operation in an asynchronous job queue. This object is available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `retrieve()`

Special Access Rules

### • BackgroundOperation doesn’t support search.

Fields

**Field Name** **Details**

```
Error

ExecutionGroup

ExpiresAt

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the execution group.

**Type**
dateTime


Standard Objects BackgroundOperation

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
After this time, the operation is removed from the asynchronous job queue.
Applies only if the operation has a status of complete, canceled, error, or merged.

```
FinishedAt

GroupLeaderId

Name

NumFollowers

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation reached the status of completed or error.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the operation that’s selected as the
leader of the execution group.

This field is a relationship field.

**Relationship Name**
GroupLeader

**Relationship Type**
Lookup

**Refers To**
BackgroundOperation

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Identifies the background operation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BackgroundOperation

**Field Name** **Details**

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Number of other operations that are in the
execution group.

```
ParentKey

ProcessAfter

RetryBackoff

RetryCount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Tag that identifies related sets of operations, if any.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The operation is scheduled to be processed after this time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation has an error status. The first retry is attempted
immediately. Each subsequent retry is increasingly delayed according to an
exponential expression that’s multiplied by the `RetryBackoff`, in milliseconds.

Specifically, the delay time is `(2` `[n]` `-1)×R`, where `n` is the `RetryCount`, and
`R` is the `RetryBackoff` .

The default value for `RetryBackoff` depends on the type of operation. For
example, the `RetryBackoff` default for write operations on external objects
is 1,000 milliseconds. For write operations, retries are attempted immediately,
after 3 seconds, after 7 seconds, after 15 seconds, and so on.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Number of attempted retries. Applies only if the operation has an error status.


Standard Objects BackgroundOperation

**Field Name** **Details**

```
RetryLimit

SequenceGroup

SequenceNumber

StartedAt

Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Maximum number of retries to attempt. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence group. Applies only if the operation is merged with other
operations into an execution group to be processed in bulk. Within an execution
group, operations can be placed into a sequence group to be executed in a
specific order.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Order position within the sequence group. Applies only if the operation is merged
with other operations into an execution group to be processed in bulk. Within
an execution group, operations can be placed into a sequence group to be run
in a specific order.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

When the operation started running.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the background operation. The options are:


Standard Objects BackgroundOperation

**Field Name** **Details**

**•** `New`

**•** `Scheduled`

**•** `Canceled`

**•** `Merged`

**•** `Waiting`

**•** `Running`

**•** `Error`

**•** `Complete`

```
SubmittedAt

Timeout

Type

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation was added to the job queue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maximum time in milliseconds to wait for results after the operation started
running.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the background operation. The options are:

**•** `ApiCatalogPoller`

**•** `BlockchainEventPoller`

**•** `CdpMetadataDeploy`

**•** `ExternalChangeDataCapture`

**•** `ExternalConnectivityPoller`

**•** `ExternalObject`

**•** `ExternalObjectSync`

**•** `ExternalServiceCallback`

**•** `MetadataChangesetOperation`

**•** `MfgBulkUpdate`


### Standard Objects BackgroundOperationResult

**Field Name** **Details**

**•** `PrivateConnectMigration`

**•** `SingularityAutoSync`

**•** `SingularityMDSSync`

**•** `SingularitySchemaEvolutionTrigger`

**•** `SiteTaskCreate`

**•** `SiteTaskPublish`

**•** `Sweeper`

**•** `WebCart`

**•** `XClean`

```
WorkerUri

```

Usage

Use the BackgroundOperation object to:

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
URI of the worker that performed the operation.

Example for a Salesforce Connect OData operation:

```
  services/data/v35.0/xds/upsert

```

**•** Monitor the job status of asynchronous operations.

**•** View errors that are related to the asynchronous operations.

**•** Extract statistics for the asynchronous job queue.

### BackgroundOperationResult

Stores error messages generated when or importing data into big objects using Bulk API. This is a big object, available in API version
37.0 and later.

### Each instance of BackgroundOperationResult represents one error. The Message field stores the text of the error message.

The `ParentID` field stores the:

**•** Batch ID for the data import, in case of Bulk API

Bulk API validates data at the time of import, and generates an error message for the first occurrence of invalid data in any row of the
data file. The validation performed depends on the type of data being imported.

**•** **Text** —The length of the input string must be less than or equal to the length of the corresponding text field in the target object.

**•** **Number** —The input data must be a number, whose scale and precision are compatible with the corresponding number field in
the target object.


Standard Objects BackgroundOperationResult

**•** **ID—** The input data must be a valid 15- or 18-character ID.

**•** **DateTime** —The input data must be a valid dateTime value, in the approved format.

**•** **Lookup** —The lookup value must be a valid 15- or 18-character ID.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
CreatedById

CreatedDate

Data

Id

Message

```

**Type**
ID

**Properties**
Nillable

**Description**
The user ID of the user initiating the Bulk API request.

**Type**
dateTime

**Properties**
Defaulted on create

**Description**
The date and time at which the Bulk API request was made.

**Type**
string

**Properties**
Nillable

**Description**
The data that generated the error message. The total length is limited to 2,000
characters, and each column can occupy a maximum of 50 characters. Any data
exceeding those limits is truncated.

**Type**
ID

**Properties**
Defaulted on create, idLookup

**Description**
The ID of the error message.

**Type**
string


### Standard Objects BatchApexErrorEvent

**Field Name** **Details**

**Properties**
Nillable

**Description**
The text of the error message.

```
MessageType

ParentId

```

Usage

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The type of error message. The possible values are: ERROR, WARNING, or INFO.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The batch ID in Bulk API.

You can check for errors by querying the `BackgroundOperationResult` object. For example, this query returns details of all
errors in a data file imported using Bulk API, whose batch ID is `751xx000000006OAAQ` .

```
SELECT CreatedbyId, CreatedDate, Id, Message, MessageType, ParentId FROM

BackgroundOperationResult WHERE ParentId = “751xx000000006OAAQ”

```

Note: You can only view errors resulting from Bulk API requests that you initiated, unless you have the global permission to view
all data.

### BatchApexErrorEvent

[The documentation has moved to BatchApexErrorEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_batchapexerrorevent.htm) _Platform Events Developer Guide_ .

### BillingBatchScheduler

Represents a scheduled processing job that triggers recurring invoice batch runs and payment batch runs in Subscription Management.
This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`


Standard Objects BillingBatchScheduler

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchscheduler.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchscheduler.htm)

Fields

**Field** **Details**

```
BillingSchedulerName

Comments

CronExpression

EndDate

FrequencyCadence

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the scheduler.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional field for comments about the scheduler.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Determines how often the scheduler recurs.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the scheduler stops triggering batch processing jobs.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects BillingBatchScheduler

**Field** **Details**

**Description**
Indicates how often the scheduler triggers the invoice batch run or the payment batch run.

Possible values are:

**•** `Daily` —The scheduled job recurs every day.

**•** `Monthly` —The scheduled job recurs every month.

**•** `Once` —The scheduled job occurs one time and doesn’t recur.

**•** `Weekly` —The scheduled job recurs every week.

```
FrequencyOptions

JobType

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Nillable

**Description**
Derived field that stores the scheduler configuration.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of batch processing job that the scheduler triggers.

Possible values are:

**•** `Invoice` —The scheduler starts a batch invoice run.

**•** `Payment` —The scheduler starts a batch payment run.

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


Standard Objects BillingBatchScheduler

**Field** **Details**

```
NextRunTime

OwnerId

RecurringSubType

RecurringType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and timestamp of the next scheduled batch invoice run or batch payment run are
shown in the user's time zone.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who created the scheduler.

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
Specifies the frequency at which the batch processing job recurs when the
`FrequencyCadence` is set to _Monthly_ .

Possible values are:

**•** `Every` —The processing job recurs at every instance of the frequency of the value. For
example, if the `RecurringSubType` is _`Every`_ and the `FrequencyCadence`
is _`Weekly`_, then the batch processing job recurs every week.

**•** `SpecificDate` —The scheduler triggers the batch processing job on the selected
date. For example, if the selected date is _`5`_, and the `FrequencyCadence` is
_`Monthly`_, then the job recurs on the fifth day of each month.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects BillingBatchScheduler

**Field** **Details**

**Description**
Specifies the frequency at which the batch processing job is repeated when the
`FrequencyCadence` is set to _Weekly_ .

Possible values are:

**•** `Every`

```
RecursOn

RecursOnDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the interval at which the scheduler triggers a batch processing job.

If the FrequencyCadence is _`Monthly`_, you must select either the specific date or the interval
when the schedule triggers the job.

Possible values are:

**•** `First`

**•** `Fourth`

**•** `Last`

**•** `Second`

**•** `Third`

**Example:** To tell the scheduler to trigger the job on the first Monday of the month, set the
following fields:

**•** `FrequencyCadence` = _`Monthly`_

**•** `RecursOn` = _`First`_

**•** `RecursOnDay` = _`Monday`_

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the date on which the scheduler triggers a batch processing job.

**Example:** To tell the scheduler to trigger the job on the fifth day of the month, set the
following fields:

**•** `FrequencyCadence` = _`Monthly`_

**•** `RecursOnDate` = _`5`_

**Example:** To tell the scheduler to trigger the job on the second to last day of the month,
set the following fields:

**•** `FrequencyCadence` = _`Monthly`_


Standard Objects BillingBatchScheduler

**Field** **Details**

**•** `RecursOnDate` = _`SecondToLast`_

If you select _`Last`_, _`SecondToLast`_, or _`ThirdToLast`_, the date of the batch processing
job varies depending on the number of days in the month.

For example, suppose _`SecondToLast`_ is selected. If the month has 30 days, such as June,
then the batch processing job occurs on the 28th day. If the month has 31 days, such as July,
then the batch processing job occurs on the 29th day.

```
RecursOnDay

RunCriteriaId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the day on which the scheduler triggers a batch processing job.

If the `FrequencyCadence` field is set to _`Weekly`_, then you must select the day when
the scheduler runs. The scheduler recurs every week on the selected day; for example, weekly
on Monday.

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the filter criteria that’s defined for the invoice batch run or the payment batch run.

This field is a polymorphic relationship field.

**Relationship Name**
RunCriteria

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRunCriteria, PaymentBatchRunCriteria


### Standard Objects BillingPeriodItem

**Field** **Details**

```
StartDate

StartTime

Status

TimeZone

### BillingPeriodItem

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date when the scheduler triggers its first batch processing job.

**Type**
time

**Properties**
Filter, Sort

**Description**
The time when the scheduler triggers the batch processing job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the scheduler. Only Active schedulers can trigger batch processing jobs.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone is either the value selected when the run was configured, or it's the user's
time zone. The time zone is shown in Greenwich Mean Time (GMT).

Represents one payment period for a subscription. The billing period item is used to pass billing information to an invoice line item in
Subscription Management. This object is available in API version 55.0 and later.

When a billing schedule is invoiced, Subscription Management creates a billing period item to store the billing and payment information
that’s passed to an invoice line. Subscription Management next creates an invoice line for billing period items that match the invoice's


Standard Objects BillingPeriodItem

target date. One billing period item is created for each billing period in the billing schedule. For example, a one-year subscription that's
billed quarterly creates a billing schedule with four billing period items.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingperioditem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingperioditem.htm)

Fields

**Field** **Details**

```
Amount

BillingPeriodEndDate

BillingPeriodItemNumber

BillingPeriodStartDate

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Price for the billing period item. Used to calculate the invoice line's Amount field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's end date.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined number that refers to the billing period item.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's start date.


Standard Objects BillingPeriodItem

**Field** **Details**

```
BillingScheduleId

CurrencyIsoCode

InvoiceBatchRunId

InvoiceLineId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Parent billing schedule of the billing period item.

This field is a relationship field.

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the org. Available only for orgs with the
multicurrency feature enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Parent invoice batch run of the billing period item.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingPeriodItem

**Field** **Details**

**Description**
This field looks up to the invoice line that's generated from the billing period item. This field
is populated only when a billing period item is generated via an invoice batch run. Otherwise,
this field is empty.

This field is a relationship field.

**Relationship Name**
InvoiceLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

```
InvoiceStatus

Status

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the invoice that contains the invoice line created from the billing period item.

Valid values are:

**•** `Canceled` —The invoice for this billing period item was canceled.

**•** `Draft` —The invoice has been created but hasn’t been posted. Available in API version
60.0 and later.

**•** `DraftInProgress` —The invoice hasn’t been created yet. When the invoice is
created, the `InvoiceStatus` field value is changed to `Draft` . If the invoice
generation process fails, the `InvoiceStatus` field value shows
`DraftInProgress` . Available in API version 60.0 and later.

**•** `Error` —The invoice for this billing period item was generated in error.

**•** `Pending` —The invoice for this billing period item is being generated.

**•** `Posted` —An invoice line based on this billing period has been created and added
successfully to the invoice.

**•** `PostingInProgress` —An invoice line based on this billing period has been created
and is in the process of being added to the invoice. Available in API version 60.0 and
later.

**•** `Voided` —An invoice line based on this billing period was voided.

**•** `VoidInProgress` —An invoice line based on this billing period is in the process of
being voided.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects BillingPolicy

**Field** **Details**

**Description**
Status of the billing period item. Draft billing period items aren't evaluated for invoice line
creation.

Valid values are:

**•** `Canceled`

**•** `Draft`

**•** `Reviewed`

### BillingPolicy

Represents a group of billing treatments, which define the rules for how to invoice a customer for an order item. This object is available
in API version 55.0 and later.

Billing policies are related to products, which pass the policy on to the resulting order items. When an order is activated, Subscription
Management assigns a billing treatment to each order item based on the values in the `BillingTreatmentSelection` field.
Then Subscription Management uses the billing treatment to create billing schedules.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingpolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingpolicy.htm)

Fields

**Field** **Details**

```
BillingTreatmentSelection

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management assigns billing treatments to order items and to
assets related to the billing policy.

Possible values are:


Standard Objects BillingPolicy

**Field** **Details**

**•** `Default` —The value specified in the DefaultBillingTreatmentId field is automatically
applied to order items and assets.

**•** `Manual` —Users must specify the billing treatment that's applied to the order items
and assets.

```
DefaultBillingTreatmentId

Description

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When `BillingTreatmentSelection` has a value of `Default`, Subscription
Management uses the selected billing treatment for all order items and assets related to the
billing policy.

This field is a relationship field.

**Relationship Name**
DefaultBillingTreatment

**Relationship Type**
Lookup

**Refers To**
BillingTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description that describes the billing policy.

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


### Standard Objects BillingSchedule

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
Name

Status

### BillingSchedule

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the billing policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The billing policy's status.

Possible values are:

**•** `Active` —Indicates that the billing policy is available for use on products.

**•** `Draft` —Indicates that the billing policy isn't available for use on products. Use this
status when creating billing policies that aren't ready to be activated.

**•** `Inactive` —Indicates that the billing policy isn't available for use on products.

Stores the order item information used in the invoicing process. This object is available in API version 55.0 and later.

When you activate an order, Subscription Management creates one billing schedule for each order item in an order. For example, if an
order contains 15 order items, Subscription Management creates 15 billing schedules, one billing schedule for each item. The invoice
scheduler uses the information in the billing schedule to determine when it's time to invoice an order item.

Billing schedules for all order items that are generated from one asset are summarized in a billing schedule group.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).


Standard Objects BillingSchedule

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedule.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedule.htm)

Fields

**Field** **Details**

```
BillDayOfMonth

BilledAmount

BillingAccountId

BillingPeriodAmount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
An integer from 1 to 31 that indicates the day of the month.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount (excluding tax) that has been invoiced from the billing schedule.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
BillingAccount

**Refers To**
Account

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount to be invoiced each billing period.

For example, if the billing period is monthly, this field shows the monthly amount that appears
on the invoice line.


Standard Objects BillingSchedule

**Field** **Details**

```
BillingScheduleEndDate

BillingScheduleGroupId

BillingScheduleNumber

BillingScheduleStartDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last date that the billing schedule is available for invoicing. Inherited from the EndDate
field on the order item.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the billing schedule group that contains the billing schedule. Billing schedules are
grouped when they have the same source order item. The source order item is the original
order item that a customer bought. Afterwards, if the customer amends, cancels, or renews
the order item, a new billing schedule is created with the BillingScheduleGroupId for the
original order item.

This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Relationship Type**
Lookup

**Refers To**
BillingScheduleGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated reference number for the billing schedule.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the billing schedule is available for invoicing. Inherited from the ServiceDate
on the order item.


Standard Objects BillingSchedule

**Field** **Details**

```
BilledThroughPeriod

BillingTreatmentItemId

CancellationDate

Category

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last billing period that includes this date.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The billing treatment item used to configure invoiceable amounts on the billing schedule.

This field is a relationship field.

**Relationship Name**
BillingTreatmentItem

**Relationship Type**
Lookup

**Refers To**
BillingTreatmentItem

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date on which the subscriber can no longer access the service. For example, if a service
ends on August 31, then the cancellation date is September 1, because that’s the date when
the subscriber can no longer use the service.

Subscription Management doesn't invoice billing schedules past their cancellation date.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The business action represented by the billing schedule.

Possible values are:

**•** AmendQuantity—A billing schedule for an order that changes the quantity. This object
is available in API version 56.0 and later.

**•** Cancellation—A billing schedule for an order that was canceled


Standard Objects BillingSchedule

**Field** **Details**

**•** Original—A billing schedule for the initial order

**•** Renewal—A billing schedule for an order that was renewed

```
CurrencyIsoCode

InvoiceBatchRunId

InvoiceRunBatch

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the invoice.

The default value is USD.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The invoice batch run that evaluated this billing schedule and its billing period items to
produce an invoice.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The batch value used by the invoice run that evaluated this billing schedule. During an
invoice run, billing schedules with the same batch value (including null) are grouped to the
same invoice run.

For example, create one batch of invoices for Premium Customers and another batch for
Regular Customers.

Possible values are:

**•** Premium Customers

**•** Regular Customers


Standard Objects BillingSchedule

**Field** **Details**

```
NextBillingDate

NextChargeFromDate

OriginalBillingScheduleId

PendingAmount

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the next billing period starts for the invoice. Used to calculate which invoice
lines are included on an invoice. When an invoice scheduler or API evaluates an order for
invoicing, billing schedules with a next billing date on or before the invoice's target date are
included on the invoice.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the billing schedule is invoiced in the upcoming billing period. For example,
if you invoiced a customer for a billing period of 01/01/22 through 01/31/22, the billing
schedule's `NextChargeFromDate` is 02/01/22.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this billing schedule is an amended or canceled billing schedule, then this field shows the
original billing schedule. Otherwise, this field is null.

This field is a relationship field.

**Relationship Name**
OriginalBillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount from the current billing term that hasn't been billed yet. For example, the unbilled
amount for a month, quarter, or year, depending on this billing schedule's billing term.


Standard Objects BillingSchedule

**Field** **Details**

```
Quantity

ReferenceEntityId

ReferenceEntityItemId

Status

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The quantity of the order item that created the billing schedule.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent order of the order item that created the billing schedule.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order item or asset that created the billing schedule.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustementLineTime, or OrderItemSummary

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the order item that the billing schedule represents.


### Standard Objects BillingScheduleGroup

**Field** **Details**

Possible values are:

**•** `CompletelyBilled`

**•** `Error`

**•** `Processing`

**•** `ReadyForInvoicing`

```
TaxTreatmentId

TotalAmount

UnitPrice

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Shows the treatment used to calculate tax for the billing schedule. Defined based on the
order item's tax policy.

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
Filter, Nillable, Sort

**Description**
The total amount of the order item represented by the billing schedule.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The price for an individual unit of the billing schedule's parent order item, including charges,
adjustments, and discounts. Inherited from the order item's `UnitPrice` field.

### BillingScheduleGroup

Represents a consolidated view of all billing schedules related to the order items generated from one asset, including new orders and
amendment orders. This object is available in API version 55.0 and later.


Standard Objects BillingScheduleGroup

When an order is created, a billing schedule is generated for each order item. The billing schedule group summarizes fields from each
billing schedule. For example, it summarizes financial fields such as Total Billed Amount and Total Pending Amount and billing fields
such as Billing Day of Month and Billing Term.

The billing schedule group includes schedules generated from a new order item and schedules generated from amendment order items.
The billing schedule group shows users the summarized financial data that includes any changes, such as new orders or amendments,
made to the asset.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Subscription Management, Commerce Subscriptions, and Billing (Revenue Cloud). If your org has both
Subscription Management and Commerce Subscriptions, then Subscription Management takes precedence.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulegroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulegroup.htm)

Fields

**Field** **Details**

```
BillDayOfMonth

BillToContactId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Billing Day of Month for the billing schedules that comprise the billing schedule group.

Subscription Management uses the order item's billing day of month to calculate the order
item’s next billing date, which the billing schedule then inherits. For example, an order item
can be billed on the first day of the month.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The contact related to the billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.

**Relationship Name**
BillToContact


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
BillingAccountId

BillingAddress

BillingCity

BillingCountry

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Salesforce account for the billing schedule group.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the billing address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.


Standard Objects BillingScheduleGroup

**Field** **Details**

```
BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

BillingMethod

BillingPostalCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the billing address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLongitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –90 and 90 with up to 15 decimal places. See Compound Field](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of billing used for the source item.

Possible values are:

**•** `Evergreen`

**•** `OrderAmount`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
Details for the billing address of this billing schedule group. Maximum size is 20 characters.

```
BillingScheduleGroupNumber

BillingStartMonth

BillingState

BillingStreet

BillingTerm

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the billing schedule group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field used with annual billing. The field shows the numbers from 1 to 12, which
indicate the month when billing begins for an annual subscription. For example, if billing
starts in January, the value is 1; if billing starts in June, the value is 6. This field is available in
API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this billing schedule group.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used with `BillingTermUnit` to define a billing cycle. For example, bill every 20 days
or every two months. In this example, the `BillingTerm` is _`20`_ and the
`BillingTermUnit` is _`days`_


Standard Objects BillingScheduleGroup

**Field** **Details**

```
BillingTermUnit

BillingType

CancellationDate

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The frequency with which the billing schedule is invoiced.

Possible values are:

**•** `Day`

**•** `Month`

**•** `OneTime`

**•** `Quarter`

**•** `Semi-Annual`

**•** `Year`

Used with `BillingTermUnit` to define a billing cycle.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Inherited from the shared value of each billing schedule in the billing schedule group. Defines
when Subscription Management bills a product or service relative to when it’s provided to
the customer. Advance billing invoices a product or service before you provide it, while
arrears billing invoices a product or service after you provide it. Subscription Management
evaluates the billing type when it calculates an order's next billing date.

Possible values are:

**•** `Advance`  - If the billing schedule is billed in advance, Subscription Management
evaluates the order’s billing day of month to choose the nearest date on or before the
order product’s start date. For example, if a monthly order product’s start date is January
1, and the order’s billing day of month is 15, the next billing date is December 15.

**•** `Arrears`  - If the billing schedule is billed in arrears, Subscription Management evaluates
the order’s billing day of month to choose the nearest date after the order product’s start
date. For example, if a monthly order product’s start date is January 1 and the order’s
billing day of month is 15, the order product’s next billing date is January 15.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
The date that a cancellation was made against the billing schedule. Subscription Management
doesn't invoice billing schedules past their cancellation date.

```
Controller

CurrentBillingPeriodAmount

CurrentQuantity

EffectiveNextBillingDate

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
During the invoicing process, this field determines which date is used when the billing
schedule group and billing schedule have a related field with conflicting values.

For example, when `Controller` has a value of `BillingScheduleGroup`, if the
billing schedule's billing day of month is 5 while the billing schedule group's billing day of
month is 10, the invoice is sent on the 10th day of the month.

Possible values are:

**•** `BillingScheduleGroup` —The date on the billing schedule group controls.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The earliest `NextBillingDate` from all billing schedules in the billing schedule group.
This field is a reference field that isn't used for any features or calculations.

This field is a calculated field.


Standard Objects BillingScheduleGroup

**Field** **Details**

```
EndDate

LastReferencedDate

LastViewedDate

OwnerId

PaymentTermId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The latest end date from all billing schedules in the billing schedule group.

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
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The Salesforce user who owns the billing schedule group.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


Standard Objects BillingScheduleGroup

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the payment term used in this billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

```
PeriodBoundary

Product2Id

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Inherited from the order item's parent quote line item or sales transaction item. The period
boundary helps determine the start and end date of the billing periods.

Possible values are:

**•** `AlignToCalendar` —the period starts on the first day of the term unit; for example,
the first day of the month.

**•** `Anniversary` —The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod` —the period starts on the day indicated by `PeriodBoundaryDay` .

**•** `EndOfPeriod` —the period starts on the last day of the pricing term unit.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the product for the order item represented by each billing schedule in the billing
schedule group.

This field is a relationship field.

**Relationship Name**
Product2


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductName

ProrationPolicyId

ReferenceEntityId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product for the order item represented by each billing schedule in the
billing schedule group.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Refers to the proration policy that applies to this billing schedule group. The proration policy
defines how time periods are calculated for subscription orders. For example, whether partial
periods are allowed.

Inherited from the shared proration policy for each billing schedule in the billing schedule
group.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset used to create the billing schedules in the billing schedule group.

This field is a relationship field.

**Relationship Name**
ReferenceEntity


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Asset

```
ShippingAddress

ShippingCity

ShippingCountry

ShippingGeocodeAccuracy

ShippingLatitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the shipping address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. City maximum size is 40
characters

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Country maximum size is 80
characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the shipping address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

```
ShippingLongitude

ShippingPostalCode

ShippingState

ShippingStreet

StartDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with ShippingLatitude to specify the precise geolocation of an address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Postal code maximum size
is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. State maximum size is 80
characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address for this billing schedule group. Maximum of 255
characters.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects BillingTreatment

**Field** **Details**

**Description**
The earliest start date from all billing schedules in the billing schedule group.

```
TotalBilledAmount

TotalPendingAmount

### BillingTreatment

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that has been invoiced for all billing schedules within the billing schedule group.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that hasn't yet been invoiced for all billing schedules within the billing schedule
group.

This field is a calculated field.

Defines how Subscription Management bills an order item. The Exclude From Billing field controls whether the order item is invoiced.
Child billing treatment items control how much of the order item's balance is invoiced for each invoice across the subscription's lifecycle.
Billing treatments are assigned to order items based on the parent billing policy's Billing Treatment Selection field. This object is available
in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatment.htm)


Standard Objects BillingTreatment

Fields

**Field** **Details**

```
BillingPolicyId

Description

ExcludeFromBilling

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the billing policy for the billing treatment.

This field is a relationship field.

**Relationship Name**
BillingPolicy

**Relationship Type**
Lookup

**Refers To**
BillingPolicy

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description of the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Excludes any order items assigned to the treatment from creating billing schedules.

Possible values are:

**•** `No`

**•** `Yes`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects BillingTreatment

**Field** **Details**

```
LastViewedDate

LegalEntityId

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the legal entity used to assign the treatment to order items when the parent billing
policy's `BillingTreatmentSelection` is `LegalEntity` .

This field is a relationship field.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup

**Refers To**
LegalEntity

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Draft or inactive billing treatments can't be assigned to order items.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`


### Standard Objects BillingTreatmentItem

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BillingTreatmentHistory (API version 55.0)**
History is available for tracked fields of the object.

### BillingTreatmentItem

A billing treatment item defines how the order item's total amount is distributed into billing schedules over the course of the order
item's lifecycle. In the Subscription Management pilot, billing treatments must have only one billing treatment item, so that the billing
treatment item covers 100% of the order item's total value. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatmentitem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatmentitem.htm)

Fields

**Field** **Details**

```
BillingTreatmentId

BillingType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent billing treatment for the billing treatment item.

This field is a relationship field.

**Relationship Name**
### BillingTreatment

**Relationship Type**
Lookup

**Refers To**
### BillingTreatment

**Type**
picklist


Standard Objects BillingTreatmentItem

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines when Subscription Management invoices a product or service relative to when it’s
provided to the customer. Advance billing invoices a product or service before it's provided,
while arrears billing invoices a product or service after it has provided Subscription
Management evaluates billing type when calculating an order product’s next billing date.

Possible values are:

**•** `Advance`                   - If the order item is billed in advance, Subscription Management evaluates
the order’s billing day of month to choose the nearest date on or before the order
product’s start date. For example, if a monthly order product’s start date is January 1,
and the order’s billing day of month is 15, the next billing date is December 15.

**•** `Arrears`                   - If the order item is billed in arrears, Subscription Management evaluates
the order’s billing day of month to choose the nearest date after the order product’s start
date. For example, if a monthly order product’s start date is January 1 and the order’s
billing day of month is 15, the order product’s next billing date is January 15.

Important: Arrears billing isn't available in Subscription Management API Version
54.0.

```
Controller

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
During the invoicing process, this field determines which value Subscription Management
uses when the billing schedule group and billing schedule have a shared field with different
values. For example, when `Controller` has a value of `BillingScheduleGroup`,
if the billing schedule's billing day of month is 5 while the billing schedule group's billing
day of month is 10, Subscription Management uses the value of 10.

In the Subscription Management API version 54.0, only `BillingScheduleGroup` is
supported.

Possible values are:

**•** `BillingScheduleGroup`  

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three-letter ISO 4217 currency code associated with the billing treatment item.


Standard Objects BillingTreatmentItem

**Field** **Details**

```
Description

FlatAmount

Handling0Amount

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for the billing treatment item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount in terms of units of currency (such as $10 or $21.52) to invoice from the order
item. Used only when `Type` has a value of `FlatAmount` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows how Subscription Management invoices billing period items that have an amount
of $0.

Possible values are:

**•** `CreateInvoice` —Create a $0 invoice line.

**•** Null —No invoice line is created.

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


Standard Objects BillingTreatmentItem

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

```
Name

Percentage

ProcessingOrder

Sequencing

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage (such as 10% or 12.5%) to invoice from the order item. Used only when
`Type` has a value of `Percentage` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Defines the order in which Subscription Management creates billing schedules based on
each billing treatment item. Lower numbers are evaluated first. For example, if your billing
treatment has a billing treatment item that invoices at 25 `Percentage` and a
`ProcessingOrder` of 1, and another item that invoices at 75 `Percentage` and a
`ProcessingOrder` of 2, your first billing schedule will be for 25 percent of the order
item's total amount, and your second billing schedule will be for 75% of the order item's
total amount.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows users to define the number used to start invoice numbers on invoices generated from
this billing treatment item.

Subscription Management API Version 54.0 supports only manual sequencing.

Possible values are:


### Standard Objects BlockedRedirectEventLog

**Field** **Details**

**•** `Manual—` Invoices created from this billing treatment item begin with an invoice number
of 1.

```
Status

Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Draft billing treatment items aren't evaluated for creating billing schedules.

Possible values are:

**•** `Active`

**•** `Draft`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines whether billing schedules created from this billing treatment item are based on a
flat amount or a percentage of the order item's total amount.

Possible values are:

**•** `FlatAmount` —The billing schedule is for a flat currency amount of the order item's
total amount (for example, $50 or $200.50.)

**•** `Percentage` —The billing schedule is for a percentage of the order item's total amount
(for example, 12.5% or 54%).

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BillingTreatmentItemHistory (API version 55.0)**
History is available for tracked fields of the object.

### BlockedRedirectEventLog

Blocked Redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. This object
is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects BlockedRedirectEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BlockedUri

BlockedUriDomain

IsMalformedUrl

Origin

Referrer

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The full string of the target for the redirection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If BLOCKED_URI is a URL, the domain for that URL. To allow future redirections to the
[BLOCKED_URI, BLOCKED_URI_DOMAIN is the value to add to RedirectWhitelistUrl.](https://developer.salesforce.com/docs/atlas.en-us.256.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm?q=%22Trusted%20URL%22)

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this redirection was blocked because the target URL failed a syntax check
or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin that caused the request to the BLOCKED_URI. For example, if a form on an
Experience Cloud Visualforce site page redirects a user to an untrusted URL via the saveURL
parameter, ORIGIN contains the base URL of that site.

**Type**
string


### Standard Objects Bookmark

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The absolute or partial address from which the request to the BLOCKED_URI came. The
`Referrer-Policy HTTP` Header of the request determines how much of the URL is
shared.

```
RemoteAddress

RequestIdentifier

Timestamp

### Bookmark

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Remote IP address of the client making the request.

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
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

Represents a link between opportunities that share common information.

This object is available to organizations with the Similar Opportunities feature enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects Bookmark

Fields

**Field** **Details**

```
ID

FromId

ToId

 IsDeleted

```

Usage

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
ID of the bookmark. Label is **Bookmark ID** .

**Type**
ID

**Properties**
Filter

**Description**
The originating opportunity. Label is **Bookmarked From ID**

**Type**
ID

**Properties**
Filter

**Description**
The opportunity to which the originating opportunity is linked. Label is **Bookmarked To**
**ID** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

The Bookmark object works with the Opportunity object only.

Use this read-only object to query the bookmarks between opportunities in your organization. In the online application, users can search
for opportunities that share attributes with their opportunity. The user can then bookmark the appropriate opportunities for future
reference.


### Standard Objects BotDefinition BotDefinition

Represents a top level object for Einstein Bots or Agentforce Agents. This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
AgentTemplate

AgentType

BotUserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this BotDefinition represents an agent, this field represents the name of the agent template
used to create it.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The agent type. For example, Agentforce Service Agent (ASA) or Agentforce Employee Agent
(AEA).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID associated with the bot definition.

**Relationship Name**
BotUser

**Refers To**
User


### Standard Objects BotVersion

**Field** **Details**

```
Description

DeveloperName

MasterLabel

Type

### BotVersion

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description for the bot or agent.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name for this object.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The master label of the bot.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
### This field represents the configuration type of the bot. The default value is Bot .

Possible values are:

### • Bot —Default Einstein Bot configuration.

**•** `ExternalCopilot`  - An external-facing agent. For example, Agenforce Service
Agent.

**•** `InternalCopilot`  - An internal-facing agent. For example, Agentforce (Default).

Represents a version of a bot or agent defined by a BotDefinition record. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects BotVersion

Fields

**Field** **Details**

```
BotDefinitionId

CopilotPrimaryLanguage

CopilotSecondaryLanguages

DeveloperName

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

Required. This field relates a bot version to its parent BotDefinition record.

This field is a relationship field.

**Relationship Name**
BotDefinition

**Refers To**
BotDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The primary language that the bot or agent communicates in.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

A comma-separated list of additional languages that the bot or agent supports.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects BrandingSet

**Field** **Details**

**Description**
Required. Indicates whether the bot version is active or inactive. Only one version for a related
BotDefinition can be active at once.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Inactive` .

```
ToneType

VersionNumber

### BrandingSet

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines the tone of the bot.

Possible values are:

**•** `Casual`  

**•** `Formal`  

**•** `Neutral`  

The default value is `Casual` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number for this version of the bot or agent.

Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder. This object is available in API version 40.0 and later.

Supported Calls

create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

Special Access Rules

The BrandingSet type is available when at least one of the following is enabled in your org: Digital Experiences, Surveys, or Lightning
Experience. All users, including unauthenticated guest users, can access this type.


Standard Objects BrandingSet

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

NamespacePrefix

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the set of branding properties.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. API name of the BrandingSet object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the branding set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user-facing label of the set of branding properties.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix with a 15 character limit. You
can refer to a component in a managed package by using
the `namespacePrefix__componentName` notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.


### Standard Objects BrandTemplate

**Field** **Details**

In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix. `NamespacePrefix` is null if the publisher is Salesforce.

### BrandTemplate

Letterhead for HTML EmailTemplate.

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
Description

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the letterhead. Limited to 1000 characters.

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
are reflected in a subscriber’s organization. Label is **Letterhead Unique Name** .


Standard Objects BrandTemplate

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

```
IsActive

Name

NamespacePrefix

Value

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the letterhead is available for use ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the template as it appears in the user interface. Limited to 255 characters. Label is
**Brand Template Name** .

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
textarea

**Properties**
Create, Update


### Standard Objects Brief

**Field** **Details**

**Description**
The contents of the letterhead, in HTML, including any logos.

Usage

Use this object to brand EmailTemplate records with your letterhead. You can also set a brand template to active or inactive. For example,
if you have five different marketing brands, you can maintain each different brand in one template, and assign to the appropriate
EmailTemplate.

SEE ALSO:

EmailTemplate

### Brief

Represents a marketing brief. A brief contains information that’s used for positioning and grounding a marketing campaign. Agentforce
can help you create a campaign that best fits the goals and requirements in your brief. This object is available in API version 61.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdditionalNotes

AgentGuardrails

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Context related to the campaign that isn’t represented in the other fields.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Guardrails that the agent must follow when creating a campaign. Use these guardrails to
prevent damage to your brand and to ensure safety and compliance.


Standard Objects Brief

**Field** **Details**

```
BrandId

Description

IsConversational

KeyMessage

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of your brand.

This field is a relationship field.

**Relationship Name**
Brand

**Refers To**
ManagedContent

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the brief.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the campaign contains conversational elements.

The default value is `false` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The main theme or message that you want to deliver to your customers through the campaign
that’s associated with the brief.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last referenced by a campaign.


Standard Objects Brief

**Field** **Details**

```
LastViewedDate

Name

PlanName

PrimaryCtas

PrimaryGoal

PrimaryKpi

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the brief.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An agent-generated name for the campaign. When you save a campaign preview, the
resulting campaign has this name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The main calls-to-action (CTAs) for the brief. The agent uses this information to understand
the actions that it can use to meet the goals of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The goal of the campaign that’s associated with the brief. The agent uses this field to
understand the main objective of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects BriefcaseAssignment

**Field** **Details**

**Description**
The main key performance indicator (KPI) for measuring progress toward the goal. The agent
uses this field to prioritize actions that contribute to the goal of the campaign.

```
Priority

TargetAudience

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The priority of the brief. The agent uses this field to prioritize actions that contribute to the
goal of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the characteristics of the audience that you want to reach through the
campaign that’s associated with this brief.

### BriefcaseAssignment

Represents the assignment of a briefcase definition to selected users and user groups. This object is available in API version 50.0 and
later.

Use this object to assign selected records for users and groups to view offline. Briefcase objects are available in orgs that have Briefcase
Builder and Field Service enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is **Briefcase Definition ID** .


### Standard Objects BriefcaseDefinition

**Field** **Details**

```
UserOrGroupId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the user or group requiring access to the briefcase. Label is **User or Group**
**ID** .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseAssignmentChangeEvent (API version 55.0)**
Change events are available for the object.

### BriefcaseDefinition

Represents a briefcase definition. A briefcase makes selected records available for users to view when they’re offline in the Salesforce
Field Service mobile app for iOS and Android. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Briefcase objects are available in orgs that have Briefcase Builder and Field Service enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Packaging Considerations

An org can have up to 5 briefcases. Installed briefcases are counted against this limit. You can’t install a package that includes a briefcase
if your org already has 5 briefcases. When a managed package includes a briefcase, the only changes allowed for the briefcase are
activating or deactivating and assigning users or groups to the briefcase.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects BriefcaseDefinition

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Description of the briefcase definition. Limited to 1024 characters.

```
DeveloperName

IsActive

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
are reflected in a subscriber’s organization. Limited to 80 characters. Label is **Name** .

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the briefcase is available for use ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the briefcase. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned.

Possible values are:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`


Standard Objects BriefcaseDefinition

**Field** **Details**

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
Filter, Group, Sort

**Description**
The master label for the briefcase. This internal label doesn’t get translated. Limited to 80
characters.

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


### Standard Objects BriefcaseRule

Usage

Use this object to query a briefcase or a list of briefcases with selected records and user assignments. For example:

```
   SELECT Id, Description FROM BriefcaseDefinition

   WHERE Id in (SELECT BriefcaseId FROM BriefcaseRule

   WHERE TargetEntity='Account')

   AND Id in (SELECT BriefcaseId FROM BriefcaseAssignment where

   UserOrGroupId='00GR0000000VtwUMAS')

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseDefinitionChangeEvent (API version 55.0)**
Change events are available for the object.

### BriefcaseRule

Represents a rule that specifies records for a briefcase definition. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is **Briefcase Definition ID** .

This field is a relationship field.

**Relationship Name**
### Briefcase

**Relationship Type**
Lookup


Standard Objects BriefcaseRule

**Field** **Details**

**Refers To**
BriefcaseDefinition

```
FilterLogic

IsAscendingOrder

OptionsIsRelatedFilesRule

OrderBy

ParentRuleId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The filter logic for record selection, for example, `1 AND 2` where 1 and 2 correspond to
filter 1 and filter 2. Filter logic operators include `AND` and `OR` . Limited to 255 characters.
Label is **Filter Logic** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the records should be sorted in ascending order. Label is
**Ascending** .

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the briefcase rule is part of a hierarchical set of rules that configure the
offline priming of file attachments. Available only for the Offline App (Salesforce Mobile App
Plus).

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The field to order the records by, which determines how the records can be sorted. For
example, `AccountName` or `CreatedBy` . Label is **Order By** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BriefcaseRule

**Field** **Details**

**Description**
The ID of the parent rule of this briefcase rule. This field is a relationship field.

**Relationship Name**
ParentRule

**Relationship Type**
Lookup

**Refers To**
BriefcaseRule

```
QueryScope

RecordLimit

RelationshipField

RelationshipType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. A group of records to restrict the scope of this rule.

Possible values are:

**•** `assignedToMe`

**•** `everything`

**•** `mine`

The default value is `everything` (All Records). The value `assignedToMe` is available
only for the `ServiceAppointment` object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record limit for the object. The recommended number for record limit is up to 500 records
per object for optimal performance. The maximum number is 2000. Label is **Limit** .

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The Salesforce object field that relates the briefcase rule to another briefcase rule. For example,
an Account rule can be related to a Contact rule using the Account ID object field. In this
example, the value for the briefcase rule's `RelationshipField` is `AccountID` .

**Type**
picklist


### Standard Objects BriefcaseRuleFilter

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The relationship of the briefcase rule to another briefcase rule. Possible values are:

**•** `ParentToChild`

**•** `ChildToParent`

```
TargetEntity

### BriefcaseRuleFilter

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The standard object, custom object, or custom metadata type that the briefcase rule selects
records from. The UI label is **Target Object** .

Represents a filter criteria for a briefcase rule. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseRuleId

FilterOperator

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase rule.

**Type**
picklist


Standard Objects BriefcaseRuleFilter

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. The comparison operator for this rule filter.

Possible values are:

**•** `d` —Ends with

**•** `e`                   - Equals

**•** `g` —Greater than

**•** `h` —Greater than or equal

**•** `i` —Like

**•** `l` —Less than

**•** `m` —Less than or equal

**•** `s` —Starts with

```
FilterSeqNumber

FilterValue

TargetEntityField

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. The filter number. When you apply multiple filters, the filters are numbered
sequentially, 1, 2, 3, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value for the field and criteria. For example, `true` or `false` for a boolean field whose
criteria or filter operator is Equals. Capitalization matters with date filter operators. Be sure
to specify date literals in uppercase. Some valid date literals include TODAY, YESTERDAY and
TOMORROW.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Required. The field to filter by. Compound fields and encrypted fields aren’t supported. Label
is **Field** .


### Standard Objects BroadcastCommAudience BroadcastCommAudience

Represents the audience that the broadcast communication is sent to. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object with Service Cloud, enable Incident Management in Setup and set up Broadcast Communications.

Fields

**Field** **Details**

```
AudienceId

### `BroadcastCommAudienceNumber`

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication audience.

**•** If `BroadcastType` is `Alert`, this value is the ID of the Group record where the
message is sent to.

**•** If `BroadcastType` is `Email`, this value is the ID of the ListEmail record where the
email is sent to.

**•** If `BroadcastType` is `ExperienceSiteBanner`, this value is the ID of the
Network record where the banner is displayed at.

**•** If `BroadcastType` is `Slack`, this value is the ID of the CollaborationRoom record
where the message is sent to.

This field is a polymorphic relationship field.

**Relationship Name**
Audience

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom, Group, ListEmail, Network

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects BroadcastCommAudience

**Field** **Details**

**Description**
Auto-generated number for the BroadcastCommAudience record.

```
BroadcastCommunicationId

BroadcastFailureReason

BroadcastType

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication record.

This field is a relationship field.

**Relationship Name**
BroadcastCommunication

**Relationship Type**
Lookup

**Refers To**
BroadcastCommunication

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason the broadcast communication failed to send.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`

**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects BroadcastCommAudience

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

MessageTimeStamp

OwnerId

SiteBannerText

```

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
Create, Filter, Group, Nillable, Sort

**Description**
If `BroacastType` is `Slack`, this value is the timestamp when the broadcast Slack
message was sent.

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
textarea

**Properties**
Create, Nillable

**Description**
If `BroadcastType` is `ExperienceSiteBanner`, this field contains the banner text
displayed on the associated site.


Standard Objects BroadcastCommAudience

**Field** **Details**

```
SiteBannerVisibility

Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `BroadcastType` is `ExperienceSiteBanner`, this field contains information
about who can view the banner.

Possible values are:

**•** `AuthenticatedUsers`

**•** `GuestUsers`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the broadcast communication.

Possible values are:

**•** `Active` —The site banner is visible on the site. Only applies if `BroadcastType` is
`ExperienceSiteBanner` .

**•** `Deleted` —The message is successfully deleted and isn’t visible anymore. Only applies
if `BroadcastType` is `Slack` .

**•** `DeleteFailed` —The message failed to delete but is still visible. Only applies if
`BroadcastType` is `Slack` .

**•** `Failed` —The message failed to send. Applies to any `BroadcastType` .

**•** `Inactive` —The site banner isn’t visible on the site. Only applies if `BroadcastType`
is `ExperienceSiteBanner` .

**•** `Sent` —The message is sent successfully. Only applies if the `BroadcastType` is
`Email` or `Slack` .

**•** `Updated` —The message is successfully edited. Only applies if the `BroadcastType`
is `Slack` .

**•** `UpdateFailed` —The message failed to edit and the update isn’t visible. Only applies
if the `BroadcastType` is `Slack` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommAudienceChangeEvent on page 68**
Change events are available for the object.


### Standard Objects BroadcastCommunication

**BroadcastCommAudienceFeed on page 55**
Feed tracking is available for the object.

**BroadcastCommAudienceHistory on page 63**
History is available for tracked fields of the object.

**BroadcastCommAudienceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BroadcastCommAudienceShare on page 67**
Sharing is available for the object.

### BroadcastCommunication

Represents a broadcast communication related to an incident. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`

Special Access Rules

To access this object with Service Cloud, enable Incident Management in setup and set up Broadcast Communications.

Fields

**Field** **Details**

```
Body

### `BroadcastCommunicationNumber`

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert`, this field contains the alert message.

**•** If `BroadcastType` is `Email`, this field contains the email body text.

**•** If `BroadcastType` is `ExperienceSiteBanner`, this field is empty.

**•** If `BroadcastType` is `Slack`, this field contains the Slack message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for every BroadcastCommunication record.


Standard Objects BroadcastCommunication

**Field** **Details**

```
BroadcastType

CustomNotificationTypeId

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`

**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the custom notification template used to frame the Slack message. Only applies if
`BroadcastType` is `Slack` .

Available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
CustomNotificationType

**Relationship Type**
Lookup

**Refers To**
CustomNotificationType

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


Standard Objects BroadcastCommunication

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

```
OwnerId

RelatedRecordId

Subject

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

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
Create, Filter, Group, Sort

**Description**
ID of the incident associated with the broadcast communication.

This field is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert`, this field is the alert message in the format “Incident
Alert | <Incident subject> | <Incident Number>.”

**•** If `BroadcastType` is `Email`, this field is the subject of the email sent.


### Standard Objects BroadcastTopic

**Field** **Details**

**•** If `BroadcastType` is `ExperienceSiteBanner`, this field is empty.

**•** If `BroadcastType` is `Slack`, this field is in the format “Incident Alert | <Incident
Subject>."

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommunicationChangeEvent on page 68**
Change events are available for the object.

**BroadcastCommunicationFeed on page 55**
Feed tracking is available for the object.

**BroadcastCommunicationHistory on page 63**
History is available for tracked fields of the object.

**BroadcastCommunicationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BroadcastCommunicationShare on page 67**
Sharing is available for the object.

### BroadcastTopic

Represents a definition of a broadcast topic. A broadcast topic is associated with a list of Experience Cloud network sites for Service Cloud
and collaboration rooms for Sales Cloud. The topic is created for a specific user role. Collaboration rooms are linked to Slack channels.
This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object with Sales Cloud, enable Slack Terms of Service and Sales Cloud for Slack App.

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.


Standard Objects BroadcastTopic

Fields

**Field** **Details**

```
BroadcastReason

Description

IsFeatured

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Reason for the broadcast topic. This field differentiates between Service Cloud and Sales
Cloud use cases.

Possible values are:

**•** `FeedChannels` —Used in Sales Cloud and associates the topic with collaboration
rooms.

**•** `IncidentCommunication` —Used in Service Cloud for Customer Service Incident
Management and associates the topic with networks.

The default value is `FeedChannels` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the broadcast topic.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the broadcast topic is featured ( `true` ) or not ( `false` ). This field is
applicable only when BroadcastReason is FeedChannels. A featured topic displays the
associated collaboration rooms to new users.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects BroadcastTopic

**Field** **Details**

```
LastViewedDate

Name

OwnerId

TopicType

```

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
Name of the broadcast topic.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the broadcast topic.

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
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Category for the broadcast topic.

Possible values are:

**•** `DealsWon` —Feed of won deals to see your team's successes. This value appears when
the Sales Cloud special access rules are enabled.


### Standard Objects BroadcastTopicGroup

**Field** **Details**

**•** `DealsToWatch` —Feed of deals that have an amount above a specified value and
are likely to close. This value appears when the Sales Cloud special access rules are
enabled.

**•** `Incident Communication` —This value appears when the Service Cloud special
access rules are enabled.

### BroadcastTopicGroup

Represents a junction object that relates a group to an alert type broadcast topic. The broadcast sends the alert to this group. This object
is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Enable Customer Service Incident Management and Broadcast Alert. To create a BroadcastTopicGroup record, set the BroadcastReason
field of the associated BroadcastTopic to Incident Communication.

Fields

**Field** **Details**

```
BroadcastTopicId

GroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast topic.

This field is a relationship field.

**Relationship Name**
### BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
### BroadcastTopic

**Type**
reference


### Standard Objects BroadcastTopicNetwork

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group where the alert of the associated BroadcastTopic record with an `Alert`
`BroadcastType` is sent to.

This field is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

```
Name

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the broadcast topic group.

This field is optional.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastTopicGroupChangeEvent on page 68**
Change events are available for the object.

Available in API version 58.0

### BroadcastTopicNetwork

Represents a link between a broadcast topic and the Experience Cloud network site for Service Cloud. This object is available in API
version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects BroadcastTopicNetwork

Special Access Rules

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.

Fields

**Field** **Details**

```
BroadcastTopicId

Name

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The BroadcastTopic ID that's linked to the Network.

This field is a relationship field.

**Relationship Name**
BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
BroadcastTopic

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the broadcast topic that's assigned to the network.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Network ID that's linked to the BroadcastTopic..

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network


### Standard Objects BrowserPolicyViolation

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastTopicNetworkChangeEvent on page 68**
Change events are available for the object.

### BrowserPolicyViolation

Represents a violation that occurred within the last seven days related to the Trusted URLs and Trusted URLs for External Redirects
allowlists. These violations include blocked resource requests based on your content security policy (CSP) and blocked redirections. This
object is available in API version 61.0 and later.

[We recommend that you manage this object through the Trusted URL and Browser Policy Violations list in Setup. See Manage Trusted](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_csp_violations.htm&type=5&language=en_US)
[URL and Browser Policy Violations in Salesforce Help.](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_csp_violations.htm&type=5&language=en_US)

Note: To help preserve performance, Salesforce uses throttling, a technique that limits the number of generated violations when
the volume is exceptionally high. Therefore, if your org generates a high volume of violations over a short period of time, some of
those violations can fail to generate a BrowserPolicyViolation.

To see detailed information about the captured CSP violations for your org, use the CSP Violation Event Type.

[To understand when Salesforce captures blocked redirections, see External Redirection Restrictions in Salesforce in Salesforce Help. For](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_external_redirections_understand.htm&language=en_US)
detailed information about each blocked redirection, use the Blocked Redirect Event Type.

When you delete a BrowserPolicyViolation, only the logged event is removed. If your allowlists still block those requests, a new
### BrowserPolicyViolation is generated the next time a matching request occurs.

To help you manage the list, a daily process deletes violations that haven’t occurred within the last seven days. To track browser policy
violations over time, schedule daily queries of the Blocked Redirect and CSP Violations event types.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with the Customize Application and Modify All Data permissions can access this object.

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
The developer name of the violation.


Standard Objects BrowserPolicyViolation

**Field** **Details**

Only users with View DeveloperName or View Setup and Configuration permission can view,
group, sort, and filter this field.

```
Language

MasterLabel

NamespacePrefix

UntrustedUrl

ViolationContext

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The language for the blocked request.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Master label for this violation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace prefix for this violation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL associated with the blocked request, without the path. For example, if a blocked
requested resource is an image with the URL
`https://www.example.com/images/image1.png`, the `UntrustedUrl` is
`https://www.example.com` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the `ViolationType` is `img-src (image)`, `font-src (fonts)`, or
`frame-src (iframe content)`, the content security policy (CSP) context for the
request. The CSP context controls which pages can load content from a CspTrustedSite.


### Standard Objects BulkApi2EventLog

**Field** **Details**

Possible values are:

**•** `Lightning` —The blocked request is related to a Lightning Experience page.

**•** `Not Applicable`                   - `ViolationContext` isn’t applicable to this violation. For
example, violations with a `ViolationType` of `Redirection` .

```
ViolationImpact

ViolationType

### BulkApi2EventLog

```

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The impact of this violation. Possible values are:

**•** `Blocked` –The policy was enforced and prevented the resource from loading. The
impact of blocked redirections and malformed URLs is always `Blocked` .

**•** `Reported` –This violation is blocked only after stricter CSP settings are configured.

For example, some resource requests associated with the `frame-src`, `font-src`,
and `img-src ViolationType` are blocked only when the Adopt updated CSP
directives setting is enabled in Session Settings.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The violation type. Possible values are:

**•** `img-src` –At least one request to load an image file from the URL was blocked because
the `UntrustedUrl` [isn’t a CspTrustedSite object with this CSP directive.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**•** `font-src` –At least one request to load a font from the URL was blocked because the
`UntrustedUrl` [isn’t a CspTrustedSite object with this CSP directive.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**•** `frame-src` –At least one request to load content in an iframe that originated from
the URL was blocked because the `UntrustedUrl` [isn’t a CspTrustedSite object with](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)
this CSP directive.

**•** `MalformedUrl` –At least one redirection to this URL failed because the
`UntrustedUrl` is malformed.

**•** `Redirect` –At least one redirection to this URL was blocked because the
`UntrustedUrl` [isn’t a RedirectWhitelistUrl object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm)

Bulk API 2 event logs contain details about Bulk API 2.0 requests. This object is available in API version 61.0 and later.


Standard Objects BulkApi2EventLog

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

FailedRecordCount

ErrorMessage

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

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The total number of records that failed. For example: `150` .

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The error message returned on failure.


Standard Objects BulkApi2EventLog

**Field** **Details**

```
JobIdentifier

JobStatus

LoginKey

ObjectType

OperationType

ProcessedRecordCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API 2.0 job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The job’s current status.

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
The type of event. The value is always `BulkApi2` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Bulk API 2.0 operation that was performed.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects BulkApi2EventLog

**Field** **Details**

**Description**
Number of records processed for this event. For example: `980` .The number of records
processed is reported differently for ingest and query jobs.

For _ingest_ jobs:

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
The ID the `WebCart on page 5826` that’s associated with this delivery group.

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

Represents an item in a `WebCart` that’s active in a store built with B2B. Cart item can be of type `Product` or `Charge` . This object
is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItem object is available only if the B2B Commerce license is enabled.


Standard Objects CartItem

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentTaxAmount

AssociatedItemPricing

BillingFrequency

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
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies how often a subscription is billed. Available in API version 59.0 and later.

Possible values are:

**•** `Annual`

**•** `MilestonePlan`

**•** `Monthly`

**•** `Quarterly`


Standard Objects CartItem

**Field** **Details**

**•** `Semi-Annual`

```
CartDeliveryGroupId

CartId

ChildProductCount

ConfigureDuringSale

```

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

**Refers To**
CartDeliveryGroup

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


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specify whether a product bundle is configurable. Available in API version 65.0 and later.

Possible values are:

**•** `Allowed`

**•** `NotAllowed`

```
CurrencyIsoCode

DistributedAdjustment

Amount

DistributedAdjustment

TaxAmount

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `AED` —UAE Dirham

**•** `AUD` —Australian Dollar

**•** `BRL` —Brazilian Real

**•** `CAD` —Canadian Dollar

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `INR` —Indian Rupee

**•** `JPY` —Japanese Yen

**•** `SEK` —Swedish Krona

**•** `USD` —U.S. Dollar

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


Standard Objects CartItem

**Field** **Details**

**Description**
A calculated field that determines the amount of a cart-wide tax adjustment due to
promotions when distributed across all items in the cart. This field is available in API version
52.0 and later.

EXAMPLE: Your discount causes a cart-wide tax reduction of (-$10), and there are 5 items in
the cart. The distributed tax adjustment is (-$2).

```
FirstPymtPriceAferAdjustments

FirstPymtTax

GrossAdjustmentAmount

GrossUnitPrice

IsShippingChargeNot

Applicable

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscription products, after price adjustments are applied.
The total amount for a non-subscription product or a non-term based subscription product,
after price adjustments are applied. This is available in API version 60.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax for the first term price for term-based subscription products. The tax amount for a
non-subscription product or a non-term subscription product. This field is available in API
version 60.0 and later.

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

**Type**
boolean


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether shipping charges are applicable ( `true` ) or not ( `false` ) to the cart item.
The default value is `false` .

This field is available in API version 64.0 and later.

```
ItemizedAdjustment

Amount

ItemizedAdjustment

TaxAmount

ListPrice

Name

```

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

**Description**
The name of this `CartItem` record. `Name` can be up to 255 characters.


Standard Objects CartItem

**Field** **Details**

```
NetAdjustmentAmount

NetUnitPrice

NetUnitPriceAfterAdjustments

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net unit price for a cart item, after all tier and promotional price adjustments are applied.
This field is available in API version 60.0 and later.

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


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Weight per unit of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.

```
PeriodBoundary

PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The. Default value is . Possible values are:

**•** `AlignToCalendar`

**•** `Anniversary`

**•** `DayOfPeriod`

**•** `LastDayOfPeriod`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The. Default value is . Possible values are:

**•** `1` —January

**•** `10` —October

**•** `11` —November

**•** `12` —December

**•** `2` —February

**•** `3` —March

**•** `4` —April

**•** `5` —May

**•** `6` —June

**•** `7` —July


Standard Objects CartItem

**Field** **Details**

**•** `8` —August

**•** `9` —September

```
PriceBookEntryId

PricingTermCount

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the price book entry for the product. This field is available in API version 60.0 and
later.

This field is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A calculated field that indicates the number of pricing terms in the subscription. This field is
available in API version 59.0 and later.

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


Standard Objects CartItem

**Field** **Details**

```
ProductClass

ProductRelated

ComponentId

ProductSellingModelId

```

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

**Refers To**
ProductRelatedComponent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the model used to sell a product. This field is available in API version 59.0 or later.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup


Standard Objects CartItem

**Field** **Details**

**Refers To**
ProductSellingModel

```
ProductValidationKey

ProductRelationship

TypeId

ProrationPolicyId

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the proration policy, which defines how prices are calculated for each time period
within a subscription term. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
Proration Policy


Standard Objects CartItem

**Field** **Details**

```
Quantity

QuantityScaleMethod

SalesPrice

SellingModelType

Sku

```

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

**•** `Proportional` —Represents a value that varies in proportion to the parent bundle’s
price or quantity.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The discounted price of a cart item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the product selling model associated with a term-based subscription product.
This field is available in API version 60.0 and later. Possible values are:

**•** `Evergreen`

**•** `OneTime`

**•** `TermDefined`

The default value is `OneTime` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The Shelf-Keeping Unit ID of a cart item.

```
StockCheckMethod

SubType

SubscriptionTerm

TaxTreatmentId

```

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
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of terms (years or months, for example) in the subscription. This field is available
in API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment for the cart item.

This field is available in API version 63.0 and later. This field is available with Subscription
Management.

This field is a relationship field.


Standard Objects CartItem

**Field** **Details**

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

```
TotalAdjustmentAmount

TotalAmount

TotalFirstPymtAdjAmount

TotalFirstPymtListPrice

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
The total adjustment amount for the first payment of a term-based susbcription product.
The TotalAdjustmentAmount for non-subscription products and non-term based subscription
products. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first-payment amount for a term-based subscription product, based on the product's
ListPrice. This is the same value as TotalListPrice for non-subscription products or non-term
based subscription products. This price is only for comparison, and not the price at which
the buyer purchases a product. This field is available in API version 63.0 and later.


Standard Objects CartItem

**Field** **Details**

```
TotalFirstPymtPrice

TotalLineAmount

TotalLineFirstPymtAmount

TotalLineFirstPymtTaxAmount

TotalLineGrossAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscription products. The price of a line item for
non-subscription products and non-term based subscription products. This price includes
price adjustments and excludes taxes. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on sales price and quantity.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscripiton products, calculated based on the sales price
and quantity, before any price adjustments are made. This is the same value as
TotalLineAmount for non-subscription products and non-term based subscription products.
This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The tax on the first payment amount, after price adjustments, for term-based subscription
products. The tax on the price of the product for non-subscription products and non-term
based subscription products. Taxes are also calculated on the delivery charge items. This
field is a calculated field. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects CartItem

**Field** **Details**

**Description**
The total gross amount of the line item (tax inclusive). This is available in API version 55.0
and later.

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


Standard Objects CartItem

**Field** **Details**

**Description**
Total price after all price adjustments are applied. This field is available in API version 52.0
and later.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

```
TotalPriceTaxAmount

TotalPromo

AdjustmentAmount

TotalPromoAdjustment

TaxAmount

TotalTaxAmount

TotalWeight

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


Standard Objects CartItem

**Field** **Details**

**Description**
Total weight of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.

```
Type

UnitAdjustedPrice

UnitAdjustedPrice

WithItemAdj

UnitAdjustmentAmount

UnitItemAdjustment

Amount

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `CartItem` type. Possible values are:

**•** `Product`

**•** `Charge`

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


Standard Objects CartItem

**Field** **Details**

**Description**
Item level adjustments made to the unit price for the item.

```
UnitPriceAfterAdjustments

WeightUnit

```

Associated Objects

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price for a cart item, after tier and promotional price adjustments are applied. This
field is available in API version 60.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unit of measurement for the weight of the cart item. This field is available in API version 62.0
and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

CartDeliveryGroup

WebCart


### Standard Objects CartItemAttribute CartItemAttribute

Represents the attributes associated with a cart item, stored as key-value pairs. These attributes are derived from the product and carried
forward to the order during checkout. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The CartItemAttribute object is available:only if the B2B Commerce license, the Salesforce CPQ feature, and Commerce Dynamic Bundles
are enabled in your Salesforce org.

Fields

**Field** **Details**

```
AttributeDefinitionId

AttributeName

AttributePicklistValueId

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


Standard Objects CartItemAttribute

**Field** **Details**

**Description**
The ID of the picklist value associated with the cart item attribute.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**

[AttributePicklistValue](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_attributepicklistvalue.htm)

```
AttributeValue

CartItemId

ExternalId

IsPriceImpacting

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the cart item attribute, such as Blue or Large.

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


### Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the attribute affects cart pricing ( `true` ) or not ( `false` ). This field
determines whether the Commerce Pricing API calls must be triggered to update the price.

```
UnitOfMeasure

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the unit of measure associated with the cart item attribute.

This field is available only if the AttributeUomPilot Org perm is enabled. Contact Salesforce
support for assistance.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**

[UnitOfMeasure](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_unitofmeasure.htm)

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


Standard Objects CartItemPriceAdjustment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItemPriceAdjustment object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentAmountScope

AdjustmentBasisReferenceId

AdjustmentSource

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


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`

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
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItemPriceAdjustment

**Field** **Details**

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

```
CartItemId

CurrencyIsoCode

Description

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


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Description**
Description of the price adjustment.

```
Name

PriceAdjustmentCauseId

Priority

TotalAmount

TotalGrossAmount

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the price adjustment.

**Type**
reference

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


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount (tax inclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

```
TotalNetAmount

TotalTax

WebCartAdjustmentGroupId

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total net amount (tax exclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

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


### Standard Objects CartTax CartTax

Represents taxes for a line item in a `WebCart` that’s active in a store built with B2B Commerce or D2C Commerce. This object is available
in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartTax object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentTargetType

Amount

CartId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Target for the price adjustment (the cart itself or individual items). This field is available in
API version 52.0 and later.

Possible values are:

### • Cart

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


Standard Objects CartTax

**Field** **Details**

```
CartItemId

CartItemPriceAdjustmentId

CurrencyIsoCode

Description

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a cart item being taxed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a price adjustment for a cart item being taxed. (This field is available in API version
52.0 and later.)

**Refers To**
CartItemPriceAdjustment

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


### Standard Objects CartValidationOutput

**Field** **Details**

```
TaxCalculationDate

TaxRate

TaxType

```

Associated Objects

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date this tax was calculated.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The applied tax rate for this line of tax.

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


Standard Objects CartValidationOutput

Supported Calls

`create()`, `delete()`, `describeLayout() describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartValidationOutput object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
BackgroundOperationId

CartId

CurrencyIsoCode

IsDismissed

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


Standard Objects CartValidationOutput

**Field** **Details**

```
Level

Message

Name

RelatedEntityId

RelatedEntityPrefix

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of output resulting from the validation process. Possible values are:

**•** 0 ( `Info` )

**•** 1 ( `Error` )

**•** 2 ( `Warning` )

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


### Standard Objects Case

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The `CartValidationOutput` type. Possible values are:

**•** `CartSave`                   - Available in API version 64.0 and later.

**•** `Entitlement`

**•** `Inventory`

**•** `Other`

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


Standard Objects Case

Fields

**Field** **Details**

```
AccountId

AssetWarrantyID

BusinessHoursId

Comments

CaseNumber

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

**Relationship Type**
Lookup

**Refers To**
Account

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


Standard Objects Case

**Field** **Details**

**Description**
Assigned automatically when each case is inserted. It can't be set directly, and it can't be
modified after the case is created.

```
ClosedDate

CommunityId

ConnectionReceivedId

ConnectionSentId

ContactEmail

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was closed.

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


Standard Objects Case

**Field** **Details**

**Description**
Email address for the contact. The Case.ContactEmail field displays the Email field on the
contact on page 1378 that is referenced by Case.ContactId. Label is `Contact Email` . This
field is available in API version 38.0 and later.

```
ContactFax

ContactId

ContactMobile

ContactPhone

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the contact. Label is `Contact Fax` . This field is available in API version
38.0 and later.

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


Standard Objects Case

**Field** **Details**

```
CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

Description

FeedItemId

```

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


Standard Objects Case

**Field** **Details**

```
HasCommentsUnreadByOwner

HasSelfServiceComments

IsClosed

IsClosedOnCreate

IsDeleted

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case contains comments that the case owner hasn’t read ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case has comments added by a Self-Service user ( `true` ) or not ( `false` ).
Only visible when Customer Portal is enabled.

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


Standard Objects Case

**Field** **Details**

```
IsEscalated

IsSelfServiceClosed

IsStopped

IsVisibleInSelfService

Language

```

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

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed for Self-Service users ( `true` ) or not ( `false` ).

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


Standard Objects Case

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MasterRecordId

Origin

OwnerId

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
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

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


Standard Objects Case

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the case.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ParentId

Priority

QuestionId

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


Standard Objects Case

**Field** **Details**

```
Reason

RecordTypeId

ServiceContractId

SlaStartDate

SourceId

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the case was created, such as `Instructions not clear`, or `User`
`didn’t attend training` .

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


Standard Objects Case

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the case, such as New, Closed, or Escalated. This field directly controls the
`IsClosed` flag. Each predefined `Status` value implies an `IsClosed` flag value. For
more information, see CaseStatus.

```
StopStartDate

Subject

SuppliedCompany

SuppliedEmail

SuppliedName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time an entitlement process was stopped on the case.

This field is available in API version 18.0 and later.

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


Standard Objects Case

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name that was entered when the case was created. Label is `Name` .

```
SuppliedPhone

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number that was entered when the case was created. Label is `Phone` .

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


Standard Objects Case

**Field** **Field Type** **Details**

`useDefaultRule` boolean

Specifies whether to use the default rule for rule-based assignment
( `true` ) or not ( `false` ). The default rule is assigned by users in
the Salesforce user interface.

For a code example that shows setting the AssignmentRuleHeader for a Lead (which is similar to setting the AssignmentRuleHeader for
a Case), see Lead.

Separating Accounts from Contacts in Cases

In releases before 8.0, the `AccountId` could not be specified, it was derived from the contact’s account. This behavior will continue
to be supported in future releases, but you can also now specify an `AccountId` . If you do not specify the `AccountId` during the
creation of a case, the value will default to the contact’s `AccountId` .

Note: When a record is updated, if the `ContactId` has not changed, then the `AccountId` is not regenerated. This prevents
the API from overwriting a value previously changed in the Salesforce user interface. However, if an API call changes the ContactId
and the `AccountId` field is empty, then the `AccountId` is generated using the contact’s account.

Using **`_case`** with Java

Depending on the development tool you use, you might need to write your application using `_case` instead of `Case`, because `case`
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


### Standard Objects CaseArticle CaseArticle

Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

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


### Standard Objects CaseComment

**Field** **Details**

**Properties**
Create, Group, Nillable

**Description**
Indicates that the article has been shared with the customer through an email.

```
KnowledgeArticleId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the KnowledgeArticle associated with the Case.

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

```

**Type**
textarea


Standard Objects CaseComment

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is
**Body** .

```
ConnectionReceivedId

ConnectionSentId

CreatorFullPhotoUrl

CreatorName

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


Standard Objects CaseComment

**Field** **Details**

```
CreatorSmallPhotoUrl

IsDeleted

IsNotificationSelected

IsPublished

ParentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

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


### Standard Objects CaseContactRole

**Field** **Details**

**Description**
Required. ID of the parent Case of the CaseComment.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
### Case

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

```

**Type**
reference


Standard Objects CaseContactRole

**Field** **Details**

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
Case

```
ContactId

IsDeleted

Role

```

**Type**
reference

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


### Standard Objects CaseHistory

**Field** **Details**

which the `CaseId`, `ContactId`, and `Role` values are identical. Different contacts can
play the same role on the same case. A contact can play different roles on the same case.

Usage

Use this object to define the role that a given Case plays on a given Contact. For example, you can use this object to be able to see all
contacts who are associated to a case, or, given a contact, be able to query all cases that they are associated with, even if they are not
the primary contact on the case.

### CaseHistory

Represents historical information about changes that have been made to the associated Case.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
### Case

**Relationship Type**
Lookup

**Refers To**
### Case


Standard Objects CaseHistory

**Field** **Details**

```
DataType

Field

IsDeleted

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
Name of the case field that was modified, or a special value to indicate some other
modification to the case. The possible values, in addition to the case field names, are:

**•** **ownerAssignment** —The owner of the case was changed.

**•** **ownerAccepted** —A user took ownership of a case from a queue.

**•** **ownerEscalated** —The owner of the case was changed due to case escalation.

**•** **external** —A user made the case visible to customers in the Customer Self-Service Portal.

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


### Standard Objects CaseHistory2

Usage

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

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
### Case

**Relationship Type**
Lookup

**Refers To**
### Case


Standard Objects CaseHistory2

**Field** **Details**

```
IsDeleted

OwnerId

PreviousUpdate

Status

```

Usage

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

**Relationship Type**
Lookup

**Refers To**
Group, User

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


### Standard Objects CaseMilestone

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseHistory2ChangeEvent on page 68**
Change events are available for the object in API version 60.0 or later.

### CaseMilestone

Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
BusinessHoursId

CaseId

CompletionDate

ElapsedTimeInDays

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


Standard Objects CaseMilestone

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in days.

```
ElapsedTimeInHrs

ElapsedTimeInMins

IsCompleted

IsViolated

MilestoneTypeId

StartDate

```

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

**Description**
The time required to complete a milestone in minutes.

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


Standard Objects CaseMilestone

**Field** **Details**

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone started on the case.

```
TargetDate

TargetResponseInDays

TargetResponseInHrs

TargetResponseInMins

TimeRemainingInDays

TimeRemainingInHrs

```

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

**Description**
The time to complete the milestone in days.

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


Standard Objects CaseMilestone

**Field** **Details**

**Properties**
Nillable

**Description**
Time remaining to reach the milestone target, measured in hours.

```
TimeRemainingInMins

TimeSinceTargetInDays

TimeSinceTargetInHrs

TimeSinceTargetInMins

```

Usage

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

**Description**
The time elapsed since the milestone target, measured in days.

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

Case

MilestoneType

SlaProcess


### Standard Objects CaseOwnerSharingRule CaseOwnerSharingRule

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

Fields

**Field** **Details**

```
CaseAccessLevel

Description

DeveloperName

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


Standard Objects CaseOwnerSharingRule

**Field** **Details**

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

```
GroupId

Name

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Cases owned by users in the source group
trigger the rule to give access.

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


### Standard Objects CaseParticipant

Usage

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

Special Access Rules

Fields and values added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

Fields

**Field** **Details**

```
AuthorizationProof

CaseId

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


Standard Objects CaseParticipant

**Field** **Details**

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

```
LastReferencedDate

LastViewedDate

Name

ParticipantId

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


Standard Objects CaseParticipant

**Field** **Details**

**Description**
The participant associated with the case participant record.

This field is a polymorphic relationship field.

**Relationship Name**
Participant

**Relationship Type**
Lookup

**Refers To**
Account, Contact

```
PreferredCallTimeFrom

PreferredCallTimeTo

PreferredCommunicationMode

Role

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

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


Standard Objects CaseParticipant

**Field** **Details**

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

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the case participant.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `In Review` (Available in API version 58.0 and later.)

**•** `Pending` (Available in API version 58.0 and later.)

**•** `Submitted` (Available in API version 58.0 and later.)

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseParticipantFeed on page 55**
Feed tracking is available for the object.

**CaseParticipantHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects CaseRelatedIssue CaseRelatedIssue

This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service failure.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CaseId

Name

RelatedEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A relationship field that represents the case you're linking a Problem or Incident to.

**Relationship Name**
### Case

**Relationship Type**
Lookup

**Refers To**
### Case

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


Standard Objects CaseRelatedIssue

**Field** **Details**

```
RelatedIssueId

RelationshipType

UniqueKeyIndex

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

