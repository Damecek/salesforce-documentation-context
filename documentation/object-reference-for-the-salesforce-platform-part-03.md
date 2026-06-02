The type of step that this rule applies to. Possible values are:

**•** `BranchStep`                     - The rule evaluates the condition of a branch step. A branch step
is an ActionCadenceStep record with the field `type` equal to `Branch` .

**•** `RepeatedStep`                     - The rule evaluates the repeat steps for quick cadence. Available
in API version 58.0 and later.

**•** `RootStep`                     - The rule evaluates a global exit condition.

**•** `SubRootStep` —Available in API version 58.0 and later.

This field is available in API version 49.0 and later.

Usage

Use ActionCadenceRule to see all the rules associated with a branch step:

```
   select RuleName from ActionCadenceRule where ActionCadenceStep.ActionCadence.Name = "High

    Priority CFO"

```

SEE ALSO:

### ActionCadence ActionCadenceRuleCondition

ActionCadenceStep

ActionCadenceStepTracker

### ActionCadenceRuleCondition

Represents the logic for a branch step. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionCadenceRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ActionCadenceRuleCondition

**Field** **Details**

**Description**
The ID of the ActionCadenceRule that this condition is associated with.

```
Operator

Resource

RuleConditionName

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The conditional operator for this rule. Possible values are:

**•** `Equal`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to evaluate. Possible values are:

**•** `CallDispositionCategory`

Use by branch steps.

**•** `EmailEngagement`

Used by ListenerBranch steps.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the rule condition. Every rule condition in a cadence must have a unique name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The event that your cadence rule condition listens for to decide when the event is complete.

Possible values for emails are:

**•** `EmailOpen`

**•** `EmailLinkClick`

Possible values for calls are:


### Standard Objects ActionCadenceStep

**Field** **Details**

**•** `CallMeaningfulConnect`

**•** `CallUnqualified`

**•** `CallLeftVoicemail`

**•** `CallNotInterested`

**•** `CallCallBackLater`

Usage

Use ActionCadenceRuleContion to see all the rule conditions associated with a branch step:

```
   select RuleConditionName from ActionCadenceRuleCondition where ActionCadenceStepId= <ID

   of a branch step>

```

SEE ALSO:

### ActionCadence

ActionCadenceRule

### ActionCadenceStep ActionCadenceStepTracker ActionCadenceStep

Represents a step in a cadence. Use ActionCadenceStep to learn which steps belong to a cadence, and how the steps are connected to
each other. This object is available in API version 48.0 and later.

An ActionCadenceStep record is created to represent a step. If the step is a branch step, then corresponding ActionCadenceRule and
ActionCadenceRuleCondition records are also created.

Note: An ActionCadenceStep with `IsOrphan` equal to `true` can be part of a cadence but is never executed. To retrieve the
steps that can be executed by the cadence, query for ActionCadenceStep records with `IsOrphan` equal to `false` .
### ActionCadenceStep records with IsOrphan equal to true are deleted.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
ActionCadenceId

```

**Type**
reference


Standard Objects ActionCadenceStep

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ActionCadence that this step belongs to.

This field is a relationship field.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

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
The number of calls having the call outcome **Call Back Later** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Left Voicemail** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Meaningful Connect** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Not Interested** .


Standard Objects ActionCadenceStep

**Field** **Details**

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where the call outcome isn’t categorized.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Unqualified** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that weren’t delivered successfully.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails delivered.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails returned for a permanent reason — for example, the email address
doesn’t exist. This field is available in API version 50.0 and later.

**Type**
int


Standard Objects ActionCadenceStep

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link count towards this total. This field is available in API version 50.0 and later.

```
AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that the target opened while working on this step. Multiple opens of
the same email count towards this total.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were returned because the recipient set an out-of-office responder.
Multiple replies count towards this total. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email count towards this total, This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The number of emails that were returned for temporary reasons — for example, the email
is too large. This field is available in API version 50.0 and later.

```
AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllManuallyCompletedCount

AllOnTimeCompletedCount

AllOverdueCompletedCount

AllSkippedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps manually completed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps completed on time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of overdue steps that were completed.

**Type**
int


Standard Objects ActionCadenceStep

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps skipped.

```
AllTotalCallsCount

BranchDefaultStepName

ChainedCadenceId

GoToStepIntervalInMinutes

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls that the sales rep made during this step.

This field is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the default step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ActionCadence for the linked action cadence. Available only if the step type is
`DaisyChain` (meaning that another action cadence is connected to this action cadence).

This field is a relationship field.

**Relationship Name**
ChainedCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
Contains information about when the step should be repeated next, in minutes. Available
in API version 58.0 and later.

```
GoToStepIterationLimit

GoToStepName

GraphState

HasVariant

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the maximum number of repeat (goto) step iterations allowed. Available in API
version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If this step’s original next step was removed during an edit after activation, this field specifies
the updated next step.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the state of the `ActionCadenceStep` within the step graph, or sequence,
of the action cadence.

Possible values are:

**•** `Included` —This step is part of the step graph.

**•** `Orphaned` —This step was removed from the step graph before the action cadence
was activated. Orphaned steps are deleted upon activation.

**•** `Pending` —This step has been created but hasn’t been added to the step graph.
Pending steps can be added to the step graph in the future.

**•** `Retired` —This step was previously part of an active action cadence step graph and
was removed during an edit after activation. Retired steps can have associated step
trackers.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
This field is valid for email and call step types. If `true`, the step has email or call template
variants. The template variants are defined in ActionCadenceStepVariant records. Available
in API version 53.0 and later.

The default value is `false` .

```
IsImmediateWakeUp

IsOrphan

IsScheduledDueDateLocked

IsScreenFlowActive

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a listener branch is immediate wake up ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, this step isn’t executed by the action cadence and will be deleted. Steps with
`IsOrphan` equal to `true` have `ParentStepName` equal to `null` .

Note: To retrieve the active steps in an action cadence, include `IsOrphan=false`
in your query.

The default value is `false` .

This field is available in API version 49.0 and later.

This field is a calculated field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether assignees can change the due date ( `true` ) or not ( `false` ). Available in
API version 58.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
Indicates whether the flow is active and can be executed ( `true` ) or not ( `false` ).

The default value is `false` .

```
IsStepAutomationActive

IsThreaded

ParentStepName

RootStepId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the flow referenced in the StepAutmationReference field is active. If false, the flow
isn’t active. Only active flows can be executed. The default value is `false` . This field is
available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is valid for email steps. Email steps have ActionCadence.StepType equal to
`SendAnEmail` . If `true`, the email for this email step is sent as a reply to the email
conversation from the previous email step. By sending the email as a reply to a previous
email, customers see a "conversation" view of the emails. Only emails from the same action
cadence are grouped as conversations.

This field can’t be true for the first email step in an action cadence, because the first email
from an action cadence must start a new conversation with the prospect.

The default value is `false` . This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The step name ( `ActionCadenceStep.StepName` ) of the previous step in the action
cadence. Must contain a valid step name value unless this step is the root step. `null` if this
step is a parent step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The ID of the root step for this action cadence. Every action cadence has exactly one root
step (so that the Salesforce API can find all the steps for this cadence).

This field is a relationship field.

**Relationship Name**
RootStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
ScheduledDaysUntilDue

ScheduledDaysUntilStart

ScheduledStartDelayInMinutes

ScheduledStartTimeInMinutes

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days after which this current step is due. Available in API version 58.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days when this step starts after the previous step completes. For delays of
greater than one day from `ScheduledStartTimeInMinutes` . Available in API version
58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Any hard waits in minutes is captured in this field. Waits greater than 1 day need to set
`ScheduledDaysUntilStart` . Available in API version 58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The specific time of day when the step starts. The time represents minutes after 00:00.
Available in API version 58.0 and later.

```
ScreenFlowReference

StepAutomationReference

StepComments

StepName

StepTitle

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The `namespace__fullname` of the screen flow. Used to describe flow objects and
launch flows client side.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that the step uses. Cadence steps can launch a cadence step flow as
the step or as a cadence autolaunched flow when a rep completes the step. The format is
`namespace__fullName` . This field is available in API version 56.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A comment that provides additional information about this step.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier for this step. Generated by Salesforce.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title given to the step when it was created.


Standard Objects ActionCadenceStep

**Field** **Details**

```
TemplateId

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If a template was added to this step, this field contains the template's ID. For example, if this
step is a call step it can contain a template for a call script. Or, if this step is an email step, it
can contain a template for an email.

This field is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of step. Possible values are:

**•** `AutoSendAnEmail`  - Salesforce automatically sends the specified email.

**•** `Branch`  - A branch step in the action cadence.

**•** `Copilot`  - The SDR agent action.

**•** `CreateTask`  - Used for custom steps.

**•** `DaisyChain`  - A daisy chain step. A daisy chain step connects this action cadence
to another action cadence. It must be the last step in the path.

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`  - A branch step for emails.

**•** `MakeACall`  - The sales rep must call the prospect at this step.

**•** `PlatformScreenFlow`

**•** `Root`  - This step is the root step for the action cadence.

**•** `SendAMessage`  - The sales rep must send the prospect a message at this step.

**•** `SendAnEmail`  - The sales rep must send the prospect an email at this step.

**•** `Terminal`  - The engagement monitor.

**•** `Wait`  - A wait step tells the sales rep not to do anything at this point in the action
cadence.


Standard Objects ActionCadenceStep

**Field** **Details**

```
TypeDetail

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

WaitTimeInSeconds

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
More detail about the step type. If the step is a cadence step flow, this field contains the flow
name. Otherwise, this field contains the same value as the Type field. This field is available
in API version 56.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that the target opened as part of this step. Multiple openings of the
same email aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email aren’t counted. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the step type is `Wait` . The time in seconds for this step to wait.


### Standard Objects ActionCadenceStepTracker

Usage

Use ActionCadenceStep to see what steps your action cadence has:

```
   select StepTitle from ActionCadenceStep where ActionCadence.ID= <the id of an action

   cadence> and IsOrphan=false

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceStepChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

### ActionCadence

ActionCadenceRule

ActionCadenceRuleCondition

### ActionCadenceStepTracker ActionCadenceStepTracker

Represents a step in an active cadence for a specific cadence target. This object is available in API version 48.0 and later.

An ActionCadenceStepTracker record is created when a target moves to a new step in a cadence. Use ActionCadenceStepTracker to
find information such as the step's current state, the reason it completed, and its type.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionCadenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ActionCadence that is related to the ActionCadenceStep.

This field is a relationship field.

**Relationship Name**
### ActionCadence


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ActionCadence

```
ActionCadenceName

ActionCadenceStepId

ActionCadenceTrackerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the related ActionCadence object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ActionCadenceStepTracker is the runtime version of an ActionCadenceStep. This field contains
the ID of the related ActionCadenceStep.

This field is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ActionCadenceTracker.

This field is a relationship field.

**Relationship Name**
ActionCadenceTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceTracker


Standard Objects ActionCadenceStepTracker

**Field** **Details**

```
ActionTakenDateTime

BranchIterationCount

Channel

CompletedById

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the action described in this step was taken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a target has entered a specific branch within the cadence. This field is
available in API version 62.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The communication medium used for this step in an active cadence. This field is available
in API version 62.0 and later.

Possible values are:

**•** `Email`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID of the sales rep who completed this step. A step can be assigned to several users
before it’s completed. This field is available in API version 50.0 and later.

This field is a relationship field.

**Relationship Name**
CompletedBy

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects ActionCadenceStepTracker

**Field** **Details**

```
CompletionDate

CompletionReason

DueDateTime

ErrorCode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this step completed. A step is completed either when the action is taken, or the
step is skipped.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that this step completed: Possible values are:

**•** `AutomaticallyCompleted`  - The sales rep successfully completed this step
and moved to the next one. Salesforce automatically marks this step as completed.

**•** `AutomaticallyExited`  - The step exited because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `ManuallyCompleted`  - The sales rep manually marked this step as completed.

**•** `ManuallySkipped`  - The sales rep skipped this step.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Some steps have a due date to indicate when they must be completed. If this step has been
assigned a due date, this field contains the date and time it is due.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AUTO_EMAIL_DAILY_LIMIT_REACHED`

**•** `AUTO_EMAIL_ORG_SETTING_OFF`

**•** `AUTO_LIST_MQ_MAX_RETRIES_FAILED`

**•** `BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED`

**•** `EAC_GLOBAL_DATA_SOURCE_ERROR` —EAC data source error

**•** `EMAIL_ORG_SETTING_OFF`


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**•** `EXCHANGE_MAX_MAILBOX_SIZE` —Max Exchange mailbox size reached

**•** `EXCHANGE_SEND_AS_DENIED`

**•** `FETCH_EMAIL_THREAD_FAILED`

**•** `FIX_WITH_RECONNECT` —Data connection failed

**•** `FROM_ADDRESS_FIELD_IS_ENCRYPTED` —FromAddress field is encrypted

**•** `GOOGLE_MAIL_SERVICE_NOT_ENABLED` —Gmail service not enabled

**•** `INVALID_DRAFT` —Invalid email draft

**•** `INVALID_FROM_ADDRESS`

**•** `INVALID_TARGET_EMAIL`

**•** `INVALID_TEMPLATE_ID`

**•** `INVALID_USER_EMAIL`

**•** `MAIL_PROVIDER_RATE_LIMIT_REACHED` —Email provider rate limit reached

**•** `MALFORMED_QUERY`

**•** `MAX_OUT_EMAIL_THREAD_RETRY`

**•** `MAX_OUT_LLMG_RETRY`

**•** `NON_EMAIL_UNKNOWN_ERROR` —Unknown error

**•** `NO_ACTIVE_ASDR_AGENT`

**•** `NO_ATTACHMENT_ACCESS`

**•** `NO_CONTENT_VERSION_ACCESS`

**•** `NO_LIST_EMAIL_PERMISSION`

**•** `NO_TARGET_ACCESS`

**•** `NO_TOS_SIQ`

**•** `ORG_WIDE_AUTO_EMAIL_LIMIT_REACHED`

**•** `ORG_WIDE_DAILY_EMAIL_LIMIT_REACHED`

**•** `OTHER_REQ_FIELD_MISSING` —Other required field missing

**•** `PARDOT_MERGE_FIELD_RENDERING_ERROR`

**•** `POST_SEND_EXCEPTION`

**•** `RETRIES_MAX_EXCEEDED` —Maximum retries exceeded

**•** `RETRY_LATER`

**•** `SCHEDULED_EMAIL_FAILED` —Unknown error

**•** `SENDER_MAILBOX_NOT_FOUND`

**•** `SHARE_LIMIT_EXCEEDED`

**•** `TARGET_DO_NOT_CONTACT_ON` —Target has Do Not Contact on

**•** `TARGET_EMAIL_BOUNCED`

**•** `TARGET_EMAIL_EMPTY`

**•** `TARGET_HAS_INVALID_ID`

**•** `TARGET_HAS_OPT_OUT_EMAIL`

**•** `TEMPLATE_DELETED`


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**•** `TEMPLATE_EMPTY` —Email subject or body missing

**•** `TEMPLATE_HAS_INVALID_MERGE_FIELD`

**•** `TEMPLATE_IS_INACTIVE`

**•** `TEMPLATE_MERGE_FIELD_RENDERING_ERROR`

**•** `TEMPLATE_NOT_PUBLIC` —No access to template

**•** `TEMPLATE_TOO_LARGE`

**•** `UNKNOWN` —Email unknown error

**•** `USER_HAS_LOST_HVS_ACCESS`

**•** `USER_IS_INACTIVE`

```
GoToStepIterationCount

IsActionTaken

ScheduledStartDateTime

SecondsOverdue

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the action cadence step tracker was created for the same step in a
cadence. Available in API version 58.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the sales rep completed an action during this step, such as making a phone call,
otherwise `false` .

The default value is `false` .

This field is a calculated field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the step starts. Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**Description**
If this step has a due date that has passed, this field contains the number of seconds that
has elapsed since the due date. Once a sales rep takes action on the cadence step, the value
of this field is the number of seconds elapsed between the due date and the time the action
was taken.

This field is a calculated field.

```
State

StepTitle

StepType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The current state of this step. Possible values are:

Possible values are:

**•** `Active`  - The current step that the sales rep is performing. There can only be one
active step for a given target.

**•** `Cancelled`  - The sales rep canceled the step. Salesforce doesn’t run any canceled
steps.

**•** `Completed`  - This step is finished. Either the work in the step completed, or the step
was skipped.

**•** `Error`  - An error occurred while executing this step.

**•** `InProgress`  - The sales rep has started the step, but it isn’t yet completed.

**•** `Paused` —The sales rep paused the step.

**•** `Queued`  - Used for automated email steps. The email step has started but the email
is waiting in the queue to be sent.

**•** `Scheduled`  - Used for email steps. An email can be scheduled to be sent later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the related step.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of step to execute. Possible values are:

**•** `AutoSendAnEmail`


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**•** `Branch`

**•** `Copilot`

**•** `CreateTask`

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow`

**•** `Root`

**•** `SendAMessage`

**•** `SendAnEmail`

**•** `SubRoot`

**•** `Terminal`

**•** `Wait`

```
TargetId

WasEverPaused

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the prospect that is assigned to this cadence.

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the sales rep had ever paused this step ( `true` ), or not ( `false` ). This field
is available in API version 50.0 and later.


### Standard Objects ActionCadenceStepVariant

Usage

List all the steps that this prospect has completed in a given cadence:

```
   select StepTitle from ActionCadenceStepTracker where TargetID = <target ID>

         and ActionCadenceId=<action cadence id> and StepType="Completed"

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceStepTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

### ActionCadence

ActionCadenceRule

### ActionCadenceStep

ActionCadenceRuleCondition

### ActionCadenceStepVariant

Represents an email template or call script variant associated with an action cadence step. Email and call steps can have up to 3 variants
associated so sales teams can compare the engagement results. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Sales Engagement and Allow Email Template and Call Script Variant Testing must be enabled.

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related action cadence step.


Standard Objects ActionCadenceStepVariant

**Field** **Details**

This is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
SplitPercentage

TemplateId

Type

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of emails to send or calls to make using this email template or call script
variant. The total for all variants must be 100%.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated email template or call script.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated action cadence step.

Possible values are:

**•** `AutoSendAnEmail`

**•** `Branch`

**•** `Copilot`

**•** `CreateTask`


### Standard Objects ActionCadenceTracker

**Field** **Details**

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow` —Available in version 55.0 and later.

**•** `Root`

**•** `SendAMessage`

**•** `SendAnEmail`

**•** `Terminal`

**•** `Wait`

Only email and call steps can have an associated action cadence step variant.

Usage

Use ActionCadenceStepVariant to retrieve the email template or call script for an action cadence step:

```
   SELECT SplitPercentage, TemplateId FROM ActionCadenceStepVariant WHERE

   ActionCadenceStepId=:[idValue]

```

Use ActionCadenceStepVariant to retrieve the call scripts from all call steps:

```
   SELECT SplitPercentage, TemplateId, ActionCadenceStepId FROM ActionCadenceStepVariant WHERE

    Type='MakeACall'

### ActionCadenceTracker

```

Represents an active cadence target. This object is available in API version 45.0 and later.

An ActionCadenceTracker record is created when you add a target to a cadence. Use ActionCadenceTracker to learn about a running
cadence target, including its state, current step, assigned prospect, and reason for completion.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionCadenceId

```

**Type**
reference


Standard Objects ActionCadenceTracker

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related ActionCadence.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

```
CompletionDisposition

CompletionReason

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The target’s disposition when it exited the action cadence. This field contains a value if the
target’s `State` is `Complete` . Sales reps can set this value when removing a target from
a cadence. This field is available in API version 51.0 and later. Possible values are:

**•** `Bad Data`  - Some of the target’s data is incorrect or invalid.

**•** `Contact Later`  - The target asked to be contacted at a later date.

**•** `Customer Connected` —The sales rep contacted the target.

**•** `Customer Engaged` —The target engaged with an email.

**•** `Disqualified`  - A sales rep determined that the target isn’t qualified.

**•** `Duplicate`  - The target has a duplicate lead, contact, or person account record.

**•** `Meeting Booked`  - The target has booked the meeting.

**•** `Meeting Requested`  - The target has requested for a meeting.

**•** `No Response`  - The target didn’t reply to any outreach.

**•** `Not Interested`  - The target stated a lack of interest.

**•** `Opt Out`  - The target has opted out.

**•** `Success`  - the cadence outreach was successful.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that the target completed the cadence. This field contains a value if the target’s
`State` is `Complete` . Possible values are:


Standard Objects ActionCadenceTracker

**Field** **Details**

**•** `AutomaticallyExited`                   - the target completed because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `AutomaticallyExitedDeletedStep`

**•** `AutomaticallyExitedInvalidParentStep`

**•** `DaisyChained`                   - the target completed because it’s connected to another action
cadence.

**•** `LeadConverted`                   - the target completed because the lead converted.

**•** `ManuallyRemoved`                   - the target completed because the sales rep removed it from
the cadence.

**•** `ManuallyRemovedNoAccess`                   - reserved for future use.

**•** `NoMoreSteps`                   - the target completed the action cadence because all the action
cadence steps were completed.

```
CurrentStepId

DaisyChainIteration

ErrorMessage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the current ActionCadenceStepTracker.

**Relationship Name**
CurrentStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of this action cadence in a sequence of linked action cadences followed by this
target. This value starts at 1 with the initial action cadence. A target can follow a sequence
of up to 10 linked action cadences. Available in API version 53.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If an error occurs while this target is being completed, this field contains the error message.


Standard Objects ActionCadenceTracker

**Field** **Details**

```
ExitGlobalRuleId

IsTrackerActive

LastCompletedStepId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If a global exit condition occurs, a target completes. One example of a global exit condition
is an email returned because of an invalid address. If the target completed because a global
exit condition occurred, this field contains the ID of the ActionCadenceRule record that
evaluated as `true` .

This field is available in API version 49.0 and later.

**Relationship Name**
ExitGlobalRule

**Relationship Type**
Lookup

**Refers To**
ActionCadenceRule

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action cadence target is active `(true)` or not `(false)` . The
default value is `false` . An action cadence target is active if the state is `Running`, `Paused`,
`Processing`, or `Initializing` . Only active targets count against the org limit of
150,000 trackers.

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the last completed ActionCadenceStepTracker.

**Relationship Name**
LastCompletedStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker


Standard Objects ActionCadenceTracker

**Field** **Details**

```
OwnerId

RelatedToAttributionType

RelatedToId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who is assigned to complete the cadence steps for the target.

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
Defines when the cadence is related to an opportunity or invoice. Available in API version
51.0 and later.

Possible values are:

**•** `Activation` —Attribute the opportunity to the cadence when the opportunity is
created.

**•** `Collected` —Attribute the value to the cadence after payment for the invoice is
collected.

**•** `Collection Advancement` —Attribute the value to the cadence when the invoice
is out for collection.

**•** `Maturation` —Attribute the opportunity to the cadence only when the opportunity
stage advances.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related opportunity if there’s one. Available in API version 51.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
RelatedTo

**Relationship Type**
Lookup


Standard Objects ActionCadenceTracker

**Field** **Details**

**Refers To**
Opportunity, Invoice

```
ScheduledResumeDateTime

State

TargetId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. Available in API version 53.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing` —Salesforce is working on changing the state of this action cadence
tracker. We recommend that you filter out steps that have this state from your dashboards.

**•** `Running`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the target that is assigned to this action cadence.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


### Standard Objects ActionCdncStpMonthlyMetric

Usage

Use ActionCadenceTracker to see what targets are currently assigned to an active action cadence.

```
   select TargetId from ActionCadenceTracker where ActionCadenceId=<Id of the action cadence>

    and State= "Running"

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

**ActionCadenceTrackerOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ActionCadenceTrackerShare on page 67**
Sharing is available for the object.

### ActionCdncStpMonthlyMetric

Represents the monthly engagement metrics for an action cadence step. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related action cadence step.

This is a relationship field.

**Relationship Name**
ActionCadenceStep


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Relationship Type**
This is an overview-detail relationship field, where ActionCadenceStep is the master object.

**Refers To**
ActionCadenceStep

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
The number of calls in the month for this step with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with no call result specified.

**Type**
int


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Unqualified.

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of sent emails that were bounced for all recipients on the email. Bounced emails
aren’t marked as delivered. Available in API version 54.0 and later.

```
AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this step in the month.

**Type**
int


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this step in the month.
Available in API version 51.0 and later.

```
AllEmailsUntrackedSentCount

AllTotalCallsCount

DeliveredRecipientCount

DeliveredRecipientRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this step in the month. Available
in API version 51.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls with all call results for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that were successfully delivered an email. Available in API version
54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. Available in API version
54.0 and later.

This field is a calculated field.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
HardBounceTrackableSends

HasTemplateAssigned

HrdBncTrackableRecipientSends

IsCompoundMetric

LinkClickTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this step has an associated email template or call script. Available in API
version 52.0 and later.

The default value is 'false'.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. Available in API
version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When true, indicates that this metric represents engagement for a combination of the action
cadence step and a single email template. The value is true for all action cadence steps
created in Summer ’21 and later.

When false, indicates that the metric represents engagement for the action cadence step
and all email templates used on the step. The value is false for all action cadence steps created
in Spring ’21 and earlier. The default value is 'false'.

Available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent with link click tracking. Available in API version 54.0 and later.

```
LinkClkTrackableRecipientSends

