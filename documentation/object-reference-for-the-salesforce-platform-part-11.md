Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with soft bounce tracking that soft bounced. This
field is a calculated field.


### Standard Objects LeadOwnerSharingRule

**Field** **Details**

Available in API version 54.0 and later.

```
UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the lead clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the lead in the month.

### LeadOwnerSharingRule

Represents the rules for sharing a lead with users other than the owner.

Note: To enable access to this object, contact Salesforce customer support. However, we recommend that you instead use
Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation. The
[SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects LeadOwnerSharingRule

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

```
DeveloperName

GroupId

LeadAccessLevel

Name

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
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Leads owned by users in the source group
trigger the rule to give access.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
string


### Standard Objects LeadShare

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. The target user or group is being given
access.

Use these objects to manage the sharing rules for leads. General sharing and Territory-related sharing use this object.

SEE ALSO:

### Lead LeadShare

LeadStatus

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### LeadShare

Represents a sharing entry on a Lead.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Lead object can access this object.


Standard Objects LeadShare

Fields

The properties available for some fields depend on the default org-wide sharing settings. The properties listed are true for the default
settings of such fields.

**Field** **Details**

```
IsDeleted

LeadAccessLevel

LeadId

RowCause

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
Level of access that the User or Group has to the Lead. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid when creating or updating these records.

This field must be set to an access level that is higher than the organization’s default access
level for leads.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Lead associated with this sharing entry. This field can’t be updated.

This is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
picklist


Standard Objects LeadShare

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Lead with them.

**•** `Owner` —The User is the owner of the Lead.

**•** `Rule` —The User or Group has access via a Lead sharing rule.

**•** `GuestRule` —The User or Group has access via a Lead guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Lead via an account relationship data sharing rule.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Lead. This field can’t be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view or edit leads owned by other users.


### Standard Objects LeadStatus

If you attempt to create a record that matches an existing record, the existing record is returned.

SEE ALSO:

AccountShare

Case

CaseShare

OpportunityShare

### LeadStatus

Represents the status of a Lead record, such as Open, Qualified, or Converted.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsConverted

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
Indicates whether this lead status value represents a converted lead ( `true` ) or not ( `false` ).
Multiple lead status values can represent a converted lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects LeadTag

**Field** **Details**

**Description**
Indicates whether this is the default lead status value ( `true` ) or not ( `false` ) in the picklist.

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
Label for this lead status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the lead status picklist. These numbers are not guaranteed
to be sequential, as some previous lead status values might have been deleted.

This object represents a value in the lead status picklist (see Lead on page 3071). The lead status picklist provides additional information
about the status of a Lead on page 3071, such as whether a given status value represents a converted Lead on page 3071. Query this object
to retrieve the set of values in the lead status picklist, and then use that information while processing Lead on page 3071 objects to
determine more information about a given lead. For example, the application could test whether a given lead is converted based on its
Status value and the value of the `IsConverted` property in the associated LeadStatus record.

SEE ALSO:

LeadOwnerSharingRule

LeadShare

### LeadTag

Associates a word or short phrase with a Lead.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects LeadTag

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

LeadTag stores the relationship between its parent TagDefinition and the Lead being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects LearningContent

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### LearningContent

Represents a Trailhead or enablement site (myTrailhead) module assigned to a user in Workforce Engagement or Learning Paths. This
object also represents a Trailhead module or video in an Enablement program exercise. This object is available in API version 54.0 and
later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

**•** The org must have a Workforce Engagement license.

**•** The user must have at least one Workforce Engagement permission set assigned to them: Workforce Engagement Admin, Workforce
Engagement Analyst, Workforce Engagement Planner, Workforce Engagement Agent.

**•** For an enablement site (myTrailhead) module, the org must have a Sales Enablement license.

**•** For a Trailhead module or video in an Enablement program, the org must have an Enablement license.

Fields

**Field** **Details**

```
ApiName

AvailablePointCount

ContainsAssessmentType

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The module's human-readable API name, such as `pure-aloe-sales-strategies` .

**Type**
int

**Properties**
Group, Nillable

**Description**
The maximum points that a user can earn on their profile by completing the module. This
value is the sum of points that the content creator assigns to the module’s units.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist


Standard Objects LearningContent

**Field** **Details**

**Description**
Specifies the type of assessment that the content’s units include.

Possible values are:

**•** `MultipleChoiceQuiz` —All the content’s units have multiple-choice quizzes.

**•** `HandsOnChallenge` —At least one unit has a hands-on challenge.

```
ContentType

ContentUrl

Description

DurationCount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**
The type of content assigned to the user.

Possible values are:

**•** `All` —The content is any supported type.

**•** `Module` —The content is a Trailhead or enablement site (myTrailhead) module.

**•** `VideoLesson` —The content is a video that's specified in the Enablement workspace
in Digital Experiences and is used in an Enablement program.

**Type**
url

**Properties**
Group, Nillable

**Description**
The absolute URL to the content, such as
`https://purealoe.my.trailhead.com/en/content/sales-team-enablement/modules/pure-aloe-sales-strategies` .

**Type**
string

**Properties**
Nillable

**Description**
The module’s description.

**Type**
int

**Properties**
Group, Nillable

**Description**
The total time, in minutes, for a learner to complete all units in the module. This value is the
sum of the estimated times that the content creator assigns to the module’s units.


### Standard Objects LearningItem

**Field** **Details**

```
ExternalId

ImageUrl

IsPublic

Title

```

SEE ALSO:

PersonTraining

### LearningItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The GUID that Trailhead uses to reference the module.

**Type**
url

**Properties**
Group, Nillable

**Description**
The absolute URL to the module’s badge art image file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group

**Description**
Indicates whether the content is public Trailhead content ( `true` ) or private enablement
site (myTrailhead) content ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The module’s title.

Represents an item that requires users to take action, including a Learning Paths entry, an Enablement program, or an exercise with
linked content in an Enablement program. For Learning Paths, users are assigned a learning item to complete. For Enablement programs
and exercises, users are assigned a program or can self-enroll in shared programs. This object is available in API version 58.0 and later.


Standard Objects LearningItem

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
CustomLearningItemTypeId

EnablementProgramId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a learning item type record if this learning item represents a custom exercise type
in an Enablement program. This field is required when the `Type` field’s value is
`CustomContent` .

This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomLearningItemType

**Relationship Type**
Lookup

**Refers To**
LearningItemType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an Enablement program that contains the outcome, milestone, or exercise.

This field is a relationship field.


Standard Objects LearningItem

**Field** **Details**

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

```
LearningContentId

OwnerId

StandardCustomContentMetadata

StandardCustomLearningItemType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that represents a Trailhead module or video in a sales program exercise.
This field is a relationship field.

**Relationship Name**
LearniningContent

**Refers To**
LearningContent

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
textarea

**Properties**
Nillable

**Description**
Reserved for future use.

**Type**
picklist


### Standard Objects LearningItemAssignment

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of learning item. Possible values are:

**•** `CustomContent` —Custom exercise content in an Enablement program, such as a
screen flow, content from external repositories, or other custom content sources. Available
in API version 62.0 and later.

**•** `EnablementProgram`

**•** `LearningContent` —Trailhead module

**•** `LearningLesson` —Lesson exercise in an Enablement program

**•** `LearningLink` —Audio Recording, Document, Scheduled Event, or Other exercise
in an Enablement program

**•** `LearningPractice` —Feedback Request exercise in an Enablement program

**•** `StandardCustomContent` —Standard Custom exercise content in an Enablement
program. Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemOwnerSharingRule on page 65 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemShare on page 67 (API version 60.0)**
Sharing is available for the object.

### LearningItemAssignment

Represents the assignment of a Learning Paths entry to users or groups or the enrollment of an Enablement program for a specific user.
This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LearningItemAssignment

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
AssigneeId

AssignmentStatus

DueDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or group assigned to the learning item. This field is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of assigning an Enablement program to a user. Possible values are:

**•** `Failed`

**•** `InProgress`

**•** `Succeeded`

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LearningItemAssignment

**Field** **Details**

**Description**
The date that the assignment is due for the user or group.

```
EnrollmentType

IsOverdue

LearningItemId

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of enrollment for a user in an Enablement program. Possible values are:

**•** `Assigned`

**•** `SelfEnrolled`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the assigned learning item is overdue ( `true` ) or not ( `false` ). The default
value is `false` .

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
ID of the user who assigned the learning item. This field is a polymorphic relationship field.


Standard Objects LearningItemAssignment

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ProgressId

StartDate

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of record that represents a user's progress towards completing an assigned learning
item, such as a Learning Paths entry or sales program. This field is a relationship field.

**Relationship Name**
Progress

**Refers To**
LearningItemProgress

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The date that the learning item was assigned to the user or group.

You can assign a learning item to a user programmatically by querying the program and user, and then inserting a record into
LearningItemAssignment.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemAssignmentOwnerSharingRule on page 65 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemAssignmentShare on page 67 (API version 60.0)**
Sharing is available for the object.


### Standard Objects LearningItemProgress LearningItemProgress

Represents the progress that a user has made towards completing an assigned learning item, such as a Learning Paths entry or Enablement
program. This object is available in API version 60.0 and later.

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
CompletedDate

CompletedOnDay

CompletedPercent

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the user completed the learning item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the learning item.

**Type**
percent

**Properties**
Filter, Sort

**Description**
Percentage of the learning item that’s complete.


Standard Objects LearningItemProgress

**Field** **Details**

```
DaysInProgress

LearningItemId

OwnerId

ProgressStatus

```

**Type**
int

**Properties**
Nillable

**Description**
Number of days that have elapsed since the learning item was assigned.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the learning item. This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the learning item assignment. Possible values are:

**•** `Behind`

**•** `Completed`


### Standard Objects LearningItemSubmission

**Field** **Details**

**•** `CompletedLate`

**•** `CompletedOnTime`

**•** `InProgress`

**•** `NoLongerTracking`

**•** `NotStarted`

**•** `OnTrack`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

```
StartDate

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a user starts a Trailhead exercise in a sales program.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemProgressChangeEvent on page 68**
Change events are available for the object.

**LearningItemProgressOwnerSharingRule on page 65**
Sharing rules are available for the object.

**LearningItemProgressShare on page 67**
Sharing is available for the object.

### LearningItemSubmission

Represents a link to a resource, such as a video recording, that a user submits as part of a Feedback Request exercise in an Enablement
program. For peer and manager feedback, this resource can be a recording of a user’s sales patch. For Einstein Coach feedback, this
resource can be a video call, and Einstein generates feedback from the call’s transcription. This object is available in API version 59.0 and
later, but Einstein Coach is available only in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LearningItemSubmission

Special Access Rules

A learning item submission record is created when users take an Enablement program that includes a Feedback Request exercise for
peer and manager feedback.

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
CallId

LearningItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the video call that a user submits for Einstein Coach feedback. Einstein generates
feedback for the user based on the call’s transcription. This field is a polymorphic relationship
field.

Available in API version 61.0 and later.

**Relationship Name**
Call

**Relationship Type**
Lookup

**Refers To**
VideoCall

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise, where the `Type` of
the learning item is `LearningPractice` . This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup


### Standard Objects LearningItemType

**Field** **Details**

**Refers To**
### LearningItem

```
OwnerId

Url

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the learning item submission. This field is a polymorphic relationship
field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
URL of the content that a user submits for peer and manager feedback. For example, a link
to a video recording of a sales rep’s practice pitch.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemSubmissionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**LearningItemSubmissionShare on page 67**
Sharing is available for the object.

### LearningItemType

Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom exercise
type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition and
EnblProgramTaskSubCategory records for when admins create a program in Program Builder. This object is available in API version 62.0
and later.


Standard Objects LearningItemType

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

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
ApexEvaluationHandlerId

ApexSerializerDeserializerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how progress and completion of the custom exercise
is assessed when users take the program in the Guidance Center.

This field is a relationship field.

**Relationship Name**
ApexEvaluationHandler

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how data related to the custom exercise type is retrieved
and deployed with change sets or managed packages.

This field is a relationship field.

**Relationship Name**
ApexSerializerDeserializer

**Refers To**
ApexClass


Standard Objects LearningItemType

**Field** **Details**

```
CustomField

CustomObject

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of a custom lookup field on the LearningItem object that references
the custom object used with this custom exercise. Add values to this picklist when you
implement a custom exercise type.

For example, if a custom exercise type shows a screen flow, maybe the custom object’s name
is `ScreenFlow_Object__c` and the custom field on LearningItem is named
`ScreenFlow_Field__c` [. For details, see Implement Custom Exercise Types for](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with Enablement Developer_
_Guide_ .

This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of the custom object used with this custom exercise. Add values
to this picklist when you implement a custom exercise type.

For example, if a custom exercise type shows a Quip document, maybe the custom object’s
name is `ScreenFlow_Object__c` [. For details, see Implement Custom Exercise Types](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with Enablement Developer_
_Guide_ .

This field is unique within your organization.

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


Standard Objects LearningItemType

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
Icon

Language

LightningComponentName

MasterLabel

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The icon to use for the custom exercise type in the Guidance Center.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon categories
[and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name, including the namespace, of the Lightning Web Component (LWC) used to show
the custom exercise’s content when a user opens the exercise in the Guidance Center. For
example, if the LWC for a screen flow custom exercise is named `screenFlowViewer`,
this value is `c:screenFlowViewer` .

This field can only be accessed from Metadata API and its value is derived from the
`lightningComponentDefinition` [field on the LearningItemType metadata type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_learningitemtype.htm)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this LearningItemType value. This display value is the internal label that doesn't get
translated.


### Standard Objects LearningPractice

**Field** **Details**

```
NamespacePrefix

### LearningPractice

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

Represents a Feedback Request exercise in an Enablement program. Users can submit a sample of their work and request feedback from
their peers and managers. Or, users can submit a video call and Einstein Coach generates feedback from the call’s transcription. This
object is available in API version 59.0 and later, but Einstein Coach feedback is available only in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.


Standard Objects LearningPractice

Fields

**Field** **Details**

```
Description

InviteeQuantity

LearningItemId

Name

```

**Type**
string

**Properties**
Filter, Sort

**Description**
Instructions to the user to provide context for completing the Feedback Request exercise.
For example, `Record yourself giving a sales pitch and request`

```
  feedback from your peers.

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of peers or managers that the user is required to invite for giving feedback when
`Type` is `PeerFeedback` . Each peer or manager receives an invitation to the assessment
survey associated with the Feedback Request exercise.

When `Type` is `AIFeedback`, this value is always `1` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise. The value must be
unique. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the Feedback Request exercise. For example, `Practice Your Sales`
`Pitch` .


Standard Objects LearningPractice

**Field** **Details**

```
PromptTemplate

SurveyId

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prompt template to use with this exercise when `Type` is `AIFeedback` .

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the assessment survey that’s sent to peers and managers when `Type` is
`PeerFeedback` . This field is a relationship field.

**Relationship Name**
Survey

**Relationship Type**
Lookup

**Refers To**
Survey

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of feedback used with this exercise. Possible values are:

**•** `AIFeedback` —Users submit a video call, and Einstein Coach generates feedback from
the call’s transcription. With this type, `PromptTemplate` is required. Available in API
version 61.0 and later.

**•** `PeerFeedback` —Users submit a URL to a sample of their work, and select peers and
managers to review their work. Selected peers and managers complete an assessment
survey. With this type, `SurveyId` is required. Available in API version 61.0 and later.

**•** `Survey` —Users complete a survey as part of their enrolled employee enablement
program. Available in API version 64.0 and later.


### Standard Objects LegalEntity LegalEntity

Represents the way an organization is structured. An organization can be a single legal entity or it can comprise more than one legal
entity. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with the Salesforce Billing managed package and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_legalentity.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_legalentity.htm)

Fields

**Field** **Details**

```
CompanyName

Description

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that this legal entity represents.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the legal entity.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime


Standard Objects LegalEntity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
LegalEntityAddress

Name

OwnerId

Status

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the company that this legal entity represents. This field is a compound field
of type Address and combines these fields: LegalEntityCity, LegalEntityCountry,
LegalEntityGeocodeAccuracy, LegalEntityLatitude, LegalEntityLongitude,
LegalEntityPostalCode, LegalEntityState, and LegalEntityStreet. For more information, see
[Address Compound Fields.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/compound_fields_address.htm)

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the legal entity.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the legal entity.

Possible values are:

**•** `Active`

**•** `Inactive`


### Standard Objects LicenseDefinitionCustomPermission (Developer Preview)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**LegalEntityFeed**

Feed tracking is available for the object.

**LegalEntityHistory**

History is available for tracked fields of the object.

**LegalEntityOwnerSharingRule**

Sharing rules are available for the object.

**LegalEntityShare**

Sharing is available for the object.

### LicenseDefinitionCustomPermission (Developer Preview)

Represents a licensed custom permission that controls access to a license's features when included in a custom permission set license
definition. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access LicenseDefinitionCustomPermission, you must have the Partner Licensing Platform developer preview enabled. To participate
[in this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)
group.

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

Fields

**Field** **Details**

```
LicenseDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the custom permission set license definition that contains the licensed custom
permission.

This is a relationship field.


### Standard Objects LightningErrorEventLog

**Field** **Details**

**Relationship Name**
LicenseDefinition

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicenseDefinition

```
LicensedCustomPermissionId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the licensed custom permission that you're including in the permission set license
definition. On the CustomPermission object, the `isLicensed` field must equal true.

This is a relationship field.

**Relationship Name**
LicensedCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.262.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)

### LightningErrorEventLog

Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile app.
This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LightningErrorEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

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

**Example**
`Chrome`, `Safari`

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

**Example**

```
  United States/California

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.


Standard Objects LightningErrorEventLog

**Field** **Details**

```
ClientIp

ComponentName

ConnectionType

DeviceIdentifier

DeviceModel

DevicePlatform

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the standard component that generated the error. The Salesforce
developer assigned the name when the standard component was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
string


Standard Objects LightningErrorEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

```
DeviceSessionIdentifier

ErrorMessage

LoginKey

MobileSdkAppType

MobileSdkVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. If the user reloads a page,
it starts a new session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message generated.

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


Standard Objects LightningErrorEventLog

**Field** **Details**

```
OperatingSystemName

OperatingSystemVersion

PageAppName

PageContext

PageObjectIdentifier

PageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name.

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Context of the page where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique entity ID of event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningErrorEventLog

**Field** **Details**

**Description**
The entity type of event

```
PageStartTime

PageUrl

PreviousPageUrl

RequestIdentifier

SdkAppVersion

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time when page was initially loaded

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number.


Standard Objects LightningErrorEventLog

**Field** **Details**

```
SessionKey

StackTrace

Timestamp

UiEventIdentifier

UiEventSequenceNumber

UiEventSource

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stack trace contains the location in the code where the error occurred along with the
calling frames that led to the error.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Example**

```
  20130715233322.670

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Lightning event type.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sequence number of current event since start of session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningErrorEventLog

**Field** **Details**

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

```
UiEventTimestamp

UiEventType

UserAgent

UserIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time at which this event occurred, measured in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of error event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.


### Standard Objects LightningExperienceTheme

**Field** **Details**

```
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

### LightningExperienceTheme

Represents information for a theme in Lightning Experience. This object is available in API Version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DefaultBrandingSetId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the default branding set.

This is a relationship field.

**Relationship Name**
DefaultBrandingSet

**Relationship Type**
Lookup

**Refers To**
BrandingSet

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the theme. Limit: 1,000 characters.


Standard Objects LightningExperienceTheme

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
The unique name of the theme in the API. This name can contain only underscores and
alphanumeric characters and must be unique in your organization. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. The label corresponds to the theme name in the user interface. Limit: 70
characters.

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

**•** `pt_BR` (Portuguese (Brazil))

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


### Standard Objects LightningLoggerEventLog

**Field** **Details**

```
MasterLabel

NamespacePrefix

ShouldOverrideLoadingImage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the theme. Specify up to 70 characters.

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
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a custom image overrides the Salesforce loading image ( `true` ) or not
( `false` ).

### LightningLoggerEventLog

Lightning Logger Event Log provides information from observed Lightning component logs. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects LightningLoggerEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s browser version in major.minor format. Some browsers don’t provide a minor
version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of <Country>/<State|Province>.

**Type**
string


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

```
ClientIp

ConnectionType

DeviceModel

DevicePlatform

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
The type of connection.Possible values are:

**•** CDMA1x

**•** CDMA

**•** EDGE

**•** EVDO0

**•** EVDOA

**•** EVDOB

**•** GPRS

**•** HRPD

**•** HSDPA

**•** HSUPA

**•** LTE

**•** WIFI

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model. For example: iPad, iPhone.

**Type**
string


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in name:experience:form format. Possible values are:

Name

**•** APP_BUILDER

**•** CUSTOM

**•** S1

**•** SFX

Experience

**•** BROWSER

**•** HYBRID

Form

**•** DESKTOP

**•** PHONE

**•** TABLET

```
DeviceSessionIdentifier

LoginKey

Message

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session is based on page load time. When the user reloads
a page, a new session starts. For example: 321a1ddfaf924803a075f1e69fc87bc06f53ccd0

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


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Description**
The message is passed to the `lightning/logger log()` method. The message can
be a JSON object or a string.

```
MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type. Possible Values:

**•** HYBRID

**•** HYBRIDLOCAL

**•** HYBRIDREMOTE

**•** NATIVE

**•** REACTNATIVE

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number. For example, 5.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from the `User Agent` . For example:

**•** Android

**•** iOS

**•** OSX

**•** Windows

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from the `User Agent` .


Standard Objects LightningLoggerEventLog

**Field** **Details**

```
PageContext

PageObjectIdentifier

PageObjectType

PageUrl

RequestIdentifier

SdkAppVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: 0013000000I3zJAAAZ.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: task, contacts.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl` . For example: /sObject/0064100000JXITSAA5/view.

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


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app version used in this request.

```
SessionKey

Timestamp

UiRootActivityIdentifier

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
The ID for the root activity, if any, when this message was logged.

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


### Standard Objects LightningOnboardingConfig

**Field** **Details**

**Description**
Type of user employing Salesforce services, whether through the UI or API.

### LightningOnboardingConfig

Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the question,
how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in Lightning Experience
Setup. Available in API version 47.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

[See Switch to Salesforce Classic Feedback Form in Salesforce Help for more details.](https://help.salesforce.com/articleView?id=lex_encourage_work_feedback.htm&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

CustomQuestion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Chatter Group where the user feedback is posted.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the custom question added by the admin. Maximum of 1,000 characters.


Standard Objects LightningOnboardingConfig

**Field** **Details**

```
DeveloperName

FeedbackFormDaysFrequency

IsCustom

Language

MasterLabel

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
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days between showing the feedback form when a user switches. A value of
`0` indicates that the form is shown for every switch. Maximum of 30.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if a feedback form includes a custom question `yes` or not `no` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the feedback form was created.

**Type**
string


### Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the prompt. Maximum of 80 characters.

```
PromptDelayTime

SendFeedbackToSalesforce

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the amount of time in seconds to delay between instances of all prompts, both
org- and Salesforce-created. Minimum of 0 hours and 0 minutes. Maximum of 99 hours and
59 minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the user feedback can be shared with Salesforce. If `yes`, share the feedback with
Salesforce. If `no`, the feedback is only shared in the Chatter Group chosen when customizing
the form. The default value is `false` .

### LightningPageViewEventLog

Lightning Page View event logs represent information about the page on which the event occurred in Lightning Experience and the
Salesforce mobile app. A Lightning Page View event log tracks the page a user visited, how long the user spent on the page, and the
load time for the page. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LightningPageViewEventLog

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
The name of the browser that the user accessed. For example: Chrome, IE, Safari, Gecko.

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
The geolocation of the client in the form of <Country>/<State|Province>. For example:
`United States/California` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
IP address of the client employing salesforce.com services.

```
ConnectionType

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

Possible values are:

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DeviceIdentifier`
is a generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model. For example: `iPad`, `iPhone` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
DevicePlatform

DeviceSessionIdentifier

DoesEffectivePageTimeDeviate

Duration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format. Possible values
are:

Name

**•** `APP_BUILDER`

**•** `CUSTOM`

**•** `S1`

**•** `SFX`

Experience

**•** `BROWSER`

**•** `HYBRID`

Form

**•** `DESKTOP`

**•** `PHONE`

**•** `TABLET`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started. For example:
`321a1ddfaf924803a075f1e69fc87bc06f53ccd0` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When a deviation is detected, `DoesEffectivePageTimeDeviate` records `true` .
The default value is `false` .

**Type**
double


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The duration in milliseconds since the page start time.

This field is being deprecated. Use `EffectivePageTime` instead.

```
EffectivePageTime

