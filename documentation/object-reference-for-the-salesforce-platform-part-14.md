Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where a personalization point's resources
originate. This is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the personalization point. This is an optional field.


Standard Objects PersonalizationPoint

**Field** **Details**

```
DeveloperName

```

IsAuthenticationRequired

```
LastReferencedDate

LastViewedDate

MaxItemsCount

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization point. This is a required field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the personalization point must use authenticated endpoints for real-time
data capture and recommendation requests. When set to `true`, all interactions with Data
Cloud are secured and verified.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the personalized point was referenced by another
resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the personalization point.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the maximum number of recommendations to return.

**Type**
string


Standard Objects PersonalizationPoint

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization point.

```
PersonalizationSchemaEnum

PersonalizationSchemaId

```

ProfileDataGraphId

RootPersonalizationPoint

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the type of personalization schema, which is related to where a
personalization decision is created. The accepted values are

**•** DecisionDefined

**•** ExperienceVariation

**•** FlowPath

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the schema that’s related to the personalization point.

**Relationship Name**
PersonalizationSchema

**Refers To**
PersonalizationSchema

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the profile data graph that’s used with the personalization
point.

**Relationship Name**
ProfileDataGraph

**Refers To**
DataGraph

**Type**
string


Standard Objects PersonalizationPoint

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the personalization point from where data is gathered.

Source

SourceRecordId

Status

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the personalization point from where data is gathered.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the specific record that contains the personalization point.

**Relationship Name**
SourceRecord

**Refers To**
FlowRecordElement, ManagedContent

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the state of the personalization point. The default value is `Processing`, and the
accepted values are:

**•** Active

**•** CreateError—Error

**•** DeleteError—Error

**•** Deleting

**•** EditError—Error

**•** Processing


### Standard Objects PersonalizationSchema

Usage

Use this object to define a specific touch point in an experience where personalization decisions can be made. For example, a
personalization point can be an banner on a webpage. After setting up data space, profile data graph, personalization type, and schema,
you can add decisions and targeting rules to the personalization point to tailor the user experience.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[PersonalizationPointChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationPointFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationPointHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationPointOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationPointShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### PersonalizationSchema

Represents a personalization response template that’s used when you build a personalization decision. Available in API version 62.0 and
later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
CurrencyIsoCode

DataSpaceId

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


Standard Objects PersonalizationSchema

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where a response template's resources originate.
This is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Description

DeveloperName

LastReferencedDate

LastViewedDate

Name

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the response template. This is an optional field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization response template. This is a
required field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the personalized response template was referenced
by another resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the response template.

**Type**
string


### Standard Objects PersonalizationTargetInfo

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization response template.

```
PersonalizationType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the kind of personalization content to present. The default value is
Recommendations, and the accepted values are ManualContent and Recommendations.

A response template outlines the attributes that marketers use to configure the personalization response. It defines an expected format
and shape for all decision response data.

**•** For a recommendation-focused personalization, the response template can include an optional placeholder attribute to include
header text before a set of recommendations.