Month

MonthInt

OooTrackableRecipientSends

OpenTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking. Available in API version
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
The month in which the engagement occurred, in `yyyymm` format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with out-of-office tracking. Out-of-office
tracking requires Inbox. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking. Available in API version
54.0 and later.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
OpenTrackableSends

OutOfOfficeTrackableSends

RecipientReplies

RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email. Available in API version 54.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique email recipients. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email. Hard bounces can mean that the
recipient's email address doesn't exist or is misspelled. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of recipients that responded with an out-of-office reply. Available in API version
54.0 and later.

```
RecipientsSoftBounced

ReplyTrackableRecipientSends

ReplyTrackableSends

SftBncTrackableRecipientSends

SoftBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email. A soft bounce often indicates a
temporary issue with the recipient's email server, such as a full inbox. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with reply tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking. Available in API
version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 54.0 and later.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
SomeEmailsDeliveredCount

SomeEmailsDeliveredRate

TemplateId

TrackableRecipientSendHrdBncRt

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the email template or call script associated with this step. Available in API version
52.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced. Available in API version 54.0 and later.

This field is a calculated field.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
TrackableRecipientSendOooRate

TrackableRecipientSendReplyRt

TrackableRecipientSendSftBncRt

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients. Available in API version 54.0 and later.

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
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced. Available in API version 54.0 and later.

This field is a calculated field.

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


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
54.0 and later.

This field is a calculated field.

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by the recipient. Available
in API version 54.0 and later.

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

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This field is a calculated field.


### Standard Objects ActionLinkGroupTemplate

**Field** **Details**

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
The number of unique recipients who clicked a link in an email for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email for this step in the month.

### ActionLinkGroupTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking on an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external
server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. Every action link belongs to an action
link group and action links within the group are mutually exclusive. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with the “Customize Application” permission can modify or delete this object.


Standard Objects ActionLinkGroupTemplate

Fields

**Field Name** **Details**

```
Category

DeveloperName

ExecutionsAllowed

HoursUntilExpiration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The location of the action link group within the feed element. Values are:

**•** `Primary` —The action link group is displayed in the body of the feed
element.

**•** `Overflow` —The action link group is displayed in the overflow menu of
the feed element.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template to use in code.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The number of times an action link can be executed. Values are:

**•** `Once` —An action link can be executed only once across all users.

**•** `OncePerUser` —An action link can be executed only once for each user.

**•** `Unlimited` —An action link can be executed an unlimited number of
times by each user. If the action link’s `actionType` is `Api` or `ApiAsync`,
you can’t use this value.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionLinkGroupTemplate

**Field Name** **Details**

**Description**
The number of hours from when the action link group is created until it's removed
from associated feed elements and can no longer be executed. The maximum
value is 8,760.

```
IsPublished

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the action link group template is published. Action link group templates
shouldn’t be published until at least one ActionLinkTemplate is associated with
it. Once set to `true`, this can’t be set back to `false` .

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
The name of the action link group template.

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


### Standard Objects ActionLinkTemplate

**Field Name** **Details**

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

Usage

Define action link templates in Setup and use `ConnectApi` in Apex or Connect REST API to instantiate action links from the templates
and to post feed elements with the action links.

If you delete a published action link group template, you delete all related action link information which includes deleting all action links
that were instantiated using the template from feed items.

### ActionLinkTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external server
or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. This object is available in API version 33.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with the “Customize Application” permission can modify or delete this object.

Fields

**Field Name** **Details**

```
ActionLinkGroupTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ActionLinkGroupTemplate with which this action link template is
associated.

This is a relationship field.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

**Relationship Name**
ActionLinkGroupTemplate

**Relationship Type**
Lookup

**Refers To**
ActionLinkGroupTemplate

```
ActionUrl

Headers

IsConfirmationRequired

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The action link URL. For example, a `Ui` action link URL is a Web page. A
`Download` action link URL is a link to the file to download. `Ui` and `Download`
action link URLs are provided to clients. An `Api` or `ApiAsync` action link URL
is a REST resource. `Api` and `ApiAsync` action link URLs aren’t provided to
clients. Links to Salesforce can be relative. All other links must be absolute and
start with `https://` .

Links to resources hosted on Salesforce servers can be relative, starting with a
`/` . All other links must be absolute and start with `https://` . This field can
contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}`, for example,
`https://www.example.com/{!Bindings.itemId}` . Set the binding
variable’s value when you instantiate the action link group from the template.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP headers sent when corresponding action links are invoked.
This field can be used only for `Api` and `ApiAsync` action links. This field can
contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, a confirmation dialog appears before the action is executed.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

```
IsGroupDefault

Label

LabelKey

LinkType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, action links derived from this template are the default or primary action
in their action groups. There can be only one default action per action group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A custom label to display on the action link button. If none of the `LabelKey`
values make sense for an action link, use a custom label. Set the `LabelKey`
field to `None` and enter a label name in the `Label` field.

Action links have four states: new, pending, success, and failed. These strings are
appended to the label for each state:

**•** _Label_

**•** _Label_ Pending

**•** _Label_ Success

**•** _Label_ Failed

For example, if the value of `Label` is “Call Home,” the values of the four action
link states are: Call Home, Call Home Pending, Call Home Success, and Call Home
Failed.

If `LabelKey` has any value other than `None`, the `Label` field is empty.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Key for the set of labels to display for these action link states: new, pending,
success, failed. For example, the Approve set contains these labels: Approve,
[Pending, Approved, Failed. For a complete list of keys and labels, see Action Link](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)
[Labels in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm) _Connect REST API Developer Guide_ .

If none of the label key values make sense for an action link, set this field to `None`
and enter a custom label name in the `Label` field.

**Type**
picklist


Standard Objects ActionLinkTemplate

**Field Name** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action link. One of these values:

**•** `Api` —The action link calls a synchronous API at the action URL. Salesforce
sets the status to `SuccessfulStatus` or `FailedStatus` based on
the HTTP status code returned by your server.

**•** `ApiAsync` —The action link calls an asynchronous API at the action URL.
The action remains in a `PendingStatus` state until a third party makes
a request to `/connect/action-links/` _**`actionLinkId`**_ to set the
status to `SuccessfulStatus` or `FailedStatus` when the
asynchronous operation is complete.

**•** `Download` —The action link downloads a file from the action URL.

**•** `Ui` —The action link takes the user to a web page at the action URL.

```
Method

Position

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
HTTP method for the action URL. One of these values:

**•** `HttpDelete` —Returns HTTP 204 on success. Response body or output
class is empty.

**•** `HttpGet` —Returns HTTP 200 on success.

**•** `HttpHead` —Returns HTTP 200 on success. Response body or output class
is empty.

**•** `HttpPatch` —Returns HTTP 200 on success or HTTP 204 if the response
body or output class is empty.

**•** `HttpPost` —Returns HTTP 201 on success or HTTP 204 if the response
body or output class is empty. Exceptions are the batch posting resources
and methods, which return HTTP 200 on success.

**•** `HttpPut` —Return HTTP 200 on success or HTTP 204 if the response body
or output class is empty.

`Ui` and `Download` action links must use `HttpGet` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
An integer specifying the position of the action link template relative to other
action links in the group. 0 is the first position.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

```
RequestBody

UserAlias

UserVisibility

```

Usage

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP request body sent when corresponding action links are
invoked. This field can be used only for `Api` and `ApiAsync` action links. This
field can contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If you selected `CustomUser` or `CustomExcludedUser` for
`UserVisibility`, this field is the alias for the custom user. Use the alias in
a template binding to specify the custom user when an action link group is
created using the template.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Who can see the action link. This value is set per action link, not per action link
group. One of these values:

**•** `Creator` —Only the creator of the action link can see the action link.

**•** `Everyone` —Everyone can see the action link.

**•** `EveryoneButCreator` —Everyone but the creator of the action link
can see the action link.

**•** `Manager` —Only the manager of the creator of the action link can see the
action link.

**•** `CustomUser` —Only the custom user can see the action link.

**•** `CustomExcludedUser` —Everyone but the custom user can see the
action link.

Create action link templates in Setup. Use Apex classes in the `ConnectApi` namespace or Connect REST API to instantiate action
links from templates and to post feed elements with the action links.


### Standard Objects ActionPlan

[For information about action links, see Working with Action Links in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/pages/connectapi_features_action_links.htm?search_text=working%20with%20action%20links) _Apex Developer Guide_ or the _Connect REST API Developer Guide_ .

### ActionPlan

Represents the instance of an action plan, a set of tasks created from an action plan template. This object is available in API version 44.0
and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

```

Fields

**Field Name** **Details**

### `ActionPlanState` `ActionPlanTemplateVersionId` `ActionPlanType`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The status of work being done for the action plan.

Possible values are:

**•** `Canceled`

**•** `Complete`

**•** `In Progress`

**•** `Not Started`

The default value is `Not Started` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the version of the action plan template used to create this action plan.
At creation, the referenced action plan template must be in the published state.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The action plan’s type.


Standard Objects ActionPlan

**Field Name** **Details**

Possible values are:

**•** `Industries`

**•** `Sales` —This value is available in API version 63.0 and later with the Sales
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** `Service`

```
IsLocked

IsUsingHolidayHours

LastReferencedDate

LastViewedDate

MayEdit

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the action plan is locked or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether task completion dates have been calculated by incrementing
the task offset for each non-work day, excluding recurring holidays.

**Type**
dateTime

**Properties**
Filter, Nllable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionPlan

**Field Name** **Details**

**Description**

Indicates whether the action plan can be edited or not.

```
Name

OwnerId

StartDate

TargetId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the action plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this record.

**Type**
date

**Properties**
Create, Default on create, Filter, Group, Sort

**Description**

The start date of the action plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the parent object record that relates to this action plan.

For API version 63.0 and later, supported parent objects are Account,
AccountPlanObjective, Applicant, ApplicationForm, ApplicationFormProduct,
Asset, BusinessLicense, BusinessMilestone, Campaign, Case, ChangeRequest,
Claim, Contact, Contract, FinancialGoal, Incident, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, Problem,
ResidentialLoanApplication, WorkOrder, and WorkOrderLineItem.

For API version 62.0 and later, supported parent objects are
ApplicationFormEvaluation and VettingEvaluation.

For API version 48.0 and later, supported parent objects are Account,
AssetsAndLiabilities, BusinessMilestone, Campaign, Card, Case, Claim, Contact,


### Standard Objects ActionPlanItem

**Field Name** **Details**

Contract, Financial Account, Financial Goal, Financial Holding, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent,
ResidentialLoanApplication, and Visit as well as custom objects with activities
enabled.

For API version 47.0 and later, supported parent objects are Account,
BusinessMilestone, Campaign, Case, Claim, Contact, Contract, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, and Visit as well
as custom objects with activities enabled.

For API version 46.0 and later, supported parent objects are Account, Campaign,
Case, Contact, Contract, Lead, and Opportunity as well as custom objects with
activities enabled.

For API version 45.0 and earlier, the only supported parent object is Account.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanItem

Represents the instance of an action plan item.This object is available in API version 44.0 and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanId

```

**Type**
reference


Standard Objects ActionPlanItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan that this item belongs to.

```
ActionPlanTemplateItemId

IsLocked

IsRequired

ItemEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the action plan template item this item was created from.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is locked or not. The default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is required or not.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of object used with the item. This field is available in API version 61.0
and later.

Possible values are:

**•** `AssessmentTask` —Assessment Task

**•** `DocumentChecklistItem` —Document Checklist Item

**•** `Event` -Available only with sales action plans in API version 63.0 and later
with the Sales Action Plans add-on license and the Sales Action Plans default
permission set.


Standard Objects ActionPlanItem

**Field Name** **Details**

**•** `GenericVisitTask` —Generic Visit Task

**•** `OtherComponentTask` —Other Component Task

**•** `RecordAction`

**•** `SignatureTask` —Signature Task

**•** `Task`

```
ItemId

ItemState

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the record created by this action plan item. This field is a polymorphic
relationship field.

**Relationship Name**
Item

**Refers To**
DocumentChecklistItem, Event, RecordAction, Task

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan item’s work state.

Possible values are:

**•** `Canceled`

**•** `Completed`

**•** `Deleted`

**•** `In Progress`

**•** `Pending`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan item.


### Standard Objects ActionPlanTemplate

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanItemFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanItemHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanItemShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplate

Represents the instance of an action plan template. This object is available in API version 44.0 and later.

Supported Calls

`create()delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`,

Fields

**Field Name** **Details**

```
ActionPlanType

Category

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

This action plan template’s type. Possible values are:

**•** `Industries`

**•** `Sales` —This value is available in API version 63.0 and later with the Sales
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** Service

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Description**
Specifies the category that the action plan template belongs to.

Available in API version 64.0 and later.

Possible values are:

**•** `Onboarding`

**•** `Application`

```
Description

EstimatedCompletionDays

FileBasedTemplatePath

IsAdHocItemCreationEnabled

IsLocked

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The description of this action plan template.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated number of days to complete the action plan.

Available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The path of the file based template using which the action plan template is
created.