EffectivePageTimeErrorType

EffectivePageTimeReason

GrandparentUiElement

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how many milliseconds it took for the page to load before a user could interact
with the page’s functionality. Multiple factors can affect effective page time, such as network
speed, hardware performance, or page complexity. If an effective page time greater than 60
seconds is detected, the value of this field is set to `null` or `0` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the origin of an error. This field is populated when
EFFECTIVE_PAGE_TIME_DEVIATION_REASON contains the PAGE_HAS_ERROR value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason for deviation in page loading time.

Examples of possible values include:

**•** `PageInDom`  - The page was loaded from a cache

**•** `PageHasError`  - An undefined page loading error occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The grandparent scope of the page element where the event occurred.


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
LoginKey

MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `UserAgent` . For example: `Android`, `iOS`,
`OSX`, `Windows` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `UserAgent` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
PageAppName

PageContext

PageObjectIdentifier

PageObjectType

PageStartTime

PageUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the application that the user accessed from the App Launcher. For
example: `LightningSales` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
`clients:cardsContainer` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: `0013000000I3zJAAAZ` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: `task`, `contacts` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the page was initially loaded, measured in milliseconds. For example:
`1471564788642` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl` . For example:
`/sObject/0064100000JXITSAA5/view` .

```
ParentUiElement

PreviousPageAppName

PreviousPageContext

PreviousPageObjectIdentifier

PreviousPageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent scope of the page element where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the previous application that the user accessed from the App Launcher.
For example: `LightningSales` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context of the previous page where the event occurred. For example:
`clients:cardsContainer` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique previous page object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The previous page object type of the event. For example: `task`, `contacts` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
PreviousPageUrl

RequestIdentifier

SdkAppVersion

SessionKey

TargetUiElement

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened. For example: `/sObject/006410000` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK application version number. For example: `5.0` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started. For example: `cdd09305cb6babf34059e27f70e47f1b11dec868` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The target page element where the event occurred. For example: `label bBody`
`truncate`, `tabitem-link` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
Timestamp

UiEventSequenceNumber

UiEventTimestamp

UserAgent

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
double

**Properties**
Filter, Nillable, Sort

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
An auto-incremented sequence number of the current event since the session started.

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
The 15-character ID of the user accessing Salesforce services through the UI or API. For
example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

Possible values are:

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

### LightningPrfmEventLog

Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This object is available in
API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AppName

```

**Type**
string


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

```
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
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

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

**Example**

```
  United States/California

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
ConnectionType

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

```
DevicePlatform

DeviceSessionIdentifier

Duration

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The duration in milliseconds since the page start time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Example**

```
                   GeJCsym5eyvtEK2I

```

```
MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

PageStartTime

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number.

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
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The time when the page was initially loaded, measured in milliseconds.

```
PageUrl

PreviousPageUrl

RequestIdentifier

SdkAppVersion

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened.

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
Mobile SDK application version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the session ID to allow tracking of all events in a session.


Standard Objects LightningPrfmEventLog

**Field** **Details**

```
Timestamp

UiEventIdentifier

UiEventSource

UiEventTimestamp

UiEventType

UserAgent

```

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
Id of the Lightning event type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source of the performance event.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp of when event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of performance event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The client user agent string.


### Standard Objects LightningToggleMetrics

**Field** **Details**

```
UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

### LightningToggleMetrics

Represents users who switched from Lightning Experience back to Salesforce Classic. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User switched from Lightning Experience to Salesforce Classic or from Salesforce
Classic to Lightning Experience.


### Standard Objects LightningUsageByAppTypeMetrics

**Field Name** **Details**

```
MetricsDate

RecordCount

UserId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user switched.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of user switches.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who switched.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### LightningUsageByAppTypeMetrics

Represents number of users on Lightning Experience and Salesforce Mobile. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.


### Standard Objects LightningUsageByBrowserMetrics

Fields

**Field Name** **Details**

```
AppExperience

MetricsDate

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s app (Lightning Experience or Salesforce Mobile).

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user accessed Lightning Experience or Salesforce Mobile.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId for user accessing Lightning Experience or Salesforce Mobile.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### LightningUsageByBrowserMetrics

Represents Lightning Experience usage grouped by user’s browser. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects LightningUsageByPageMetrics

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
Browser

MetricsDate

PageName

TotalCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Browser used to access Lightning Experience.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user accessed Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Page user viewed in Lightning Experience.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of pages accessed in Lightning Experience.

### LightningUsageByPageMetrics

Represents standard pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects LightningUsageByPageMetrics

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
MetricsDate

PageName

TotalCount

UserId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user viewed page in Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of page user viewed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of pages viewed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who viewed page.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects LightningUsageByFlexiPageMetrics

See Also

For more information about `LightningUsageByPageMetrics` [syntax and considerations, see REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_lightning_usagebypagemetrics.htm)
[Lightning Usage by Page.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_lightning_usagebypagemetrics.htm)

### LightningUsageByFlexiPageMetrics

Represents custom pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
FlexiPageNameOrId

FlexiPageType

MetricsDate

TotalCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name or Id of custom page user viewed in Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Custom page type.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user viewed page in Lightning Experience.

**Type**
int


### Standard Objects LightningExitByPageMetrics

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of custom pages viewed.

### LightningExitByPageMetrics

Represents frequency metrics about the standard pages within which users switched from Lightning Experience to Salesforce Classic.
This object is available in API version 44.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
MetricsDate

PageName

RecordCount

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date that the data was recorded.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the page from which the user switched from Lightning Experience
to Salesforce Classic.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects LinkedArticle

**Field Name** **Details**

**Description**
The number of records per user and page.

```
UserId

### LinkedArticle

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of the user who views page.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents a knowledge article that is attached to a work order, work order line item, or work type. This object is available in API version
37.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Knowledge must be enabled in your org. Field Service must be enabled. Only users that have access to the Knowledge article and the
parent record linked to it can access this object.

In Knowledge in Salesforce Classic, only Field Service objects such as Work Order, Work Type, and Work Order Line Item are supported
for linked articles. In Lightning Knowledge, other social objects such as Chat, Messaging, Voice Call, and Social Post are supported for
linked articles.

To call `update()` to attach or detach articles, enable the Read user permission on the Knowledge object and the Edit user permission
on the object whose article you update. Available in API version 58.0 and later.


Standard Objects LinkedArticle

Fields

**Field Name** **Details**

```
CurrencyIsoCode

KnowledgeArticleId

KnowledgeArticleVersionId

LinkedEntityId

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Knowledge article attached to the record. The label in the user
interface is Knowledge Article ID.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The version of the Knowledge article attached to the record. This field lists the
title of the attached version and links to the version. The label in the user interface
is Article Version.

When you attach an article to a work order, that version of the article stays
associated with the work order, even if later versions are published. If needed,
you can detach and reattach an article to a work order to link the latest version.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that the Knowledge article is attached to. The label in the
user interface is Linked Record ID.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects LinkedArticleFeed

**Field Name** **Details**

**Description**
The title of the article. The label in the user interface is Article Title.

```
RecordTypeId

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the article’s record type, if used. This field is only available for Lightning
Knowledge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of record that the Knowledge article is attached to. For
example, work order. The label in the user interface is Linked Object Type.

Admins can customize linked articles’ page layouts, fields, validation rules, and more from the Linked Articles page in Setup.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LinkedArticleChangeEvent (API version 62.0)**
Change events are available for the object.

### **LinkedArticleFeed**

Feed tracking is available for the object.

**LinkedArticleHistory**

History is available for tracked fields of the object.

### LinkedArticleFeed

Represents the comment feed on a linked article. This object is available in API version 39.0 and later.

For additional information about feeds, see FeedItem on page 2550.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LinkedArticleFeed

Special Access Rules

Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
BestCommentId

Body

CommentCount

InsertedById

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

**Type**
textarea

**Properties**
Nillable, Sort

**Description**
The body of the feed item. Required when `Type` is `TextPost` or `AdvancedTextPost` .
Optional when `Type` is `ContentPost` or `LinkPost` .

Although a value for `Body` is not required for the `ContentPost` type, an attachment
is required. If an attachment isn’t present, the type changes to `TextPost` or
`AdvancedTextPost`, depending on the API version. `TextPost` and
`AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the body of
rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.


Standard Objects LinkedArticleFeed

**Field** **Details**

```
IsRichText

LikeCount

LinkUrl

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text feed comment
using SOAP API, set `IsRichText` to `true` and escape HTML entities from the body.
Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

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

Note: In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a plain-text
representation.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Nillable, Sort


Standard Objects LinkedArticleFeed

**Field** **Details**

**Description**
The URL of a `LinkPost` .

```
ParentId

RelatedRecordId

Title

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object type to which the feed item is related. For example, set this field to a `UserId`
to post to someone’s profile feed, or an `AccountId` to post to a specific account.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC thanks posts,
it’s the ID of the WorkThanks object associated with a `RypplePost` . This field is typically
null for all posts except `ContentPost` and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed with `Type`
set to `ContentPost` .

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is the URL and
this field is the link name. The `Title` field can be updated on posts of `Type`
`QuestionPost` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`, and `TextPost`, don’t
create feed items of other types directly from the API.

**•** `ActivityEvent` —indirectly generated event when a user or the API adds a Task
associated with a feed-enabled parent record (excluding email tasks on cases). Also
occurs when a user or the API adds or updates a Task or Event associated with a case
record (excluding email and call logging).


Standard Objects LinkedArticleFeed

**Field** **Details**

For a recurring Task with CaseFeed disabled, one event is generated for the series only.
For a recurring Task with CaseFeed enabled, events are generated for the series and each
occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement and, in
Lightning Experience as of API version 39.0 and later, when a user shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric or gauge
exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a dashboard
snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post. Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply only to
CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through the user
interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment for a case
object.

**•** `ChangeStatusPost` —generated event when a user changes the status of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved to a case.

**•** `EmailMessageEvent` —generated event when an email related to a case object is
sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or reaches
violation status.


### Standard Objects LinkedArticleHistory

**Field** **Details**

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData` and
`ContentFileName` .

### LinkedArticleHistory

Represents the history of changes made to tracked fields on a linked article. This object is available in API version 37.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Knowledge must be enabled in your org.

Fields

**Field Name** **Details**

```
DataType

Field

LinkedArticleId

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
reference

**Properties**
Filter, Group, Sort


### Standard Objects ListEmail

**Field Name** **Details**

**Description**
The ID of the tracked linked article. The history is displayed on the detail page for
this record.

```
NewValue

OldValue

### ListEmail

```

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

Represents a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. When the list email is sent, the
recipients are generated by combining recipients in ListEmailIndividualRecipients and ListEmailRecipientSource. Duplicate and other
invalid recipients are removed. The result is the recipients sent any given list email. ListEmail has a one-to-many relationship with
### ListEmailRecipientSource and ListEmailIndividualRecipient. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the action cadence step that generated a list email record. Used for automated
emails in Sales Engagement.


Standard Objects ListEmail

**Field** **Details**

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

This field is available in API version 54.0 and later.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
CampaignId

ClickThroughRate

ClickToOpenRatio

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related campaign.

This field is available in API version 42.0 and later.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of visitors who click links contained in emails delivered (sent minus bounces)
to them. Multiple clicks for a same link are counted.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects ListEmail

**Field** **Details**

**Description**

The number of unique clicks divided by unique HTML opens.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

```
DeliveryRate

EmailContentId

FromAddress

FromName

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of the emails that were delivered compared to the number that bounced
(soft and hard). Note: this data includes emails that were delivered to the recipient's spam
folder.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the email content record associated with the list email.

This field is available in API version 50.0 or later. To access this field, your org must use Account
Engagement and users need the CRM User or Sales User permission set.

**Type**
textarea

**Properties**
Create, Filter, Update

**Description**
Read-only except when the list email is in a draft state. Validated against user’s addresses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Read-only except when the list email is in a draft state. Validated against user’s addresses.
This field is null for emails sent from Account Engagement.


Standard Objects ListEmail

**Field** **Details**

```
HasAttachment

HtmlBody

IsTracked

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Defaulted on create and update. Value is `true` if the list email has an attachment.
This field is null for emails sent from Account Engagement.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the list email. This field is null for emails sent from Account Engagement.

List emails can contain up to 32,000 characters for the body. These limits include visible
characters and other characters in the email, including markup.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if email tracking was on when the list email was sent. This field is blank for emails
sent from Account Engagement and synced to Salesforce. This field is null for emails sent
from Account Engagement.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when the current user last viewed a record that is related to
this list email. This field is null for emails sent from Account Engagement.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed. This
field is null for emails sent from Account Engagement.


Standard Objects ListEmail

**Field** **Details**

```
Name

OpenRate

OptOutRate

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Read-only except when the list email is in a draft state.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of unique HTML opens compared to the total number of emails delivered
(sent minus bounces).

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of users that have opted out compared to the total number of emails sent.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
References Group and User. This field is null for emails sent from Account Engagement.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ListEmail

**Field** **Details**

```
ProgramName

ScheduledDate

SentVia

SpamComplaintRate

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**

The name of an Engagement Studio program where an automated email originates. Reserved
for future use.

This field is available in API version 46.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
dateTime

**Properties**
CreateFilter, Nillable, Sort, Update

**Description**
Read-only. If null and `Status` is set to Scheduled` defaults to created time.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates whether the email was sent from Salesforce or Account Engagement. The allowed
values are `Salesforce` or `Pardot` or `MessagingService` .

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of spam complaints compared to the total number of emails sent.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects ListEmail

**Field** **Details**

**Description**
Read-only except when the list email is in a draft state.

Changing the status to Scheduled causes the list email to be sent.

Valid values:

**•** `Draft`

**•** `Scheduled`

**•** `Sent`

**•** `Limit Error`

**•** `Canceled`

**•** `Running`

```
Subject

TextBody

TotalDelivered

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
Read-only except when the list email is in a draft state. This field is null for emails sent from
Account Engagement.

List emails can contain up to 3,000 characters for the subject. These limits include visible
characters and other characters in the email, including markup.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Read-only except when the list email is in a draft state. This field is null for emails sent from
Account Engagement.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The total number of emails minus hard and soft bounces. Note: this data includes emails
that were delivered to the recipient's spam folder.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


Standard Objects ListEmail

**Field** **Details**

```
TotalHardBounced

TotalOpens

TotalOutOfOffice

TotalReplies

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of emails that permanently bounced back to the sender because the
address is invalid. A hard bounce can occur because the domain name doesn't exist or
because the recipient is unknown.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a prospect’s email client loaded the images in the HTML version
of the email. We also record an open if the prospect clicks a link within the HTML or text
email without downloading images. A click indicates that they viewed the message. Some
email clients (Outlook, Apple Mail, Thunderbird) don’t display images by default. Account
Engagement counts an open each time the images load.

This field is available in API version 41.0 and later. To access this field. users need the Sales
Engagement User permission set or your org must use Account Engagement and users need
the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of replies received with an out-of-office message.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of replies received.


Standard Objects ListEmail

**Field** **Details**

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

```
TotalSent

TotalSoftBounced

TotalSpamComplaints

TotalTrackedLinkClicks

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only. The total number of list emails sent, including bounced, opted-out, and invalid
To: addresses.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a recipient’s mail server acknowledged the email, but returned it
to the sender. Sometimes it is because the recipient's mailbox is full or the mail server is
temporarily unavailable. A soft bounce message can sometimes be deliverable at another
time. After 5 soft bounces, Account Engagement opts the prospect out of emails.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of prospects that reported the email as spam.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times prospects clicked a link in the email.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


Standard Objects ListEmail

**Field** **Details**

```
Type

UniqueClickThroughRate

UniqueOpens

UniqueOptOuts

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

The type of email sent: list email or automated email. Reserved for future use.

This field is available in API version 46.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of visitors who clicked a link contained in an email.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of prospects who loaded the images in the HTML version of the email. The
Unique Opens category counts each recipient one time only, even if the prospect loaded
images several times.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Unique opt-outs represent the total number of prospects that have clicked the link to
unsubscribe or opted out of all emails in the Email Preference Center. These prospects are
removed from future email sends.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


### Standard Objects ListEmailIndividualRecipient

**Field** **Details**

```
UniqueReplies

UniqueTrackedLinkClicks

```

Associated Objects

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique replies.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a prospect clicked a link in the email. This metric doesn’t include multiple
clicks of the same link.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ListEmailOwnerSharingRule**

Sharing rules are available for the object.

**ListEmailShare**

Sharing is available for the object.

### ListEmailIndividualRecipient

For a list email in Salesforce, represents a recipient. Each record represents a link from a list email to exactly one recipient for that list
email. Recipients can be contacts, leads, or campaign members. Has a one-to-many relationship with ListEmail. This object is available
in API version 44.0 and later.

The visibility and accessibility of this object is inherited from the related list email.


Standard Objects ListEmailIndividualRecipient

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceStepTrackerId

CurrencyIsoCode

ListEmailId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Understand which action cadence step tracker the list email individual recipient is related
to. Used for automated emails in Sales Engagement.

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

This field is available in API version 54.0 and later.

**Relationship Name**
ActionCadenceStepTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR` (Euro)

**•** `INR` (Indian Rupee)

**•** `USD` (US Dollars)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.


### Standard Objects ListEmailSentResult

**Field** **Details**

This is a relationship field.

**Relationship Name**
### ListEmail

**Relationship Type**
Lookup

**Refers To**
### ListEmail

```
Name

RecipientId

```

Usage

### ListEmailSentResult

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the list email recipient source.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
the contact, lead, person account, or campaign member ID of the individual list email recipient.

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
CampaignMember, Contact, Lead

Represents the results of a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. It contains transport
headers and information specific to the associated send action. This object is available in API version 67.0 and later.

Example:

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained
certain terms to avoid any effect on customer implementations.


Standard Objects ListEmailSentResult

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceStepTrackerId

ActivityId

EmailAdress

FirstClickedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the action cadence step tracker related to the individual recipient of the list email.
Used for automated emails in Sales Engagement.

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

**Relationship Name**
ActionCadenceStepTracker

**Refers To**
ActionCadenceStepTracker

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The task representation of the sent email.

**Relationship Name**
Activity

**Refers To**
Task

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The email address of the recipient.

**Type**
dateTime


Standard Objects ListEmailSentResult

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp for when the email link was first clicked.

```
FirstOpenedDate

HasReply

Headers

isClicked

IsLinkTracked

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp for when the email was first opened.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email has a reply ( `true` ) or not ( `false` ) The default value is `false` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The internet message headers of the email used for debugging and email threading purposes.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the individual copy of the list email is clicked `true` or `false` . The
default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates whether there are any URLs in the email that can be tracked ( `true` ) or not ( `false` ).
The default value is `false` .


Standard Objects ListEmailSentResult

**Field** **Details**

```
IsOpenTracked

IsOpened

LastClickedDate

LastOpenedDate

ListEmailId

```

**Type**
boolean

**Properties**
Create, Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is trackable ( `true` ) or not ( `false` ). The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email has been opened ( `true` ) or not ( `false` ). The default value is
`false` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the email was last clicked.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the email was last opened.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the list email that's associated with the email.

**Relationship Name**
ListEmail

**Relationship Type**
Master-detail

**Refers To**
ListEmail (the master object)


Standard Objects ListEmailSentResult

**Field** **Details**

```
MessageIdentifier

Name

Reason

RecipientId

Result

```

**Type**
string

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
The internet ID of an email.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the list email sent result.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the reason why a list email failed to send. Possible values are:

**•** `Bounced`

**•** `NoEmail`  - No Email Address

**•** `OptedOut`  - Opted Out

**•** `OutOfOffice`  - Out of Office

**•** `Restricted`

**•** `SoftBounced`  - Soft Bounced

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the individual list email recipient. This field is a polymorphic relationship field.

**Relationship Name**
Recipient

**Refers To**
Contact, Lead

**Type**
picklist


### Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted Picklist, Sort, Update

**Description**
Indicates the result of the sent list email. Possible values are:

**•** `Failed`

**•** `NotSent`

**•** `Sent`

```
ThreadIdentifier

```

**Type**
string

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
The thread ID of the email.

### ListEmailMonthlyMetric

Represents the monthly engagement metrics for a single list email. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllEmailsBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard and soft bounces that were triggered for this list email in the month.

This field is a calculated field.


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

```
AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received this list email in the month.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard bounces that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by the recipients of this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who opened this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of out-of-office replies that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Description**
The number of replies to this list email in the month.

```
AllEmailsSentCount

AllEmailsSoftBouncedCount

HardBounceTrackableSends

LinkClickTrackableSends

ListEmailId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients to whom this list email was sent in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total soft bounces that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with hard bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with link click tracking in the month.
Available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related list email.

This field is a relationship field.


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

```
Month

MonthInt

OpenTrackableSends

OutOfOfficeTrackableSends

ReplyTrackableSends

```

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
The number of recipients who were sent this list email with open tracking in the month.
Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with out-of-office tracking in the
month. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Description**
The number of recipients who were sent this list email with reply tracking in the month.
Available in API version 53.0 and later.

```
SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

TrackableSendOutOfOfficeRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with soft bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with hard bounce tracking, resulted
in a hard bounce in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who clicked on a link in this list email that was sent with link
click tracking in the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who opened this list email that was sent with open tracking in
the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom the list email, sent with out-of-office tracking, resulted
in an out-of-office reply in the month. Available in API version 54.0 and later.

This field is a calculated field.

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
The percentage of recipients for whom this list email, sent with reply tracking, resulted in a
reply in the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with soft bounce tracking, resulted
in a soft bounce in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who clicked a link in this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened this list email in the month.

**Type**
int


### Standard Objects ListEmailRecipientSource

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to this list email in the month.

### ListEmailRecipientSource

For a list email in Salesforce, represents the dynamically defined sources of recipient email addresses. Each record represents a link to a
single list view or campaign that is examined when the list email is sent. Has a one-to-many relationship with ListEmail. This object is
available in API version 41.0 and later.

The visibility and accessibility of this object is inherited from the related list email.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `getDeleted()`, `getUpdated()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ListEmailId

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.

This is a relationship field.

**Relationship Name**
### ListEmail

**Relationship Type**
Lookup

**Refers To**
### ListEmail

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects ListView

**Field** **Details**

**Description**
The auto-generated name of the list email recipient source.

```
SourceListId

SourceType

### ListView

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The id of a list view to send the list email to. Read-only except when list email is
in draft state.

This is a polymorphic relationship field.

**Relationship Name**
SourceList

**Relationship Type**
Lookup

**Refers To**
Campaign, ListView, Topic

**Type**
reference

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Read-only except when list email is in draft state.

Valid values:

**•** Include

Represents a list view. A list view shows a set of records for an object, based on specific criteria. This object is available in API version 32.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`


Standard Objects ListView

Fields

**Name** **Details**

```
DeveloperName

IsSoqlCompatible

LastModifiedById

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The fully qualified developer name of the list view.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the list view can be used with SOQL..

**Type**
User

**Properties**
Filter, Sort

**Description**
The ID of the user who last modified the list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last referenced, with a precision of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last viewed, with a precision of one second.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects ListViewChart

**Name** **Details**

**Description**
The name of the list view.

```
NamespacePrefix

SobjectType

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the list view.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The API name of the sObject for the list view.

Use this object to retrieve the metadata for a pipeline inspection view.

### ListViewChart

Represents a graphical chart that’s displayed on Salesforce for Android, iOS, and mobile web list views. The chart aggregates data that
is filtered based on the list view that’s currently displayed. This object is available in API version 33.0 and later and is accessible by portal
users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Name** **Description**

```
AggregateField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update


Standard Objects ListViewChart

**Name** **Description**

**Description**
The field that’s used for calculating data on each group. `AggregateField` can’t be the
same as `GroupingField` .