**•** For a manual content personalization, the response template can include placeholders for background images, links, call-to-action
text, and so on.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[PersonalizationSchemaChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationSchemaFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationSchemaHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationSchemaOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationSchemaShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### PersonalizationTargetInfo

Represents a target for an audience. This object is available in API version 47.0 and later.


Standard Objects PersonalizationTargetInfo

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ContainerId

DraftRowId

GroupName

PublishStatus

TargetType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Experience Cloud site or org that contains the target.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the draft PersonalizationTargetInfo.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Group name of the target. Groups bundle related targets. You can have up to 2,000 groups
and 500 targets per group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Publish status of the target.

Possible values are:

**•** `Draft`

**•** `Live`

**Type**
picklist


### Standard Objects PermissionUpdateEventLog

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target.

Possible values are:

**•** `ExperienceVariation`

**•** `NavigationLinkSet`

**•** `Topic`

**•** `CollaborationGroup`

**•** `KnowledgeArticle`

**•** `ContentDocument`

**•** `ManagedContent`

**•** `Report`

**•** `Dashboard`

**•** Custom objects

You can have up to 2,500 `ExperienceVariation` targets and 25,000 record targets.

```
TargetValue

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Value of the target. For ExperienceVariation, this is the developer name of the Experience
Variation or the record ID for the object.

### PermissionUpdateEventLog

Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets or
permission set groups. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects PermissionUpdateEventLog

Fields

**Field** **Details**

```
Context

Description

FeatureIdentifier

LoginKey

PermissionType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context for what is happening for this update.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the update that occurred in the profile, permission set, or permission set
group.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the feature, such as a profile, permission set, or permission set group, that was
updated.

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
The type of permission, such as user, object, or field, or setup entity access, such as tab
settings or Apex class access, that was updated.


Standard Objects PermissionUpdateEventLog

**Field** **Details**

```
RequestIdentifier

SessionKey

Timestamp

UpdateType

UserIdentifier

```

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
For object permissions, user permissions, and setup entity access, the type of update that
occurred. For example, a permission was updated or deleted. For other changes in profiles,
permission sets, or permission set groups, this information is tracked in the DESCRIPTION
field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who made the permission update.


### Standard Objects PersonTraining PersonTraining

Represents an assignment of a learning module in Workforce Engagement. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The org requires a Workforce Engagement license and an Enablement Sites (myTrailhead) license. The user requires at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Admin, Workforce Engagement Analyst, Workforce Engagement
Planner, or Workforce Engagement Agent.

Workforce Engagement Management uses this object to route training to agents. To assign modules to agents, users with the Learning
Manager profile require Read, Create, and View All Records access to this object. To receive routed modules, users with the Learner profile
require Read access to this object.

Fields

**Field** **Details**

```
AssigneeId

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A valid user ID for the user who’s assigned the training. `AssigneeId` can’t be empty if
the `Status` field is Assigned. We recommend that you set `AssigneeId` to the value
in `OwnerId` .

This is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects PersonTraining

**Field** **Details**

**Description**
The name of the learning module.

```
OwnerId

Status

TrainingId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the person training.

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
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the training.

Possible values are:

**•** `A` —Assigned; when the `Status` is assigned, the `AssigneeId` field can’t be empty.

**•** `C` —Completed

**•** `I` —In Progress

**•** `N` —New

**•** `P` —Paused

The default value is 'N'.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the learning module.

This is a relationship field.

**Relationship Name**
Training


### Standard Objects PicklistValueInfo

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
LearningContent

```
TrainingType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of training.

Possible values are:

**•** `T` —Trailhead

In version 54.0 and later releases, Workforce Engagement uses this object instead of the AgentTraining object to route learning modules
to agents. If you set up agent engagement in your org in an earlier release, we rename AgentTraining records as PersonTraining records.

### PicklistValueInfo

Represents the active picklist values for a given picklist field. This object is available in API version 40.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DurableId

EntityParticleId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field.

**Type**
string


Standard Objects PicklistValueInfo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the picklist field to which this value is related.

**Relationship Name**
EntityParticle

**Relationship Type**
Lookup

**Refers To**
EntityParticle

```
IsActive

IsDefaultValue

Label

ValidFor

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the picklist value is active or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this value is the default for the picklist field. Only one value can be the
default value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A set of bits where each bit indicates a controlling value for which this picklist value is valid.


### Standard Objects PickTicket

**Field** **Details**

```
Value

### PickTicket

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the picklist value.

A PickTicket represents quantities of one or more products to be picked for fulfillment at a location. It can include products belonging
to one or more fulfillment orders. This object is available in API version 57.0 and later.

A PickTicket is associated with one or more PickTicketAssignments and one or more PickTicketProducts. Each PickTicketAssignment
represents the relationship between the PickTicket and a FulfillmentOrder. Each PickTicketProduct represents the quantity of a product
to be picked as part of the PickTicket. If multiple FulfillmentOrders associated with the PickTicket include the same product, one
### PickTicketProduct can represent the total quantity of that product to be picked for all of those FulfillmentOrders.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
AssignedToId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user assigned to pick the items associated with the PickTicket.

This field is a relationship field.

**Relationship Name**
AssignedTo

**Relationship Type**
Lookup


Standard Objects PickTicket

**Field** **Details**

**Refers To**
User

```
LastReferencedDate

LastViewedDate

LocationId

OwnerId

```

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

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location fulfilling the items to be picked.

This field is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the PickTicket record. By default, the asset owner is the user who created the
record.

This field is a polymorphic relationship field.


Standard Objects PickTicket

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PickTicketNumber

Status

StatusCategory

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicket.

**Type**
picklist

**Properties**
Create, Filter, Group, Printed, Sort, Update

**Description**
Status of the PickTicket. Each status corresponds to one status category, shown here in
parentheses. You can customize the status picklist to represent your business processes, but
the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.

Default values are:

**•** `Assigned` (Active)

**•** `Canceled` (Canceled)

**•** `Completed` (Completed)

**•** `Created` (Active)

**•** `Draft` (Draft)

**•** `Picked` (Active)

**•** `Picking` (Active)

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status category of the PickTicket. Processing of the PickTicket depends on this value. Each
status category corresponds to one or more status values.

Possible values are:

**•** `ACTIVE`


### Standard Objects PickTicketAssignment

**Field** **Details**

**•** `CANCELED`

**•** `COMPLETED`

**•** `DRAFT`

The default value is `DRAFT` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PickTicketFeed on page 55**
Feed tracking is available for the object.

**PickTicketShare on page 67**
Sharing is available for the object.

SEE ALSO:

### PickTicketAssignment

PickTicketProduct

### PickTicketAssignment

Represents the association of a FulfillmentOrder with a PickTicket. A PickTicket has one PickTicketAssignment for each FulfillmentOrder
containing products to be picked as part of that PickTicket. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
AttachedToId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PickTicketAssignment

**Field** **Details**

**Description**
ID of the FulfillmentOrder to associate with a PickTicket.

This field is a relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder

```
PickTicketAssignmentNumber

PickTicketId

```

SEE ALSO:

PickTicket

FulfillmentOrder

PickTicketProduct

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the PickTicket to associate with a FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
PickTicket

**Relationship Type**
Lookup

**Refers To**
PickTicket


### Standard Objects PickTicketProduct PickTicketProduct

Represents a quantity of a product to be picked as part of a PickTicket. It can include quantities for multiple FulfillmentOrders. This object
is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
PickTicketId

### `PickTicketProductNumber`

PickedQuantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the PickTicket associated with the PickTicketProduct.

This field is a relationship field.

**Relationship Name**
### PickTicket

**Relationship Type**
Lookup

**Refers To**
### PickTicket

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketProduct.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects PickTicketProduct

**Field** **Details**

**Description**
Quantity of the PickTicketProduct that has been picked.

```
Product2Id

ProductCode

Quantity

RejectReason

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product associated with the PickTicketProduct.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code of the product associated with the PickTicketProduct.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Total quantity that’s requested to be picked of the associated product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reason why some or all of the requested quantity isn’t being picked.

Possible values are:

**•** `Defected`

**•** `Other`

**•** `Out of stock`


### Standard Objects PipelineInspectionListView

**Field** **Details**

```
RejectedQuantity

StockKeepingUnit

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested quantity that hasn’t been picked. When the status category of the associated
PickTicket is set to `Completed`, this value is automatically calculated as `Quantity`   `PickedQuantity` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the associated product.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PickTicketProductFeed on page 55**
Feed tracking is available for the object.

SEE ALSO:

PickTicket

PickTicketAssignment

Product2

### PipelineInspectionListView

Represents a pipeline view, an intelligence view, or a saved filter. A pipeline view shows a set of opportunity records, based on specific
criteria. An intelligence view shows a set of account, lead, or contact records, based on specific criteria. This object is available in API
version 53.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects PipelineInspectionListView

Special Access Rules

To access this object, enable the Pipeline Inspection user permission and the Pipeline Inspection setting. To create and modify list views,
users must have the Create and Customize List Views permission. To create and modify public list views, users must have the Manage
Public List Views permission.

Fields

**Field** **Details**

```
ChangePeriodLiteralType

ChangePeriodStartDate

DateLiteralType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The date literal associated with the pipeline changes metrics group, used for filtering by a
custom time period.

Possible values are:

**•** `CUSTOM_DATE`

**•** `FOUR_WEEKS_AGO`

**•** `ONE_MONTH_AGO`

**•** `ONE_WEEK_AGO`

**•** `START_OF_THE_PERIOD`

**•** `THIS_MONTH`

**•** `THIS_WEEK`

**•** `THREE_MONTHS_AGO`

**•** `THREE_WEEKS_AGO`

**•** `TWO_MONTHS_AGO`

**•** `TWO_WEEKS_AGO`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date used when filtering by a custom time period for pipeline changes metrics and
forecast category metrics groups.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects PipelineInspectionListView

**Field** **Details**

**Description**
The date literal associated with the pipeline and intelligence views, used for filtering by the
close date, created date, or activity date.

Possible values are:


Standard Objects PipelineInspectionListView

**Field** **Details**

                           - Available in API version 60.0 and later.

** Available on the "My Important" list views.

```
EndDate

IsSystemManaged

ListViewId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date used when filtering by a custom time period for close dates.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the system is managing changes to visibility and deletion of a pipeline
view ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ListView record. This field is unique within your organization.

This is a relationship field.

**Relationship Name**
ListView


Standard Objects PipelineInspectionListView

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ListView

```
MarketSegments

StartDate

SummaryField

UserId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The customer segments selected in the Prospecting Center view.

This field is available in API version 61.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date used when filtering by a custom time period for close dates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The opportunity field specified in a pipeline view to summarize pipeline inspection metrics.

Possible values are standard field names or custom field IDs for custom currency and number
fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** _**`custom_field_ID`**_

This field is available in API version 56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user whose records you want to see by default in the list view. This field is a
relationship field.


### Standard Objects PipelineInspectionSumField

**Field** **Details**

This field is available in API version 58.0 and later.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

```
ViewType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The corresponding API name for the pipeline or intelligence view type.

Possible values are:

**•** `MY_ACCOUNTS` –Available in API version 60.0 and later.

**•** `MY_AGENTFORCE_SDR_CONTACTS` –Available in API version 64.0 and later.

**•** `MY_AGENTFORCE_SDR_LEADS` –Available in API version 63.0 and later.

**•** `MY_CONTACTS`

**•** `MY_IMPORTANT_ACCOUNTS` –Available in API version 60.0 and later.

**•** `MY_IMPORTANT_CONTACTS`

**•** `MY_IMPORTANT_LEADS`

**•** `MY_IMPORTANT_OPPORTUNITIES`

**•** `MY_LEADS`

**•** `MY_PIPELINE`

**•** `MY_PROSPECTING_CENTER_ACCOUNTS` –Available in API version 61.0 and later.

Use this object to retrieve the metadata for a pipeline inspection view.

### PipelineInspectionSumField

Use this object to learn which field from the opportunity object is used to aggregate Pipeline Inspection metrics on a pipeline view. This
object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects PipelineInspMetricConfig

Special Access Rules

To use PipelineInspectionSumField, enable Pipeline Inspection. Users with a Pipeline Inspection user permission, the Customize Application
permission or the Modify All Data permission can access this object. To create and modify records, users must have either the Customize
Application permission or the Modify All Data permission.

Fields

**Field** **Details**

```
SobjectType

SummaryField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that stores the summary fields.

Possible values are:

**•** `Opportunity`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field used to summarize Pipeline Inspection metrics. Possible values are standard field
names or custom field IDs for custom currency and number fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** custom_field_ID

### PipelineInspMetricConfig

Represents the configuration of a forecast category metric that appears in the Pipeline Inspection view. This object is available in API
version 55.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects PipelineInspMetricConfig

Fields

**Field** **Details**

```
DeveloperName

IsCumulative

Language

MasterLabel

Metric

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Read only. The unique name of a Pipeline Inspection metric configuration in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Whether the metric is cumulative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Read only. The language of the Pipeline Inspection metric.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Customized label of the Pipeline Inspection metric. Limit: 50 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The Pipeline Inspection metric.

Possible values are:

**•** `BestCase`

**•** `ClosedLost`

**•** `ClosedWon`

**•** `Commit`


### Standard Objects PipelineInspMetricConfigLocalization

**Field** **Details**

**•** `MostLikely`

**•** `OpenPipeline`

**•** `TotalPipeline`

### PipelineInspMetricConfigLocalization

Represents the translated label of a Pipeline Inspection metric. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Language

NamespacePrefix

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language of the Pipeline Inspection metric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the Pipeline Inspection metric language.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related Pipeline Inspection metric.

This field is a relationship field.

**Relationship Name**
Parent


### Standard Objects PlatformAction

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PipelineInspMetricConfig

```
Value

### PlatformAction

```

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the Pipeline Inspection metric.

### PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device format,

and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ActionListContext

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The list context this action applies to. Valid values are:

**•** `Assistant`

**•** `BannerPhoto`

**•** `Chatter`

**•** `Dockable`

**•** `FeedElement`

**•** `Flexipage`

**•** `Global`

**•** `ListView`


Standard Objects PlatformAction

**Field** **Details**

**•** `ListViewDefinition`

**•** `ListViewRecord`

**•** `Lookup`

**•** `MruList`

**•** `MruRow`

**•** `ObjectHomeChart`

**•** `Photo`

**•** `Record`

**•** `RecordEdit`

**•** `RelatedList`

**•** `RelatedListRecord`

```
ActionTarget

ActionTargetType

ActionTargetUrl

```

**Type**
textarea

**Properties**
Nillable

**Description**
The URL to invoke or describe the action when the action is invoked. If the action is a standard
button overridden by a Visualforce page, the ActionTarget returns the URL of the Visualforce
page, such as `/apex/` _`pagename`_ .

This field is available in API version 35.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the target when this action is triggered. Valid values are:

**•** `Describe` —applies to actions with a user interface, such as quick actions

**•** `Invoke` —applies to actions with no user interface, such as action links or invocable
actions

**•** `Visualforce` —applies to standard buttons overridden by a Visualforce page

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to invoke or describe the action when the action is invoked. This field is deprecated in
API version 35.0 and later. Use `ActionTarget` instead.


Standard Objects PlatformAction

**Field** **Details**

```
Category

ConfirmationMessage

DeviceFormat

ExternalId

GroupId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Applies only to action links. Denotes whether the action link shows up in the feed item list
of actions or the overflow list of actions. Valid values are:

**•** `Primary`

**•** `Overflow`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only to action links. The message to display before the action is invoked. Field is null
if no confirmation is required before invoking the action.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies which action icon the PlatformAction query returns. If this field isn’t specified, it
defaults to Phone. Valid values are:

**•** `Aloha`

**•** `Desktop`

**•** `Phone`

**•** `Tablet`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID for the PlatformAction. If the action doesn’t have an ID, its API name is used.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PlatformAction

**Field** **Details**

**Description**
The unique ID of a group of action links.

```
IconContentType

IconHeight

IconUrl

IconWidth

InvocationStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type—such as .jpg, .gif, or .png—of the icon for this action. Applies to both
custom and standard icons assigned to actions.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The height of the icon for this action. Applies only to standard icons.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the icon for this action.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The width of the icon for this action. Applies only to standard icons.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the action within the feed item. Applies to action links only. Valid values are:

**•** `Failed`

**•** `New`

**•** `Pending`


Standard Objects PlatformAction

**Field** **Details**

**•** `Successful`

```
InvokedByUserId

IsGroupDefault

IsMassAction

Label

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who most recently invoked this action within the current feed item. Applies
to action links only.

This is a relationship field.

**Relationship Name**
InvokedByUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Denotes whether this action is the default in an action link group. False for other action types.
Applies to action links only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action can be performed on multiple records.

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label to display for this action.


Standard Objects PlatformAction

**Field** **Details**

```
PrimaryColor

RelatedListRecordId

RelatedSourceEntity

Section

SourceEntity

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary color of the icon for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of a record in an object’s related list.

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the `ActionListContext` is RelatedList or RelatedListRecord, this field represents
the API name of the related list to which the action belongs.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The section of the user interface the action resides in. Applicable only to Lightning Experience.
Valid values are:

**•** ActivityComposer

**•** CollaborateComposer

**•** NotesComposer

**•** Page

**•** SingleActionLinks

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects PlatformAction

**Field** **Details**

**Description**
Required. The object or record with which this action is associated.

```
Subtype

TargetObject

TargetUrl

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subtype of the action. For quick actions, the subtype is `QuickActionType` . For
custom buttons, the subtype is `WebLinkTypeEnum` . For action links, subtypes are `Api`,
`ApiAsync`, `Download`, and `Ui` . Standard buttons and productivity actions have no
subtype.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of object record the action creates, such as a contact or opportunity.

This field is available in API version 41.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The URL that a custom button or link points to.

This field is available in API version 41.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the action. Valid values are:

**•** `ActionLink` —An indicator on a feed element that targets an API, a web page, or a
file, represented by a button in the Salesforce Chatter feed UI.

**•** `CustomButton` —When clicked, opens a URL or a Visualforce page in a window or
executes JavaScript.

**•** `InvocableAction`


### Standard Objects PlatformEventUsageMetric

**Field** **Details**

**•** `ProductivityAction` —Productivity actions are predefined and attached to a
limited set of objects. Productivity actions include Send Email, Call, Map, View Website,
and Read News. Except for the Call action, you can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit, and Delete.

Usage

PlatformAction can be described using describeSObject().

You can directly query for PlatformAction. For example, this query returns all fields for actions associated with each of the records of the
listed objects:

```
   SELECT ExternalId, ActionTargetType, ActionTargetUrl, ApiName, Category,

       ConfirmationMessage, ExternalId, GroupId, UiTheme, IconUrl, IconContentType,

       IconHeight, IconWidth, PrimaryColor, InvocationStatus, InvokedByUserId,

       IsGroupDefault, Label, LastModifiedDate, Subtype, SourceEntity, Type

   FROM PlatformAction

   WHERE SourceEntity IN ('001xx000003DGsH', '001xx000003DHBq', ‘Task’) AND

       ActionListContext = ‘Record’;

```

Note: To query PlatformAction, provide the `ActionListContext` and `SourceEntity` . If you query for
`ActionListContext` with a value of `RelatedList`, and don't specify a `RelatedSourceEntity`, the query returns
the API name of the related list. In API v43.0 and before, `SourceEntity = '` _**`Object API Name`**_ `' and`
`ActionListContext = 'ListView'` is an invalid combination to fetch quick actions in a SOQL query. Use
`SourceEntity = '` _**`Object ID`**_ `' and ActionListContext = 'ListView'` instead.

This query uses multiple `ActionListContext` values in its `WHERE` clause to return all actions in the Lightning Experience user
interface ( `DeviceFormat = 'Desktop'` ) for the specified object:

```
   SELECT ActionListContext, Label, Type, Subtype, Section, SourceEntity,

      RelatedSourceEntity, ActionTarget, ActionTargetType, ApiName, Category,

      ConfirmationMessage, DeviceFormat, ExternalId, GroupId, IconContentType,

      IconHeight, IconUrl, IconWidth, Id, InvocationStatus, InvokedByUserId,

      IsGroupDefault, LastModifiedDate, PrimaryColor

   FROM PlatformAction

   WHERE ActionListContext IN ('Record','Chatter','RelatedList') AND

       SourceEntity = '001xx000003DlvX' AND

       DeviceFormat = 'Desktop'

### PlatformEventUsageMetric

```

Contains usage data for event publishing and delivery to CometD and Pub/Sub API clients, `empApi` Lightning components, and event
relays. If Enhanced Usage Metrics isn't enabled, usage data is available for the last 24 hours, ending at the last hour, and for historical
daily usage. In API 58.0 and later, you can enable Enhanced Usage Metrics to get usage data by event name and client for granular time
intervals. PlatformEventUsageMetric contains separate usage metrics for platform events and change data capture events. This object
is available in API version 50.0 and later.


Standard Objects PlatformEventUsageMetric

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
Client

EndDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The ID of the client. The
`Client` field is populated with one of the following values.

The `Client` field can be one of these values.

**•** For a Streaming API (CometD) client and the empApi Lightning component, the client
value is the ID of the CometD session.

**•** For a Pub/Sub API client, the client value is `PUB_SUB_API` .

**•** For an event relay, the client value is `EVENT_RELAY` .

**•** For the publish usage of Change Data Capture events, the client value is `SYSTEM` .

**•** For publish usages using REST API, the client value is `REST_API` .

**•** For publish usages using Flow, the client value is `FLOW` .

**•** For publish usages using SOAP API, the client value is `SOAP_API` .

**•** For publish usages using Bulk API, the client value is `BULK_API` .

**•** For Apex, the publish usage client value is `APEX` and the delivery usage client value is
the Apex Trigger ID starting with 01q.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time in UTC used for querying usage metrics. The date granularity is hourly.

To get usage data for the last 24 hours, the end date is the current date in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-04T11:00:00.000Z

To get historical data, the end date in UTC is the end of the date range with hours specified
as 0. For example: 2020-08-04T00:00:00.000Z. To query a date range, you can use the < or
<= operators.

[For the date format to use, see Date Formats and Date Literals in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm) _SOQL and SOSL Reference_ .


Standard Objects PlatformEventUsageMetric

**Field** **Details**

```
EventName

EventType

ExternalId

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The API name of a
custom platform event or a change event.

**•** Custom platform event with the label My Event: `My_Event__e`

**•** Change event example: `AccountChangeEvent`

When you query usage metrics for `EventName`, specify the `UsageType` field in the
`SELECT` or `WHERE` clause.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event you would
like to query usage metrics for, such as a change event or a custom platform event.

Possible values are:

**•** `CHANGE_EVENT` —A Change Data Capture event.

**•** `CUSTOM_PLATFORM_EVENT` —A platform event that an admin defined in your
Salesforce org.

When you query usage metrics for `EventType`, specify the `UsageType` field in the
`SELECT` or `WHERE` clause.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the metric to get usage for.

Possible values are:


Standard Objects PlatformEventUsageMetric

**Field** **Details**

**•** `CHANGE_EVENTS_DELIVERED` —Number of change data capture events delivered
to CometD and Pub/Sub API clients, `empApi` Lightning components, and event relays

**•** `CHANGE_EVENTS_PUBLISHED` —Number of change data capture events published

**•** `PLATFORM_EVENTS_DELIVERED` —Number of platform events delivered to CometD
and Pub/Sub API clients, `empApi` Lightning components, and event relays

**•** `PLATFORM_EVENTS_PUBLISHED` —Number of platform events published

```
StartDate

TimeSegment

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date and time in UTC used for querying usage metrics. The date granularity is hourly.

To get usage data for the last 24 hours, the start date is the previous day in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-03T11:00:00.000Z

To get historical data, the start date is the start of the date range with hours specified as 0.
For example: 2020-08-03T00:00:00.000Z. To specify a date range, you can use the > or >=
operators.

If Enhanced Usage Metrics is enabled, keep in mind these tips.

**•** Make sure the time span between `StartDate` and `EndDate` is valid for the
`TimeSegment` value chosen.

**•** The maximum date range that you can specify between `StartDate` and `EndDate`
is 60 days.

[For the date format to use, see Date Formats and Date Literals in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm) _SOQL and SOSL Reference_ .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The time interval used for
aggregating usage data returned in the query results. Valid `TimeSegment` values depend
on the time range specified with `StartDate` and `EndDate` .

Possible values are:


### Standard Objects PlatformStatusAlertEvent

**Field** **Details**

```
UsageType

Value

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event usage
metrics to query for, such as event publishing or event delivery. Use this field with the
`EventName` or `EventType` fields.

Possible values are:

**•** `PUBLISH` —Usage metrics for published events.

**•** `DELIVERY` —Usage metrics for events that were delivered to subscribers.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The usage value for the specified metric and date range.

[For more information, see Monitor Platform Event Publishing and Delivery Usage in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_monitor_usage.htm) _Platform Events Developer Guide_ .

### PlatformStatusAlertEvent

[The documentation has moved to PlatformStatusAlertEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_platformstatusalertevent.htm) _Platform Events Developer Guide_ .


### Standard Objects PortalDelegablePermissionSet PortalDelegablePermissionSet PortalDelegablePermissionSet is a base platform object used to store permission sets that can be assigned by a delegated portal/external

user admin (DPUA) to portal users. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

PermissionSetId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string used to identify the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string to identify the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the permission set the DPUA profile can assign to other portal users.


### Standard Objects PplnInspListViewCalcClmn

**Field** **Details**

```
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the DPUA profile.

### PplnInspListViewCalcClmn

Represents a column configuration for a pipeline inspection list view. Determines which calculated columns appear in a pipeline or
intelligence view and their display order. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable the Pipeline Inspection user permission and the Pipeline Inspection setting.

Fields

**Field** **Details**

```
ColumnName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of calculated column to display in the pipeline or intelligence view.

Possible values are:

**•** `ActivityHeatmap` –Activity metrics for the record.

**•** `AgentActivity` –Agentforce activity associated with the record.

**•** `Contacts` –Contacts associated with the record.

**•** `CriticalInsights` –Alerts and critical insights for the record.

**•** `NextOpportunityDate` –Next close date for an associated opportunity.

**•** `OpenOpportunityValue` –Total value of open opportunities associated with the
record.

**•** `SalesMethodology` –Sales methodology progress for the record.


### Standard Objects PresenceConfigDeclineReason

**Field** **Details**

```
ColumnWidth

PipelineInspectionListViewId

SortOrder

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The width of the column in pixels. If null, the default column width is used.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the pipeline inspection list view that this calculated column belongs to.

This is a relationship field.

**Relationship Name**
PipelineInspectionListView

**Relationship Type**
Lookup

**Refers To**
PipelineInspectionListView

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The position of the calculated column in the list view. Determines the display order of columns
from left to right.

Use this object to configure which calculated columns appear in a pipeline inspection list view and in what order. Each record represents
one column in a specific view. Query this object to retrieve the column configuration for a given PipelineInspectionListView record.

### PresenceConfigDeclineReason

Represents the settings for a decline reason that a presence user provides when declining work. This object is available in API version
37.0 and later.


### Standard Objects PresenceDeclineReason

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

### `PresenceDeclineReasonId`

```
PresenceUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the PresenceDeclineReason record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the PresenceUserConfig record where the decline reasons are added.

### PresenceDeclineReason

Represents an Omni-Channel decline reason that agents can select when declining work requests. This object is available in API version
37.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects PresenceUserConfig

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the PresenceDeclineReason.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label for the PresenceDeclineReason.

### PresenceUserConfig

Represents a configuration that determines a presence user’s settings. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`


Standard Objects PresenceUserConfig

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AcwExtensionDuration

AfterConvoWorkMaxTime

Capacity

CustomSoundId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Specify a value from 10 through 3600.

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if `HasAfterConvoWorkTimer` is
set to `true` . Specify a value from 10 through 3600.

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The maximum number of work units an agent can be assigned at one time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  CustomSound

```


Standard Objects PresenceUserConfig

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**

```
                   StaticResource

```

**Description**
The ID of the static resource for the custom sound selected to play for the
`PresenceUserConfig` object.

```
DeveloperName

HasAcwExtensionEnabled

HasAfterConvoWorkTimer

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

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance may slow while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, agents can extend their After Conversation Work (ACW) time. Available only
if `HasAfterConvoWorkTimer` is set to `true` . If set to `true`, you must also set the
`AcwExtensionDuration` and `MaxExtensions` fields. The default value is `true` .

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects PresenceUserConfig

**Field** **Details**

**Description**
If set to `true`, After Conversation Work (ACW) time can be configured for the channel. If
set to `true`, you must also set the `AfterConvoWorkMaxTime` field. The default value
is `false` .

This field is available in API version 56.0 and later.

```
Language

MasterLabel

MaxExtensions

OptionsIsAllowAnyDestinationQueueForTransferEnabled

OptionsIsAllowAnyDestinationFlowForTransferEnabled

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence configuration.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true` .

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
queue ( `true` ) or only the selected queues ( `false` ).

This field is available in API version 61.0 and later.

**Type**
boolean


Standard Objects PresenceUserConfig

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
flow ( `true` ) or only the selected flows ( `false` ).

This field is available in API version 61.0 and later.

```
OptionsIsAllowAnyDestinationProfileForTransferEnabled

OptionsIsAutoAcceptEnabled

OptionsIsDeclineEnabled

OptionsIsDeclineReasonEnabled

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
profile ( `true` ) or only the selected profiles ( `false` ).

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether work items that are routed to agents are automatically accepted ( `true` )
or not ( `false` ). Available only if `OptionsIsDeclineEnabled` is set to `false` .

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can decline work items that are routed to them ( `true` ) or not
( `false` ). Available only if `OptionsIsAutoAcceptEnabled` is set to `false` .

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can select a reason for declining work requests ( `true` ) or not
( `false` ). This can be selected only if decline reasons are enabled.


Standard Objects PresenceUserConfig

**Field** **Details**

```
OptionsIsDisconnectSoundEnabled

OptionsIsRequestSoundEnabled

PresenceStatusOnDeclineId

PresenceStatusOnPushTimeoutId

SoundLength

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound is played when agents are disconnected from Omni-Channel
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound plays with incoming work requests ( `true` ) or not ( `false` ). Set
to `true` by default.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
declines a work item. Available only if `OptionsIsDeclineEnabled` is set to `true` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
doesn’t respond to a work item before push timeout occurs. Available in API version 36.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.


### Standard Objects PresenceUserConfigProfile PresenceUserConfigProfile

Represents a configuration that determines the settings that are assigned to presence users who are assigned to a specific profile.
User-level configurations override profile-level configurations. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
PresenceUserConfigId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If an individual user is also assigned a presence configuration through the
### PresenceUserConfigProfile, this configuration will override that.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the profile that’s associated with this presence configuration. A profile can be
associated with only one presence configuration.

### PresenceUserConfigUser

Represents a configuration that determines the settings that are assigned to a presence user. These user-level configurations override
profile-level configurations. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`


### Standard Objects PriceAdjustmentGroupShape

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
PresenceUserConfigId

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the presence configuration.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user who’s associated with this presence configuration. A user can be associated
with only one presence configuration.

### PriceAdjustmentGroupShape

Defines the business logic for a top-level price adjustment, for example, a discount applied to an entire order. This object is available in
API version 57.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AdjustmentSource

```

**Type**
picklist


Standard Objects PriceAdjustmentGroupShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the source of the adjustment. This field is available with B2B Commerce.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually, for example, by a sales rep.

**•** `Promotion` —The adjustment is part of a promotion.

**•** `Rule` —Reserved for future use.

**•** `System` —The adjustment is configured by the system data, for example, as part of a
pricing rule or discount schedule.

```
AdjustmentType

AdjustmentValue

Description

PriceAdjustmentCauseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the adjustment is a percentage, an amount, or an override.

Possible values are:

**•** `AdjustmentAmount` —Reserved for future use. The adjustment value is a numerical
amount.

**•** `AdjustmentPercentage`  - The adjustment value is a percentage.

**•** `OverrideAmount`  - The override value is a numerical amount.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The value of the adjustment. To indicate a discount, use a negative number.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
User-entered description of the price adjustment group. Available in API versions 57.0.

**Type**
reference


Standard Objects PriceAdjustmentGroupShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that is the source of the adjustment. For example, if the price adjustment
is due to a promotion, this field contains the ID of the promotion record. If the price
adjustment is due to a price adjustment tier, this field contains the ID of the price adjustment
tier record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

```
PriceAdjustmentGroupShapeName

Priority

SalesTransactionShapeId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Name of the price adjustment group shape.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A positive integer indicating the order in which this price adjustment group is applied, relative
to other price adjustment groups. A `Priority` of `1` indicates this price adjustment group
is applied first.

Price adjustments with a null priority are applied after price adjustments with a specified
priority. If two or more price adjustments have a null priority, percentage adjustments are
applied **before** amount adjustments. Applying a percentage adjustment before an amount
adjustment results in a larger total adjustment.

Note: The value of `Priority` must be unique among price adjustment groups
in the same sales transaction.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
The ID of the sales transaction that the price adjustment group belongs to.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

```
TotalAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total amount of adjustments of all related price adjustment items, inclusive of quantity,
prorated for the duration of the subscription. This field is a calculated field equal to the sum
of the `TotalAmount` fields in the related price adjustment items.

### PriceAdjustmentItemShape

Defines the business logic for an item-level price adjustment, for example, a discount on an order item. This object is available in API
version 57.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total` —The adjustment applies to the line item's total and isn’t multiplied by the
quantity.

For example, let's say a sales transaction item quantity is `10` and the
`TotalLineAmount` is `1000` . If the price adjustment item has an
`AdjustmentValue` of `-10`, an `AdjustmentType` of `AdjustmentAmount`,
and an `AdjustmentAmountScope` of `Total`, the $10 discount is applied to the
total line amount. The `TotalAmount` of the price adjustment item is $1000 + (-$10)
= $990.

**•** `Unit` —The adjustment is multiplied by the line item’s quantity.

For example, let's say a sales transaction item quantity is `5` and the
`TotalLineAmount` is `1000` . If the price adjustment item has an
`AdjustmentValue` of `-10`, an `AdjustmentType` of `AdjustmentAmount`,
and an `AdjustmentAmountScope` of `Unit`, the $10 discount is applied to each
line amount. The TotalAmount of the price adjustment item is $1000 + (-$10 x 5) = $950.

**•** `UnproratedTotal` —No adjustment is applied to the line items.

```
AdjustmentSource

AdjustmentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the source of the adjustment.

Possible values are:

**•** `Discretionary`  - The adjustment is entered manually; for example, by a sales rep.

**•** `Promotion`  - The adjustment is a promotion.

**•** `Rule`  - Reserved for future use.

**•** `System`  - The adjustment is determined by the pricing configuration for the product;
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the adjustment is a percentage, an amount, or an override.

Possible values are:

**•** `AdjustmentAmount` —The adjustment value is a numerical amount.


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**•** `AdjustmentPercentage`                   - The adjustment value is a percentage.

**•** `OverrideAmount`                   - The override value is a numerical amount.

```
AdjustmentValue

Description

PriceAdjustmentCauseId

PriceAdjustmentGroupShapeId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The value of the adjustment. Used together with `AdjustmentAmountScope` to
determine the amount of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The user-entered description of the price adjustment item. Available in API version 57.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. For example, if the price adjustment is due
to a promotion, this field contains the ID of the Promotion record. If the price adjustment is
due to a price adjustment tier, this field contains the ID of the `PriceAdjustmentTier`
record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
A reference to the object interface or object that summarizes the values from multiple price
adjustment items. If the related entity is an object, the object must implement the
`PriceAdjustmentGroupShape` object.

This field is a relationship field.

**Relationship Name**
PriceAdjustmentGroupShape

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentGroupShape

```
PriceAdjustmentItemShapeName

Priority

SalesTransactionItemShapeId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the price adjustment item shape.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A positive integer indicating the order in which this price adjustment item is applied, relative
to other price adjustment items. A `Priority` of `1` indicates this price adjustment item
is applied first.

Price adjustments with a null priority are applied after price adjustments with a specified
priority. If two or more price adjustments have a null priority, percentage adjustments are
applied **before** amount adjustments. Applying a percentage adjustment before an amount
adjustment results in a larger total adjustment.

Note: The value of `Priority` must be unique among price adjustment items
related to the same price adjustment group. For example, you can’t have two price
adjustment items with a priority of `1` .

For example, let’s say that two price adjustment items apply to the same item to be priced.
The first price adjustment, Spring_Promotion, defines a 10% discount and has `Priority`
of `1` . The second price adjustment, Early_Renewal_Discount, defines a $2,000 discount and
has a `Priority` of `2` . In this case, the Spring_Promotion price adjustment is applied
before the Early_Renewal_Discount price adjustment.

**Type**
reference


### Standard Objects PriceAdjustmentSchedule

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the sales transaction shape item that the price adjustment item applies to.

This field is a relationship field.

**Relationship Name**
SalesTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

```
TotalAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total amount of the adjustment that applies to the item to be priced, inclusive of quantity,
prorated for the duration of the subscription.

For example, let’s say the price adjustment item has an `AdjustmentAmountScope` of
`Unit`, an `AdjustmentType` of `AdjustmentAmount`, and an `AdjustmentValue`
of `-10` . This configuration indicates a $10 per-unit discount. If the subscription is priced for
12 months and the pricing term is `1`, the `PricingTermCount` on the sales transaction
item is 12. If the quantity is 5, the value of `TotalAmount` is 5 x 12 x -10 = -600

### PriceAdjustmentSchedule

Represents a series of discounts offered depending on your product's configuration, quantity, and when they’re purchased in combination
with other products. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when the B2B Commerce license is enabled or when Subscription Management is enabled.


Standard Objects PriceAdjustmentSchedule

Fields

**Field** **Details**

```
AdjustmentMethod

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method for applying tiered pricing. Possible values are:

**•** `Range` —All items receive the discount of the highest tier the quantity falls in.

**•** `Slab` —Items receive the discount defined for the tier they fall in.

The default value is `Range` . Term-based discounts can’t be of type `Slab` . This field is
available in API version 51.0 and later.

The `Slab` method functions in the same way as the `Range` method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price adjustment schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price adjustment schedule is active ( `true` ) or not ( `false` ). You can
change this field’s value as often as necessary. Label is **Active** . The default value is `False` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates whether the price adjustment schedule has been archived ( `true` ) or not ( `false` ).
This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PriceAdjustmentSchedule

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

ScheduleType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the price adjustment schedule. This field is read-only. Label is **Price**
**Adjustment Schedule Name** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The Salesforce ID of the sales representative who owns the price adjustment schedule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the price adjustment is determined. This field is available when Subscription
Management is enabled. This field is available in API version 55.0 and later.

Possible values are:

**•** `Attribute` —The characteristics or properties of a product determine the price
adjustment.

**•** `Bundle` —The price adjustment that is determined when you want to sell a group of
products or services as a unit.

**•** `Custom` —The price adjustment that can be customized for the user's needs.

**•** `Term` —The length of the subscription determines the price adjustment. Available in
API version 58.0 and later.

**•** `Volume` —The quantity purchased determines the price adjustment.

The default value is `Volume` .


Standard Objects PriceAdjustmentSchedule

Usage

When you create a PriceAdjustmentSchedule, you associate PriceAdjustmentTiers with it. A PriceAdjustmentSchedule is inactive until
at least one PriceAdjustmentTier is added to it. A PriceAdjustmentSchedule comprises all related PriceAdjustmentTiers, with a maximum
limit of 25 PriceAdjustmentTiers for Subscription Management.

To use PriceAdjustmentSchedule, associate it with a PriceBookEntry.

**•** You can associate a PriceBookEntry with up to five PriceAdjustmentSchedules, but only one PriceAdjustmentSchedule can be
associated with a PriceBookEntry.

**•** When you activate or deactivate a PriceAdjustmentSchedule, its PriceBookEntry association is also activated or deactivated.

**•** An adjustment to a PriceBookEntry is applied only if the associated PriceAdjustmentSchedule is active.

**•** After a PriceAdjustmentSchedule is associated with a PriceBookEntry, if multicurrency is enabled, the currencyIsoCode field can’t be
modified.

**•** When you associate a PriceAdjustmentSchedule with a PricebookEntry, a junction object PricebookEntryAdjustment is created.

You can modify the PriceAdjustmentTier object, and the `ScheduleType` and `AdjustmentMethod` fields, only when a
PriceAdjustmentSchedule is inactive.

Code Sample

```
   public void priceAdjustmentScheduleSample()

             {try

              /* This code snippet will do the following:

     *

     * 1. Create a new Price Adjustment Schedule

     * 2. Create and attach a Price Adjustment Tier to the Schedule

     * 3. Activate the Schedule

     * 4. Create a new PricebookEntry Adjustment. This will associate the Schedule to a

   Pricebook Entry. */

     //Create a Price Adjustment Schedule

     PriceAdjustmentSchedule pas = new PriceAdjustmentSchedule();

     pas.Name = 'Sample PAS';

     pas.Description = 'Sample Price Adjustment Schedule';

     pas.AdjustmentMethod = 'Range';

     insert pas;

     //Attach a valid Price Adjustment Tier

     PriceAdjustmentTier pat = new PriceAdjustmentTier();

     pat.PriceAdjustmentScheduleId = pas.Id;

     pat.LowerBound = 1.0;

     pat.UpperBound = 100.0;

     pat.TierType = 'AdjustmentPercentage';

     pat.TierValue = 5.0;

     insert pat;

     //Activate the Schedule

     pas.IsActive = true;

     upsert pas;

     //Create a new PricebookEntry Adjustment

     PricebookEntryAdjustment pbea = new PricebookEntryAdjustment();

```


### Standard Objects PriceAdjustmentTier

```
     pbea.PricebookEntryId = '01uRM0000007Hb5YAE';

     pbea.PriceAdjustmentScheduleId = pas.Id;

     insert pbea;

    } catch (ConnectionException ce) {

     ce.printStackTrace();

    }

   }

```

SEE ALSO:

### PriceAdjustmentTier

PricebookEntryAdjustment

### PriceAdjustmentTier

Represents a discount tier in a price adjustment schedule. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
LowerBound

Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The minimum quantity the discount can be applied to. It must be a positive integer and less
than or equal to the upper bound of the tier.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.


Standard Objects PriceAdjustmentTier

**Field** **Details**

```
PriceAdjustmentScheduleId

TierType

TierValue

UpperBound

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the price adjustment schedule that the discount is applied to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of the discount. Possible values are:

**•** `AdjustmentAmount` —An amount discounted from an item’s list price. Label is
Amount.

**•** `AdjustmentPercentage` —A percentage discounted from an item’s list price.
Label is Percentage.

**•** `AdjustmentOverride` —An override of an item’s list price. Label is Override.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the discount.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum quantity the discount can be applied to. The quantity must be a positive
integer. Not inclusive. Set this value one digit higher than the quantity you want the tier to
include. For example, if a tier’s upper bound is 99, set the value of `UpperBound` to 100.
For the last tier, the value is optional.

To use PriceAdjustmentTiers, associate them with a PriceAdjustmentSchedule.


### Standard Objects Pricebook2

Tiers can’t overlap, and no gaps are allowed between tiers.

SEE ALSO:

PriceAdjustmentSchedule

### Pricebook2

Represents a price book that contains the list of products that your org sells.

Note: Price books are represented by Pricebook2 objects. As of API version 8.0, the Pricebook object is no longer available. Requests
containing Pricebook are refused, and responses don’t contain the Pricebook object.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

IsActive