Available in API version 64.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can add tasks or other items to generated action plans
( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template is locked or not. The default value is
`false` .

```
LastReferencedDate

LastViewedDate

MayEdit

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template can be edited or not. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Description**

The ID of the user who owns this action plan template. This field is a polymorphic
relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
SourceType

Status

Subcategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the source type to which the action plan template belongs to.

Available in API version 64.0 and later.

Possible values are:

**•** `CRM`

**•** `MigratedFromSandbox`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The status of this action plan template.

Possible values are:

**•** `Draft`

**•** `Final—Published`

**•** `Obsolete`

**•** `ReadOnly`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The subcategory to which the action plan template belongs.

Available in API version 64.0 and later.

Possible values are:


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**•** `Product Onboarding`

**•** `Customer Onboarding`

```
TargetEntityType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Restricted picklist, Sort

**Description**

The parent object this action plan template relates to.

Possible values are organized by the API version in which they were introduced.
Values are available in all versions after introduction unless noted otherwise.

API Version 62.0 and later with Financial Services:

**•** `AccountPlanObjective`

**•** `FinancialDeal`

**•** `PartyProfile`

API Version 62.0 and later with Public Sector Solutions:

**•** `ApplicationFormEvaluation`

**•** `VettingEvaluation`

API version 60.0 and later with Education Cloud

**•** `ProgramEnrollment`

API version 58.0 and later with Health Cloud

**•** `CareBarrier`

API version 58.0 and later with Nonprofit Cloud:

**•** `Benefit`

**•** `Program`

API Version 58.0 and later with Public Sector Solution and Education Cloud:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Program`

API Version 56.0 and later with Automotive Cloud:

**•** `Account`

**•** `Asset`

**•** `Asset Account Participant`

**•** `Asset Contact Participant`

**•** `Asset Milestone`

**•** `Fleet`


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**•** `Lead`

**•** `Opportunity`

**•** `Record Alert`

**•** `Vehicle`

**•** `Case`

**•** `Claim`

**•** `Contact`

API Version 58.0 and later with Grantmaking:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Budget`

**•** `BudgetAllocation`

**•** `CareBarrier`

**•** `FundingAward`

**•** `FundingAwardAmendment`

**•** `FundingAwardRequirement`

**•** `FundingDisbursement`

**•** `FundingOpportunity`

**•** `Program`

API Version 52.0 and later:

**•** `BusinessLicenseApplication`

**•** `IndividualApplication`

**•** `PublicComplaint`

**•** `RegulatoryCodeViolation`

**•** `ViolationEnforcementAction`

API Version 47.0 and later:

**•** `BusinessMilestone`

**•** `Claim`

**•** `InsurancePolicy`

**•** `InsurancePolicyCoverage`

**•** `PersonLifeEvent`

**•** `Visit`

API Version 46.0 and later:

**•** `Campaign` —Unsupported for Grantmaking.

**•** `Case`

**•** `Contact`


### Standard Objects ActionPlanTemplateItem

**Field Name** **Details**

**•** `Contract`

**•** `Lead`

**•** `Opportunity`

**•** `Custom objects with activities enabled`

API Version 44.0 and later:

Account

```
UniqueName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template. This field is unique within your
organization.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplateItem

Represents the instance of an item on an action plan template version. This object is available in API version 44.0 and later.

Supported Calls

```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

```


Standard Objects ActionPlanTemplateItem

Fields

**Field Name** **Details**

```
ActionPlanTemplateVersionId

DisplayOrder

IsActive

IsLocked

IsRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**

The version of the action plan template this item is for.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The order in which this item is displayed within the action plan template version.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item is locked or not. The default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is required. The default
value is `false` .


Standard Objects ActionPlanTemplateItem

**Field Name** **Details**

```
ItemEntityType

LastReferencedDate

LastViewedDate

MayEdit

Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of action plan template item entity..

Possible values are:

**•** `Document Checklist Item`

**•** `Event` —This value is available in API version 63.0.

**•** `RecordAction`

**•** `Task`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item can be edited or not. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, idLookup, Update


### Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Description**

The unique identifier for this action plan template item record.

```
UniqueName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template item. This field is unique within
your organization.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateItemFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateItemHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateItemShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplateItemValue

Represents the value associated with an action plan template item. This object is available in API version 44.0 and later.

Supported Calls

```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanTemplateItemId

```

**Type**
reference


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan template item that this value relates to.

**Relationship Name**
ActionPlanTemplateItem

**Relationship Type**
Master-detail

**Refers To**
ActionPlanTemplateItem (the master object)

```
IsActive

IsLocked

ItemEntityFieldName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item value is locked or not. The
default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The name of the field on the action plan template item that this value is for.
Available fields include:

**•** `AssessmentTask.AssessmentTaskDefinitionId` —Assessment
Task Definition ID

**•** `AssessmentTask.AssignedToId` —AssignedTo ID

**•** `AssessmentTask.Description` —Description

**•** `AssessmentTask.EndTime` —End Time

**•** `AssessmentTask.IsRequired` —Required


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `AssessmentTask.Name` —Name

**•** `AssessmentTask.OwnerId` —Owner ID

**•** `AssessmentTask.ParentId` —Visit ID

**•** `AssessmentTask.ReferenceRecordId` —ReferenceRecord ID

**•** `AssessmentTask.SequenceNumber` —Sequence

**•** `AssessmentTask.StartTime` —Start Time

**•** `AssessmentTask.Status` —Status

**•** `AssessmentTask.TaskDefinitionId` —TaskDefinition ID

**•** `AssessmentTask.TaskType` —Task Type

**•** `DocumentChecklistItem.Comments` —Comments

**•** `DocumentChecklistItem.DocumentCategoryId` —Document
Category ID

**•** `DocumentChecklistItem.DocumentTypeId` —Document Type
ID

**•** `DocumentChecklistItem.Instruction` —Instructions

**•** `DocumentChecklistItem.IsAccepted` —Accepted

**•** `DocumentChecklistItem.IsFrozen` —Frozen

**•** `DocumentChecklistItem.IsRequired` —Required

**•** `DocumentChecklistItem.Name` —Name

**•** `DocumentChecklistItem.OwnerId` —Owner ID

**•** `DocumentChecklistItem.ParentRecordId` —Parent Record ID

**•** `DocumentChecklistItem.ReceivedDocumentId` —Received
Document ID

**•** `DocumentChecklistItem.Status` —Status

**•** `DocumentChecklistItem.ValidatedById` —User ID

**•** `DocumentChecklistItem.ValidationDateTime` —Validation
Date Time

**•** `DocumentChecklistItem.WhoId` —Who ID

**•** `Event.ActivityDate` —Due Date Only

**•** `Event.ActivityDateTime` —Due Date Time

**•** `Event.Description` —Description

**•** `Event.DurationInMinutes` —Duration

**•** `Event.EndDateTime` —End Date Time

**•** `Event.EventSubtype` —Event Subtype

**•** `Event.IsAllDayEvent` —All-Day Event

**•** `Event.IsPrivate` —Private

**•** `Event.IsRecurrence` —Create Recurring Series of Events

**•** `Event.IsReminderSet` —Reminder Set

**•** `Event.Location` —Location


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `Event.OwnerId` —Assigned To ID

**•** `Event.Recurrence2PatternText` —Recurrence Pattern

**•** `Event.RecurrenceDayOfMonth` —Recurrence Day of Month

**•** `Event.RecurrenceDayOfWeekMask` —Recurrence Day of Week
Mask

**•** `Event.RecurrenceEndDateOnly` —Recurrence End

**•** `Event.RecurrenceInstance` —Recurrence Instance

**•** `Event.RecurrenceInterval` —Recurrence Interval

**•** `Event.RecurrenceMonthOfYear` —Recurrence Month of Year

**•** `Event.RecurrenceStartDateTime` —Recurrence Start

**•** `Event.RecurrenceTimeZoneSidKey` —Recurrence Time Zone

**•** `Event.RecurrenceType` —Recurrence Type

**•** `Event.ReminderDateTime` —Reminder Date/Time

**•** `Event.ShowAs` —Show Time As

**•** `Event.StartDateTime` —Start Date Time

**•** `Event.Subject` —Subject

**•** `Event.Type` —Type

**•** `Event.WhatId` —Related To ID

**•** `Event.WhoId` —Name ID

**•** `GenericVisitTask.DefinitionReferenceId` —Generic Visit
Task ID

**•** `GenericVisitTask.Description` —Description

**•** `GenericVisitTask.EndDateTime` —End Date Time

**•** `GenericVisitTask.IsRequired` —Required

**•** `GenericVisitTask.Name` —Name

**•** `GenericVisitTask.OwnerId` —Owner ID

**•** `GenericVisitTask.Sequence` —Sequence

**•** `GenericVisitTask.StartDateTime` —Start Date Time

**•** `GenericVisitTask.Status` —Status

**•** `GenericVisitTask.VisitId` —Visit ID

**•** `OtherComponentTask.Description` —Description

**•** `OtherComponentTask.FullyQualifiedName` —Fully Qualified
Name

**•** `OtherComponentTask.Name` —Name

**•** `OtherComponentTask.OwnerId` —Owner ID

**•** `OtherComponentTask.ParentTaskId` —Assessment Task ID

**•** `OtherComponentTask.ParticipantRoleId` —ParticipantRole
ID

**•** `RecordAction.ActionDefinition` —Action Definition


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `RecordAction.ActionType` —Action Type

**•** `RecordAction.FlowDefinition` —Interaction Definition ID

**•** `RecordAction.FlowInterviewId` —FlowInterview ID

**•** `RecordAction.IsMandatory` —Is Mandatory

**•** `RecordAction.IsUiRemoveHidden` —Hide Remove Action in UI

**•** `RecordAction.Order` —Order

**•** `RecordAction.ParticipantRoleId` —ParticipantRole ID

**•** `RecordAction.Pinned` —Pinned

**•** `RecordAction.RecordId` —Parent Record ID

**•** `RecordAction.Status` —Status

**•** `SignatureTask.Description` —Description

**•** `SignatureTask.Name` —Name

**•** `SignatureTask.ParentTaskId` —Assessment Task ID

**•** `Task.APT_Custom_Text_1_c__c` —APT Custom Text - 1

**•** `Task.ActivityDate` —Due Date Only

**•** `Task.Boolean_Test__c` —Boolean Test

**•** `Task.CallDisposition` —Call Result

**•** `Task.CallDurationInSeconds` —Call Duration

**•** `Task.CallObject` —Call Object Identifier

**•** `Task.CallType` —Call Type

**•** `Task.Custom_Picklist__c` —Custom Picklist

**•** `Task.Description` —TEstActivityDEs

**•** `Task.IsRecurrence` —Create Recurring Series of Tasks

**•** `Task.IsReminderSet` —Reminder Set

**•** `Task.OwnerId` —Assigned To ID

**•** `Task.Priority` —Priority

**•** `Task.RecurrenceDayOfMonth` —Recurrence Day of Month

**•** `Task.RecurrenceDayOfWeekMask` —Recurrence Day of Week Mask

**•** `Task.RecurrenceEndDateOnly` —Recurrence End

**•** `Task.RecurrenceInstance` —Recurrence Instance

**•** `Task.RecurrenceInterval` —Recurrence Interval

**•** `Task.RecurrenceMonthOfYear` —Recurrence Month of Year

**•** `Task.RecurrenceRegeneratedType` —Repeat This Task

**•** `Task.RecurrenceStartDateOnly` —Recurrence Start

**•** `Task.RecurrenceTimeZoneSidKey` —Recurrence Time Zone

**•** `Task.RecurrenceType` —Recurrence Type

**•** `Task.ReminderDateTime` —Reminder Date/Time

**•** `Task.Status` —Status


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `Task.Subject` —Subject

**•** `Task.TaskSubtype` —Task Subtype

**•** `Task.Type` —Type

**•** `Task.WhatId` —Related To ID

**•** `Task.WhoId` —Name ID

**•** `Task.test__c` —test

**•** `Task.text_3__c` —text 3

```
ItemEntityType

LastReferencedDate

LastViewedDate

MayEdit

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of action plan template item.

Possible values are:

**•** `Document Checklist Item`

**•** `Event` —Available in API version 63.0 and later with the Sales Action Plans
add-on license and the Sales Action Plans default permission set.

**•** `RecordAction`

**•** `Task`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Description**

Indicates whether this action plan template item value can be edited or not. The
default value is `false` .

```
Name

ValueFormula

ValueLiteral

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique identifier for this record.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A formula used to calculate the value for this action plan template item.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**

The value for this action plan template item.

This object has the following associated objects. If the API version isn't specified, they're available in the same API versions as this object.
Otherwise, they're available in the specified API version and later.

**[ActionPlanTemplateItemValueChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateItemValueFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateItemValueHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateItemValueOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateItemValueShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects ActionPlanTemplateVersion ActionPlanTemplateVersion

Represents the version of an action plan template. This object is available in API version 44.0 and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search

   ( )undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanTemplateId

ActivationDateTime

InactivationDateTime

IsLocked

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Group

**Description**

The ID of the action plan template this version represents.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort,

**Description**

The date and time at which this version became active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

The date and time at which this version became inactive.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version is locked or not. The default
value is `false` .


Standard Objects ActionPlanTemplateVersion

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

MayEdit

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort,, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version can be edited. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update,

**Description**

The name of this version item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan template version’s state. Possible values are:

**•** `Draft`

**•** `Final – Published`

**•** `Obsolete`

**•** `ReadOnly`


### Standard Objects ActiveFeatureLicenseMetric

**Field Name** **Details**

```
Version

```

Associated Objects

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

The index number of this action plan template version.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateVersionShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActiveFeatureLicenseMetric

Represents the number of active, assigned, and purchased feature licenses in the org. This object is available in API version 52.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license who have logged in within the last 30 days.


Standard Objects ActiveFeatureLicenseMetric

**Field** **Details**

```
AssignedUserCount

FeatureType

MetricsDate

TotalLicenseCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of feature license.

Possible values are:

**•** `AvantgoUser` —AvantGo User

**•** `ChatterAnswersUser` —Chatter Answers User

**•** `InteractionUser` —Flow User

**•** `JigsawProspectingUser` —Data.com User

**•** `KnowledgeUser` —Knowledge User

**•** `LiveAgentUser` —Chat User

**•** `MarketingUser` —Marketing User

**•** `MobileUser` —Apex Mobile User

**•** `OfflineUser` —Offline User

**•** `SFContentUser` —Salesforce CRM Content User

**•** `SiteforceContributorUser` —Site.com Contributor User

**•** `SiteforcePublisherUser` —Site.com Publisher User

**•** `SupportUser` —Service Cloud User

**•** `WirelessUser` —Wireless User

**•** `WorkDotComUserFeature` —WDC User

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that feature license metrics were collected.

**Type**
int


### Standard Objects ActivePermSetLicenseMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of feature licenses in the organization.

### ActivePermSetLicenseMetric

Represents the number of active, assigned, and purchased permission set licenses in the org. This object is available in API version 52.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

AssignedUserCount

DeveloperName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license who have logged in within the last 30
days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of this permission set license object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must begin


Standard Objects ActivePermSetLicenseMetric

**Field** **Details**

with a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

```
MasterLabel

MetricsDate

PermissionSetLicenseId

TotalLicenses

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the permission set license.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that permission set license metrics were collected.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the permission set license.

This is a relationship field.

**Relationship Name**
PermissionSetLicense

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicense

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of this permission set licenses that are available to your org.


### Standard Objects ActiveProfileMetric ActiveProfileMetric

Represents the profile associated with the active, assigned, and purchased user licenses. This object is available in API version 52.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

AssignedUserCount

MetricsDate

ProfileId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile who have logged in within the last 30 days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that profile metrics were collected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the profile.

This is a relationship field.

**Relationship Name**
Profile


### Standard Objects ActiveScratchOrg

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Profile

```
UserLicenseId

### ActiveScratchOrg

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user license.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense

Represents an active scratch org. This object is available in API version 41.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
update()

```

Fields

**Field Name** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this scratch org.


Standard Objects ActiveScratchOrg

**Field Name** **Details**

```
Edition

ExpirationDate

Features

HasSampleData

LastLoginDate

LastReferencedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org edition of this scratch org. Possible values are `Group`, `Developer`,
`Enterprise`, and `Professional` . This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org expires. This field is read only.

**Type**
textarea

**Properties**
Nillable

**Description**
The features enabled in this scratch org, such as `MultiCurrency` . See the
_Salesforce DX Developer Guide_ for the full list of valid features. This field is read
only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the scratch org contains sample data. If set to `true`, the
sample data is similar to the data in a Salesforce free trial org.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date of the last user login to the scratch org. This field is read only.

**Type**
dateTime


Standard Objects ActiveScratchOrg

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record. This field is read only.

```
LastViewedDate

Name

Namespace

OrgName

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, and `LastReferenceDate` isn’t null, the user accessed this
record or list view indirectly. This field is read only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated ID of this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace associated with this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the scratch org. This field is read only.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this scratch org. This field is read only.


Standard Objects ActiveScratchOrg

**Field Name** **Details**

```
ScratchOrg

ScratchOrgInfoId

SignupEmail

SignupInstance

SignupTrialDays

SignupUsername

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The org ID of the scratch org. This field is read only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The id of the associated `ScratchOrgInfo` object. This field is read only.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the Administration user. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce instance on which this scratch org resides. This field is read only.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days between the scratch org's creation and expiration. This field
is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActiveScratchOrg

**Field Name** **Details**

**Description**
The username of the Administration user of the scratch org. This field is read only.

```
Snapshot

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this scratch org was created from a scratch org snapshot, then this field contains
either the name or ID of the snapshot. Specifically, the name corresponds to the
`Name` field of the snapshot’s record in the OrgSnapshot standard object; the ID
corresponds to the record ID.

If this scratch org wasn’t created from a snapshot, this field is empty. This field is
read only.

This field is available in API version 61.0 and later.

Salesforce automatically creates an instance of this object after a `ScratchOrgInfo` record moves to the Active state. The new
`ActiveScratchOrg` gets many of its field values from the `ScratchOrgInfo` object with which it’s associated.

When you delete an `ActiveScratchOrg` record, its associated scratch org is deleted and its associated `ScratchOrgInfo`
record is moved to the Deleted state.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ActiveScratchOrgFeed**

Feed tracking is available for the object.

**ActiveScratchOrgHistory**

History is available for tracked fields of the object.

**ActiveScratchOrgShare**

Sharing is available for the object.

SEE ALSO:

ScratchOrgInfo

NamespaceRegistry

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev)_


### Standard Objects ActivityFieldHistory ActivityFieldHistory

Represents a change in a field value for a tracked object or field. This object is a big object. This object is available in API version 55.0 and
later.

Supported Calls

`delete()describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, users must have ViewAllData permissions.

Fields

**Field** **Details**

```
ActivityId

ChangedById

ChangedDate

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the task or event that changed.

This field is a polymorphic relationship field.

**Relationship Name**
### Activity

**Refers To**
Event, Task

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the user who made the change.

This field is a relationship field.

**Relationship Name**
ChangedBy

**Refers To**
User

**Type**
dateTime


Standard Objects ActivityFieldHistory

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The date the field value changed.

```
DataType

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The type of the field with the changed value.

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


Standard Objects ActivityFieldHistory

**Field** **Details**

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
FieldName

IsDataAvailable

NewValueDateTime

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the field changed.

**Type**
boolean

**Properties**
Defaulted on create

**Description**
Indicates whether valid data is available in the old and new value fields. This field is `false`
if, for example, the fields are encrypted or the changed values are too large, such as for
Description field types.

The default value is `false` .

**Type**
dateTime

**Properties**
Nillable


Standard Objects ActivityFieldHistory

**Field** **Details**

**Description**
The new value for date type fields.

```
NewValueNumber

NewValueText

OldValueDateTime

OldValueNumber

OldValueText

Operation

```

**Type**
double

**Properties**
Nillable

**Description**
The new value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The new value for all other field types that are not a date or number type.

**Type**
dateTime

**Properties**
Nillable

**Description**
Old value for date type fields.

**Type**
double

**Properties**
Nillable

**Description**
Old value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The old value for all other field types that are not a date or number type.

**Type**
picklist

**Properties**
Restricted picklist


### Standard Objects ActivityHistory

**Field** **Details**

**Description**
The operation of the field value change.

Possible values are:

**•** `delete`

**•** `update`

Indexed Fields

When you're querying ActivityFieldHistory with SOQL, you must specify indexed fields in the `WHERE` clause filter starting from the first
field defined in the index. If you specify a partial list of indexed fields, don't leave any gaps between indexed fields after the first field.
Here are the indexed fields for ActivityFieldHistory, listed from first to last in the index order.

1. `ActivityId`

2. `ChangedDate`

3. `ChangedById`

4. `FieldName`

5. `ActivityFieldChange`

For example, this SOQL query succeeds because the first three indexed fields are in the `WHERE` clause.

```
   SELECT ActivityId, OldValueText, NewValueText, FieldName, ChangedDate

   FROM ActivityFieldHistory

   WHERE ActivityId = 'SomeId' AND ChangedDate >= :startDate AND ChangedDate <= :endDate

   ORDER BY ChangedDate

```

If you remove the `ActivityId` field from the `WHERE` clause, the query fails.

```
   SELECT ActivityId, OldValueText, NewValueText, FieldName, ChangedDate

   FROM ActivityFieldHistory

   WHERE ChangedDate >= :startDate AND ChangedDate <= :endDate

   ORDER BY ChangedDate

```

SEE ALSO:

[Big Objects Implementation Guide: SOQL with Big Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.bigobjects.meta/bigobjects/big_object_querying.htm)

[Big Objects Implementation Guide: Big Objects](https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object.htm)

### ActivityHistory

This read-only object is displayed in a related list of closed activities—past events and closed tasks—related to an object. It includes
activities for all contacts related to the object. ActivityHistory fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.


Standard Objects ActivityHistory

Supported Calls

```
   describeSObjects()

```

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
AccountId

ActivityDate

ActivityDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the related account, which is determined as follows:

**•** The account associated with the `WhatId`, if it exists; or

**•** The account associated with the `WhoId`, if it exists; otherwise

**•** `null`

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates one of the following:

**•** The due date of a task

**•** The due date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time Coordinated
(UTC) time zone. The time stamp doesn’t represent the time of the activity; don’t attempt
to alter it to accommodate time zone differences. Label is `Date` .

**Type**
dateTime


Standard Objects ActivityHistory

**Field** **Details**

**Properties**
Aggregate, Filter, Nillable, Sort

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` . The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is **Due Date Time** .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

```
ActivitySubtype

ActivityType

AlternateDetailId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.
This field isn’t updateable.

Possible values are:

**•** Task

**•** Email

**•** Call

**•** Event

**•** LinkedIn —Available in API version 56.0 and later.

**•** List Email

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents one of the following values: `Call`, `Email`, `Meeting`, or `Other` . Label is
`Type` . These are default values, and can be changed.

`ActivityType` is the union of `TaskType` and `EventType` . If the same activity appears
in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are distinct from
each other.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActivityHistory

**Field** **Details**

**Description**
The ID of a record the activity is related to which contains more details about the activity.
For example, an activity can be related to an EmailMessage record.

This is a relationship field.

**Relationship Name**
AlternateDetail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
CallDisposition

CallDurationInSeconds

CallObject

CallType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Duration of the call in seconds.

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


Standard Objects ActivityHistory

**Field** **Details**

```
CompletedDateTime

ConnectionReceivedId

ConnectionSentId

Description

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.

**•** For insert, if the task is saved with a Closed status the field is set. If the task is saved with
an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is no change
to the field.

Note: The status is a dynamic enum. If the Closed mapping is changed it won’t cause
an update of existing tasks. Only new insert/update operations are affected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that shared this record with your
organization. This field is available only if your organization has enabled Salesforce to
Salesforce and only in API versions 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that your organization shared this record
with. This field is available only if your organization has enabled Salesforce to Salesforce, and
only in API versions 28.0 and later. The value is always `null` . You can use the
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Nillable

**Description**

Contains a description of the event or task. Limit is 32 KB.


Standard Objects ActivityHistory

**Field** **Details**

```
Division

DurationInMinutes

EndDateTime

IsAllDayEvent

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Indicates the duration of the event or task.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0 and later. This
field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a full day, and
the `ActivityDate` defines the date of the event. If the value of this field is set to `false`,
then the activity may be an event spanning less than a full day, or it may be a task. The default
value of this field is `false` . Label is `All-Day Event` .


Standard Objects ActivityHistory

**Field** **Details**

```
IsClosed

IsDeleted

IsHighPriority

IsOnlineMeeting

IsReminderSet

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default value of this
field is `false` . This field is set indirectly by setting the `Status` field on the task—each
picklist value has a corresponding `IsClosed` value. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the activity has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

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
Defaulted on create, Filter

**Description**

Indicates whether the activity represents an online meeting ( `true` ) or not ( `false` ).

Note: This field is not available in API version 16.0 or later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ).The default value
of this field is `false` .


Standard Objects ActivityHistory

**Field** **Details**

```
IsTask

IsVisibleInSelfService

Location

OwnerId

PrimaryAccountId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If the value of this field is set to `true`, then the activity is a task. If the value is set to `false`,
then the activity is an event. The default value of this field is `false` . Label is `Task` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If the value of this field is set to `true`, then the activity can be viewed in the self-service
portal. The default value of this field is `false` . Label is `Visible in Self-Service` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

If the activity is an event, then this field contains the location of the event. If the activity is a
task, then the value is `null` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Indicates the ID of the user or group who owns the activity.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

**Type**
reference


Standard Objects ActivityHistory

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `AccountId` value from the activity record. Available in API versions 30.0 and
later to organizations that use Shared Activities.

```
PrimaryWhoId

Priority

ReminderDateTime

StartDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `WhoId` value from the activity record. Available in API versions 30.0 and later
to organizations that have enabled Shared Activities.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of this field is
`Normal` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time when the reminder is scheduled to fire, if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then the user may have deselected the
reminder checkbox in the Salesforce user interface, or the reminder has already fired at the
time indicated by the value.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Indicates the start date and time of the event.

Available in versions 29.0 and later.

If the event’s `IsAllDayEvent` flag is set to true (indicating an all-day event), then the
time stamp in `StartDateTime` is always set to midnight in the Coordinated Universal
Time (UTC) time zone.


Standard Objects ActivityHistory

**Field** **Details**

Note: Don’t attempt to alter the time stamp to account for any time zone differences.

If the event’s `IsAllDayEvent` flag is set to false, then you must translate the time portion
of the time stamp in `StartDateTime` to or from a local time zone for the user or the
application, as appropriate. The translation must be in the Coordinated Universal Time (UTC)
time zone.

If this field has a value, then `ActivityDate` and `ActivityDateTime` either must
be null or must match the value of this field.

If the activity is a task, `StartDateTime` is null

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

Indicates the current status of a task,. The default value of this field is `Not Started` . Each
predefined status field sets a value for `IsClosed` . To obtain picklist values, query TaskStatus.

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

The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatId` s are polymorphic. Polymorphic means a `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID` .

This is a polymorphic relationship field.


Standard Objects ActivityHistory

**Field** **Details**

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
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .


Standard Objects ActivityHistory

**Field** **Details**

If your organization uses Shared Activities, when you query activities in API version 30.0 or
later, the returned value of the `WhoId` field matches the value in the queried object, not
necessarily in the activity record itself.

If Shared Activities is enabled, the value of this field is not populated and the field
`PrimaryWhoId` should be queried instead.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

**Query activities that are related to an object**

**1.** Optionally, issue a describe call against the object whose activities you wish to query, to get a suggestion of the correct SOQL
to use.

**2.** Issue a SOQL relationship query with a main clause that references the object, and an inner clause that references the activity
history; for example:

```
       SELECT

        (SELECT ActivityDate, Description

         FROM ActivityHistories)

       FROM Account

       WHERE Name Like 'XYZ%'

```

The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following constraints on users who don’t have the “View All Data” permission help prevent performance issues.

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with “A.” Instead, you must reference a single account record.

```
       SELECT

        (SELECT ActivityDate, Description

         FROM ActivityHistories

         ORDER BY ActivityDate DESC NULLS LAST, LastModifiedDate DESC

         LIMIT 500)

       FROM Account

       WHERE Name = 'Acme'

       LIMIT 1

```

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.


### Standard Objects ActivityMetric

**•** In the inner clause of the query, you must sort on `ActivityDate` in descending order and `LastModifiedDate` in
descending order. You can optionally display nulls last. For example: `ORDER BY ActivityDate DESC NULLS LAST,`
`LastModifiedDate DESC` .

SEE ALSO:

Task

### ActivityMetric

Represents activities that were added to Salesforce automatically by Einstein Activity Capture and manually by users.

This object is available in API version 45.0.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Unless otherwise noted, Einstein Activity Capture and Activity Metrics must be enabled.

Fields

**Field** **Details**

```
BaseId

BaseType

FirstCallDateTime

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort

**Description**
The ID of the record that the activities apply to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entity that corresponds to the BaseId

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ActivityMetric

**Field** **Details**

**Description**
Indicates the date when the first call was made. This field is available only to Sales Engagement
users. Einstein Activity Capture and Activity Metrics aren’t required.

```
FirstEmailDateTime

InactiveDays

LastActivityDateLastModDate

LastActivityDateTime

LastCallDateLastModDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the first email was sent. This field is available only to Sales
Engagement users. Einstein Activity Capture and Activity Metrics aren’t required.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the number of days since the most recent activity was completed. This field is
derived from the Last Activity Date field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastActivityDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent activity was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastCallDateTime field was last modified.


Standard Objects ActivityMetric

**Field** **Details**

```
LastCallDateTime

LastEmailDateLastModDate

LastEmailDateTime

LastEmailReceivedDateTime

LastEmailSentDateTime

LastEventDateLastModDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent call was made through Sales Dialer or Inbox.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastEmailDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent or received.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was received.

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent.

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ActivityMetric

**Field** **Details**

**Description**
Indicates when the LastEventDateTime field was last modified.

```
LastEventDateTime

LastTaskDateLastModDate

LastTaskDateTime

NextActivityDateLastModDate

NextActivityDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent event was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastTaskDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the last task was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the NextActivityDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date of the next scheduled task or event. Only open tasks in the future are
included.


### Standard Objects ActivityUsrConnectionStatus

Usage

Use this object to see data about sales activities that were added to Salesforce manually and by Einstein Activity Capture. Activity Metric
fields are derived from your activity data. For example, the Inactive Days field indicates the number of days since the most recent activity
was completed. Create a trigger that notifies a user when there isn’t any activity on an account for a certain amount of time.

### ActivityUsrConnectionStatus

Represents the status of the email connections for Einstein Activity Capture users. You can also see whether users accepted the required
terms of service to capture emails. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, enable Einstein Activity Capture in your org.

Fields

**Field** **Details**

```
ConfigurationName

ConnectivityStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Einstein Activity Capture configuration that the user is assigned to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user’s email connection.

Possible values are:

**•** `ACTIVE`

**•** `DISABLED`

**•** `INITIALIZING`

**•** `NEEDSATTENTION`

**•** `NEEDSATTENTIONGLOBAL` (used when an org-level connection isn’t working)


Standard Objects ActivityUsrConnectionStatus

**Field** **Details**

**•** `NEEDSATTENTIONHYBRID` (used when both org-level and user-level connections
aren’t working)

**•** `PENDING`

**•** `PROCESSING`

```
ContactsSynced

EmailAddress

EventsSynced

ExternalId

GlobalOauthTermsState

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of contacts synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address that’s used to capture and sync data between Salesforce and the user’s
Microsoft or Google account.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of events synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ActivityUsrConnectionStatus

**Field** **Details**

**Description**
Indicates the user’s terms of service status. When emails are enabled for Einstein Activity
Capture, each user must accept the terms of service.

Possible values are:

**•** `ACCEPTED`

**•** `DECLINED`

**•** `PENDING`

This field is available only if you use an org-level OAuth 2.0 or a service account authentication
method. In connection report CSV files downloaded from Einstein Activity Capture Status &
Metrics, this field is labeled Global Auth User Email Consent Status.

```
IsTermsOfServiceAccepted

RecommendedActionDescription

RecommendedActionTitle

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has accepted the Einstein Activity Capture terms of service or
not. When emails are enabled for Einstein Activity Capture, each user must accept the terms
of service.

The default value is `false` .

This field is available only if you use a user-level authentication method. In connection report
CSV files downloaded from Einstein Activity Capture Status & Metrics, this field is labeled
User Auth Terms of Service Accepted.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Recommended action to take when the user’s `ConnectivityStatus` is
`NEEDSATTENTION` . Available in API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reason for the user's `ConnectivityStatus` when the status is `NEEDSATTENTION` .
Available in API version 58.0 and later.

**Type**
string


### Standard Objects AdditionalNumber

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user.

```
UserName

UserOnboardingStatus

### AdditionalNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the Einstein Activity Capture user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The initial sync status when the user connects Salesforce with their external email account
and syncs data for the first time. This field is available in API version 59.0 and later.

Possible values are:

**•** `NOT_STARTED`

**•** `IN_PROGRESS`

**•** `NOT_CONFIGURED`

**•** `COMPLETE`

**•** `FAILED`

Represents an optional additional number for a call center. This additional number is visible in the call center's phone directory.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can't access this object.


Standard Objects AdditionalNumber

Fields

**Field** **Details**

```
CallCenterId

Description

Name

Phone

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
System field that contains the ID of the user who created the call center associated with this
additional number. If value is null, this additional number is displayed in every call center's
phone directory.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the additional number, such as Conference Room B.

Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the additional number.

Limit: 80 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
The phone number that corresponds to this additional number.

Create an additional number for a call center directory. Use this object if the number is not easily categorized as a User, Contact, Lead,
Account, or the other object. Examples include phone queues or conference rooms.


### Standard Objects Address Address

Represents a mailing, billing, or home address.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The following access checks must be enabled:

**•** Industries Insurance

**•** Retail Execution

**•** Industries Visit

**•** Field Service

**•** Order Management

**–** Perms: FulfillmentOrder, OrderSummary,AdvancedOrderManagement, OrderCCS

**–** Prefs: OrdersEnabled, EnhancedCommerceOrders

**•** Public Sector

**•** Employee Experience

**•** Contact Tracing For Employees

You can create an address only when creating a location.

Fields

**Field Name** **Details**

### `Address` `AddressType`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The full address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Mailing


Standard Objects Address

**Field Name** **Details**

**•** Shipping

**•** Billing

**•** Home

```
City

Country

Description

DrivingDirections

GeocodeAccuracy

```

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
The address country.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the address.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.


Standard Objects Address

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Latitude

LocationType

Longitude

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user viewed this record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Filter, Group, Sort, Update

**Description**
Picklist of location types. The available values are:

**•** Warehouse (default)

**•** Site

**•** Van

**•** Plant

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Address

**Field Name** **Details**

**Description**
Used with `Latitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal
places.

```
Name

ParentId

PostalCode

State

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the address.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A lookup field to the parent location.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.


### Standard Objects AgentWork

**Field Name** **Details**

```
Street

TimeZone

```

Usage

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.

Important: “Address” in Salesforce can also refer to the Address compound field found on many standard objects. When referencing
the Address object in your Apex code, always use `Schema.Address` instead of `Address` to prevent confusion with the
standard Address compound field. If referencing both the address object and the Address field in the same snippet, you can
differentiate between the two by using `System.Address` for the field and `Schema.Address` for the object.

Associated Object

This object has the following associated object. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AddressHistory (API version 62.0)**
History is available for tracked fields of the object.

### AgentWork

Represents a work assignment that’s been routed to an agent. If the work is transferred to another agent, a new AgentWork record is
created. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


Standard Objects AgentWork

Fields

**Field** **Details**

```
AcceptDateTime

ActiveTime

AcwExtensionCount

AcwExtensionDuration

AfterConversationActualTime

```

**TypedateTime**

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was accepted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time an agent is actively working on a work item in their console. Active time
is tracked only for tasks routed using the tab-based capacity model. It's tracked only when
the work tab is open and in focus in the console. If the agent switches console tabs, the time
spent on the other tabs isn't counted. Active time continues to count if you switch to a new
browser tab or window. Active time stops when the agent closes the work item or the after
conversation work time ends, whichever happens first.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that an agent extended the After Conversation Work (ACW) timer. This
field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of time (in seconds) that the After Conversation Work (ACW) timer was extended
each time that the agent extended the timer. This field is available in API version 55.0 and
later.

To find the total extension duration, multiply this field by `AcwExtensionCount` or use
`AfterConversationActualTime` .

**Type**
int


Standard Objects AgentWork

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of seconds an agent spent on After Conversation Work (ACW) after customer
contact ended. This field is available in API version 52.0 and later.

```
AgentCapacityWhenDeclined

AssignedDateTime

BotId

BotType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The agent’s capacity when declining work, either explicitly or through push timeout.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was assigned to an agent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Enhanced Einstein Bot or AI agent that performed the work. This is a relationship
field. This field is available in API version 52.0 and later.

**Relationship Name**
Bot

**Relationship Type**
Lookup

**Refers To**
BotDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of bot. Valid values are:

**•** Bot. Refers to an Einstein bot.


Standard Objects AgentWork

**Field** **Details**

**•** ExternalCopilot. Refers to an AI agent with whom your customers can interact.

The default value is Bot. This field is available in API version 63.0 and later.

```
CancelDateTime

CapacityModel

CapacityPercentage

CapacityWeight

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was canceled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the capacity model used to determine agent capacity. Valid values are
`StatusBased` and `TabBased` . This field is available in API version 50.0 and later.

A work item consumes agent capacity only if it was first assigned to the agent by Omni-Channel
using queues or skills.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is in progress.
Valid values are from 0 to 100.

The agent can receive a new work item only if they have enough available capacity for the
item. Voice calls must have a capacity percentage of _`100`_, so an agent on a call doesn’t
receive new work items until the call ends.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The amount of an agent’s capacity that’s consumed when this work item is in progress.

For example, if cases are assigned a capacity weight of _`2`_, an agent with a capacity of _`6`_ can
accept up to 3 cases before the agent is at capacity and can’t receive new work items.

Voice calls must use the entire capacity weight.


Standard Objects AgentWork

**Field** **Details**

```
CloseDateTime

DeclineDateTime

DeclineReason

ExternalBotId

HandleTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was closed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the agent declined this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The provided reason for why an agent declined the work request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the third-party bot that handles the work item. This is a relationship field. This field
is available in API version 64.0 and later.

**Relationship Name**
ExternalBot

**Relationship Type**
Lookup

**Refers To**
ExternalConversationBotDef

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The amount of time an agent had the work item open, calculated by `CloseDateTime`

                          - `AcceptedDateTime` . Handle time stops when the agent closes the work item or the
after conversation work time ends, whichever happens first.

```
IsConference

IsInterruptible

IsOwnerChangeInitiated

IsPreferredUserRequired

IsStatusChangeInitiated

```

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the agent was conferenced on the work item by another agent ( `true` )
or not ( `false` ). The default value is `false` . Available in API version 44.0 and later. This
field is accessible in Reports, but not via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item consumes interruptible or primary capacity. The default value
is false. Available in API version 57.0 and later when the Interruptible Capacity feature is
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item owner change triggered the direct assignment of the work
item to the agent. The default value is `false` . Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item stays with the preferred user even when the user isn’t available.
The default value is false. This field is available in API version 50.0 and later.

**Type**
boolean


Standard Objects AgentWork

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item status change triggered the direct assignment of the work
item to the agent. The default value is false. Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

```
IsTransfer

Name

OriginalGroupId

OriginalQueueId

```

**Type**
boolean

**Properties**
Filter,Group, Sort

**Description**
Indicates whether the agent received the work item through transfer from another agent
( `true` ) or not ( `false` ). The default value is `false` . Available in API version 38.0 and later.
This field is accesible in Reports, but not via the API.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the queue that the work assignment was originally routed to. This field is a
relationship field.

**Relationship Name**
OriginalGroup

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The ID of the queue that the work assignment was originally routed to. Due to API changes,
`OriginalQueueId` is no longer recommended. Use `OriginalGroupId` instead.

```
OwnerId

PausedCapacityPercentage

PausedCapacityWeight

PendingServiceRoutingId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the AgentWork. This field is a polymorphic relationship field. This field
is available in API version 50.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity and Enhanced Omni-Channel
only. This field is available in API version 62.0 and later.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity and Enhanced Omni-Channel
only. This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The ID of the PendingServiceRouting on page 4114 from which the AgentWork was created.
This field is a relationship field. This field is available in API version 50.0 and later.

**Relationship Name**
PendingServiceRouting

**Relationship Type**
Lookup

**Refers To**
PendingServiceRouting

```
PreferredUserId

PushTimeout

PushTimeoutDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the preferred user to handle the work. This field is a relationship field. This field is
available in API v46.0 and later.

**Relationship Name**
PreferredUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time limit set for an agent to respond to an item before it’s pushed to another agent.
The time limit is measured in seconds. This field is available in API version 36.0 and later.

Effective API version 57.0, for inbound Voice calls, this field represents the time limit set for
an agent to respond to a call before it’s declined. The value must be between 0 and 20. The
value is capped at 20, so any number greater than that is treated as 20 seconds. This applies
to the following telephony models:

**•** Salesforce Voice with Amazon Connect

**•** Salesforce Voice with Partner Telephony from Amazon Connect

**Type**
dateTime


Standard Objects AgentWork

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the push timeout event occurred. This field is available in
API version 36.0 and later.

```
RequestDateTime

RoutingModel

RoutingPriority

RoutingType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work was requested.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines how incoming work items are routed to agents assigned to a service channel.
Possible values are:

**•** `ExternalRouting`

**•** `LeastActive`

**•** `MostAvailable`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which work items from the queue that are associated with the routing
configuration are routed to agents.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Omni-Channel routing. Possible values are:

**•** `QueueBased`

**•** `SkillsBased`


Standard Objects AgentWork

**Field** **Details**

```
SecondaryRoutingPriority

ServiceChannelId

ShouldSkipCapacityCheck

SpeedToAnswer

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the secondary routing priority.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel that’s associated with the work assignment. This field is a
relationship field.

**Relationship Name**
ServiceChannel

**Relationship Type**
Lookup

**Refers To**
ServiceChannel

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to skip checking an agent’s available capacity ( `true` ) or not ( `false` )
when an externally routed work item is created. This field is used when agents can
simultaneously handle work from both Omni-Channel queues and queues using external
routing.

When `true`, the receiving agent can exceed their set capacity to accept the item, but they
don’t receive more Omni-Channel routed work. When `false`, the receiving agent can’t
exceed their set capacity and must have enough open capacity to accept the item.

The default value is `false` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time between when the work was requested and when an agent accepted
it.


Standard Objects AgentWork

**Field** **Details**

```
Status

TargetAcceptDateTime

TransferRequesterId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The working status of the work item. Valid values are:

**•** `Assigned`  - The item is assigned to the agent but hasn’t been opened.

**•** `Canceled`  - The item no longer needs to be routed. For example: a chat visitor cancels
their Omni-Channel routed chat request before it reaches an agent.

**•** `Closed`  - The item is closed.

**•** `Declined`  - The item was assigned to the agent but the agent explicitly declined it.

**•** `DeclinedOnPushTimeout`  - The item was declined because push time-out is
enabled and the item request timed out with the agent.

**•** `Opened`  - The agent opened the item.

**•** `Transferred` –The item was transferred from an agent to another agent, queue, or
skill.

**•** `Unavailable`  - The item was assigned to the agent but the agent became unavailable
(went offline or lost connection).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time by when a rep must accept a work item. Influences backlog ordering by
prioritizing work items with earlier target acceptance deadlines. The field can be dynamically
set using Flow for each work item during the routing process. This allows for flexible
prioritization based on case urgency, customer tier, or other business rules. Available in API
version 65.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the rep who reassigned the work using the Reassign action. This field is
populated in reassigned AgentWork records only, not the original AgentWork record. This
is a relationship field. This field is available in API version 63.0 and later.

**Relationship Name**
TransferRequester

**Relationship Type**
Lookup


Standard Objects AgentWork

**Field** **Details**

**Refers To**
User

```
UserId

WorkItemId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that the work item was assigned to. This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object that’s routed to the agent through Omni-Channel.

This field is a polymorphic relationship field.

**Relationship Name**
WorkItem

**Relationship Type**
Lookup

**Refers To**
Custom objects and these standard objects: Account, Activity, Case, Claim, ClaimCoverage,
ClaimRecovery, Contact, ContactRequest, CustomEntityData, Incident, Lead,
LiveChatTranscript, MessagingSession, Opportunity, Orchestration Work Items, Order,
PaymentRequest, PersonTraining,Referral, SocialPost, SwarmMember, and VoiceCall.
WorkOrder is available in version 58.0 and later.

`AgentWork` records can only be deleted if they have the status Closed, Declined, or Unavailable. They can’t be deleted if their status
is Assigned or Opened because they’re active in Omni-Channel.

When `AgentWork` records are created, they have the status Assigned. After a record is created, it’s automatically pushed to the
assigned agent.


### Standard Objects AgentWorkConversationalData While the metadata for AgentWork indicates support for upsert() and update(), these calls aren’t used with AgentWork

because none of its fields can be updated.

### Apex triggers are supported with AgentWork .

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**AgentWorkChangeEvent (API version 63.0)**
Change events are available for the object.

**AgentWorkOwnerSharingRule**

Sharing rules are available for the object.

**AgentWorkShare**

Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Understand the Details of the Routing Lifecycle](https://help.salesforce.com/s/articleView?id=service.omnichannel_psr_lifecycle.htm&type=5&language=en_US)

### AgentWorkConversationalData

Stores conversation data for agent work sessions, such as agent interactions, transfer information, and operational metrics. This object
is available in API version 66.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

You must have the Agentforce Contact Center Admin (Salesforce Voice) permission set enabled in your org.

Fields

**Field** **Details**

```
AgentChannelRecordingId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier for the recording associated with the agent channel conversation.

This field is a relationship field.

**Relationship Name**
AgentChannelRecording


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Refers To**
VoiceCallRecording

```
AgentConnectDateTime

AgentCustomerMergeTime

AgentDisconnectDateTime

AgentId

AgentType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the agent connected to the conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the service rep and customer conversations are merged after consultation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the agent disconnected from the conversation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of an agent or a rep involved in the conversation.

This field is a polymorphic relationship field.

**Relationship Name**
Agent

**Refers To**
BotDefinition, ExternalConversationBotDef, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Description**
Type of agent handling the conversation.

Possible values are:

**•** `ExternalBot`

**•** `Human`

**•** `InternalBot`

```
AgentWorkId

ChannelSessionRecordId

LongestPauseDuration

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the `AgentWork` record associated with the conversational data.

This field is a relationship field.

**Relationship Name**
AgentWork

**Refers To**
AgentWork

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the channel session for the conversation.

This field is a relationship field.

**Relationship Name**
ChannelSessionRecord

**Refers To**
VoiceCall

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Duration of the longest pause during the conversation, measured in seconds.

**Type**
string


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the agent work conversational data record.

```
NextAgentWorkConvId

OwnerId

OwnershipEndDateTime

OwnershipStartDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the next record in a sequence of conversations.

This field is a relationship field.

**Relationship Name**
NextAgentWorkConv

**Refers To**
AgentWorkConversationalData

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the conversational data record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when ownership of the conversation ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Description**
Timestamp for when ownership of this conversation started.

```
PauseCount

PrevAgentWorkConvId

QualityScore

TotalPauseDuration

TransferType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of times the conversation was paused.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the previous record in a sequence of conversations.

This field is a relationship field.

**Relationship Name**
PrevAgentWorkConv

**Refers To**
AgentWorkConversationalData

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Value of the Mean Opinion Score (MOS) that measures voice call quality.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total duration of all pauses during the conversation, measured in seconds.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects AgentWorkSkill

**Field** **Details**

**Description**
Type of transfer for the conversation.

Possible values are:

**•** `Cold`

**•** `Warm`

### AgentWorkSkill

Represents a skill used to route a work assignment to an agent. AgentWorkSkill is used for reporting and represents the result of a routing
decision. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AgentWorkId

IsAdditionalSkill

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The AgentWork object associated with this skill.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
After a designated timeout period, a skill marked as additional is dropped from Omni-Channel
routing. The case is then routed to the best-matched agent, even if the agent doesn’t have
all the skills. The default value is false. Available in API version 48.0 and later.


Standard Objects AgentWorkSkill

**Field** **Details**

```
Name

SkillId

SkillLevel

SkillPriority

WasDropped

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The skill that is required or additional.

**Type**
double

**Properties**
Filter, Sort

**Description**
The level of the required or additional skill. Skill levels can range from 1 to 10. Depending on
your business needs, you might want the skill level to reflect years of experience, certification
levels, or license classes.

**Type**
int

**Properties**
Aggregatable, Filter, Group, Nillable, Sort

**Description**
For additional skills, specifies the order in which skills are dropped if after the specified timeout
no agent with that skill is available. Higher priority-value skills are dropped first. Lower
priority-value skills, for example 0, are dropped last. Skills with the same priority value are
dropped as a group. You can set skill priority using attribute setup for skills-based routing or
Apex code.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
For skills marked as additional, indicates if the skill was dropped from Omni-Channel routing
because an agent with this skill was not available. The default value is false. Available in API
version 48.0 and later.


### Standard Objects AIApplication

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AgentWorkSkillChangeEvent (API version 62.0)**
Change events are available for the object.

### AIApplication

Represents an AI application such as Einstein Prediction Builder. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

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
The language of the application. Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish


Standard Objects AIApplication

**Field** **Details**

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

Status

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the AI application throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the application if installed with a managed package.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of the AI application. Possible values are:

**•** `Disabled`

**•** `Enabled`

**•** `Migrated`


### Standard Objects AIApplicationConfig

**Field** **Details**

```
Type

### AIApplicationConfig

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of application. Possible values are:

**•** `PredictionBuilder`

Additional prediction information related to an AI application. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

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
The language of the application. Possible values are:


### Standard Objects AiGenActionItem

**Field** **Details**

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

### AiGenActionItem

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the AI application throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the application config, if installed with a managed package.

Represents business actions suggested by generative AI. AI-generated action items are sent to either agents for automatic execution or
human users for review, depending on org preference and if there are any errors in the process. This object is available in API version
64.0 and later.


Standard Objects AiGenActionItem

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`

Special Access Rules

Agentforce Pipeline Management must be enabled. Only the agent user can create AiGenActionItem records.

Fields

**Field** **Details**

```
ActionItemOwnerId

ActionResult

AgentType

AiGenActionItemInfoId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID associated with the owner of the AI-generated action item. The owner can be an
agent or human user, and can change during the review and execution process. By default,
the owner is an agent or queue.

This field is a polymorphic relationship field.

**Relationship Name**
ActionItemOwner

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The result generated when the agent action is executed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The specific agent that processes the AI-generated action item.

**Type**
reference


Standard Objects AiGenActionItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the AI-generated action item information record associated with this action item.
Available in API version 67.0 and later.

This field is a relationship field.

**Relationship Name**
AiGenActionItemInfo

**Refers To**
AiGenActionItemInfo

BotDefinitionId

BotVersionId

```
Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bot record with a template name that matches the value in the Sales Management agent
template.

This field is a relationship field.

**Relationship Name**
BotDefinition

**Refers To**
BotDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bot version from the bot record with an ID that matches the ID of the Sales Management
agent bot record.

This field is a relationship field.

**Relationship Name**
BotVersion

**Refers To**
BotVersion

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects AiGenActionItem

**Field** **Details**

**Description**
The explanation of why the action item has been suggested. The description provides
additional context to guide human users and agents in their decision-making.

```
ExpirationDate

GeneratedResponseIdRef

OwnerId

ParentId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date that the action item expires and is deleted. AI-generated action items are no longer
visible to users after 14 days and removed from records after 30 days.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of generated result in the GenAIGeneration DMO. This field can be used by human
users to provide feedback on the AI-generated action item.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the record that the AI-generated action item is associated with. Available in API
version 67.0 and later.

This field is a polymorphic relationship field.


Standard Objects AiGenActionItem

**Field** **Details**

**Relationship Name**
Parent

**Refers To**
Account, Opportunity

```
Status

Subject

SuggestedNewValue

Type

UnmodActionItemOutput

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the AI-generated action item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject line that displays to users indicating what the action item is.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The new field value suggested by generative AI for the action item. Available in API version
67.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that the action item falls under. This field can be used to search for specific
action items, such as field updates or follow-up sales emails.

**Type**
textarea

**Properties**
Nillable

**Description**
The unmodified output for the action item produced by AI, whether from a prompt template
or other generation method.


### Standard Objects AIInsightAction

**Field** **Details**

```
Utterance

### AIInsightAction

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The user utterance or prompt that generated this action item. Available in API version 67.0
and later.

Represents an Einstein prediction insight action. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightAction is a one-to-many child of AIRecordInsight. AIInsightAction contains information about predicted actions for this particular

insight. AIInsightAction has one or more AIInsightValue children which contain predicted values for the action. For example, an
### AIInsightAction could represent a quick action, and have a child AIInsightValue with the recommended value used by the quick action.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
ActionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated action, such as the ID of a Macro.

This is a polymorphic relationship field.

**Relationship Name**
Action

**Relationship Type**
Lookup


Standard Objects AIInsightAction

**Field** **Details**

**Refers To**
ApexClass, AuraDefinitionBundle

```
ActionName

AiRecordInsightId

Confidence

Name

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The ID of the action. For example, a value of “Case.SendEmail” indicates a send email quick
action on Case.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightAction.


### Standard Objects AIInsightFeedback

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
The type of action. Possible values are:

**•** `InvocableAction` —Invocable Action

**•** `Macro` —Macro

**•** `QuickAction` —Quick action.

**•** `StandardAction` —Standard Action. An example standard action would be to
update a record.

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

### AIInsightFeedback

Represents an Einstein prediction insight feedback. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightFeedback is a one-to-many child of AIRecordInsight. AIInsightFeedback contains information about explicit and implicit feedback

collected from users for a particular insight.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects AIInsightFeedback

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
ActualValue

AiFeedback

AiInsightFeedbackType

AiRecordInsightId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The raw feedback value. This field is null when no recommendation is selected.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The feedback user sentiment. Possible values are:

**•** `Negative` —Negative feedback

**•** `Neutral` —Neutral feedback

**•** `Positive` —Positive feedback

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The nature of the feedback. Possible values are:

**•** `Explicit` —Explicit feedback. For example, a user applies and saves an Einstein
recommendation on a case.

**•** `Implicit` —Implicit feedback. For example, a user edits or updates a case field without
viewing or applying field recommendations from Einstein.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.


Standard Objects AIInsightFeedback

**Field** **Details**

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

```
 Name

 Rank

 ValueId

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightFeedback.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feedback score.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightValue.

This is a polymorphic relationship field.

**Relationship Name**
Value

**Relationship Type**
Lookup

**Refers To**
AIInsightAction, AIInsightValue

Salesforce creates AIInsightFeedback records based on user responses to predictions after the prediction has been created. User feedback,
such as a thumbs up/down response or accepting a recommended value, results in the creation of a feedback record in which the
feedback type is explicit. An implicit feedback record is created when Einstein makes a recommendation but the field is updated in
another way, for example, by a process. Once the AIInsightFeedback record has been created, it’s immutable.


### Standard Objects AIInsightReason

Custom fields can’t be added to Einstein insight objects.

### AIInsightReason

Represents an Einstein prediction insight reason. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightReason is a one-to-many child of AIInsightValue. AIInsightReason contains details about how Einstein predicted an insight value.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
AiInsightValueId

Contribution

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIInsightValue.

This is a relationship field.

**Relationship Name**
AiInsightValue

**Relationship Type**
Lookup

**Refers To**
AIInsightValue

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The contribution weight for this insight reason.


Standard Objects AIInsightReason

**Field** **Details**

```
FeatureType

FeatureValue

FieldName

FieldValue

Intensity

Name

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the feature, such as BOOL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the feature, such as TRUE or FALSE.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the field the insight uses for its evaluation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value for the field the insight uses for its evaluation.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The intensity weight for this insight reason.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightReason.


Standard Objects AIInsightReason

**Field** **Details**

```
Operator

ReasonLabelKey (Beta)

RelatedInsightReasonId

(Beta)

SortOrder (Beta)

Variance

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The logical operator the insight uses to compare the field value with the expression value.
For example, if the prediction evaluates whether the fieldValue for the field `bonus__c` is
greater than $5,000, the logical operator is `greater than` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key used to map an Einstein Key Accounts Identification (Beta) insight phrase or phrases
to the correct messaging template.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID used to relate multiple insights to a single model reason in the Einstein Key Accounts
Identification (Beta) feature.

This is a relationship field.

**Relationship Name**
RelatedInsightReason

**Relationship Type**
Lookup

**Refers To**
AIInsightReason

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number value used to organize the phrases in the model’s insights message in the Einstein
Key Accounts Identification (Beta) feature.

**Type**
double


### Standard Objects AIInsightValue

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The variance weight for this insight reason.

Usage

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

### AIInsightValue

Represents an Einstein prediction insight value. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightValue is a one-to-many child of AIRecordInsight. AIInsightValue represents a predicted value of a predicted insight.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available when Einstein features such as Prediction Builder or Case Classification are enabled. To access an AIInsightValue record, you
must have access to the related AIRecordInsight record. To grant a user the right to create an AIInsightValue record, you can use the
AICreateInsightObjects or the CreateAIInsights permission.


Standard Objects AIInsightValue

Fields

**Field** **Details**

```
AiInsightActionId

AiRecordInsightId

Confidence

Field

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightAction.

This is a relationship field.

**Relationship Name**
AiInsightAction

**Relationship Type**
Lookup

**Refers To**
AIInsightAction

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

**Type**
picklist


Standard Objects AIInsightValue

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the target field Einstein is making predictions for, such as “AnnualRevenue”.

```
FieldValueLowerBound

FieldValueUpperBound

Name

SobjectLookupValueId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The lower bound value.

**Type**
textarea

**Properties**
Nillable

**Description**
The upper bound value.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightValue.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the value object, if this insight value references an object.

This is a relationship field.

**Relationship Name**
SobjectLookupValue

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskIndDefinition,


Standard Objects AIInsightValue

**Field** **Details**

AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, AssociatedLocation,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CampaignMember, CardPaymentMethod, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CodeSetBundle, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, ContactRequest, ContentVersion, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo, CreditMemoLine,
DataUseLegalBasis, DataUsePurpose, DelegatedAccount, DigitalWallet,
DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument,
Image, Individual, IndividualApplication, Invoice, InvoiceLine, Lead, Location,
LocationTrustMeasure, MemberPlan, MessagingEndUser, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, Order, OrderItem, OtherComponentTask,
PartyConsent, Payment, PaymentAuthAdjustment, PaymentAuthorization, PaymentGateway,
PaymentGroup, PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry, ProcessException,
Product2, ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PurchaserPlan,
PurchaserPlanAssn, QuickText, ReceivedDocument, Recommendation, Refund,
RefundLinePayment, ReportAnomalyEventStore, ResourceAbsence, ResourcePreference,
ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore,
SharingRecordCollection, Shift, Shipment, ShipmentItem, SkillRequirement, SocialPersona,
SocialPost, Solution, Task, TimeSlot, UnitOfMeasure, UserProvisioningRequest, VideoCall, Visit,
VisitedParty, Visitor, VoiceCall, VolunteerProject, WorkBadge, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
SobjectType

```

**Type**
picklist


Standard Objects AIInsightValue

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the value object, such as Account or Case, if this insight value references an
object.

```
 Value

 ValueType

```

Usage

**Type**
textarea

**Properties**
Nillable

**Description**
The prediction result insight value.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the prediction result insight value. Possible values are:

**•** `Boolean` —Boolean

**•** `Currency` —Currency

**•** `DateTime` —DateTime

**•** `Enum` —Enum

**•** `Lookup` —Lookup

**•** `Number` —Number

**•** `String` —String

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.


### Standard Objects AiJobRun

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

### AiJobRun

Represents an execution instance of an AI job. This object tracks the overall status and manages the lifecycle of the job from initiation
to completion. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EndTime

ErrorCode

ErrorMessage

JobType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the job run ends.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the job run fails, this field indicates the specific error that occurred.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a detailed, human-readable message that explains the reason for the job run failure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects AiJobRun

**Field** **Details**

**Description**
Defines the job's logic.

Possible values are:

**•** `PromptTemplate`

```
Label

Name

OwnerId

StartTime

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A user-defined name or label for the job run, which can be used for identification and tracking.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique, system-generated identifier for the `AiJobRun` record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user group that owns the `AiJobRun` record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the job run's status changes to `InProgress` .

**Type**
picklist


### Standard Objects AiJobRunItem

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tracks the lifecycle of the job run. Valid values are:

**•** `New` : The job run has been created.

**•** `ReadyToStart` : The job run is ready for the user to initiate processing.

**•** `Queued` : The job run is queued to start.

**•** `InProgress` : The job run is currently processing.

**•** `Completed` : The job run completed.

**•** `Failed` : The job run failed.

**•** `Aborted` : The job run was aborted by the user.

**•** `Archived` : The job run was archived by the user.

```
Target

### AiJobRunItem

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A metadata field used to specify job-specific details, such as a `PromptTemplateId`,
`PromptTemplateName`, or `ModelId` . This provides further context for the job
execution.

Stores an individual item associated with a parent AiJobRun, including the inputs and resulting response. This object is available in API
version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AiJobRunId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AiJobRunItem

**Field** **Details**

**Description**
A required reference to the parent AiJobRun record that this item belongs to.

This field is a relationship field.

**Relationship Name**
AiJobRun

**Refers To**
AiJobRun

```
ErrorCode

ErrorMessage

Input

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If processing for this item fails, this field contains a numeric code indicating the error.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a detailed, human-readable message that explains the reason for the job run item
failure.

**Type**
textarea

**Properties**
Create, Update

**Description**
Contains the input data for a single item within the job run. For example, in a PromptTemplate
job, this is the JSON input for the prompt template.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique, system-generated identifier for the AiJobRunItem record.

**Type**
reference


### Standard Objects AiModelLanguage

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user or group that owns the AiJobRunItem record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
PreprocessedInput

Response

Status

### AiModelLanguage

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Stores an intermediate version of the input data after the preprocessing step. For example,
this field could be a hydrated JSON prompt.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the generated response for the job item after processing is complete.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tracks the status of the individual job item. Valid values are:

**•** `Ready` : The default value. The job run item is ready to start processing.

**•** `Completed` : Processing for the job run item is complete.

**•** `Failed` : Processing for the job run item failed.

An object that stores language related information that is generated for each AI model. This object is available in API version 55.0 and
later.


Standard Objects AiModelLanguage

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

For Einstein Reply Recommendations:

Requires the Einstein Reply Recommendations org permissions, Einstein Reply Recommendations org pref, and Admin user or user with
Einstein Reply Manager permissions.

Fields

**Field** **Details**

```
ApplicationType

ExternalAiModelId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of application using the AI model.

Possible values are:

**•** `ARTICLE_RECOMMENDATION`

**•** `EAR_FOR_CONVERSATION`

**•** `EAR_FOR_VOICE`

**•** `FAQ`

**•** `REPLY_RECOMMENDATION`

**•** `USE_CASE_EXPLORER`

**•** `UTTERANCE_RECOMMENDATION`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the AI model used to generate predictions.

This field is a relationship field.

**Relationship Name**
ExternalAiModel

**Relationship Type**
Lookup

**Refers To**
ExternalAIModel


Standard Objects AiModelLanguage

**Field** **Details**

```
Language

Name

ServingStatus

TranscriptCount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Languages supported by this AI model.

Possible values are:

**•** `Arabic`

**•** `Chinese-simplified`

**•** `Chinese-traditional`

**•** `Dutch`

**•** `English`

**•** `French`

**•** `German`

**•** `Italian`

**•** `Japanese`

**•** `Korean`

**•** `Polish`

**•** `Portuguese`

**•** `Russian`

**•** `Spanish`

**•** `Thai`

**•** `Turkish`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
AI model name.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the language is enabled or disabled for this AI model.

**Type**
int


### Standard Objects AIRecordInsight

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Transcript count detected for each language.

### AIRecordInsight

Represents an Einstein prediction insight. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIRecordInsight contains information on the Einstein prediction, the AI prediction field where results were written, and other details

such as the type of prediction.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

Prediction insight objects are available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
AiApplicationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the AiApplication that generated this prediction.

This is a relationship field.

**Relationship Name**
AiApplication

**Relationship Type**
Lookup

**Refers To**
AIApplication


Standard Objects AIRecordInsight

**Field** **Details**

```
Confidence

MlPredictionDefinitionId

ModelId

Name

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight, from 0.0 to 1.0. Higher
values (near 1.0) indicate stronger confidence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is a relationship field.

**Relationship Name**
MlPredictionDefinition

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the model to use when generating the insight.

This field is a polymorphic relationship field.

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
The name of the AIRecordInsight.


Standard Objects AIRecordInsight

**Field** **Details**

```
PredictionField

RunGuid

RunStartTime

Status

TargetField

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the field that Einstein is making predictions for, such as “Case.IsEscalated”.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A unique identifier for the Einstein process that made the prediction.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the Einstein prediction process was started.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this insight. Possible values are:

**•** `Defunct` —The insight has been consumed by the Einstein feature that owns the
prediction. For example, Case Classification marks an insight as defunct if a predicted
recommendation was presented to a user and the user either accepted or ignored the
recommendation. This behavior ensures that the same recommendation isn’t presented
multiple times to the user.

**•** `New` —The insight hasn’t been consumed by the Einstein feature.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The field to which prediction results are written. Case Classification doesn’t use this field.


Standard Objects AIRecordInsight

**Field** **Details**

```
TargetId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the record Einstein is making predictions for.

This is a relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskIndDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, AssociatedLocation,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CampaignMember, CardPaymentMethod, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CodeSetBundle, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, ContactRequest, ContentVersion, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo, CreditMemoLine,
DataUseLegalBasis, DataUsePurpose, DelegatedAccount, DigitalWallet,
DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument,
Image, Individual, IndividualApplication, Invoice, InvoiceLine, Lead, Location,
LocationTrustMeasure, MemberPlan, MessagingEndUser, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, Order, OrderItem, OtherComponentTask,
PartyConsent, Payment, PaymentAuthAdjustment, PaymentAuthorization, PaymentGateway,
PaymentGroup, PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,


Standard Objects AIRecordInsight

**Field** **Details**

PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry, ProcessException,
Product2, ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PurchaserPlan,
PurchaserPlanAssn, QuickText, ReceivedDocument, Recommendation, Refund,
RefundLinePayment, ReportAnomalyEventStore, ResourceAbsence, ResourcePreference,
ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore,
SharingRecordCollection, Shift, Shipment, ShipmentItem, SkillRequirement, SocialPersona,
SocialPost, Solution, Task, TimeSlot, UnitOfMeasure, UserProvisioningRequest, VideoCall, Visit,
VisitedParty, Visitor, VoiceCall, VolunteerProject, WorkBadge, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
TargetSobjectType

Type

ValidUntil

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target object, such as Account or Case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values are:

**•** `Action` —An insight that indicates a suggested action, such as sending an email.

**•** `Lookup` —An insight that indicates a related value not directly related to the target
object and field.

**•** `MultiValue` —An insight with multiple values, such as a multi-class classification.

**•** `SimilarRecord` —An insight that indicates similar or duplicate records.

**•** `SingleValue` —A single value insight, such as a regression number or a score.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The day and time this insight is valid until. After this day and time, the insight might no longer
be valid due to new prediction results from new or changed data. If this field is `null`, this
insight never expires.


### Standard Objects AIResearchPromptResult

Usage

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

Considerations for Case Classification

To generate reports on the effectiveness of Einstein Case Classification predictions, use the root AIRecordInsight object and its child
[objects, AIInsightFeedback and AIInsightValue. For example, you can determine how many cases received predictions, or how often](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_aiinsightfeedback.htm)
agents accepted or rejected them.

**•** To determine how many cases received recommendations, the AIRecordInsight table identifies the case and contains a row for each
field and each recommendation. In AIRecordInsight, the TargetId field contains the case ID. The PredictionField indicates which case
field is being predicted. Each field value recommendation is contained in a separate AIInsightValue object with AIRecordInsight as
the parent. For a picklist field, Einstein creates AIInsightValue objects with up to 10 field value recommendations. However, just the
top three predictions appear to agents in the Einstein Field Recommendations component.

**•** To learn whether agents acted on any of the top three predictions, use the AIInsightFeedback object. When an agent updates fields
after viewing Einstein’s recommendations, or when Einstein applies a recommendation automatically, the object’s
AiInsightFeedbackType field contains Explicit. If the agent updates fields without viewing the predictions, such as on the case details
tab, AiInsightFeedbackType is set to Implicit. When the agent applies the recommended value, the object’s AiFeedback field is set
to Positive; if the agent applies a different value, AiFeedback is Negative.

### AIResearchPromptResult

Represents the research result generated by Agentforce or by a generative AI feature from a standard or custom prompt template. This
object is available in API version 64.0 and later.

When an Agentforce or a generative AI feature researches a record and saves the results, an AIResearchPromptResult record is created
and populated with information about the researched record.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`


Standard Objects AIResearchPromptResult

Special Access Rules

Research results are only available in orgs that have Agentforce or generative AI features enabled.

Fields

**Field** **Details**

AiGenActionItemId

IsToxicityDetected

```
LatestErrorMessage

LatestGenResponseIdRef

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business action suggested by generative AI.

This field is a polymorphic relationship field.

**Relationship Name**
AiGenActionItem

**Refers To**
AiGenActionItem

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the generated response contains toxic language ( `true` ) or not ( `false` ).
The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error message that displays if the result can't be generated.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the most recently generated result in the GenAIGeneration object. The object is
derived from the Data Cloud data model object (DMO).


Standard Objects AIResearchPromptResult

**Field** **Details**

```
LatestGenerationDate

LatestResult

LatestSafetyScore

LatestStatus

OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the result was most recently generated.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The AI-generated result.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Overall safety score for the generated research. A higher value means the generated response
is more likely to be safe. Minimum value of 0.0. Maximum value of 1.0.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the generated result.

Possible values are:

**•** `Generating`

**•** `Success`

**•** `Failed`

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the generated research result.

This field is a polymorphic relationship field.


Standard Objects AIResearchPromptResult

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
Group, User

```
ReferenceRecordId

StandardPromptTemplate

```

Version

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID that the research result was generated for.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Refers To**
Account, Contact, Lead, Opportunity

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The standard prompt template used to generate the result.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prompt template version number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AIResearchPromptResultFeed on page 55**
Feed tracking is available for the object.

**AIResearchPromptResultHistory on page 63**
History is available for tracked fields of the object.

**AIResearchPromptResultOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects AllowedEmailDomain

**AIResearchPromptResultShare on page 67**
Sharing is available for the object.

### AllowedEmailDomain

Represents an allowed email domain for users in your organization. You can define an allowlist to restrict the email domains allowed in
a user’s `Email` field. This object is available in API version 29.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “Manage Internal Users” user permission to use this object.

Note: If you don't see this object, contact your Salesforce representative to enable it.

Fields

**Field** **Details**

```
Domain

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
An allowed email domain for users.

### AlternativePaymentMethod

Represents a payment method that isn’t cash, a debit card, or a credit card. This object defines methods that aren’t defined by the
CardPaymentMethod or DigitalWallet objects. Examples of alternative payment methods include CashOnDeliver, Klarna, and Direct
### Debit. AlternativePaymentMethod functions the same as any other type of payment method for processing transactions

through a payment gateway. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects AlternativePaymentMethod

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

AlternativePaymentMethod

Number

AuditEmail

BankAccountHolderType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account for the alternative payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce ID number for the alternative payment method.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the payment owner where audit information about payments is sent.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines if the bank account is held by a business or an individual.


Standard Objects AlternativePaymentMethod

**Field** **Details**

Possible values are:

**•** `Business`

**•** `Individual`

```
BankAccountType

BillingFirstName

BillingLastName

BillingName

Comments

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of bank account such as a checking or savings account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first and last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

```
CompanyName

Email

```

ExtendedPaymentMethodType

```
GatewayToken

GatewayTokenDetails

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name for this payment method. Part of the payment method’s address.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Other alternative payment methods used for the transaction. This field is available in API
version 66.0 and later.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Tokenized form of the alternative payment method, returned by the gateway. Stored as
encrypted text.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique tokenized ID generated by the payment gateway when this payment method first
interacts with the gateway. Used to identify the payment method during future transactions.


Standard Objects AlternativePaymentMethod

**Field** **Details**

```
IpAddress

IsAutoPayEnabled

LastReferencedDate

LastViewedDate

MacAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address for the payment method owner.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Alternative Payment Method page layout in the UI. It isn't automatically
added.

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
it's possible the user only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mac Address of the payment method holder.


Standard Objects AlternativePaymentMethod

**Field** **Details**

```
NickName

OwnerId

PaymentGatewayId

PaymentMethodAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined nickname for this payment method.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the alternative payment method.

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
ID of the payment gateway entity used to handle transactions from this payment method.

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


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
Full address associated with the alternative payment method. For more information about
address fields, see Address Compound Fields.

```
PaymentMethodCity

PaymentMethodCountry

PaymentMethodDetails

PaymentMethodGeocode

Accuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

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


Standard Objects AlternativePaymentMethod

**Field** **Details**

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
PaymentMethodLatitude

PaymentMethodLongitude

PaymentMethodPostalCode

PaymentMethodState

PaymentMethodStreet

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Longitude of the payment method address. Used with the PaymentMethodLatitude to
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
Details of the address for this payment method.

```
PaymentMethodSubType

PaymentMethodType

Phone

ProcessingMode

SavedPaymentMethodId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be a digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction, such as Visa, Mastercard, EPS, SepaDebit, and
Klarna. This field is available in API version 57.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payment method's owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the payment method was created in Salesforce or externally. Required.

Possible values are:

**•** `External` : Select this value if you create the alternative payment method record
through any method other than the Salesforce Payments Connect API.

**•** `Salesforce` : Select this value if you use Salesforce Payments Connect API to create
the alternative payment method record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects AnalyticsAssetAction

**Field** **Details**

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

```
StandardEntryClassCode

Status

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A three-letter code that indicates how a customer or a business initiated and authorized an
ACH payment.

Possible values are:

**•** `CCD` —Corporate credit or debit entry

**•** `PPD` —Pre-arranged payment and deposit entry

**•** `TEL` —Telephone-initiated entry

**•** `WEB` —Internet or mobile-initiated entry

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the payment method. Required.

Possible values are:

**•** `Active` —The Payments platform can use the alternative payment method to make
payments. Active alternative payment methods can't be deleted.

**•** `Canceled` —The Payments platform can no longer use the payment method to make
payments. A value of `Canceled` can't be changed back to `Active` or `Inactive`

**•** `InActive` —The Payment platform currently can't use the payment method to make
payments. Admins can change this value to `Active` or `Canceled` when needed.

### AnalyticsAssetAction

Represents a Tableau Next asset action. This object is available in API version 67.0 and later.


Standard Objects AnalyticsAssetAction

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
ActionType

AssetId

EventType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of asset action.

Possible values are:

**•** `filter`

**•** `flow`

**•** `navigate`

**•** `parameter`

**•** `recordaction`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the asset the action is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
Asset

**Relationship Type**
Master-detail

**Refers To**
AnalyticsDashboardWidget, AnalyticsVisualization

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects AnalyticsChangeEventLog

**Field** **Details**

**Description**
The widget event type that triggers the action.

Possible values are:

**•** `click`

**•** `select`

```
Version

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The version of the asset action.

### AnalyticsChangeEventLog

Analytics Change Event Logs represent route or page changes made in the CRM Analytics. This object is available in API version 61.0 and
later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location where the dashboard is displayed. In the Salesforce mobile app, embedded
dashboards are logged as embedded first.


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

```
AnalyticsSessionIdentifier

AnalyticsTimestamp

ClientIp

CpuTime

IsMobile

IsNew

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the dashboard is displayed in mobile (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

**Description**
The field indicates that this action opens a new tab ( `true` ) or goes back to a previously
opened tab ( `false` ).

The default value is `false` .

```
LoginKey

PageContext

PageIdentifier

RecordIdentifier

ReopenCount

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
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CRM Analytics dashboard page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the CRM Analytics object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If `IsNew` is `false`, the number of times that an existing page opens.


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

```
RequestIdentifier

RunTime

SavedViewIdentifier

SessionKey

TabIdentifier

Timestamp

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
The ID of the CRM Analytics dashboard saved view.

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
The ID of the particular Analytics tab in the user interface.

**Type**
dateTime


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Type

Uri

UserIdentifier

ViewMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Apex callout. For example: REST or AJAX.

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
The 15-character Identifier of the user who’s using Salesforce services through the UI or the
API. For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`


### Standard Objects AnalyticsContainerWidgetDef AnalyticsContainerWidgetDef

Represents a Tableau Next dashboard container widget definition. This object is available in API version 67.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsDashboardWidgetId

BackgroundSourceId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the dashboard widget.

This field is a relationship field.

**Relationship Name**
AnalyticsDashboardWidget

**Relationship Type**
Master-detail

**Refers To**
AnalyticsDashboardWidget

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the background source for the container.

This field is a relationship field.

**Relationship Name**
BackgroundSource

**Refers To**
ContentAsset


### Standard Objects AnalyticsDashboard AnalyticsDashboard

Represents a Tableau Next dashboard. This object is available in API version 64.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsWorkspaceId

Description

DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Tableau Next workspace the dashboard is associated with.

This field is a relationship field.

**Relationship Name**
AnalyticsWorkspace

**Refers To**
AnalyticsWorkspace

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the dashboard.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the dashboard.


Standard Objects AnalyticsDashboard

**Field** **Details**

```
Language

LastDraftModifiedDate

LastPublishedDate

MasterLabel

NamespacePrefix

OwnerId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The supported languages for the visualization. There are over 50+ supported language and
dialect values.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date for the dashboard in draft mode.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last published date for the dashboard.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label for the dashboard.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the dashboard.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects AnalyticsDashboard

**Field** **Details**

**Description**
The user ID of the user who created the dashboard.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User

```
Style

TemplateAssetSourceName

TemplateSource

Version

```

**Type**
textarea

**Properties**
Nillable

**Description**
The widget style for the dashboard, represented as a JSON string. For example,

```
  {"widgetStyle":{"backgroundColor":"#ffffff","borderEdges":[],"borderColor":"#cccccc","borderWidth":1,"borderRadius":0}}

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the dashboard was created from a template, this is name of the asset source.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the dashboard was created from a template, this is name of the template.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for the dashboard.


### Standard Objects AnalyticsDashboardWidget AnalyticsDashboardWidget

Represents a Tableau Next dashboard widget. This object is available in API version 67.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsDashboardId

Label

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Tableau Next dashboard the widget is associated with.

This field is a relationship field.

**Relationship Name**
### AnalyticsDashboard

**Relationship Type**
Master-detail

**Refers To**
AnalyticsDashboard (the master object)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the widget.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of widget.


### Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

Possible values are:

**•** `button`

**•** `container`

**•** `extension`

**•** `filter`

**•** `image`

**•** `metric`

**•** `parameter`

**•** `summary`

**•** `text`

**•** `visualization`

```
WidgetName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the widget.

### AnalyticsDownloadEventLog AnalyticsDownloadEventLog represent downloads made from lens and dashboard in the CRM Analytics. This object is available in API

version 61.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

```
AnalyticsTimestamp

AssetIdentifier

AssetType

ClientIp

CpuTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset ID from the user download.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset type from the user download.

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


Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

```
DatasetIdentifiers

DownloadFormat

LoginKey

RecordCount

RequestIdentifier

RunTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A comma-separated list of used dataset IDs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The format of the data for export.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records exported.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique identifier for a given request.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

**Description**
The amount of time that the request took in milliseconds.

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
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:


### Standard Objects AnalyticsInteractEventLog

**Field** **Details**

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

### AnalyticsInteractEventLog

Analytics Interact Event Log represents route or page changes made in the CRM Analytic UI. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

```

**Type**
string


Standard Objects AnalyticsInteractEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

```
AnalyticsTimestamp

ClickCount

ClientIp

CpuTime

LoginKey

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of clicks performed on a page in the CRM Analytics UI.

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

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AnalyticsInteractEventLog

**Field** **Details**

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

```
ReadTime

RecordIdentifier

RequestIdentifier

RunTime

SessionCount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time a user spent on a particular tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the CRM Analytics object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a user returned to a particular page.


Standard Objects AnalyticsInteractEventLog

**Field** **Details**

```
SessionKey

TabIdentifier

Timestamp

TotalTime

Type

Uri

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
The ID of the particular Analytics tab in the UI.

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
The total amount of time (in milliseconds) a tab is open.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The CRM Analytics object type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AnalyticsLicensedAsset

**Field** **Details**

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

```
UserIdentifier

ViewMode

```

Usage

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
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

This event type is captured when a tab is closed. It collates the interaction statistics over the life of the tab, including total open time,
read time, and so on. These statistics are aggregated as you go to other tabs and then return, and logged only when the tab is closed.

### AnalyticsLicensedAsset

Represents a licensed Analytics asset. In this context, Analytics is CRM Analytics, Sonic, or Mulesoft Data Path. Available in API version
52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects AnalyticsPerfEventLog

Fields

**Field** **Details**

```
ConsumerNamespace

LicenseType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consumer namespace for the asset. The possible values are:

**•** `Industries`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The license type for the asset. The possible values are:

**•** `Aqs` (Analytics Query Service)

**•** `Cdp` (Data Cloud)

**•** `DataPipelineQuery` (Data Pipeline Query)

**•** `EinsteinAnalytics` (CRM Analytics)

**•** `MulesoftDataPath` (Mulesoft DataPath)

**•** `Sonic` (Salesforce Data Pipelines)

The default value is `EinsteinAnalytics` .

### AnalyticsPerfEventLog

Analytics Perf Event Log helps track trends in your Analytics performance. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects AnalyticsPerfEventLog

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

AnalyticsTimestamp

ClientIp

CpuTime

EffectivePageTime

IsInitialLoad

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line is generated.

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
The experienced page time in milliseconds.

**Type**
boolean


Standard Objects AnalyticsPerfEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is for the initial load of the Dashboard ( `true` ) or not ( `false` ).

The default value is `false` .

```
LoginKey

QueriedName

RecordIdentifier

RequestIdentifier

RunTime

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
The asset title or query string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the CRM Analytics object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects AnalyticsPerfEventLog

**Field** **Details**

**Description**
The amount of time that the request took in milliseconds.

```
SessionKey

TabIdentifier

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
The ID of the particular Analytics tab in the UI.

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
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .


### Standard Objects AnalyticsVisualization

**Field** **Details**

```
ViewMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

### AnalyticsVisualization

Represents a Tableau Next viusalization. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsWorkspaceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Tableau Next workspace the visualization is associated with.

This field is a relationship field.

**Relationship Name**
AnalyticsWorkspace

**Refers To**
AnalyticsWorkspace


Standard Objects AnalyticsVisualization

**Field** **Details**

```
Description

DeveloperName

Language

LastDraftModifiedDate

LastPublishedDate

MasterLabel

```

**Type**
string

**Properties**
Create, Nillable, Update

**Description**
The description of the visualization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the visualization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The supported languages for the visualization. There are over 50+ supported language and
dialect values.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last modified date for the visualization in draft mode.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last published date for the visualization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects AnalyticsVisualization

**Field** **Details**

**Description**
The label for the visualization.

```
NamespacePrefix

OwnerId

TemplateAssetSourceName

TemplateSource

Version

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the visualization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The user ID of the user who created the visualization.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the visualization was created from a template, this is name of the asset source.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the visualization was created from a template, this is name of the template.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects AnalyticsVizField

**Field** **Details**

**Description**
The API version for the visualization.

### AnalyticsVizField

Represents a Tableau Next viusalization field. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AdHocCalc

DisplayCategory

FieldKey

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An ad-hoc calculation for the visualization field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The display category for the visualization field.

Possible values are:

**•** `Continuous` —continuous

**•** `Discrete` —discrete

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AnalyticsVizField

**Field** **Details**

**Description**
The key for the visualization field.

```
Function

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The function for the visualization field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `CountD`

**•** `DatePartDay`

**•** `DatePartHour`

**•** `DatePartMinute`

**•** `DatePartMonth`

**•** `DatePartQuarter`

**•** `DatePartSecond`

**•** `DatePartWeek`

**•** `DatePartWeekDay`

**•** `DatePartYear`

**•** `DateTruncDay`

**•** `DatePartHour`

**•** `DatePartMinute`

**•** `DateTruncMonth`

**•** `DateTruncQuarter`

**•** `DateTruncWeek`

**•** `DateTruncYear`

**•** `FiscalDatePartMonth`

**•** `FiscalDatePartQuarter`

**•** `FiscalDatePartWeek`

**•** `FiscalDatePartYear`

**•** `FiscalDateTruncMonth`

**•** `FiscalDateTruncQuarter`

**•** `FiscalDateTruncWeek`

**•** `FiscalDateTruncYear`

**•** `Max`


Standard Objects AnalyticsVizField

**Field** **Details**

**•** `Mdy`

**•** `Median`

**•** `Min`

**•** `My`

**•** `Stdev`

**•** `Stdevp`

**•** `Sum`

**•** `UserAgg`

**•** `Var`

**•** `Varp`

```
HierarchyName

Label

PositionName

Positional

Role

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The hierarchy name for the visualization field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label for the visualization field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The position name for the visualization field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The positional text for the visualization field.

**Type**
picklist


Standard Objects AnalyticsVizField

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role for the visualization field.

Possible values are:

**•** `Dimension`

**•** `Measure`

```
SemanticFieldApiName

SemanticObjectApiName

Type

UniqueIndex

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API for the field in the semantic model.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name for object the field belongs to in the semantic model.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type for the visualization field.

Possible values are:

**•** `Field`

**•** `MapPosition`

**•** `MeasureNames`

**•** `MeasureValues`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique index value for the visualization field.


### Standard Objects AnalyticsVizViewDef

**Field** **Details**

This field is a calculated field.

```
VisualizationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the visualization the field belongs to.

This field is a relationship field.

**Relationship Name**
Visualization

**Relationship Type**
Master-detail

**Refers To**
AnalyticsVisualization (the master object)

### AnalyticsVizViewDef

Represents a Tableau Next viusalization view definition. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

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
The API name of the visualization view definition.


Standard Objects AnalyticsVizViewDef

**Field** **Details**

```
IsOriginal

Language

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the view definition is original ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The supported languages for the visualization view definition.

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
Create, Filter, Group, idLookup, Sort, Update


Standard Objects AnalyticsVizViewDef

**Field** **Details**

**Description**
The label for the visualization view definition.

```
NamespacePrefix

OwnerId

Version

VisualizationId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the visualization view definition.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The user ID of the user who created the visualization view definition.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for the visualization view definition.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

This field is a relationship field.

**Relationship Name**
Visualization

**Refers To**
AnalyticsVisualization


### Standard Objects AnalyticsWorkspace AnalyticsWorkspace

Represents a Tableau Next workspace. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

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
Nillable

**Description**
The description for the workspace.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name for the workspace.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The supported languages for the workspace.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)