```
AggregateType

ChartType

DeveloperName

GroupingField

Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The type of calculations to run on each group. The supported `AggregateType` values are
`Count`, `Sum`, and `Avg` .

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist,Retrieve, Sort, Update

**Description**
The type of chart to create. The supported chart types are horizontal bar chart, vertical bar chart,
and donut chart.

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The fully qualified developer name of the chart.

Note: Only users with View DeveloperName OR View Setup and Configuration permission
can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The field that’s used to divide the data into collections. The field must be supported by SOQL
`GROUP BY` functionality. `GroupingField` can’t be the same as `AggregateField` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ListViewChartInstance

**Name** **Description**

**Description**
The language of the `MasterLabel` .

```
MasterLabel

OwnerId

SobjectType

```

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The label for the chart.

**Type**
reference

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The ID of the user who owns the chart.

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
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort

**Description**
The API name of the sObject for the chart.

### ListViewChartInstance

Retrieves metadata for all standard and custom charts for a given entity in context of a given list view. This object is available in API
versions 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ListViewChartInstance

Fields

**Field Name** **Details**

```
AggregateField

AggregateType

ChartType

DataQuery

DataQueryWithoutUserFilters

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The field that’s used for calculating data on each group. `AggregateField`
can’t be the same as `GroupingField` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of calculations to run on each group. The supported `AggregateType`
values are `Count`, `Sum`, and `Avg` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of chart to create. The supported chart types are horizontal bar chart,
vertical bar chart, and donut chart.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart,
without user filters.

Available in API v43.0 and later.


Standard Objects ListViewChartInstance

**Field Name** **Details**

```
DeveloperName

ExternalId

GroupingField

IsDeletable

IsEditable

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the chart. This name can contain only underscores and alphanumeric
characters, and must be unique in your org. It must begin with a letter, not include
spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a
managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The field that’s used to divide the data into collections. The field has to be
supported by SOQL `GROUP BY` functionality. `GroupingField` can’t be the
same as `AggregateField` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the chart can be deleted.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ListViewChartInstance

**Field Name** **Details**

**Description**
Indicates if the chart can be edited. Standard charts are not editable.

```
IsLastViewed

Label

ListViewChartId

ListViewContextId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if a chart is the last viewed by a user.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The display name of the chart.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the chart created by a user. For standard charts, this is null.

This is a relationship field.

**Relationship Name**
ListViewChart

**Relationship Type**
Lookup

**Refers To**
ListViewChart

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the list view in context of which the chart is generated. Required to query
`ListViewChartInstance` .

This is a relationship field.

**Relationship Name**
ListViewContext


### Standard Objects LiveAgentSession

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
ListView

```
SourceEntity

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the entity to which the chart is related. Required to query
`ListViewChartInstance` .

**Example 1. Retrieve all custom and standard charts for Account entity for All Accounts list view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextId=’00BR0000000U8Hr’

```

**Example 2. Retrieve metadata for a specific custom chart by ID for Account entity and All Accounts list view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextID=’00BR0000000U8Hr’ and ListViewChartId=’0DdR00000004CBxKAM’

```

**Example 3. Retrieve metadata for a specific standard chart by its developer name for Account entity and All Accounts list**
**view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextID=’00BR0000000U8Hr’ and DeveloperName=’AccountsByIndustry’

### LiveAgentSession

```

This object is automatically created for each Chat session and stores information about the session. This object is available in API versions
28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.


Standard Objects LiveAgentSession

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`

Fields

**Field Name** **Details**

```
AgentId

ChatReqAssigned

ChatReqDeclined

ChatReqEngaged

ChatReqTimedOut

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the agent associated with the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that were assigned to an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that were declined by an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chats in which an agent was engaged during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that timed out in an agent’s queue during a session.


Standard Objects LiveAgentSession

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

LoginTime

LogoutTime

Name

NumFlagLoweredAgent

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time an agent logged in during the session.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time an agent logged out during a session.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookupSort

**Description**
The name of the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the agent.


Standard Objects LiveAgentSession

**Field Name** **Details**

```
NumFlagLoweredSupervisor

NumFlagRaised

OwnerId

TimeAtCapacity

TimeIdle

TimeInAwayStatus

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the supervisor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags raised by the agent.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with the maximum number of chats in his
or her queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent idle during the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects LiveAgentSessionHistory

**Field Name** **Details**

**Description**
The amount of time an agent spent with a status of “Away” during a session.

```
TimeInChats

TimeInOnlineStatus

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent engaged in chats during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with a status of “Online” during a session.

Use this object to query and manage chat session records.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

### **LiveAgentSessionHistory**

History is available for tracked fields of the object.

**LiveAgentSessionOwnerSharingRule**

Sharing rules are available for the object.

**LiveAgentSessionShare**

Sharing is available for the object.

### LiveAgentSessionHistory

This object is automatically created for each Chat session and stores information about changes made to the session. This object is
available in API versions 28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LiveAgentSessionHistory

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
DataType

Field

LiveAgentSessionId

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
The name of the field that was changed in a session record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the session record that was changed.

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
The original value of the field that was changed.


### Standard Objects LiveAgentSessionShare

Usage

Use this object to identify changes to chat session records.

### LiveAgentSessionShare

This object is automatically created for each Chat session and stores information about the session. This object is available in API versions
28.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

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
Level of access that the User or Group has to the LiveAgentSession. The possible
values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for chat transcripts.

**Type**
reference


### Standard Objects LiveChatBlockingRule

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any.

```
RowCause

UserOrGroupId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values can include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the LiveAgentSession with them.

**•** `Owner` —The User is the owner of the LiveAgentSession or is in a role above
the LiveAgentSession owner in the role hierarchy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that has been given access to the LiveAgentSession.

This object lets you determine which users and groups can view and edit LiveAgentSession records owned by other users.

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

### LiveChatBlockingRule

Represents a rule for blocking chat visitors’ IP addresses from starting new chats with agents. This object is available in API version 34.0
and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`


Standard Objects LiveChatBlockingRule

Special Access Rules

To create a new rule, you must be logged in with the “Customize Application” permission or as a system administrator.

Fields

**Field Name** **Details**

```
Description

DeveloperName

FromIpAddress

```

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the blocking rule—for example, the reason why the given IP
address or range of addresses is being banned from starting new chats.

**Type**
string

**Properties**
Create, Filter, Group, Sort

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

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The IP address of the user that you want to block, or the beginning of the range
of IP addresses you want to block. If you want to block a range of IP addresses,
indicate the end of the range in the `ToIpAddress` field. If you don’t indicate


### Standard Objects LiveChatObjectAccessConfig

**Field Name** **Details**

an IP address in the `ToIpAddress` field, the only IP address that will be blocked
is the IP address in the `FromIpAddress` field.

```
Language

MasterLabel

ToIpAddress

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Label for the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
(Optional) The end of the range of IP addresses that you want to block. The range
begins with and includes the IP address in the `FromIpAddress` field, and it
ends with and includes the IP address in the `ToIpAddress` field.

Use this object to query and manage rules for blocking customers from starting new chats with agents.

### LiveChatObjectAccessConfig

Represents the action you can perform on a specified object by the Chat API. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.


Standard Objects LiveChatObjectAccessConfig

Fields

**Field** **Details**

```
AccessType

ParentId

SobjectType

```

SEE ALSO:

LiveChatObjectAccessDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The API action you can perform on the object specified in `SobjectType` .

Possible values are:

**•** `Create`

**•** `Find`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated LiveChatObjectAccessDefinition record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
LiveChatObjectAccessDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The object that the action specified by `AccessType` applies to.

Possible values are all standard and custom objects. Custom objects are available as picklist
values in API version 55.0 and later.


### Standard Objects LiveChatObjectAccessDefinition LiveChatObjectAccessDefinition

Represents the parent record for one or more LiveChatObjectAccessConfig objects. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language for labels displayed
in an application.

Possible values are:

**•** `da` —Danish


### Standard Objects LiveChatButton

**Field** **Details**

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

```
MasterLabel

### LiveChatButton

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object's record. This display value is the internal label that doesn’t get
translated.

Represents a button that allows visitors to request chats with Chat users. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects LiveChatButton

Fields

**Field Name** **Details**

```
Animation

AutoGreeting

ChasitorIdleTimeout

ChasitorIdleTimeoutWarning

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of animation used when an automated chat invitation appears on-screen.
For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Appear`

**•** `Custom`

**•** `Fade`

**•** `Slide`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

Note: A greeting message in the `AutoGreeting` field of the
LiveChatButton object overrides individual users’ greeting messages in
the `AutoGreeting` field in the LiveChatUserConfig object.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before the
chat times out.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before a
warning appears and a timer begins a countdown. This value must be shorter


Standard Objects LiveChatButton

**Field Name** **Details**

than the `ChasitorIdleTimeout` value. We recommend at least 30 seconds
shorter.

```
ChatPageId

CustomAgentName

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page that contains the custom chat
window code.

This field is a relationship field.

**Relationship Name**
ChatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The custom name of the agent associated with the button. Available in API version
29.0 and later.

Note: A custom agent name in the `CustomAgentName` field of the
LiveChatButton object overrides individual users’ custom agent name in
the `CustomAgentName` field in the LiveChatUserConfig object.

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


Standard Objects LiveChatButton

**Field Name** **Details**

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

```
HasQueue

InviteEndPosition

InviteImageId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether or not to allow queing incoming chat requests until an
agent is available.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation ends.

Note: You don’t need to select an end position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`

**•** `BottomLeft`

**•** `BottomRight`

**•** `Center`

**•** `Left`

**•** `Right`

**•** `Top`

**•** `TopLeft`

**•** `TopRight`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects LiveChatButton

**Field Name** **Details**

**Description**
The record ID of the static image resource displayed on your automated chat
invitation. For automated chat invitations only. Available in API version 29.0 and
later.

This field is a relationship field.

**Relationship Name**
InviteImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

```
InviteStartPosition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation begins.

Note: You don’t need to select a start position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`

**•** `BottomLeft`

**•** `BottomLeftBottom`

**•** `BottomLeftLeft`

**•** `BottomRight`

**•** `BottomRightBottom`

**•** `BottomRightRight`

**•** `Left`

**•** `Top`

**•** `Right`

**•** `TopLeft`

**•** `TopLeftLeft`

**•** `TopLeftTop`

**•** `TopRight` —Top Right

**•** `TopRightRight`

**•** `TopRightTop`


Standard Objects LiveChatButton

**Field Name** **Details**

```
IsActive

IsRoutingFlowEnabled

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For automated chat invitations, specifies whether an automated chat invitation
is active or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether routing flow is enabled or not.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the chat.

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


Standard Objects LiveChatButton

**Field Name** **Details**

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

NumberOfReroutingAttempts

OfflineImageId

OnlineImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the chat button.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of times a chat request can be rerouted to available agents
if all agents reject the chat request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
offline (inactive).

This field is a relationship field.

**Relationship Name**
OfflineImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
online (active).


Standard Objects LiveChatButton

**Field Name** **Details**

This field is a relationship field.

**Relationship Name**
OnlineImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

```
OptionsHasChasitorIdleTimeout

OptionsHasInviteAfterAccept

OptionsHasInviteAfterReject

OptionsHasRerouteDeclinedRequest

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether Customer Time-Out is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has accepted a prior automated chat invitation ( `true` ) or not
( `false` ). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has rejected a prior automated chat invitation ( `true` ) or not
( `false` ). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request that has been rejected by all available agents
should be rerouted to available agents again ( `true` ) or not ( `false` ).


Standard Objects LiveChatButton

**Field Name** **Details**

```
OptionsIsAutoAccept

OptionsIsInviteAutoRemove

OverallQueueLength

PerAgentQueueLength

PostchatPageId

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request should be automatically accepted by the agent
it’s assigned to ( `true` ) or not `false` ). For chat buttons and automated chat
invitations with `RoutingType` set to `Most Available` or `Least`
`Active` . Available in API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation should be automatically removed
from the screen after a certain amount of time ( `true` ) or not ( `false` ). For
automated chat invitations only. Available in API version 29.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue for each agent with
the required skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed when the chat ends.

This field is a relationship field.


Standard Objects LiveChatButton

**Field Name** **Details**

**Relationship Name**
PostchatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

```
PostchatUrl

PrechatFormPageId

PrechatFormUrl

PushTimeout

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to after the chat ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed before the chat begins.

This field is a relationship field.

**Relationship Name**
PrechatFormPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to before the chat begins.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects LiveChatButton

**Field Name** **Details**

**Description**
The number of seconds an agent has to answer a chat request before it’s routed
to the next available agent.

```
QueueId

RoutingConfigurationId

RoutingType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the queue used for this chat button.

This field is a relationship field.

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the routing configuration used for this chat button.

This field is a relationship field.

**Relationship Name**
RoutingConfiguration

**Relationship Type**
Lookup

**Refers To**
QueueRoutingConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How chat requests are routed to agents. The values are:

**•** `Choice` —Incoming chat requests are added to the queue in Live Agent in
the Salesforce console and are available to any agent with the required skill.


Standard Objects LiveChatButton

**Field Name** **Details**

**•** `Least Active` —Incoming chats are routed to the agent with the
required skill who has the fewest active chats.

**•** `Most Available` —Incoming chats are routed to the agent with the
required skill and the greatest difference between chat capacity and active
chat sessions. For example, if Agent A and Agent B each have a chat capacity
of five, and Agent A has three active chat sessions while Agent B has one,
incoming chats will be routed to Agent B.

**•** `Omni` —Incoming chats are routed using Omni-Channel queues.

```
SiteId

SkillId

TimeToRemoveInvite

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the site used for loading static resources and custom VisualForce
pages.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the skill used to route incoming chat requests. To associate
multiple skills with a chat button, reference one skill in the `SkillId` field and
use LiveChatButtonSkill junction objects for the remaining skills.

This field is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
int


Standard Objects LiveChatButton

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds an automated invitation stays on-screen before it is
automatically removed. For automated chat invitations only. Available in API
version 29.0 and later.

```
Type

WindowLanguage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of element to display to customers.

Possible values are:

**•** `Invite` —Automated invitation

**•** `Standard` —Chat button

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for standard chat windows. Custom chat windows use the
language of the user’s browser.

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


### Standard Objects LiveChatButtonDeployment

**Field Name** **Details**

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

Usage

Use this object to query and manage chat buttons and automated chat invitations.

### LiveChatButtonDeployment

Associates an automated chat invitation with a specific deployment. This object is available in API versions 28.0 and later.

Supported Calls

`create()`, `delete()query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
ButtonId

DeploymentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the automated invitation associated with the deployment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the deployment that will feature the automated invitation.

Use this object to associate automated chat invitations with specific deployments.


### Standard Objects LiveChatButtonSkill LiveChatButtonSkill

Represents all the skills available to a LiveChatButton except the one currently assigned. To retrieve the skill currently assigned, query
LiveChatButton. This object is available in API version 25.0 and later.

Supported Calls

`create()`, `delete()`, `update()`, `query()`

Fields

**Field Name** **Details**

```
ButtonID

SkillID

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the button.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.

Use this object to assign a specific skill to a specific button for multi-skill routing. For example:

```
String myButtonId = " button_Id ";

String myButtonDevName = " button_DeveloperName ";

List<String> skillIds = new List<String>();

//Get one skill ID from button

for(LiveChatButton lcb : [SELECT SkillId FROM LiveChatButton WHERE DeveloperName =:

myButtonDevName]) {

   skillIds.add(lcb.SkillId);

}

//Get remaining skills from LiveChatButtonSkill join object

for(LiveChatButtonSkill lcbs : [SELECT SkillID FROM LiveChatButtonSkill WHERE ButtonId =:

myButtonId]) {

   skillIds.add(lcbs.SkillId);

}

```


### Standard Objects LiveChatDeployment

```
   //Retrieve all skills into a single list

   List<Skill> skills = [SELECT Id, DeveloperName FROM Skill WHERE Id IN :SkillIds];

### LiveChatDeployment

```

Represents the general settings for deploying Live Agent on a website. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
BrandingId

ConnectionTimeoutDuration

ConnectionWarningDuration

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource that’s displayed in the chat window.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before the chat times out, in seconds.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before a time-out warning is displayed to the agent,
in seconds.

**Type**
string

**Properties**
Create, Filter, Group, Sort


Standard Objects LiveChatDeployment

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
Domains

HasTranscriptSave

Language

MasterLabel

```

**Type**
textarea

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Nillable, Sort (unavailable
in API version 25.0 and later)

**Description**
A comma-separated list of domains the deployment is allowlisted for. Leave this
blank to allow the deployment to be used on any domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether visitors can download and save transcripts from the chat
window.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the deployment.

**Type**
string


Standard Objects LiveChatDeployment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the deployment

```
MobileBrandingId

OptionsHasPrechatApi

SiteId

WindowTitle

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource displayed in the mobile version of the
chat window.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether developers can access the Pre-Chat API.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the site used for loading static resources.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The text displayed in the title bar of the browser window used to launch the chat
window.

Use this object to query and manage live chat deployments.


### Standard Objects LiveChatSensitiveDataRule LiveChatSensitiveDataRule

Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). This object is available in
API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `update()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
ActionType

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action to take on the text (remove or replace) when the sensitive data rule
is triggered.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the sensitive data rule—for example, “Block social security
numbers.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the


Standard Objects LiveChatSensitiveDataRule

**Field Name** **Details**

object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
EnforceOn

IsEnabled

Language

MasterLabel

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Determines the roles on which the rule is enforced. The value is determined
using bitwise OR operation. There are seven possible values:

**1.** Rule enforced on Agent

**2.** Rule enforced on Visitor

**3.** Rule enforced on Agent and Visitor

**4.** Rule enforced on Supervisor

**5.** Rule enforced on Agent and Supervisor

**6.** Rule enforced on Visitor and Supervisor

**7.** Rule enforced on Agent, Visitor, and Supervisor

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a sensitive data rule is active ( `true` ) or not ( `false` ). Default
value (if none is provided) is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the sensitive data rule.

**Type**
string


Standard Objects LiveChatSensitiveDataRule

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the sensitive data rule.

```
NamespacePrefix

Pattern

Priority

Replacement

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
prefix of the org for all objects that support it, unless an object is in an
installed managed package. In that case, the object has the namespace prefix
of the installed managed package. This field’s value is the namespace prefix
of the Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
textarea

**Properties**
Create, Update

**Description**
The pattern of text blocked by the rule. Written as a JavaScript regular expression
(regex).

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the priority level of a Chat.

**Type**
string


### Standard Objects LiveChatTranscript

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The string of characters that replaces the blocked text (if `ActionType`
_`Replace`_ is selected).

Usage

Use this object to mask or delete data of specified patterns, such as credit card, social security, phone and account numbers, or even
profanity.

### LiveChatTranscript

This object is automatically created for each Live Agent chat session and stores information about the session. This object is available in
API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Abandoned

AccountId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time in seconds an incoming chat request remained unanswered
by an agent before the chat was disconnected by the customer.

**Type**
ID

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with the chat transcript.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
AverageResponseTimeOperator

AverageResponseTimeVisitor

Body

Browser

BrowserLanguage

CaseID

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent’s average response time (in seconds) to chat messages from the visitor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s average response time (in seconds) to chat messages from the agent.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The browser the visitor used for the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The language of the visitor’s browser.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with the chat transcript.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
ChatDuration

ChatKey

ContactID

EndedBy

EndTime

IpAddress

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total duration of the chat in seconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
The session ID of the chat before it is persisted. `ChatKey` can be used with
advanced integrations in the Salesforce console. This field is available in API
version 25.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact associated with the chat transcript.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The way the chat was ended: by the operator, the visitor, or the system.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat ended.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Description**
The auto-populated visitor’s IP address. Do not edit. Create a custom field if you
need an IP address field for your use case.

```
IsChatbotSession

LastReferencedDate

LastViewedDate

LeadID

LiveChatButtonID

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the visitor is chatting with a chatbot ( `true` ) or not ( `false` ).

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced ( `LastReferencedDate` )
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the lead associated with the chat transcript.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatButton the chat session originated from.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
LiveChatDeploymentID

LiveChatVisitorID

Location

MaxResponseTimeOperator

MaxResponseTimeVisitor

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatDeployment the chat session originated from.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the visitor associated with the chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated best-guess approximation of the visitor’s location. Do not
edit.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took an agent to respond to a chat visitor’s
message.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took a customer to respond to an agent’s
message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Description**
The name of the transcript.

```
OperatorMessageCount

OwnerID

Platform

ReferrerUri

RequestTime

ScreenResolution

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by one or more agents during the chat.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the operator who participated in the chat last; for missed chats, this is
a system user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s operating system platform.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated URI where the chat request originated. Do not edit.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the visitor requested the chat.

**Type**
string


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s screen resolution.

```
SkillId

StartTime

Status

SupervisorTranscriptBody

UserAgent

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated record ID of the primary Skill associated with the
LiveChatButton the chat session originated from. Do not edit. To associate multiple
skills with a LiveChatTranscript, use LiveChatTranscriptSkill junction objects.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The final status of the chat: completed, missed, or blocked.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The text body of the supervisor’s chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s user agent string.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
VisitorMessageCount

VisitorNetwork

WaitTime

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by the visitor during the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The network or service provider the chat visitor used for the chat.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total amount of time in seconds a chat request was waiting to be accepted
by an agent.

Use this object to query and manage live chat transcripts.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 44.0)**
Change events are available for the object.

**LiveChatTranscriptFeed (API version 47.0)**
Feed tracking is available for the object.

**LiveChatTranscriptHistory**

History is available for tracked fields of the object.

**LiveChatTranscriptOwnerSharingRule (API version 29.0)**
Sharing rules are available for the object.

**LiveChatTranscriptShare**

Sharing is available for the object.


### Standard Objects LiveChatTranscriptEvent LiveChatTranscriptEvent

Captures specific events that occur over the lifetime of a chat. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
AgentId

Detail

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the agent associated with the event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Details associated with the event.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.


Standard Objects LiveChatTranscriptEvent

**Field Name** **Details**

```
LiveChatTranscriptId

Name

Time

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the live chat transcript associated with the event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the event.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the event happened.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of event that occurred.

**•** `Accept` —Accepted

**•** `AgentBlocked` —Blocked by Agent

**•** `AlertCriticalWaitChat` —Critical Wait Alert Time Reached

**•** `CancelBlocked` —Cancel (Blocked)

**•** `CancelNoAgent` —Cancel (No Agent)

**•** `CancelNoQueue` —Cancel (No Queue)

**•** `CancelVisitor` —Canceled by Visitor

**•** `ChasitorIdleTimeout` —Visitor Idle Time-Out

**•** `ChasitorIdleTimeoutWarningCleared` —Visitor Idle Time-Out
Warning Cleared

**•** `ChasitorIdleTimeoutWarningTriggered` —Visitor Idle Time-Out
Warning Appeared

**•** `ChatRequest` —Chat Requested


Standard Objects LiveChatTranscriptEvent

**Field Name** **Details**

**•** `ChatResumedAfterTransfer` —Chat resumed

**•** `ChatbotEndChat` —Chatbot end chat

**•** `ChatbotEndedChatByAction` —Conversation ended by automated
action

**•** `ChatbotEstablished` —Accepted by Chatbot

**•** `ChatbotNotEstablished` —Chatbot Request Failed

**•** `ChoiceRoute` —Routed (Choice)

**•** `ClearCriticalWaitChat` —Critical Wait Alert Cleared

**•** `ConferenceRequest` —Chat Conference Requested

**•** `ConferenceRequestCanceled` —Chat Conference Canceled

**•** `ConferenceRequestDeclined` —Chat Conference Declined

**•** `ConnectionTimeout` —Visitor connection timed out. Available in API
version 38.0 and later.

**•** `ConnectionWarning` —Warning that visitor hasn't been connected for
some time and that the connection times out soon. Available in API version
38.0 and later.

**•** `DeclineManual` —Decline (Manual)

**•** `DeclineTimeout` —Decline (Timeout)

**•** `EndAgent` —Ended by Agent

**•** `EndVisitor` —Ended by Visitor

**•** `Enqueue` —Queued

**•** `FileCanceledAgent` —File Transfer Canceled by Agent

**•** `FileCanceledChasitor` —File Transfer Canceled by Visitor

**•** `FileTransferFailure` —File Transfer Failure

**•** `FileTransferRequested` —File Transfer Requested by Agent

**•** `FileTransferSuccess` —File Transfer Success