IsArchived

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price book.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price book is active ( `true` ) or not ( `false` ). Inactive price books are
hidden in many areas in the user interface. You can change this field’s value as often as
necessary. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the price book has been archived (true) or not (false). This field is read
only.


Standard Objects Pricebook2

**Field** **Details**

```
IsDeleted

IsStandard

LastReferencedDate

LastViewedDate

Name

ValidFrom

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the price book has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the price book is the standard price book for the org ( `true` ) or not
( `false` ). Every org has one standard price book—all other price books are custom price
books.

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
Required. Name of this object. This field is read-only for the standard price book. Label is
**Price Book Name** .

**Type**
dateTime


Standard Objects Pricebook2

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is initially valid. If this field is `null`, the
price book is valid immediately when active. Available in API version 48.0 and later.

```
ValidTo

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is valid to. If this field is `null`, the price
book is valid until it’s deactivated. Available in API version 48.0 and later.

A price book is a list of products that your org sells.

**•** Each org has one standard price book that defines the standard or generic list price for each product or service that it sells.

**•** An org can have multiple custom price books to use for specialized purposes, such as for discounts, different channels or markets,
or select accounts or opportunities. While your client application can create, delete, and update custom price books, your client
application can only update the standard price book.

**•** For some orgs, the standard price book is the only price needed. If you set up other price books, you can reference the standard
price book when setting up list prices in custom price books.

Use this object to query standard and custom price books that have been configured for your org. A common use of this object is to
allow your client application to obtain valid Pricebook2 object IDs for use when configuring PricebookEntry records via the API.

Your client application can perform the following tasks on PricebookEntry objects:

**•** Query

**•** Create for the standard price book or custom price books.

**•** Update

**•** Delete

**•** Change the `IsActive` field when creating or updating records

PriceBook2, Product2, and PricebookEntry Relationships

In the API:

**•** Price books are represented by Pricebook2 records (as of version 8.0, the Pricebook object is no longer available).

**•** Products are represented by Product2 records (as of version 8.0, the Product object is no longer available).

**•** Each price book contains zero or more entries (represented by PricebookEntry records) that specify the products that are associated
with the price book. A price book entry defines the price for which you sell a product at a particular currency.


Standard Objects Pricebook2

These objects are defined only for those orgs that have products enabled as a feature. If the org doesn’t have the products feature
enabled, the Pricebook2 object doesn’t appear in the `describeGlobal()` call, and you can’t access it via the API.

If you delete a Pricebook2 while a line item references PricebookEntry in the price book, the line item is unaffected, but the Pricebook2
is archived and unavailable from the API.

For a visual diagram of the relationships between Pricebook2 and other objects, see Product and Schedule Objects.

Price Book Setup

The process of setting up a price book via the API usually means:

**1.** Load product data into Product2 records (creating one Product2 record for each product that you want to add).

**2.** For each Product2 record, create a PricebookEntry that links the Product2 record to the standard Pricebook2. Define a standard price
for a product at a given currency (if you have multicurrency enabled) before defining a price for that product in the same currency
in a custom price book.

**3.** Create a Pricebook2 record to represent a custom price book.

**4.** For each Pricebook2 record, creating a PricebookEntry for every Product2 that you want to add, specifying unique properties for
each PricebookEntry (such as the `UnitPrice` and `CurrencyIsoCode` ) as needed.

Code Sample—Java

```
   public void pricebookSample() {

     try {

      //Create a custom pricebook

      Pricebook2 pb = new Pricebook2();

      pb.setName("Custom Pricebok");

      pb.setIsActive(true);

      SaveResult[] saveResults = connection.create(new SObject[]{pb});

      pb.setId(saveResults[0].getId());

      // Create a new product

      Product2 product = new Product2();

      product.setIsActive(true);

      product.setName("Product");

      saveResults = connection.create(new SObject[]{product});

      product.setId(saveResults[0].getId());

      // Add product to standard pricebook

      QueryResult result = connection.query(

        "select Id from Pricebook2 where isStandard=true"

      );

      SObject[] records = result.getRecords();

      String stdPbId = records[0].getId();

      // Create a pricebook entry for standard pricebook

      PricebookEntry pbe = new PricebookEntry();

      pbe.setPricebook2Id(stdPbId);

      pbe.setProduct2Id(product.getId());

      pbe.setIsActive(true);

      pbe.setUnitPrice(100.0);

      saveResults = connection.create(new SObject[]{pbe});

```


### Standard Objects Pricebook2History

```
      // Create a pricebook entry for custom pricebook

      pbe = new PricebookEntry();

      pbe.setPricebook2Id(pb.getId());

      pbe.setProduct2Id(product.getId());

      pbe.setIsActive(true);

      pbe.setUnitPrice(100.0);

      saveResults = connection.create(new SObject[]{pbe});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[Pricebook2ChangeEvent (API version 48.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **Pricebook2History**

History is available for tracked fields of the object.

### Pricebook2History

Represents historical information about changes that have been made to the standard fields of the associated Pricebook2, or to any
custom fields with history tracking enabled. This object is available in API version 66.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
Pricebook2Id

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects Pricebook2History

**Field** **Details**

**Description**
ID of the Pricebook2 associated with this record.

This is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
DataType

Field

IsDeleted

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
Name of the price book field that was modified, or a special value to indicate some other
modification to the price book.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
This is a standard system field. Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified price book field. Maximum of 255 characters.


### Standard Objects PricebookEntry

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
Previous value of the modified price book field. Maximum of 255 characters.

Price book history entries are indirectly created each time a price book is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Pricebook2

### PricebookEntry

Represents a product entry (an association between a Pricebook2 and Product2) in a price book.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

Note: Salesforce Object Search Language (SOSL) allows you to search records across standard and custom objects. When filtering
records in the PriceBookEntry object using SOSL, you can only sort by fields related to Product2.

**Field** **Details**

```
ActivePriceAdjustmentQuantity

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PricebookEntry

**Field** **Details**

**Description**
The count of active price adjustment schedules associated with the price book entry. This
field is available in API version 49.0 and later. This field is available with a B2B or D2C
Commerce license.

```
CurrencyIsoCode

IsActive

IsArchived

Name

Pricebook2Id

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry is active ( `true` ) or not ( `false` ). Although you can
never delete PricebookEntry records, your client application can set this flag to `false` .
Inactive PricebookEntry records are hidden in many areas in the user interface. You can
change this flag on a PricebookEntry record as often as necessary.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the PricebookEntry has been archived (true) or not (false). This field is set
to `true` when the Product2 record it’s associated with is archived, or when the Pricebook2
record is archived. This field is read only. Available in API version 45.0 and later. Label is
**Archived** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this PricebookEntry record. This read-only field references the value in the Name
field of the Product2 record. Label is **Product Name** .

**Type**
reference


Standard Objects PricebookEntry

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Pricebook2 record with which this record is associated. This field must
be specified when creating Pricebook2 records. It can’t be changed in an update.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
Product2Id

ProductCode

ProductSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 record with which this record is associated. This field must be
specified when creating Product2 records. It can’t be changed in an update.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code for this record. This read-only field references the value in the **ProductCode**
field of the associated Product2 record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects PricebookEntry

**Field** **Details**

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and later.
This field is available when Subscription Management is enabled.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

```
UnitPrice

UseStandardPrice

```

Usage

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Unit price for this price book entry. You can specify a value only if
`UseStandardPrice` is set to `false` . Label is **List Price** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry uses the standard price defined in the standard
Pricebook2 record ( `true` ) or not ( `false` ). If set to `true`, then the `UnitPrice` field is
read-only, and the value is the same as the `UnitPrice` value in the corresponding
PricebookEntry in the standard price book (that is, the PricebookEntry record whose
`Pricebook2Id` refers to the standard price book and whose `Product2Id` and
`CurrencyIsoCode` are the same as this record). For PricebookEntry records associated
with the standard Pricebook2 record, this field must be set to `true` .

Use this object to define the association between your organization’s products (Product2) and your organization’s standard price book
or to custom price books ( Pricebook2). Create one PricebookEntry record for each standard or custom price and currency combination
for a product in a Pricebook2.

When creating these records, you must specify the IDs of the associated Pricebook2 record and Product2 record. Once these records are
created, your client application can’t update these IDs.

This object is defined only for those organizations that have products enabled as a feature. If the organization doesn’t have the products
feature enabled, then the PricebookEntry object doesn’t appear in the describeGlobal call, and you can’t access it.

If you delete a PriceBookEntry that is referenced by a line item, the line item is unaffected, but the PriceBookEntry is archived and
unavailable from the API. Deleted PriceBookEntry records can’t be recovered.


### Standard Objects PricebookEntryAdjustment

You must load the standard price for a product before you’re permitted to load its custom prices.

Associated Objects

This object has the following associated objects. Unless otherwise noted, they’re available in the same API version as this object.

**PricebookEntryChangeEvent(API version 57.0)**
Change events are available for the object.

**PricebookEntryHistory**

History is available for tracked fields of the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### PricebookEntryAdjustment

Read-only junction object created when you associate a price adjustment schedule with a price book entry. This object is available in
API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Name

PriceAdjustmentScheduleId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects PriceProtectionExecution

**Field** **Details**

**Description**
The ID of the price book entry adjustment.

```
PricebookEntryId

```

SEE ALSO:

PriceAdjustmentSchedule

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book entry that this price book entry adjustment is associated with.

### PriceProtectionExecution

Represents an instance of running the price protection process, capturing execution time, status, and the effective date of price changes.
This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ExecutionJobId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Data processing engine instance responsible for creating price protection records.

This field is a relationship field.

**Relationship Name**
ExecutionJob

**Refers To**
BatchCalcJobDefinition


Standard Objects PriceProtectionExecution

**Field** **Details**

```
ExecutionReferenceNumber

LastExecutionTime

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

Unique reference number generated by the Data Processing Engine for this execution. This
can be used to associate related line items to the same execution.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date and time when the price protection execution was last performed by the Data Processing
Engine.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the record was last referenced. This is used internally to optimize
performance and user experience.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Date and timestamp when the record was last viewed in the Salesforce UI. Helps track user
engagement.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

Auto-generated name for the price protection execution record. Used as the primary identifier
within the system.


### Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
OwnerId

PriceChangeEffectiveDate

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifier for the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Date when the new price goes into effect as part of the price protection execution.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the current lifecycle status of the price protection execution process.

Possible values are:

**•** `Completed`

**•** `New`

**•** `Processing`

### PriceProtectExecLineItem

Represents a line item created as part of a Price Protection Execution. This object is available in API version 63.0 and later.

A PriceProtectExecLineItem record is automatically generated by the Data Processing Engine when eligible product transactions are
processed for price protection. It links to execution records, products, and pricing terms, and stores per-unit pricing, eligibility, and
calculation details.


Standard Objects PriceProtectExecLineItem

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

CalculatedAmount

CalculationReferenceRecordId

ClaimReferenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the partner account related to the transaction being evaluated for price protection.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total protected amount calculated based on the applicable price difference and quantity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the rebate or pricing rule used to compute the claim.

This field is a relationship field.

**Relationship Name**
CalculationReferenceRecord

**Refers To**
ProgramRebateType

**Type**
reference


Standard Objects PriceProtectExecLineItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to the related rebate claim, if one has been generated.

This field is a polymorphic relationship field.

**Relationship Name**
ClaimReference

**Refers To**
RebateClaim

```
HasWarnings

InTransitQuantity

IsEligible

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the execution line item has associated warnings.

The default value is `false` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity of the product in transit.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the record qualifies for price protection.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by a user or system.


Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
LastViewedDate

LocationId

Name

NewSalePricePerUnit

NewSalePriceType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and timestamp when the record was last opened in the UI.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the inventory or sales location relevant to the line item.

This field is a relationship field.

**Relationship Name**
Location

**Refers To**
Location

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated identifier for the line item record.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The new sale price per unit after the price change.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of sale price applied post-adjustment (e.g., List Price, Net Price).


Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
PriceDifference

PriceProtectionExecutionId

PriceProtectionTermId

ProductId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Difference between the old and new sale price per unit.

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Links to the parent Price Protection Execution record.

This field is a relationship field.

**Relationship Name**
PriceProtectionExecution

**Relationship Type**
Master-detail

**Refers To**
PriceProtectionExecution (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the Price Protection Term used for evaluating eligibility and calculations.

This field is a relationship field.

**Relationship Name**
PriceProtectionTerm

**Refers To**
PriceProtectionTerm

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the product involved in the price protection claim.


Standard Objects PriceProtectExecLineItem

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Product

**Refers To**
Product2

```
RemainingQuantity

SalePricePerUnit

SalePriceType

Status

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Quantity of product still eligible for claim after partial adjustments.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Original sale price per unit before the price adjustment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of sale price recorded during the original transaction.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Current processing state of the line item.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `New`

**•** `ReadyForClaim` —Ready For Claim

**•** `ReadyForPricing` —Ready For Pricing

**•** `ReadyForSimulation` —Ready For Simulation


### Standard Objects PriceProtectionTerm

**Field** **Details**

```
StatusReason

TransactionDate

TransactionReferenceId

WarningMessage

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional explanation or message associated with the current status.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date when the original sale or transaction occurred.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the transaction record from which this line item originates.

This field is a polymorphic relationship field.

**Relationship Name**
TransactionReference

**Refers To**
PartnerUnsoldInventory

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Descriptive warning associated with this line item, if applicable.

### PriceProtectionTerm

Represents a configuration record that defines the rules, types, and eligible conditions for price protection. This object is available in API
version 63.0 and later.

A PriceProtectionTerm record is referenced during claims processing to calculate supported price and quantity adjustments based on
predefined terms.


Standard Objects PriceProtectionTerm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CalculationReferenceRecordId

IsPayable

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Rebate type that's applicable for the claim amount calculation. This field is a relationship
field.

**Relationship Name**
CalculationReferenceRecord

**Refers To**
ProgramRebateType

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the inventory is eligible for payment or refund after a price protection
adjustment.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the record was last referenced by the current user. Useful for activity
tracking.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PriceProtectionTerm

**Field** **Details**

**Description**

Date and the timestamp when the record was last viewed by the user. Helps in understanding
record engagement.

```
Name

NewSalePriceType

OwnerId

PriceProtectionType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique name for the Price Protection Term. This is typically used as a primary identifier for
UI display or business logic.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the type of new sale price applicable after a price protection scenario. This helps
classify how the adjusted sale price can be handled.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifier for the user or group who owns the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the type of price protection applied.

Possible values are:

**•** `PriceProtection` —Price Protection

**•** `ReversePriceProtection` —Reverse Price Protection


### Standard Objects PrivacyHold

**Field** **Details**

The default value is `PriceProtection` .

```
SalePriceType

SupportedPricePercent

SupportedQuantityPercent

### PrivacyHold

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of sale price before price protection is applied. This helps calculate the
protection delta during claim processing.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of the price that is supported for price protection. Helps calculate
eligible claim amounts.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of quantity that is eligible for price protection. Used to determine
prorated reimbursement.

Represents a Privacy Hold that indicates that a record should be preserved from masking or deletion by Data Management policies in
Privacy Center. This object is available in API version 59.0 and later.

Use Privacy Hold with Data Management policies in Privacy Center. Add a condition to your policy to exclude records with an active
Privacy Hold status from masking or deletion actions.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.


Standard Objects PrivacyHold

Fields

**Field** **Details**

```
EndDate

IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if Privacy Hold is active on the record.

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
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Hold.

**Type**
reference


Standard Objects PrivacyHold

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PrivacyHoldReasonId

ReferenceRecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the associated Privacy Hold Reason.

This field is a relationship field.

**Relationship Name**
PrivacyHoldReason

**Relationship Type**
Lookup

**Refers To**
PrivacyHoldReason

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record marked for the Privacy Hold.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, Lead, User


### Standard Objects PrivacyHoldReason

**Field** **Details**

```
ReferenceRecordType

RegisteredDate

### PrivacyHoldReason

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the record with the Privacy Hold is associated with.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`

**•** `User`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold was added to the record.

Represents the business or legal purpose for why a record has a Privacy Hold. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.

Fields

**Field** **Details**

```
Detail

```

**Type**
string


Standard Objects PrivacyHoldReason

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The details of the Privacy Hold Reason, such as the business or legal purpose for the hold.

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
The name of the Privacy Hold Reason.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects PrivacyJobSession PrivacyJobSession

Represents the status of past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and later.

This object is Read-only.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
CreationDate

CurrentObject

EndTime

FailureLog

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that the policy job is currently processing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job finished executing.

**Type**
textarea

**Properties**
Nillable


Standard Objects PrivacyJobSession

**Field** **Details**

**Description**
The description of why the policy job failed to execute.

```
JobStartType

JobStatus

Name

OptionsProcessingFailed

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the policy job session was started.

Possible values are:

**•** `manual`

**•** `scheduled`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the status of the policy job session.

Possible values are:

**•** `cancelled`

**•** `completed`

**•** `failures`

**•** `inactive`

**•** `running`

**•** `running_next`

**•** `scheduled`

**•** `suspended`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
boolean

**Properties**
Filter


Standard Objects PrivacyJobSession

**Field** **Details**

**Description**
Indicates that the policy job session failed to process the records with the deletion or masking
rules in the policy.

```
OptionsTraversalComplete

OptionsTraversalFailed

OwnerId

PolicyDescription

PolicyName

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session was completed without errors.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session was completed with errors.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with this customer.

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
Filter, Group, Nillable, Sort

**Description**
The description of the policy the job session is associated with.

**Type**
string


Standard Objects PrivacyJobSession

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy the job session is associated with.

```
PolicyType

PrivacyPolicyDefinitionId

PrivacyRtbfRequestId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of policy the job session is associated with.

Possible values are:

**•** `datamanagement` —Data Management.

**•** `datamask` —This policy type is reserved for future use.

**•** `rtbf`  - Right to Be Forgotten.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the policy the job session is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyPolicyDefinition

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Right to Be Forgotten request the policy job is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyRtbfRequest


### Standard Objects PrivacyObjectSession

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PrivacyRTBFRequest

```
ScheduledTime

SerializedPolicy

StartTime

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session is scheduled to run.

**Type**
textarea

**Properties**
Nillable

**Description**
The serial ID of a snapshot of the policy the job session is for. A snapshot of the policy is taken
to maintain consistent metadata for the policy the job is for, in case changes are made to
the policy while the job is executing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session started executing.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyJobSessionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyJobSessionShare on page 67**
Sharing is available for the object.

### PrivacyObjectSession

Represents the status of each object being processed in past, ongoing, and scheduled policy jobs in Privacy Center. This object is available
in API version 59.0 and later.


Standard Objects PrivacyObjectSession

See the status of each object as a policy executes. For example, if a Data Management policy includes an Account object and a Contact
object, then a PrivacyObjectSession record is created for each object.

Each object in a policy has five potential queues to enter. The first queue captures and stores records targeted by the policy filters. If the
first queue run fails to capture every record, then the object goes through three retry attempts to capture the remaining records. The
fifth queue stores the record IDs of any records that weren’t captured in any of the four attempts.

This object is Read-only.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
CurrentEntity

Name

ObjectFailureLog

ObjectStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object in the policy.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
textarea

**Properties**
Nillable

**Description**
This field is reserved for later use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects PrivacyObjectSession

**Field** **Details**

**Description**
The policy execution status for the object.

Possible values are:

**•** `processing_completed`

**•** `processing_failed`

**•** `processing_ongoing`

**•** `processing_pending`

**•** `traversal_completed`

**•** `traversal_failed`

**•** `traversal_ongoing`

```
OwnerId

PolicyNode

Position

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with the customer that the policy was executed
for.

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
Filter, Group, Nillable, Sort

**Description**
The ID of the object in the serialized policy. This field associates the object session in the
policy execution with the coordinating object in the Privacy Center policy.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a record’s position in the batch queue for the object being processed.


Standard Objects PrivacyObjectSession

**Field** **Details**

```
PrivacyJobSessionObjectId

ProcessType

ProcessedFailures

ProcessedSuccesses

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyJobSessionObject

**Relationship Type**
Lookup

**Refers To**
PrivacyJobSession

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of action being executed on the object in the policy.

Possible values are:

**•** `delete`

**•** `mask`

**•** `retry_delete`

**•** `retry_mask`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution failed to process.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution successfully processed.


Standard Objects PrivacyObjectSession

**Field** **Details**

```
ProcessedTotal

Processor

Queue

QueueLength

RecordsAffected

Retry

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records processed in the policy job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the deletion, masking, or traversal processor executing the policy job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for later use.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records in the queue to be processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects PrivacyRequest

**Field** **Details**

**Description**
The queue number of the retry session after a failed policy execution attempt. Each attempt
to retry the policy execution is put into a retry queue.

```
TraversalEndTime

TraversalStartTime

UniqueConstraint

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end time of the record-capturing phase for the object session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start time of the record-capturing phase for the object session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For internal use only.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyObjectSessionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyObjectSessionShare on page 67**
Sharing is available for the object.

### PrivacyRequest

See details and monitor the status of Data Subject Access Requests made in Privacy Center. This object is available in API version 54.0
and later.


Standard Objects PrivacyRequest

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

Fields

**Field** **Details**

```
CompletedDateTime

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was completed.

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
The name of the Privacy Request.

**Type**
reference


Standard Objects PrivacyRequest

**Field** **Details**

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

```
RelatedRecord

StartedDateTime

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Subject Access Request (DSAR) or Right to Be Forgotten request (RTBF) record
related to the request.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Approved`

**•** `Cancelled`

**•** `Completed`

**•** `Created`

**•** `In Progress`

**•** `Rejected`


Standard Objects PrivacyRequest

**Field** **Details**

```
TargetRecord

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record that is listed in the request.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the type of request that was made.

Possible values are:

**•** `DSAR`

**•** `GlobalOptOut`

**•** `RTBF`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRequestFeed on page 55**
Feed tracking is available for the object.

**PrivacyRequestHistory on page 63**
History is available for tracked fields of the object.

**PrivacyRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyRequestShare on page 67**
Sharing is available for the object.

Usage

In API version 66.0 and later, users can click **New Privacy Request** to create privacy requests directly from the Privacy Requests page.
This action supports Right to Be Forgotten (RTBF) request types. The New Privacy Request button uses a custom dialog based on search
criteria defined in Setup. The standard New button uses the default record creation dialog. To streamline the user interface and avoid
redundancy, hide the standard New button.


### Standard Objects PrivacyRTBFRequest PrivacyRTBFRequest

Represents a Right to Be Forgotten Request made in Privacy Center. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
Description

JobRecord

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the customer’s Right to Be Forgotten request.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID that is processed by the Right to Be Forgotten request.

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


Standard Objects PrivacyRTBFRequest

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

PolicyNameId

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Right to Be Forgotten request.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

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
The name of the Right to Be Forgotten policy applied to this request.

This field is a relationship field.

**Relationship Name**
PolicyName

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
picklist


### Standard Objects PrivacySessionRecordFailure

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Cancelled`

**•** `Complete`

**•** `Error`

**•** `Pending`

**•** `Scheduled`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRTBFRequestHistory on page 63**
History is available for tracked fields of the object.

**PrivacyRTBFRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyRTBFRequestShare on page 67**
Sharing is available for the object.

### PrivacySessionRecordFailure

Represents error messages encountered during policy job executions in Privacy Center. This object is available in API version 59.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.


Standard Objects PrivacySessionRecordFailure

Fields

**Field** **Details**

```
ErrorMessage