### Standard Objects AnalyticsWorkspaceAsset

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
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label for the workspace.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the workspace.

### AnalyticsWorkspaceAsset

Represents a Tableau Next asset in a workspace. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.


Standard Objects AnalyticsWorkspaceAsset

Fields

**Field** **Details**

```
ActivePromotionRequestId

AnalyticsWorkspaceId

AssetId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active promotion request for the workspace asset.

This field is a relationship field.

**Relationship Name**
ActivePromotionRequest

**Refers To**
DataAssetPromotionRequest

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Tableau Next workspace the asset is associated with.

This field is a relationship field.

**Relationship Name**
AnalyticsWorkspace

**Relationship Type**
Master-detail

**Refers To**
AnalyticsWorkspace (the master object)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the asset.

This field is a polymorphic relationship field.

**Relationship Name**
Asset

**Refers To**
AnalyticsDashboard, AnalyticsVisualization


Standard Objects AnalyticsWorkspaceAsset

**Field** **Details**

```
AssetType

AssetUsageType

HistoricalPromotionStatus

MetadataSourceType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of asset.

Possible values are:

**•** `AnalyticsDashboard` —Analytics Dashboard

**•** `AnalyticsVisualization` —Analytics Visualization

**•** `MktCalculatedInsightObject` —Calculated Insight Object