**•** `FileTransferToChasitor` —File Transfer Initiated by Agent

**•** `FlagLoweredAgent` —Flag Lowered by Agent

**•** `FlagLoweredSupervisor` —Flag Lowered by Supervisor

**•** `FlagRaised` —Flag Raised

**•** `LeaveAgent` —Agent Left

**•** `LeaveVisitor` —Visitor Left

**•** `OperatorJoinedConference` —Agent Joined Conference

**•** `OperatorLeftConference` —Agent Left Conference

**•** `Other`

**•** `PushAssignment` —Routed (Push)

**•** `SensitiveDataAgent` —Sensitive data blocked (Agent)

**•** `SensitiveDataSupervisor` —Sensitive data blocked (Supervisor)

**•** `SensitiveDataVisitor` —Sensitive data blocked (Visitor)


### Standard Objects LiveChatTranscriptShare

**Field Name** **Details**

**•** `Transfer` —Transfer Accepted

**•** `TransferCancelled` —Transfer Request Canceled

**•** `TransferDeclined` —Transfer Request Declined

**•** `TransferRequest` —Transfer Requested

**•** `TransferToBotFailed` —Transfer to bot failed

**•** `TransferToButtonFailed` —Transfer to button failed

**•** `TransferToQueueFailed` —Transfer to queue failed

**•** `TransferredToBot` —Transferred to bot

**•** `TransferredToButton` —Transferred to button

**•** `TransferredToQueue` —Transferred to queue

**•** `TransferredToSbrSkill` —Transferred to skill

**•** `TransferredToSbrSkillFailed` —Transfer to skill failed

**•** `Unassigned`

Usage

Use this object to query and manage live chat transcript events.

Note: LiveChatTranscriptEvent records are inserted after the chat is closed and the LiveTranscript record updated). However, the
trigger on the LiveChatTranscriptEvent sObject fires separately on each LiveChatTranscriptEvent record within the same transaction.

All the LiveChatTranscriptEvent records are inserted in a single transaction but one by one. For example, the trigger is executed
for each individual record.

```
      trigger LCTE on LiveChatTranscriptEvent (before insert) {

         // Trigger.New will have only 1 record at a time and trigger will execute for

      individual record

         for(LiveChatTranscriptEvent l : Trigger.New)

         system.debug(l.Type + '>>' +l.Detail);

         }

```

To avoid hitting any governors and limits, design your functionality considering this behavior. You can execute the logic by filtering
the records based on the `Type` field of LiveChatTranscriptEvent.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 62.0)**
Change events are available for the object.

### LiveChatTranscriptShare

Represents a sharing entry on a LiveChatTranscript object. This object is available in API version 24.0 and later.


Standard Objects LiveChatTranscriptShare

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()update()`, `upsert()`

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
Level of access that the User or Group has to the LiveChatTranscript. The possible
values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for live chat transcripts.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects LiveChatTranscriptSkill

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values can include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the LiveChatTranscript with them.

**•** `Owner` —The User is the owner of the LiveChatTranscript or is in a role above
the LiveChatTranscript owner in the role hierarchy.

```
UserOrGroupID

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the LiveChatTranscript.

This object lets you determine which users and groups can view and edit LiveChatTranscript records owned by other users.

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

### LiveChatTranscriptSkill

Represents a join between LiveChatTranscript and Skill. This object is available in API version 25.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`

Fields

**Field Name** **Details**

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
The name of the transcript.

```
SkillId

TranscriptId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the transcript.

Use this object to assign a specific skill to a specific transcript for multi-skill routing.

### LiveChatUserConfig

Represents a setting that controls the console settings for Chat users. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
AutoGreeting

```

**Type**
textarea

**Properties**
Create, Nillable


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

```
Capacity

CriticalWaitTime

CustomAgentName

DeveloperName

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Limits the amount of active chat sessions an agent can engage in.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The amount of time before a chat flashes to alert an agent to answer it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The custom name of the agent associated with the Live Agent configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.


Standard Objects LiveChatUserConfig

**Field Name** **Details**

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
HasLogoutSound

HasNotifications

HasRequestSound

HasSneakPeek

HasTransferConferenceGreeting

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a sound plays when an agent logs out of the console.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether desktop notifications are enabled for the configuration.
Available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a sound plays when a chat request comes in.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether an agent sees a real-time preview of the messages typed
by a visitor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether to enable sending an autogreeting when you transfer to
another agent or invite an agent to a conference chat.

The default value is `false` . Available in API version 53.0 and later.


Standard Objects LiveChatUserConfig

**Field Name** **Details**

```
IsAutoAwayOnDecline

Language

MasterLabel

OptionsHasAgentFileTransfer

OptionsHasAgentSneakPeek

OptionsHasAssistanceFlag

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether agents’ status is automatically changed to Away when they
decline a chat request. Available in API version 26.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the configuration.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can initiate a file transfer from a chat customer.
Available in API version 31.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether Sneak Peek is enabled for agents. Available in API version
29.0 and later.

**Type**
boolean

**Properties**
Create, Filter


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
Determines whether assistance flags are enabled for agents. Available in API
version 29.0 and later.

```
OptionsHasChatConferencing

OptionsHasChatMonitoring

OptionsHasChatTransferToAgent

OptionsHasChatTransferToButton

OptionsHasChatTransferToSkill

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can invite other agents into a customer chat. Available
in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether supervisors can view agents’ ongoing chats. Available in
API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat directly to another agent. Available
in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat to an agent assigned to a particular
chat button. Available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
Specifies whether an agent can transfer a chat to agents assigned to a particular
skill. Available in API version 36.0 and later.

```
OptionsHasTransferConferenceGreeting

OptionsHasVisitorBlocking

OptionsHasWhisperMessage

OptionsIsAutoAwayOnPushTimeout

SupervisorDefaultAgentStatus

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an agent can transfer a chat to an autogreeting or conference
greeting. Available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent can block IP addresses of troublesome visitors.
Available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether supervisors can send private messages to agents within an
agent’s chat with a customer. Available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent’s status automatically changes to Away if the agent
doesn’t respond to a chat request within the specified push time-out limit.
Available in API version 34.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects LiveChatUserConfigProfile

**Field Name** **Details**

**Description**
The default agent status by which to filter agents in the Agent Status list in the
supervisor panel.

```
SupervisorDefaultButtonId

SupervisorDefaultSkillId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default button ID by which to filter agents in the Agent Status list in the
supervisor panel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default skill ID by which to filter agents in the Agent Status list in the
supervisor panel.

Use this object to query and manage agent configurations in Chat.

### LiveChatUserConfigProfile

Represents a join between LiveChatUserConfig and Profile. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects LiveChatUserConfigUser

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

ProfileId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the agent configuration

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the profile

Use this object to assign specific agent configurations to specific user profiles.

### LiveChatUserConfigUser

Represents a join between Live Chat User Config and User. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects LiveChatVisitor

**Field Name** **Details**

**Description**
The record ID of the agent configuration

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the user

Use this object to assign specific agent configurations to specific users.

### LiveChatVisitor

Represents a website visitor who has started or tried to start a chat session. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`,

```
upsert()

```

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


### Standard Objects Location

**Field Name** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

```
Name

SessionKey

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the visitor

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session key used to uniquely identify the visitor.

Use this object to query and manage live chat visitors.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatVisitorChangeEvent (API version 62.0)**
Change events are available for the object.

### Location

Represents a warehouse, service vehicle, work site, or other element of the region where your team performs field service work. In API
version 49.0 and later, you can associate activities with specific locations. Activities, such as the tasks and events related to a location,
appear in the activities timeline when you view the location detail page. Also in API version 49.0 and later, Work.com users can view
Employees as a related list on Location records. In API version 51.0 and later, this object is available for Omnichannel Inventory and
represents physical locations where inventory is available for fulfilling orders.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Location

Special Access Rules

At least one of these features must be enabled:

**•** Commerce Store

**•** Contact Tracing for Employees

**•** Employee Experience

**•** Field Service

**•** Fulfillment Orders

**•** Health Cloud

**•** Industries Insurance

**•** Industries Visit

**•** Locations

**•** Omnichannel Inventory

**•** Public Sector

**•** Retail Execution

**•** Work.com

Fields

**Field Name** **Details**

```
AssignedFoCount

CloseDate

ConstructionEndDate

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of fulfillment orders assigned to the location. Confirming held
fulfillment order capacity increments this value. To reset the location’s capacity,
set this value to 0.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location closed or went out of service.

**Type**
date


Standard Objects Location

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction ended at the location.

```
ConstructionStartDate

DefaultPickupTime

DefaultProcessingTime

DefaultProcessingTimeUnit

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction began at the location.

**Type**
time

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default pickup time at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time unit at the location. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`


Standard Objects Location

**Field Name** **Details**

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

```
Description

DrivingDirections

EarliestPickupTimeOffset

ExternalReference

FoCapacity

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the location.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the location.

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest pickup time for BOPIS. This value is measured in minutes after the
start of business hours.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of a location.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.


Standard Objects Location

**Field Name** **Details**

This field is available in API version 55.0 and later.

```
FulfillingBusinessHours

FoCapacity

IsEligibleForPickup

IsInventoryLocation

IsMobile

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Fulfilling business hours at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates whether the location supports BOPIS

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location stores parts.

Note: This field must be selected if you want to associate the location
with product items.

**Type**
boolean


Standard Objects Location

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location moves. For example, a truck or tool box.

```
LastReferencedDate

LastViewedDate

LatestPickupTimeOffset

Latitude

Location

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the location was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date the location was last viewed.

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest pickup time for BOPIS. This value is measured in minutes before the
end of business hours.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location.

**Type**
location

**Properties**
Nillable

**Description**
The geographic location.


Standard Objects Location

**Field Name** **Details**

```
LocationLevel

LocationType

LogoId

Longitude

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location’s position in a location hierarchy. If the location has no parent or
child locations, its level is 1. Locations that belong to a hierarchy have a level of
1 for the root location, 2 for the child locations of the root location, 3 for their
children, and so forth.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Picklist of location types. It has no default values, so you must populate it before
creating any location records.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A ContentAsset representing a logo for the location.

This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
Logo

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location.


Standard Objects Location

**Field Name** **Details**

```
Name

OpenDate

OwnerId

ParentLocationId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location. For example, Service Van #4.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location opened or came into service.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The location’s owner or driver.

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
The location’s parent location. For example, if vans are stored at a warehouse
when not in service, the warehouse is the parent location.

This is a relationship field.

**Relationship Name**
ParentLocation

**Relationship Type**
Lookup


Standard Objects Location

**Field Name** **Details**

**Refers To**
Location

```
PickupProcessingTime

PossessionDate

Priority

RemodelEndDate

RemodelStartDate

```

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

**The processing time required for BOPIS orders at this location.**

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the location was purchased.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the location when routing orders. No default values are included.
Add values to the picklist and reference them in your custom routing logic.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction ended at the location.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction started at the location.


Standard Objects Location

**Field Name** **Details**

```
RootLocationId

ShouldSyncWithOci

ShouldTrackFoCapacity

TimeZone

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The top-level location in the location’s hierarchy.

This is a relationship field.

**Relationship Name**
RootLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should sync its data with Omnichannel Inventory.
The default value is `false` .

This field is available in API version 51.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should track its fulfillment order capacity. The
default value is `false` .

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.


Standard Objects Location

**Field Name** **Details**

```
VisitorAddressId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup to an account’s or client’s address.

This is a relationship field.

**Relationship Name**
VisitorAddress

**Relationship Type**
Lookup

**Refers To**
Address

Before creating any location records, add at least one value to the Location Type picklist. LocationType is a required field.

To track your inventory in Salesforce, create product items, which represent the stock of a particular product a particular location. For
example, create a product item that represents the 500 bolts you have in stock at your Warehouse A location. Each product item must
be associated with a location.

To get a more granular picture of your field service operation, associate locations with service territories. For example, if a warehouse is
located in a particular service territory, add it as a service territory location.

Important: “Location” in Salesforce can also refer to the geolocation compound field found on many standard objects. When
referencing the Location object in your Apex code, always use `Schema.Location` instead of `Location` to prevent confusion
with the standard Location compound field. If referencing both the Location object and the Location field in the same snippet,
you can differentiate between the two by using `System.Location` for the field and `Schema.Location` for the object.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationChangeEvent (API version 48.0)**
Change events are available for the object.

**LocationFeed**

Feed tracking is available for the object.

**LocationHistory**

History is available for tracked fields of the object.

**LocationOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects LocationGroup

**LocationShare**

Sharing is available for the object.

SEE ALSO:

### LocationGroup LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_ : Inventory Data Model

### LocationGroup

Represents a group of Omnichannel Inventory locations, providing an aggregate view of inventory availability across those locations.
Omnichannel Inventory can create an inventory reservation for an order at the location group level, then assign the reservation to one
or more locations in the group as needed. This object is available in API version 51.0 and later.

You can define location groups according to the logic of your business needs. For example, a location group can represent the warehouses
in a geographic region, or it can include the fulfillment centers associated with a particular online storefront.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.

Fields

**Field** **Details**

```
Description

ExternalReference

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the location group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used when OCI is integrated with B2C Commerce to associate the location group with an
inventory list in B2C Commerce. This value must match the inventory list ID in B2C Commerce.


Standard Objects LocationGroup

**Field** **Details**

```
IsEnabled

LastReferencedDate

LastViewedDate

LocationGroupName

OwnerId

ShouldSyncWithOci

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location group is in use. If set to _`false`_, then inventory functions
ignore this location group and its data isn’t synchronized with OCI. The default value is _`true`_ .

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
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this location group. Default value is the API user that
created the record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects LocationGroupAssignment

**Field** **Details**

**Description**
Specifies whether to synchronize inventory data for this location group with Omnichannel
Inventory. The default value is _`true`_ .

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationGroupChangeEvent (API version 62.0)**
Change events are available for the object.

**LocationGroupFeed**

Feed tracking is available for the object.

**LocationGroupHistory**

History is available for tracked fields of the object.

**LocationGroupOwnerSharingRule**

Sharing rules are available for the object.

**LocationGroupShare**

Sharing is available for the object.

SEE ALSO:

### Location LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_ : Inventory Data Model

### LocationGroupAssignment

Represents the assignment of a location to a location group. This object is available in API version 51.0 and later.

You can assign a location to multiple location groups, which associates it with one location group assignment for each location group
that it’s assigned to. Each location group assignment represents the relationship between one location and one location group, so a
location or location group can be associated with multiple location group assignments.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.


Standard Objects LocationGroupAssignment

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationExternalReference

LocationGroupAssignment

LocationGroupExternalReference

LocationGroupId

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
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the location group assignment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects LocationShippingCarrierMethod

**Field** **Details**

**Description**
(Master-Detail) The associated location group.

```
LocationGroupName

LocationId

LocationName

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location group name of the associated location group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The associated location.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated location.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LocationGroupAssignmentChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

### Location

LocationGroup

### LocationShippingCarrierMethod

The available shipping carrier services associated with a location or location group. Allows the assignment of different shipping methods
to a specific location and enables flexibility and customization in the shipping process. This object is available in API version 61.0 and
later.


Standard Objects LocationShippingCarrierMethod

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The LocationShippingCarrierMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationSourceId

Name

```

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
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location source ID.

This is a polymorphic relationship field.

**Relationship Name**
LocationSource

**Refers To**
Location, LocationGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects LocationTrustMeasure

**Field** **Details**

**Description**
Name of the shipping carrier service associated with the location or location group.

```
OwnerId

PickupTime

ShippingCarrierMethodId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this LocationShippingCarrierMethod object. Default value
is the user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the shipping carrier picks up the order from the associated location or location
group. This field is available in API version 66.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Shipping carrier method ID.

This is a relationship field.

**Relationship Name**
ShippingCarrierMethod

**Refers To**
Location, ShippingCarrierMethod

### LocationTrustMeasure

Represents the COVID safety protocols that your business follows. For example, enforcement of masks, social distancing, cleanliness,
and capacity limits. This object is available in API version 50.0 and later.


Standard Objects LocationTrustMeasure

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

IconUrl

IsVisibleInPublic

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the safety protocol. For example, “Employees and customers are required
to wear a mask in the store.”

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A public image URL to display for the LocationTrustMeasure object.

**Type**
boolean

**Properties**
Create, defaulted on create, Filter, Group, Sort, Update

**Description**
If true, displays the LocationTrustMeasure object on your site. If false, hides the
LocationTrustMeasure object on your site.

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


Standard Objects LocationTrustMeasure

**Field** **Details**

**Description**
The date on which the record was last viewed.

```
LocationExternalReference

LocationId

Name

OwnerId

SortOrder

Title

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An ID assigned to the LocationTrustMeasure objects for a particular location.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID for the location associated with the LocationTrustMeasure.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned name for the LocationTrustMeasure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which to display LocationTrustMeasure objects on your site.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects LocWaitlistMsgTemplate

**Field** **Details**

**Description**
The name of the safety protocol. For example, Enforcement of Masks.

### LocWaitlistMsgTemplate

Represents a junction object connecting LocationWaitlist to MessagingTemplate. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationWaitlistId

MessagingTemplateId

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
The date on which the record was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the LocationWaitlist record.

**Type**
reference


### Standard Objects LocationWaitlist

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the MessagingTemplate record.

```
Name

OwnerId

Type

### LocationWaitlist

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `approaching` —In Progress

**•** `confirmation` —Confirmed

**•** `inactive` —Inactive

**•** `ready` —Ready

**•** `removed` —Removed

Represents a queue created for a specific location. Multiple queues can be created for a single location. For example, you can have a
queue for each sales agent or a standard queue and a queue for vulnerable groups. The specific party of people in a queue is represented
by LocationWaitlistedParty. This object is available in API version 50.0 and later.


Standard Objects LocationWaitlist

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessHoursId

ClosedDateTime

CumulativeGuestCount

CumulativeGuestGroupCount

CurrentGuestCount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the BusinessHours record that contains the hours the business is open.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is closed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of guests allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of groups allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current number of guests.


Standard Objects LocationWaitlist

**Field** **Details**

```
Description

GuestCapacity

LastReferencedDate

LastViewedDate

MaxPartySize

MessagingChannelId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total capacity of guests.

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
The date on which the record was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum size of a group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects LocationWaitlist

**Field** **Details**

**Description**
The messaging channel ID.

```
Name

OpenDateTime

OwnerId

PartyReminderDelayMinutes

PlaceId

ResourceCapacity

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is open.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of minutes between when a party is notified and when they receive a reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location ID for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects LocationWaitlistedParty

**Field** **Details**

**Description**
The capacity for this resource.

```
ResourceOccupancyCount

Status

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The occupancy count for this resource.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `closed`

**•** `open`

**•** `paused`

### LocationWaitlistedParty

Represents a specific party of people waiting in a queue. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this queue.


Standard Objects LocationWaitlistedParty

**Field** **Details**

```
EntryDateTime

EstimatedWaitHours

EstimatedWaitMinutes

LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time a party is added to the queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated hours of wait time for a party.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated minutes of wait time for a party.

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
The date on which the record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects LocationWaitlistedParty

**Field** **Details**

**Description**
The name of the group.

```
OwnerId

PartySize

PartyStatus

SignUpDateTime

WaitlistId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The size of the queued party.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The state of a party in the queue.

Possible values are:

**•** `canceled`

**•** `entered`

**•** `exited`

**•** `ready`

**•** `waiting`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a party signed up for the queue.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects LoginAsEventLog

**Field** **Details**

**Description**
The ID for the queue.

### LoginAsEventLog LoginAsEventLog contains details about when a user logs in as another user in your org. This object is available in API version 61.0 and

later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

DelegatedUserIdentifier

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
string


Standard Objects LoginAsEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID that identifies the user who’s logging in as, or impersonating, another user. For
example: `00530000009M943` .

```
DelegatedUserName

LoginKey

RequestIdentifier

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the user who’s logging in as, or impersonating, another user.

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
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

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


### Standard Objects LoginEvent

**Field** **Details**

**Description**
The impersonated user’s unique session ID. You can use this value to identify all user events
within a session. When a user logs out and logs in again, a new session is started. For Login
Event Type, this field is usually null because the event is captured before a session is created.
For example: `d7DEq/ANa7nNZZVD` .

```
Timestamp

Uri

UserIdentifier

### LoginEvent

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
Unique ID that identifies the user who is being logged in as, or impersonated, by another
user. For example: `005000000000123` .

[The documentation has moved to LoginEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm) _Platform Events Developer Guide_ .

### LoginEventLog

Login event logs contain details about your Salesforce org's user login history. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects LoginEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiType

ApiVersion

AuthenticatedMethodReference

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

**•** `I` —SOAP Cross Instance

**•** `M` —SOAP Metadata

**•** `O` —Old SOAP

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `X` —XmlRPC

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used. For example: `36.0` .

**Type**
string


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol.

```
BrowserType

CipherSuite

ClientIp

CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv%3A50.0)`

```
   Gecko/20100101 Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`

```
   AppleWebKit/537.36 (KHTML, like Gecko)

   Chrome/51.0.2704.84 Safari/537.36

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)

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


Standard Objects LoginEventLog

**Field** **Details**

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

```
DatabaseTotalTime

ForwardedForIp

LoginKey

LoginStatus

LoginSubType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseTotalTime` . Compare this field to `CpuTime`
to determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The status of the login attempt. For successful logins, the value is LOGIN_NO_ERROR. All
other values indicate errors or authentication issues. For details, see Login Event Type —
LOGIN_STATUS Values on page 2308.

**Type**
string


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login flow used. Possible values are:

**•** uiup—UI Username-Password

**•** oauthpassword—OAuth Username-Password

**•** oauthtoken—OAuth User-Agent

**•** oauthhybridtoken—OAuth User-Agent for Hybrid Apps

**•** oauthtokenidtoken—OAuth User-Agent with ID Token

**•** oauthclientcredential—OAuth Client Credential

**•** oauthcode—OAuth Web Server

**•** oauthhybridauthcode—OAuth Web Server for Hybrid Apps

```
LoginType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** 7—AppExchange

**•** A—Application

**•** s—Certificate-based login

**•** k—Chatter Communities External User

**•** n—Chatter Communities External User Third Party SSO

**•** r—Employee Login to Community

**•** z—Lightning Login

**•** l—Networks Portal API Only

**•** 6—Remote Access Client

**•** i—Remote Access 2.0

**•** I—Other Apex API

**•** R—Partner Product

**•** w—Passwordless Login

**•** 3—Customer Service Portal

**•** q—Partner Portal Third-Party SSO

**•** 9—Partner Portal

**•** 5—SAML Idp Initiated SSO

**•** m—SAML Chatter Communities External User SSO

**•** b—SAML Customer Service Portal SSO

**•** c—SAML Partner Portal SSO


Standard Objects LoginEventLog

**Field** **Details**

**•** h—SAML Site SSO

**•** 8—SAML Sfdc Initiated SSO

**•** E—SelfService

**•** j—Third Party SSO

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
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action.

Possible values are:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For Login Event Type, this
field is usually null because the event is captured before a session is created. For example:
`d7DEq/ANa7nNZZVD` .

```
SourceIp

Timestamp

TransportLayerSecurityProtocol

Uri

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source IP of the login request.

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
The TLS protocol used for the login.

Possible values are:

**•** `1.0`

**•** `1.1`

**•** `1.2`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .


Standard Objects LoginEventLog

**Field** **Details**

```
UserIdentifier

UserName

UserType

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
The username that’s used for login.

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


### Standard Objects LoginGeo

**Field** **Details**

```
Username

### LoginGeo

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username that’s used for login.

Represents the geographic location of the user’s IP address for a login event. Due to the nature of geolocation technology, the accuracy
of geolocation fields (for example, country, city, postal code) may vary. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Manage Users permissions can access this object.

Fields

**Field** **Details**

```
City

Country

CountryIso

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country where the user’s IP address is physically located. This value is not localized.

**Type**
string


