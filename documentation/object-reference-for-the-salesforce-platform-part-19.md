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

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkGoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
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

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
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

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
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

LocationId

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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
reference


Standard Objects WorkPlanSelectionRule

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the location.

```
OwnerId

Product2Id

ServiceTerritoryId

WorkPlanSelectionRuleNumber

WorkPlanTemplateId

WorkTypeId

```

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

**Type**
reference


### Standard Objects WorkPlanTemplate

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type.

Associated Objects

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

**Properties**
Create, Nillable, Update


Standard Objects WorkPlanTemplate

**Field** **Details**

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

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner who created the work plan template.


### Standard Objects WorkPlanTemplateEntry

**Field** **Details**

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

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
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

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundShare**

Sharing is available for the object.

### WorkRewardFundType

Represents the type of WorkRewardFund object.

Note: The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information,
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

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring '22. This object isn't available as of API version 54.0. For more information, see
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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects WorkThanks

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
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

AccountInsight object 281
AccountUserTerritory2View object 334
AnalyticsLicensedAsset object 544

B

Big Objects
Composite primary key 33
Custom Big Object 33
Defining 33
Deploying 33
# Index 33

Overview 31

C

ContactSuggestionInsight object 1459

D

Data access
standard objects 27
Delegated Account Objects 1848

E

Electronic_Media_Group_object 1911
Electronic_Media_Use_object 1913
External Account Hierarchy History Object 2497
External_Account_Hierarchy_object 2494
ExternalSocialAccount object 2514

F

FormulaFunction object 2814
FormulaFunctionCategory object 2817
Freeze users 5657

H

HealthCareDiagnosis object 2907
HealthCareProcedure object 2911

# I

IframeWhiteListUrl object 2937

L

LandingPage object 3065

M

Managed_Content 3384
Managed_Content_Channel 3387
Managed_Content_Channelobject 3387
Managed_Content_Info_object 3389
Managed_Content_object 3384
Managed_Content_Variant 3392
Managed_Content_Variant_object 3392
MarketingForm object 3395
MarketingLink object 3398

O

Object_name object 4821
ObjectPermissions object 3602
Objects
AccountInsight 281
AccountUserTerritory2View 334
AnalyticsLicensedAsset 544
ContactSuggestionInsight 1459
Electronic_Media_Group 1911
Electronic_Media_Use 1913
External_Account_Hierarchy 2494
ExternalSocialAccount 2514
FormulaFunction 2814
FormulaFunctionCategory 2817
HealthCareDiagnosis 2907
HealthCareProcedure 2911
IframeWhiteListUrl 2937
LandingPage 3065
LightningExperienceTheme 3162
Managed_Content_Info 3389
MarketingForm 3395
MarketingLink 3398
Object_name 4821
ObjectPermissions 3602
OmniSupervisorConfig 3615
OmniSupervisorConfigAction 3617
OmniSupervisorConfigGroup 3618
OmniSupervisorConfigProfile 3619
OmniSupervisorConfigUser 3624
OpportunityContactRoleSuggestionInsight 3661
OpportunityInsight 3668
PermissionSet 4150
PermissionSetGroup 4138, 4140
Product_Attribute 4339


**Index**

Objects _(continued)_
Product_Attribute_Set 4340
Product_Attribute_Set_Item 4342
Product_Attribute_Set_Product 4343
Product_Category 4347, 4350
Product_Media 4372
Prompt 4485, 4498
PromptAction 4476, 4480
PromptActionOwnerSharingRule 4482
PromptActionShare 4483, 4487
Recommendation 4632
Sales_Store_Catalog 4803
SocialPersona 5106
SocialPost 5112
SurveyQuestionScore 5179
UiFormulaCriterion 5481
UiFormulaRule 5483
VoiceCallQualityFeedback 5819
WebStore 5888, 5912
WebStoreCatalog 5900
OmniSupervisorConfig object 3615
OmniSupervisorConfigAction object 3617
OmniSupervisorConfigGroup object 3618
OmniSupervisorConfigProfile object 3619
OmniSupervisorConfigUser object 3624
OpportunityContactRoleSuggestionInsight object 3661
OpportunityInsight object 3668

P

PermissionSetGroup object 4138

PermissionSetGroupComponent object 4140
PermissionSetTabSetting object 4150
Product_Attribute_object 4339
Product_Attribute_Set_Item_object 4342
Product_Attribute_Set_object 4340
Product_Attribute_Set_Product_object 4343
Product_Category_object 4347, 4350
Product_Media_object 4372

R

Recommendation object 4632

S

Sales_Store_Catalog_object 4803
SocialPersona object 5106
SocialPost object 5112
Standard objects
data access 27
SurveyQuestionScore object 5179

U

UiFormulaCriterion object 5481
UiFormulaRule object 5483

V

VoiceCallQualityFeedback object 5819

W

WebStore object 5888, 5912
WebStoreCatalog_object 5900