**•** `MktDataConnection` —Data Cloud Connection

**•** `MktDataLakeObject` —Data Lake Object

**•** `MktDataModelObject` —Data Model Object

**•** `SemanticModel` —Semantic Model

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of usage for the asset.

Possible values are:

**•** `Created`

**•** `Referenced`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The historical promotion status for the asset.

Possible values are:

**•** `pending`

**•** `promoted`

**•** `unpromoted`

**Type**
picklist


### Standard Objects Announcement

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The source type of the asset metadata.

Possible values are:

**•** `Promoted`

**•** `Reused`

### Announcement

Represents a Chatter group announcement. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ExpirationDate

FeedItemId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

Required. The date on which the announcement expires. Announcements display
on the group UI until 11:59 p.m. local time on the selected date.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

Required. The ID of the FeedItem that contains the content of the announcement.
### Announcements are stored as text posts.

This is a relationship field.

**Relationship Name**
FeedItem


Standard Objects Announcement

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
FeedItem

```
ParentId

SendEmails

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the parent CollaborationGroup that the announcement belongs to. An
announcement can belong only to a single Chatter group.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Set to `true` to email all group members when an announcement is posted to
the group. The default is `false` . This requires the user to have the “Send
announcement on email” permission.

This field is available in API version 36.0 and later.

Note: This field is currently available to select customers through a pilot
program. To be nominated to join this pilot program, contact Salesforce.
Additional terms and conditions may apply to participate in the pilot
program. Please note that pilot programs are subject to change, and as
such, we cannot guarantee acceptance into this pilot program or a
particular time frame in which this feature can be enabled. Any unreleased
services or features referenced in this document, press releases, or public
statements are not currently available and may not be delivered on time
or at all. Customers who purchase our services should make their purchase
decisions based upon features that are currently available.


### Standard Objects ApexCalloutEventLog

Usage

Group owners, managers, and users with the “Modify All Data” permission can use the Announcement object to create, edit, and delete
group announcements. Creating a group announcement is a three-step process.

**1.** Use the FeedItem object to create a text post with the announcement’s content. Use the CollaborationGroup record you want to
post the announcement to as the parent of this feed item.

**2.** Next, use the feed item ID and an expiration date to create the announcement record.

**3.** Finally, update the `AnnouncementId` field in the CollaborationGroup record with the ID of the announcement you created.

To delete the group announcement, simply delete the `AnnouncementId` value in the CollaborationGroup record. To restore a group
announcement, update the `AnnouncementId` field for a group with the announcement’s ID. The expiration date for the announcement
should be in the future and the feed item used to create the announcement should be parented by the same group.

### ApexCalloutEventLog

Apex Callout event logs contain details about callouts (external requests) during Apex code execution. This object is available in API
version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

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


Standard Objects ApexCalloutEventLog

**Field** **Details**

```
ClientIp