Standard Objects LoginGeo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166](http://www.iso.org/iso/country_codes.htm)

```
Latitude

LoginTime

Longitude

PostalCode

Subdivision

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude where the user’s IP address is physically located.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time of the login attempt, in GMT time zone.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude where the user’s IP address is physically located.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subdivision where the user’s IP address is physically located. In the U.S., this
value is usually the state name (for example, Pennsylvania). This value is not localized.


### Standard Objects LoginHistory

Usage

The API allows you to do many powerful queries. A few examples are:

**Sample Query** **Query String**

Query showing the country for a login event, where `SELECT Country FROM LoginGeo WHERE Id =`
`Id=LoginGeoId` from AuthSession `'0LE###############'`

Query showing the city and postal code for a login event, where `SELECT City, PostalCode FROM LoginGeo WHERE`
`Id=LoginGeoId` from LoginHistory `Id = '0SO###############'`

### LoginHistory

Represents the login history for all successful and failed login attempts for organizations and enabled portals. This object is available in
API version 21.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

With one exception, only users with Manage Users or Monitor Login History permissions can access this object. The exception is that, in
API version 37.0 and later, all users can retrieve their own login history records.

Fields

**Field** **Details**

```
ApiType

ApiVersion

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the API type, for example `Soap Enterprise` . Label is **API Type** .

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the API version used by the client. Label is **API Version** .


Standard Objects LoginHistory

**Field** **Details**

```
Application

AuthContextClassRef

AuthMethodReference

AuthenticationServiceId

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The application used to access the organization. Label is **Application** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If provided by a third-party identity provider, the authentication method indicated in the
Authentication Context Class Reference (ACR) claim.

**•** SAML providers—stores the value of the `AuthnContextClassRef` statement in
the SAML response.

**•** OpenID Connect providers—stores the value of the ACR claim in the ID token

This field is available in API version 67.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol. This field is available in API version 51.0 and later. Label is
**Authentication Method Reference** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for an authentication service for a login event. For example, you can use
this field to identify the SAML or authentication provider configuration with which the user
logged in. This field is available in API version 34.0 and later. Label is **Authentication Service**
**Id** .

This field is a polymorphic relationship field.

**Relationship Name**
AuthenticationService


Standard Objects LoginHistory

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig

```
Browser

CipherSuite

ClientVersion

CountryIso

ForwardedForIp

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The current browser version. Label is **Browser** .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)
This field is available in API version 37.0 and later.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Version of the API client. Label is **Client Version** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166. This field is available in API version 37.0 and later.](http://www.iso.org/iso/country_codes.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LoginHistory

**Field** **Details**

**Description**
The value in the `X-Forwarded-For` header of HTTP requests sent by the client. For
logins that use one or more HTTP proxies, the `X-Forwarded-For` header is sometimes
used to store the origin IP and all proxy IPs.

The `ForwardedForIp` field stores whatever value the client sends, which might not be
an IP address. The maximum length is 256 characters. Longer values are truncated. The
`ForwardedForIp` field isn’t populated for logins completed via OAuth flows or single
sign-on (SSO).

Available in API version 61.0 and later.

```
LoginGeoId

LoginSubType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a successful or
unsuccessful login event. The accuracy of geolocation fields like country, city, or postal code
can vary because of the nature of the technology.

The Manage Users permission is required for accessing this field. This field is available in API
version 34.0 and later.

This field is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

**Refers To**
LoginGeo

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login flow used.

**•** `InternalSalesforceAuthentication`  - `Internal Salesforce`

```
   Authentication

```

This subtype is for internal use only.

**•** `OauthClientCredentials`  - `OAuth Client Credentials`

**•** `OauthHybridRefreshToken`  - `OAuth Refresh Token for Hybrid`

```
   Apps

```


Standard Objects LoginHistory

**Field** **Details**

**•** `OauthHybridTokenExchange`                   - `OAuth Token Exchange for Hybrid`

```
                     Apps

```

**•** `OauthHybridUserAgent`                   - `OAuth User-Agent for Hybrid Apps`

**•** `OauthHybridWebServer`                   - `OAuth Web Server for Hybrid Apps`

**•** `OauthOtpLogin`                   - `OAuth OTP Login`

**•** `OauthRefreshToken`                   - `OAuth Refresh Token`

**•** `OauthTokenExchange`                   - `OAuth Token Exchange`

**•** `OauthUserAgent`                   - `OAuth User-Agent`

**•** `OauthUserAgentIdToken`                   - `OAuth User-Agent with ID Token`

**•** `OauthUsernamePassword`                   - `OAuth Username-Password`

**•** `OauthWebServer`                   - `OAuth Web Server`

**•** `SoapApiLogin`                   - `SOAP API`

This subtype is for internal use only.

**•** `SoapApiLoginMobile`                   - `SOAP API (Mobile)`

This subtype is for internal use only.

**•** `SoapApiLoginNetworksPortal`                   - `SOAP API (Networks Portal)`

This subtype is for internal use only.

**•** `SoapApiLoginPortal`                   - `SOAP API (Portal)`

This subtype is for internal use only.

**•** `SoapApiLoginSelfService`                   - `SOAP API (Self-Service)`

This subtype is for internal use only.

**•** `UiPasswordReset`                   - `UI Password Reset`

**•** `UsernamePasswordUiLogin`                   - `UI Username-Password`

Label is **Login Subtype** .

```
LoginTime

LoginType

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time zone is based on GMT. Label is **Login Time** .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of login used to access the session.


Standard Objects LoginHistory

**Field** **Details**

**•** `AppExchange`                   - `AppExchange`

**•** `Application`                   - `Application`

**•** `Certificate`                   - `Certificate-based login`

**•** `ChatterCommunityPortalUnPwd`                   - `Chatter Communities External`

```
                     User

```

**•** `ChatterCommunityThirdPartySso`                   - `Chatter Communities`

```
                     External User Third Party SSO

```

**•** `CrossTenantLogin`                   - `Cross Tenant Login` —For internal use only.

**•** `EmployeeLoginToCommunity`                   - `Employee Login to Community`

**•** `HelpAndTraining`                   - `Help And Training`

**•** `IeOfflineClient`                   - `Offline Client`

**•** `LightningLogin`                   - `Lightning Login`

**•** `NetworksPortalApiOnly`                   - `Networks Portal API Only`

**•** `Oauth, Remote Access Client`                   - `Remote Access Client`

**•** `Oauth2, Remote Access 2.0`                   - `Remote Access 2.0`

**•** `OtherApi`                   - `Other Apex API`

**•** `Partner`                   - `Partner Product`

**•** `PasswordlessLogin`                   - `Passwordless Login`

**•** `PasswordlessPasskeyLogin`                   - `Passwordless Login via Passkeys`
(beta)

Passwordless login with passkeys is a pilot or beta service that is subject to the Beta
[Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if](https://www.salesforce.com/company/legal/agreements/)
[executed by Customer, and applicable terms in the Product Terms Directory. Use of this](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
pilot or beta service is at the Customer's sole discretion.

**•** `Portal`                   - `Customer Service Portal`

**•** `PortalThirdPartySso`                   - `Customer Service Portal Third-Party`

```
                     SSO

```

**•** `PrmPortalThirdPartySso`                   - `Partner Portal Third-Party SSO`

**•** `PrmPortal`                   - `Partner Portal`

**•** `Saml`                   - `SAML Idp Initiated SSO`

**•** `SamlChatterNetworks`                   - `SAML Chatter Communities External`

```
                     User SSO

```

**•** `SamlCspPortal`                   - `SAML Customer Service Portal SSO`

**•** `SamlPrmPortal`                   - `SAML Partner Portal SSO`

**•** `SamlSite`                   - `SAML Site SSO`

**•** `Saml2`                   - `SAML Sfdc Initiated SSO`

**•** `SelfService`                   - `SelfService`

**•** `ThirdPartySso`                   - `Third Party SSO`

Label is **Login Type** .


Standard Objects LoginHistory

**Field** **Details**

```
LoginUrl

NetworkId

OptionsIsGet

OptionsIsPost

Platform

SourceIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL from which the login request is coming. Label is **Login URL** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that the user is logging in to. This field is available in API
version 31.0 and later, if Salesforce Experience Cloud sites are enabled for your org.

**Type**
boolean

**Properties**
Filter

**Description**
The HTTP method used for the session login is a GET request.

**Type**
boolean

**Properties**
Filter

**Description**
The HTTP method used for the session login is a POST request.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Operating system on the login machine. Label is **Platform** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LoginHistory

**Field** **Details**

**Description**
The IP address of the incoming client request that first reaches Salesforce during a login. For
example, `126.7.4.2` .

For clients that redirect through one or more HTTP proxies, this field stores the IP address of
the first proxy to reach Salesforce. To better identify the origin IP for these cases, check the
`ForwardedForIp` field instead.

The `SourceIp` field doesn't support the `LIKE` [comparison operator.](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_comparisonoperators.htm)

```
Status

TlsProtocol

UserId

```

Usage

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the status of the attempted login. Status is either success or a reason for failure.
Label is **Status** .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS protocol used for the login. Possible values are:

**•** `TLS 1.0`

**•** `TLS 1.1`

**•** `TLS 1.2`

**•** `TLS 1.3`

**•** `Unknown`

This field is available in API version 37.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user logging in. Label is **User ID** .

Not all fields are filterable. You can only filter on the following fields:

**•** `AuthenticationServiceId`


### Standard Objects LoginIp

**•** `CipherSuite`

**•** `CountryIso`

**•** `Id`

**•** `LoginTime`

**•** `LoginType`

**•** `LoginUrl`

**•** `NetworkId`

**•** `OptionsIsGet`

**•** `OptionsIsPost`

**•** `TlsProtocol`

**•** `UserId`

The API allows you to do many powerful queries. A few examples are:

**Sample Query** **Query String**

Simple query showing UserId & LoginTime for each user `SELECT UserId, LoginTime from LoginHistory;`

Query showing logins only after a specified date and time `SELECT UserId, LoginTime from LoginHistory`

```
                             WHERE LoginTime > 2010-09-20T22:16:30.000Z;

```

Query showing logins for a specific time interval

Query showing the authentication service for a SAML login event,
where `Id=AuthenticationServiceId` from LoginHistory

Query showing the authentication service for an authentication
provider login event, where
`Id=AuthenticationServiceId` from LoginHistory

### LoginIp

```
SELECT UserId, LoginTime from LoginHistory

WHERE LoginTime > 2010-09-20T22:16:30.000Z

AND LoginTime < 2010-09-21T22:16:30.000Z;

SELECT DeveloperName, Issuer, Version FROM

SamlSsoConfig WHERE Id =

'0LE###############'

SELECT Type, DeveloperName FROM

AuthProvider WHERE Id =

'0SO###############'

```

Represents a validated IP address. This object is available in version 28.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`


Standard Objects LoginIp

Fields

**Field** **Details**

```
ChallengeMethod

ChallengeSentDate

IsAuthenticated

SourceIp

UsersId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The challenge method used to confirm the user’s identity. Possible values include the
following.

**•** `Email`

**•** `SMS`

**•** `TOTP_CHOICE` : The user chooses multi-factor authentication.

**•** `TOTP_ONLY` : The user is required to use multi-factor authentication.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the user was authenticated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has already been authenticated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address the user logged in from.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.


### Standard Objects LogoutEventLog

**Field** **Details**

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

Usage

At every login, the IP address of the login request is checked against the validated IP addresses using LoginIp. A match means the login
IP address is a known IP address. If there’s no match, the address is unknown, and the user is asked to confirm their identity.

### LogoutEventLog

Contains details of user sessions ending or being revoked. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiType

```

**Type**

Contains details of user sessions ending or being revoked.

string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata


Standard Objects LogoutEventLog

**Field** **Details**

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

```
ApiVersion

AppType

BrowserType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
double

**Properties**
Filter, Nillable, Sort

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv%3A50.0)`

```
   Gecko/20100101 Firefox/50.0

```


Standard Objects LogoutEventLog

**Field** **Details**

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`

```
                     AppleWebKit/537.36 (KHTML, like Gecko)

                     Chrome/51.0.2704.84 Safari/537.36

```

```
ClientIp

ClientVersion

IsUserInitiatedLogout

LoginKey

PlatformType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The version of the client that was in use upon logging out.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The value is 1 if the user intentionally logged out of the organization by clicking the Logout
button. If the user’s session timed out due to inactivity or another implicit logout action, the
value is 0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects LogoutEventLog

**Field** **Details**

**Description**
The code for the client platform. If a timeout caused the logout, this field is null.

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

```
RequestIdentifier

ResolutionType

SessionKey

SessionLevel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The screen resolution of the client. If a timeout caused the logout, this field is null.

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


Standard Objects LogoutEventLog

**Field** **Details**

**Description**
The security level of the session that was used when logging out.

```
SessionType

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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

**•** `F` : TempUIFrontdoor

**•** `U` : UI

**•** `E` : UserSite

**•** `V` : Visualforce

**•** `W` : WDC_API

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

When a customer logs out by using the **Logout** button, the `TIMESTAMP` field records the
actual logout time. However, when a customer is logged out automatically, Salesforce detects


### Standard Objects LogoutEventStream

**Field** **Details**

the event by using a process that runs every 15 minutes. `TIMESTAMP` values can reflect a
logout time up to 15 minutes later than the actual automatic logout time.

```
UserIdentifier

UserType

### LogoutEventStream

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

[The documentation has moved to LogoutEventStream in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_logouteventstream.htm) _Platform Events Developer Guide_ .

### LookedUpFromActivity

This read-only object is displayed as a related list on an activity record (an event or a task); the list contains records that have custom
lookup relationships from the activity to another object. This object is not queryable.

Supported Calls

```
describeSObjects()

```

Fields

**Field Name** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Indicates the ID of the related account, which is determined as follows:

**•** The account associated with the `WhatId`, if it exists; or

**•** The account associated with the `WhoId`, if it exists; otherwise

**•** `null`

For information on IDs, see Field Types

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

ActivityDateTime

ActivitySubtype

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates one of the following:

**•** The due date of a task

**•** The date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time
Coordinated (UTC) time zone. The time stamp doesn’t represent the time of the
activity; don’t attempt to alter it to accommodate time zone differences. Label
is `Date` .

**Type**
dateTime

**Properties**
Aggregate, Filter, Nillable, Sort

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` .
The time portion of this field is always transferred in the Coordinated Universal
Time (UTC) time zone. Translate the time portion to or from a local time zone for
the user or the application, as appropriate. Label is **Due Date Time** .

The value for this field and `StartDateTime` must match, or one of them
must be `null` .

**Type**
picklist


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity
subtypes. This field isn’t updateable.

Possible values are:

**•** Task

**•** Email

**•** Call

**•** Event

**•** LinkedIn —Available in API version 56.0 and later.

**•** List Email

```
ActivityType

CallDisposition

CallDurationInSeconds

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents one of the following values: `Call`, `Email`, `Meeting`, or `Other` .
Label is `Type` . These are default values, and can be changed.

`ActivityType` is the union of `TaskType` and `EventType` . If the same activity
appears in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are
distinct from each other.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the result of a given call; for example, “we’ll call back,” or “call
unsuccessful.” Limit is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Duration of the call in seconds.


Standard Objects LookedUpFromActivity

**Field Name** **Details**

```
CallObject

CallType

CompletedDateTime

Description

DurationInMinutes

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.

**•** For insert, if the task is saved with a Closed status the field is set. If the task is
saved with an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is
no change to the field.

Note: The status is a dynamic enum. If the Closed mapping is changed
it won’t cause an update of existing tasks. Only new insert/update
operations are affected.

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


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Indicates the duration of the event or task.

```
EndDateTime

IsAllDayEvent

IsClosed

IsHighPriority

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0
and later. This field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both
fields is allowed if the values add up to the same amount of time. If both
fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both
fields is allowed if the values add up to the same amount of time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a
full day, and the `ActivityDate` defines the date of the event. If the value of
this field is set to `false`, then the activity may be an event spanning less than
a full day, or it may be a task. The default value of this field is `false` . Label is
`All-Day Event` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default
value of this field is `false` . This field is set indirectly by setting `Status` on
the task—each picklist value has a corresponding `IsClosed` value. Label is
`Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Indicates a high-priority task. The default value of this field is `false` . This field
is derived from the `Priority` field.

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
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ). The
default value of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is a task; if the value is
set to `false`, then the activity is an event. The default value of this field is
`false` . Label is `Task` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity can be viewed in the
self-service portal. The default value of this field is `false` . Label is `Visible`
`in Self-Service` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the activity is an event, then this field represents the location of the event. If
the activity is a task, then the value is `null` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Indicates the ID of the user or group who owns the activity.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

```
Priority

ReminderDateTime

StartDateTime

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of
this field is `Normal` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time at which a reminder is scheduled to fire if
`IsReminderSet` is set to `true` . If `IsReminderSet` is set to `false`,
then either the user has deselected the reminder checkbox in the user interface
or the reminder has already fired at the time indicated by the value.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the start date and time of the event. Available in versions 13.0 and later.

The `StartDateTime` field contains the event start date.

However, if the event’s `IsAllDayEvent` flag is set to `true` (indicating an
all-day event), then the time stamp in the `StartDateTime` field is always
set to midnight in the Coordinated Universal Time (UTC) time zone. Don’t attempt
to alter the time stamp to account for any time zone differences.

If the event’s `IsAllDayEvent` flag is set to `false`, then you must translate
the time portion of the time stamp in the `StartDateTime` field to or from


Standard Objects LookedUpFromActivity

**Field Name** **Details**

a local time zone for the user or the application, as appropriate, and the translation
must be in the Coordinated Universal Time (UTC) time zone.

If this field has a value, then `ActivityDate` and `ActivityDateTime`
either must be `null` or must match the value of this field.

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
Indicates the current status of a task. The default value of this field is `Not`
`Started` . Each predefined status field sets a value for `IsClosed` .

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
The `WhatId` represents nonhuman objects such as accounts, opportunities,
campaigns, cases, or custom objects. `WhatId` s are polymorphic. Polymorphic
means a `WhatId` is equivalent to the ID of a related object. The label is
`Related To ID` .

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, Award,
BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, Campaign,
CareBarrier, CareBarrierDeterminant, CareBarrierType, CareDeterminant,
CareDeterminantType, CareDiagnosis, CareInterventionType, CareMetricTarget,
CareObservation, CareObservationComponent, CarePgmProvHealthcareProvider,
CarePreauth, CarePreauthItem, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct,
CareProgramProvider, CareProgramTeamMember, CareProviderAdverseAction,
CareProviderFacilitySpecialty, CareProviderSearchableField, CareRegisteredDevice,
CareRequest, CareRequestDrug, CareRequestExtension, CareRequestItem,
CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant,
ContactRequest, Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo,
DelegatedAccount, DocumentChecklistItem, EnrollmentEligibilityCriteria,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, IdentityDocument,
Image, IndividualApplication, Invoice, ListEmail, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PartyConsent, PersonLifeEvent,
PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution,
Visit, VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are
polymorphic. Polymorphic means a WhoId is equivalent to a contact’s ID or a
lead’s ID. The label is `Name ID` .

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


### Standard Objects Macro

Usage

**Query activities related to an object**

**1.** Optionally, issue a describe call against the object whose activities you wish to query, to get a suggestion of the correct SOQL
to use.

**2.** Issue a SOQL relationship query with a main clause that references the object, and an inner clause that references the activity
custom lookup relationship; for example:

```
       SELECT id, name,

       (SELECT id, subject from sponsoredact__r)

       FROM Contact

```

In this example _`sponsoredact__r`_ is a user defined relationship list.

The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following restrictions on users who don’t have “View All Data” permission help prevent performance issues:

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with ‘A’; instead, you must reference a single account record.

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.

**•** You must sort on `ActivityDate` in descending order and `LastModifiedDate` in descending order; you can display
nulls last. For example: `ORDER BY ActivityDate DESC NULLS LAST, LastModifiedDate DESC` .

### Macro

Represents a macro, which is a set of instructions that tells the system to perform one or more tasks. This object is available in API version
32.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of what this macro does.


Standard Objects Macro

**Field** **Details**

```
FolderId

FolderName

IsAlohaSupported

IsLightningSupported

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Returns the ID of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Specifies whether the macro is supported in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Specifies whether the macro is supported in Lightning Experience.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last viewed.


Standard Objects Macro

**Field** **Details**

```
Name

OwnerId

StartingContext

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the macro.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object the macro performs actions on. In Salesforce Classic, macros are supported on
objects with both feed-based layouts and quick actions. In Lightning Experience, macros are
supported on standard and custom objects that allow quick actions and have a customizable
page layout.

A macro definition consists of a Macro object and several associated MacroInstruction objects.

First, create a Macro object. Then, create MacroInstructions that specify objects, operations, conditions, and targets for the macro.

A macro contains an ordered list of macro instructions whose index field, `sortOrder`, is 0-based. If there’s an incorrect sequence of
macro instructions, the macro doesn’t execute.

If you update a macro definition or add or remove instructions from a macro, make sure that the `sortOrder` field that defines the
execution order is correct. To delete an entire macro definition, invoke the delete operation on the Macro object.

The table describes the supported macro instruction targets and how they relate to each other.

Note: Strings indicated by `<brackets>` are variables. The variable description describes the required type. For example,
`Tab.<EntityApiName>` requires the entity name. If your custom entity name is `MyCustomObject`, your target API is
`Tab.MyCustomObject__c` .

If a macro instruction listed in the table supports an implicit operation, you can use that operation as a direct child instruction without
explicitly specifying a target. The hyphens used in the table illustrate the hierarchical relationship between targets. A target isn't available
if its parent isn’t.


Standard Objects Macro

**Table 1: Macro Instruction Target Grammar and Hierarchy**

Example: This example describes a macro that opens a quick action, sets some fields in the quick action, and submits the quick
action.

```
      0. SELECT Tab.Case

      1. SELECT QuickAction.Case.Email

      2. SET Field.EmailMessage.Subject

      3. SET Field.EmailMessage.ToAddress

      4. INSERT Field.EmailMessage.HtmlBody.cursor

      5. SUBMIT

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects MacroInstruction

**MacroChangeEvent (API version 48.0)**
Change events are available for the object.

**MacroHistory**

History is available for tracked fields of the object.

**MacroOwnerSharingRule**

Sharing rules are available for the object.

**MacroShare**

Sharing is available for the object.

### MacroInstruction

Represents an instruction in a macro. An instruction can specify the object that the macro interacts with, the context or publisher that
the macro works within, the operation or action that the macro performs, and the target of the macro’s actions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
MacroId

Name

Operation

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the macro that contains this instruction.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Name of the instruction.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The action that the macro instruction performs. Valid values are:


Standard Objects MacroInstruction

**Field Name** **Details**

**•** Select

**•** Set

**•** Insert

**•** Submit

**•** Close

To create macro instructions that execute conditionally, these values are available
in API version 46.0 and later.

**•** IF

**•** ELSEIF

**•** ELSE

**•** ENDIF

```
SortOrder

Target

Value

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Order of this instruction in the macro.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The object that’s the target of the operation. For example, the target for the active
case tab (Tab.Case) or a quick action, like the Send Email action on the case object
(QuickAction.Case.SendEmail).

In Lightning Experience, macros are supported on standard and custom objects
that allow quick actions and have a customizable page layout.

In Salesforce Classic, macros are supported on objects with feed-based layouts
and quick actions.

You can specify relative dates and times for the following targets.

**•** DateTime

**•** Date

**•** Time

**•** DueDate

**•** Birthday

**Type**
string


Standard Objects MacroInstruction

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Value of a field. If the operation is Select, then the value is null, because the
operation selects the object on which the macro performs an action. An
instruction can contain both a `Value` field and a `ValueRecord` field, but
only one of these fields can have a value. The other field value must be null.

To create relative dates and times, specify a valid Salesforce formula, prefaced
by `MacroFormula` . For example, the following formula creates a date that is
1 day from now:

```
                       MacroFormula:NOW() + 1

```

You can’t edit custom relative formulas in the Macro Builder.

```
ValueRecord

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the value or record. The `ValueRecord` can be either a value or a record,
but not both. An instruction can contain both a `Value` field and a
`ValueRecord` field, but only one of these fields can have a value. The other
field value must be null.

MacroInstructions can specify objects, operations, conditions, and targets. For example, a macro containing these instructions performs
a quick action that sends an email.

```
    Select Email QuickAction

    Set Subject…

    Set To…

    Set Body…

    Submit

```

You can create conditional macros using `IF`, `ELSEIF`, `ELSE`, and `ENDIF` as operations. In a conditional statement, the ExpressionFilter
and ExpressionFilterCriteria objects are used to control which instructions execute. The ExpressionFilter object lets you define a logical
expression with one or more conditions. It uses a child object, ExpressionFilterCriteria, to represent each condition that is evaluated.

For example, consider the following conditional statement and macro instructions.

```
IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)

    Select Email QuickAction

    Set Subject…

    Set To…

    Set Body…

    Submit

```


Standard Objects MacroInstruction

```
   ELSE

       Select Update Case Detail

       Update Case Description…

       Submit

   ENDIF

```

The ExpressionFilter object includes a `FilterConditionLogic` field containing `1 AND 2`, where 1 and 2 are ExpressionFilterCriteria
objects. The SortOrder field in the ExpressionFilterCriteria object maps condition 1 to `Case.Status EQUALS New`, and condition
2 to `Case.Origin EQUALS Phone` . If the conditional statement evaluates to true, then the instructions in the `IF` block are
executed; otherwise, the instructions in the `ELSE` block are executed.

Any number of macro instructions can be present inside an `IF`, `ELSEIF`, or `ELSE` block. In addition, conditions can be nested.

Data Model

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MacroInstructionChangeEvent (API version 48.0)**
Change events are available for the object.


### Standard Objects MacroUsage MacroUsage

Represents macro usage on a record, including which macro was used, who used it, and how they used it. This object is available in API
version 47.0 and later.

Supported Calls

describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

delete() is supported in API version 55.0 and later.

Special Access Rules

This object is always read-only. Only users with “Modify All Data” permission can delete MacroUsage records.

Fields

**Field** **Details**

```
AppContext

ConditionCount

ContextRecord

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the macro was run. Possible values are:

**•** `Aloha` —Salesforce Classic

**•** `Lightning` —Lightning Experience

**•** `Unknown`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of conditional instructions contained in the macro at execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record on which the macro was run.


Standard Objects MacroUsage

**Field** **Details**

```
DurationInMs

ExecutedInstructionCount

ExecutionEndTime

ExecutionState

FailureReason

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The execution time, in milliseconds, for the macro.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of macro instructions that ran successfully. If the macro completed successfully,
this value is the same as `InstructionCount` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time at which macro execution completed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The end state of macro execution. Possible values are

**•** `SUCCESS`

**•** `FAILURE`

**•** `CANCELED`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `ExecutionState` is failure, this field stores the reason for the failure. Possible values
are:

**•** `ACCESS`

**•** `GENERIC`


Standard Objects MacroUsage

**Field** **Details**

**•** `TIMEOUT`

**•** `UNSUPPORTED`

```
FolderId

InstructionCount

IsFromBulk

MacroID

Name

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the macro at the time it was used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of instructions in the macro at the start of execution.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the macro was run as a bulk macro. When a bulk macro is run on multiple records,
usage is recorded per record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the macro.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the macro.

**Type**
reference


### Standard Objects MailmergeTemplate

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the macro.

```
UserId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that ran the macro.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MacroUsageOwnerSharingRule**

Sharing rules are available for the object.

**MacroUsageShare**

Sharing is available for the object.

### MailmergeTemplate

Represents a mail merge template (a Microsoft Word document) used for performing mail merges for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** All users can view this object, but you need the “Customize Application” permission to modify it.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Body

```

**Type**
base64


Standard Objects MailmergeTemplate

**Field** **Details**

**Properties**
Create

**Description**
Required. Microsoft Word document to use as a mail merge template. Due
to limitations with Microsoft Word mail merge templates, your client
application can specify the Body field when creating these records, but not
when updating them. Limit: 5 MB.

```
BodyLength

Category

Description

Filename

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the Microsoft Word document.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of document template. Possible values are:

**•** `Document`

**•** `Envelope`

**•** `Label`

The default value is `Document` .

**Type**
string

**Properties**
Create, Filter,Group, Nillable, Sort, Update

**Description**
Required. Text description of this mail merge template. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. File name of the Microsoft Word document that was uploaded as
a mail merge template. Limit: 255 characters in length.


Standard Objects MailmergeTemplate

**Field** **Details**

```
IsDeleted

LastUsedDate

Name

SecurityOptionsAttachmentHasFlash

SecurityOptionsAttachmentHasXSSThreat

SecurityOptionsAttachmentScannedforFlash

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or
not ( `false` ). Label is **Deleted** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this MailmergeTemplate was last used.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this mail merge template.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if Flash Injection was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if a cross site scripting threat was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update


### Standard Objects MaintenanceAsset

**Field** **Details**

**Description**
Required. True if the attachment has been scanned for Flash Injection.

```
SecurityOptionsAttachmentScannedForXSS

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if the attachment has been scanned for a cross site scripting
threat.

Use this object to manage mail merge templates for your organization.

SEE ALSO:

Overview of Salesforce Objects and Fields

### MaintenanceAsset

Represents an asset covered by a maintenance plan in field service. Assets can be associated with multiple maintenance plans.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The asset associated with the maintenance asset.


Standard Objects MaintenanceAsset

**Field Name** **Details**

```
ContractLineItemId

LastReferencedDate

LastViewedDate

MaintenanceAssetNumber

MaintenancePlanId

NextSuggestedMaintenanceDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contract line item associated with the maintenance asset. This field can only list
a contract line item that is associated with the asset, and whose parent service
contract is associated with the parent maintenance plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the maintenance asset was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-assigned number that identifies the maintenance asset.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Maintenance plan associated with the maintenance asset.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects MaintenancePlan

**Field Name** **Details**

**Description**
The suggested date of service for the maintenance asset’s first work order (not
the date the work order is created). This corresponds to the work order’s
`SuggestedMaintenanceDate` . If left blank when the maintenance asset
is created, this field inherits its initial value from the related maintenance plan.

This field auto-updates after each batch is generated. Its label in the user interface
is Date of the first work order in the next batch.

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work type associated with the maintenance asset. Work orders generated from
the maintenance plan inherit its work type’s duration, required skills and products,
and linked articles. Maintenance assets covered by the plan use the same work
type, though you can update them to use a different one.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MaintenanceAssetChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenanceAssetFeed**

Feed tracking is available for the object.

**MaintenanceAssetHistory**

History is available for tracked fields of the object.

### MaintenancePlan

Represents a preventive maintenance schedule for one or more assets in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects MaintenancePlan

Fields

**Field Name** **Details**

```
AccountId

ContactId

Description

DoesAutoGenerateWorkOrders

DoesGenerateUponCompletion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated account, which typically represents the customer receiving the
maintenance service.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated contact.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the plan.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Turns on auto-generation of work order batches for a maintenance plan and
prohibits the manual generation of work orders via the Generate Work Orders
action. If this option is selected, a new batch of work orders is generated for the
maintenance plan on the `NextSuggestedMaintenanceDate` listed on
each maintenance asset, or on the maintenance plan if no assets are included.
If a `GenerationHorizon` is specified, the date of generation is that many
days earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects MaintenancePlan

**Field Name** **Details**

**Description**
If both this option and `DoesAutoGenerateWorkOrders` are set to true,
a new batch of work orders isn’t generated until the last work order generated
from the maintenance plan is completed. A work order is considered completed
when its status falls into one of the following status categories: Cannot Complete,
Canceled, Completed, or Closed.

If a maintenance plan covers multiple assets, work orders are generated per asset.
If a maintenance asset’s final work order is completed late, its work order
generation is delayed, which may cause a staggered generation schedule between
maintenance assets.

```
EndDate

Frequency

FrequencyType

GenerationHorizon

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last day the maintenance plan is valid.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
(Optional) Amount of time between work orders. The unit is specified in the
`FrequencyType` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Optional) The unit of frequency:

**•** Days

**•** Weeks

**•** Months

**•** Years

For example, to perform monthly maintenance visits you need a work order for
each visit, so enter 1 as the `Frequency` and select Months.

**Type**
int


Standard Objects MaintenancePlan

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Moves up the timing of batch generation if
`DoesAutoGenerateWorkOrders` is set to true. A generation horizon of
5 means the new batch of work orders is generated 5 days before the
maintenance asset’s (or maintenance plan’s, if there are no assets)
`NextSuggestedMaintenanceDate` . The generation horizon must be a
whole number.

```
GenerationTimeframe

GenerationTimeframeType

LastReferencedDate

LastViewedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

(Required) How far in advance work orders are generated in each batch. The unit
is specified in the `GenerationTimeframeType` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Required) The generation timeframe unit:

**•** Days

**•** Weeks

**•** Months

**•** Years

For example, if you need work orders for six months, enter 6 and select Months.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime


Standard Objects MaintenancePlan

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it's possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
LocationId

MaintenancePlanNumber

MaintenancePlanTitle

MaintenanceWindowEndDays

MaintenanceWindowStartDays

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the service takes place.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) An auto-assigned number that identifies the maintenance plan.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name for the maintenance plan.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Days after the suggested service date on the work order that its service
appointment can be scheduled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MaintenancePlan