ErrorType

Name

OwnerId

PrivacyObjectSessionId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the error encountered during the policy job execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of error encountered during the policy job execution.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with the customer that the policy was executed
for.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


### Standard Objects Problem

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the object in the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyObjectSession

**Relationship Type**
Lookup

**Refers To**
PrivacyObjectSession

```
RecordIdNumber

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that failed to be processed by the policy job.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacySessionRecordFailureOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacySessionRecordFailureShare on page 67**
Sharing is available for the object.

### Problem Problems represent the root cause data of one or more incidents. This object contains all the details of a problem, documenting the

history of the problem from detection to closure. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Problem

Fields

**Field** **Details**

```
Category

Description

Impact

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The type of problem. Administrators set field values.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The problem's impact.

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
The date and time (in UTC) when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Problem

**Field** **Details**

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view.
( `LastReferencedDate` ) but not viewed it.

```
OwnerId

ParentProblemId

Priority

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This is a polymorphic relationship field that represents the user or group assigned to resolve
the problem.

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
The ID of a problem above one or more related problems in a problem hierarchy.

This is a relationship field.

**Relationship Name**
ParentProblem

**Relationship Type**
Lookup

**Refers To**
Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the problem.

Possible values are:

**•** `Critical`


Standard Objects Problem

**Field** **Details**

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
PriorityOverrideReason

ProblemNumber

ResolutionDateTime

ResolutionSummary

ResolvedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the priority should be changed or edited.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated problem number.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the problem was resolved.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the steps needed to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who resolved the problem.

This is a relationship field.


Standard Objects Problem

**Field** **Details**

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

```
RootCauseSummary

Status

StatusCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem resolution or root cause. This field can store up to 32 KB of data,
but only the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages customers wants to track. This will be a dependent picklist.

Possible values are:

**•** `Closed`

**•** `Fix in Progress`

**•** `Known Error`

**•** `New`

**•** `Open`

**•** `Pending Change`

**•** `Resolved`

**•** `Root Cause Analysis`

**•** `Work In Progress`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the problem.

Possible values are:


Standard Objects Problem

**Field** **Details**

**•** `Closed`

**•** `FixInProgress`

**•** `KnownError`

**•** `New`

**•** `Open`

**•** `PendingChange`

**•** `Resolved`

**•** `RootCauseAnalysis`

**•** `WorkInProgress`

The default value is 'New'.

```
SubCategory

Subject

Urgency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of problem. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the problem.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long a resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


### Standard Objects ProblemIncident ProblemIncident

Represents a junction object that relates a Problem to an Incident. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IssueId

Name

RelatedEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

**Relationship Name**
Issue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident that's related to the problem.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object type of the related entity.

Possible values are:

**•** `Incident`


Standard Objects ProblemIncident

**Field** **Details**

**•** `Problem`

```
RelatedIssueId

RelationshipType

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

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
Shows how the Problem and Incident records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Similar`

The default value is `Caused By` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemIncidentChangeEvent on page 68**
Change events are available for the object.

**ProblemIncidentFeed on page 55**
Feed tracking is available for the object.

**ProblemIncidentHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ProblemRelatedItem ProblemRelatedItem

Represents a junction object that relates a Problem to an Asset. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

Comment

ImpactLevel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the Problem.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the problem.

Possible values are:

**•** `High`


Standard Objects ProblemRelatedItem

**Field** **Details**

**•** `Low`

**•** `Medium`

The default value is `High` .

```
ImpactType

Name

ProblemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The effect of the problem-related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the problem-related item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Problem ID that’s related to the Asset.

This field is a relationship field.

**Relationship Name**
Problem

**Relationship Type**
Lookup

**Refers To**
Problem


### Standard Objects ProcessDefinition

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemRelatedItemChangeEvent on page 68**
Change events are available for the object.

**ProblemRelatedItemFeed on page 55**
Feed tracking is available for the object.

**ProblemRelatedItemHistory on page 63**
History is available for tracked fields of the object.

### ProcessDefinition

Represents the definition of a single approval process.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Portal and communities users with the Customer Community Plus and Partner Community licenses can access this object. All users in
org with approvals enabled have read access to ProcessDefinition.

Fields

**Field** **Details**

```
Description

DeveloperName

LockType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description of this process, with a maximum of 3,000 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique process name, used internally.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects ProcessDefinition

**Field** **Details**

**Description**
The type of lock applied to the record being approved. When a record is in the approval
process, it’s always locked, and only an administrator can edit it. However, the currently
assigned approver can also be allowed to edit the record.

**•** Total

**•** Admin

**•** Owner

**•** Workitem

**•** Node

**•** none

```
Name

State

TableEnumOrId

Type

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The external name of the process; the name seen by users.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current state of this process.

**•** Active

**•** Inactive

**•** Obsolete

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the object associated with the approval process, such as Account or Contact.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this process.


### Standard Objects ProcessException

**Field** **Details**

**•** Approval Process—Used to control the action taken for a record.

**•** State-based Process—Used internally to track various control processes, such as for
developing Salesforce Knowledge articles.

Usage

Use this object to read the description of an approval process. The definition is read-only.

### ProcessException

Represents a business exception, such as a processing failure on an order summary. A separate process is required to resolve the failure
that caused the process exception before processing can continue. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AttachedToId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the object associated with the ProcessException.

This field is a polymorphic relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
AsyncOpSyndicationFeedFile, AsyncOperationTracker

CreditMemo, FulfillmentOrder, Invoice, Order, OrderItem, OrderItemSummary,
OrderPaymentSummary, OrderSummary, Payment, PaymentAuthorization, Refund,
ReturnOrder

**Type**
reference


Standard Objects ProcessException

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the case associated with the ProcessException.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
Category

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ProcessingException type. You can customize the category picklist to represent your business
processes.

Possible values are:

**•** `Fulfillment`

**•** `Invoicing`

**•** `Order Activation`

**•** `Order Approval`

**•** `Order To Asset`

**•** `Order Item Summary To Asset`

**•** `Order To Billing Schedule`

**•** `Payment`

The default value is `Order Activation` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the ProcessException.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro


Standard Objects ProcessException

**Field** **Details**

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
Description

ExternalReference

FlowOrchestrationInstRelaObj

GroupById

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Detailed description of the ProcessException.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of external entities associated with the ProcessException.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The flow orchestration instance related object associated with this record.

This field is a relationship field.

**Relationship Name**
FlowOrchInstRelaObj

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstRelaObj

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID used in the entity to group exceptions, such as the Async Operation Tracker.

This field is a polymorphic relationship field.

**Relationship Name**
GroupBy


Standard Objects ProcessException

**Field** **Details**

**Refers To**
AsyncOperationTracker

```
LastReferencedDate

LastViewedDate

Message

OrderSummaryId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. A null value can mean that this
record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Short description of the ProcessException

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the OrderSummary associated with the ProcessException. The ProcessException
component is displayed on this OrderSummary.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary


Standard Objects ProcessException

**Field** **Details**

```
OwnerId

Priority

ProcessExceptionNumber

Severity

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this ProcessException. Default value is the User who
created the record.

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
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Resolution priority for the ProcessException. You can customize the priority picklist to
represent your business processes.

Possible values are:

**•** `High`

**•** `Low`

The default value is `Low` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the ProcessException, formatted as PE-(00000000).

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ProcessException

**Field** **Details**

**Description**
Severity of the ProcessException. Each severity value corresponds to one severity category.
You can customize the severity picklist to represent your business processes. If you customize
the severity picklist, include at least one severity value for each severity category.

Possible values are:

**•** `High`

**•** `Low`

The default value is `High` .

```
SeverityCategory

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Severity category of the ProcessException. Each severity category corresponds to one or
more severity values. The severity category is used to show the severity icon in the
ProcessException list view.

Possible values are:

**•** `HIGH`

**•** `LOW`

**•** `MEDIUM`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the ProcessException. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes.
If you customize the status picklist, include at least one status value for each status category.

Possible values are:

**•** `Ignored` (Inactive)

**•** `New` (Active)

**•** `Paused` (Inactive)

**•** `Resolved` (Resolved)

**•** `Triaged` (Active)

**•** `Voided` (Inactive)

The default value is `New` .


### Standard Objects ProcessFlowMigration

**Field** **Details**

```
StatusCategory

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the ProcessException. Each status category corresponds to one or more
statuses.

Possible values are:

**•** `ACTIVE`

**•** `INACTIVE`

**•** `RESOLVED`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProcessExceptionChangeEvent (API version 62.0)**
Change events are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.

### ProcessFlowMigration

Represents a process's migrated criteria and the resulting migrated flow. This object is available in API version 58.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ProcessFlowMigration

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.

```
Language

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Lanaguage of the `MasterLabel` .

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

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh

**•** `da` —Danish


Standard Objects ProcessFlowMigration

**Field** **Details**

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


Standard Objects ProcessFlowMigration

**Field** **Details**

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

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ji` —Yiddish

**•** `ka` —Georgian

**•** `kk` —Kazakh

**•** `kl` —Greenlandic

**•** `km` —Khmer


Standard Objects ProcessFlowMigration

**Field** **Details**

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

**•** `ru_UA` —Russian (Ukraine)

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sm` —Samoan

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)


Standard Objects ProcessFlowMigration

**Field** **Details**

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
MasterLabel

MigratedCriteriaLabel

MigratedCriteriaName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the ProcessFlowMigration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the criteria that was migrated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the criteria that was migrated.


### Standard Objects ProcessInstance

**Field** **Details**

```
NamespacePrefix

### ProcessInstance

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the package containing the process flow migration object.

Represents an instance of a single, end-to-end approval process. Use this and the node, step, and workitem process instance objects to
create approval history reports.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

For approval process instances that were completed before the Summer '14 rollout, all Process Instance fields are automatically populated,
with one exception: `CompletedDate` is never populated for approval process instances that were completed before January 1, 2013.
For approval process instances that were pending during the Summer '14 rollout, all ProcessInstance fields are automatically populated,
with two exceptions: `CompletedDate` and `LastActorId` are populated only after the approval process instance is complete.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompletedDate

ElapsedTimeInDays

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of the approval process. The `ElapsedTimeDay,`
`ElapsedTimeHours`, and `ElapsedTimeMinutes` field values are calculated using
`CompletedDate` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ProcessInstance

**Field** **Details**

**Description**
The total elapsed time in days between when the approval process instance was started and
now.

```
ElapsedTimeInHours

ElapsedTimeInMinutes

LastActorId

ProcessDefinitionId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in hours between when the approval process instance was started
and now.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in minutes between when the approval process instance was started
and now.

**Type**
reference

**Properties**
Group, Filter, Nillable, Sort

**Description**
The last actor that approved, rejected, or recalled the process.

This is a relationship field.

**Relationship Name**
LastActor

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Group, Filter, Sort

**Description**
The ID of this approval process instance.

This is a relationship field.


Standard Objects ProcessInstance

**Field** **Details**

**Relationship Name**
ProcessDefinition

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition

```
Status

SubmittedById

TargetObjectId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of this approval process instance.

Possible values are:

**•** `Approved`

**•** `Fault`

**•** `Held`

**•** `NoResponse`

**•** `Pending`

**•** `Reassigned`

**•** `Rejected`

**•** `Removed`

**•** `Started`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who submitted the approval process.

This is a relationship field.

**Relationship Name**
SubmittedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


Standard Objects ProcessInstance

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval process instance.

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, Award, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, Campaign, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CodeSetBundle, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConsumptionRate, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, DataStream, DataUseLegalBasis,
DataUsePurpose, DelegatedAccount, DigitalSignature, DocumentChecklistItem,
DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType,
EnrollmentEligibilityCriteria, ExternalEventMapping, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, IdentityDocument,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, LocationTrustMeasure,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingEndUser,
MessagingSession, MktCalculatedInsight, Opportunity, Order, OrgMetricScanResult,
OrgMetricScanSummary, OtherComponentTask, PartyConsent, PaymentAuthAdjustment,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, ProcessException, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction,
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, Quote, ReceivedDocument,


### Standard Objects ProcessInstanceHistory

**Field** **Details**

ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, ServiceAppointment, ServiceResource,
ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SharingRecordCollection, SharingRecordCollectionItem, SharingRecordCollectionMember,
Shift, Shipment, ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel,
UnitOfMeasure, UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording,
Visit, VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember

Usage

Use this object to query or retrieve an approval process.

The following SOQL query returns details for all the ProcessInstanceStep records related to individual ProcessInstance records. The nested
query references `Steps`, which is the child `relationshipName` for ProcessInstanceStep in the ProcessInstance object.

```
   SELECT Id, (SELECT Id, StepStatus, Comments FROM Steps)

   FROM ProcessInstance

```

The following SOQL query returns details for all the ProcessInstanceWorkItem records related to individual ProcessInstance records. The
nested query references `Workitems`, which is the child `relationshipName` for ProcessInstanceWorkItem in the ProcessInstance
object.

```
   SELECT Id, (SELECT Id, ActorId, ProcessInstanceId FROM Workitems)

   FROM ProcessInstance

### ProcessInstanceHistory can help provide a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects.

```

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

### **ProcessInstanceHistory**

History is available for tracked fields of the object.

**ProcessInstanceChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

### ProcessInstanceHistory

ProcessInstanceStep

ProcessInstanceWorkitem

### ProcessInstanceHistory

This read-only object shows all steps and pending approval requests associated with an approval process (ProcessInstance).


Standard Objects ProcessInstanceHistory

Supported Calls

```
   describeSObjects()

```

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
ActorId

Comments

ElapsedTimeInDays

ElapsedTimeInHours

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is assigned to this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Comments for a ProcessInstanceStep . This field doesn't apply to ProcessInstanceWorkitem
records.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days between when the approval process instance was started and when
it was completed.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ProcessInstanceHistory

**Field** **Details**

**Description**
The total time in hours between when the approval process instance was started and when
it was completed.

```
ElapsedTimeInMinutes

IsPending

OriginalActorId

ProcessInstanceId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes between when the approval process instance was started and
when it was completed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the ProcessInstance is pending ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance.

This is a relationship field.


Standard Objects ProcessInstanceHistory

**Field** **Details**

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

```
ProcessNodeId

RemindersSent

StepStatus

TargetObjectId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of reminders that have been sent. Default is 0 (zero).

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the ProcessInstanceStep.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object being approved.


Standard Objects ProcessInstanceHistory

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, Award, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, Campaign, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CodeSetBundle, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConsumptionRate, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, DataStream, DataUseLegalBasis,
DataUsePurpose, DelegatedAccount, DigitalSignature, DocumentChecklistItem,
DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType,
EnrollmentEligibilityCriteria, ExternalEventMapping, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, IdentityDocument,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, LocationTrustMeasure,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingEndUser,
MessagingSession, MktCalculatedInsight, Opportunity, Order, OrgMetricScanResult,
OrgMetricScanSummary, OtherComponentTask, PartyConsent, PaymentAuthAdjustment,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, ProcessException, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction,
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, ReceivedDocument, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType, SharingRecordCollection,
SharingRecordCollectionItem, SharingRecordCollectionMember, Shift, Shipment,
ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel, UnitOfMeasure,


### Standard Objects ProcessInstanceNode

**Field** **Details**

UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording, Visit,
VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

Usage

This object helps you replicate the related list functionality of the Salesforce user interface for approval processes. Use ProcessInstanceHistory
for a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects. You can’t query ProcessInstanceHistory.
Instead, you can query ProcessInstanceHistory by including it in a nested query on the parent ProcessInstance object. For example, this
SOQL query returns all the ProcessInstanceHistory records related to individual ProcessInstance records. The nested query references
`StepsAndWorkitems`, which is the child `relationshipName` for ProcessInstanceHistory in the ProcessInstance object.

```
   SELECT Id, (SELECT Id, StepStatus, Comments FROM StepsAndWorkitems)

     FROM ProcessInstance

```

This object respects field-level security on the parent object.

SEE ALSO:

### ProcessInstance

ProcessInstanceStep

ProcessInstanceWorkitem

### ProcessInstanceNode

Represents a step in an instance of an approval process. Compare to ProcessNode, which describes the step in a process definition. Use
this object to retrieve approval history.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceNode fields are never populated for approval process instances that were completed before the Summer '14 rollout. For

approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceNode fields are populated only after
the approval process instance is next acted upon after the Summer '14 rollout.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ProcessInstanceNode

Fields

**Field** **Details**

```
CompletedDate

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

LastActorId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of this step in the approval process. The `ElapsedTimeDay,`
`ElapsedTimeHours`, and `ElapsedTimeMinutes` field values are calculated using
`CompletedDate` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this step was started.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last actor that approved or rejected this step.

This is a relationship field.

**Relationship Name**
LastActor


Standard Objects ProcessInstanceNode

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
NodeStatus

ProcessInstanceId

ProcessNodeId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval instance, for example Started, Pending, or Approved.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval process this step is part of.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The identifier for this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode


### Standard Objects ProcessInstanceStep

**Field** **Details**

```
ProcessNodeName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of this step.

The contents of this field can be publicly viewed.

### ProcessInstanceStep

Represents one work item in an approval process (ProcessInstance).

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceStep fields are never populated for approval process instances that were completed before the Summer '14 rollout. For

approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceStep fields are populated only after the
approval process instance is next acted upon after the Summer '14 rollout.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActorId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who’s assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ProcessInstanceStep

**Field** **Details**

```
Comments

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

OriginalActorId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Limit: 4,000 bytes.

The contents of this field can be publicly viewed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this step was started.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup


Standard Objects ProcessInstanceStep

**Field** **Details**

**Refers To**
Group, User

```
ProcessInstanceId

StepNodeId

StepStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance that this approval step belongs to.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the node currently assigned to this approval step.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval step.

**•** Approved

**•** Fault

**•** Held

**•** NoResponse

**•** Pending

**•** Reassigned

**•** Rejected

**•** Removed

**•** Started


### Standard Objects ProcessInstanceWorkitem

**Field** **Details**

If the approval step requires unanimous approval and one approver rejects the request, the
value of this field for the other approvers changes to NoResponse. Likewise, if approval is
based on the first response and an approver responds, the value of this field for the other
approvers changes to NoResponse.

Usage

Query or retrieve a new step in an approval process (ProcessInstance).

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ProcessInstanceStepChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

### ProcessInstance

ProcessInstanceHistory

### ProcessInstanceWorkitem ProcessInstanceWorkitem

Represents a user’s pending approval request.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceWorkitem fields are never populated for approval process instances that were completed before the Summer ’14 rollout.

For approval process instances that were pending during the Summer ’14 rollout, all ProcessInstanceWorkitem fields are populated after
the approval process instance is next acted upon after the Summer ’14 rollout, with three exceptions. The `ElapsedTimeInDays`,
`ElapsedTimeInHours`, and `ElapsedTimeInMinutes` fields are never populated in ProcessInstanceWorkitem records for
which equivalent ProcessInstanceStep records were created before the Summer ’14 rollout.

For all other ProcessInstanceWorkitem records, these three fields are populated after the approval process instance is next acted upon
after the Summer ’14 rollout.

ProcessInstanceHistory combines fields from ProcessInstanceStep and ProcessInstanceWorkitem. As a result, incorrect elapsed times of
0 can appear in ProcessInstanceHistory records because the elapsed time fields were never populated in the related
### ProcessInstanceWorkitem record.

Note: Knowledge articles use ProcessInstanceWorkitem records to track the article history, so ProcessInstanceWorkitems records
associated with Knowledge articles can’t be deleted.


Standard Objects ProcessInstanceWorkitem

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
ActorId

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user responsible for approving an approval request.

This field is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this approval request was started.


Standard Objects ProcessInstanceWorkitem

**Field** **Details**

```
 OriginalActorId

 ProcessInstanceId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user originally assigned this approval request.

This field is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the ProcessInstance associated with this approval request.

This field is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

Use this object to manage a pending approval request for a user.

SEE ALSO:

ProcessInstance

ProcessInstanceHistory

ProcessInstanceStep


### Standard Objects ProcessNode ProcessNode

Describes a step in a process definition. Compare to ProcessInstanceNode, which describes a step in a running process. This object is
available in API version 31.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Description

DeveloperName

Name

ProcessDefinitionId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description of this node, no longer than 3,000 bytes.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The external name of the node that’s seen by users.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique node name.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval instance.

A relationship field.

**Relationship Name**
ProcessDefinition


### Standard Objects ProducerCommission

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition

Usage

Use this object to get details about the process node or the process definition that it's associated with.

### ProducerCommission

Represents a producer's commission for an insurance policy. The commission can be calculated from the commissionable transactions
or can be populated from an external system. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommissionableAmount

CommissionAmount

CommissionScheduleId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount on which the commission is applied. This can be a transaction amount or a
portion of the premium.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The calculated commission amount for the insurance policy transaction.

**Type**
reference


Standard Objects ProducerCommission

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
CommissionSchedule

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule

```
InsurancePolicyAssetId

InsurancePolicyCoverageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insured item for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyAsset

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyAsset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy coverage for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyCoverage

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyCoverage


Standard Objects ProducerCommission

**Field** **Details**

```
InsurancePolicyId

InsurancePolicyTransactionId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insurance policy for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicy

**Relationship Type**
Lookup

**Refers To**
InsurancePolicy

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The transaction for which the commission record was created.

This is a relationship field.

**Relationship Name**
InsurancePolicyTransaction

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyTransaction

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


Standard Objects ProducerCommission

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

```
MaxCommissionAmount

MinCommissionAmount

Name

OwnerId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the producer commission.

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


Standard Objects ProducerCommission

**Field** **Details**

```
ParentProducerCommissionId

PaymentDatetime

ProcessingProducerId

ProducerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The original commission record that was adjusted or modified.

This is a relationship field.

**Relationship Name**
ParentProducerCommission

**Relationship Type**
Lookup

**Refers To**
ProducerCommission

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the commission was paid.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer who performed the commissionable event.

This is a relationship field.

**Relationship Name**
ProcessingProducer

**Relationship Type**
Lookup

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.


Standard Objects ProducerCommission

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Producer

```
ProducerProductionCode

SourceSystem

SourceSystemIdentifier

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The production code for the producer who performs the commissionable event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The system from which the producer commission record was sourced.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the producer commission record in the source system. This field is unique within
your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the commission payment.

Possible values are:

**•** `Disputed`

**•** `Paid`

**•** `Pending`

**•** `Reversed`


### Standard Objects Product2

**Field** **Details**

```
Type

### Product2

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of commission paid to a producer, account, or contact for a commissionable
transaction.

Possible values are:

**•** `Advance`

**•** `Bonus`

**•** `Chargeback`

**•** `Commission`

**•** `Contingent Commission`

Represents a product that your company sells.

This object has several fields that are used only for quantity and revenue schedules (for example, annuities). Schedules are available only
for orgs that have enabled the products and schedules features. If these features aren’t enabled, the schedule fields don’t appear, and
you can’t query, create, or update the fields.

Note: As of API version 8.0, the Product object is no longer available. Requests that contain Product are refused, and responses
don’t contain the Product object. Use the Products2 object instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ConfigureDuringSale and IsSoldOnlyWithOtherProds fields are available in version 58.0 and later when Industry Automotive or
Subscription Management is enabled.

Fields

**Field** **Details**

```
BillingPolicyId