CpuTime

IsSuccess

LoginKey

Method

PlannerIdentifier

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the callout request was successful.

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
The HTTP method of the callout. For example: `GET`, `POST`, `PUT`, and so on.

**Type**
string


Standard Objects ApexCalloutEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

```
RequestIdentifier

RequestSize

RequestTime

ResponseSize

RunTime

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
The size of the callout request body, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Not used for this event type. Use the `RequestTime` field instead.


Standard Objects ApexCalloutEventLog

**Field** **Details**

```
SessionKey

StatusCode

Timestamp

Type

Uri

Url

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The returned status code of the request.

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
The type of Apex callout. For example: `REST` or `AJAX` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Nillable, Sort


### Standard Objects ApexClass

**Field** **Details**

**Description**
The callout endpoint URL. For example, `www.salesforce.com` .

```
UserIdentifier

### ApexClass

```

Represents an Apex class.

Supported Calls

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

Body

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex class definition.

Limit: 1 million characters.


Standard Objects ApexClass

**Field** **Details**

```
BodyCrc

IsValid

LengthWithoutComments

Name

NamespacePrefix

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the class was last compiled
( `true` ) or not ( `false` ). The default value is `false` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Length of the class without comments.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Name of the class.

Limit: 255 characters

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


### Standard Objects ApexComponent

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
Status

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex class. The following string values are valid:

**•** `Active` —The class is active.

**•** `Deleted` —The class is marked for deletion. This is useful for managed packages,
because it allows a class to be deleted when a managed package is updated.

**•** `Inactive` —This option is unused and is only supported for ApexTrigger. For more
[information, see the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/)

Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexTrigger

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/)

### ApexComponent

Represents a definition for a custom component that can be used in a Visualforce page alongside standard components such as

`<apex:relatedList>` and `<apex:dataTable>` .

Represents a definition for a custom component that can be used in a Visualforce page alongside standard components such as

`<apex:relatedList>` and `<apex:dataTable>` [. For information, see the Visualforce Developers Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects ApexComponent

Fields

**Field** **Details**

```
ApiVersion

ControllerKey

ControllerType

Description

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this custom component. Every custom component has an API version
specified at creation. If the API version is less than 15.0 and `ApiVersion` is not specified,
`ApiVersion` defaults to 15.0.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier for the controller associated with this custom component:

**•** If the `ControllerType` parameter is set to `Standard` or `StandardSet`, this
value is the name of the sObject that defines the controller.

**•** If the `ControllerType` parameter is set to `Custom`, this value is the name of the
Apex class that defines the controller.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of controller associated with this Visualforce custom component. Possible values
include:

**•** `Not Specified`, for custom components defined without a value for the
`controller` attribute on the `<apex:component>` tag

**•** `Standard`, a value that can't be used with custom components or errors may occur

**•** `StandardSet`, a value that can't be used with custom components or errors may
occur

**•** `Custom`, for components that have a value for the `controller` attribute on the

`<apex:component>` tag

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ApexComponent

**Field** **Details**

**Description**
Description of the Visualforce custom component.

```
Markup

MasterLabel

Name

NamespacePrefix

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The Visualforce markup, HTML, Javascript, and any other Web-enabled code that defines the
content of the custom component.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text used to identify the Visualforce custom component in the Setup area of Salesforce.
The Label for this field is **Label** .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this Visualforce custom component.

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


### Standard Objects ApexEmailNotification

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Usage

Use custom components to encapsulate a common design pattern and then reuse that pattern several times in one or more Visualforce
pages. All users who can view Visualforce pages can view custom components, but the “Customize Application” permission is required
to create or update custom components.

SEE ALSO:

ApexPage

StaticResource

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

### ApexEmailNotification

Stores a Salesforce user ID or external email address to be notified when unhandled Apex exceptions occur. This object is available in
API version 35.0 and later.

Note: Each ApexEmailNotification contains either an email or a user ID, but not both.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Email

UserId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The external email address to which the notification is sent. Mutually exclusive with the
`UserId` field.

**Type**
reference


### Standard Objects ApexExecutionEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user to which the notification is sent. Mutually exclusive with the `Email` field.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Usage

To notify users of your org at the email addresses they have on record, use `UserId` . To notify external users or alternate email addresses,
use `Email` .

### ApexExecutionEventLog

Apex Execution event logs contain details about Apex classes that are used. This object is available in API version 55.0 and later.

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


Standard Objects ApexExecutionEventLog

**Field** **Details**

```
BotSessionIdentifier

CalloutTime

ClientIp

CpuTime

DatabaseTotalTime

EntryPoint

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The bot session ID.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Time spent waiting on webservice callouts, in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

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
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
string


Standard Objects ApexExecutionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entry point for this Apex execution. For example,
`GeneralCloner.cloneAndInsertRecords` or `VF- /apex/CloneUser` .

```
ExecutionTime

IsLongRunningRequest

LoginKey

PlannerIdentifier

Quiddity

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time (in milliseconds).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the request is counted against your org’s concurrent long-running Apex
request limit ( `true` ) or not ( `false` ).

Asynchronous Apex jobs (batch, queueable, scheduled, and future), background processes,
and bulk API requests are not counted against the concurrent long-running limit.

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
The ID of the agent planner.

**Type**
string


Standard Objects ApexExecutionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of outer execution associated with this event. For example:

**•** `A` –ACS Batch Apex

**•** `C` –Scheduled Apex

**•** `E` –Inbound Email Service

**•** `F` –Future

**•** `H` –Apex REST

**•** `I` –Invocable Action

**•** `K` –Quick Action

**•** `L` –Lightning

**•** `M` –Remote Action

**•** `P` –Bulk Apex jobs running in parallel

**•** `Q` –Queueable

**•** `R` –Synchronous uncategorized (which is where all transactions not specified elsewhere
end up)

**•** `S` –QueryLocator Batch Apex (Batch Apex jobs run faster when the start method returns
a QueryLocator object that doesn't include related records via a subquery. See Batch
[Apex Best Practices in Using Batch Apex.)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_best_practices)

**•** `T` –Tests Apex

**•** `V` –Visualforce

**•** `W` –SOAP Webservices

**•** `X` –Execute Anonymous

Implementations of the Process.Plugin interface use the quiddity value `R` .

```
RequestIdentifier

RunTime

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


Standard Objects ApexExecutionEventLog

**Field** **Details**

**Description**
The amount of time the request took, as measured by SFDC code.

```
SessionKey

SoqlQueryCount

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of SOQL queries that were executed during the event.

This value is the aggregate across all namespaces, and can exceed the per-namespace limits.
For test executions, the aggregate total value across all test methods executed in the request
is used. If you are using this value to track limit consumption, consider filtering out test
execution quiddities (indicated by the `Quiddity` field).

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


### Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### ApexExtlCalloutEventLog

Apex Extl Callout EventLog represent external data callouts via custom adapters for Salesforce Connect. This object is available in API
version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
Action

ExecutionTime

FetchTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Action performed by the callout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time in milliseconds.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Description**
Duration (in milliseconds) it takes to retrieve the query results from the external system.

```
IsSuccess

Message

ObjectType

QueryFilter

QueryLimit

QueryOffset

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the query was successful ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Error or warning message associated with the failed call.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of event. The value is always BulkApi2.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field expressions to filter the rows to return. Corresponds to `WHERE` in SOQL queries.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Type**
double


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in SOQL
queries.

```
QueryOrderBy

QuerySelect

RequestIdentifier

RowCount

RowsFetched

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Comma-delineated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of records in the result set.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Description**
Number of rows fetched by the callout.

```
Subqueries

Throughput

Timestamp

TotalTime

UserIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of subqueries this query has been split into.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of records retrieved in one second.

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
How long it takes (in milliseconds) to prepare and execute the query and to retrieve the
query results.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .


### Standard Objects ApexInlineEventLog ApexInlineEventLog

This object is reserved for future use. This object is available in API version 66.0 and later.

### ApexLog

Represents a debug log containing information about a transaction, including information about Apex, Visualforce, and workflow and
validation rules. This object is available in API version 19.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Application

DurationMilliseconds

Location

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
This value depends on the client type that triggered the log.

**•** For API clients, this value is the client ID.

**•** For browser clients, this value is `Browser` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Duration of the transaction in milliseconds.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the location of the origin of the log. Values are:

**•** `Monitoring` —Log is generated as part of debug log monitoring. These types of logs
are maintained for seven days or until a user deletes them.


Standard Objects ApexLog

**Field** **Details**

**•** `SystemLog` —Log is generated from the Developer Console. These types of logs are
maintained for 24 hours or until the user clears them.

```
LogLength

LogUserId

Operation

Request

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Length of the log in bytes.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user whose actions triggered the debug log.

This is a polymorphic relationship field.

**Relationship Name**
LogUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the operation that triggered the debug log, such as `APEXSOAP`, `Apex Sharing`
`Recalculation`, and so on.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Request type. Values are:

**•** `API` —Request came from the API

**•** `Application` —Request came from the Salesforce user interface


### Standard Objects ApexPage

**Field** **Details**

```
RequestIdentifier

StartTime

Status

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the request that triggered the debug log. Use this request identifier
to correlate multiple debug logs triggered by the same request.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Start time of the transaction.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Status of the transaction. This value is either `Success`, or the text of an unhandled Apex
exception.

You can read information about this object, as well as delete it, but you can't update or insert it.

SEE ALSO:

ApexClass

ApexTrigger

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/)

### ApexPage

Represents a single Visualforce page.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects ApexPage

Fields

**Field** **Details**

```
ApiVersion

ControllerKey

ControllerType

Description

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this page. Every page has an API version specified at creation. If the API
version is less than 15.0 and `ApiVersion` is not specified, `ApiVersion` defaults to
15.0.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier for the controller associated with this page:

**•** If the `ControllerType` parameter is set to `Standard` or `StandardSet`, this
value is the name of the sObject that defines the controller.

**•** If the `ControllerType` parameter is set to `Custom`, this value is the name of the
Apex class that defines the controller.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of controller associated with this Visualforce page. Possible values include:

**•** `Not Specified`, for pages defined with neither a `standardController` nor
a `controller` attribute on the `<apex:page>` tag

**•** `Standard`, for pages defined with the `standardController` attribute on the

`<apex:page>` tag

**•** `StandardSet`, for pages defined using the `standardController` and
`recordSetVar` attribute on the `<apex:page>` tag

**•** `Custom`, for pages defined with the `controller` attribute on the `<apex:page>`
tag

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ApexPage

**Field** **Details**

**Description**
Description of the Visualforce page.

```
IsAvailableInTouch

IsConfirmationTokenRequired

Markup

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if Visualforce tabs associated with the Visualforce page can be used in the Salesforce
mobile app ( `true` ) or not ( `false` ). (Use of this field for Salesforce Touch is deprecated.)
This field is available in API version 27.0 and later.

Standard object tabs that are overridden with a Visualforce page aren’t supported in the
Salesforce mobile app, even if you set this field for the page. The default Salesforce app page
for the object is displayed instead of the Visualforce page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether `GET` requests for the page require a CSRF confirmation token ( `true` ) or
not ( `false` ). This field is available in API version 28.0 and later.

If you change this field’s value from `false` to `true`, links to the page require a CSRF token
to be added to them, or the page will be inaccessible.

**Type**
textarea

**Properties**
Create, Update

**Description**
The Visualforce markup, HTML, Javascript, and any other Web-enabled code that defines the
content of the page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text used to identify the Visualforce page in the Setup area of Salesforce. The Label is
**Label** .


### Standard Objects ApexPageInfo

**Field** **Details**

```
Name

NamespacePrefix

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this Visualforce page.

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

Use Visualforce pages to add custom content that extends the base Salesforce application functionality. All users in Visualforce-enabled
organizations can view Visualforce pages, but the “Customize Application” permission is required to create or update them.

SEE ALSO:

ApexComponent

StaticResource

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

### ApexPageInfo

Represents metadata about a single Visualforce page. This object is available in API version 48.0 and later.


Standard Objects ApexPageInfo

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

As of Summer '20 and later, this object can only be accessed by users who can view a particular Visualforce page, and users with the
View Setup and Configuration permission.

Fields

**Field** **Details**

```
ApexPageId

ApiVersion

Description

DurableId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID for the Visualforce page.

**Type**
double

**Properties**
Filter, Sort

**Description**
The API version for the page. Every page has an API version specified at creation. If the API
version is less than `15.0` and `ApiVersion` is not specified, `ApiVersion` defaults to
`15.0` .

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Description of the Visualforce page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.


Standard Objects ApexPageInfo

**Field** **Details**

```
IsAvailableInTouch

IsShowHeader

MasterLabel

Name

NameSpacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if Visualforce tabs associated with the Visualforce page can be used in the Salesforce
app ( `true` ) or not ( `false` ). The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The `showHeader` value for the Visualforce page. This will be “unknown” if the Visualforce
page uses an expression to compute `showHeader` . The default value is `true` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The text used to identify the Visualforce page in the Setup area of Salesforce.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the Visualforce page.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition org that creates
a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a
component in a managed package by using the
`namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, the namespace prefix is set to the namespace prefix of the
org for all objects that support it.


### Standard Objects ApexRestApiEventLog

**Field** **Details**

Note: If an object is in an installed managed package, the object has the
namespace prefix of the installed managed package. This field’s value is the
namespace prefix of the Developer Edition org of the package developer.

**•** In non-Developer Edition orgs, `NamespacePrefix` is only set for objects that are
part of an installed managed package. Objects outside of an installed managed package
do not have a namespace prefix.

Usage

Use `ApexPageInfo` to query limited metadata about Visualforce pages. Some of this metadata corresponds to settings for a Visualforce
page available in Visualforce Pages. To access Visualforce Pages, from _`Setup`_, in the _`Quick Find`_ box, enter _`Custom Code`_ . Then,
select Visualforce Pages. Other values are only available via API. Use `ApexPageInfo` [in Visualforce pages to add custom content that](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_apexpage.htm)
extends the base Salesforce application functionality.

Users can only query `ApexPageInfo` records if they can display the associated Visualforce page, or if they have the View Setup &
Configuration permission. Allow users to view Visualforce pages by modifying their user profile or assigning permission sets.

### ApexRestApiEventLog

Apex REST API event logs capture information about every Apex REST API request. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .


Standard Objects ApexRestApiEventLog

**Field** **Details**

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
Filter, Nillable, Sort

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.


Standard Objects ApexRestApiEventLog

**Field** **Details**

```
FieldCount

LoginKey

MediaType

Method

ObjectName

RequestIdentifier

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of fields or columns, where applicable.

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
The media type of the response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The apex method name.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API objects that are accessed. For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexRestApiEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RequestSize

RequestStatus

ResponseSize

RowsProcessed

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout request body, in bytes.

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


Standard Objects ApexRestApiEventLog

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
The amount of time the request took, as measured by SFDC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP status code for the response.

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


### Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.For
example: `00530000009M943` .

```
UserType

```

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

### ApexSoapApiEventLog

Apex SOAP event logs contain details about custom SOAP web service calls. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ApexSoapApiEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClassName

ClientIp

ClientName

CpuTime

DatabaseTotalTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Apex class name. If the class is part of a managed package, this string includes the
package namespace.

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
The name of the client that’s using Salesforce services. This field is an optional parameter
that can be passed in API calls. If blank, the caller didn't specify a client in the CallOptions
header.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

```
LoginKey

MethodName

QueryString

RateLimitUsage

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
Filter, Group, Nillable, Sort

**Description**
The name of the calling Apex method.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query, if one was performed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The percent of the current usage of your rate limit.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RequestStatus

RunTime

SessionKey

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

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

Requests with a value over five seconds are considered long-running requests for the purposes
of the Concurrent Long-Running Apex Limit.

HTTP callout processing time isn't included when calculating the 5-second limit. We pause
the timer for the callout and resume it when the callout completes.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

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


### Standard Objects ApexTestQueueItem

**Field** **Details**

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

### ApexTestQueueItem

Represents a single Apex class in the Apex job queue. This object is available in API version 23.0 and later.

This object is available in API version 23.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

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


Standard Objects ApexTestQueueItem

**Field Name** **Description**

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

```
ExtendedStatus

ParentJobId

ShouldSkipCodeCoverage

Status

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The pass rate of the test run.

For example: “(4/6)”. This means that four out of a total of six tests passed.

If the class fails to execute, this field contains the cause of the failure.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Points to the AsyncApexJob that represents the entire test run.

If you insert multiple Apex test queue items in a single bulk operation, the queue
items share the same parent job. This means that a test run can consist of the
execution of the tests of several classes if all the test queue items are inserted in
the same bulk operation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to opt out of collecting code coverage information during
Apex test runs. Available in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update


### Standard Objects ApexTestResult

**Field Name** **Description**

**Description**
The status of the job. Valid values are:

**•** `Holding` [1]

**•** `Queued`

**•** `Preparing`

**•** `Processing`

**•** `Aborted`

**•** `Completed`

**•** `Failed`

1 This status applies to batch jobs in the Apex flex queue.

```
TestRunResultId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the associated ApexTestRunResult object.

Insert an `ApexTestQueueItem` object to place its corresponding Apex class in the Apex job queue for execution. The Apex job
executes the test methods in the class.

To abort a class that is in the Apex job queue, perform an update operation on the ApexTestQueueItem object and set its `Status`
field to _`Aborted`_ .

If you insert multiple Apex test queue items in a single bulk operation, the queue items share the same parent job. This means that a
test run can consist of the execution of the tests of several classes if all the test queue items are inserted in the same bulk operation.

### ApexTestResult

Repres ents the result of an Apex test method execution. This object is available in API version 23.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.


Standard Objects ApexTestResult

Fields

**Field Name** **Details**

```
ApexClassId

ApexLogId

ApexTestRunResultId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The Apex class whose test methods were executed.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexLog for this test method execution if debug logging is enabled;
otherwise, `null` .

This is a relationship field.

**Relationship Name**
ApexLog

**Relationship Type**
Lookup

**Refers To**
ApexLog

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the ApexTestRunResult that represents the entire test run.

This is a relationship field.

**Relationship Name**
ApexTestRunResult


Standard Objects ApexTestResult

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
ApexTestRunResult

```
AsyncApexJobId

IsTestSetup

Message

MethodName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the AsyncApexJob that represents the entire test run.

This field points to the same object as
`ApexTestQueueItem.ParentJobId` .

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates if the results are for a test setup method. The default is false.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The exception error message if a test failure occurs; otherwise, `null` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ApexTestResult

**Field Name** **Details**

**Description**

The test method name.

```
Outcome

QueueItemId

RunTime

StackTrace

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The result of the test method execution. Can be one of these values:

**•** Pass

**•** Fail

**•** CompileFail

**•** Skip

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexTestQueueItem, which is the class that this test method is part
of.

This is a relationship field.

**Relationship Name**
QueueItem

**Relationship Type**
Lookup

**Refers To**
ApexTestQueueItem

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test method to run, in milliseconds.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ApexTestResult

**Field Name** **Details**

**Description**

The Apex stack trace if the test failed; otherwise, `null` .

```
TestCategory

TestName

TestNamespace

TestTimestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The category of the test class. This field is available in API version 65.0 and later.

Possible values are:

**•** `Apex` —run Apex tests.

**•** `Flow` —run flow tests.

**•** `IntegrationTest` —run integration tests. This field is available as a
[Developer Preview in API version 67.0 and later. See Apex Integration Tests](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_integration_testing.htm)
[for Agentforce and Data 360 Services (Developer Preview) in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_integration_testing.htm) _Apex_
_Developer Guide_ .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The name of the test class. This field is available in API version 65.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The namespace of the test class.