**Field Name** **Details**

**Description**
Days before the suggested service date on the work order that its service
appointment can be scheduled.

The maintenance window start and end fields affect the Earliest Start Permitted
and Due Date fields on the maintenance plan’s work orders’ service appointments.
For example, if you enter 3 for both the maintenance window start and end, the
Earliest Start Permitted and the Due Date will be 3 days before and 3 days after,
respectively, the Suggested Maintenance Date on each work order. If the
maintenance window fields are left blank, the service appointment date fields
list their work order’s suggested maintenance date.

```
NextSuggestedMaintenanceDate

OwnerId

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The suggested date of service for the first work order (not the date the work order
is created). This corresponds to the work order’s
`SuggestedMaintenanceDate` . You can use this field to enforce a delay
before the first maintenance visit (for example, if monthly maintenance should
begin one year after the purchase date). Its label in the user interface is Date of
the first work order in the next batch.

For example, if you want the first maintenance visit to take place on May 1, enter
May 1. When you generate work orders, the earliest work order will list a suggested
maintenance date of May 1, and the dates on the later work orders will be based
on the `GenerationTimeframe` and `Frequency` .

Important: Maintenance assets also list a
`NextSuggestedMaintenanceDate`, which is initially inherited
from the maintenance plan. If the plan has maintenance assets, this date
auto-updates on the maintenance assets after each batch is generated,
but doesn’t update on the maintenance plan itself because batch timing
is calculated at the maintenance asset level. If the plan doesn’t have
maintenance assets, this date auto-updates on the maintenance plan after
each batch is generated.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the maintenance plan.


Standard Objects MaintenancePlan

**Field Name** **Details**

```
ServiceContractId

StartDate

SvcApptGenerationMethod

WorkOrderGenerationMethod

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service contract associated with the maintenance plan. The service contract
can’t be updated if any child maintenance asset is associated with a contract line
item from the service contract.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the maintenance plan is valid.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The service appointment generation method.

**•** One service appointment per work order

**•** One service appointment per work order line item

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.

If Work Order Generation Method is set to One work order line item per asset,
you must select a Service Appointment Generation Method.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The work order generation method.

**•** One work order per asset


Standard Objects MaintenancePlan

**Field Name** **Details**

**•** One work order line item per asset

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is left as None, the generation is defaulted to
one work order per asset.

When One work order line item per asset is set, and all maintenance assets have
the same Next Suggested Maintenance Date on the maintenance plan, they are
grouped in one work order. However, if maintenance assets have different Next
Suggested Maintenance Dates, multiple work orders are created for each date.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.

```
WorkOrderGenerationStatus

WorkTypeId

```

Associated Objects

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read Only) Indicates the status of work order generation:

**•** NotStarted—the default value, work order generation has not started

**•** InProgress—work order generation is underway

**•** Completed—work order generation is complete

**•** Unsuccessful—it was not possible to generate work orders

You can generate only one batch at a time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated work type. Work orders generated from the maintenance plan
inherit its work type’s duration, required skills and products, and linked articles.
Maintenance assets covered by the plan use the same work type, though you
can update them to use a different one.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects MaintenanceWorkRule

**MaintenancePlanChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenancePlanFeed**

Feed tracking is available for the object.

**MaintenancePlanHistory**

History is available for tracked fields of the object.

**MaintenancePlanOwnerSharingRule**

Sharing rules are available for the object.

**MaintenancePlanShare**

Sharing is available for the object.

### MaintenanceWorkRule

Represents the recurrence pattern for a maintenance record. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DoesFloatingWorkOrder

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the maintenance plan uses the floating work order adjustment. The default is
false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
dateTime


Standard Objects MaintenanceWorkRule

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last viewed.

```
Name

NextSuggestedMaintenanceDate

OwnerId

ParentMaintenancePlanId

ParentMaintenanceRecordId

RecordsetFilterCriteriaId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this maintenance work rule.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next date on which this rule will generate maintenance items.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The assigned owner of the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance record this work rule applies to.

**Type**
reference


Standard Objects MaintenanceWorkRule

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recordset filter criteria associated with this maintenance work rule. Available in API
version 52.0 and later.

```
RecurrencePattern

SortOrder

Title

Type

WorkTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The RRULE that defines the pattern of recurrence for this work order rule.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The sort order that applies to this work order rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The title of this work order rule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of maintenance work rule. Available values are:

**•** `Criteria-based`

**•** `Calendar-based` (default)

Available in API version 52.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ManagedContent

**Field** **Details**

**Description**
The ID of the work type that this work order rule generates.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MaintenanceWorkRuleChangeEvent**

Change events are available for the object.

**MaintenanceWorkRuleFeed**

Feed tracking is available for the object.

**MaintenanceWorkRuleHistory**

History is available for tracked fields of the object.

**MaintenanceWorkRuleOwnerSharingRule**

Sharing rules are available for the object.

**MaintenanceWorkRuleShare**

Sharing is available for the object.

### ManagedContent

Represents managed content in a Salesforce CMS workspace for use in an Experience Cloud site or a channel. The ManagedContent
object represents the complete instance of a managed content record. It provides a consistent identifier for the managed content so
that variants of the content item can be created over time. This object is available in API version 56.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContent is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ManagedContent

**Field** **Details**

**Description**

The unique API name of the Salesforce CMS content. Name requirements:

**•** must be 80 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain two consecutive underscores

This field is available in API version 62.0 and later.

```
AuthoredManagedContentSpaceId

ContentKey

ContentTypeFullyQualifiedName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce CMS workspace ID where the content resides.

This field is a relationship field.

**Relationship Name**
AuthoredManagedContentSpace

**Relationship Type**
Lookup

**Refers To**
ManagedContentSpace

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified name of the content type of this CMS content. In an enhanced CMS
workspace, the `ContentTypeFullyQualifiedName` for each standard content
type is:

**•** News: `sfdc_cms__news`


Standard Objects ManagedContent

**Field** **Details**

**•** Image: `sfdc_cms__image`

**•** Document: `sfdc_cms__document`

In a CMS workspace, the `ContentTypeFullyQualifiedName` for each standard
content type is:

**•** News: `news`

**•** Image: `cms_image`

**•** Document: `cms_document`

In both CMS workspaces and enhanced CMS workspaces, the
`ContentTypeFullyQualifiedName` for a custom content type is the same as the
developer name of the custom content type.

This field is available in API version 62.0 and later.

```
Name

PrimaryLanguage

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the Salesforce CMS content. When you view this content in a CMS workspace,
`Name` is the title of the latest content version. In an enhanced CMS workspace, `Name` is
the title of the content in the workspace’s default language.

This field is available in API version 58.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default language of the Salesforce CMS workspace where the content resides.

When you create or add content in a Salesforce CMS workspace, the content is uniquely identified by the Salesforce CMS workspace, a
content key, and a default language. `ManagedContent` can be queried through the public sObject API. Use this object to create
and retrieve information for a specific managed content.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ManagedContentChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.


### Standard Objects ManagedContentChannel ManagedContentChannel

Represents the details of a CMS channel. CMS channels correspond to managed content publishing endpoints. They deliver published
content from your Salesforce CMS workspaces to an audience. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContentChannel is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

```
CacheControlMaxAge

Domain

DomainHostName

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS content resource in the CMS
channel to expire before a new request for the resource must be made.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The domain for a public channel. Only public channels can have an assigned domain.

Possible value is:

**•** mydomain.cdn.salesforce-experience.com

Note: The `mydomain` value is specific to the domain of the channel.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hostname of the domain assigned to the CMS channel. Only public channels can have
an assigned domain.


Standard Objects ManagedContentChannel

**Field** **Details**

```
MediaCacheControlMaxAge

Name

OptionsIsCacheControlPublic

OptionsIsDomainLocked

OptionsIsSearchable

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS image or document content
resource in the CMS channel to expire before a new request for the resource must be made.
This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the CMS channel.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the CMS channel connection type is public. When `false`, the cache control
is private. The default value is `false` .

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the domain set to the channel can’t be changed. Only public channels can
have this field set to `true` . If the channel type is `COMMUNITY`, the default value is `true` .
For all other channel types, the default value is `false` .

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, users can search for all published CMS content types within the channel. The
default value is `false` .


### Standard Objects ManagedContentInfo

**Field** **Details**

```
Type

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The connection type of the CMS channel. The connection type determines which audience
can access the CMS content delivered in the channel.

Possible values are:

**•** `COMMUNITY` : User access is controlled by the settings of the Experience Cloud site.

**•** `CloudToCloud` : Connects Salesforce CMS to the B2C Commerce Page Designer.

**•** `ConnectedApp` : User access to the channel is controlled by the connected application
associated with the channel.

**•** `PublicUnauthenticated` : No user authentication required, content can be cached
on public CDNs.

**•** `Record` : User access to the content is controlled by the user access to the associated
record. Content is only accessible to users with access to the record.

**•** `UserPermission` : This value is reserved for future use.

`ManagedContentChannel` can be queried through the public sObject API. Use this object to retrieve information for a specific
CMS channel.

### ManagedContentInfo

Allows the creation of relationship to Product using ProductMedia. This object is available in API version 49.0 to 57.0. In API version 58.0
and later, use the ManagedContent object.

Supported Calls

```
describeSObjects()

```

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Usage

The CMS content import process returns a ManageContentInfo ID for each piece of content. The ManagedContentInfo entity has a 1:1
relationship with ProductMedia. To create this relationship, ProductMedia must be associated with a Product entity, for example, Product

- ProductMedia > ManagedContentInfo. Use the ID to associate content uploaded through the API with the ProductMedia entity


### Standard Objects ManagedContentSpace ManagedContentSpace

Represents the complete instance of a Salesforce CMS workspace that stores managed content. Users and groups with designated
permissions can access and manage the content in a CMS workspace. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContentSpace is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

ApiName

```
DefaultLanguage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique API name of an enhanced Salesforce CMS workspace. Name requirements:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can’t end with an underscore

**•** can’t contain two consecutive underscores

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default language for the Salesforce CMS workspace.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)


Standard Objects ManagedContentSpace

**Field** **Details**

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

```
Description

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the Salesforce CMS workspace.

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


### Standard Objects ManagedContentVariant

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the Salesforce CMS workspace.

### ManagedContentVariant

Represents a variant of a managed content item. This object is available in API version 56.0 and later.

### Managed content variants are associated with a ManagedContent object. The managed content and variants are counted as one

content record in your Salesforce org.

For example, say you have a managed content item of content type News and a default language of English. When you translate the
News content into other languages such as Spanish, Japanese, and French, a managed content variant for each language is created.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

### ManagedContentVariant is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

```
ContentTypeFullyQualifiedName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified name of the content type of this CMS content. In an enhanced CMS
workspace, the `ContentTypeFullyQualifiedName` for each standard content
type is:

**•** News: `sfdc_cms__news`

**•** Image: `sfdc_cms__image`

**•** Document: `sfdc_cms__document`

The `ContentTypeFullyQualifiedName` for a custom content type is the same as
the developer name of the custom content type.

This field is available in API version 62.0 and later.


Standard Objects ManagedContentVariant

**Field** **Details**

```
IsPublished

Language

ManagedContentId

ManagedContentKey

ManagedContentVariantStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the managed content variant is published to a channel.

The default value is `false` .

This field is calculated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Language of the variant.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Globally unique identifier for the managed content item.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Relationship Type**
Lookup

**Refers To**
ManagedContent

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Globally unique identifier for managed content that associates with the managed content
variant.

**Type**
picklist


Standard Objects ManagedContentVariant

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Publication status of the managed content.

Possible values are:

**•** `Draft`

**•** `Published`

**•** `Revised`

```
Name

UrlName

VariantType

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the managed content variant.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL name of the managed content variant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of variant.

Possible value is:

**•** `Content`

Managed content variants are associated with a `ManagedContent` object. The managed content and managed content variants
are counted as one content record in your Salesforce org.

`ManagedContentVariant` can be queried through the public sObject API. Use this object to retrieve information for a specific
content in a certain language and format of a managed content.


### Standard Objects MarketingForm MarketingForm

Represents an Account Engagement marketing form that has been synched to Salesforce. Use forms on your website and landing pages
to collect information about visitors and turn anonymous visitors into identified prospects. This object is available in API version 42.0
and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set.

Fields

**Field Name** **Details**

```
CampaignId

ErrorRate

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of views that led to an error.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp that indicates when the current user last viewed a record that is
related to this form.

**Type**
dateTime


Standard Objects MarketingForm

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
`LastReferencedDate` ) and not viewed.

```
Name

SubmissionRate

TotalErrors

TotalSubmissions

TotalTrackedLinkClicks

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the marketing form.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of the views that led to a form submission.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a form error prevented a submission.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times the form was successfully submitted.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects MarketingForm

**Field Name** **Details**

**Description**

The total number of link clicks from your thank you page.

```
TotalViews

Type

UniqueErrors

UniqueSubmissions

UniqueTrackedLinkClicks

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times your form has been viewed. Includes multiple views
from the same visitor.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Specifies the type of marketing form record, either a form or form handler.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of errors generated by separate visitors.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique submissions. Removes multiple submissions from
the same prospect.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique link clicks from your thank you page. Removes
multiple clicks from the same prospect.


### Standard Objects MarketingLink

**Field Name** **Details**

```
UniqueViews

```

Associated Objects

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of form views by separate visitors.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MarketingFormEvent (API version 44.0)**
Change events are available for the object.

**MarketingFormFeed**

Feed tracking is available for the object.

### MarketingLink

Represents an Account Engagement marketing link record, either a custom redirect or a file, that has been synced to Salesforce. This
object is available in API version 42.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set.

Fields

**Field Name** **Details**

```
CampaignId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.


Standard Objects MarketingLink

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

TargetUrl

TotalTrackedLinkClicks

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp that indicates when the current user last viewed a record that is
related to this marketing link.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
`LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the marketing link.

**Type**
url

**Properties**
Filter, Group, Sort

**Description**

The target URL of the marketing link.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of clicks for the redirect. Includes clicks from visitors and
identified prospects. When a person clicks the link multiple times, each click is
counted in this number.


### Standard Objects MatchingRule

**Field Name** **Details**

```
Type

UniqueTrackedLinkClicks

```

Associated Objects

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Specifies the type of marketing link record, either a custom redirect or file.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of unique clicks for the redirect. Includes clicks from visitors and
identified prospects. Only the first click is counted in this number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MarketingFormEvent (API version 44.0)**
Change events are available for the object.

**MarketingLinkFeed**

Feed tracking is available for the object.

### MatchingRule

Represents a matching rule that is used to identify duplicate records. This object is available in API version 33.0 and later.

A matching rule compares field values to determine whether a record is similar enough to existing records to be considered a duplicate.
For example, a matching rule can specify that if the `Email` and `Phone` values of two records match exactly, the records are possible
duplicates. Your organization uses matching rules with duplicate rules to define what happens when duplicates are identified.

If the rule is for a Person Account, `SobjectSubType` is automatically set to `PersonAccount` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.


Standard Objects MatchingRule

Fields

**Field Name** **Details**

```
BooleanFilter

Description

DeveloperName

Language

MasterLabel

MatchEngine

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies filter logic conditions.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the matching rule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name for the matching rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language selected for your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule.

**Type**
picklist


Standard Objects MatchingRule

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The match engine used by the matching rule.