```

**Type**
reference


Standard Objects Product2

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related billing policy. This field is available when Subscription Management is
enabled. This field is available in API version 55.0 and later.

This field is a relationship field.

**Relationship Name**
BillingPolicy

**Relationship Type**
Lookup

**Refers To**
BillingPolicy

```
CanUseQuantitySchedule

CanUseRevenueSchedule

ConnectionReceivedId

ConnectionSentId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the product can have a quantity schedule ( `true` ) or not ( `false` ). Label
is **Quantity Scheduling Enabled** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the product can have a revenue schedule ( `true` ) or not ( `false` ). Label
is **Revenue Scheduling Enabled** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your org. This field is
available when Salesforce to Salesforce is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Product2

**Field** **Details**

**Description**
ID of the PartnerNetworkConnection that this record is shared with. This field is available
Salesforce to Salesforce is enabled. In API version 16.0 and later, this value is `null` . Use
PartnerNetworkRecordConnection object to forward records to connections.

```
ConfigureDuringSale

CurrencyIsoCode

Description

DisplayUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether a user can edit a configuration when creating a bundle order or quote.

This field is available in API version 58.0 and later.

This field is available when Industries Automotive or Subscription Management is enabled.

Possible values are:

**•** `Allowed`  - Changes are allowed while adding line items to a bundle; for example,
when adding products or editing quantity.

**•** `NotAllowed` —Changes aren’t allowed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A text description of this record. Label is **Product Description** .

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL leading to a specific version of a record in the linked external data source.


Standard Objects Product2

**Field** **Details**

```
ExternalDataSourceId

ExternalId

Family

IsActive

IsArchived

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the related external data source.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of a record in the linked external data source. For example, _`ID #123`_ .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the product family associated with this record. Product families are configured as
picklists in the user interface. To obtain a list of valid values, call `describeSObjects()`
and process the result for the values associated with the `Family` field. Label is **Product**
**Family** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Inactive Product2 records
are hidden in many areas in the user interface. You can change the `IsActive` flag on a
Product2 object as often as necessary. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Describes whether the product is archived. The default value is `false` .

**Type**
boolean


Standard Objects Product2

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
IsSerialized

IsSoldOnlyWithOtherProds

LastReferencedDate

LastViewedDate

Name

```

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates if a product is a serialized product ( `true` ) or not ( `false` ). Label is **Serialized** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Determines whether the product can be sold independently or only as part of a bundle.

This field is available in API version 58.0 and later. This field is available when Industries
Automotive or Subscription Management is enabled. The default value is `false`, which
means that the product can be sold independently.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last interacted with this record, directly or indirectly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string


Standard Objects Product2

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record. Label is **Product Name** .

```
NumberOfQuantityInstallments

NumberOfRevenueInstallments

ProductClass

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the product has a quantity schedule, the number of installments.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the product has a revenue schedule, the number of installments.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
This field is read-only. Its value is determined by the value of the `Type` field and whether
the product is associated with a `ProductAttribute` record. It describes whether a
product is a bundle, set, or simple product, a variation parent, or a product variation. Possible
values are:

**•** `Bundle` —This product is a parent or component in a product bundle.

**•** `Set` —This product is included in a product set.

**•** `Simple` —This product has no variations

**•** `VariationParent` —This product is a variation parent. It’s the base product for one
or more product variations and, though it has its own stock-keeping unit (SKU), isn’t a
sellable entity. Instead, it’s the parent of sellable entities—its variations.

**•** `Variation` —This product is a variation of a parent product. Each variation has its
own SKU.

When the value of `ProductClass` = `VariationParent`, it never changes. The
value of `ProductClass` changes between `Simple` and `Variation` when you attach
or detach a `ProductAttribute` record to the product.

If you attach a `ProductAttribute` record to a product, then the product’s
`ProductClass` value changes to `Variation` . Conversely, when you detach all


Standard Objects Product2

**Field** **Details**

`ProductAttribute` records from a product, the `ProductClass` value changes to
`Simple` .

The default value is `Simple` .

This field is available in API version 50.0 and later. It was introduced to support of B2B and
B2C Commerce implementations.

```
ProductCode

QuantityInstallmentPeriod

QuantityScheduleType

QuantityUnitOfMeasure

RecalculateTotalPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default product code for this record. Your org defines the product’s code-naming pattern.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the product has a quantity schedule, the amount of time covered by the schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the quantity schedule, if the product has one.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unit of the product; for example, kilograms, liters, or cases. This field comes with only one
value, Each, so consider creating your own. The `QuantityUnitOfMeasure` field on
ProductItem inherits this field’s values.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Product2

**Field** **Details**

**Description**
Changes behavior of OpportunityLineItem calculations when a line item has child schedule
rows for the `Quantity` value. When enabled, if the rollup quantity changes, then the
quantity rollup value is multiplied against the sales price to change the total price.

```
RevenueInstallmentPeriod

RevenueScheduleType

StockCheckMethod

StockKeepingUnit

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the product has a revenue schedule, the time period covered by the schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the revenue schedule, if the product has one.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The method for how a product's inventory is checked. Stock checks on parent products are
common when bundles are prepackaged and individual child components can't be sold
separately. Stock checks on child products are common when bundles aren't prepackaged
and must be put together during fulfillment. If bundles aren’t prepackaged, child components
can usually be sold separately.

Possible values are:

**•** `Null` —Check stock on the product SKU.

**•** `DoNotCheck` —The stock shouldn't be check.

**•** `ParentProduct` —If the product is a parent of a bundle, check stock on the parent
product.

**•** `ChildProducts` —If the product is a parent of a bundle, check stock on the child
components.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Product2

**Field** **Details**

**Description**
The SKU for the product. Use in tandem with or instead of the `ProductCode` field. For
example, you can track the manufacturer’s identifying code in the Product Code field and
assign the product a SKU when you resell it.

```
TaxPolicyId

TransferRecordMode

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax policy.

This field is available when Subscription Management is enabled. This field is available in API
version 55.0 and later.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If serialized, indicates when the serial number is recorded. This field is visible based on
field-level security.

The value affects the read-only value of the `Product2TransferMode` field on the
`ProductTransfer` object.

Possible values are:

**•** `SendAndReceive` —The serial number is recorded when sending or receiving.

**•** `ReceiveOnly` —The serial number is recorded when receiving only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects Product2

**Field** **Details**

**Description**
The type of product. This field's value affects the read-only value of the `ProductClass` field
on the `Product2` object. The following mappings define how the `Type` selection updates
the `ProductClass` .

**•** `Base` —When `Type` = `Base`, then `ProductClass` = `VariationParent` .

**•** `Null` —When `Type` = `Null`, then `ProductClass` = `Simple` for standalone
products.

**•** `Null` —When `Type` = `Null`, then `ProductClass` = `Variation` for variation
products.

**•** `Bundle` —When `Type` = `Bundle`, then `ProductClass` = `Bundle` .

**•** `Set` —When `Type` = `Set`, then `ProductClass` = `Set` .

Note:

**•** Revenue Cloud doesn't support products with these specific combinations: `Type`
= `Base` and `ProductClass` = `VariationParent` or `Type` = `Null`
and `ProductClass` = `Variation` .

**•** Values `Null`, `Base`, `Bundle`, and `Set` are available in environments where
both Commerce and Revenue Cloud co-exist.

**•** The Type field can only be updated from Null to Bundle for products with a Simple
ProductClass

This field is available when Revenue Cloud, B2B Commerce, B2C Commerce, or other clouds
with PCM add-on is enabled.

This field is available in API version 50.0 and later.

```
UnitOfMeasureId

```

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


Standard Objects Product2

Schedule Enabled Flags

When enabling the schedules feature, you can decide whether to enable quantity schedules, revenue schedules, or both. In addition,
you can use the API to control quantity and revenue scheduling at the product level via the `CanUseQuantitySchedule` and
`CanUseRevenueSchedule` flags. A value of `true` for either flag indicates that the product and any `OpportunityLineItems`
can have a schedule of that type. These flags can be set when creating or updating Product2 records.

Default Schedule Fields

The remaining schedule fields for this object define default schedules. Default schedule values are used to create an
OpportunityLineItemSchedule when an OpportunityLineItem is created for the Product.

The default schedule fields support the following valid values (all fields are also nillable).

**Field** **Valid Values**

`RevenueScheduleType` Divide, Repeat

`RevenueInstallmentPeriod` Daily, Weekly, Monthly, Quarterly, Yearly

`NumberOfRevenueInstallments` Integer from 1 to 150, inclusive.

`QuantityScheduleType` Divide, Repeat

`QuantityInstallmentPeriod` Daily, Weekly, Monthly, Quarterly, Yearly

`NumberOfQuantityInstallments` Integer from 1 to 150, inclusive

When you attempt to set the schedule fields when creating or updating, the API applies cross-field integrity checks. The integrity
requirements are:

**•** If the schedule type is nil, the installment period and number of installments must be nil.

**•** If the schedule type is set to any value, then the installment period and number of installments must be non-nil.

Any create or update that fails these integrity checks is rejected with an error.

These default schedule fields, `CanUseQuantitySchedule`, and `CanUseRevenueSchedule`, are restricted picklist fields and
are available only if the org has the schedules feature enabled.

Usage

Use this object to define the default product information for your org. This object is associated by reference with Pricebook2 objects via
PricebookEntry objects. The same product can be represented in different price books as price book entries. In fact, the same product
can be represented multiple times (as separate PricebookEntry records) in the same price book with different prices or currencies. A
product can only have one price for a given currency within the same price book. To be used in custom price books, all standard prices
must be added as price book entries to the standard price book.

Note: Note: You can’t create lookup fields to Product2 object, which have **Required** check box set to true or the **Don't Allow**
**Deletion** " radio button selected, as the platform would otherwise interpret this and throw an error that you cannot create a
master-detail relationship to the object.

You can query the products that have been configured for your org. For example, you can allow your client application to obtain valid
product IDs for use when configuring PricebookEntry records via the API. Your client application can perform the following tasks on
PricebookEntry objects:


### Standard Objects Product2DataTranslation

**•** Query

**•** Create for the standard price book or custom price books.

**•** Update

**•** Delete

**•** Change the `IsActive` field when creating or updating records

This object is defined only for those orgs that have products enabled as a feature. If the org doesn’t have the products feature, this object
doesn’t appear in the describeGlobal call, and you can't describe or query this object.

If you try to delete a product via the API but there's an opportunity that uses that product, the delete fails. The workaround is to delete
the product in the user interface, which gives you an option to archive the product.

Note: On opportunities and opportunity products, the workflow rules, validation rules, and Apex triggers fire when an update to
a child opportunity product or schedule causes an update to the parent record. This means your custom application logic is
enforced when there are updates to the parent record, ensuring higher data quality and compliance with your organization’s
business policies.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[Product2ChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[Product2Feed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[Product2History](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[Product2OwnerSharingRule (API version 50.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**
Sharing rules are available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### Product2DataTranslation

Represents the translated values of the data stored within a Product2 record’s fields. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.


Standard Objects Product2DataTranslation

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
Create, Filter, Nillable, Sort, Update

**Description**
The translated value for the Product2 description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent Product2 record is updated after the last translation was filed.

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
The translated value for the Product2 record name. This field is required to translate the text
in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the Product2 associated with the data that is being translated.


### Standard Objects ProductAttribute

Usage

Use this object to translate the data stored in a Product2 record into the different languages supported by Salesforce. If data translation
is enabled for custom fields on the Product2 object, additional Product2DataTranslation fields exist for translating the data contained
within those fields.

You can’t use a custom external id field in an upsert call for a Product2DataTranslation object.

### ProductAttribute

Represents the attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeLayout()`, `describeSObjects()`, `getDeleted`, `getUpdated`, `query()`, `retrieve()`,
`undelete`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

ProductId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ProductAttributeSet

**Field** **Details**

**Description**
The ID of the product that the attribute is associated with. This field is unique within your
organization.

```
Sequence

VariantParentId

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product attributes appear in.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the variation parent record associated with the product attribute.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductAttributeEvent (API version 55.0)**
Change events are available for the object.

### ProductAttributeSet

Represents a group of attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeSObjects()`, `query()`, `retrieve()`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.


Standard Objects ProductAttributeSet

Fields

**Field** **Details**

```
Description

DeveloperName

Language

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Text description of the product attribute set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` Spanish

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


### Standard Objects ProductAttributeSetItem

**Field** **Details**

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the product attribute set.

### ProductAttributeSetItem

Represents a set of attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeSObjects()`, `query()`, `retrieve()`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.

Fields

**Field** **Details**

```
Field

FieldApiName

```

**Type**
reference

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The field’s API name.

**Type**
string

**Properties**
Filter, Sort

**Description**

A derived field whose values comes from CustomFieldDefinition object.


### Standard Objects ProductAttributeSetProduct

**Field** **Details**

```
IsGroupedBy

ProductAttributeSetId

Sequence

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if product variations are grouped by a specific attribute.

This field is available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the product attribute set.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product attributes appear in.

### ProductAttributeSetProduct

Represents the product associated with a set of attributes. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeLayout()`, `describeSObjects()`, `getDeleted`, `getUpdated`, `query()`, `retrieve()`,
`undelete`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.


### Standard Objects ProductCatalog

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

ProductAttributeSetId

ProductId

### ProductCatalog

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The name of the product associated with the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product associated with the product attribute set.

The container that holds a Product Category hierarchy. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProductCatalog

Special Access Rules

You must have the Industries, Retail, or B2B Commerce license.

Fields

**Field** **Details**

```
CatalogCode

CatalogType

CurrencyIsoCode

Description

```

**Type**
text

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique ID associated with the catalog. Maximum size is 80 alphanumeric characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The category of an entry in the catalog.

Possible values are:

**•** `Sales`

**•** `ServiceProcess` —Service Process

The default value is `Sales` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.


Standard Objects ProductCatalog

**Field** **Details**

```
EffectiveEndDate

EffectiveStartDate

LastReferencedDate

LastViewedDate

Name

NumberOfCategories

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.

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
Name of the ProductCatlog record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ProductCategory

**Field** **Details**

**Description**
Number of ProductCategory records assigned to this ProductCatalog record.

```
OwnerId

Status

### ProductCategory

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner.

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
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive

Represents the category that products are organized in.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access product media.


Standard Objects ProductCategory

Fields

**Field** **Details**

```
CatalogId

CurrencyIsoCode

Description

IsNavigational

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the catalog.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
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


Standard Objects ProductCategory

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
Name

NumberOfProducts

ParentCategoryId

SortOrder

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the category.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of products in a category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product’s parent category.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order that the category is displayed in.


### Standard Objects ProductCategoryProduct

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryChangeEvent (API version 55.0)**
Change events are available for the object.

### ProductCategoryProduct

Holds the relation between product and product category to assign products to a category. This object is available in API version 55.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the Industries, Retail, or B2B Commerce license.

Fields

**Field** **Details**

```
Catalog

CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the ProductCatalog ID of the Category.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** EUR—Euro

**•** USD—U.S. Dollar

The default value is `USD` .


Standard Objects ProductCategoryProduct

**Field** **Details**

```
EffectiveEndDate

EffectiveStartDate

IsPrimaryCategory

Name

ProductCategory

Product

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the ProductCategory is the primaryProductCategory for a given product in a
ProductCatalog. The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the ProductCategoryProduct record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the ProductCategory ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ProductCategoryDataTranslation

**Field** **Details**

**Description**
ID of the product.

```
ProductToCategory

Status

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenated Product ID and Category ID.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryProductEvent (API version 55.0)**
Change events are available for the object.

### ProductCategoryDataTranslation

Represents the translated values for the data stored within a ProductCategory record’s fields. This object is available in API version 46.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission


Standard Objects ProductCategoryDataTranslation

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The translated value for the Product Category description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ProductCategory record is updated after the last translation was
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
The translated value for the Product Category name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the category being translated.


### Standard Objects ProductComponentGroup

Usage

Use this object to translate the data stored in a Product Category record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ProductCategory object, additional ProductCategoryDataTranslation fields exist for
translating the data contained within those fields.

### ProductComponentGroup

Represents the logical grouping of associated products in a bundle and the products’ arrangement policy (group cardinality). This object
is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when Industries EPC or Subscription Management is enabled.

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Describes the group items of a product bundle feature. For example, a group’s contents can
be the associated products that accompany a main product in a bundle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a related record or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductComponentGroup

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user indirectly accessed this record ( `LastReferencedDate` ), but
not viewed it.

```
MaxBundleComponents

MinBundleComponents

Name

OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of associated products allowed in a group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum number of associated products allowed in a group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the product component group. Maximum length is 255 characters (of any type).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique identifier of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects ProductConsumed

**Field** **Details**

```
ParentProductId

Sequence

### ProductConsumed

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier associated with the main product record.

This field is a relationship field.

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.

Represents an item from your inventory that was used to complete a work order or work order line item in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Note: To create products consumed, you need Read permission on product items.

Note: To delete or undelete product consumed for non-serialized products, you need Edit, Create, and Read permission on
product consumed. For product consumed records that lookup to serialized products, you need Modify All Data or Modify All
Records permission on product consumed.


Standard Objects ProductConsumed

Fields

**Field Name** **Details**

```
Description

IsConsumed

IsLocked

IsProduct2Serialized

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes and context about the product consumed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that a product consumed has been processed if the Product2 it refers
to has IsSerialized=true selected. The default is false.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates if a product is a serialized product. The default is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime


Standard Objects ProductConsumed

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last viewed.

```
MayEdit

PricebookEntryId

Product2Id

ProductConsumedNumber

ProductItemId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record can be edited or not.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Price book associated with the product consumed. If the work order and the
product item’s associated product are related to the same price book, the Price
Book Entry auto-populates based on the product item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product associated with the product consumed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) Auto-generated number identifying the product consumed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects ProductConsumed

**Field Name** **Details**

**Description**
Product item associated with the product consumed. Creating a product
consumed record subtracts the quantity consumed from the linked product
item’s quantity.

```
ProductName

QuantityConsumed

QuantityUnitOfMeasure

TotalPrice

UnitPrice

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name for the product consumed.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of products consumed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Units of the consumed item; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price paid for the product items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The price per unit of the product consumed.


### Standard Objects ProductDetectedPriceChange

**Field Name** **Details**

```
WorkOrderId

WorkOrderLineItemId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Work order that the product was consumed for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work order line item that the product was consumed for.

When a product is consumed during the completion of a work order, create a product consumed record to track its consumption. You
can add products consumed to work orders or work order line items. Track product consumption at the line item level if you want to
know which products were used for each line item’s tasks.

The way you use products consumed depends on how closely you want to track the state of your inventory in Salesforce. If you want
to track the entire lifecycle of items in your inventory, including their storage, transfer, and consumption, link your products consumed
records to product items. This approach ensures that your inventory numbers auto-update to reflect the consumption of products from
your inventory. If you want to track product consumption only, however, specify a Price Book Entry on each product consumed record
and leave the Product Item field blank.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductConsumedChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductConsumedFeed**

Feed tracking is available for the object.

**ProductConsumedHistory**

History is available for tracked fields of the object.

### ProductDetectedPriceChange

Represents a detected change in price for a product associated with a partner account. This object is available in API version 63.0 and
later.


Standard Objects ProductDetectedPriceChange

A ProductDetectedPriceChange record is automatically created when the system identifies a change in product pricing that can require
price protection evaluation or further processing.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

EffectiveDate

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the partner account for which the price change was detected.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date when the new price becomes effective for the product.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by the current user. Useful for activity
tracking.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductDetectedPriceChange

**Field** **Details**

**Description**
Date and the timestamp the record was last referenced by a user or system process.

```
Name

OwnerId

ProcessingStatus

ProductId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique name or identifier for the price change record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
User or group that owns this record. This is a polymorphic relationship field.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the current processing stage of the price change.

Possible values are:

**•** `Completed`

**•** `Inactive`

**•** `New`

**•** `Processing` —In Progress

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the product for which the price change was detected.


### Standard Objects ProductEntitlementTemplate

**Field** **Details**

This field is a relationship field.

**Relationship Name**
### Product

**Refers To**
Product2

### ProductEntitlementTemplate

Represents predefined terms of customer support (Entitlement) that users can add to products (Product2).

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
EntitlementTemplateId

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the entitlement template. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with the entitlement template. Must be a
valid ID.


### Standard Objects ProductFeaturedProduct

Usage

Use to query and manage entitlement templates.

SEE ALSO:

Entitlement

### ProductFeaturedProduct

Represents the user-defined collection of featured products that are meant to cross-sell or upsell with your product. This object is available
in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
FeatrProdtRelaType

FeaturedProductId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the featured product is related to the product.

Possible values are:

**•** `Complete the Look`

**•** `Featured Products`

**•** `New Arrivals`

**•** `Top Seller`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the featured product that is linked to the product.

This field is a relationship field.


Standard Objects ProductFeaturedProduct

**Field** **Details**

**Relationship Name**
FeaturedProduct

**Refers To**
Product2

```
LastReferencedDate

LastViewedDate

Name

ProductId

Sequence

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the user-defined collection of featured products.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that your company sells.

This field is a relationship field.

**Relationship Name**
Product

**Refers To**
Product2

**Type**
int


### Standard Objects ProductItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the order in which featured products are displayed.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductFeaturedProductChangeEvent**

Change events are available for the object.

### ProductItem

Represents the stock of a particular product at a particular location in field service, such as all bolts stored in your main warehouse.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product item was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductItem

**Field Name** **Details**

**Description**
The date when the product item was last viewed.

```
LocationId

OwnerId

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Location associated with the product item. This usually indicates where the
product item is stored.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product item’s owner.

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
Product associated with the product item, which represents the type of product
in your inventory.

This is a relationship field.


Standard Objects ProductItem

**Field Name** **Details**

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductItemNumber

ProductName

QuantityOnHand

QuantityUnitOfMeasure

SerialNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A name for the product item. Try to select a name that indicates what is being
stored where; for example, Batteries in Warehouse A.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity at the location. If you want to add a serial number, this value must
be 1.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the product item; for example, kilograms or liters. Quantity Unit of Measure
picklist values are inherited from the Quantity Unit of Measure field on products.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ProductItemTransaction

**Field Name** **Details**

**Description**
A unique number for identification purposes. If you want to enter a serial number,
the Quantity on Hand must be 1.

Usage

Each product item is associated with a product and a location in Salesforce. If a product is stored at multiple locations, the product will
be tracked in a different product item for each location.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductItemFeed**

Feed tracking is available for the object.

**ProductItemHistory**

History is available for tracked fields of the object.

**ProductItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductItemShare**

Sharing is available for the object.

### ProductItemTransaction

Represents an action taken on a product item in field service. Product item transactions are auto-generated records that help you track
when a product item is replenished, consumed, or adjusted.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `undelete()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Only users with Modify All Data or Modify All Records permissions can delete this object.


Standard Objects ProductItemTransaction

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

LastViewedDate

ProductItemId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the transaction. The description is blank when the transaction
record is created, but can be updated.

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
value is null, it's possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated product item.

This is a relationship field.

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem


Standard Objects ProductItemTransaction

**Field Name** **Details**

```
ProductItemTransactionNumber

Quantity

RelatedRecordId

TransactionType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item transaction.

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
The quantity of the product item involved in the transaction. If inventory was
consumed, the quantity is negative.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The product consumed or product transfer related to the action. If
the action wasn’t related to consumption or transfer, the related record is blank.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
ProductTransfer, Visit

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The action that the transaction tracks.