Apex tests are in the default namespace, so the `TestNamespace` value for
Apex tests is `null` .

[Flow tests are in the FlowTesting namespace. If a flow test is in a namespaced](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_flowtesting.htm)
package or org, the `TestNamespace` value is
`FlowTesting.<NamepacePrefix>` .

This field is available in API version 65.0 and later.

**Type**
dateTime


### Standard Objects ApexTestResultLimits

**Field Name** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**

The start time of the test method.

Usage

### You can query the fields of the ApexTestResult record that corresponds to a test method executed as part of an Apex class

execution.

### Each ApexTestResult record represents a single test method execution. For example, if an Apex test class contains six test methods, six ApexTestResult records are created. These records are in addition to the ApexTestQueueItem record that represents

the Apex class.

Each ApexTestResult record has an associated ApexTestResultLimits on page 609 record, which captures the Apex limits used during
execution of the test method.

### ApexTestResultLimits

Captures the Apex test limits used for a particular test method execution. An instance of this object is associated with each ApexTestResult
record. This object is available in API version 37.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Details**

```
ApexTestResultId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the associated ApexTestResult object.

This is a relationship field.


Standard Objects ApexTestResultLimits

**Field Name** **Details**

**Relationship Name**
ApexTestResult

**Relationship Type**
Lookup

**Refers To**
ApexTestResult

```
AsyncCalls

Callouts

Cpu

Dml

DmlRows

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of asynchronous calls made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of callouts made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The amount of CPU used during the test run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of DML statements made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ApexTestResultLimits

**Field Name** **Details**

**Description**

The number of rows accessed by DML statements during the test run.

```
Email

LimitContext

LimitExceptions

MobilePush

QueryRows

Soql

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of email invocations made during the test run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether the test run was synchronous or asynchronous.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether your org has any limits that differ from the default limits.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of mobile push calls made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of rows queried during the test run.

**Type**
int


### Standard Objects ApexTestRunResult

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of SOQL queries made during the test run.

```
Sosl

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of SOSL queries made during the test run.

The ApexTestResultLimits object is populated for each test method execution, and it captures the limits used between the Test.startTest()
and Test.stopTest() methods. If startTest() and stopTest() aren’t called, limits usage isn’t captured. Note the following:

**•** The associated test method must be run asynchronously.

**•** Limits for asynchronous Apex operations (batch, scheduled, future, and queueable) that are called within test methods aren’t
captured.

**•** Limits are captured only for the default namespace.

### ApexTestRunResult

Contains summary information about all the test methods that were run in a particular Apex job. This object is available in API version
37.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Details**

```
AsyncApexJobId

```

**Type**
reference


Standard Objects ApexTestRunResult

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The parent Apex job ID for the result.

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

```
ClassesCompleted

ClassesEnqueued

EndTime

IsAllTests

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The total number of classes executed during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The total number of classes enqueued during the test run.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The time at which the test run ended.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether all Apex test classes were run.


Standard Objects ApexTestRunResult

**Field Name** **Details**

```
JobName

MethodsCompleted

MethodsEnqueued

MethodsFailed

Source

StartTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Reserved for future use.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods completed during the test run. This value is updated
after each class is run.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods enqueued for the test run. This value is initialized
before the test runs.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods that failed during this test run. This value is updated
after each class is run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The source of the test run, such as the Developer Console.

**Type**
dateTime


Standard Objects ApexTestRunResult

**Field Name** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**

The time at which the test run started.

```
Status

TestSetupTime

TestTime

UserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The status of the test run. Values include:

**•** Queued

**•** Preparing

**•** Processing

**•** Aborted

**•** Completed

**•** Failed

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the setup methods to run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test to run, in milliseconds.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user who ran the test run.

This is a relationship field.


### Standard Objects ApexTestSuite

**Field Name** **Details**

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### ApexTestSuite

Represents a suite of Apex classes to include in a test run. A TestSuiteMembership object associates each class with the suite. This object
is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
TestSuiteName

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Unique, Update

**Description**

The name of the Apex test suite. This label appears in the user interface.

This value is case-sensitive and must be unique.

Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.


### Standard Objects ApexTrigger

The following SOQL query returns the membership object that relates this Apex class to this test suite.

```
   SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'

      AND ApexTestSuiteId = '05FD00000004CDBMA2'

```

SEE ALSO:

TestSuiteMembership

### ApexTrigger

Represents an Apex trigger.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

Body

```

BodyCrc

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this trigger. Every trigger has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex trigger definition.

Limit: 1 million characters.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.


Standard Objects ApexTrigger

**Field** **Details**

```
IsValid

LengthWithoutComments

Name

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the trigger was last compiled
( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Length of the trigger without comments

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the trigger.

Limit: 255 characters

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


Standard Objects ApexTrigger

**Field** **Details**

```
Status

TableEnumOrId

UsageAfterDelete

UsageAfterInsert

UsageAfterUndelete

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex trigger. The following string values are valid:

**•** `Active` —The trigger is active.

**•** `Inactive` —The trigger is inactive, but not deleted.

**•** `Deleted` —The trigger is marked for deletion. This is useful for managed packages,
because it allows a class to be deleted when a managed package is updated.

Note: `Inactive` [is not valid for ApexClass. For more information, see the Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/)
[API Developer Guide .](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/)

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the object associated with the trigger, such as Account or Contact.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after delete` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after insert` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after undelete` trigger ( `true` ) or not ( `false` ).


Standard Objects ApexTrigger

**Field** **Details**

```
UsageAfterUpdate

UsageBeforeDelete

UsageBeforeInsert

UsageBeforeUpdate

UsageIsBulk

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after update` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before delete` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before insert` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before update` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is defined as a bulk trigger ( `true` ) or not ( `false` ).

Note: This field is not used for Apex triggers saved using Salesforce API version 10.0
or higher: all triggers starting with that version are automatically considered bulk, and
this field will always return `true` .


### Standard Objects ApexTriggerEventLog

Usage

Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexClass

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/)

### ApexTriggerEventLog

Apex Trigger event logs contain details about triggers that fire in an organization. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ClientIp

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


Standard Objects ApexTriggerEventLog

**Field** **Details**

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

```
CpuTime

DatabaseTotalTime

ExecutionTime

LoginKey

ObjectName

```

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
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time (in milliseconds).

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

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexTriggerEventLog

**Field** **Details**

**Description**
The name of the object affected by the trigger.

```
PlannerIdentifier

RequestIdentifier

RequestStatus

RunTime

```

**Type**
String

**Description**
The ID of the agent planner.

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
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered long-running requests for the purposes
of the Concurrent Long-Running Apex Limit.


Standard Objects ApexTriggerEventLog

**Field** **Details**

HTTP callout processing time isn't included when calculating the 5-second limit. We pause
the timer for the callout and resume it when the callout completes.

```
SessionKey

Timestamp

TriggerIdentifier

TriggerName

TriggerType

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
The 15-character ID of the trigger that was fired.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
For triggers coming from managed packages, `TriggerName` includes a namespace prefix
separated with a `.` character. If no namespace prefix is present, the trigger is from an
unmanaged trigger. For example:

**•** `examplePackage.managedExampleTrigger` —Managed trigger from the
examplePackage namespace

**•** `unmanagedExampleTrigger` —Unmanaged trigger

**Type**
String


Standard Objects ApexTriggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of this trigger.

Possible values are:

**•** AfterInsert

**•** AfterUpdate

**•** BeforeInsert

**•** BeforeUpdate

```
Uri

UserIdentifier

UserType

```

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

**Type**
String

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


### Standard Objects ApexTypeImplementor

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

### ApexTypeImplementor

Represents Apex classes that directly or indirectly implement an interface. Using a SOQL query, this object gets information about public
or global classes and only global classes for installed managed packages. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApexClassId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the outer class that contains the Apex class implementing the interface.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass


Standard Objects ApexTypeImplementor

**Field** **Details**

```
ClassName

ClassNamespacePrefix

DurableId

InterfaceApexClassId

InterfaceName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Apex class name that implements the interface. For an inner class that implements the
interface, the outer class and inner name separated by a period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that implements the interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the interface and implementor.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The foreign key to the outer class that contains the Apex class defining the interface. Null
for built-in system interfaces, such as `System.Batchable` .

This is a relationship field.

**Relationship Name**
InterfaceApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ApexTypeImplementor

**Field** **Details**

**Description**
The interface name for which Apex class implementation is retrieved. For an inner interface,
the outer Apex class name and the inner interface name separated by a period.

```
InterfaceNamespacePrefix

IsConcrete

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that defines the interface.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the implementing class is abstract ( `false` ) or not ( `true` ).

ApexTypeImplementor considers access modifiers based on the context, such as the namespace from which the ApexTypeImplementor
entity is queried. These are additional usage considerations.

**•** In installed managed packages, you get information about all global implementors in the org, and public implementors from the
managed package itself.

**•** ApexTypeImplementor appropriately filters classes that are annotated with `@Deprecated` . For example it respects the package
version dependency settings of a class when queried from that class.

**•** ApexTypeImplementor returns implementors where `ApexClass.IsValid` is set to `False` (invalid classes) in addition to
when it’s set to `True` . Classes that don’t compile or execute can be returned. An implementor class is only guaranteed to be usable
if `ApexClass.IsValid` is set to `True` for the implementor.

**•** If a package is installed but not yet compiled because Compile on Deploy is disabled, ApexTypeImplementor returns no values until
compilation is complete. In environments like sandboxes where Compile on Deploy can be disabled, you must perform a manual
compilation to get complete results.

**•** To avoid cross-namespace collisions, always specify an InterfaceNamespacePrefix as a WHERE clause in SOQL queries for
ApexTypeImplementor. Otherwise, the query includes all namespaces instead of only the current namespace. If a package contains
an interface with the same name as an interface in a different namespace, a query without a specified InterfaceNamespacePrefix
can return false implementors that can’t be assigned to the interface.

For example, say a managed package contains a global interface named `RoundingStrategy` and a global class named
`HalfDown` that implements `RoundingStrategy` . If a subscriber org has an interface that’s also named `RoundingStrategy`,
then the query `[SELECT ApexClass.Id FROM ApexTypeImplementor WHERE InterfaceName =`
`'RoundingStrategy']`, if performed in the subscriber org, can return the ID of `HalfDown` instead of an implementor in
the subscriber org. To avoid this issue, perform a query that specifies a InterfaceNamespacePrefix: `[SELECT ApexClass.Id`


Standard Objects ApexTypeImplementor

```
    FROM ApexTypeImplementor WHERE InterfaceName = 'RoundingStrategy' AND
```

`InterfaceNamespacePrefix = 'PackageNamespace']` .

Example

This example demonstrates how an interface allows flexibility in a configuration, record, or user-driven selection of the rounding strategy
to apply. The multiple implementations of the interface can be discovered using ApexTypeImplementor and the specific implementation
chosen based on user requirements.

```
   // Common interface that all rounding strategies will implement

   public interface RoundingStrategy {

      Decimal round(Decimal toRound);

   }

   public abstract class RoundingStrategies {

      public class Ceiling implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.round(System.RoundingMode.CEILING);

        }

      }

      public class HalfDown implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.round(System.RoundingMode.HALF_DOWN);

        }

      }

      public class TwoDecimalPlaces implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.setScale(2, System.RoundingMode.HALF_UP);

        }

      }

   }

   List<ApexTypeImplementor> interfaceImpls = [

           SELECT ClassName, ClassNamespacePrefix

           FROM ApexTypeImplementor

           WHERE InterfaceName = 'RoundingStrategy' and IsConcrete = true and

   InterfaceNamespacePrefix = ''

           ORDER BY ClassName ASC NULLS LAST];

   // For example, an admin can be presented with a list of Apex classes

   // that can be applied. Simulated selection of 2 decimal places

   ApexTypeImplementor selectedRoundingStrategy = interfaceImpls[2];

   System.assertEquals('RoundingStrategies.TwoDecimalPlaces',

      selectedRoundingStrategy.ClassName);

   // Create an instance of the class that implements the interface

   RoundingStrategy rs = (RoundingStrategy)

   Type.forName(selectedRoundingStrategy.ClassNamespacePrefix,

      selectedRoundingStrategy.ClassName).newInstance();

```


### Standard Objects ApexUnexpectedExcpEventLog

```
   Decimal rounded = rs.round(7.1459);

   System.assertEquals(7.15, rounded);

### ApexUnexpectedExcpEventLog

```

Apex Unexpected Excp Event Log captures information about unexpected exceptions in Apex code execution. This object is available
in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ExceptionCategory

ExceptionMessage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of the unexpected Apex exception. For example, the LimitException exception
type is split into subcategories that indicate if you exceeded a limit, such as the total heap
size or CPU time. Possible values:

**•** Subcategories of LimitException that indicate the Apex limit you’ve exceeded. Examples:

**•** LimitException: CpuTime: Maximum CPU time on the Salesforce servers.

**•** LimitException: HeapSize: Total heap size

**•** LimitException: Queries: Total number of SOQL queries issued.

**•** LimitException: QueryRows: Total number of records retrieved by SOQL queries.

**•** LimitException: DmlStatements: Total number of DML statements issued.

**•** LimitException: Callouts: Total number of callouts (HTTP requests or web services calls)
in a transaction.

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects ApexUnexpectedExcpEventLog

**Field** **Details**

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

```
ExceptionType

RequestIdentifier

StackTrace

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The class type of the unexpected exception. For example: System.MathException

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

**Properties**
Filter, Nillable, Sort

**Description**
The stack trace for the exception. For example:

```
  Class.OpportunityUtility.insert: line 22, column 1

  AnonymousBlock: line 1, column 1

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.


### Standard Objects ApiTotalUsageEventLog ApiTotalUsageEventLog

API Total Usage Event Log contains details about Platform SOAP API, Platform REST API, and Bulk API requests. This object is available in
API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiFamily

ApiResource

ClientIp

ClientName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API family. For example, REST, SOAP, or Bulk.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API method or resource. For example, `describeSObjects` for SOAP.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
string


Standard Objects ApiTotalUsageEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the client making the API request.

```
ConnectedAppIdentifier

HttpMethod

IsApiLimitCounted

ObjectName

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the connected app making the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method. For example, `GET` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the request counted against the API limit ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AppAnalyticsQueryRequest

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

```
StatusCode

Timestamp

UserIdentifier

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP response status code for the request.

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
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

### AppAnalyticsQueryRequest

Represents a request for AppExchange App Analytics data.

AppExchange App Analytics is available for packages that passed security review and are registered to a License Management App
(LMA). Usage data is provided as package usage logs, as month-based package usage summaries, or as point-in-time subscriber snapshots.
Usage logs, monthly usage summaries, and subscriber snapshots are downloadable comma-separated value (.csv) files. For information
[on how to optimize your use of App Analytics, see AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

[Note: Usage data from Government Cloud and Government Cloud Plus orgs isn’t available in App Analytics.](https://www.salesforce.com/solutions/industries/government1/products/government-cloud/)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects AppAnalyticsQueryRequest

Special Access Rules

[See Get Started with AppExchange App Analytics in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_intro_2gp.htm) _Second-Generation Managed Packaging Developer Guide_ .

Fields

**Field Name** **Details**

```
AvailableSince

DataType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

An optional value used to limit the requested results file to data newly arrived in
the data lake after the specified date and time. This field is always transferred in
the Coordinated Universal Time (UTC) time zone. Use the `AvailableSince`
field as part of your catch-up query strategy.

`AvailableSince` must be later than `StartTime` and `EndTime`, if
specified. `AvailableSince` must be earlier than now. A query must include
`StartTime`, `AvailableSince`, or both.

For example, to schedule a catch-up query on `2021-04-03T18:00:00Z`
for this date range:

**•** `StartTime=2021-03-29T00:00:00Z`

**•** `EndTime=2021-03-30T00:00:00Z`

Valid `AvailableSince` values range from `2021-03-30T00:00:00Z`
`to 2021-04-03T18:00:00Z` .