```
NamespacePrefix

RuleStatus

SobjectSubtype

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for matching rules for your organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The activation status of the matching rule. Values are:

**•** _`Inactive`_

**•** _`Deactivating`_

**•** _`DeactivationFailed`_

**•** _`Active`_

**•** _`Activating`_

**•** _`ActivationFailed`_

Important: The only valid values you can declare when deploying a
package are _`Active`_ and _`Inactive`_ .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only. Indicates if the matching rule is defined for the `Person` subtype of
`Account` . Valid values are:

**•** `PersonAccount`

**•** `None`

If the rule is for a Person Account, `SobjectSubType` is automatically set to
`PersonAccount` .


### Standard Objects MatchingRuleItem

**Field Name** **Details**

```
SobjectType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object for the matching rule.

Use the Salesforce API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API to create,
update, or delete these objects.

SEE ALSO:

### MatchingRuleItem

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_matchingrule.htm)

### MatchingRuleItem

Represents criteria used by a matching rule to identify duplicate records. This object is available in API version 33.0 and later.

A matching rule item determines which field the matching rule uses to identify a duplicate record. It also determines the method used
to compare value that two records have for the field. For example, a matching rule item might specify that the `Email` field values of
two records must match exactly in order for the records to be considered duplicates.

When a matching rule has multiple matching rule items, it means that multiple fields must match in order for the records to be identified
as dupcliates.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
BlankValueBehavior

```

**Type**
picklist


Standard Objects MatchingRuleItem

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies how blank fields affect whether the fields being compared are considered
matches. Valid values are:

**•** _`MatchBlanks`_

**•** _`NullNotAllowed`_ (default)

```
Field

MatchingMethod

MatchingRuleId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates which field to compare when determining if a record is similar enough
to an existing record to be considered a match.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines how the fields are compared. Choose between the exact matching
method and various fuzzy matching methods. Valid values are:

**•** _`Exact`_

**•** _`FirstName`_

**•** _`LastName`_

**•** _`CompanyName`_

**•** _`Phone`_

**•** _`City`_

**•** _`Street`_

**•** _`Zip`_

**•** _`Title`_

For details on each matching method, see “Matching Methods Used with
Matching Rules” in the Salesforce Help.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects MerchAccPaymentMethodSet

**Field Name** **Details**

**Description**
The ID for the matching rule.

This is a relationship field.

**Relationship Name**
MatchingRule

**Relationship Type**
Lookup

**Refers To**
MatchingRule

```
SortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The order of the matching rule items for a matching rule.

Use the Salesforce SOAP API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API
to create, update, or delete these objects.

SEE ALSO:

MatchingRule

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_matchingrule.htm)

### MerchAccPaymentMethodSet

Defines an ordered list of payment methods that are available to a merchant's cudstomer during checkout. You can configure multiple
payment method sets, each designated for a specific locale, payment region, or sale channel. This object is available in API version 58.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects MerchAccPaymentMethodSet

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
CurrencyIsoCode

DeveloperName

MerchantAccountId

PaymentMethodSetNumber

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. The ISO code for
any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique name for the object given by the Payments admin.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the MerchantAccount.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects MerchAccPaymentMethodType

**Field** **Details**

**Description**
Auto-assigned ID for the `MerchAccPaymentMethodSet` .

```
PaymentMethodSummary

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Summary field that is automatically populated with comma-separated values from
### MerchAccPaymentMethodType.

This field is a calculated field.

### MerchAccPaymentMethodType

Refers to a payment method that is in a payment method set, which is defined by the `MerchAccPaymentMethodSet` object.
This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
CurrencyIsoCode

PaymentInstrumentType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency used by the org.

**Type**
picklist


Standard Objects MerchAccPaymentMethodType

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of instrument the payer can pay with.

Possible values are:

**•** `us_bank_account - ACH_Debit`

**•** `affirm - Affirm`

**•** `afterpay - Afterpay`

**•** `afterpay_clearpay - Afterpay/Clearpay`

**•** `amazon_pay - Amazon Pay`

**•** `applepay - Apple Pay`

**•** `au_becs_debit - BECS_Debit`

**•** `bacs_debit - BACS_Debit`

**•** `bancontact - Bancontact`

**•** `card - Credit Cards`

**•** `cashapp - Cash App`

**•** `clearpay - Clearpay`

**•** `eps - EPS`

**•** `googlepay - Google Pay`

**•** `ideal - iDEAL`

**•** `klarna - Klarna`

**•** `link - Link`

**•** `paypal - PayPal`

**•** `sepa_debit - SEPA Debit`

**•** `venmo - Venmo`

**•** `wechat_pay - WeChat Pay`

```
PaymentMethodSetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MerchAccPaymentMethodSet.

This field is a relationship field.

**Relationship Name**
PaymentMethodSet

**Relationship Type**
Lookup


### Standard Objects MerchantAccount

**Field** **Details**

**Refers To**
MerchAccPaymentMethodSet

```
PaymentMethodSetTypeNumber

SortOrder

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-assigned ID for the MerchAccPaymentMethodSet.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sort order for the MechAccPaymentMethodType within the
MerchAccPaymentMethodSetExperience.

This object has these associated object. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**MerchAccPaymentMethodTypeHistory on page 63**
History is available for tracked fields of the object.

### MerchantAccount

A type of bank account that lets a merchant accept payments from a variety of payment methods, including credit or debit cards, or
digital wallets. A Salesforce Payments merchant account is linked to an underlying payment gateway to process payments This object
is available in API version 56.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.


Standard Objects MerchantAccount

Fields

**Field** **Details**

```
AccountDescription

CountryIsoCode

CurrencyIsoCode

LastReferencedDate

LastViewedDate

Mode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Information about the merchant account.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Country where the legal entity representing the account is.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization. Available only for
organizations with multi-currency enabled.

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
the user can have accessed this record or list view but not viewed it.

**Type**
picklist


Standard Objects MerchantAccount

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The operational mode of the merchant account. This field determines the account’s ability
to accept payments. For production, the account must be in Live mode.

Possible values are:

**•** `Connected`                   - Merchant account is active but it can’t accept payments. This option is
only valid in production orgs.

**•** `Live`                   - Merchant account is active and can accept payments. This option is only valid
in production orgs.

**•** `Test` –Merchant account is active but not able to accept payments. This option is only
valid in sandbox orgs, and the account can accept only test transactions.

```
Name

OwnerId

PaymentStatus

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the merchant account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Name of the individual or group assigned to the merchant account.

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
Merchant account is active and can accept payments.

Possible values are:


Standard Objects MerchantAccount

**Field** **Details**

**•** `Disabled`

**•** `Enabled`

The default value is `Disabled` .

```
PayoutStatus

Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Money can be moved from the payment provider account to the designated merchant
account.

Possible values are:

**•** `Disabled`

**•** `Enabled`

The default value is `Disabled` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the state of the merchant account.

Possible values are:

**•** `Active`  - The merchant account can accept payments.

**•** `Complete`  - `PaymentStatus` and `DepositStatus` are enabled and all the
required information is provided.

**•** `Enabled`  - `PaymentStatus` and `PayoutStatus` are enabled, but the payment
provider requires more information later. If the merchant doesn't provide the information,
then the account becomes restricted. The time limit that the merchant has to provide
the information is longer than the `RestrictedSoon` state.

**•** `Pending`  - The merchant account exists but it can’t accept payments. This option
maintains backward compatibility for accounts that were created with API version 55.0
and earlier.

**•** `Rejected`  - The account is rejected and an explanation is provided.

**•** `Restricted`  - `PaymentStatus`, `PayoutStatus`, or both are disabled, so the
merchant account’s operation is limited.

**•** `Restricted Soon`  - `PaymentStatus` and `PayoutStatus` are enabled, but
the payment provider requires more information. If the merchant doesn't provide the
information in a specific time period, then the account becomes restricted.


### Standard Objects MerchantAccountEvent

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MerchantAccountChangeEvent (API version 62.0)**
Change events are available for the object.

**MerchantAccountFeed**

Feed tracking is available for the object.

**MerchantAccountHistory**

History is available for tracked fields of the object.

**MerchantAccountOwnerSharingRule**

Sharing rules are available for the object.

**MerchantAccountShare**

Sharing is available for the object.

### MerchantAccountEvent

Represents a merchant account platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0
and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)

Supported Calls

```
   describeSObjects()

```

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
ChangeType

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of merchant account event, which triggers an event notification. You can write code
to listen to operate conditionally on the value of this field. For example, you can ignore a
create change but get notified of updates.

Possible values are:


### Standard Objects MessagingChannel

**Field** **Details**

**•** `Create` –Merchant account is created.

**•** `Disable` –The account is deactivated. For example, the payment provider or the
merchant disables an account due to fraudulent activity.

**•** `PaymentEnable` –The account is active and ready to receive payments.

**•** `PayoutEnable` –The account is ready to receive payouts.

**•** `Update` –Merchant account property change occurs.

```
MerchantAccountId

### MessagingChannel

```

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the merchant account for which the event occurs.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

Represents a communication channel that an end user can use to send a message to an agent. A communication channel can be an
SMS number, a Facebook page, or another supported messaging channel. This object is available in API version 40.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
The operating hours for your business, when agents are available. Available only
in orgs that use Einstein Bots.

This is a relationship field.

**Relationship Name**
BusinessHours

**Relationship Type**
Lookup

**Refers To**
BusinessHours

```
ChannelAddressIdentifier

ChannelDefinitionId

ConsentType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A UUID that identifies a deployed messaging channel. This identifier is unique
across orgs, so a channel with the same MessagingPlatformKey in a sandbox and
production will have a different ChannelAddressIdentifier for each. Available in
API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated conversation channel definition, which is used only in Bring Your
Own Channel for Messaging and Bring Your Own Channel for CCaaS. Available
in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

**Type**
picklist

**Properties**
Create, defaultedOnCreate, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of consent, or opt-in, that is required to message users on this channel.
This field is available in API version 48.0 and later. Possible values are:


Standard Objects MessagingChannel

**Field Name** **Details**

**•** `DoubleOptIn`

**•** `ExplicitOptIn`

**•** `ImplicitOptIn` (default value)

The property `defaultedOnCreate` has been removed in API version 51.0
and later. Now the consent type is defaulted to `ImplicitOptIn` when the
consent type isn’t set on create only for channels that support consents.

```
ConversationEndResponse

CriticalWaitTime

Description

DeveloperName

DoubleOptInPrompt

EngagedResponse

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the customer when the agent ends the conversation.
(Optional)

**Description**
Reserved for future use. This field has been deprecated as of API version 52.0.

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name for the messaging channel. This value is a concatenation
of the messaging platform key and the message type.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the end user to prompt them to doubly opt in to receiving
messages. Available in API version 48.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
Automated response to the customer when the conversation is accepted by the
agent. (Optional)

```
InitialResponse

IsActive

IsAuthenticated

IsoCountryCode

IsRequireDoubleOptIn

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
First automated response to the customer for a new conversation. (Optional)

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a channel is active and can receive messages.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a user is authenticated to a voice assistant. The org permission
Live Message Voice is required to access and update this field. Available in API
version 44.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Two-letter ISO 3166-1 alpha-2 code for the country that the phone number is
associated with. For example, the code for United States is `US` . Available in API
version 44.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
Indicates whether double opt-in is required ( `true` ) or not ( `false` ) for this
Messaging channel. Available in API version 48.0 and later.

```
IsRestrictedToBusinessHours

IsUserMatchByExternalIdOnly

Language

MasterLabel

MessageType

```

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to restrict matching on customer by external ID only (and not
use the full name). This field has been deprecated as of API version 52.0.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique name for the `MessagingChannel` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel for Messaging or Bring Your
Own Channel for CCaaS. Available in API version 58.0 and later.

**•** `EmbeddedMessaging` —Represents Enhanced Chat. Available in API
version 50.0 and later.

**•** `Facebook`


Standard Objects MessagingChannel

**Field Name** **Details**

**•** `Phone`

**•** `PSTNVoice` —Represents an Agentforce Voice channel that uses PSTN.
Available in API version 65.0 and later.

**•** `SIPVoice` —Represents an Agentforce Voice channel that uses SIP.
Available in API version 65.0 and later.

**•** `Text`

**•** `Voice`

**•** `WhatsApp`

```
MessagingPlatformKey

OfflineAgentsResponse

OptInPrompt

OptInResponse

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique key for a channel that the end user can message or call based on the
MessageType.

**•** In PSTNVoice, SMS, WhatsApp, and LINE channels, the platform key is the
phone number associated with this channel.

**•** In Facebook Messenger channels, the platform key is the Facebook page ID
associated with this channel.

**•** In Apple Messages for Business channels, the platform key is the Apple
Messages identifier.

**•** In Enhanced Chat, the platform key is identical to the Channel Address
Identifier.

**Description**
Reserved for future use.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Automated response to the end user to prompt them to explicitly opt in to
receiving messages. Available in API version 49.0 and earlier.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**

Automated response to the end user when they opt in to messaging. Available
in API versions 48.0 and 49.0. Use the `OptInConfirmation` field of the
MsgChannelLanguageKeyword on page 3501 object instead.

```
OptionsIdentifyEndUserLanguage

OptOutResponse

OutsideBusinessHoursResponse

PlatformType

RoutingConfigurationId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Auto-populates the Language field for this channel’s messaging users if their
locale is known. Supported for Enhanced Chat and Apple Messages for Business
only.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**

Automated response to the end user when they opt out of messaging. Available
in API version 48.0 only. Use the `OptOutConfirmation` field of the
MsgChannelLanguageKeyword object instead.

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the channel is `Standard` or `Enhanced` .

When a standard SMS or Facebook Messenger channel is upgraded, the
PlatformType changes from `Standard` to `Enhanced` . When a standard
WhatsApp channel is upgraded, the original channel’s PlatformType remains
`Standard` and a new channel is created with a PlatformType of `Enhanced` .

Enhanced Chat channels have a PlatformType of `Enhanced` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**

Specifies which Omni-Channel routing configuration to use. This field is required
when `RoutingType` is `OmniSkills` [. To learn more, see Create Routing](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)
[Configurations.](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)

```
RoutingType

SessionHandler

TargetQueueId

TargetUserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type used to support Omni-Channel’s different routing methods.

**•** `OmniQueue` (queue-based routing)

**•** `OmniSkills` (skills-based routing)

When this value isn’t set, `OmniQueue` is used.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The queue or Omni-Channel flow that the channel's messaging sessions are
routed to. Available in API version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Queue in which incoming conversations are placed while waiting for an agent
to accept.

This is a relationship field.

**Relationship Name**
TargetQueue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference


### Standard Objects MessagingChannelSkill

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Messaging User or agent for the conversation. Available in API version 50.0 and
earlier.

Usage

While third-party messaging channels can be created via Apex, we recommend creating channels via the Messaging Settings page in
Setup. Channels created via Apex may not work and can't be deleted.

In enhanced WhatsApp, Facebook Messenger, Apple Messages for Business, and LINE channels, the flow of a channel's messaging traffic
is controlled by an associated MessagingChannelUsage record. The MessagingChannelUsage determines whether the channel is active
or deactivated.

### MessagingChannelSkill

Junction object that represents an association between MessagingChannel and Skill. This object is available in API version 45.0 and later.

For example, when we want to use Omni-Channel skills-based routing in Live message, this object maintains the mapping between the
messaging channel and the skill.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
MessagingChannelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MessagingChannel on page 3414.

This is a relationship field.

**Relationship Name**
### MessagingChannel

**Relationship Type**
Lookup


### Standard Objects MessagingChannelUsage

**Field Name** **Details**

**Refers To**
### MessagingChannel

```
SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Skill on page 5081.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

### MessagingChannelUsage

Represents the status of an enhanced Messaging channel or of an application in a Unified Messaging channel. This object is available in
API version 60.0 and later.

A MessagingChannel can be associated with up to three MessagingChannelUsage records, each with a unique DeploymentType. The
role of a MessagingChannelUsage record differs slightly depending on whether it's used in an enhanced Messaging channel or a Unified
Messaging channel.

**•** In enhanced WhatsApp, Facebook Messenger, Apple Messages for Business, and LINE channels, each channel has one associated
### MessagingChannelUsage record with a DeploymentType of Conversation . The MessagingChannelUsage record determines

the channel's flow of messaging traffic. When you activate such a channel in Setup, its MessagingChannelUsage record updates to
use a `DeploymentStatus` of `Active`, and messaging traffic can flow to and from Salesforce. Similarly, deactivating the
channel in Setup causes its MessagingChannelUsage record to update to a `DeploymentStatus` of `Disabled`, and stops the
flow of messaging traffic.

**•** In Unified Messaging channels, the MessagingChannelUsage record represents the status of a connected Service Cloud or Marketing
Cloud application. For example, if a WhatsApp Unified Messaging channel is connected to both Service Cloud and Marketing Cloud,
the MessagingChannel record has two associated MessagingChannelUsage records with a `DeploymentType` of `Conversation`
and `MJ`, respectively. These MessagingChannelUsage records are created when a user selects the Marketing or Service application
during Unified Messaging setup.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects MessagingChannelUsage

Fields

**Field** **Details**

```
ConsentType

DeploymentStatus

DeploymentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of customer consent required for your business to message a customer on this
channel. Customers can opt out at any time.

Possible values are:

**•** `Implicit Opt-In` : By sending an initial message to your business, the customer
agrees to receive messages.

**•** `Explicit Opt-In` : The customer uses keywords to actively opt into receiving
messages.

**•** `Double Opt-In` : The customer uses keywords to opt in twice to receiving messages.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the connected channel or application. If the DeploymentStatus is `Active`,
messages can be sent or received (if permitted).

Possible values are:

**•** `New` —Admin selected the Marketing or Service application in Unified Messaging Setup,
or created a new enhanced WhatsApp, Facebook Messenger, Apple Messages for Business,
or LINE channel on the Messaging Settings page in Setup.

**•** `Provisioning` —Admin clicked **Connect** on an application in Unified Messaging
Setup, or **Activate** on an enhanced Messaging channel.

**•** `Active` —Provisioning was successful and the channel can be used to message with
customers via the connected application or channel.

**•** `Error` —Provisioning or deprovisioning wasn’t successful. The admin can retry.

**•** `Deprovisioning` —Admin clicked **Disconnect** on an application in Unified
Messaging Setup, or **Deactivate** on an enhanced Messaging channel.

**•** `Disabled` —Deprovisioning was successful and the channel or application can no
longer be used to message with customers.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects MessagingChannelUsage

**Field** **Details**

**Description**
Indicates whether the record is related to Service Cloud or Marketing Cloud.

Possible values are:

**•** `Conversation` —Relating to Service Cloud.

**•** `MessagingEngagement` —Relating to Marketing Cloud.

**•** `MJ` —Relating to Marketing Cloud. J stands for Journey Builder.

```
DisabledTime

ErrorReason

MessagingChannelId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time the MessagingChannelUsage record entered the Disabled state after an admin
clicked **Disconnect** or **Deactivate** on the application or channel.

When the record is disabled, all inbound and outbound messages aren’t sent via the
connected application. Any sessions with a status other than Ended or Error are automatically
ended within 48 hours unless the MessagingChannelUsage record is reenabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If an error occurs during connection, activation, disconnection, or deactivation of a
MessagingChannelUsage record, the ErrorReason provides more information about what
went wrong. For example, if an associated Service Cloud application for a Unified Messaging
channel is missing a fallback queue or consent keywords, the connection attempt fails with
an ErrorReason of `ProvisioningError` .

Possible values are:

**•** `DeprovisioningError`

**•** `InternalError`

**•** `InvalidSelection`

**•** `ProvisioningError`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects MessagingConfiguration

**Field** **Details**

**Description**
The enhanced Messaging channel or Unified Messaging channel that the
MessagingChannelUsage record is associated with. A MessagingChannel can be associated
with up to three MessagingChannelUsage records.

This field is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

```
RoutingOverride

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Applicable only to MessagingChannelUsage records with a deployment type of MJ (Marketing
Cloud). RoutingOverride indicates how messages are delivered in a unified channel where
both the Service and Marketing applications are connected.

Possible values are:

**•** `MJKeywordsOnly` —If a messaging user sends a marketing keyword that is defined
in Journey Builder, Journey Builder handles the message delivery and response. If a
messaging user sends a non-keyword message, Omni-Channel handles the message
delivery and response.

**•** `NonSessionMessages` —If a messaging user is engaged in an active Service Cloud
messaging session, Service Cloud handles message delivery and response. If the user
isn’t engaged in an active session, Journey Builder handles message delivery and response.

Regardless of the RoutingOverride value, outbound messages are always handled by Service
Cloud if the messaging user is engaged in an active Service Cloud messaging session. A
session is considered active if its status isn't Ended or Error.

### MessagingConfiguration

Represents the details for a Messaging configuration. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects MessagingConfiguration

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

MessagingServiceUrl

ProvisioningServiceUrl

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name for this Messaging configuration.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of this Messaging configuration.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the Messaging configuration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the Messaging service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the provisioning service.


### Standard Objects MessagingDeliveryError MessagingDeliveryError

Represents a log of triggered outbound failures to verify when a triggered outbound has failed. This object is available in API version
44.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CreatedById

CreatedDate

DestinationPhoneNumber

FailureReason

```

**Type**
reference

**Properties**
Defaulted on createFilter, Group, Sort

**Description**
ID of the user who created the error.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date the error was created.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recipient of the phone call.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The provided reason for why the message failed.


Standard Objects MessagingDeliveryError

**Field** **Details**

```
FlowEntity

FullMessage

Id

IsDeleted

LastModifiedById

LastModifiedDate

MessagingChannelId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entity that triggered the flow to send the message.

**Type**
textarea

**Description**
Plain error text.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
Identifier of the error.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the error has been deleted.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the user who last modified the error log.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the Messaging error log was last modified.

**Type**
reference


Standard Objects MessagingDeliveryError

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the MessagingChannel on page 3414.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

```
MessagingEndUserId

MessagingTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier for the Messaging user.

This is a relationship field.

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Messaging template used.

This is a relationship field.

**Relationship Name**
MessagingTemplate

**Relationship Type**
Lookup

**Refers To**
MessagingTemplate


### Standard Objects MessagingEndUser

**Field** **Details**

```
Name

SystemModstamp

Type

### MessagingEndUser

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Namefield, Sort

**Description**
Name of the error. Maximum length is 80 characters.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
System modification time for the Messaging delivery error log.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The kind of event that occurred. Possible values include:

**•** `Error` (Default)

**•** `Warning`

Represents a single address—such as a phone number or Facebook page—communicating with a single Messaging channel. This
object is available in API version 40.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects MessagingEndUser

Fields

**Field** **Details**

```
AccountId

ContactId

HasInitialResponseSent

IsFullyOptedIn

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Account associated with this Messaging end user. Available in API version 43.0 and
later.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated Contact. Available in API version 43.0 and later.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an initial response has been sent to the Messaging end user ( `true` ) or
not ( `false` ).

**Type**
boolean


Standard Objects MessagingEndUser

**Field** **Details**

**Properties**
Defaulted on create, Filter, Sort

**Description**
Indicates whether the Messaging end user has opted in to receiving messages ( `true` ) or
not ( `false` ). This field compares the related messaging channel’s consent requirement to
the user’s consent status; if the user’s status meets the channel’s required consent level,
`IsFullyOptedIn` is set to `true` . Available in API version 48.0 and later.

```
IsOptedOut

IsoCountryCode

LastReferencedDate

LastViewedDate

LeadId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Messaging end user has opted out of receiving messages. Available
in API version 48.0 and earlier. Use `MessagingConsentStatus` and
`IsFullyOptedIn` instead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ISO country code associated with the Messaging end user.

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


Standard Objects MessagingEndUser

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated lead. Available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

```
Locale

Language

MessageType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The preferred language of the messaging user who participated in the messaging session.
SUpported for Messaging for In-App and Web and Apple Messages for Business only.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel. Available in API version 58.0 and later.

**•** `EmbeddedMessaging` —Represents Messaging for In-App and Web. Available in
API version 50.0 and later.

**•** `Facebook`

**•** `Phone`

**•** `Text`

**•** `Voice`


Standard Objects MessagingEndUser

**Field** **Details**

**•** `WhatsApp`