**•** Replenished: When a part is stocked at a location. A Replenished transaction
is created when a product item is created.

**•** Consumed: When parts are consumed to complete a work order. A Consumed
transaction is created when a record is added to the Products Consumed
related list on a work order or work order line item.


### Standard Objects ProductMedia

**Field Name** **Details**

**•** Adjusted: When there’s a discrepancy or a change in consumption. An
Adjusted transaction is created when a product item’s Quantity on Hand is
edited, a product consumed is updated or delete, or a product transfer is
deleted.

**•** Transferred: When parts are transferred between locations.

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ProductItemTransactionChangeEvent**

Change events are available for the object.

**ProductItemTransactionFeed**

Feed tracking is available for the object.

**ProductItemTransactionHistory**

History is available for tracked fields of the object.

### ProductMedia

Represents the rich media, including images and attachments, that can be added to products.This object is available in API version 49.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
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

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar


Standard Objects ProductMedia

**Field** **Details**

```
ElectronicMediaGroupId

ElectronicMediaId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media group.

This field is a relationship field.

**Relationship Name**
ElectronicMediaGroup

**Relationship Type**
Lookup

**Refers To**
ElectronicMediaGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media record.

This field is a polymorphic relationship field.

**Relationship Name**
ElectronicMedia

**Relationship Type**
Lookup

**Refers To**
ManagedContent, ManagedContentInfo

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


Standard Objects ProductMedia

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
Name

ProductId

SortOrder

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the media.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that the media is associated with.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product media is displayed in.

**ProductMediaChangeEvent (API version 57.0)**
Change events are available for the object.

**ProductMediaHistory on page 63**
History is available for tracked fields of the object.

**ProductMediaOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects ProgramProduct

**ProductMediaShare on page 67**
Sharing is available for the object.

### ProgramProduct

Represents a junction between Program and Product2. This will hold Product2 values related to a Program. This object is available in
API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
Name

ProductId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ProgramProduct object.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Program.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2


Standard Objects ProgramProduct

**Field** **Details**

```
ProgramId

Status

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Program parent object associated with the record.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup

**Refers To**
Program

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the ProgramProduct object.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Pending For Approval`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ProgramProductChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ProgramProductFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ProgramProductHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ProgramProductOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ProgramProductShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects ProductQuantityRule ProductQuantityRule

Represents the relationship between a quantity rule and a product. This object assigns quantity rules to a product. This object is available
in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ProductQuantityRule object is available only if the B2B Commerce license or Automotive Cloud license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

ProductId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. This field is exposed
in orgs that have multicurrency enabled. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product quantity rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product.

This field is a relationship field.


### Standard Objects ProductRelatedComponent

**Field** **Details**

**Relationship Name**
### Product

**Relationship Type**
Lookup

**Refers To**
Product2

```
PurchaseQuantityRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related purchase quantity rule.

This field is a relationship field.

**Relationship Name**
PurchaseQuantityRule

**Relationship Type**
Lookup

**Refers To**
PurchaseQuantityRule

### ProductRelatedComponent

Represents a product that is included in a product bundle, a set, or a product and an add-on. This object is available in API version 57.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, Industries Automotive, Industries EPC, or Subscription
Management is enabled.

In version 57.0, this object is available when B2B Commerce, B2C Commerce, or Industries Automotive is enabled.


Standard Objects ProductRelatedComponent

Fields

**Details**

```
ChildProductId

ChildProductRole

ChildSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated product.

This field is a relationship field. In a bundle relationship, this item is the child product.

**Relationship Name**
ChildProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The position of the associated product in the relationship.

Possible values are:

**•** `AddOnComponent` —The child product is an add-on to another product. Available
in API version 58.0 and later.

**•** `BundleComponent` —The child product is a component in a bundle.

**•** `SetComponent` —The child product is a component in a set.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the associated product’s sales model.

This field is a relationship field.

**Relationship Name**
ChildSellingModel

**Relationship Type**
Lookup


Standard Objects ProductRelatedComponent

**Details**

**Refers To**
ProductSellingModel

```
DoesBundlePriceIncludeChild

IsComponentRequired

IsDefaultComponent

IsQuantityEditable

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the bundle price includes the associated product’s price.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is required for configuring a bundle or set.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is part of the product bundle or set automatically,
or can be added after the bundle’s or set’s creation.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether you can edit the component’s quantity in the bundle or set after the
bundle’s or set’s creation.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductRelatedComponent

**Details**

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

MaxQuantity

MinQuantity

Name

ParentProductId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user accessed this record or list view ( `LastReferencedDate` )
without viewing it.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed maximum quantity.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed minimum quantity.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the associated product.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the main product around which the bundle or set is built.

This field is a relationship field.


Standard Objects ProductRelatedComponent

**Details**

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

```
ParentProductRole

ParentSellingModelId

ProductComponentGroupId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main product in the relationship.

Possible values are:

**•** `AddOn` —The main product is the add-on parent. Available in API version 58.0 and later.

**•** `Bundle` —The main product is the bundle parent.

**•** `Set`  - The main product is the set parent.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the main product’s sales model.

This field is a relationship field.

**Relationship Name**
ParentSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the group of a product bundle or set. This group contains the
associated products that can be included in the main product’s bundle or set.

This field is a relationship field.


Standard Objects ProductRelatedComponent

**Details**

**Relationship Name**
ProductComponentGroup

**Relationship Type**
Lookup

**Refers To**
ProductComponentGroup

```
ProductRelationshipTypeId

Quantity

QuantityScaleMethod

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier of the record that describes the relationship between the main and
associated products.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit count of the associated product.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The scaling method is used to calculate the associated product’s quantity based on changes
made to the main product’s quantity in a transaction.

Possible values are:

**•** `Constant`  - The associated product’s quantity remains the same in relation to the
main product’s quantity. For example, the main product has a quantity of one and the
associated component has a quantity of one. If you increase the quantity of the main
product to two, the associated component’s quantity remains at one.


### Standard Objects ProductRelationshipType

**Details**

**•** `Proportional`                   - The associated product’s quantity increases or decreases based
on the main product’s quantity. For example, the main component has a quantity of one
and the associated product has a quantity of two. If you increase the quantity of the main
product to two, the associated product’s quantity increases to four.

The default value is `Proportional` .

```
Sequence

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.

### ProductRelationshipType

Defines the relationship between two sales transaction items. For example, defines a relationship between a bundle and a bundle
component. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, or Subscription Management is enabled.

In version 57.0, this object is available when B2B Commerce or B2C Commerce is enabled.

Fields

**Field** **Details**

```
AssociatedProductRoleCat

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The position category that the associated product plays in the relationship.

Possible values are:

**•** `AddOnComponent` —The associated product is an add-on.


Standard Objects ProductRelationshipType

**Field** **Details**

**•** `BundleComponent`                   - The associated product is part of a bundle.

**•** `SetComponent`                   - The associated product is part of a set.

```
LastReferencedDate

LastViewedDate

MainProductRoleCat

Name

```

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
the user might have only accessed this record or list view ( `LastReferencedDate` ), but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The position category that the main product plays in the relationship.

Possible values are:

**•** `AddOn` —The parent of the add-on.

**•** `Bundle` —The bundle parent.

**•** `Set` —The set parent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the relationship between two product items.


### Standard Objects ProductRequest ProductRequest

Represents an order for a part or parts in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Authenticated external users can create and update ProductRequest objects.

Fields

**Field Name** **Details**

```
AccountId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the product request.

This is a relationship field.

**Relationship Name**
Case


Standard Objects ProductRequest

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Case

```
CurrencyIsoCode

Description

DestinationLocationId

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

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text field for details not recorded in the provided fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is delivered.

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
Filter, Nillable, Sort


Standard Objects ProductRequest

**Field Name** **Details**

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

```
LastViewedDate

NeedByDate

OwnerId

ProductRequestNumber

ShipToAddress

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

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
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the shipment.

**Type**
address


Standard Objects ProductRequest

**Field Name** **Details**

**Properties**
Filter, Nillable

**Description**
The address that the product is to be delivered to.

```
ShipToCity

ShipToCountry

ShipToCountryCode

ShipToGeocodeAccuracy

ShipToLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city that the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country that the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase country code conforming to the ISO 3166-1 alpha-2
standard.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The accuracy of the geocode for the shipping address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the product is to be delivered to.


Standard Objects ProductRequest

**Field Name** **Details**

```
ShipToLongitude

ShipToPostalCode

ShipToState

ShipToStateCode

ShipToStreet

ShipmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the state where the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase state code conforming to the ISO 3166-1 alpha-2 standard.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values by default:


Standard Objects ProductRequest

**Field Name** **Details**

**•** None

**•** Rush

**•** Overnight

**•** Next Business Day

**•** Pick Up

```
SourceLocationId

Status

WorkOrderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location the product is shipped from.

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
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder


### Standard Objects ProductRequestLineItem

**Field Name** **Details**

```
WorkOrderLineItemId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order line item that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductRequestChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestFeed**

Feed tracking is available for the object.

**ProductRequestHistory**

History is available for tracked fields of the object.

**ProductRequestOwnerSharingRule**

Sharing rules are available for the object.

**ProductRequestShare**

Sharing is available for the object.

### ProductRequestLineItem

Represents a request for a part in field service. Product request line items are components of product requests.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProductRequestLineItem

Special Access Rules

Field Service must be enabled. You can't use product request line item as a master in an master detail relationship (through a custom
field) with a custom object with data.

Fields

**Field Name** **Details**

```
AccountId

CareProgramEnrolleeId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request line item.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the care program enrollee associated with the product request line
item. This field is available from API version 49.0 and later.

This is a relationship field.

**Relationship Name**
CareProgramEnrollee

**Relationship Type**
Lookup

**Refers To**
CareProgramEnrollee

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The case associated with the product request line item.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
Description

DestinationLocationId

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Details not recorded in the provided fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is delivered.

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
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
NeedByDate

ParentId

Product2Id

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The product request that the line item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The product associated with the product request line item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


Standard Objects ProductRequestLineItem

**Field Name** **Details**

```
ProductRequestLineItemNumber

QuantityRequested

QuantityUnitOfMeasure

ShipToAddress

ShipToCity

ShipToCountry

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) An auto-assigned number that identifies the product request line
item.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The amount requested.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the requested product; for example, grams, liters, or units. The picklist
values can be customized.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The country of the address where the product is needed.

```
ShipToGeocodeAccuracy

ShipToLatitude

ShipToLongitude

ShipToPostalCode

ShipToState

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the product is needed. See
Compound Field Considerations and Limitations for details on geolocation
compound fields. This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. See Compound Field Considerations and Limitations for
details on geolocation compound fields. This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields. This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The state of the address where the product is needed.

```
ShipToStreet

ShipmentType

SourceLocationId

Status

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the product is needed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values, which can be
customized:

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is at the time of the request.

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
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** `Draft`

**•** `Submitted`

**•** `Received`

```
WorkOrderId

WorkOrderLineItemId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order for which the product is needed.

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
The work order line item for which the product is needed.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ProductRequired

**ProductRequestLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestLineItemFeed**

Feed tracking is available for the object.

**ProductRequestLineItemHistory**

History is available for tracked fields of the object.

### ProductRequired

Represents a product that is needed to complete a work order or work order line item in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ProductRequired

**Field Name** **Details**

**Description**
The work order or work order line item that the product is required for.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Visit, WorkOrder, WorkOrderLineItem, WorkType

```
ParentRecordType

Product2Id

ProductName

ProductRequiredNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the parent record is a work order or a work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The required product.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product required.

**Type**
string


Standard Objects ProductRequired

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the product required.

```
QuantityRequired

QuantityUnitOfMeasure

```

Usage

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity required of the product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the required product; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

Required products can be added to work types, work orders, and work order line items to ensure that the assigned service resource
arrives with the right equipment.

Adding required products to work types saves you time and keeps your business processes consistent. Work orders and work order line
items inherit their work type’s required products. For example, if all light bulb replacement jobs require a ladder and a light bulb, add
the ladder and light bulb as required products to your Light Bulb Replacement work type. When it’s time to create a work order for a
customer’s light bulb replacement, applying that work type to the work order adds the required products.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductRequiredChangeEvent**

Change events are available for the object.

**ProductRequiredFeed**

Feed tracking is available for the object.

**ProductRequiredHistory**

History is available for tracked fields of the object.


### Standard Objects ProductSellingModel ProductSellingModel

Defines one method by which a product can be sold; for example, as a one-time sale, an evergreen subscription, or a term-defined
subscription. If the product is sold on subscription, this object defines the subscription’s term. A product can have multiple product
selling models. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Revenue Cloud and Subscription Management. This object is available for Commerce when the Subscriptions
(Beta) permission is enabled.

Fields

**Field** **Details**

```
Name

PricingTerm

PricingTermUnit

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name given to the product selling model.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the duration of the pricing term for a given selling model. Used with
`PricingTermUnit` . For example, if this field’s value is 1 and the `PricingTermUnit`
is `Months`, the subscription is priced monthly.

If the selling model is one-time, this field must be null.

Possible value is:

**•** `1`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProductSellingModel

**Field** **Details**

**Description**
The unit of time used to define the pricing term. Used with `PricingTerm` to define the
length of the pricing term. For example, if this field is `Months` and `PricingTerm` is 1,
the subscription is priced monthly. If the selling model is one-time, this field must be null.

Possible values are:

**•** `Annual` —UI label is `Years`

**•** `Months`

```
SellingModelType

Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the product is sold as a one-time sale, an evergreen subscription, or a
subscription with a defined term.

Possible values are:

**•** `Evergreen` —A subscription without an end date. An evergreen subscription continues
until the customer affirmatively cancels it.

**•** `OneTime` —A product that isn’t sold as a subscription.

**•** `TermDefined` —A subscription with a defined end date. The subscription continues
for a specified time period. When the term ends, the subscription ends.

The default value is `OneTime` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the product selling model.

Possible values are:

**•** `Active` —An active product selling model can’t be deleted, and only the `Name` and
`Status` fields can be modified. An active product selling model can’t be changed back
to draft.

**•** `Draft` —A draft product selling model can be modified and deleted.

**•** `Inactive` —An inactive product selling model can’t be deleted, and only the `Name`
and `Status` fields can be modified. An inactive product selling model can’t be changed
back to draft.

The default value is `Draft` .


### Standard Objects ProductSellingModelOption ProductSellingModelOption

A junction object between Product Selling Model and Product2. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. Some fields require Industries EPC to
be enabled.

Fields

**Field** **Details**

```
Description

DisplayName

Increment

IsDefault

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the product selling model option.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model option to display to customers.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of pricing term units that can be used to increase a subscription term.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ProductSellingModelOption

**Field** **Details**

**Description**
Indcates the default product selling model for a product. Setting a default is optional. A
product can only have one default product selling model.

The default value is `false` . This field requires Industries EPC.

```
LastReferencedDate

LastViewedDate

Maximum

Minimum

Name

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
the user might have only accessed this record or list view but not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of pricing term units for a subscription term.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum number of pricing term units for a subscription term.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model.


Standard Objects ProductSellingModelOption

**Field** **Details**

```
Product2Id

ProductSellingModelId

ProrationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Product2 record associated with this ProductSellingModelOption record.

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
Create, Filter, Group, Sort

**Description**
The ID of the ProductSellingModel record associated with this ProductSellingModelOption
record.

This is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the ProrationPolicy record associated with this ProductSellingModelOption record.

This is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup


### Standard Objects ProductServiceCampaign

**Field** **Details**

**Refers To**
ProrationPolicy

### ProductServiceCampaign

Represents a set of activities to be performed on a product service campaign asset, such as a product recall for safety issues or product
defects. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

EndDate

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the product service campaign.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the product service campaign ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. The UI label is Last Modified Date.


Standard Objects ProductServiceCampaign

**Field** **Details**

```
LastViewedDate

OwnerId

Priority

Product2Id

ProductServiceCampaignName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product service campaign’s owner. By default, the product service campaign owner is
the user who created the product service campaign record. The UI label is Product Service
Campaign Owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the product service campaign.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Product2 associated with this campaign. The UI label is Product.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the product service campaign.


Standard Objects ProductServiceCampaign

**Field** **Details**

```
StartDate

Status

StatusCategory

Type

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date on which the product service campaign starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `New` —Product service campaign created, but there hasn’t yet been any activity.