For more information on `AvailableSince` and catch-up queries, read
[AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The type of usage data being requested. Valid values include:

**•** `PackageUsageLog`

**•** `PackageUsageSummary`

**•** `SubscriberSnapshot`


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

Note: In Summer ’20, we changed the enum names from
`CustomObjectUsageSummary` and `CustomObjectUsageLog`
to `PackageUsageSummary` and `PackageUsageLog` .

If you wrote integrations using `CustomObjectUsageSummary` or
`CustomObjectUsageLog`, they continue to work only with v47 and
earlier. After you upgrade to v48, you must update the `DataType` to
`PackageUsageSummary` and `PackageUsageLog` .

```
DownloadExpirationTime

DownloadSize

DownloadUrl

EndTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The time when the download URL is no longer valid. The expiration time is 60
minutes after the query is completed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the AppExchange App Analytics results file available for download,
in bytes.

**Type**
textarea

**Properties**
Nillable

**Description**

URL that the user can download data from. Populated after the request is
completed. This URL expires and is removed after the expiration time is reached.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter end time in format yyyy-MM-ddTHH:mm:ss.

Example:

2019-04-15T12:00:00


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`

```
ErrorMessage

FileCompression

FileType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Stores error message text that results from this query.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The file compression format of your requested results file. `FileCompression`
and `FileType` must align. If `FileType` is `csv`, `FileCompression`
defaults to `none` and can be `none` or `gzip` . If `FileType` is `parquet`,
`FileCompression` is `snappy` by default and can be `snappy`, `gzip`, or
`none` .

Valid values include:

**•** `gzip`

**•** `snappy`

**•** `none`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The data format of your requested results file. The default is `csv` .
`FileCompression` and `FileType` must align. If `FileType` is `csv`,
`FileCompression` defaults to `none` and can be `none` or `gzip` . If
`FileType` is `parquet`, `FileCompression` is `snappy` by default and
can be `snappy`, `gzip`, or `none` .

Valid values include:


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

**•** `csv`

**•** `parquet`

```
LastReferencedDate

LastViewedDate

Name

OrganizationIds

PackageIds

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
null, it’s possible that this record was referenced (LastReferencedDate) and not
viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The auto-generated name of the App Analytics query request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

Optional. Enter up to 16 comma-separated org IDs without spaces between IDs.
Or enter up to 15 comma-separated org IDs with spaces between the IDs.

To request data for all the orgs the package is installed in, leave the field blank.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

**Description**

Optional. Enter up to 16 comma-separated package IDs without spaces between
IDs. Or enter up to 15 comma-separated package IDs with spaces between the
IDs. Use the subscriber package ID that begins with `033` . To retrieve a list of your
second-generation managed package IDs, run `sf package list`
`--verbose` in Salesforce CLI.

To request data on all packages registered to this License Management App,
leave the field blank.

```
QuerySubmittedTime

RequestState

StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time that the App Analytics query request was received for
processing, in Coordinated Universal Time (UTC). `QuerySubmittedTime`
is read only.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Status of the query request. Valid values are:

**•** `New`

**•** `Pending`

**•** `Complete`

**•** `Expired`

**•** `Failed`

**•** `NoData`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter start time in format yyyy-MM-ddTHH:mm:ss. All App Analytics query requests
must include `StartTime` or `AvailableSince` or both.

Example:

2019-04-14T12:00:00


### Standard Objects AppDefinition

**Field Name** **Details**

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`

Usage

To request usage data, log in to the License Management Org (LMO) that your package is registered to, and initiate the API request from
the LMO. In a 24-hour period, you can download a maximum 20 GB of AppExchange App Analytics data.

[See Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_download_mp_logs.htm) _Second Generation Managed Packaging_
_Developer Guide_ .

If requests to view package usage log or subscriber snapshot data are inactive for 90 days, we reserve the right to stop collecting this
[data. To resume data collection, log a support case in the Salesforce Partner Community. For product, specify](https://partners.salesforce.com) **Partner Programs &**
**Benefits** . For topic, specify **ISV Technology Request** .

### AppDefinition

Represents the metadata of an app and its navigation items. Metadata is returned only for apps that the current user can access. This
object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
Description

DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The optional description of the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AppDefinition

**Field Name** **Details**

**Description**
The developer name of the application.

```
DurableId

HeaderColor

Id

IsLargeFormFactorSupported

IsMediumFormFactorSupported

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique virtual Salesforce ID for the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The header color in the application. Specify the color with a hexadecimal code,
such as #0000FF for blue.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
A default Salesforce ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Large form factor is set in the `CustomApplication`
metadata.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Medium form factor is set in the `CustomApplication`
metadata.


Standard Objects AppDefinition

**Field Name** **Details**

```
IsNavAutoTempTabsDisabled

IsNavPersonalizationDisabled

IsNavTabPersistenceDisabled

IsOmniPinnedViewEnabled

IsOverrideOrgTheme

IsSmallFormFactorSupported

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the navigation automatically creates temporary tabs settings.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether navigation personalization is disabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether workspace tabs are cleared for each new console session.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Omni-Channel component is enabled in sidebar view. The
default is false.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to override the global theme for the org. When true, the color
scheme and logo that the user has set are used. When false, the global theme
for the org is used, even if the user has set a color scheme and logo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AppDefinition

**Field Name** **Details**

**Description**
Indicates whether the Small form factor is set in the `CustomApplication`
metadata.

```
Label

LogoUrl

MasterLabel

NamespacePrefix

NavType

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The localized label value corresponding to the MasterLabel field.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logo URL of the application as selected by the admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The non-translated label entered when the application was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the application.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of navigation for the application. The value `Standard` is for Lightning
Experience. The value `Console` is for Salesforce console. A null value is for
Salesforce Classic.


### Standard Objects AppExtension

**Field Name** **Details**

```
UiType

UtilityBar

### AppExtension

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of custom application. The value `Aloha` is for Salesforce
Classic, and `Lightning` is for Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the utility bar associated with this application.

Represents a connection between the Field Service mobile app and another app, typically for passing record data to the Salesforce
mobile app or other apps. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

### `AppExtensionLabel`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label in the UI for the app extension.


Standard Objects AppExtension

**Field Name** **Details**

```
AppExtensionName

FieldServiceMobileSettingsId

InstallationUrl

LaunchValue

ScopedToObjectTypes

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the app extension.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a set of field service mobile settings.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL that takes the user to the app install location, such as the App Store or
Google Play.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A value directing the Field Service app to the appropriate app extension. The
Launch Value can be a static URL or a dynamic value that you can represent with
certain tokens. These tokens pass field information from the record that the user
is currently viewing. The basic format for these tokens is based on the field names;
for example: **{!$Name}** .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the types of records from which the app extension can be activated.
Scoping an app extension to an object lets users activate the app extension from
records of the specified type. For example, to scope to both work orders and


### Standard Objects ApplicationFormTemplate

**Field Name** **Details**

service appointments you would use the value
`WorkOrder,ServiceAppointment` .

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A picklist of types of app extensions: iOS, Android, Flow, and Lightning Apps

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppExtensionChangeEvent**

Change events are available for the object. Available in API version 55.0 and later.

### ApplicationFormTemplate

Represents the fields to capture application metadata as a template which is used in application tracking and processing. This object is
available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
ApprovalFlowName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ApplicationFormTemplate

**Field** **Details**

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

```
ApplicationType

ApprovalLimitAmount

ApprovalFlowName

ApproverId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of application or template.

Possible values are:

**•** `Contractor`

**•** `EVCharger` —EV Charger

**•** `EnergyEfficiency` —Energy Efficiency

**•** `NewConnection` —New Connection

The default value is `NewConnection` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount up to which the approver has the authority to approve applications.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user who must approve the application payout.

This field is a relationship field.

**Relationship Name**
Approver


### Standard Objects AppMenuItem

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
Description

Name

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the application form template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the application form template.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ApplicationFormTemplateChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ApplicationFormTemplateFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ApplicationFormTemplateHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ApplicationFormTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ApplicationFormTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### AppMenuItem

Represents the organization’s default settings for items in the app menu or App Launcher.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects AppMenuItem

Fields

**Field** **Details**

```
ApplicationId

CanvasAccessMethod

CanvasEnabled

CanvasOptions

CanvasReferenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The access method for the canvas app. Values can be:

**•** `Get` —OAuth Webflow

**•** `Post` —Signed Request

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the app menu item is a canvas app ( `true` ) or not ( `false` ). The default setting
is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the options enabled for a canvas connected app. The options are:

**•** `PersonalEnabled` —The app is enabled as a canvas personal app.

**•** `HideHeader` —The publisher header, which contains the “What are you working on?”
text, is hidden.

**•** `HideShare` —The publisher **Share** button is hidden.

This field is available in API version 34.0 and later.

**Type**
string


Standard Objects AppMenuItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The canvas app unique identifier.

```
CanvasSelectedLocations

CanvasUrl

Description

IconUrl

InfoUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The selected locations for the canvas app which define where the canvas app can appear in
the user interface. For example:

```
  Chatter,ChatterFeed,Publisher,ServiceDesk

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the canvas app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of this menu item.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The icon for the menu item’s application.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for more information about the application.


Standard Objects AppMenuItem

**Field** **Details**

```
IsAccessible

IsRegisteredDeviceOnly

IsUsingAdminAuthorization

IsVisible

Label

LogoUrl

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the current user is authorized to use the app. The default setting is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, indicates that the app is available to registered devices only. The default setting is
`false` . Available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the app is pre-authorized for certain users by the administrator. The default setting
is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**

If `true`, the app is visible to users of the organization. The default setting is `false` .

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


Standard Objects AppMenuItem

**Field** **Details**

**Description**
The logo for the menu item’s application. The default is the initials of the `Label` value.

```
MobileAppBinaryId

MobileAppInstallUrl

MobileAppInstalledDate

MobileAppInstalledVersion

MobileAppVer

MobileDeviceType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the Mobile App Binary file.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to install the app. Available in API version 49.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a user installed a mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the user’s installed mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the mobile app. Available in API version 49.0 and later.

**Type**
string


Standard Objects AppMenuItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The supported device form factors for the mobile app. Available in API version 49.0 and later.

```
MobileMinOsVer

MobilePlatform

MobileStartUrl

Name

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The minimum version required for the app. Available in API version 49.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mobile platform for the app. Possible values include:

**•** `android – Android`

**•** `ios – iOS`

Available in API version 49.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to after they’ve authenticated. This field is used with
connected apps and Experience Builder sites. For sites only, this location is a fully qualified
domain name. For other apps, it’s a relative URL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the item.

**Type**
string


Standard Objects AppMenuItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
SortOrder

StartUrl

Type

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The index value that controls where this item appears in the menu. For example, a menu
item with a sort order of 5 appears between items with sort order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a connected app, the location users are directed to after they’ve authenticated. Otherwise,
the application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of application represented by this item. The types are:

**•** `ConnectedApplication`

**•** `Network`

**•** `ServiceProvider`


### Standard Objects AppointmentAssignmentPolicy

**Field** **Details**

**•** `TabSet`

```
UserSortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that represents where the user set this item in the menu (or App Launcher).
For example, an item with a sort order value of 5 appears between items with sort order
values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both values. For
example, if you want the user-sorted items to appear first, followed by the organization order
for the rest, use:

```
  SELECT ApplicationId,SortOrder,UserSortOrder FROM AppMenuItem

   order by userSortOrder NULLS LAST, sortOrder NULLS LAST

```

Use this read-only object to view an entry in the Lightning Platform app menu or the App Launcher. You can create a SOQL query to
retrieve all items, even items the user does not see from the user interface.

There are many ways you can use AppMenuItem. Here are some examples:

**•** Build your own App Launcher or app menu in Salesforce. Create a custom page showing all the apps you have access to and that
lets you run them using single sign-on.

**•** Build your own App Launcher or app menu on a tablet or mobile app. You can have your own app for launching applications on
various mobile devices.

**•** Build an app launcher into your company’s intranet. There’s no need to have it run on Salesforce because Salesforce APIs let you
integrate with Salesforce programmatically and build an app launcher.

Tip: To get metadata information about apps and their tabs, use the Apex `Schema.describeTabs()` method, REST API
`/vXX.X/tabs/` resource, or SOAP API `describeTabs()` call.

### AppointmentAssignmentPolicy

Stores information about resource assignment rules. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects AppointmentAssignmentPolicy

Fields

**Field** **Details**

```
FullName

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the AppointmentAssignmentPolicy object.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment assignment policy.

Possible values are:

**•** `Possible` values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


Standard Objects AppointmentAssignmentPolicy

**Field** **Details**

```
MasterLabel

PolicyApplicableDuration

PolicyType

UtilizationFactor

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the appointment assignment policy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which the utilization of service resources is calculated. This field is available
in API version 53.0 and later.

Possible values are:

**•** `Parameter-Based`

**•** `Monthly`

**•** `Weekly`

The default value is Parameter-Based.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of appointment assignment policy.

Possible values are:

**•** `loadBalancing`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the count type for the resource utilization. This field is available in API version 53.0
and later.

Possible values are:

**•** `NumberOfAppointments`

**•** `TotalAppointmentDuration`

The default value is TotalAppointmentDuration.


### Standard Objects AppointmentScheduleAggr AppointmentScheduleAggr

Records the utilization of a service resource, by date, for the Load Balancing appointment assignment policy. This object is available in
API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppointmentDate

Name

ResourceUtilizationCount

ServiceResourceId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name or ID of the AppointmentScheduleAggr object.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of appointments scheduled for a service resource. Available in API version 53.0
and later.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling aggregate.


Standard Objects AppointmentScheduleAggr

**Field** **Details**

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
TotalResourceUtilization

UsageType

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of minutes for which the service resource has scheduled appointments.

This is a calculated field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the usage type of the AppointmentScheduleAggr object.

Possible values are:

**•** `FSL_Daily`

**•** `FSL_Monthly`

**•** `FSL_Weekly`

**•** `LightningScheduler`

The default value is 'LightningScheduler'.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleAggrOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentScheduleAggrShare on page 67**
Sharing is available for the object.


### Standard Objects AppointmentScheduleLog AppointmentScheduleLog

Stores service appointments of each service Resource. This object is used to calculate the utilization of a service resource for the
AppointmentScheduleAggr object. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppointmentDate

AppointmentScheduleAggrId

IsUsedForResourceUtilization

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The appointment scheduling aggregate associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
AppointmentScheduleAggr

**Relationship Type**
Lookup

**Refers To**
AppointmentScheduleAggr

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the appointment scheduling log is used for deriving the appointment
scheduling aggregate.

The default value is 'false'.


Standard Objects AppointmentScheduleLog

**Field** **Details**

```
Name

RelatedRecordId

ResourceUtilization

ServiceResourceId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name or ID of the AppointmentScheduleLog object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service appointment, resource absence, event, or any other related record associated
with the appointment scheduling log.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Event, ServiceAppointment

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes the service resource already has scheduled appointments for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup


### Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Refers To**
ServiceResource

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the product associated with the AppointmentScheduleLog object.

Possible values are:

**•** `FSL_Daily` —FSL - Daily

**•** `FSL_Monthly` —FSL - Monthly

**•** `FSL_Weekly` —FSL - Weekly

**•** `LightningScheduler` —Lightning Scheduler

The default value is 'LightningScheduler'.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleLogChangeEvent on page 68**
Change events are available for the object.

**AppointmentScheduleLogFeed on page 55**
Feed tracking is available for the object.

**AppointmentScheduleLogHistory on page 63**
History is available for tracked fields of the object.

**AppointmentScheduleLogOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentScheduleLogShare on page 67**
Sharing is available for the object.

### AppointmentSchedulingPolicy

Represents a set of rules for scheduling appointments using Salesforce Scheduler. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects AppointmentSchedulingPolicy

Fields

**Field** **Details**

```
AppointmentAssignmentPolicyId

AppointmentStartTimeInterval

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name or ID of the appointment assignment policy. This is a relationship field, available
in version 52.0 and later.

**Relationship Name**
AppointmentAssignmentPolicy

**Relationship Type**
Lookup

**Refers To**
AppointmentAssignmentPolicy

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The proposed time interval in minutes between appointment start times. For example, set
the interval to 15. Appointments can then begin at the top of the hour and at 15-minute
intervals thereafter (10:00 AM, 10:15 AM, 10:30 AM, and so on). Possible values are:

**•** `5`

**•** `10`

**•** `15`

**•** `20`

**•** `30`

**•** `45`

**•** `60`

**•** `90`

**•** `120`

**•** `150`

**•** `180`

**•** `240`

**•** `300`

**•** `360`

**•** `420`

**•** `480`


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

```
DeveloperName

ExtCalEventHandlerId

IsOrgDefault

IsSvcTerrOpHoursWithShiftsUsed

IsSvcTerritoryMemberShiftUsed

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the AppointmentSchedulingPolicy object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the custom Apex class that checks service resources’ external calendar
events and returns the time slots where service resources are already booked. Available in
API version 50.0 and later.

This is a relationship field.

**Relationship Name**
ExtCalEventHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this scheduling policy is the default appointment scheduling policy for
Lightning Scheduler appointments in this org.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this scheduling policy considers the intersection of shifts and service
territory operating hours when determining the availability of service resources for
appointments (true). The default value is false. Available in API version 56.0 and later.

**Type**
boolean


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this scheduling policy considers shifts of service territory members when
determining the availability of service resources for appointments (true). The default value
is false. Available in API version 56.0 and later.

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment scheduling policy.

Possible values are:

**•** `Possible` values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

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
The label for the appointment scheduling policy.


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

```
ShouldConsiderCalendarEvents

ShouldEnforceExcludedResource

ShouldEnforceRequiredResource

ShouldMatchSkill

ShouldMatchSkillLevel

ShouldRespectVisitingHours

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this policy checks the Salesforce calendar for resource availability.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents excluded service resources
from being assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills and skill levels to be assigned to appointments.

**Type**
boolean


### Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents users from scheduling
appointments outside of an account’s visiting hours.

```
ShouldUsePrimaryMembers

ShouldUseSecondaryMembers

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only service resources who are
primary members of a service territory to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows service resources who are
secondary members of a service territory to be assigned to appointments.

### AppointmentTopicTimeSlot

Represents a lookup to a work type or a work type group for a time slot This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `AppointmentTopicTimeSlotKey`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Description**
Non-editable validating field used to ensure no two rows have the same time slot and work
type or work type group values in an instance.

```
Name

OperatingHoursId

TimeSlotId

WorkTypeGroupId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name or ID of the AppointmentTopicTimeSlot object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating hours that contain the time slot.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the time slot.

This is a relationship field.

**Relationship Name**
TimeSlot

**Relationship Type**
Lookup

**Refers To**
TimeSlot

**Type**
reference


Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type group associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentTopicTimeSlotChangeEvent on page 68**
Change events are available for the object.

**AppointmentTopicTimeSlotFeed on page 55**
Feed tracking is available for the object.

**AppointmentTopicTimeSlotHistory on page 63**
History is available for tracked fields of the object.

**AppointmentTopicTimeSlotOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentTopicTimeSlotShare on page 67**
Sharing is available for the object.


### Standard Objects Approval Approval

Represents an approval request for a Contract.

Note: This object is read-only and is specific to approvals on the Contract object. It isn't equal to or involved in the approval
processes represented by the ProcessInstance, which is more powerful.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ApproveComment

IsDeleted

OwnerId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Text entered by the user when they approved or rejected this approval request. Required.
Limit: 4,000 characters.

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
Filter, Group, Sort

**Description**
Required. ID of the User being asked to approve or reject the approval request. Must be a
valid User ID. Required.


Standard Objects Approval

**Field** **Details**

```
 ParentId

 RequestComment

 Status

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the Contract associated with this approval request. Must be a valid contract
ID.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Text entered by the User who created the approval request. Optional. This field can't be
updated after the Approval has been created. Limit: 4,000 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. Status of this approval request. One of the following picklist values:

**•** `Pending` —Specified only when the Approval request is created ( `create()` call)

**•** `Approved` —Specified only when the Approval request is approved ( `update()`
call)

**•** `Rejected` —Specified when the Approval request is rejected ( `update()` call) or
when it is created ( `create()` call) and immediately rejected for archival/historical
purposes.

This object allows client applications to programmatically handle approval requests for a Contract. Initially, to request a Contract approval,
a client application might create a new Approval request record, specifying the `ParentId`, OwnerId (user approving or rejecting the
request), Status (Pending), and (optionally) RequestComment fields. Note that when a client application creates the first approval request,
if the value of the Contract `Status` field is Draft, then the Approval `Status` for this record is automatically changed to In Approval
Process (see ContractStatus for more information).

A client application might subsequently update an existing Approval request, specifying the `Status` (Approved or `Rejected` ) and
an `ApproveComment` (required); the `RequestComment` field can't be updated. Updating an Approval record (either to approve
or reject) requires the client application to be logged in with “Approve Contract” permission. To update an Approval request, its `Status`
must be Pending—a client application can't update an Approval that has already been Approved or Rejected. To re-submit an approval
request for a given Contract, a client application must create a new, separate Approval record and repeat the approval process.


### Standard Objects ApprovalAlertContentDef

Once a Contract has been approved (not rejected), the Contract `LastApprovedDate` field is automatically updated, however the
Contract `Status` field isn't updated, it keeps the value InApproval.

An approved Contract must be activated explicitly. Client applications can activate a Contract by setting the value in its `Status` field
to Activated, or a User can activate a Contract via the Salesforce user interface.

A Contract can have multiple approval requests in various states (Pending, Approved, and Rejected). In addition, one User can have
multiple approval requests associated with the same Contract.

Client applications can't explicitly deleteApproval records. Approval records are deleted automatically if the parent Contract is deleted.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ApprovalAlertContentDef

Represents the mapping that links specific user-created email templates to different notification events such as initial assignment or
reassignment within an Advanced Approvals flow. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled.

Fields

**Field** **Details**

```
ApprovalFlowApiName

ApprovalStepApiName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the approval workflow.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique API name of the approval step.


Standard Objects ApprovalAlertContentDef

**Field** **Details**

```
EmailTemplateId

Name

NotificationReason

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email template that's associated with an approval step in the approval workflow.

This field is a relationship field.

**Relationship Name**
EmailTemplate

**Refers To**
EmailTemplate

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the approval alert content definition.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The reason within an approval step's lifecycle that triggers the notification for which an email
is sent. For example, when an approval work item is moved from one user to another, a
reassignment notification email is sent to the user.

Possible values are:

**•** `ApprovalCreationSuccess`

**•** `ApprovalStepAssignment`

**•** `ApprovalStepAssignmentToDelegate`

**•** `ApprovalStepReassignment`

**•** `ApprovalStepReassignmentToDelegate`

**•** `ApprovalSubmissionApprovedOrRejectedStatusUpdate`

**•** `ApprovalWorkItemStatusUpdate`

**•** `AutoApprovalConfirmation`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.


### Standard Objects ApprovalSubmission

**ApprovalAlertContentDefHistory on page 63**
History is available for tracked fields of the object.

### ApprovalSubmission

Represents the instance of an approval request that's submitted for a record of the related object. This object is available in API version
62.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available for users with a Salesforce user license of type Salesforce in Enterprise, Performance, Unlimited, and Developer
Editions.

Fields

**Field** **Details**

```
Comments

DoesSendApprovalEmail

FlowOrchestrationInstanceId

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they submit the request for approval.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether approval request emails are sent to approvers and delegates
( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects ApprovalSubmission

**Field** **Details**

**Description**
The ID of the flow orchestration instance record that's associated with the approval.

This field is a relationship field.

**Relationship Name**
FlowOrchestrationInstance

**Refers To**
FlowOrchestrationInstance

```
IsEligibleForSmartApproval

IsSmartApprovalRun

Name

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the approval submission is eligible for smart approval ( `true` ) or not
( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this approval submission either is run in smart approval mode ( `true` ) or
not ( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval submission record, for example
AS-000000001.

**Type**
reference

**Properties**
Filter, Group, Sort, Update


Standard Objects ApprovalSubmission

**Field** **Details**

**Description**
The ID of the user or the group that owns the approval submission record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
User

```
RelatedRecordId

RelatedRecordObjectName

SmartApprvlBasisSubmissionId

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The API name of the related record that’s submitted for approval.

**Relationship Name**
RelatedRecord

**Refers To**
The objects that you have access to for approvals.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The type of record that was submitted for approval.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The previous approval submission used as reference for the auto-approval evaluation.

This field is a relationship field.

This field is only available with Advanced Approvals enabled.

**Relationship Name**
SmartApprvlBasisSubmission

**Refers To**
ApprovalSubmission

**Type**
picklist


### Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The status of the approval.

Valid values are:

**•** `Approved`

**•** `Canceled`

**•** `Errored`

**•** `InProgress`

**•** `Recalled`

**•** `Rejected`

**•** `Suspended`

```
SubmittedById

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the user who submitted the record for approval.

This field is a relationship field.

**Relationship Name**
SubmittedBy

**Refers To**
User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ApprovalSubmissionShare on page 67**
Sharing is available for the object.

**ApprovalSubmissionHistory on page 63**
History is available for tracked fields of the object.

### ApprovalSubmissionDetail ApprovalSubmissionDetail contains additional information about operations happening during the approval lifecycle. It will not hold

any information that’s already captured in the existing ApprovalSubmission and ApprovalWorkItem entities. This object is available in
API version 62.0 and later.


Standard Objects ApprovalSubmissionDetail

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

```
   update()

```

Special Access Rules

This object is available in Enterprise, Performance, Unlimited, and Developer Editions for users with access to the Approval Submission
object.

Fields

**Field** **Details**

```
ActionChannelName

ActionContext

ActionName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the channel where the action was performed.

Valid values are:

**•** `Agent` : This value is available with ITSM

**•** `ApprovalRecord`

**•** `Email`

**•** `InvocableAction`

**•** `ScreenFlow`

**•** `Slack`

**•** `System`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The context of the action taken for the item assigned for approval. For example, if the approval
has been reassigned the string would be `Reassigned from User Id -`
_**`<original_assignee_id>`**_ .

**Type**
picklist


Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The action taken for the item assigned for approval.

Valid values are:

**•** `Cancel`

**•** `Override`

**•** `Reassign`

**•** `Recall`

**•** `Review`

```
ActionPerformedById

ActionPerformerRole

ApprovalSubmissionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who performed the action on the item submitted for approval.

This field is a relationship field.

**Relationship Name**
ActionPerformedBy

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the user who performed the action on the item submitted for approval.

Valid values are:

**•** `Admin`

**•** `Assignee`

**•** `Delegate`

**•** `Submitter`

**•** `System`

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**Description**
The approval submission that's associated with the detail record.

This field is a relationship field.

**Relationship Name**
ApprovalSubmission

**Relationship Type**
Master-detail

**Refers To**
ApprovalSubmission (the master object)

```
ApprovalWorkItemId

Comments

Name

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The approval assignment associated with the detail record.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItem

**Refers To**
ApprovalWorkItem

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they cancel, review, reassign or recall the request.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval submission detail record, for example
ASD-000000026.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ApprovalWorkItem

**ApprovalSubmissionDetailHistory on page 63**
History is available for tracked fields of the object.

### ApprovalWorkItem

Contains run-time information about each step in an approval workflow, such as assignees and their decisions regarding the object's
approval. Has a master-detail relationship with ApprovalSubmission. This object is available in API version 61.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

```
   update()

```

Special Access Rules

This object is available in Enterprise, Performance, Unlimited, and Developer Editions for users with access to the Approval Submission
object.

Fields

**Field** **Details**

```
ApprovalChainName

ApprovalConditionName

ApprovalSubmissionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the related approval chain. This field is populated when there are multiple
approval chains that are run in parallel. This field is only available with Advanced Approvals
enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the condition that assigns the work item to a user or group for approval.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval submission that's associated with this item.


Standard Objects ApprovalWorkItem

**Field** **Details**

This field is a relationship field.

**Relationship Name**
ApprovalSubmission

**Relationship Type**
Master-detail

**Refers To**
ApprovalSubmission (the master object)

```
AssignedToId

Comments

FlowOrchestrationWorkItemId

IsAutoReviewed

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The user, group, or queue that was assigned the work item.

This field is a polymorphic relationship field.

**Relationship Name**
AssignedTo

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they review or override the work item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the associated flow orchestration work item.

This field is a relationship field.

**Relationship Name**
FlowOrchestrationWorkItem

**Refers To**
FlowOrchestrationWorkItem

**Type**
boolean


Standard Objects ApprovalWorkItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the work item was auto-reviewed ( `true` ) or not ( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

```
IsEligibleForAutoApproval

IsEligibleForSmartApproval

Name

ParentWorkItemId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether custom logic is used for auto-approval of this approval work item (true)
or not (false).

This field is only available with Advanced Approvals enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the approval work item is eligible for smart approval ( `true` ) or not
( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the related record that’s submitted for approval, for
example AWI-000000001.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent approval work item. When multiple group members receive child work
items, this field links each child to its parent.


Standard Objects ApprovalWorkItem

**Field** **Details**

This field is available in API version 67.0 and later.

**Relationship Name**
ParentWorkItem

**Relationship Type**
Lookup

**Refers To**
ApprovalWorkItem

```
RelatedRecordId

RelatedRecordObjectName

ReviewedById

ReviewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of the related record that's submitted for approval.

**Relationship Name**
RelatedRecord

**Refers To**
The objects that you have access to for approvals.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the related record that's submitted for approval.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the user that reviewed the work item.

This field is a relationship field.

**Relationship Name**
ReviewedBy

**Refers To**
User

**Type**
dateTime


Standard Objects ApprovalWorkItem

**Field** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time when the work item was reviewed.

```
SmartApprovalBasisWorkItemId

Status

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The previous approval work item used as a reference for the auto-approval evaluation.

This field is a relationship field.

This field is only available with Advanced Approvals enabled.

**Relationship Name**
SmartApprovalBasisWorkItem

**Refers To**
ApprovalWorkItem

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the approval work item.

Possible values are:

**•** `Approved`

**•** `Assigned`

**•** `Canceled`

**•** `Errored` —Error

**•** `Recalled`

**•** `Rejected`

**•** `Withdrawn`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ApprovalWorkItemHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ApprovalWorkItemCondition ApprovalWorkItemCondition

Represents a condition for starting and concluding an approval step that's evaluated as part of the smart approval process. This object
is available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled with the
Modify All Data or the Approval Admin user permission.

Fields

**Field** **Details**

```
ApprovalWorkItemCriteriaId

ConditionSequencePosition

HasEvaluationSucceeded

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval work item criteria associated with the approval work item condition. The
approval work item criteria defines the logic by which the approval conditions are evaluated.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItemCriteria

**Relationship Type**
Master-detail

**Refers To**
ApprovalWorkItemCriteria (the master object)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order in which the condition is evaluated relative to other conditions that are part of the
requirement logic.

**Type**
boolean


Standard Objects ApprovalWorkItemCondition

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the first value (left side) evaluates against the second value (right side)
successfully ( `true` ) or not ( `false` ).

The default value is `false` .

```
IsConditionExcluded

LeftValue

LeftValueDataType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the condition must be excluded from evaluation ( `true` ) or not ( `false` )
in an auto-approval process.

The default value is `false` .

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The first value of the condition that's evaluated against the second value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the first operand (left side) in this condition.

Possible values are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —Date/Time

**•** `MultiSelectPicklist` —Multi-Select Picklist

**•** `Number`

**•** `Other`

**•** `Picklist`

**•** `Text`


Standard Objects ApprovalWorkItemCondition

**Field** **Details**

**•** `Time`

```
Name

OperatorType

RightValue

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval work item condition record, for example
AWCO-000000071.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The operator for the condition.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqualTo`

**•** `HasError`

**•** `In`

**•** `IsBlank`

**•** `IsChanged`

**•** `IsEmpty`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqualTo`

**•** `None`

**•** `NotEqualTo`

**•** `NotIn`

**•** `StartsWith`

**•** `WasSelected`

**•** `WasSet`

**•** `WasVisited`

**Type**
textarea


### Standard Objects ApprovalWorkItemCriteria

**Field** **Details**

**Properties**
Nillable, Update

**Description**
The second value (right side) of the condition that's evaluated against the first value.

```
RightValueDataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the second operand for the condition.

Possible values are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —Date/Time

**•** `MultiSelectPicklist` —Multi-Select Picklist

**•** `Number`

**•** `Other`

**•** `Picklist`

**•** `Text`

**•** `Time`

### ApprovalWorkItemCriteria

Represents the logic by which a smart approval request is evaluated. This object is available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled with the
Modify All Data or the Approval Admin user permission.


Standard Objects ApprovalWorkItemCriteria

Fields

**Field** **Details**

```
ApprovalStepApiName

ApprovalWorkItemId

CriteriaType

Name

```

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The unique API name of the approval step that uses the logic in the approval work item
criteria.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The parent approval work item associated with the approval work item criteria.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItem

**Relationship Type**
Master-detail

**Refers To**
ApprovalWorkItem (the master object)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the requirement logic is for an entry or exit condition.

Possible values are:

**•** `Entry`

**•** `Exit`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval work item criteria record, for example
AWCR-000000071.


### Standard Objects AppTabMember

**Field** **Details**

```
RequirementLogic

### AppTabMember

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The requirement logic of all entry or exit conditions.

Represents the list of tabs for each of the available apps. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
AppDefinitionId

DurableId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `AppDefinition` object.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.


### Standard Objects ApptBundleAggrDurDnscale

**Field Name** **Details**

```
SortOrder

TabDefinitionId

WorkspaceDriverField

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number used to sort this tab in the application.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `TabDefinition` object.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Refers to the workspace mapping in the `CustomApplication` Metadata
API object.

### ApptBundleAggrDurDnscale

Sums the duration of the bundle members, reduced by a predefined percentage. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ApptBundleAggrDurDnscale

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundleAggregationPolicyId

FromBundleMemberNumber

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent appointment bundle aggregation policy.

This is a relationship field.