```
MessagingChannelId

MessagingConsentStatus

MessagingPlatformKey

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging channel associated with the Messaging end user.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consent status of the messaging user. This field is available in API version 48.0 and later.
Possible values are:

**•** `DoublyOptedIn`

**•** `ExplicitlyOptedIn`

**•** `ImplicitlyOptedIn`

**•** `OptedOut`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The phone number, Facebook page ID, or unique key associated with this Messaging end
user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects MessagingLink

**Field** **Details**

**Description**
The name of the Messaging end user. Because this field is editable, we don’t recommend
referencing it in automation. Instead, use the Messaging Platform Key.

```
 OwnerId

 ProfilePictureUrl

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner associated with this Messaging end user.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL of the Messaging end user's profile picture.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingEndUserChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingEndUserHistory**

History is available for tracked fields of the object.

**MessagingEndUserOwnerSharingRule**

Sharing rules are available for the object.

**MessagingEndUserShare**

Sharing is available for the object.

### MessagingLink

Represents the link between a Messaging Channel and where it's shared. This object is available in API version 47.0 and later.


Standard Objects MessagingLink

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
EntityType

MessagingChannelId

RecordTypeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Account`

**•** `Case`

**•** `Contact`

**•** `CustomEntityDefinition` —Custom Object Definition

**•** `Lead`

**•** `Opportunity`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The channel being shared. This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This is a relationship field.

**Relationship Name**
RecordType


### Standard Objects MessagingSession

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
RecordType

```
 ShouldAttemptAutoLink

 ShouldPromptCreate

### MessagingSession

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that an incoming messaging session was auto-linked to a
Salesforce contact or account based on information such as a phone number.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that a contact or account was created for the messaging user if
none existed.

Represents a session on a Messaging channel. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AcceptTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when an agent accepts an incoming Messaging session.


Standard Objects MessagingSession

**Field** **Details**

```
AgentMessageCount

AgentType

CaseId

ChannelEndUserFormula

ChannelKey

```

**Type**
int

**Properties**
Nillable

**Description**
The number of messages sent by the agent during the session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of agent that is assigned to the Messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `BotToAgent` —Bot & Agent

**•** `System` —Used for triggered outbound messages

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with this Messaging session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A concatenation of the Messaging channel and Messaging user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the associated Messaging channel.


Standard Objects MessagingSession

**Field** **Details**

```
ChannelLocale

ChannelName

ChannelType

ConversationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The locale of the associated Messaging channel.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated Messaging channel.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated Messaging channel. Possible values are:

**•** `Alexa`

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `EmbeddedMessaging` —Available in API version 55.0 and later.

**•** `Facebook`

**•** `GoogleHome`

**•** `Line`

**•** `Omega`

**•** `Phone`

**•** `Text`

**•** `Voice`

**•** `WeChat`

**•** `WebChat`

**•** `WhatsApp`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related conversation. Available in API version 55.0 and later.


Standard Objects MessagingSession

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
Conversation

```
EndedByType

EndTime

EndUserAccountId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Who or what ended the enhanced messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `System` :

**–** The session is inactive for a while, so the session ends.

**–** An automation ends the session.

**–** The session ended because of an error.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session ended.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the end user's account record.

This is a relationship field.

**Relationship Name**
EndUserAccount

**Relationship Type**
Lookup


Standard Objects MessagingSession

**Field** **Details**

**Refers To**
Account

```
EndUserContactId

EndUserLanguage

EndUserMessageCount

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the end user's contact record.

This is a relationship field.

**Relationship Name**
EndUserContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The preferred language of the messaging user who participated in the messaging session.

**Type**
int

**Properties**
Nillable

**Description**
The number of messages sent by the Messaging end user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


Standard Objects MessagingSession

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

```
LeadId

MessagingChannelId

MessagingEndUserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Lead associated with this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging channel associated with this Messaging session.

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
Create, Filter, Group, Sort

**Description**
The ID of the Messaging end user associated with this Messaging session.

This is a relationship field.

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser


Standard Objects MessagingSession

**Field** **Details**

```
Name

OpportunityId

Origin

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the opportunity record associated with this Messaging session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The origin of this Messaging session. Possible values are:

**•** `AgentInitiated`

**•** `ConversationClose` —Messaging user deleted the conversation in Apple Messages

**•** `ConversationControlLost` —Third-party bot resumes control from Salesforce
bot or agent

**•** `Help`

**•** `InboundInitiated`

**•** `OptIn` —Opt In Status Change

**•** `OptOut` —Opt Out Status Change

**•** `TriggeredOutbound`

Messaging sessions can’t be created using Apex code. They can be created only through
customer initiation or by using Process Builder, flows, or the Start Conversation action.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner associated with this Messaging session.

This is a polymorphic relationship field.


Standard Objects MessagingSession

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PreviewDetails

SessionKey

StartTime

Status

```

**Type**
string

**Properties**
Nillable

**Description**
The preview shown to an agent for this Messaging session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier for the Messaging session.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session started.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the Messaging session. Possible values are:

**•** `New` (standard channels only)

**•** `Active`

**•** `Consent` (enhanced channels only)

**•** `Waiting`

**•** `Paused` (enhanced channels only)

**•** `Inactive` (enhanced channels only)

**•** `Ended`


Standard Objects MessagingSession

**Field** **Details**

**•** `Error` (enhanced channels only)

[To learn more about these statuses, see Lifecycle of a Messaging Session in Salesforce Help.](https://help.salesforce.com/s/articleView?id=service.messaging_life_cycle.htm&type=5&language=en_US)

```
 TargetUserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the target user associated with this Messaging session.

This is a relationship field.

**Relationship Name**
TargetUser

**Relationship Type**
Lookup

**Refers To**
User

To monitor messaging session activity, report on the MessagingSession and MessagingSessionMetrics on page 3447 objects.
[MessagingSessionMetrics captures metrics about a messaging session, such as agent and end user response time. See Report on](https://help.salesforce.com/s/articleView?id=service.messaging_reporting.htm&type=5&language=en_US)
[Messaging Activity in Service Cloud.](https://help.salesforce.com/s/articleView?id=service.messaging_reporting.htm&type=5&language=en_US)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingSessionChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingSessionFeed**

Feed tracking is available for the object.

**MessagingSessionHistory**

History is available for tracked fields of the object.

**MessagingSessionOwnerSharingRule**

Sharing rules are available for the object.

**MessagingSessionShare**

Sharing is available for the object.


### Standard Objects MessagingSessionMetrics MessagingSessionMetrics

Represents a metric gathered about a specific enhanced messaging session, such as average agent response time. This object is available
starting in October 2024 in API version 62.0 and later.

To reference this object in reports, create a custom report type with Messaging Session as the primary object and Messaging Session
Metrics as the secondary object.

Be sure to include the `MessagingSessionMetricType` field in your custom report. These records are available only for Messaging
sessions created after October 1, 2024.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Multiple MessagingSessionMetrics records are generated when a session ends in an enhanced Messaging channel or Messaging for
In-App and Web channel. These records aren't generated for standard messaging sessions.

Fields

**Field** **Details**

```
MessagingSessionId

MessagingSessionMetricType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related messaging session.

This field is a relationship field.

**Relationship Name**
### MessagingSession

**Relationship Type**
Master-detail

**Refers To**
MessagingSession (the master object)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The metric that this record captures.

Possible values are:


### Standard Objects MessagingTemplate

**Field** **Details**

**•** `AgentMessageCount` —The number of messages sent by the agent in the session.

**•** `ServiceRepFirstResponseTime` —The time when a Service rep sends their
first response to a customer.

**•** `AverageAgentResponseTime` —The average number of seconds between an
end user's message and the agent’s response in the session.

**•** `AverageEndUserResponseTime` —The average number of seconds between
an agent or bot’s message and the end user's response in the session.

**•** `EndUserMessageCount` —The number of messages sent by the end user in the
session.

**•** `MaxAgentResponseTime` —The longest span of time (in seconds) between an
end user's message and the agent’s response in the session.

**•** `MaxEndUserResponseTime`                   - The longest span of time (in seconds) between
an agent or bot’s message and the end user's response in the session.

For each closed messaging session in enhanced Messaging channels and Messaging for
In-App and Web, one MessagingSessionMetrics record is generated per
MessagingSessionMetricType value. This means that six MessagingSessionMetrics records
are generated per session.

```
MessagingSessionMetricValue

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The value of the measured metric. For example, if the MessagingSessionMetricType is
`EndUserMessageCount`, a MessagingSessionMetricValue of `12` means that the end
user sent 12 messages during the messaging session.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An autogenerated number identifying the MessagingSessionMetrics record.

### MessagingTemplate

Represents a Messaging template used to send pre-formatted messages. This object is available in API version 47.0 and later.


Standard Objects MessagingTemplate

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

Message

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the Messaging template.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the Messaging template.

**Type**
textarea

**Properties**
Create, Update


### Standard Objects MetadataApiOpEventLog

**Field** **Details**

**Description**
The body text of the Messaging template.

### MetadataApiOpEventLog MetadataApiOpEventLog stores details of Metadata API retrieval and deployment requests. This object is available in API version 62.0

and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIdentifier

ClientIp

CpuTime

```

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

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects MetadataApiOpEventLog

**Field** **Details**

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

```
LoginKey

OperationType

RequestIdentifier

RunTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

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
Globally unique id for a given request.

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort


### Standard Objects MetadataPackage

**Field** **Details**

**Description**
The amount of time that the request took in milliseconds.

```
SessionKey

Timestamp

Uri

UserIdentifier

### MetadataPackage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

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
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

Represents a package that has been developed in the org you’re logged in to. Applies to unlocked, unmanaged, first-generation, and
second-generation managed packages.


Standard Objects MetadataPackage

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
Name

NamespacePrefix

PackageCategory

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For first-generation and second-generation managed packages, and unlocked
packages with namespaces, this field is the namespace prefix assigned to the
package. For unmanaged packages, or no-namespace unlocked packages, this
field is blank.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of package. Valid values are:

**•** `Application` (internal use only)

**•** `Module` (internal use only)

**•** `Package` —Represents either an unmanaged package or a first-generation
managed package.

**•** `Package2` —Represents either an unlocked package or a second-generation
managed package.

The default value is Package.

This field is available in API version 49.0 and later.


### Standard Objects MetadataPackageVersion

Usage

Here are examples of the types of API queries you can perform.

**Query** **String**

Show all managed and unmanaged packages in the org `SELECT Name, NamespacePrefix FROM`

### `MetadataPackage`

Show only managed packages in the org

### MetadataPackageVersion

```
SELECT Name, NamespacePrefix FROM

MetadataPackage WHERE NamespacePrefix <>

''

```

Represents a package version (managed or unmanaged) that has been uploaded from the org you’re logged in to.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
BuildNumber

IsDeprecated

MajorVersion

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The build number of the version. For example, if you upload two beta versions,
they have build numbers 1 and 2. Then, when you upload a non-beta version,
the build number is 3. When you upload a new version, the build number resets
to 1.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the package version is deprecated. Available in API version
46.0 and later.

**Type**
int


Standard Objects MetadataPackageVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first number in a package version number. A version number either has an
`x.y` format or an `x.y.z` format. The `x` represents the major version, `y` the
minor version, and `z` the patch version.

```
MetadataPackageId

MinorVersion

Name

PatchVersion

ReleaseState

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character package ID starting with `033` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The second number in a package version number. A version number either has
an `x.y` format or an `x.y.z` format. The `x` represents the major version, `y`
the minor version, and `z` the patch version.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package version.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The third number in a package version number, if present. A version number
either has an `x.y` format or an `x.y.z` format. The `x` represents the major
version, `y` the minor version, and `z` the patch version.

**Type**
picklist


Standard Objects MetadataPackageVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the package version is a beta version, the value is `Beta` . Otherwise, the value
is `Released` .

Usage

Here are examples of the types of API queries you can perform.

**Query** **String**

Get all package versions for the package that has a `SELECT Id, Name, ReleaseState,`
`MetadataPackageID` of 033D00000001xQlIAI `MajorVersion, MinorVersion, PatchVersion`

```
                             FROM MetadataPackageVersion WHERE

                             MetadataPackageId = '033D00000001xQlIAI'

```

Get the package version for the package with a specific
`MetadataPackageID` and a major version greater than 1

Get released package versions for the package with a specific

```
MetadataPackageID

```

**Java Code Sample**

```
SELECT Id FROM MetadataPackageVersion WHERE

MetadataPackageId ='033D00000001xQlIAI'

AND MajorVersion > 1

SELECT Id FROM MetadataPackageVersion WHERE

MetadataPackageId = '033D00000001xQlIAI'

AND ReleaseState = 'Released'

```

Suppose you want to push version 3.4.6 of your package to all orgs. Let’s write some code to identify the orgs eligible for the upgrade.
This example demonstrates how to generate the list of subscriber orgs eligible to be upgraded to version 3.4.6 of a package.

This code sample uses the Web Services Connector (WSC).

```
// Finds all Active subscriber orgs that have the package installed

String PACKAGE_SUBSCRIBER_ORG_KEY_QUERY = "Select OrgKey from PackageSubscribers where

OrgStatus = 'Active' and InstalledStatus = 'I'";

// Finds all MetadataPackageVersions lower than the version given, including the list

// of subscribers for each version

String METADATA_PACKAGE_VERSION_QUERY = "Select Id, Name, ReleaseState, (%s) from"

 + " MetadataPackageVersion where MetadataPackageId = '%s' AND ReleaseState = 'Released'"

 + " AND (MajorVersion < 3 OR (MajorVersion = 3 and MinorVersion < 4)"

 + " OR (MajorVersion = 3 and MinorVersion = 4 and PatchVersion < 6))";

// conn is an EnterpriseConnection instance initialized with a ConnectionConfig object

// representing a connection to the developer org of the package

QueryResult results = conn.query(String.format(METADATA_PACKAGE_VERSION_QUERY,

PACKAGE_SUBSCRIBER_ORG_KEY_QUERY));

```


### Standard Objects Metric

```
   // This list will hold all of the PackageSubscriber objects that are eligible for upgrade

   // to the given version

   List<PackageSubscriber> subscribers = new ArrayList<>();

   for (SObject mpvso : results.getRecords()) {

     // Cast the sObject to a MetadataPackageVersion

     MetadataPackageVersion mpv = (MetadataPackageVersion) mpvso;

     // Add subscribers to our list

     if (mpv.getPackageSubscribers() != null) {

     for (SObject psso : mpv.getPackageSubscribers().getRecords()) {

      subscribers.add((PackageSubscriber) psso);

     }

    }

   }

```

**Next Step**

Create a push request using PackagePushRequest.

### Metric

The Metric object represents the components of a goal metric such as its name, metric type, and current value.

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CompletionDate

CurrentValue

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the metric.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


Standard Objects Metric

**Field Name** **Details**

**Description**
The current value of the metric.

```
Description

DueDate

GoalId

InitialValue

IsCompletionMetric

LastComment

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the metric. The maximum length is 65,535 characters.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The due date of the metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the goal the metric is related to.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The initial value of the metric.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. If `true`, the metric measures whether or not the metric is finished.
If `false`, the metric measures how much is finished compared to a targeted
value.

**Type**
textarea


Standard Objects Metric

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A comment that provides more context about the metric, such as its status or
progress. The maximum length is 255 characters.

```
LastReferencedDate

LastViewedDate

Name

OwnerId

Progress

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this metric.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed this metric. If this value is
null, this record might have been only referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the metric.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the metric.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects Metric

**Field Name** **Details**

**Description**
Read only. The overall progress of the metric.

```
RecordTypeId

StartDate

Status

TargetValue

Weight

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the related record type.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the metric.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the metric. Possible values include:

**•** Not Started

**•** On Track

**•** Behind

**•** Critical

**•** Completed

**•** Postponed

**•** Canceled

**•** Not Completed

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The target value of the metric.

**Type**
double


### Standard Objects MetricDataLink

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The weight of the metric. The sum of the weights should equal 100%.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricFeed**

Feed tracking is available for the object.

**MetricHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricShare**

Sharing is available for the object.

### MetricDataLink

The link between the metric and the data source, such as a report.

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DatasourceFieldName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MetricDataLink

**Field Name** **Details**

**Description**
The field name of the data source, such as a report summary field.

```
DataSourceId

LastSynchronizationTime

Name

TargetId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the data source.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time the data was synchronized.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name given to the data link record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the metric that the data is linked to.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricDataLinkHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)


### Standard Objects MigratedEmail MigratedEmail

For internal use only.

### MilestoneType

Represents a milestone (required step in a customer support process). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
Description

Name

RecurrenceType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
A description of the milestone.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
The name of the milestone.

**Type**
picklist

**Properties**
Create,Update

**Description**
The type of recurrence for the milestone.


### Standard Objects MktJourneyDcsnSetup

Usage

Use this object to query and manage the milestone type for CaseMilestone records.

SEE ALSO:

CaseMilestone

SlaProcess

### MktJourneyDcsnSetup

Represents a collection of Marketing Cloud Engagement journeys that you can interact with by using Salesforce Flow in Marketing Cloud.
This object is available in API version 65.0 and later.

You can use interaction data from a Marketing Cloud Engagement journey to trigger a Flow, or to configure decision activities in a Flow.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessUnitId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique Marketing Cloud business unit ID to use with the collection of journeys. This ID
is configured in Marketing Cloud, and is different from the Member ID (MID) or Enterprise
ID (EID) of your Marketing Cloud Engagement account.

This field is a relationship field.

**Relationship Name**
BusinessUnit

**Refers To**
BusinessUnit

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the collection of journeys.


### Standard Objects MLField

**Field** **Details**

```
EnterpriseIdentifier

Name

### MLField

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Enterprise ID (EID) of your parent Marketing Cloud Engagement account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A name for the collection of journeys.

Represents a single field in a data definition. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Entity

Field

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object that contains the field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field.


### Standard Objects MlIntentUtteranceSuggestion MlIntentUtteranceSuggestion

Represents a customer input, used for training purposes in the feedback loop process of a conversation. Admins can add these inputs
to the intent training model. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ConfigId

IntentSuggestion

ReviewStatus

Utterance

UtteranceCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended intent.

**Type**
picklist

**Properties**
Filter, Group, Restricted Picklist, Sort

**Description**
Possible values are: Ignore, New

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text input from the end user.

**Type**
integer

**Properties**
Filter, Group, Sort


### Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
A count of the Utterance field.

### MLPredictionDefinition

Represents a prediction definition that specifies details about the prediction. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApplicationId

DeveloperName

Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the parent AI Application.

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


Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
The language of the prediction. Possible values are:

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

```
MasterLabel

NamespacePrefix

PredictionField

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the prediction throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the prediction, if installed with a managed package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
Field that the prediction is based on.

```
PushbackField

Status

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field that the prediction writes scores to.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the prediction. Possible values are:

**•** `Disabled`

**•** `Draft`

**•** `Enabled`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of model that returns the prediction values. Possible values are:

**•** `BinaryClassification`

**•** `DeepLearningIntentClassification`

**•** `DeepLearningNameEntityRecognition`

**•** `GlobalDeepLearningIntentClassification`

**•** `GlobalDeepLearningNameEntityRecognition`

**•** `LanguageDetection`

**•** `MulticlassClassification`

**•** `Regression`

**•** `ScoringSpecificOutcome`


### Standard Objects MLModel MLModel

Represents an AI model that can be used in Einstein Prediction Builder, Einstein Recommendation Builder, and other Einstein features.
This object is available in API version 53.0 and later.

This object contains information that represents many types of AI models. Some fields contain information for only a specific type of
model.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
ApprovalStatus

Dataset

ModelType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the model is approved, pending approval, or rejected.

Possible values are:

**•** `Approved`

**•** `Pending`

**•** `Rejected`

The default value is `Pending` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dataset used to create the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects MLModel

**Field** **Details**

**Description**
Indicates the type of model.

Possible values are:

**•** `BinaryClassification`

**•** `DecisionTree`

**•** `DeepLearningIntent`

**•** `DeepLearningNER`

**•** `GeneralizedLinearModels`

**•** `GlobalDeepLearningIntent`

**•** `GlobalDeepLearningNER`

**•** `GlobalLanguageDetection`

**•** `GradientBoostedTrees`

**•** `LinearRegression`

**•** `LinearSupportVectorClassifiers`

**•** `LogisticRegression`

**•** `MulticlassClassification`

**•** `NaiveBayes`

**•** `NeuralNet`

**•** `PopularityCount`

**•** `RandomForest`

**•** `Regression`

**•** `XGBoost`

```
Name

PredictionDefinitionId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related prediction definition.

This field is a relationship field.

**Relationship Name**
PredictionDefinition


Standard Objects MLModel

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

```
RecommendationDefinitionId

ScoringStatus

TrainingEndTime

TrainingStartTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related recommendation definition.

This field is a relationship field.

**Relationship Name**
RecommendationDefinition

**Relationship Type**
Lookup

**Refers To**
MLRecommendationDefinition

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether scoring is enabled or disabled.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the date and time when the training ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects MLModelFactor

**Field** **Details**

**Description**
Indicates the date and time when the training started.

### MLModelFactor

Represents a field value that has a positive or negative effect on the model’s score. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
Correlation

FactorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows the strength of association between the variable and the outcome. The higher the
correlation, the greater the association.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of factor.

Possible values are:

**•** `ModelFactlet` —The field value strongly influences the outcome because the model
determined that this field is always important. For example, the model can decide that
the field `Industry` is always important to the outcome, regardless of its value.

**•** `ModelFactor` —The field value is important to the outcome because the field’s value
is significant. For example, the model can decide that the `Annual Revenue` field
value is important to the outcome because the value is above $1,000,000 or below
$50,000.


Standard Objects MLModelFactor

**Field** **Details**

```
Importance

ModelId

Name

Type

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows how much the variable influences the outcome. The higher the value, the greater
the impact.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related model.

This field is a relationship field.

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
The automatically generated ID that uniquely identifies the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of model factor.

Possible values are:

**•** `And`

**•** `Basic`

**•** `Or`


### Standard Objects MLModelFactorComponent

**Field** **Details**

```
Weight

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how significant the field value is to the outcome or score. Model factlets tend to
have higher weights than model factors.

### MLModelFactorComponent

Represents information about the related MLModelFactor. For example, this object can represent a field value or a field range such as
“Title = CEO” or “Annual Revenue >10000000”. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
FactorLabelKey

FeatureType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maps the model factor component to a label that can be displayed to the user.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
`FeatureType` and `FeatureValue` indicate a feature that doesn’t have a corresponding
field. For example, to indicate the feature “Percent = 97%”, the `FeatureType` is `Percent`
and the `FeatureValue` is `97` .

Possible values are:


Standard Objects MLModelFactorComponent

**Field** **Details**

**•** `Binary`

**•** `Combobox`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `ID`

**•** `Integral`

**•** `MultiPicklist`

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `Real`

**•** `Text`

**•** `TextArea`

**•** `URL`

```
FeatureValue

LeftHandDerivedField

ModelFactorId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feature’s value. See `FeatureType` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the left side of the equation. For example, if the model factor component is `Title =`
`CEO`, this value is `Title` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModelFactor.

This field is a relationship field.


Standard Objects MLModelFactorComponent

**Field** **Details**

**Relationship Name**
ModelFactor

**Relationship Type**
Lookup

**Refers To**
MLModelFactor

```
ModelId

Name

Operator

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related MLModel.

This field is a relationship field.

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
The automatically generated ID that uniquely identifies the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the model factor component is an equation, this field represents the operator. For example,
if the model factor component is `Title = CEO`, the operator is `Equals` .

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`


### Standard Objects MLModelMetric

**Field** **Details**

**•** `IsNotNull`

**•** `IsNull`

**•** `LessThan`

**•** `NotEquals`

**•** `StartsWith`

```
RightHandDerivedField

SortOrder

Value

### MLModelMetric

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the right side of the equation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor has multiple model factor components, this field indicates the order in
which this model factor component appears.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component specifies a value, this field represents the value. For example,
if the model factor component is `Title = CEO`, this field is `CEO` .

Represents a metric or statistic about the related model, such as accuracy, precision, or RSquared. Use a model’s metrics to learn about
its performance and to compare it with other models. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects MLModelMetric

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
BasicMetricValue

ComplexMetricValue

DataSetType

EndTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of a basic metric. A basic metric is a single number. For metrics that comprise a
set of graph points, see `ComplexMetricValue` .

**Type**
textarea

**Properties**
Nillable

**Description**
The X and Y values for a complex metric. A complex metric is a coordinate on a graph. For
example, in classification models, you can use a line on a graph to create classification
categories.

**Type**
picklist

**Properties**