**•** `In Progress` —Product service campaign has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work couldn’t be completed.

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a _`Waiting for Response`_ value, add it the _`On Hold`_ category.
To learn which processes reference `StatusCategory` [, see How are Status Categories](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ProductServiceCampaignItem

**Field** **Details**

**Description**
The type of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `Modification` —The asset requires an on-site alteration.

**•** `Recall` —The asset must be returned to the manufacturer for modification or upgrade.

**•** `Service` —The asset needs to be serviced.

**•** `Upgrade` —The asset needs updating.

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the product service campaign. A customer uses this field as
a guide when setting work type for work orders for the product service campaign.
`Duration`, `Duration Type`, and required skills.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignFeed**

Feed tracking is available for the object.

**ProductServiceCampaignHistory**

History is available for tracked fields of the object.

**ProductServiceCampaignOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignShare**

Sharing is available for the object.

### ProductServiceCampaignItem

Represents a product service campaign's asset. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ProductServiceCampaignItem

Fields

**Field** **Details**

```
AssetId

LastReferencedDate

LastViewedDate

Product2Id

ProductServiceCampaignId

ProductServiceCampaignItemNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the product service campaign. Must be present if `Product2Id`
is not present.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. Its UI label is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Product2 associated with this campaign. The UI label is Product. Must be present
if `AssetID` is not present.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The item’s parent product service campaign record.

**Type**
string


Standard Objects ProductServiceCampaignItem

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the product service campaign item.

```
Status

StatusCategory

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign item. The picklist includes the following values,
which can be customized:

**•** `New` —Product service campaign item created, but there hasn’t yet been any activity.

**•** `In Progress` —Product service campaign item has begun.

**•** `On Hold` —Product service campaign item is paused.

**•** `Completed` —Product service campaign item is complete.

**•** `Cannot Complete` —Product service campaign item couldn’t be completed.

**•** `Closed` —All product service campaign item and associated activity is complete.

**•** `Canceled` —Product service campaign item is canceled, typically before any work
began.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a _`Waiting for Response`_ value, add it to the _`On Hold`_
category. To learn which processes reference `StatusCategory` [, see How are Status](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignItemFeed**

Feed tracking is available for the object.

**ProductServiceCampaignItemHistory**

History is available for tracked fields of the object.


### Standard Objects ProductServiceCampaignItemStatus

**ProductServiceCampaignItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignItemShare**

Sharing is available for the object.

### ProductServiceCampaignItemStatus

Represents a status for a product service campaign item in field service. This object is available in API version 51.0 and later.

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
Indicates that the status value is the default status on product service campaign items when
`true` . Only one status value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value in the UI.


### Standard Objects ProductServiceCampaignStatus

**Field** **Details**

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
The value’s position in the dropdown list in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has seven values
that are identical to the default Status values.

The Status field on product service campaign items comes with the following values:

**•** New—Product service campaign item created, but there hasn’t been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work couldn’t be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The ProductServiceCampaignItemStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled
By Supplier—creates a product service campaign item status record, and vice versa.

Note: Product service campaign items also come with a Status Category field whose values are identical to the default status
values. If you create custom status values, you must indicate which category it belongs to. For example, if you create a _`Customer`_

_`Absent`_ value, add it to the _`Cannot Complete`_ [category. To learn which processes reference StatusCategory, see How are](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ProductServiceCampaignStatus

Represents a status for a product service campaign in field service. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects ProductServiceCampaignStatus

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

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
Indicates that the status value is the default status on product service campaigns when
`true` . Only one status value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the dropdown list in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has seven values
that are identical to the default Status values.


### Standard Objects ProductTransfer

Usage

The Status field on product service campaigns comes with the following values:

**•** New—Product service campaign created, but there hasn’t been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work couldn’t be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The ProductServiceCampaignStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled
By Supplier—creates a product service campaign status record, and vice versa.

Note: Product service campaigns also come with a Status Category field whose values are identical to the default status values.
If you create custom status values, you must indicate which category it belongs to. For example, if you create a _`Customer`_

_`Absent`_ value, add it to the _`Cannot Complete`_ [category. To learn which processes reference StatusCategory, see How are](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ProductTransfer

Represents the transfer of inventory between locations in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Description

DestinationLocationId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields.

**Type**
reference


Standard Objects ProductTransfer

**Field Name** **Details**

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

```
ExpectedPickupDate

IsReceived

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be picked up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Checkbox identifying that the product was received.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.


Standard Objects ProductTransfer

**Field Name** **Details**

```
OwnerId

Product2Id

Product2TransferRecordMode

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the product transfer.

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
Lookup field for the product associated with the product transfer.

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
If serialized, indicates when the serial number is recorded. It is visible on the
product transfer as a read-only field depending on the field-level security. Possible
values are:

**•** `SendAndReceive` —The serial number is recorded when sending or
receiving.

**•** `ReceiveOnly` —The serial number is recorded when receiving only.

**Relationship Name**
Product2.TransferRecordMode


Standard Objects ProductTransfer

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2.TransferRecordMode

```
ProductRequestId

ProductRequestLineItemId

ProductTransferNumber

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the product request associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product request line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the product transfer.


Standard Objects ProductTransfer

**Field Name** **Details**

```
QuantityReceived

QuantitySent

QuantityUnitOfMeasure

ReceivedById

ReturnOrderId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of product received at the destination location.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of product sent from the source location.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The units of the product, for example grams, liters, or units.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the contact who received the product at the destination location.

This is a polymorphic relationship field.

**Relationship Name**
ReceivedBy

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the product transfer.


Standard Objects ProductTransfer

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

```
ReturnOrderLineItemId

ShipmentExpectedDeliveryDate

ShipmentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the shipment related to the product transfer.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup


Standard Objects ProductTransfer

**Field Name** **Details**

**Refers To**
Shipment

```
ShipmentStatus

ShipmentTrackingNumber

ShipmentTrackingUrl

SourceLocationId

SourceProductItemId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the source location related to the product transfer.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference


### Standard Objects ProductWarrantyTerm

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product item related to the product transfer.

**Relationship Name**
SourceProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductTransferChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductTransferFeed**

Feed tracking is available for the object.

**ProductTransferHistory**

History is available for tracked fields of the object.

**ProductTransferOwnerSharingRule**

Sharing rules are available for the object.

**ProductTransferShare**

Sharing is available for the object.

### ProductWarrantyTerm

Defines the relationship between a product or product family and warranty term. This object is available in API version 50.0 and later.


Standard Objects ProductWarrantyTerm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CoveredProductFamily

CoveredProductId

LastReferencedDate

LastViewedDate

ProductWarrantyTermNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product family that the warranty term applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product that the warranty term applies to.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier for this product warranty term.


### Standard Objects Profile

**Field** **Details**

```
WarrantyTermId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the warranty term.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductWarrantyTermChangeEvent (API version 62.0)**
Change events are available for the object.

### Profile

Represents a profile, which defines a set of permissions to perform different operations. Operations can include creating a custom profile
or querying, adding, updating, or deleting information.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, Customer Portal and Partner Portal users _can’t_ access this object.

To view the following settings, assignments, and permissions for standard and custom objects in a specified profile, the View Setup and
Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Starting in Winter ’21, only users with correct permissions can view profile names other than their own if the Profile Filtering setting is
enabled.


Standard Objects Profile

Important: Profile names are also exposed when users with permissions to perform the following tasks take these actions:

**•** Create a tab or record type with a wizard step that includes the assignment of tabs and record types to profiles.

**•** Configure a login flow where viewing profile lists is required to make flow associations.

**•** Set up delegated admins where looking up profiles is needed to identify assignable profiles.

**•** Administer an org as a delegated customer admin.

**•** Administer an org as a delegated admin to view and assign profiles of the delegated group.

Fields

**Field** **Details**

```
Description

IsSsoEnabled

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the profile.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to this profile can delegate username and password authentication
to a corporate database instead of the user database.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this profile. Available
in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this profile. Available in API version 29.0
and later.


Standard Objects Profile

**Field** **Details**

```
Name

Permissions PermissionName

UserLicenseId

UserType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true`, users assigned to this profile have the named
permission. The number of fields varies depending on the permissions for the org and license
type.

Tip: To get a list of available permissions in SOAP API, use `describeSObjects()` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the UserLicense associated with this profile.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and later,
valid values include:


Standard Objects Profile

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
and access the application through a Customer Portal. Label is **Customer Portal Manager** .

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is **Chatter Free** .

**•** Guest: user whose access is limited because they’re an unauthenticated user without login
credentials. Label is **Guest** .

`UserType` replaces `LicenseType`, which is unavailable as of API version 10.0. In API
versions 8.0 and 9.0 `LicenseType` is still available with the following valid values:

**•** AUL: Lightning Platform user license. Label is **Apex Platform** .

**•** AUL1: Lightning Platform user license with only one user. Label is **Apex Platform One** .

**•** Salesforce: Salesforce user license. Label is **Salesforce** .

**•** PackageManager: user who can create and work with managed packages for AppExchange.
Label is **Package Manager** .

**•** PRM: user whose access is limited because they’re a partner and typically accesses the
application through a partner portal. Label is **Partner** .

**•** CustomerUser: user whose access is limited because they’re an org's customer and accesses
the application through a Customer Portal. Label is **Customer Portal User** .

**•** CustomerManager: user whose access is limited because they’re an org's customer and
accesses the application through a Customer Portal. Label is **Customer Portal Manager** .

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

In API version 53.0 and later, you can’t set the value of `UserType` using Apex.

Usage

Use the Profile object to create custom profiles that start without any permissions enabled except for required permissions for the profile’s
user license. While you can use the Profile Metadata type to deploy profiles, we recommend that you use the Profile SOAP API object
because it allows you to create empty profiles.

You can also query the set of currently configured user profiles in your org. Your client application can use Profile objects to obtain valid
profile IDs for use when querying or modifying users through the API.


### Standard Objects ProfileSkill

In the user interface, profiles can be used to assign user licenses from specific pools (Lightning Platform user license or Salesforce user
license, for example). When users are reassigned to profiles with different license types, the number of available licenses in the old license
type pool increases, one per user assignment updated. Also, the number of available licenses decreases by the same amount in the new
license type pool.

SEE ALSO:

Overview of Salesforce Objects and Fields

PermissionSet

### ProfileSkill

Represents a profile skill, which describes a user’s professional knowledge. This is a global record for the organization, and users are
associated through the ProfileSkillUser object.

Note: For information about Live Agent skills, see the Skill topic.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the profile skill.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the current user last viewed a record related to
this profile skill. Available in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProfileSkill

**Field Name** **Details**

**Description**
The timestamp indicating when the current user last viewed this profile skill.
Available in API version 29.0 and later.

```
Name

OwnerId

UserCount

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile skill.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the profile skill.

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
Filter, Group, Nillable, Sort

**Description**

The number of users with the profile skill.

Use the ProfileSkill object to look up the attributes of a skill that can be assigned to a user. This is a global object and is not owned by
any specific user.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects ProfileSkillEndorsement

**ProfileSkillFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillHistory**

History is available for tracked fields of the object.

**ProfileSkillOwnerSharingRule**

Sharing rules are available for the object.

**ProfileSkillShare**

Sharing is available for the object.

### ProfileSkillEndorsement

Represents a detail relationship of ProfileSkillUser. An endorsement of a profile skill shows approval and support of another user’s publicly
declared skill.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

ProfileSkillUserId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the profile skill being endorsed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkillUser record that is being endorsed.

This is a relationship field.

**Relationship Name**
ProfileSkillUser

**Relationship Type**
Lookup

**Refers To**
ProfileSkillUser


### Standard Objects ProfileSkillShare

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the person giving the endorsement.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Use the ProfileSkillEndorsement object to query about a single endorsement given to a user about a specific skill. Users can’t endorse
themselves, they can only be endorsed by others unless they are administrators with the “Modify All Data” permission.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillEndorsementChangeEvent (API version 62.0)**
Change events are available for the object.

**ProfileSkillEndorsementFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillEndorsementHistory**

History is available for tracked fields of the object.

### ProfileSkillShare

Represents a sharing entry on a ProfileSkill.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


Standard Objects ProfileSkillShare

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

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
Level of access that the User or Group has to the ProfileSkill. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for ProfileSkill objects.

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
ProfileSkill

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects ProfileSkillUser

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values may include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the ProfileSkill with them.

**•** `Owner` —The User is the owner of the ProfileSkill or is in a role above the
ProfileSkill owner in the role hierarchy.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the ProfileSkill.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object is read only. It is visible because of constraints to the ProfileSkill object, but it is ignored and does not control which users
and groups can view and edit ProfileSkill records owned by other users.

### ProfileSkillUser

Represents a detail relationship of User. The object connects profile skills with users.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProfileSkillUser

Fields

**Field Name** **Details**

```
EndorsementCount

Name

ProfileSkillId

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of endorsements.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the skill user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkill.

This is a relationship field.

**Relationship Name**
ProfileSkill

**Relationship Type**
Lookup

**Refers To**
ProfileSkill

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user. This field can’t be changed once it is created.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects ProgramRebateType

**Field Name** **Details**

**Refers To**
User

Usage

Use this object to assign specific skills to specific users. ProfileSkillUser appears on the Overview tab on the Chatter profile page. Users
can only create a skill mapping for themselves, they can’t create skill mappings for others unless they are administrators with the “Modify
All Data” permission. Additionally, users can only edit this object if they are the context user and are not editing the `UserId` field.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillUserFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillUserHistory**

History is available for tracked fields of the object.

### ProgramRebateType

Represents a rebate structure associated with a Rebate Program. This object is available in API version 63.0 and later.

A ProgramRebateType record is created to define how benefits are calculated—such as accruals, payouts, or both—based on specified
measure fields and logic.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccrualRate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The rate of accrual based on the value selected in the Measure Type field. For example, when
the measure type is percent and you enter 10, the accrual rate is 10%.


Standard Objects ProgramRebateType

**Field** **Details**

```
AggregateObjectName

BenefitQualifierField

CalcObjectId

CalculationBasis

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The object that stores the aggregation results.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The field on the aggregation object used to define thresholds for qualifying benefits (minimum
or maximum).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to a calculation definition from the Data Processing Engine.

This field is a relationship field.

**Relationship Name**
CalcObject

**Refers To**
BatchCalcJobDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the method used to calculate the rebate amount.

Possible values are:

**•** `Accrual`

**•** `Payout`

**•** `PayoutAndAccrual` —Payout and Accrual

The default value is `Payout` .


Standard Objects ProgramRebateType

**Field** **Details**

```
CalculationMethod

CalculationType

ExecutionProcedureId

FilterAction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines how tiered rebate benefits are calculated.

Possible values are:

**•** `Retrospective`

**•** `Stepped`

The default value is `Retrospective` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of rebate calculation logic to use.

Possible values are:

**•** `AggregateBased` —Aggregate Based

**•** `Custom`

**•** `GrowthBased` —Growth Based

**•** `PerTransaction` —Per Transaction

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to business rules that define custom execution logic.

This field is a relationship field.

**Relationship Name**
ExecutionProcedure

**Refers To**
ExpressionSet

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProgramRebateType

**Field** **Details**

**Description**
Logical operator to apply between filter conditions.

Possible values are:

**•** `AllConditionsMet` —All Conditions Are Met (AND)

**•** `AnyConditionMet` —Any Condition Is Met (OR)

**•** `CustomLogic` —Custom Condition Logic

**•** `NoConditionsMet` —No Conditions Are Met

```
FilterCriteria

FilterLogic

IsIntegratable

LastReferencedDate

```

**Type**
textarea

**Properties**
Nillable

**Description**

Holds the filter conditions in textual format. Used to define eligibility criteria for rebate
qualification.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Logical formula used to combine filter conditions, typically using field references and logical
operators.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When selected, allows this rebate type to be applied on transactional records such as orders
or opportunities.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last referenced by the user. Useful for user
activity tracking.


Standard Objects ProgramRebateType

**Field** **Details**

```
LastViewedDate

MeasureField

Name

OwnerId

ProductFilterType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last opened or viewed. Tracks user interaction
history.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The aggregation object field used with measure type and benefit value to calculate the
rebate amount. This is required for the Amount per Unit and Percentage of Revenue measure
types.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique name that identifies the rebate type configuration. Used as a reference label across
related components.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifies the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProgramRebateType

**Field** **Details**

**Description**
Specifies whether the rebate applies to included or excluded products.

Possible values are:

**•** `ExcludeProducts` —Exclude Products

**•** `IncludeProducts` —Include Products

```
RebateMeasureType

RebateProgramId

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the method to measure benefit payout.

Possible values are:

**•** `AmountperUnit` —Amount per Unit

**•** `Custom`

**•** `FixedAmount` —Fixed Amount

**•** `PercentageOfRevenue` —Percentage of Revenue

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Links this rebate type to its parent rebate program.

This field is a relationship field.

**Relationship Name**
RebateProgram

**Relationship Type**
Master-detail

**Refers To**
RebateProgram (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies whether the rebate type is currently active.

Possible values are:

**•** `Active`


### Standard Objects Promotion

**Field** **Details**

**•** `Inactive`

The default value is `Inactive` .

```
UnitOfMeasureId

ValidityDuration

ValidityDurationType

### Promotion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the unit of measure associated with the rebate type.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Duration for which the inventory is eligible for price protection.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to measure ValidityDuration.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Years`

The default value is `Years` .

Represents a promotion for B2B or D2C stores. This object is available in API version 52.0 and later.


Standard Objects Promotion

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Some of the fields on the Promotion object are available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AreQualItemsExclFromDiscounts

CurrencyIsoCode

Description

DiscountOrder

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Exclude qualifying items from discount. You can use this field to create buy-one-get-one
promotions. The default value is false. This field is available in API version 56.0 and later.

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
Description of the promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to apply discounts first to the least expensive products or to the most
expensive products.

Possible values are:


Standard Objects Promotion

**Field** **Details**

**•** `LeastExpensive`

**•** `MostExpensive`

The default value is `MostExpensive` .

This field is available in API version 56.0 and later.

```
DiscountRestriction

DisplayName

EndDateTime

ExclusivityType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to restrict the products that can be discounted based on the least expensive
qualifying product.

Possible values are:

**•** `LeastExpensive`

**•** `None`

The default value is `None` .

This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Display name of the promotion.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion ends.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether a promotion can be combined with other promotions.

Possible values are:

**•** `No`  - Can be combined with other promotions.


Standard Objects Promotion

**Field** **Details**

**•** `Class`                   - Can’t be combined with a promotion of the same class (product, order, or
shipment), but allows for promotions of separate classes to be combined. For example,
an order discount on top of a product discount.

**•** `Global`                   - Only promotion that can be applied to the order, regardless of class.

The default value is `Class` .

This field is available in API version 58.0 and later.

```
IsActive

IsApproachingDiscountApplicable

IsAutomatic

IsCommercePromotion

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the promotion is active (true) or inactive (false).

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the promotion shows an approaching discount message. Set an approaching
discount threshold value on the PromotionQualifier object. This field is available in API version
64.0 and later.

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the promotion is automatic or manual. If the promotion is automatic,
it automatically applies to eligible carts with no buyer action required. if the promotion is
manual, the buyer applies a coupon to redeem the promotion.

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the promotion is a B2B Commerce promotion (true) or not (false).


Standard Objects Promotion

**Field** **Details**

The default value is false.

```
IsTiered

LastReferencedDate

LastViewedDate

MaximumUsageCount

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the promotion uses promotion tiers (true) or not (false). This value can’t
be changed.

The default value is false.

A tiered promotion can have up to 10 associated tiers.

This field is available in API version 57.0 and later.

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
possible that this record was referenced and not directly accessed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of times the promotion can be applied to a cart. If left blank, the default
value is 1. This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects Promotion

**Field** **Details**

**Description**
Name of the promotion.

```
Objective

OwnerId

PriorityNumber

QualifierCriteria

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
More information, if any, about the purpose of the promotion.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the promotion.

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
Priority for the promotion. The priority determines which promotions apply first. The lower
the number, the higher the priority.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple qualifiers, this field determines whether all qualifiers must be
met or whether any must be met for the promotion to apply.

Possible values are:

**•** `All`


Standard Objects Promotion

**Field** **Details**

**•** `Any`

The default value is 'All'.

This field is available in API version 53.0 and later.

```
StartDateTime

TargetCriteria

TermsAndConditions

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion begins.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple targets, indicates whether a cart must meet the criteria for any
target or the criteria for all targets.

Possible values are:

**•** `All`

**•** `Any`

This field is available in API version 56.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Terms and conditions the buyer accepts before applying the promotion.

This field is available in API version 53.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionFeed on page 55**
Feed tracking is available for the object.

**PromotionHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects PromotionLineItemRule

**PromotionShare on page 67**
Sharing is available for the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionLineItemRule

Lists compound conditions about a promotion. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssociatedReferenceId

AssociatedType

```

**Type**
Reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated reference.

**Relationship Name**
AssociatedReference

**Relationship Type**
Lookup

**Refers To**
PromotionQualifier, PromotionTarget

**Type**
Picklist


Standard Objects PromotionLineItemRule

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of object the rule is associated with.

Possible values are:

**•** `PromotionQualifier`

**•** `PromotionTarget`

```
Name

OperatorType

OwnerId

```

**Type**
String

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion rule.

**Type**
Picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Operator type for promotion line item rule.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_OR_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_OR_EQUAL_TO`

**•** `NOT_EQUAL_TO`

The default value is `EQUAL_TO` .

**Type**
Reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects PromotionMarketSegment

**Field** **Details**

**Refers To**
Group, User

```
Type

TypeReferenceId

TypeValue

```

**Type**
Picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type on which the rule is being applied.

Possible values are:

**•** `Attribute`

**•** `Price`

**•** `Product`

**•** `ProductCategory`

**Type**
Reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the type.

**Relationship Name**
TypeReference

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Value of the type selected.

### PromotionMarketSegment

Represents a market segment within B2B Commerce that promotions can be assigned to. This object is available in API version 52.0 and
later.


Standard Objects PromotionMarketSegment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionMarketSegment object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

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

**Description**
The name of the promotion segment.


Standard Objects PromotionMarketSegment

**Field** **Details**

```
PromotionId

PromotionSegmentId

```

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to associate with your promotion segment.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion segment that you want to associate with.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment


### Standard Objects PromotionQualifier PromotionQualifier

Represents the product, product category, or order that you want to target with your promotion qualifier in a B2B or D2C store. This
object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionQualifier object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ApproachingDiscountThreshold

CurrencyIsoCode

ExternalQualifier

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount that a customer has to reach before seeing an approaching discount message.

For example, if a promotion qualifier minimum is set at $150 and this field is set at $50, then
a customer receives a banner notification that they're approaching the discount when they
have at least $50 in their cart. This field is available in API version 64.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A qualifying product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.


Standard Objects PromotionQualifier

**Field** **Details**

Note: This field is available through the API only.

```
LastReferencedDate

LastViewedDate

MinimumAmount

MinimumQuantity

Name

PromotionId

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum dollar amount that a buyer must purchase to qualify for the promotion.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum quantity that a buyer must purchase to qualify for the promotion.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion qualifier.

**Type**
reference


Standard Objects PromotionQualifier

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to associate with your promotion qualifier.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

```
PromotionTierId

QualifierId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion tier associated with the qualifier. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the qualifier.

This is a polymorphic relationship field.

**Relationship Name**
Qualifier

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory


Standard Objects PromotionQualifier

**Field** **Details**

```
QualifierOperator

QualifierProductCategoryName

QualifierProductName

QualifierProductSku

QualifierRuleCriteriaType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** `EQUAL_TO`

**•** `NONE`

**•** `NOT_EQUAL_TO`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the qualifier. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the qualifier. This field is available in API version 55.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the qualifier. This field is available in API
version 55.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier rule criteria.

Possible values are:


### Standard Objects PromotionSegment

**Field** **Details**

**•** `All`

**•** `Any`

```
QualifierType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier that you want to add to the promotion. `Product` applies the qualifier
to a single product, `ProductCategory` to a predetermined group of products, and
`TransactionTotal` to the entire order.

Possible values are:

**•** `Product`

**•** `ProductCategory`

**•** `TransactionTotal`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionQualifierFeed on page 55**
Feed tracking is available for the object.

**PromotionQualifierHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment PromotionSegmentBuyerGroup PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegment

Represents a promotion segment, which you can assign to different stores or buyer groups, allowing them to access the promotion.
This object is available in API version 52.0 and later.


Standard Objects PromotionSegment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegment object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

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
Name of the promotion segment.


### Standard Objects PromotionSegmentBuyerGroup

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
The ID of the user who created this promotion segment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentFeed on page 55**
Feed tracking is available for the object.

**PromotionSegmentHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegmentBuyerGroup

Represents a promotion segment, associated with a buyer group, and used for B2B Commerce. This object is available in API version
52.0 and later.


Standard Objects PromotionSegmentBuyerGroup

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegmentBuyerGroup object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
BuyerGroupId

CurrencyIsoCode

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Buyer Group that you want to include in your market segment.

This is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

This field is available in API version 53.0 and later.


Standard Objects PromotionSegmentBuyerGroup

**Field** **Details**

```
LastViewedDate

Name

PromotionSegmentId

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

This field is available in API version 53.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion segment you want to associate with your buyer group.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentBuyerGroupFeed on page 55**
Feed tracking is available for the object.


### Standard Objects PromotionSegmentSalesStore

**PromotionSegmentBuyerGroupHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment

PromotionSegmentBuyerGroup

### PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegmentSalesStore

Represents a promotion segment, associated with a store, and used for B2B Commerce. This object is available in API version 52.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegmentSalesStore object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PromotionSegmentSalesStore

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

PromotionSegmentId

SalesStoreId

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion segment you want to associate with your store.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store you want to include in your promotion segment.

This is a relationship field.

**Relationship Name**
SalesStore


### Standard Objects PromotionTarget

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
WebStore

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentSalesStoreFeed on page 55**
Feed tracking is available for the object.

**PromotionSegmentSalesStoreHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

### PromotionTarget

PromotionTier

### PromotionTarget

Represents the product, product category, or order that you want to target with your promotion in a B2B Store or D2C store. This object
is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionTarget object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects PromotionTarget

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentPercent

AdjustmentType

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The promotion discount is expressed as an amount, not as a percentage.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage discount of the promotion. Valid values include numbers from 1 through
100.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of adjustment discount applied to the product or group of products.

Possible values are:

**•** `FixedAmountOffLineItemTotal` —Fixed amount off the total of all line
items.

**•** `FixedAmountOffTransaction` —Fixed amount off the entire transaction.
This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice` —Fixed amount off the unit price.

**•** `FixedPrice` —Fixed price for a product. This value is available in API version
56.0 and later.

**•** `TotalFixedPrice` —Fixed price for a set number of products. Requires a
quantity limit. This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice` —Fixed amount off the unit price.

**•** `PercentageDiscount` —Percentage discount.

**•** `BonusProduct` —Gift product at no additional cost after qualifying purchases.
This value is available in API version 64.0 and later.

**Type**
picklist


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code
for any currency allowed by the organization.

```
ExternalTarget

IsMinItemCountRequired

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A target product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.

Note: This field is available through the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the max value in the `RestrictionQuantity` field must be met before
the promotion is applied. The default value is `false` . This field is available in API version
56.0 and later.

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


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion target.

```
PromotionId

PromotionTierId

RestrictionQuantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to reference.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion tier associated with the target. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum number of times the discount can be applied to the target. This field is
available in API version 56.0 and later.


Standard Objects PromotionTarget

**Field** **Details**

```
TargetId

TargetOperator

TargetProductCategoryName

TargetProductName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product or product category that you want to target.

This is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
For product and category targets, specify if the qualifying product or item in the
qualifying category must be in the cart to determine if the cart satisfies the promotions
criteria. For example, a quantity or amount across one or more items. This field is available
in API version 59.0 and later.

Possible values are:

**•** `EQUAL_TO` —Specifies that the qualifying product or item in the qualifying category
must be in the cart.

**•** `NOT_EQUAL_TO` —Specifies that the qualifying product or item in the qualifying
category isn’t required to be in the cart.

**•** `NONE` —Specifies that none of the other possible values apply. If the target type is
for an order, you must use none.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the target. This field is available in API
version 55.0 and later.

**Type**
string


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the target. This field is available in API version
55.0 and later.

```
TargetProductSku

TargetRuleCriteriaType

TargetType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the target. This field is available in
API version 55.0 and later.

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls what promotion rules must be met for the promotion to be valid. This field is
available in API version 59.0 and later.

Possible values are:

**•** `ALL` —Specifies that all of the promotion rules must be met.

**•** `ANY` —Specifies that any of the promotion rules can be met.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The target of the promotion.

Possible values are:

**•** `Product` —Applies the promotion to a single product.

**•** `ProductCategory` —Applies the promotion to a group of products.

**•** `Shipping` —Applies the promotion to all shipping methods on the order.

**•** `StandardShippingRate` —Applies the promotion to a single shipping method
on the order.


### Standard Objects PromotionTier

**Field** **Details**

**•** `Transaction` —Applies the promotion to the entire order.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

### PromotionTier PromotionTier

Represents a tier of a promotion that includes multiple tiers. A promotion can have up to 10 tiers. This object is available in API version
57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

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


Standard Objects PromotionTier

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it can mean that the user accessed this record or list view ( `LastReferencedDate` ) but
didn’t view it.

```
Name

PromotionId

Rank

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the promotion tier.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the promotion tier.

This field is a relationship field.

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
Priority of the tier among the associated promotion’s tiers. Tiers are evaluated in order from
lowest to highest rank. Each tier in a promotion must have a unique rank.

Use promotion tiers with promotion qualifiers and promotion targets to create tiered promotions. Instead of associating one promotion
qualifier and one promotion target with each promotion, associate one promotion qualifier and one promotion target with each
promotion tier.


### Standard Objects Prompt

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionTierFeed on page 55**
Feed tracking is available for the object.

**PromotionTierHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### Prompt

Represents record details about an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

### Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.

Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

### Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects Prompt

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

NamespacePrefix

```

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the in-app guidance was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


### Standard Objects PromptAction

**Field** **Details**

refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

### PromptAction

Represents how the user interacted with the in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
LastDisplayDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last displayed to the user.


Standard Objects PromptAction

**Field** **Details**

```
LastResult

LastResultDate

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the last user interaction. Valid values are:

**•** `CustomAction`

**•** `Dismiss`

**•** `Error`

**•** `Finish` —(walkthroughs only)

**•** `NoAction`

**•** `NotSeen`

**•** `Snooze`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last interacted with.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the in-app guidance.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects PromptAction

**Field** **Details**

**Refers To**
Group, User

```
PromptVersionId

SnoozeUntil

StepCount

StepNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptVersion object.

This is a relationship field.

**Relationship Name**
PromptVersion

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp for when the user’s snooze request expires. The user won’t see the prompt
again until they navigate to the page after the snooze time expires.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the total number of steps in the walkthrough. Available in API version 49.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the number of the last step the user viewed or interacted with in a walkthrough.
Maximum value is 10. Available in API version 49.0 and later.


Standard Objects PromptAction

**Field** **Details**

```
TimesActionTaken

TimesDismissed

TimesDisplayed

TimesSnoozed

UserId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user took action on the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user dismissed the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the in-app guidance was displayed to the user.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of times the user snoozes the prompt.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects PromptError

Associated Objects

This object has the following associated objects. They are available in API version 46.0 and later.

**PromptActionOwnerSharingRule**

Sharing rules are available for the object.

**PromptActionShare**

Sharing is available for the object.

### PromptError

Represents the error or warning associated with the PromptAction. Available in API version 52.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
IsError

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the in-app guidance had an error `true` or a warning `false` . The default is
`false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the PromptError record.


Standard Objects PromptError

**Field** **Details**

```
OwnerId

PromptActionId

StepNumber

Type

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptAction that the PromptError is related to.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the step number that the user encountered an error or warning in a walkthrough.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the type of error or warning. Possible values are:

**•** `NoAccessToApp` —A step on this walkthrough is on an app that some of your users
don’t have access to.

**•** `NoAccessToPage` —A step on the walkthrough is on a page that some of your users
don’t have access to.

**•** `ReferenceElementNotFound` —The target element has moved or is no longer
on your page. Targeted prompts attached to unavailable elements convert to floating
prompts. Check your access to the element, or enter targeting mode and reassign the
targeted prompt.

**•** `Unavailable` —Users tried to open this walkthrough using its URL, but it's inactive
or the users aren’t licensed to see it. To make it accessible to users, check its settings or
activate it.


### Standard Objects PromptActionOwnerSharingRule

Associated Objects

This object has the following associated objects. They are available in API version 52.0 and later.

**PromptErrorOwnerSharingRule**

Sharing rules are available for the object.

**PromptErrorShare**

Sharing is available for the object.

### PromptActionOwnerSharingRule Represents a rule which determines PromptAction sharing access for the owners. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
   create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

   update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AccessLevel

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the access level of users for in-app guidance. Valid values are `Read` and `Edit` .

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the in-app guidance. Maximum of 255 characters.


### Standard Objects PromptActionShare

**Field** **Details**

```
DeveloperName

GroupId

Name

UserOrGroupID

### PromptActionShare

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### ID of the group whose PromptAction are shared.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the in-app guidance.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### ID of the user or group with whom PromptAction access is shared.

Represents a sharing entry on a prompt action record. Available in API version 46.0 and later.


Standard Objects PromptActionShare

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

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
Indicates the access level of users for in-app guidance. Valid values are `Read`, `Edit`, and
`All` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects PromptLocalization

**Field** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule` —The User or Group has access via a sharing rule.

**•** `GuestRule` —The User or Group has access via a guest user sharing rule.

**•** `Manual` —The User or Group has access because a User with “All” access manually
shared the prompt action with them.

**•** `Owner` —The User is the owner of the prompt action.

```
UserOrGroupId

### PromptLocalization

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the User or Group.

Represents the translated value of a label for record details about in-app guidance when the Translation Workbench is enabled for your
org. Available in API version 48.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects PromptLocalization

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
Language

NamespacePrefix

ParentId

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the language used in the org where the in-app guidance was created.

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

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update


### Standard Objects PromptVersion

**Field** **Details**

**Description**
The actual translated record details for the in-app guidance.

### PromptVersion

Represents an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, see Considerations for](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)
[Creating In-App Guidance and Permissions for Creating and Accessing In-App Guidance in](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US) _Salesforce Help_ for permissions.

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
ActionButtonLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the action button or link. Maximum of 25 characters. For a walkthrough, specify
this value on the last step.


Standard Objects PromptVersion

**Field** **Details**

```
ActionButtonLink

Body

DelayDays

Description

DismissButtonLabel

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for the action button or link. Maximum of 1,000 characters. You can’t use the `GROUP`
`BY` option in a SOQL query for this field. For a walkthrough, specify this value on the last
step.

**Type**
textarea

**Properties**
Create, Update

**Description**
Body content.

In API version 60.0 and later, enter up to 4,000 characters for all prompt types.

In earlier API versions, enter up to 240 characters for floating prompts and targeted prompts.
Enter up to 4,000 characters for docked prompts.

For docked prompts, the maximum characters include HTML markup, not just readable text.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of days between occurrences. For a walkthrough, specify this value on the first step.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the dismiss button of a floating or targeted prompt. Maximum of 15 characters.


Standard Objects PromptVersion

**Field** **Details**

```
DisplayPosition

DisplayType

ElementRelativePosition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position of a floating prompt on the page. Valid values are:

**•** `TopLeft`

**•** `TopCenter`

**•** `TopRight`

**•** `MiddleLeft`

**•** `MiddleCenter`

**•** `MiddleRight`

**•** `BottomLeft`

**•** `BottomCenter`

**•** `BottomRight`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of prompt. Valid values are:

**•** `DockedComposer` —A docked prompt

**•** `FloatingPanel` —A floating prompt

**•** `Targeted` —A targeted prompt. Available in API version 52.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The location of a targeted prompt relative to the element. This field is available in API version
52.0 and later. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `LeftBottom`

**•** `LeftCenter`

**•** `LeftTop`


Standard Objects PromptVersion

**Field** **Details**

**•** `RightBottom`

**•** `RightCenter`

**•** `RightTop`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

```
EndDate

Experience

ExperienceContextId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date to stop showing the in-app guidance. For a walkthrough, specify this value on the
first step.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field corresponds to the **Environment** picklist in In-App Guidance Builder. Available in
version 60.0 and later.

Possible values are:

**•** `Lightning` —Default. The in-app guidance is used in a Lightning Experience app or
page.

**•** `Site` —The in-app guidance is used in a supported Experience Cloud site page.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the value of `Experience` is `Site` . The ID of the Experience Cloud site context
associated with the in-app guidance prompt. Available in version 60.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ExperienceContext

**Relationship Type**
Lookup

**Refers To**
Site


Standard Objects PromptVersion

**Field** **Details**

```
Header

ImageAltText

ImageId

ImageLocation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the header of a docked prompt. This value is the label contained in the window’s
browser bar. Maximum of 36 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the alt text of an image. Required if `ImageLocation` or `ImageID` is specified.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentAsset that holds the image. Required if `ImageLocation` or
`ImageAltText` is specified.

This is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the location of the image in relation to the body text. Required if `ImageID` or
`ImageAltText` is specified. Valid values are:

**•** `Top`

**•** `Bottom`

**•** `Right`, which is for floating or targeted prompts only

**•** `Left`, which is for floating or targeted prompts only


Standard Objects PromptVersion

**Field** **Details**

```
IndexWithIsPublished

IndexWithoutIsPublished

IsPublished

MasterLabel

ParentId

```

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance is active ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Prompt


Standard Objects PromptVersion

**Field** **Details**

```
PublishedByUserId

PublishedDate

ReferenceElementContext

ShouldDisplayActionButton

ShouldIgnoreGlobalDelay

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who activated the in-app guidance. If the in-app guidance is part of a
package, this value is the user who installed the package.

This is a relationship field.

**Relationship Name**
PublishedByUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was activated. If installed from a package, this value
is the date when the package was installed. For walkthroughs, this field can only be specified
on the first step.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Used by Salesforce to identify the element that the targeted prompt is associated with.
Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an action button or link is included ( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects PromptVersion

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance ignores the global time delay and instead shows on
page load ( `true` ) or not ( `false` ). This field is available in API version 48.0 and later.

```
StartDate

StepNumber

TargetAppDeveloperName

TargetAppNamespacePrefix

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the date to start showing the in-app guidance. For a walkthrough, specify this value
on the first step.

In API version 48.0 and earlier, this field is required.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for walkthroughs only. Indicates the number of the last step the user viewed or
interacted with in a walkthrough. Include up to 10 steps. Numbers must be consecutive
without repeated or skipped numbers. Available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s developer name where the in-app guidance appears. Deprecated in API version
51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s namespace prefix where the in-app guidance appears. This value must match the
target app’s `NamespacePrefix` in the org that the package is being installed into.
Maximum of 15 characters. Deprecated in API version 51.0 and later.


Standard Objects PromptVersion

**Field** **Details**

```
TargetPageKey1

TargetPageKey1Ref

TargetPageKey2

TargetPageKey3

TargetPageKey4

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Used by Salesforce to identity the prompt’s page location along with
`targetPageKey2`, `targetPageKey3`, `targetPageKey4`, and
`targetPageType` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey2`,
`TargetPageKey3`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey1`,
`TargetPageKey3`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey1`,
`TargetPageKey2`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the page location along with `TargetPageKey1`,
`TargetPageKey2`, `TargetPageKey3`, and `TargetPageType` . This field is available
in API version 53.0 and later.


Standard Objects PromptVersion

**Field** **Details**

```
TargetPageType

TargetRecordType

ThemeColor

ThemeSaturation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of page where the in-app guidance appears.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to determine if in-app guidance is specific to a record type. This field is
available in API version 53.0 and later.

**Relationship Name**
TargetRecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which custom theme color is applied to the in-app guidance. Required if
`ThemeSaturation` is specified. For a walkthrough, specify this value on the first step.
Valid values are:

**•** `Theme1` —derived from the current brand color

**•** `Theme2` —derived from the current page background color

**•** `Theme3` —derived from the current global header color

**•** `Theme4` —derived from the current app theme color

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects PromptVersion

**Field** **Details**

**Description**
Indicates which color value, or saturation, is applied to the in-app guidance that has a custom
theme color. Required if `ThemeColor` is specified. For a walkthrough, specify this value
on the first step. Valid values are:

**•** `Dark`

**•** `Light`

```
TimesToDisplay

Title

UserAccess

UserProfileAccess

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if recurrences are scheduled. The maximum number of times to show the in-app
guidance. Salesforce detects whether the user interacts with the in-app guidance, then
determines whether to show the in-app guidance again or cancel scheduled recurrences.
Maximum value of 30. For a walkthrough, specify this value on the first step.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The label for the title. Maximum of 36 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which permissions can see the in-app guidance. Valid values are:

**•** `Everyone`, which indicates that there’s no permission restrictions

**•** `SpecificPermissions`, which indicates that only users with all the specific user
permissions specified can see the in-app guidance

In API version 48.0 and earlier, this field is required.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which profiles can see the in-app guidance. This field is available in API version 48.0
and later. Valid values are:


### Standard Objects PromptVersionLocalization

**Field** **Details**

**•** `Everyone`, which indicates that there are no profile restrictions

**•** `SpecificProfiles`, which indicates that users with any of the specified user profiles
can see the in-app guidance

```
VersionNumber

VideoLink

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The number remains `1` since multiple versions aren’t saved in the org.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The embed URL for a video in a docked prompt. Maximum of 1,000 characters. You can
specify this field or the `image` field, but not both. This field is available in API version 48.0
[and later. See Considerations for Creating In-App Guidance.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)

### PromptVersionLocalization

Represents the translated value of a label for-app guidance when the Translation Workbench is enabled for your org. Available in API
version 48.0 and later.

Use prompts and walkthroughs to display announcements, training, or news to users within the app. Choose to add an action button
or link that links to a URL of your choice. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects PromptVersionLocalization

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
Language

NamespacePrefix

ParentId

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the language used in the org where the in-app guidance was created.

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

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update


### Standard Objects Prospect

**Field** **Details**

**Description**
The actual translated label of the in-app guidance.

### Prospect

Represents a prospect. A prospect is an individual who has shared contact information, but isn't yet qualified. This object is available in
API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Address

AnnualRevenue

City

Company

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Street address of the prospect. Up to 255 characters are allowed.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The prospect company's yearly revenue.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City that's included in the prospect’s address.

**Type**
string


Standard Objects Prospect

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's company.

```
ConvertedAccountId

ConvertedContactId

ConvertedDate

ConvertedLeadId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the account into which the prospect converted.

This is a relationship field.

**Relationship Name**
ConvertedAccount

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the contact into which the prospect converted.

This is a relationship field.

**Relationship Name**
ConvertedContact

**Refers To**
Contact

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date on which this prospect was converted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Prospect

**Field** **Details**

**Description**
Object reference ID that points to the lead into which the prospect has been converted.

This is a relationship field.

This field is a relationship field.

**Relationship Name**
ConvertedLead

**Refers To**
Lead

```
ConvertedOpportunityId

Country

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the opportunity into which the prospect has been
converted.

This is a relationship field.

**Relationship Name**
ConvertedOpportunity

**Refers To**
Opportunity

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Prospect's country.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects Prospect

**Field** **Details**

**Description**
The prospect’s description.

```
Email

FirstName

GenderIdentity

GeocodeAccuracy

Industry

IsConverted

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's email address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect’s first name. Up to 40 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect’s self-identified experience of their gender, which does or doesn’t correspond
to the prospect’s designated sex at birth.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. For details on geolocation compound fields,
see Geolocation Compound Field on page 18.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Primary business of the prospect’s company

**Type**
boolean


Standard Objects Prospect

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the prospect has been converted ( `true` ) or not ( `false` ). Label is
**Converted** .

```
LastName

Latitude

LeadSource

Longitude

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The Last name of the prospect. Up to 80 characters are allowed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –90 and 90 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations on page 19.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin or source of the lead.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations on page 19.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Prospect

**Field** **Details**

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

```
NumberOfEmployees

Phone

PostalCode

ProspectRecordName

ProspectStatus

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of employees at the prospect's company. Label is **Employees** .

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code that's included in the prospect's address. Label is **Zip/Postal Code** .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the prospect record used for managing prospects.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the prospect.

Possible values are:

**•** `Contacted`

**•** `New`


Standard Objects Prospect

**Field** **Details**

**•** `Nurturing`

**•** `Qualified`

**•** `Unqualified`

The default value is `New` .

```
Salutation

State

Street

Title

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's preferred title.

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Mx.`

**•** `Prof.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State that's included in the prospect's address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street number or name that's included in the prospect's address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's business title, such as CFO or CEO. The maximum size is 128 characters. When
converting a prospect to a person account, the conversion fails if the prospect Title field
contains more than 80 characters.


### Standard Objects ProspectingAgentDataSource ProspectingAgentDataSource

For internal use only.

### ProspectingAgentRcmdTarget

Represents prospecting information suggested by generative AI. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

This object is available if Agentforce Prospecting is enabled in your org and your org has an Agentforce for Sales or an Agentforce for
an Industry add-on license. To access this object, you need the Sales Agentic Prospecting Manager user permission.

Fields

**Field** **Details**

```
ExpirationDate

OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the recommendation expires, after which the recommendation is automatically
deleted.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The ID associated with the owner of the AI-generated recommendation. The owner
can be an individual user or a list.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


### Standard Objects ProspectingAgentSpec

**Field** **Details**

```
Rationale

Status

TargetId

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The explanation of why the agent recommended the target contact or lead. The rationale
provides context to guide users in their decision making.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the AI-generated recommendation.

Possible values are:

**•** `Accepted`

**•** `New`  - Default

**•** `Rejected`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID associated with the contact or lead recommended by the AI agent.

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Refers To**
Contact, Lead

### ProspectingAgentSpec

For internal use only.

### ProspectingAgentSpecParm

For internal use only.


### Standard Objects ProspectingAgentUserSpec ProspectingAgentUserSpec

For internal use only.

### ProrationPolicy

Defines how the price of a subscription is divided into time periods and how the price is calculated for each time period. This object is
available in API version 55.0 and later.

The proration policy defines whether partial periods are allowed and how remainder amounts are handled.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   search()

```

Special Access Rules

This object is available when Subscription Management is enabled.

Fields

**Field** **Details**

```
ArePartialPeriodsAllowed

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a subscription can be canceled partway through a period.

Set the value to `True` if a subscription can be canceled partway through a period. Otherwise,
set the value to `false` .

For example, if the proration period is monthly and this field is `true`, then customers can
cancel a subscription partway through the month. If the proration period is monthly and
this field is `false`, then the subscription is canceled at the end of the current month.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects ProrationPolicy

**Field** **Details**

```
LastViewedDate

Name

ProrationPolicyType

RemainderStrategy

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list `viewLastReferencedDate` but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the proration policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of proration policy.

Possible values are:

**•** `StandardTimePeriods` —Indicates that the proration policy divides the subscription
into similar time periods, and prorates the subscription using the time periods. For
example, a monthly subscription that's subscribed to for 12 months for a total amount
of $120 is prorated as $10 per month.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates how the leftover amount from the price calculation is allocated.

For example, if the total amount is $100 and the subscription has 12 periods, the price per
period is $8.33, with $0.04 remaining. To indicate that the $0.04 is included in the first period,
use the value `AddToFirst` . To indicate that the $0.04 is included in the final period, use
the value `AddToLast` .

Possible values are:

**•** `AddToFirst` —Add the remaining amount to the first period.

**•** `AddToLast` —Add the remaining amount to the last period.


### Standard Objects PublicComplaint PublicComplaint

Represents the complaints submitted by public users. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Fields added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

Fields

**Field** **Details**

```
AccountId

BusinessAddress

BusinessName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Account associated with this complaint.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address of the business.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The name of the business.

```
CauseSubtype

CauseType

Comments

CompensationAmount

ComplaintCaseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Misleading advertisement or documentation`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Product Communication`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Additional details about the complaint. This field is available in API version 51.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Any amount of money offered to resolve the complaint. This field is available in API version
58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The ID of the related Case. This field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ComplaintCase

**Relationship Type**
Lookup

**Refers To**
Case

```
ComplaintCaseStatus

ComplaintSubType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The status of the related Case. This field is available in API version 58.0 and later.

Possible values are:

**•** `Closed`

**•** `Escalated`

**•** `In Progress`

**•** `Merged`

**•** `New`

**•** `On Hold`

**•** `Response Received`

**•** `Waiting for Customer`

**•** `Working`

The default value is `New` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint. All values except `Fire Safety` are available in API version
58.0 and later.

Possible values are:

**•** `Account Opening/Closure`

**•** `Amount Not Dispensed`

**•** `Attempts to Collect Debt not Owed`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Auto Debit Mandate`

**•** `Communication Tactics`

**•** `Credit Limit Changed`

**•** `Credit Report / Credit Score`

**•** `Delays / Timescales`

**•** `Disputes over sums/charges`

**•** `Errors / not following instructions`

**•** `Fire Safety`

**•** `Fraud Handling`

**•** `Inaccessible ATMs`

**•** `Inaccessible Branch Entrances`

**•** `Inaccessible Mobile banking features`

**•** `Inaccessible Website`

**•** `Misleading Advertising`

**•** `Mobile Banking - Features or Functionality`

**•** `No Written Notification About Debt`

**•** `Online Banking - Features or Functionality`

**•** `Other General Admin/Customer Service`

**•** `Others`

**•** `Problem when Making Payments`

**•** `Product Disclosure Information`

**•** `Product Performance/Features`

**•** `Unauthorised Transaction(s)`

**•** `Unclear Arrangement`

**•** `Unclear Guidance`

**•** `Unsuitable Advice`

```
ComplaintSummary

ComplaintType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of customer complaints and related cases. This field is available in API version
62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The type of complaint. All values except `Safety` are available in API version 58.0 and later.

Possible values are:

**•** `Accessibility Issues`

**•** `Advising, Selling and Arranging`

**•** `Digital or Technology`

**•** `Financial Hardship or Collections`

**•** `General Admin/ Customer Service`

**•** `Information, sums/ charges or Product Performance`

**•** `Lending / Credit`

**•** `Marketing or Corporate Communications`

**•** `Others`

**•** `Safety`

**•** `Transaction Related`

```
Description

Email

EscalationCause

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the complaint.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email of the complainant.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the complaint was escalated. This field is available in API version 58.0 and later.

Possible values are:

**•** `Alleged ADA Violation`

**•** `Alleged Discrimination`

**•** `Alleged MLA Violation`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Alleged SCRA Violation`

**•** `Alleged UDAAP Violation`

**•** `Consumer Protection Agency Involvement`

**•** `Lawsuit Filed`

**•** `Media Involvement`

**•** `None`

**•** `Received by Executive Leadership`

The default is `None` .

```
FirstName

IncidentDate

IsComplainantAuthorized

IsReporterConfidential

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The given name of the complainant.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date of the incident.

The default is the date this record was created, but this field is editable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the person who filed the complaint is an authorized representative of the Account.
This field is available in API version 58.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The reporter's request for confidentiality.

The default value is `false` .


Standard Objects PublicComplaint

**Field** **Details**

```
LastName

LastReferencedDate

LastViewedDate

MobileNumber

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The family name of the complainant.

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
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The mobile number of the complainant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the complaint.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The ID of the complaint owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Priority

ProductType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the complaint.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `Medium` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product that the complaint is about. This field is available in API version 58.0 and later.

Possible values are:

**•** `ATM / debit card`

**•** `Credit Card or Prepaid Card`

**•** `Insurance`

**•** `Investments`

**•** `Merchant Services`

**•** `Mobile / electronic banking`

**•** `Money transfers, virtual currency, and money services`

**•** `Mortgage / Home Finance`

**•** `Other`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Personal Loan / other loans`

**•** `Vehicle loan or lease`

```
ReceivedDate

ReferenceRecordId

ReporterAddress

ReporterCategory

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the complaint was received. This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset, vehicle, or financial account that’s associated with the public complaint. This field
is available in API version 64.0 and later with Automotive Cloud.

This field is a relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Financial Account, Asset, Vehicle, Product2

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address of the reporter for further communication.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Role of the reporter in the organization.

Possible values are:

**•** `Childcare Providers`

**•** `Healthcare worker`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Law Enforcement`

**•** `Medical Examiners`

**•** `Mental Health Professionals`

**•** `Other`

**•** `School Personnel`

**•** `Social Worker`

The default value is `School Personnel` .

```
ReporterOrganization

ShouldInclInRegulatoryRpt

SourceType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The organization the reporter is part of.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this complaint must be included in a regulatory report. This field is available in API
version 58.0 and later.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the complaint. This field is available in API version 58.0 and later.

Possible values are:

**•** `Branch`

**•** `Consumer Protection Agency`

**•** `Contact Centre`

**•** `Mobile App`

**•** `Regulatory Agency`

**•** `Social Media`

**•** `Web Chat`


### Standard Objects PurchaseQuantityRule

**Field** **Details**

```
Status

Subject

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the complaint.

Possible values are:

**•** `In Review`

**•** `Resolved`

**•** `Submitted`

The default value is `Submitted` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Subject of the complaint. This field is available in API version 51.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
