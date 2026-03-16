For example, your filters check whether a case’s Type equals Problem (1), Type equals Feature Request (2), and Escalated equals true
(3). At run time, the filters are combined to `(1 OR 2) AND 3` .

**•** The available filter operators depend on the data type of the selected fields. For details, see Flow Operators in Data Elements and
Record Choice Sets.

Usage

Warning:

**•** Be careful when testing flows that contain delete elements. Even if the flow is inactive, it triggers the delete operation.

**•** To prevent deleting records by mistake, be as specific in your filter criteria as possible.

**•** Records are deleted from your org the moment the flow executes the delete element.

**•** Deleted records are sent to the Recycle Bin and remain there for 15 days before they’re permanently deleted.

**•** Flows can delete records that are pending approval.

Note: At run time, the record isn’t deleted until the interview’s transaction is completed. Transactions are complete when the
interview either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Flow Operators in Data Elements and Record Choice Sets

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Elements

Flow Element: Email Alert

Send an email using an Email Alert action where you specify an email template and a static list of
recipients. You add an Action element to your flow and search for the name of your already
configured Email Alert action.

Note: If you're using Marketing Cloud Growth, use the Send Email Message action instead
of the Email Alert action. Email Alert actions don't work with segments.

Before you begin:

**•** [Create a Lightning email template or Classic email template. Specify the recipient record in any](https://help.salesforce.com/s/articleView?id=sf.email_templates_lightning_parent.htm&language=en_US)
merge fields you use. For example, you could use the contact record or the lead record. When
you build the email Alert, you match the object to the referenced record in the flow. For example,
if the email alert references the Lead object, use a lead record ID when configuring the element
in the flow.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** [In Setup, search for Email Alerts and configure your email alert on page 813. See Email Alert Actions in the Actions Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_email_alert.htm)

**•** Understand the daily limits for emails sent from email alerts.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Determine which record you want to reference in the email and use that record's ID in the element. For example, if you’re sending
the email to the contact that triggered the flow, use the ID of the triggering contact. Or, if you’re using a Get Records element to get
the record that receives the email, use the ID of the record found in the Get Records element. If the email alert has merge fields, the
referenced record is the starting point for those fields.

Add an Action element to your flow. Search for your email alert using the name of the email alert and select the email alert to configure.
To filter the list of email alerts by a specific object, enter the API name of the object. The unique name for each email alert is prefixed
with its object. For example, email alert `emailAlert-Account.Owner_Changed` is associated with the Account object.

Set Input Values

**Field** **Description**

```
Record ID

```

Usage

Select a resource that contains the ID for the record that you want the email to reference. If the email alert
uses merge fields, this record is the starting point for those merge fields.

This field accepts single-value resources of any type. The value is treated as text. The object of the referenced
record must match the object of the email alert.

At run time, the email isn’t sent until the interview’s transaction is completed. Transactions are complete when the interview either
finishes or executes a Screen, Local Action, or Wait element.

Flow Builder displays email alerts from managed packages only if the email alert isn’t protected.

SEE ALSO:

Options for Sending Emails from Flows

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Daily Allocations for Email Alerts

Flow Element: Loop

Start a loop path for iterating over items in a collection variable. For each iteration, the flow
temporarily stores the item in the loop variable. To execute actions on each item’s field values, use
other elements in the loop.

A _collection_ is a list of items, such as field values or email addresses. A loop uses a _loop variable_ to
store the values for the current item in the collection. When the loop finishes examining an item,
it copies the field values for the next item into the loop variable. To reference each collection item
in elements along the loop path, use the loop variable. To keep changes made along the loop path,
add the loop variable as an item in a new collection variable.

**Field** **Description**

`Collection` The collection that you want to loop through. This field accepts any collection
`Variable` variable.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

`Direction` Determines whether the flow starts with the first item or the last item in the collection variable.

`Loop Variable` The variable that the flow uses to contain the current item’s values during a loop iteration.

**•** If `Collection Variable` is set to a non-record collection variable, this field accepts a variable with
the same data type.

**•** If `Collection Variable` is set to a record collection variable, this field accepts a record variable
with the same object type.

Usage

After you add a Loop element and the elements that you want the loop to include, from the Loop element:

**•** Determine which element to execute first when a new item’s values are copied into the loop variable by using the “For each item”
connector.

**•** Determine which element to execute after the loop has processed all the items in the collection by using the “After last item”
connector.

Sample Flow That Loops Through a Collection
Transfer ownership of accounts from one user to another by using record collection variables and loops. The flow already has the
required user IDs.

SEE ALSO:

Move and Connect Elements to Change a Flow Route

Flow Elements

Flow Resource: Variable

Sample Flow That Loops Through a Collection

Transfer ownership of accounts from one user to another by using record collection variables and
loops. The flow already has the required user IDs.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

First, create an Account-based record collection variable called `collReassignedAccts` .

Next, add the Get Records element to get all account records that John Smith owns.


Automate Your Business Processes with Salesforce Flow Flow Reference

Then create a loop that iterates through the collection. For each item in the collection, the loop:

**1.** Assigns the collection item to the loop variable.

**2.** Evaluates whether the account has more than 10,000 employees.

**3.** If the account has more than 10,000 employees, assigns Madison's user ID to the `OwnerId` field in the loop variable.

**4.** If the account doesn't have more than 10,000 employees, assigns Amber's user ID to the `OwnerId` field in the loop variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

**5.** Adds the loop variable's values as a new item in the `collReassignedAccts` collection.

Finally, add an Update Records element to update the accounts in `collReassignedAccts` with the new `OwnerId` after the
loop finishes iterating through the collection.

This section of the flow uses a single query to look up the list of accounts and a single DML statement to update those accounts. If you
updated the records by setting the fields individually, you would use:

**•** One Update Records element to find all accounts that John owns and have more than 10,000 employees (1 query). Then update
those records’ `OwnerId` to Madison’s Id (1 DML statement).

**•** One Update Records element to find all accounts that John owns and don’t have more than 10,000 employees (1 query). Then
update those records’ `OwnerId` to Amber’s Id (1 DML statement).


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Elements: Wait

Resume a flow interview after specific conditions are met, a specified amount of time passes, or
until a specific date.

Note:

**•** Flows that contain Wait elements must be autolaunched. If a flow includes Wait elements
and screens, choice, or choice sets, you can’t activate or run it.

**•** Before you add a Wait element to your flow, understand the special behavior and
limitations. See Paused Flow Interview Considerations on page 267 for details.

Flow Element: Wait for Conditions
Resume a flow interview after specific conditions are met.

Flow Element: Wait for Amount of Time
Resume a flow interview after a specific amount of time.

Flow Element: Wait Until Date
Resume a flow interview after a specific date.

SEE ALSO:

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Elements

Define Conditions in a Flow

Marketing Cloud Growth Campaign Flow Element: Wait Until Event

[Configure the Process Trigger](https://help.salesforce.com/articleView?id=process_start.htm&language=en_US)

Flow Element: Wait for Conditions

Resume a flow interview after specific conditions are met.

Each wait configuration corresponds to a wait connector on the canvas. When a flow pauses, it
waits for one or more resume events. For the first resume event that occurs, the flow resumes and
executes the connector for the associated pause configuration.

Flow Wait Conditions
Each wait configuration that you define in a flow has optional wait conditions. At run time,
these conditions determine whether the flow waits for the associated resume event.

Flow Resume Events
Define the event to wait for if the wait conditions are met. When an event occurs, the flow
resumes and takes the path associated with this wait configuration.

Sample Flows That Wait for Events
Configure a flow to wait for events in one of four ways.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Wait Conditions

Each wait configuration that you define in a flow has optional wait conditions. At run time, these
conditions determine whether the flow waits for the associated resume event.

If the wait conditions aren’t met for a resume event, the interview doesn’t wait for that event. If all
resume events have unmet wait conditions, the interview doesn’t pause. Instead, it executes the
default path.

Example: Use wait conditions when:

**•** The flow waits for different events based on a field value on a given record.

For example, send an email reminder to a contract’s owner before the contract’s end
date. However, the date on which you send the email depends on the rating of the
contract’s account. If the account is hot, send the email a month before the end date. If
the account isn’t hot, send the email two weeks before the end date.

For this example, you create two events. The event for hot accounts occurs 30 days before
the contract’s end date. Its wait conditions check whether the rating for the contract’s
account is equal to “Hot.”

The second event occurs 14 days before the contract’s end date. Its wait conditions check
whether the rating for the contract’s account is not equal to “Hot.” If the account is hot,
the interview doesn’t wait for the second event.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**•** The flow waits for multiple events to occur, such as to send periodic email reminders. For an example of this scenario, see
Sample Flow That Pauses Until Multiple Resume Events Occur on page 352.

SEE ALSO:

Define Conditions in a Flow

Flow Elements: Wait

Flow Resume Events

Define Conditions in a Flow

Flow Elements: Wait

Flow Resume Events

Flow Resume Events

Define the event to wait for if the wait conditions are met. When an event occurs, the flow resumes and takes the path associated with
this wait configuration.

Flow Resume Event: Specific Time
Resume the paused flow when a specific time occurs.

Flow Resume Event: Platform Event Message
Resume the flow interview when it receives a platform event message.

SEE ALSO:

Flow Elements: Wait

Flow Wait Conditions

**Flow Resume Event: Specific Time**
Resume the paused flow when a specific time occurs.

Make sure to familiarize yourself with Paused Flow Interview Considerations.

Define Resume Time: Flow-Based Time

When the time source is a specific time, configure the resume time with these fields.


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: To resume the flow 3 days after the flow paused, use the `$Flow.CurrentDate` global variable as the base time,
set the offset number to 3, and set the offset unit to Days.

Define Resume Time: Record-Based Time

When the time source is a record field, configure the resume time with these fields. The base resume time is a date/time field value on
a record.

Example: You want to resume the flow 3 days before a contract ends. To identify the base resume time, set `Object` to
_`Contract`_, `Field` to _`EndDate`_, and `Record ID` to {!varContractId}. To offset the base resume time, set the offset number
to _`-3`_, and set the offset unit to _`Days`_ .

Store Output Values in Variables

Reference information from the resume event in your flow by storing its outputs in flow variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

Record-Based Time: Supported Objects

You can configure a flow to wait for a record-base time for any custom object or the following standard objects.

**•** Account

**•** AccountContactRelation

**•** AccountRelationship

**•** ActionPlan

**•** ActiveScratchOrg

**•** ActivityMetric

**•** ActivityMetricRollup

**•** Address

**•** AgentWork

**•** AgentWorkSkill

**•** AiImageDetectedObject

**•** AiImageObject

**•** AiImageTrainingObject

**•** Asset

**•** AssetRelationship

**•** AssignedResource

**•** AssistantProgress

**•** BusinessAccount

**•** Campaign

**•** CampaignInfluence

**•** CampaignMember

**•** CareBarrier

**•** CareBarrierDeterminant

**•** CareBarrierType

**•** CareDeterminant

**•** CareDeterminantType

**•** CareDiagnosis

**•** CareInterventionType


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** CarePreauth

**•** CarePreauthItem

**•** CareProgram

**•** CareProgramCampaign

**•** CareProgramEnrollee

**•** CareProgramTeamMember

**•** CareRequest

**•** CareRequestDrug

**•** CareRequestItem

**•** Case

**•** CaseComment

**•** Certification

**•** CertificationDef

**•** CertificationSectionDef

**•** CertificationStep

**•** CertificationStepDef

**•** ChannelProgram

**•** ChannelProgramLevel

**•** ChannelProgramMember

**•** ChatterActivity

**•** Claim

**•** CollaborationGroup

**•** CollaborationGroupMember

**•** ConsumptionRate

**•** ConsumptionSchedule

**•** Contact

**•** ContactEmail

**•** ContactPhone

**•** ContactPointConsent

**•** ContactPointTypeConsent

**•** ContactRequest

**•** ContactWeb

**•** Contract

**•** ContractLineItem

**•** CoverageBenefit

**•** CoverageBenefitItem

**•** CoverageLimit

**•** CoverageType

**•** CustomerAssetAuto

**•** CustomerAssetHome


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** DandBCompany

**•** DataSharingCustomerLocal

**•** DataUsePurpose

**•** DigitalSignature

**•** DuplicateRecordItem

**•** DuplicateRecordSet

**•** EmailMessage

**•** EngagementProgramNode

**•** EngagementProgramVersion

**•** Entitlement

**•** EntitlementContact

**•** EntityMilestone

**•** EnvironmentHubMember

**•** EnvironmentHubMemberRel

**•** Event

**•** ExchangeUserMapping

**•** ExpressionFilter

**•** ExpressionFilterCriteria

**•** ExternalEventMapping

**•** FeedItem

**•** Goal

**•** GoalLink

**•** HealthCareDiagnosis

**•** HealthCareProcedure

**•** Idea

**•** IdentityDocument

**•** IdentityProvEventLog

**•** Image

**•** InStoreLocation

**•** Individual

**•** InsurancePolicy

**•** InsurancePolicyAsset

**•** InsurancePolicyBeneficiary

**•** InsurancePolicyCoverageLimit

**•** InsurancePolicyMember

**•** InsurancePolicyOwner

**•** InsuranceProfile

**•** KeyPerformanceIndicator

**•** Lead

**•** LinkedArticle


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** LiveAgentSession

**•** LiveChatTranscript

**•** LiveChatTranscriptEvent

**•** LiveChatTranscriptSkill

**•** Location

**•** Macro

**•** MacroAction

**•** MacroInstruction

**•** MaintenanceAsset

**•** MaintenancePlan

**•** MemberPlan

**•** MessagingEndUser

**•** MessagingSession

**•** Metric

**•** MobileDeviceCommand

**•** NetworkMember

**•** OperatingHours

**•** Opportunity

**•** OpportunityLineItem

**•** OpportunityScore

**•** OpportunitySplit

**•** OpportunityTeamMember

**•** Order

**•** OrderDeliveryGroup

**•** OrderDeliveryGroupLine

**•** OrderDeliveryMethod

**•** OrderItem

**•** OrderItemSummary

**•** OrderPriceAdjustDistrLine

**•** OrderPriceAdjustmentLine

**•** OrderSummary

**•** OrgDeleteRequest

**•** OrgSnapshot

**•** Organization

**•** PartnerFundAllocation

**•** PartnerFundClaim

**•** PartnerFundRequest

**•** PartnerMarketingBudget

**•** PaymentAuthorizationReversal

**•** PendingServiceRouting


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** PersonAccount

**•** PersonEducation

**•** PersonEmployment

**•** PersonLifeEvent

**•** PlanBenefit

**•** PlanBenefitItem

**•** Producer

**•** Product2

**•** ProductCategoryProduct

**•** ProductConsumed

**•** ProductCoverage

**•** ProductCoverageLimit

**•** ProductItem

**•** ProductItemTransaction

**•** ProductRequest

**•** ProductRequestLineItem

**•** ProductRequired

**•** ProductTransfer

**•** ProfileSkill

**•** ProfileSkillEndorsement

**•** ProfileSkillUser

**•** PurchaserPlan

**•** PurchaserPlanAssn

**•** Question

**•** QuickText

**•** Quote

**•** QuoteLineItem

**•** Reply

**•** RequestsForAccessSIQ

**•** ResourceAbsence

**•** ResourcePreference

**•** RetailLocationGroup

**•** RetailStore

**•** RetailStoreKpi

**•** RetailStoreVisitTemplate

**•** RetailVisitKpi

**•** RetailVisitTemplate

**•** RetailVisitTemplateWorkTask

**•** RetailVisitWorkTask

**•** RetailWorkTask


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** RetailWorkTaskKpi

**•** ReturnOrder

**•** ReturnOrderLineItem

**•** SOSSession

**•** SOSSessionActivity

**•** SalesAgreement

**•** SalesAgreementProduct

**•** SalesAgreementProductSchedule

**•** ScoreIntelligence

**•** ScratchOrgInfo

**•** ServiceAppointment

**•** ServiceAppointmentCapacityUsage

**•** ServiceContract

**•** ServiceCrew

**•** ServiceCrewMember

**•** ServiceReport

**•** ServiceResource

**•** ServiceResourceCapacity

**•** ServiceResourceSkill

**•** ServiceTerritory

**•** ServiceTerritoryLocation

**•** ServiceTerritoryMember

**•** ServiceTerritoryWorkType

**•** SettingUsageMap

**•** Shipment

**•** SignupRequest

**•** Site

**•** SkillRequirement

**•** SocialPersona

**•** SocialPost

**•** Solution

**•** SsoUserMapping

**•** StreamActivityAccess

**•** StreamingChannel

**•** Survey

**•** SurveyInvitation

**•** SurveyPage

**•** SurveyQuestion

**•** SurveyQuestionChoice

**•** SurveyQuestionResponse


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** SurveyQuestionScore

**•** SurveyResponse

**•** SurveySubject

**•** SurveyVersion

**•** Task

**•** TimeSheet

**•** TimeSheetEntry

**•** TimeSlot

**•** Topic

**•** TopicAssignment

**•** UsageEntitlementPeriod

**•** User

**•** UserLicense

**•** UserProvisioningRequest

**•** UserServicePresence

**•** Visit

**•** WebStore

**•** WebStoreNetwork

**•** WebStorePricebook

**•** WorkBadge

**•** WorkBadgeDefinition

**•** WorkCapacityLimit

**•** WorkCapacityUsage

**•** WorkCoaching

**•** WorkFeedback

**•** WorkFeedbackQuestion

**•** WorkFeedbackQuestionSet

**•** WorkFeedbackRequest

**•** WorkFeedbackTemplate

**•** WorkGoal

**•** WorkOrder

**•** WorkOrderLineItem

**•** WorkPerformanceCycle

**•** WorkReward

**•** WorkRewardFund

**•** WorkRewardFundType

**•** WorkThanks

**•** WorkType

**•** WorkTypeGroup

**•** WorkUpgradeAction


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** WorkUpgradeCustomer

**•** WorkUpgradeUser

**•** _`article`_ __kav

SEE ALSO:

Flow Resume Events

**Flow Resume Event: Platform Event Message**
Resume the flow interview when it receives a platform event message.

Make sure to familiarize yourself with Paused Flow Interview Considerations.

Filter Platform Event Messages

If you leave the condition requirements set to **No Conditions**, the flow interview resumes when it receives any platform event message,
regardless of field values. The fields are defined in the platform event definition.

Store Output Values in Variables

When a platform event message resumes a flow, the message provides one output value. The output value includes the values for every
field on the platform event message that resumed the flow. To use values from the message, store Platform Event Message in a record
variable. Make sure that the record variable’s object matches the platform event.

For example, to reference Expected Delivery Date from a Vendor Response platform event, store Platform Event Message in the
`{!vendorResponse}` record variable. Then reference `{!vendorResponse.Expected_Delivery_Date__c}` to get
the specific field value.

Note: To create a record variable to store values from the platform event message, you must have the Customize Application
permission.

SEE ALSO:

[Define and Manage Platform Events](https://help.salesforce.com/s/articleView?id=sf.platform_events.htm&language=en_US)

Flow Resume Events

Sample Flows That Wait for Events

Configure a flow to wait for events in one of four ways.

Sample Flow That Pauses Until a Single Event Occurs
This flow waits for a single event. The base time for the event in this example, which uses a flow-based resume time, is the
`{!$Flow.CurrentDateTime}` global variable.

Sample Flow That Pauses Until Only the First Resume Event Occurs
This flow waits for the first of multiple events to occur before proceeding. The base times for these events are field values, so this
example's resume events use record-based time.

Sample Flow That Pauses Until Multiple Resume Events Occur
This flow waits for many resume events to occur, rather than just the first one. The base times for these events are field values, so
this example's resume events use record-based time.


Automate Your Business Processes with Salesforce Flow Flow Reference

Sample Flow That Pauses Until a Platform Event Message is Received
You’re designing a flow that places a supply order and waits for shipment confirmation from the vendor. Then it assigns an installation
task the day after the supplies are expected to be delivered.

SEE ALSO:

Flow Elements: Wait

**Sample Flow That Pauses Until a Single Event Occurs**

This flow waits for a single event. The base time for the event in this example, which uses a
flow-based resume time, is the `{!$Flow.CurrentDateTime}` global variable.

You’re designing a flow that requests feedback from customers after a contract is activated, but
you want to delay the email by a day.

Example

This flow already contains the following populated variables. The flow activates a contract (1) and
then pauses (2).

**•** `{!customerEmail}` contains the email address for the customer

**•** `{!creatorEmail}` contains the email address for the flow’s creator

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Within the Wait element, a single resume event is defined (1 day after activated). The flow sends the feedback request one day after the
contract is activated, so configure a flow-based resume time. The base time is the `{!$Flow.CurrentDateTime}` global variable
(3), and the offset is one day (4).


Automate Your Business Processes with Salesforce Flow Flow Reference

Because there’s only one wait configuration and you only want the feedback request to be sent one time, don’t set any wait conditions
for this wait configuration. However, just in case something goes wrong, don’t forget to set a fault path. In this example, the fault path
sends an email that contains the fault message to the user who created the flow.

SEE ALSO:

Flow Elements: Wait

Flow Resume Event: Specific Time

**Sample Flow That Pauses Until Only the First Resume Event Occurs**

This flow waits for the first of multiple events to occur before proceeding. The base times for these
events are field values, so this example's resume events use record-based time.

You’re designing a flow that reminds account owners to follow up with their customers a week
before either the account renews or the contract ends. The flow sends a reminder email for whichever
date occurs first.

Example

This flow already contains these populated variables. Before the flow executes the Wait element,
it looks up and stores the contract’s `ID`, its parent account’s `ID` and `OwnerId`, and the account
owner’s `Email` .

**•** `{!accountId}` contains the ID for the account


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**•** `{!contractId}` contains the ID for the contract

**•** `{!accountOwner}` contains the ID for the account’s owner

**•** `{!ownerEmail}` contains the account owner’s email address

The Wait element defines two time-based resume events.

Tip: Every time-based resume event consists of a base time and an offset. For record-based time, the flow needs three pieces of
information to determine the base time: the object, the date/time field, and the specific record. The offset for record-based time
works the same as it does for flow-based time. The flow must know the unit (either _`Days`_ or _`Hours`_ ) and the number of those
units. For both of these events, the base time is offset by -7 days, because weeks isn’t an acceptable offset unit.

The base time for the first event (“Week before account renews”) is the value of `Account.Renewal_Date__c` (1) on the record
whose ID is stored in `{!accountId}` (2). The offset is -7 days (3).


Automate Your Business Processes with Salesforce Flow Flow Reference

The base time for the second event (“Week before contract expires”) is the value of `Contract.EndDate` (4) on the record whose
ID is stored in `{!contractId}` (5). The offset is -7 days (6).

You only want to send one follow-up reminder and the flow always waits for both events, so neither of these events need wait conditions.
However, just in case something goes wrong, set a fault path. In this example, the fault path sends an email that contains the fault
message to the user who created the flow.

SEE ALSO:

Flow Elements: Wait

Flow Resume Event: Specific Time

Flow Wait Conditions


Automate Your Business Processes with Salesforce Flow Flow Reference

**Sample Flow That Pauses Until Multiple Resume Events Occur**

This flow waits for many resume events to occur, rather than just the first one. The base times for
these events are field values, so this example's resume events use record-based time.

You’re designing a flow that reminds contract owners to follow up with their customers before the
contract ends. Rather than sending just one reminder, however, the flow sends them regularly. This
example shows how to use one Wait element to send a reminder two weeks before and then again
one week before the contract ends. You could easily extend this flow to send reminders at more
intervals, such as three days and one day before the contract ends.

Example

This flow already contains these populated variables. Before the flow executes the Wait element,
it looks up and stores the contract’s `EndDate` and `OwnerId` .

**•** `{!contract}` is a record variable that contains the contract’s `EndDate` and `OwnerId`

**•** `{!contractId}` is a text variable that contains the contract’s `Id`

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** `{!oneWeekVisited}` is a Boolean variable whose default value is _`{!$GlobalConstant.False}`_

**•** `{!twoWeeksVisited}` is a Boolean variable whose default value is _`{!$GlobalConstant.False}`_

Because the flow sends the reminder emails both two weeks and a week before the contract’s end date, the Wait element defines two
time-based resume events that use record-based time.

Tip: Every time-based resume event consists of a base time and an offset. For record-based time, the flow needs three pieces of
information to determine the base time: the object, the date/time field, and the specific record. The offset for record-based time
works the same as it does for flow-based time. The flow must know the unit (either _`Days`_ or _`Hours`_ ) and the number of those
units. To wait for a number of days or hours before the record field, set `Offset Number` to a negative integer.

For both of these events, the offset is declared in _`Days`_, because weeks isn’t an acceptable offset unit.


Automate Your Business Processes with Salesforce Flow Flow Reference

The base time for the first event (“2 Weeks”) is the value of `Contract.EndDate` (1) on the record whose ID is stored in
`{!contractId}` (2). The offset is -14 days (3) to represent two weeks.

You want to use the same Wait element for every reminder, so after a flow interview sends one email reminder, it returns to the Wait
element. But first, to ensure that the interview doesn’t send the same email again and again, use _wait conditions_ . When an interview
executes a Wait element, it first checks the conditions for each wait configuration to determine whether to wait for those events. If a
wait configuration has conditions set and those conditions aren’t met, the interview doesn’t wait for the associated resume event.

For the first resume event, the interview checks whether the Boolean variable `{!twoWeekVisited}` is set to false. The variable’s
default value is set to _`{!$GlobalConstant.False}`_, so the flow waits for the event until the variable’s value is changed.

Indicate what the flow does when the “2 Weeks” event occurs by connecting the Wait element to other elements. Then, before you
return the flow path to the Wait element, change the value of `{!twoWeeksVisited}` to _`{!$GlobalConstant.True}`_ . You
can do so with an Assignment element. If the value for `{!twoWeeksVisited}` isn’t false when the Wait element is executed, the
flow doesn’t wait for the “2 Weeks” event to occur. Essentially, the interview checks whether the first resume event has occurred yet,
since the variable is changed to true only in the associated wait configuration’s path. If that resume event has occurred (and the variable
isn’t set to false), the interview knows not to wait for that event.

The second event (“1 Week”) has the same base time as the first event; the offset is -7 days to represent a week.


Automate Your Business Processes with Salesforce Flow Flow Reference

For the second event, the flow checks whether the Boolean variable `{!oneWeekVisited}` is set to false. If it isn’t, the flow doesn’t
wait for this event.

Like with the first wait configuration, use an Assignment element to change the value of `{!oneWeekVisited}` to
_`{!$GlobalConstant.True}`_ before the flow path returns to the Wait element. As long as `{!oneWeekVisited}` isn’t false,
the flow doesn’t wait for the “1 Weeks” event to occur.

Tip: When a flow executes a Wait element and all the wait configurations have conditions that aren’t met, the flow executes the
_default path_ . Because this flow is finished after it sends the final reminder, don’t connect the default path to another element.

Just in case something goes wrong, set a fault path. In this example, the fault path sends an email that contains the fault message to
the user who created the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Sample Flow That Pauses Until a Platform Event Message is Received**

You’re designing a flow that places a supply order and waits for shipment confirmation from the
vendor. Then it assigns an installation task the day after the supplies are expected to be delivered.

The vendor that you buy supplies from has set up a platform event for you to subscribe to. This
platform event, called Vendor Response, includes the order number, order status, and expected
delivery date.

Note: This flow is part of a larger example. It gets launched by a process that starts when a
Printer Status platform event message is received. For details about the process, see Sample
Process: Printer Management.

The Order Printer Supplies flow starts when the Printer Management process launches it. The process
populates the following variables in the flow.

**•** `{!assetId}` —The asset’s ID

**•** `{!assetOwner}` —The asset’s owner

**•** `{!inkManufacturer}` —The manufacturer of the printer’s ink

**•** `{!inkNeeded}` —Whether the printer needs more ink

**•** `{!inkType}` —Specific type of ink that the printer uses

**•** `{!paperNeeded}` —Whether the printer needs more paper

**•** `{!paperSize}` —Paper size that the printer uses

**•** `{!serialNumber}` —The asset’s serial number

EDITIONS

Available in both Salesforce
Classic and Lightning
Experience

Available in: **Performance**,
**Unlimited**, **Enterprise**, and
**Developer** Editions

First, the flow determines whether to order ink or paper. Based on the decision, it submits an order of ink or paper with the vendor by
using an Apex action. Then it pauses until the vendor sends a platform event message that says the order has been shipped. When
Salesforce receives the specified event message, the flow resumes and creates a task for the asset’s owner to install the new supplies.

Decision Element

The decision includes two outcomes: Ink and Paper. The Ink outcome is true if the variable `{!inkNeeded}` is true. The Paper outcome
is true if the variable `{!paperNeeded}` is true.


Automate Your Business Processes with Salesforce Flow Flow Reference

Apex Action Elements

The flow includes two Apex actions that submit a supply order with a vendor but provide different information to it based on whether
the flow executed the Ink outcome or Paper outcome. All the variables used for input values (like `{!serialNumber}` and
`{!paperSize}` ) are set when a process launches the flow.

The first Apex action provides information about which ink to order.

The second Apex action provides information about which paper to order.

In both Apex actions, the action returns an order number. The flow stores that value in the `{!orderNumber}` variable to reference
in the Wait element.


Automate Your Business Processes with Salesforce Flow Flow Reference

Wait Element

After the Apex action submits the supply order, the flow waits for confirmation that the order has been shipped. That confirmation is
received through the Vendor Response platform event.

The flow pauses until Salesforce receives a Vendor Request event message with specific values. The order number must be the same as
the order number that the Apex action provided. And the order status must be Shipped.

When the correct event message is received and the flow resumes, the flow stores the event message’s data in a record variable. That
way, you can reference the expected delivery date to calculate when the supplies are scheduled to be installed.

Create Records Element

When the flow resumes, it creates a task for the asset owner to install the new supplies.


Automate Your Business Processes with Salesforce Flow Flow Reference

For the task’s field values, the flow uses these resources.

**•** `{!installDate}` —A formula that calculates the day after the event’s expected delivery date.

**•** `{!taskDescription}` —A text template that gives more details about the installation.

**•** `{!assetOwner}` —Provided by the process that launches the flow

**•** `{!assetId}` —Provided by the process that launches the flow


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Wait for Amount of Time

Resume a flow interview after a specific amount of time.

**Field** **Description**

`Amount of Time` How long to wait until resuming the flow.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Resume at a specific

time of day

```

Specifies whether to wait to resume a flow until a specific time of day. When enabled, if the specified
amount of time expires after the resume time, the flow doesn’t resume until the resume time on the
following day.

`Resume Time` When to resume the flow.

`Time Zone` The time zone used to resume the flow.

Flow Element: Wait Until Date

Resume a flow interview after a specific date.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

`Resume Date` The date to resume the flow.

`Resume Time` The time to resume the flow.

`Time Zone` The time zone used to resume the flow.

Flow Element: Recommendation Assignment

Generate Einstein Next Best Action recommendations by combining data from records in the
recommendation object, records in other objects, values in collections, and manually entered values.

The Recommendation Assignment element is similar to the Assignment element: both set values
in variables. However, there are important differences:

**•** Use Recommendation Assignment to output a new recommendation collection variable. In
contrast, use Assignment to add or change values in an existing variable.

##### • Recommendation Assignment can’t update values in existing variables. • Recommendation Assignment can set a field’s value across all recommendations in the output

collection. For example, if you set the AcceptanceLabel to _`Accept`_, the AcceptanceLabel for
all records in the output collection is set to Accept.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

##### • Recommendation Assignment can create recommendations from another object’s records. For

example, use leads in the source collection to create recommendations that have the same names as those leads.

##### • Recommendation Assignment is available only in Recommendation Strategy flows.

Set Source Collection

Select a record collection variable with the data that you want to use to create recommendations. Recommendation Assignment creates
one recommendation for every record in the source collection.

If you select a record collection variable that contains recommendations, you can choose the fields that set values in the target collection.
If you select a record collection variable that contains any other object’s records, the element requires certain recommendation fields.

Set Target Collection Values

Assign values to recommendation fields in the output recommendation collection. Values defined in this section are set in every record
in the output collection. If there are values in the source collection variable that aren’t set here, those values are passed to the output
recommendation collection.

To use the source collection records’ values from a specific field, select `currentItemFromSourceCollection` in the Value
column, then select the desired field.


Automate Your Business Processes with Salesforce Flow Flow Reference

Each value is modified by the operator and value combination.

Einstein Next Best Action always requires certain recommendation fields to display a recommendation. However, the Recommendation
Assignment element only requires these fields if you select a source collection that contains non-recommendation records. If you select
a source collection with recommendations, Recommendation Assignment doesn’t require the fields because it’s possible that your
source collection already has values in those fields. However, the fields are still required to display the recommendation.

**•** AcceptanceLabel

**•** ActionReference

**•** Description

**•** Name

**•** RejectionLabel


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

Recommendation Assignment outputs a collection with the assembled recommendation records and doesn’t change the contents of
the source collection. The output collection is null until its corresponding Recommendation Assignment element runs.

Note: A Recommendation Assignment’s output collection is named after its API name. For example, if a Recommendation
Assignment element is named _`CreateRecs`_, its output collection is called _`Recommendations from CreateRecs`_ .

However, recommendations display to users only if they’re in the outputRecommendations variable. To add recommendations to the
outputRecommendations collection, use an Assignment element.

SEE ALSO:

Get Started with Einstein Next Best Action

Create Recommendations

Recommendation Fields

Einstein Next Best Actions Considerations

Flow Element: Screen

Collect information from or display information to a user who runs the flow.

##### Screen Properties

When you don’t have a screen component or record field selected, the properties pane shows the
entire screen.

**•** Configure Frame—Control whether the header and footer are displayed for this screen. These
options are supported only in Lightning runtime. If you hide the footer, use a custom screen
component to let the user navigate between screens.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

**•** Control Navigation—Deselect the navigation options that you want to disable for this screen. and **Developer** Editions
By default, navigation options appear as buttons in the screen footer. The Next action is available
when an element is in the flow after the screen. The Finish action is available when the screen
is the last element in the flow. The Previous action is available when a screen is before this screen. The Pause action is available when
**Let users pause flows** is enabled in your org’s Process Automation settings.

For example, a flow prompts a user to enter information and uses that information to get a Contact record. If no matching contact
is found, the flow displays a screen to tell the user to go back and try again.

Tip:

**–** If you hide the footer but want to let the user navigate between screens, expose the actions with Lightning components.

**–** If a data element precedes the screen element, such as Update Records, or an action, such as Post to Chatter, deselect
**Previous** .

**–** To force the flow user to go back, such as to correct an earlier input, deselect **Next or Finish** .

If the Pause action is enabled:

**–** Use **Pause Confirmation Message** to tell the user where to resume the flow. For the components that list a user’s paused
flows, see Make It Easy for Users to Find Their Paused Flow Interviews.

**–** Customize the flow’s interview label.

**–** In your org’s Process Automation settings, enable **Let users pause flows** .


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Provide Help—Give your users more context for this screen. The text you enter is available in an info bubble in the screen’s header.
If you hide the header but want to expose the help text, use a custom screen component.

Screen Components

The Components tab contains all the standard input components, standard display components, and custom components that are
available for the screen. Click and drag a component to add it to the screen.

Tip: If you have many custom components, enter text in the search field to find the one you need. You can access third-party
custom components on AppExchange using the button at the bottom of the pane.

Record Fields

Build screen flows faster by adding your existing Salesforce record fields directly from the Fields tab. When you add a record field to a
flow screen, the field’s name, data type, help text, requiredness, and existing values are automatically configured for you. To add a record
field, select or create a record variable, then click and drag a field to add it to the screen.

Make Flow Screens Dynamic with Conditional Visibility
You can control when screen components appear with conditional visibility.

Validate User Input on Flow Screens
Validate user input on a flow screen at run time by using a Boolean formula expression, and provide a custom error message to
guide the user.

Adding Record Fields to Flow Screens
Build flow screens faster by adding fields directly from your Salesforce objects. When you add a record field to a flow screen, its name,
data type, help text, requiredness, and, in certain cases, existing values are automatically configured. Record fields use a record
variable to determine which fields can be placed on a flow screen and their configuration.

Flow Screen Actions
Screen actions are used in Screen elements to retrieve or process data by triggering an autolaunched flow. The output from the
autolaunched flow is then made available to all components on that same screen, reducing the number of screens needed in a flow.
Screen actions are triggered by an Action Button (beta) component.

SEE ALSO:

Flow Elements

Build Rich Screens with Custom Screen Components

Move and Connect Elements to Change a Flow Route

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

###### Make Flow Screens Dynamic with Conditional Visibility

You can control when screen components appear with conditional visibility.

**1.** For the screen component, expand the Set Component Visibility section.

**2.** Define the conditions for when the component is visible.

**3.** Define the filter logic if you entered multiple conditions.

SEE ALSO:

Flow Conditional Visibility Considerations

###### Validate User Input on Flow Screens

Validate user input on a flow screen at run time by using a Boolean formula expression, and provide
a custom error message to guide the user.

The formula expression used to validate user input must return a Boolean value ( `true` or `false` ).
If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates
to `false`, the custom error message appears below the component.

Note: If the user leaves a required field blank, the flow shows the default error message, not
your custom error message.

Tip: In regular expressions, use a double backslash to escape any characters that start with
a slash. For example, _`\d`_ becomes _`\\d`_ .

To add input validation to a flow screen component:

**1.** In Flow Builder, on a screen, add a screen input component, and then expand the Validate Input
section.

**2.** Customize the error message that appears if the user enters an invalid value.

To format the error message, use HTML tags.

**3.** Define the values allowed for the component by entering a Boolean formula. In the formula,
reference the correct output for the component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**a.** If the component has one output, reference the component itself. For example, for a Text component labeled Cancellation
Reason, reference `{!Cancellation_Reason}` .

**b.** If the component has multiple outputs, reference the specific output of the component. For example, for an Email component
labeled Contact Email, reference `{!Contact_Email.value}` .

Tip: For a component to reference itself in the Validate Input section, you must click away from the component configuration
pane after you add it to the screen to save its state before you attempt to reference it.

Use these example formulas as a guide.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** This formula validates the format of an email address in a Text component.

```
     REGEX({!Email_Address},"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}")

```

**•** This formula validates the format of a ZIP code in a Text component.

```
     REGEX({!Zipcode},"\\d{5}(-\\d{4})?")

```

**•** This formula validates that a user uploaded at least one file in a File Upload component.

```
     NOT({!fileUpload.contentDocIds} = "[]")

```

**•** This formula validates that a specific account is selected from a list of accounts in a Lookup component

```
     CONTAINS({!myLookup.recordIds},{!getSpecificAccount.Name})

```

Note: Validating record collections or Apex-defined type collections isn’t supported.

Note: At run time, if a user leaves a component blank, the component's value isn't validated for these components: Checkbox,
Checkbox Group, Choice Lookup, Currency, Date, Date & Time, Long Text Area, Multi-Select Picklist, Number, Password, Picklist,
Radio Buttons, Text.

SEE ALSO:

_Salesforce Help_ [: Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

Flow Formula Considerations

###### Adding Record Fields to Flow Screens

Build flow screens faster by adding fields directly from your Salesforce objects. When you add a
record field to a flow screen, its name, data type, help text, requiredness, and, in certain cases,
existing values are automatically configured. Record fields use a record variable to determine which
fields can be placed on a flow screen and their configuration.

Place Record Fields Directly on Flow Screens
To add record fields to a screen flow, follow these steps.

Record Fields on Flow Screens Considerations
Before you add fields from your Salesforce objects directly to your flow screens, consider record
field behaviors.

Place Record Fields Directly on Flow Screens

To add record fields to a screen flow, follow these steps.

**1.** Create or edit a screen element.

EDITIONS

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**2.** On the Fields tab, select a record variable or create a variable with the Record data type and the object that contains the desired
field.

Alternatively, select a record variable automatically created by a Get Records element or a Loop element.

**3.** From the list of fields that appear, drag a field to the screen canvas.

**4.** To use a record field’s existing value, use a Get Records element for the record variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Note: If a field contains a value in the record variable, that value is set on the screen at run time as a default value.

Record Fields on Flow Screens Considerations

Before you add fields from your Salesforce objects directly to your flow screens, consider record field behaviors.

**Account Ticker Field**

Placing the standard Ticker Symbol field on Account records in your screen prevents your flow from saving.

**Creating and Updating Records**

Just like other fields on a screen, record fields don’t save data automatically. To save the record field data, use the associated record
variable in a Create Records or Update Records element.

**Default Values**

Record fields don’t support the default values of their source fields. If a record field’s source field has a default value, the record field is
blank.

If the field contains a value in the record variable, that value is set in the screen at runtime as a default value.

**Event and Task Record Fields**

Some event and task record fields aren’t supported. The supported field types are Date, Date/Time, Checkbox, Number, Text, Text Area,
and Text Area (Long).

At run time, event and task record fields behave differently on a screen than other types of record fields.

**•** Checkbox field labels aren’t shown in line with the checkbox. They’re shown above or below the checkbox.

**•** When edited, the record field doesn’t have a yellow background, and the undo button isn’t shown.

**Lookup**

**•** Creating a record from Lookup isn’t supported in these environments: Flows launched from URLs (such as List Buttons), Flow
Debugger, Lightning Out, Digital Experiences (LWR), and Embedded Service Flows.

**•** Lookup fields aren’t compatible with mobile devices.

**•** To view or change the value of a Master-Detail relationship for existing records, the Allow reparenting setting must be enabled for
that field.

**•** Lookup fields with filters applied don’t immediately display errors from the flow runtime when a user running the flow attempts to
create a record. Errors display only when creating or updating the records that reference the newly created record.

**•** UI API must support the object where the Lookup resides.

**Lookup Filters**

If a lookup filter relies on the field values of the current record in the flow, fields used in the lookup filter must be added on the same
screen. If you must limit the available records in your Lookup based on the actions taken by a user in a flow, use the Choice Lookup
component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Multi-Select Picklists**

Using the Add Item operator in assignments allows for duplicate values in multi-select picklist fields.

**Name Field**

If the value of a Name subfield is changed at runtime, the new value is set, and the subfield shows the new value. But the full Name
record field still shows the original value.

**Permissions**

System context doesn’t apply to record fields. If a user doesn’t have access to a record field, they can’t see it in a flow.

If no ID is set for the record variable, then the running user needs both `Read` and `Create` access to change any record field values.

If an ID is set, the running user needs both `Read` and `Edit` access to change any record field values.

In the record field details, the values in Update Compatible and Create Compatible reflect the properties of the field and your permissions.
The values don’t reflect the permissions of the users running the flow.

Screen flows don’t display record fields that are set to read only at the object level.

**Person Accounts**

If PersonAccount is enabled and Account record fields have been added to a screen:

**•** When the record type is a Person Account, only Person* fields and common fields display.

**•** If the record type is a business Account, only Business account fields and common fields are displayed.

All account record fields are displayed and the record type is ignored.

The `Account.Name` displays as a `PersonName` field if the record type is a Person Account and as a Text field if the record type is
a business account. `Account.Name` displays as a Text field.

**Picklist**

Record fields support dependent picklists only if the dependent field is on the same screen as its controlling field.

If a record field has a record type ID set when entering the screen, its values are filtered by record type. If the record type ID isn’t set, all
values are displayed.

**Referencing Record Fields**

You can’t reference record fields in other areas of your flow, such as formulas, decisions, and conditional visibility. Instead, reference the
record variable that you used to create the record fields.

**Runtime Environments**

Record fields aren’t supported in screen flows on Experience Cloud sites that use Lightning Web Runtime (LWR).

**Supported Field Data Types**

Record fields support these field data types: Address, Checkbox, Date, Date and Time, Email, Lookup, Name, Number, Phone, Picklist,
Text, Text Area, and Text Area (Long).


Automate Your Business Processes with Salesforce Flow Flow Reference

**Other Considerations**

**•** Record fields use the labels returned by the User Interface (UI) API, which can differ from the labels that appear on record pages and
in Object Manager. For record fields of the Name data type, the label appears as Full Name instead of Name for most objects.

**•** Record fields aren’t supported in the Repeater screen component.

**•** Validating user input isn’t supported.

###### Flow Screen Actions

Screen actions are used in Screen elements to retrieve or process data by triggering an autolaunched
flow. The output from the autolaunched flow is then made available to all components on that
same screen, reducing the number of screens needed in a flow. Screen actions are triggered by an
Action Button (beta) component.

To use a screen action, add an Action Button component to a Screen element.

SEE ALSO:

Flow Screen Input Component: Action Button

Flow Element: Start

Connect the Start element to the flow element that you want to execute first at run time. In an
autolaunched flow, you can open the Start element to add a trigger that launches the flow. Without
a trigger, you must set up other things to invoke the autolaunched flow, such as custom buttons,
processes, Apex classes, or Einstein Bots.

Note: In event-triggered flows, you can set the flow to run as the default workflow user. If
the default workflow user gets unset, the flow runs as the automated process user.

SEE ALSO:

Schedule Triggers for Flows That Run for Batches of Records

Record Triggers for Flows That Make Before-Save Updates

Creating Flow Formulas with Flow Formula Builder

Flow Element: Subflow

Launch another active flow that’s available in your org. A flow launched by another flow is called
the _referenced flow_ .

Add a Subflow element to your flow and then, using the label or API name of the flow, search for
a flow to configure. The flow you select is the referenced flow. To open the referenced flow in a
new window, click the action menu. You can’t reference a screen or a template-triggered prompt
flow from an autolaunched flow. A template-triggered prompt flow can only be referenced from
another template-triggered prompt flow. For each flow, the list shows the label and API name of
the active version. If a flow doesn’t have an active version, the list displays the label and API name
of the latest version. You can’t call flows that contain wait elements.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Tip: Create smaller flows that perform common tasks. For example, build utility flows to capture address and credit card information
or to authorize a credit card purchase amount. Then call those flows as needed from multiple product-ordering flows.

Note: Only flow admins can run inactive flows. For other users, the flow fails at run time if a Subflow element calls a flow with no
active version.

Set Input Values

To set the input variables for the referenced flow, use values from earlier in the flow. In the Set Input Values tab, the Subflow elements
displays only input variables from the active version and the latest version of the referenced flow.

The values are assigned at run time when the flow calls the referenced flow. However, for a text, picklist, or multi-select picklist variable
that isn’t a collection, a value of `null` is converted to an empty string. in the referenced flow.

Store Output Values in Flow Types Except Prompt Flows

To use the referenced flow’s outputs later in the flow, store them in variables. The values are assigned when the referenced flow finishes
running. In the Store Output Values tab, the Subflow elements show only output variables from the active version and the latest version
of the referenced flow.

Store Output Values in Prompt Flows

To use the outputs of the referenced flow later in the flow, either reference the output of the Subflow element or store them as manually
assigned variables.

Usage

**•** Flow Builder doesn’t display descriptions for input and output values. For details about each variable in the referenced flow, ask the
admin who built the flow for more information.

**•** In API version 61.0 and later, screen flows and record-triggered flows call the active version of a referenced flow by default. If a
referenced flow has no active version, the flow calls the latest version of the referenced flow. In previous API versions, screen flows
call the latest version of a referenced flow by default. To run only the latest version of each referenced flow, you have two options.

**–** In Flow Builder, click **Debug**, select **Run the latest version of each flow called by subflow elements**, and then click **Run** .
This option isn’t available when you debug a flow in the Flow Builder canvas.

**–** Append the URL for the parent flow with `?latestSub=true` .

**•** In API version 62.0 and later, the prompt flow type supports the Subflow element. The prompt flow can call the active version of a
referenced prompt flow by default. If a referenced prompt flow has no active version, the flow calls the latest version of the referenced
prompt flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

###### Flow Example: Subflow in Prompt Flow

Let’s build a flow that uses a referenced flow to create meeting invites for each marketing event generated by the sales email
template-triggered prompt flow.

SEE ALSO:

Flow Elements

Add and Edit Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Lightning Runtime Considerations

###### Flow Example: Subflow in Prompt Flow

Let’s build a flow that uses a referenced flow to create meeting invites for each marketing event
generated by the sales email template-triggered prompt flow.

Template-triggered prompt flows aren’t compatible with prompt templates created in Winter ’24.

Let’s say you’re a Salesforce admin. You create a flow that sends instructions to the prompt template
to get Marketing events in the same city and state where your contacts live. Now, you can add a
prompt flow as a referenced flow in the parent flow. This new flow creates a meeting invite for your
contacts for each marketing event.

Before creating your parent flow, you create a flow that retrieves a list of marketing events. See
Example of Sales Email Template-Triggered Prompt Flow on page 45.

**1.** Create the flow.

**a.** Click **New Flow** .

**b.** From Flow Builder, select **Start from Scratch**, and then click **Next** .

**c.** Select **Template-Triggered Prompt Flow**, and then click **Create** .

**2.** Configure the flow.

**a.** Select **Automatic Inputs** .

**b.** For Prompt Template Type, select **Sales Email Template** .

Each prompt template type is associated with its prompt template type in Prompt Builder.

**c.** For Recipient, select **Contact** .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions with the
Einstein for Sales, Einstein for
Platform, or Einstein for
Service add-on

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create and manage
prompt templates in Prompt
Builder:

**•** Prompt Template
Manager permission set

Automate Your Business Processes with Salesforce Flow Flow Reference

**3.** Add a Subflow element and configure it.

**a.** Click, and then click the **Subflow** element.

**b.** For Label, enter _`Event Details`_, and use the default API name _`Event_Details`_ .

**c.** For Recipient, select **Prompt Template Input > Contact** .

**d.** For Sender, select **Prompt Template Input > User** .


Automate Your Business Processes with Salesforce Flow Flow Reference

**4.** Add the Add Prompt Instructions element and configure it.

**a.** Click, and then click the **Add Prompt Instructions** element.

**b.** For Label, enter _`Meeting Invite`_, and use the default API name _`Meeting_Invite`_ .

**c.** For Prompt Instructions, enter _`Send a meeting invite to {!$Input.Recipient.Name} with`_
_`{!Event_Details.Prompt}`_ .

**5.** Save your flow.

**a.** For Flow Label, enter _`Send Marketing Events Invite`_, and use the default API name
_`Send_Marketing_Events_Invite`_ .

**b.** Save your work.

**6.** Before activating the flow, click **Debug** to troubleshoot for any flow errors.

**7.** Set the debug options and input variables.

If you want to run the flow as another user, ensure that **Let admins debug flows as other users** is enabled in **Process Automation**
**Settings** .

**8.** Click **Run** .

The debug details for the run appear in a panel on the right.

**9.** To see the results, review the debug details. If the flow fails, troubleshoot the flow errors on page 233.

**10.** Activate the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

Now that you completed the flow, you create a sales email prompt template in Prompt Builder. You add the parent flow to the prompt
template. When you preview the prompt template in Prompt Builder, it triggers the parent flow, which then runs the referenced flow.
The parent flow sends its prompt instructions to the prompt template.

SEE ALSO:

Example of Sales Email Template-Triggered Prompt Flow

_Trailhead_ [: Run a Flow Within a Flow](https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/run-flow-within-flow?trail_id=build-flows-with-flow-builder)

Flow Element: Transform

Select the flow resources for mapping and transforming source data to target data. You can use
the Transform element in screen flows, autolaunched flows with no triggers, and record-triggered
flows.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

To use the Transform element, understand these general limitations.

**•** When you transform a collection, the transformation can’t include joining, sorting, or filtering data. To filter or sort a collection, you
can use the Collection Filter or Collection Sort element in the flow instead.

**•** Viewing the debug details of the source and target data in a rich and interactive format is supported only for autolaunched flows
with no triggers and record-triggered flows.

**•** When the resource for target data is an Apex class from an external service registration, the debug details in Flow Builder show
modified field names.

Note: When an external service is registered, Salesforce creates an Apex class that stores the input and output of the service.

**–** If a field uses a reserved name, `z0` is prepended to the field name, for example, z0type. When the flow calls out to the external
[service, the original field name—in this example, type—is used. See Apex Reserved Keywords.](https://help.salesforce.com/s/articleView?id=sf.external_services_schema_def_apex_reserved_keywords.htm&language=en_US)

**–** Fields that append `_set`, such as name_set, are added automatically to the dynamic Apex class. The fields appear only in the
[flow debug details and when you inspect the dynamic Apex class. See External Service Registrations in Apex.](https://help.salesforce.com/s/articleView?id=sf.external_services_apex_registrations.htm&language=en_US)

**•** Accessing related records via lookup fields on standard, custom, and external objects isn’t supported.

**•** The Checkbox Group, Picklist, and Choice Lookup screen components aren’t supported as a flow resource for the source or target
data.

Understand these rules that preserve the integrity of the data structure in collections.

**•** When mapping a field in a source collection to a field in the target collection, both collections must be at the same hierarchical level
in their respective resources. For example, the collection A in the source data and collection A in the target data aren’t within any
other collections. Because they’re both the top collections in their respective resources, you can map fields between them.

**•** Before you map a field in a collection that’s within another collection, map the field in the parent collection. For example, the flow
resources for the source and target data each contain collection A, which has the same data structure. Collection A contains collection
B. Before you map fields in collection B, map a field in collection A, and then map a field in collection B.

At run time, if a target data field isn’t mapped or is null, it’s removed from the flow resource that’s generated from the Transform element.


Automate Your Business Processes with Salesforce Flow Flow Reference

Limits

**•** The Transform element supports mapping up to one nested collection.

**•** A field on an Apex-defined flow resource can reference up to 10 levels of Apex-defined fields within it. For example, the Name field
on CollectionA is the first level. A field on CollectionB is the second level, and so on.

**•** Debug details show up to 20 records in a collection.

**•** In the Transform element, a formula expression can contain up to 255 characters. Characters that exceed 255 are truncated. To enter
more than 255 characters in a formula expression, you can create a formula resource in the flow. The formula resource can exceed
255 characters in its formula expression. In the Transform element, you can select the formula resource when you use a formula to
transform data.

SEE ALSO:

Transform Data in a Flow

Sum or Count Items in Collections with the Transform Element

Flow Element: Update Records

Identify Salesforce records to update, and set the values to change in those records. To do so, use
the IDs and field values stored in a record variable or record collection variable, or use specify
conditions to identify the records and set the field values individually.

Note: Looking for the Fast Update and Record Update elements from Cloud Flow Designer?
The Update Records element combines the functionality from both elements. For the
equivalent of a Fast Update element, choose to use the IDs and field values from a record
variable or record collection variable. For the equivalent of a Record Update element, choose
to specify conditions to identify the records and set the field values individually.

In the Update Records element, your selection for how to identify the records or related records to
update and set their values determines what to enter in the rest of the element.

Use a record variable or record collection variable

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you’ve populated a record variable or record collection variable with the field values to change, choose to use the IDs and field values
from a record variable or record collection variable, and then select the variable to use. To update the field values in a record variable or
record collection variable, configure an Assignment element earlier in the flow.

Important: For the variable that you select, make sure that each record’s ID value is set. That ID value is how the flow identifies
which records to update.

When you use a record collection variable to update multiple records at once, you reduce the number of DML requests in your flow.
That means you’re more likely to stay within your org’s limits. For more information, see Flow Bulkification in Transactions.


Automate Your Business Processes with Salesforce Flow Flow Reference

Use conditions and set fields individually

Otherwise, choose to use conditions and set fields individually. Choose the object whose records or related records you want to update,
add conditions to filter down the list of records, and set the field values to change for those records. You can update any field on the
record, but the Update Records element doesn’t know which fields are required for this object.

Important: Configure at least one filter condition, or the flow updates all the records for the object.

Example: On an opportunity record, when a user clicks the “Won” button, a flow updates the opportunity’s stage.

Considerations for Defining Filter Criteria

**•** When you define multiple filters, the filter logic usually defaults to AND. However, if multiple filters have the same field selected and
use the equals operator, the filters are combined with OR.

For example, your filters check whether a case’s Type equals Problem (1), Type equals Feature Request (2), and Escalated equals true
(3). At run time, the filters are combined to `(1 OR 2) AND 3` .

**•** The available filter operators depend on the data type of the selected fields. For details, see Flow Operators in Data Elements and
Record Choice Sets.

Usage

Note: At run time, the record isn’t updated until the interview’s transaction is completed. Transactions are complete when the
interview either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Flow Operators in Data Elements and Record Choice Sets

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Elements

Flow Builder Elements for Marketing Cloud

A Flow Builder element represents an action that a flow can execute. Examples include decisions
based on criteria and creating and deleting Salesforce data. Some Flow Builder elements are available
only in Marketing Cloud, such as Send Email Message and Send SMS Message.

In Marketing Cloud, Flow Builder builds flows in auto-layout. In auto-layout, click to display the
types of elements that you can add.

Marketing Cloud Growth Campaign Flow Element: Send Email
The Send Email Message action in a Marketing Cloud Growth campaign flow sends an email
from your Salesforce CMS to an audience segment. You can configure the action to track clicks
and opens, send messages to your opt-in list only, and get help from Einstein for send-time
optimization (STO) and identifying which clicks and opens are real.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Starter**,
**Enterprise**, and **Unlimited**
Editions with Marketing
Cloud **Growth** Edition

Marketing Cloud Growth Campaign Flow Element: Send SMS
The Send SMS Message action in a Marketing Cloud Growth campaign flow sends an SMS message from your Salesforce CMS to an
audience segment. You can configure the action to track clicks and opens, send messages to your opt-in list only, and get help from
Einstein for send-time optimization (STO) and identifying which clicks and opens are real.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Path Experiment
Experiment with up to 10 different versions of a customer journey to determine the most effective path. The Path Experiment element
randomly assigns individuals to paths for an unbiased outcome.

Marketing Cloud Growth Campaign Flow Element: Wait Until Event
Resume a flow interview after an engagement event.

Marketing Cloud Growth Campaign Flow Element: Send Email

The Send Email Message action in a Marketing Cloud Growth campaign flow sends an email from
your Salesforce CMS to an audience segment. You can configure the action to track clicks and opens,
send messages to your opt-in list only, and get help from Einstein for send-time optimization (STO)
and identifying which clicks and opens are real.

Set Input Values

You select the segment from the campaign record or from the flow’s Start element. You can
customize the contents of the email from the campaign record.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Starter**,
**Enterprise**, and **Unlimited**
Editions with Marketing
Cloud **Growth** Edition

```
Email

```

The email content to be sent.

This field is populated with the email template that was created when
you created the campaign. If you remove the email from this field, you
can select a different one from your content workspace in your CMS.

`Einstein Send` Optional. Einstein Send Time Optimization (STO) determines the best
`Time` time to send a message. Using machine learning, Einstein predicts optimal
`Optimization` send times so that a user is more likely to engage with your message. A
Salesforce admin must enable this feature.

```
Einstein

Metrics Guard

Select Sender

```

Optional. Einstein Metrics Guard works behind the scenes to filter out
most email security scanner clicks and opens without blocking legitimate
visitor activity. A Salesforce admin must enable this feature.

The sender for the email message.

Sender addresses are configured in Setup in Organization-Wide Addresses.

`Track Clicks` Optional. If enabled, the flow tracks how many times email recipients
click links that are included in your message.

`Track Opens` Optional. If enabled, the flow tracks whether recipients open your emails.

`Communication` Optional. If you select a communication subscription, the message is sent
`Subscription` only to recipients who opt in to receiving it.

Usage

The email is sent based on the schedule configured in the Start element. If there are multiple Send Email elements separated by Wait
elements, the flow doesn’t send the email until the Wait conditions are met.

The monthly limit of email sends is 15,000.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

Emails sent using the Send Email Message element don't include email signatures from My Email Settings. To include a signature, add
one to the email template.

Marketing Cloud Growth Campaign Flow Element: Send SMS

The Send SMS Message action in a Marketing Cloud Growth campaign flow sends an SMS message
from your Salesforce CMS to an audience segment. You can configure the action to track clicks and
opens, send messages to your opt-in list only, and get help from Einstein for send-time optimization
(STO) and identifying which clicks and opens are real.

Set Input Values

You select the segment from the campaign record or from the flow’s Start element. You customize
the contents of the SMS message from the campaign record.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise** and
**Unlimited** Editions with
Marketing Cloud **Growth**
Edition

```
SMS

Sender ID

```

The SMS message content to be sent.

This field is populated with the SMS content that was created when you
created the campaign. If you remove the SMS message content from this

field, you can select different content from your content workspace in
your CMS.

The sender for the SMS message.

This address is configured in Unified Messaging Setup.

`Track Clicks` Optional. If enabled, the flow tracks how many times message recipients
click links that are included in your message.

`Communication` Optional. If you select a communication subscription, the message is sent
`Subscription` only to recipients who opt in to receiving it.

`Communication` The ID of the communication subscription channel type that points to
`Subscription` the communication subscription.

```
Channel Type

ID

```

Usage

The SMS message is sent based on the schedule configured in the Start element. If there are multiple Send SMS Message elements
separated by Wait elements, the flow doesn’t send the SMS message until the Wait conditions are met.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Path Experiment

Experiment with up to 10 different versions of a customer journey to determine the most effective
path. The Path Experiment element randomly assigns individuals to paths for an unbiased outcome.

Prerequisites

To add the Path Experiment element to a flow, the user requires either the Marketing Cloud Manager
or Marketing Cloud Admin permission set. The Path Experiment element also requires Einstein
Personalization. To set up Einstein Personalization, use Marketing Cloud Assisted Setup. Einstein
Personalization setup is found in Reporting and Optimization, on the Customer Engagement tab.
After setting up Einstein Personalization, return to the Customer Engagement tab. Under the
Configure Basic Personalization section, select a data graph.

###### Path Experiment is available only for segment-triggered flows.

Paths

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise** and
**Unlimited** Editions with
**Marketing Cloud Advanced**
**Edition** .

Create a path for each customer journey you want to test. For each path, specify what percentage of the total audience you want to go
down that path. Individuals are randomly assigned an Experiment cohort and flow path based on the path’s distribution percentage. If
an individual reenters the experiment in any way, for example through a loop or Go To connector, they’re always assigned the same
path as their first assignment.

**Field** **Description**

`Label` Identifies the path on the canvas.

`Path API Name` The requirement for uniqueness applies only to elements within the current flow. Two elements can have the
same API name, provided they're used in different flows.An API name can include underscores and alphanumeric

characters without spaces. It must begin with a letter and can’t end with an underscore. It also can’t have two
consecutive underscores.

`Percentage` The distribution percentage of individuals to send down this path. The total distribution percentage across all
paths must equal 100%.


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: With the Path Experiment element, you can test the effectiveness of two subscription renewal campaigns.

**•** Send 80% of the individuals to Path 1, and send them a renewal email. The flow waits for one day before sending a follow-up
SMS.

**•** Send 20% of the individuals to Path 2, and send them a renewal email that includes testimonials. The flow waits for one week
before sending a follow-up SMS with a discount code.

To see more details about the results of a Send Email action or other type of message engagement, create a Data Cloud report
using one of the Message Engagement DMOs, filtered by the flow element ID.

Example:

SEE ALSO:

_Salesforce Help_ [: Data Cloud Reports and Dashboards](https://help.salesforce.com/s/articleView?id=sf.datacloud_reports_dashboards_overview.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Flow Reference

Marketing Cloud Growth Campaign Flow Element: Wait Until Event

Resume a flow interview after an engagement event.

**Field** **Description**

`Object` The object to monitor for engagements.

`Flow Action to` The flow action to monitor for engagements.

```
Monitor

```

`Content Interaction` The kind of engagement that resumes the flow.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise** and
**Unlimited** Editions with
Marketing Cloud **Growth**
Edition

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

`Amount of Time` The maximum amount of time to wait. If the duration is exceeded, the flow resumes and follows a
timeout path.

SEE ALSO:

Flow Elements: Wait

Provided Flow Core Actions

Perform an action outside of the flow. Choose from Salesforce-provided actions, like Submit for Approval or Send Email, or from your
org’s quick actions and local actions. To add one of these actions to your flow, add an Action element. Then, in the Action field, search
for the appropriate action.

Flow Core Action: Activate Session-Based Permission Set
Activate a session-based permission set for the running user.

Flow Core Action: Deactivate Session-Based Permission Set
Deactivate a session-based permission set for the running user.

Flow Core Action: Einstein Discovery
Get predictive and prescriptive intelligence directly in your flows with Einstein Discovery-powered models. Select the row or fields
to use for your predictions and let Einstein Discovery generate predictions, suggested ways to improve predicted outcomes, and
other details.

Flow Core Action: Get Forecast Context
Get forecast context for a specific user. To be used in the Forecast Guidance Flow as part of the Get Forecast Guidance copilot action.

Flow Core Action: Get Forecast Opportunities
Get forecast opportunities for a user that matches the specified criteria. To be used in the Forecast Guidance flow as part of the Get
Forecast Guidance copilot action.

Flow Core Action: Get Record Prioritization Data
Get record data and field metadata to prioritize records for a user. This action is used in the Get Opportunity Details flow as part of
the Prioritize Opportunities copilot action.

Flow Core Action: Lock Record
Locks or unlocks a workflow-enabled or approval-enabled record for editing during an approval and specifies who can edit the
record while it's locked.

Flow Core Action: Post to Chatter
Post a message to a specified feed, such as a Chatter group or a case record. The message can contain mentions and topics, but only
text posts are supported.

Flow Core Action: Prompt Template Actions
Creates a response based on the large language model (LLM) response for the specified prompt template and inputs.

Flow Core Action: Global or Object-Specific Action
Call an object-specific or global action that’s already been configured in your org. Only Create, Update, and Log a Call actions are
available.

Flow Core Action: Run a Batch Data Transform in Data Cloud
Run a batch data transform.


Automate Your Business Processes with Salesforce Flow Flow Reference

Quip Flow Core Actions
Quip provides several core actions for organizing, creating, and copying your Quip content in flows. To add one of these actions to
your flow, add an Action element. Then select the **Quip** category, and search for the appropriate action.

B2B Commerce Checkout Flow Core Actions
The B2B Commerce Checkout Flow provides several core actions for implementing a successful checkout process within your
Commerce org. To add one of these actions to your flow, add an Action element. Then select the **B2B Commerce** category, and
search for the appropriate action.

Commerce Checkout Flow Core Actions
The Commerce Checkout Flow provides several core actions for implementing a successful checkout process within your Commerce
org. To add one of these actions to your flow, add an Action element. Then select the **Commerce** category, and search for the
appropriate action. Cart actions aren’t available in flows for B2B stores built on an Aura template.

Salesforce Order Management Flow Core Actions
Salesforce Order Management provides several core actions for implementing order management functionality in flows. To add one
of these actions to your flow, add an Action element. Then select the **Order Management** category, and search for the appropriate
action.

Salesforce Omnichannel Inventory Flow Core Actions
Salesforce Omnichannel Inventory provides several core actions for implementing inventory functionality in flows. To add one of
these actions to your flow, add an Action element. Then select the **Omnichannel Inventory Service** category, and search for the
appropriate action.

Flow Core Actions: Send Conversation Messages
Send a messaging component to one or more messaging users in enhanced WhatsApp, enhanced Apple Messages for Business,
enhanced SMS, or Messaging for In-App.

Flow Core Action: Send Custom Notification
Add the Send Custom Notification action to a flow, then add recipients and content.

Flow Core Action: Send Email
Send and optionally log an email by specifying the email content and recipients in a flow. If you’re using Marketing Cloud Growth,
use the Send Email Message on page 377 element to send an email to your audience segment.

Flow Core Action: Send Notification Actions
Call a notification type to send. Each Send Notification action corresponds to a supported notification type. Send Notification actions
are available only for Slack-enabled custom notification types and certain Slack-enabled standard notification types.

Flow Core Action: Send Surveys
Create an action to send an active survey by specifying the name, subject, recipients, and invitation link options in the flow.

Flow Core Action: Perform Survey Sentiment Analysis
Get insights into the sentiments that underlie survey responses.

Flow Core Action: Get Assessment Response Summary
Create a printable summary view of assessments taken. This action enables you to extract responses saved in an assessment and
create a flow to generate a document.

Slack Flow Core Actions
Manage Slack channels, channel members, and messages from flows. As your Salesforce records change, a flow can trigger changes
in Slack.

Flow Core Action: Submit for Approval
Submit one Salesforce record for approval.


Automate Your Business Processes with Salesforce Flow Flow Reference

Salesforce Anywhere Core Flow Actions (Beta)
Salesforce Anywhere provides several core actions for implementing Salesforce Anywhere functionality in flows. To add one of these
actions to your flow, add an Action element. Then select the Salesforce Anywhere category, and search for the appropriate action.

SEE ALSO:

Add and Edit Elements

Flow Core Action: Activate Session-Based Permission Set

Activate a session-based permission set for the running user.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Permission Set`_,
##### and select Activate Session-Based Permission Set .

Set Input Values

Use values from earlier in the flow to identify the permission set to activate.

Important: You can run queries, but don’t modify Salesforce data in flows that also activate
session-based permission sets.

**Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Permission Set

Name

Permission Set

Namespace

```

The developer name of the permission set.

This parameter accepts single-value resources of any type. That value is
treated as text.

Optional. The permission set’s namespace.

This parameter accepts single-value resources of any type. That value is
treated as text.

Example: A junior buyer in your org occasionally requires access to your Contracts object. Create a session-based permission set
with access to the object. Then create a flow that uses the Activate Session-Based Permission Set core action. Configure the action
to activate the permission set.

The junior buyer runs the flow to access contracts during the current user session. The action activates the permission set for the
junior buyer during the current session.

SEE ALSO:

Flow Core Action: Deactivate Session-Based Permission Set

[Create a Flow That Can Activate or Deactivate a Session-Based Permission Set](https://help.salesforce.com/s/articleView?id=sf.perm_sets_session_activate_flow.htm&language=en_US)

Plan for Success in Flow Builder

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Deactivate Session-Based Permission Set

Deactivate a session-based permission set for the running user.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Permission Set`_,
##### and select Deactivate Session-Based Permission Set .

Set Input Values

Use values from earlier in the flow to identify the permission set to deactivate.

**Field** **Description**

```
Permission Set

Name

Permission Set

Namespace

```

SEE ALSO:

The developer name of the permission set.

This parameter accepts single-value resources of any type. That value is
treated as text.

The permission set’s namespace.

This parameter accepts single-value resources of any type. That value is
treated as text.

Flow Core Action: Activate Session-Based Permission Set

[Create a Flow That Can Activate or Deactivate a Session-Based Permission Set](https://help.salesforce.com/s/articleView?id=sf.perm_sets_session_activate_flow.htm&language=en_US)

Plan for Success in Flow Builder

Add and Edit Elements

Flow Core Action: Einstein Discovery

Get predictive and prescriptive intelligence directly in your flows with Einstein Discovery-powered
models. Select the row or fields to use for your predictions and let Einstein Discovery generate
predictions, suggested ways to improve predicted outcomes, and other details.

Set Input Values

Note: To view Einstein Discovery predictions, improvements, and other details, users must
have the **View Einstein Discovery Recommendations** system permission. To learn more,
[see Assign Einstein Discovery Permission Sets to Users .](https://help.salesforce.com/s/articleView?id=sf.bi_edd_setup_assign_permsets.htm&language=en_US)

Use values from an Einstein Discovery model to set the inputs for the action.

**Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

`Action` Search for the deployed models to which you have access.

`Label` Descriptive label for the action.

`API Name` API name for the action.

`Description` Description for the action.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

What to Store

`Predictions` Enable output from a predictive model to be stored in a flow resource.

`Top Predictors` Enable top predictors to be stored in a flow resource.

`Top Improvements` Enable suggested actions to be stored in a flow resource. Applies only to numeric
and binary classification models.

`Select Object Record ID Field` Generate predictions based on a Salesforce object record.

`Map Fields` Generate predictions using flow resources.

`Record ID Field` ID of the record to use for the prediction.

`Model Variable` Map the prediction model variables to flow resources.

```
Advanced

```

SEE ALSO:

[About Models](https://help.salesforce.com/s/articleView?id=sf.bi_edd_model_about.htm&language=en_US)

Add and Edit Elements

Optionally, for predictions associated with multiclass classification models, expand
Advanced, select **Manually assign variables**, and selectively store output values
(class probabilities, the prediction, and top predictors).

Flow Core Action: Get Forecast Context

Get forecast context for a specific user. To be used in the Forecast Guidance Flow as part of the Get
Forecast Guidance copilot action.

In Flow Builder, add an Action element to your Flow. In the New Action window, search for Get
##### Forecast Context, and then select Get Forecast Context .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

Store Output Values

EDITIONS

Available in: Lightning
Experience

Available in: **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

The Get Forecast Context action is a part of the Forecast Guidance Flow, designed to retrieve forecasting context for a specific user. It's
primarily used in conjunction with the Get Forecast Guidance copilot action.

Limitations

This action is limited to usage within Flow. It can't be invoked through other methods such as Apex, REST API, Copilot, Prompt Studio,
or Einstein Bots. While actions can typically be invoked through various frameworks like InvocableActionService, this specific action is
restricted solely to Flow.

SEE ALSO:

_Salesforce Help_ [: Copilot Action: Get Forecast Guidance](https://help.salesforce.com/s/articleView?id=sf.copilot_actions_ref_get_forecast_guidance.htm&language=en_US)

Flow Core Action: Get Forecast Opportunities

Get forecast opportunities for a user that matches the specified criteria. To be used in the Forecast
Guidance flow as part of the Get Forecast Guidance copilot action.

In Flow Builder, add an Action element to your flow. In the New Action window, search for Get
##### Forecast Opportunities, and then select Get Forecast Opportunities .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.


EDITIONS

Available in: Lightning
Experience

Available in: **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

Usage

The Get Forecast Opportunities retrieves opportunity ID records for a user based on specified criteria. It's designed mainly to be used
within the Forecast Guidance flow as part of the Get Forecast Guidance copilot action.

Limitations

This action is limited to usage within a flow. It can't be invoked through other methods such as Apex, REST API, Copilot, Prompt Studio,
or Einstein Bots. While actions can typically be invoked through various frameworks like InvocableActionService, this specific action is
restricted solely to Flow.

SEE ALSO:

_Salesforce Help_ [: Copilot Action: Get Forecast Guidance](https://help.salesforce.com/s/articleView?id=sf.copilot_actions_ref_get_forecast_guidance.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Get Record Prioritization Data

Get record data and field metadata to prioritize records for a user. This action is used in the Get
Opportunity Details flow as part of the Prioritize Opportunities copilot action.

In Flow Builder, add an Action element to your flow. In the New Action window, search for
##### Prioritization, and select Get Record Prioritization Data .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

Store Output Values

EDITIONS

Available in: Lightning
Experience

Available in: **Professional**,
**Enterprise**, **Performance**,
Unlimited, and **Developer**
Editions

Usage

The Get Record Prioritization Data action is a part of the Get Opportunity Details flow, which is designed to retrieve record data and field
metadata record prioritization. It’s primarily used with the Prioritize Opportunities copilot action.

Limitations

This action is limited to usage within flow. It can’t be invoked through other methods such as Apex, REST API, Copilot, Prompt Studio,
or Einstein Bots. While actions can typically be invoked through frameworks such as InvocableActionService, this specific action is
restricted to flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Lock Record

Locks or unlocks a workflow-enabled or approval-enabled record for editing during an approval and specifies who can edit the record
while it's locked.

Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience

Available in: **Essentials**, **Professional**, **Enterprise**, **Performance**, **Unlimited**, and **Developer** Editions

##### In Flow Builder, add an Action element to your flow. In the New Action window, search for Lock Record, and then select Lock

**Record** .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Field** **Description**

**Action**
Required. Specifies the action to perform on the record. Valid values are:

##### • Lock

**•** `Unlock`

**Record ID**
Required. The ID of the record to be locked or unlocked.

**Allowed ID** Optional. The ID of a user, group, queue. or user role record that represents who can edit the record
while it's locked.

Usage

This action is available in flows running in API version 61.0 and later.

To lock a record, a user must have view access to the record.

To edit a locked record, an allowed user must have edit access to the record, but system admins can always edit a locked record.

If a user role is specified for the Allowed ID parameter, a user must have a user role on or above the specified user role in the role hierarchy
to be able to edit the locked record.

A group or queue specified for the Allowed ID parameter must be a group or queue of users. The specified group or queue can’t contain:

**•** roles

**•** roles and internal subordinates.

An attempt to lock a record that’s already locked results in an error with the UNABLE_TO_LOCK_RECORD error code.

A system admin, the user who locked a record, or someone who’s an allowed user for the locked record can unlock the record. An
attempt by any other user results in an error with the INSUFFICIENT_ACCESS_OR_READ_ONLY error code.

The action completes without error when the action attempts to unlock a record that’s already unlocked.


Automate Your Business Processes with Salesforce Flow Flow Reference

Limitations

If a record is locked with this action and the record is submitted to an approval process, then the approval process overwrites the record
lock.

**•** If the approval process overwrites the lock from this action, then the allowed users specified by this action can no longer edit the
record.

**•** The approval process can be interrupted when this action unlocks a record locked by the approval process.

SEE ALSO:

_Salesforce Help_ [: Approval Processes](https://help.salesforce.com/s/articleView?id=sf.what_are_approvals.htm&type=5&language=en_US)

Flow Core Action: Post to Chatter

Post a message to a specified feed, such as a Chatter group or a case record. The message can
contain mentions and topics, but only text posts are supported.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Chatter`_, and select
##### Post to Chatter .

Set Input Values

Use values from earlier in the flow to set the inputs for the Chatter post.

**Input** **Description**
**Parameter**

`Message` The text that you want to post.

**•** To mention a user or group, enter _`@[reference]`_, where _`reference`_
is the ID for the user or group that you want to mention. The reference can
be a literal value, a merge field, or a flow resource. For example:
`@[{!UserId}]` .

**•** To add a topic, enter _`#[string]`_, where _`string`_ is the topic that you
want to add. For example: `#[Action Required]` .

This parameter accepts single-value resources of any type. That value is treated
as plain text and is limited to 10,000 characters.

`Target` Reference to the user, Chatter group, or record whose feed you want to post to.
`Name or` **•** To post to a user’s feed, enter the user’s ID or username. For example:
```
ID
        jsmith@salesforce.com

```

**•** To post to a Chatter group, enter the group’s name or ID. For example:

```
        Entire Organization

```

**•** To post to a record, enter the record’s ID. For example: _`001D000000JWBDx`_

This parameter accepts single-value resources of any type. That value is treated
as text.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Community

ID

```

ID of an Experience Cloud site to post to.

Valid only if Digital Experiences is enabled. Required if posting to a user or Chatter
group that belongs to an Experience Cloud site.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

This parameter accepts single-value resources of any type. That value is treated as text.

```
Target Type

Visibility

```

Required only if `Target Name or ID` is set to a username or a Chatter group name.

The type of feed that you want to post to. Valid values are:

**•** _`User`_ —If `Target Name or ID` is set to a user’s username, enter this value.

**•** _`Group`_ —If `Target Name or ID` is set to a Chatter group’s name, enter this value.

Specifies whether this feed item is available to Experience Cloud site users. To display this feed item only to
internal users, set it to _`internalUsers`_ .

Valid only if Digital Experiences is enabled. Valid values are:

**•** _`allUsers`_

**•** _`internalUsers`_

Store Output Values

To use the Chatter post’s ID later in the flow, store it in a variable. The values are assigned when the Chatter post is created.

**Output Parameter** **Description**

```
Feed Item ID

```

Usage

Assigns the created post’s ID to a resource in the flow.

This parameter accepts any single-value variables of type Text, Picklist, or Multi-Select Picklist.

At run time, the Chatter post isn’t created until the interview’s transaction completes. Transactions are complete when the interview
either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Flow Run Context

Flow Elements

Flow Core Action: Prompt Template Actions

Creates a response based on the large language model (LLM) response for the specified prompt
template and inputs.

##### In Flow Builder, add an Action element to your flow. In the New Action window, select the Prompt

**Template** category, and then select the name of the prompt template to use.

The API name for each action is prefixed with `generatePromptResponse` .


EDITIONS

Available in: Lightning
Experience

Available in: Enterprise,
Unlimited, and
Developer Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Set Input Values

Additional input values are based on the input variables specified for the prompt template.

Store Output Values

Usage

This action is available only if the following are true. Otherwise, the action fails.

**•** Prompt Builder is enabled.

**•** The user who runs the flow has the Prompt Template User permission.

**•** The specified prompt template has an active version.

SEE ALSO:

[Prompt Builder](https://help.salesforce.com/s/articleView?id=sf.prompt_builder_about.htm&type=5&language=en_US)

Flow Core Action: Global or Object-Specific Action

Call an object-specific or global action that’s already been configured in your org. Only Create,
Update, and Log a Call actions are available.

In Flow Builder, add an Action element to your flow. In the Action field, select the object-specific
or global action to configure.

The API name for each object-specific action is prefixed with the object it’s associated with, such
as `quickAction-Task.UpdatePriority` . The API name for each global action has no
prefix, such as `quickAction-NewAccount` .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

```
Related Record

ID

Input

Parameter

```

Only for object-specific actions. The ID of the record from which the action executes.

For example, the action creates a case that’s associated with a given account. Assign the ID for that account
to `Related Record ID` .

This parameter accepts single-value resources of any type. That value is treated as text.

Varies for each action.

The action layout determines which parameters are required. Required parameters appear by default and can’t
be removed. If a required field has a default or predefined value, that field is optional in object-specific and

global actions in the flow. If you later remove the field’s default or predefined value and you didn’t set a value
in the flow, the interview fails at run time.

The value must be compatible with the parameter.

Example: Your org has an object-specific action that creates a case record on an account. The flow calls that action at run time
and uses values from earlier in the flow to identify the account ID.

Note: At run time, the record isn’t created or updated until the interview’s transaction completes. Transactions are complete
when the interview either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Add and Edit Elements

Flow Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Core Action: Run a Batch Data Transform in Data Cloud

Run a batch data transform.

##### In Flow Builder, add an Action element to your flow. In the New Action window, select Run Batch

**Transform** .

Set Input Values

Use values from earlier in the flow to set an input for the action.

**Input Parameter** **Description**

`Batch Transform Name` Required. The name or the record ID of the batch data transform
to run.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

##### Quip Flow Core Actions

Quip provides several core actions for organizing, creating, and copying your Quip content in flows.
##### To add one of these actions to your flow, add an Action element. Then select the Quip category,

and search for the appropriate action.

Important: Quip core actions don’t support system-run flows or automated process users.
Quip core actions execute in the context of the user, who is also referred to as the context
user. The flow has access to whatever the context user has access to.

Flow Core Actions for Quip: Create Quip Document
Create a document, spreadsheet, or slide deck, and add content to it.

Flow Core Action for Quip: Create Quip Chat
Create a chat room, and send a message to its members.

Flow Core Action for Quip: Create Quip Folder
Create a private folder, or add it to existing folders.

EDITIONS

Available in: **Lightning**
**Experience**

Flow Core Action for Quip: Copy Quip Document
To use a document as a template, create a copy. By default, copied documents are added to the running user’s Private folder in Quip.

Flow Core Action for Quip: Copy Quip Content (Retired)
Copy content from a source slide deck, and paste it in a target slide.

Flow Core Action for Quip: Copy with Live Paste
Copy content from a source document, and paste it with Live Paste in a new document. When the source content is updated,
documents with the live pasted content stay up to date.

Flow Core Action for Quip: Attach Quip Document to Record
Attach a document to a Salesforce record. Linked documents show up in the Quip Associated Documents component.

Flow Core Action for Quip: Edit Quip Document
Edit content in a document, spreadsheet, or slide. Add or replace content based on a document section.

Flow Core Action for Quip: Lock Quip Document
To mark a document as complete, lock document edits.

Flow Core Action for Quip: Lock Quip Section
To mark sections of a document as complete or to keep them safe from accidental edits, lock them.

Flow Core Action for Quip: Export Quip Document to PDF
To mark a document as complete and to keep a copy for your records, export it as a PDF. You can attach the exported PDF to a
document or to a Salesforce record.

Flow Core Action for Quip: Send Message in Quip Chat
Send a message in a chat room.

Flow Core Action for Quip: Send a Message in a Document
Add a message to the conversations pane of a document.

Flow Core Action for Quip: Add Quip Document to Folder
Add a document to a folder to organize and share your documents.

Flow Core Action for Quip: Add Members to Document
Add members with different levels of access to a document.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Quip: Add Members to Quip Chat
Add users to a chat room.

Flow Core Action for Quip: Remove Quip Document from Folder
Remove a document from a folder. Make a shared document private again.

Flow Core Action for Quip: Remove Members from Quip Document
To rescind access to a document for certain users, remove them from the document.

Flow Core Action for Quip: Remove Members from Quip Chat
Remove users from a chat room.

SEE ALSO:

Add and Edit Elements

Flow Core Actions for Quip: Create Quip Document

Create a document, spreadsheet, or slide deck, and add content to it.

Warning: Quip is retiring slides on January 31, 2021. After this date, the Copy Content action
in Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Create Quip Document .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Document Title` The title of the new document. Only string values are supported.

`Add Members by Email Address` Optional. A list of user emails separated by commas to add to the new document. Valid
values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Company Link Address` Optional. Link sharing settings for the new document. By default, new documents are
set to edit-access. Valid values are:

**•** _`view`_ –To let users view the document, enter this value.

**•** _`edit`_ –To let users view and edit the document, enter this value.

**•** _`none`_ –To block user access to the document, enter this value.

`Content Type` Optional. Format of content added to the document. By default, content format is set to
html. Valid values are:

**•** _`html`_ –To format text added to `Document Content` with html, enter this value.

**•** _`liveapp`_ –To add a live app to your document, enter this value. Only valid if
`Document Type` is set to _`document`_ .


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Document Content

```

Optional. Content added to the new document. Valid only when `Content Type` is
set to html. By default, the document title is used for the document’s content. Valid values
are:

**•** String values

**•** _`@[Salesforce user ID]`_ –To @mention a Salesforce user in the document,
enter the Salesforce ID. If the user’s Salesforce email is connected to Quip, the user
ID is replaced with a Quip user @mention. If not, the Salesforce ID is replaced with
the user’s Salesforce email.

**•** _`@[person1@quip.com]`_ –To @mention a user by email, enter this value.

**•** _`@Everyone`_ –To send a notification to all users added to document, enter this value.

`Document Type` Optional. Type of document created including documents and spreadsheets. By default,
new documents are created as documents. Valid values are:

**•** _`document`_ –To create a document, enter this value.

**•** _`spreadsheet`_ –To create a spreadsheet, enter this value.

`Live App Type` Type of live app added to the document. Required if `Content Type` is set to
_`liveapp`_ . Only documents support live apps. Valid values are:

**•** _`salesforce_record`_ –To add the Salesforce Record live app to the document,
enter this value.

**•** _`salesforce_list`_ –To add the Salesforce List live app to the document, enter
this value.

```
Object Type

```

Type of object used by the Salesforce List live app. Required if `Live App Type` is set
to _`salesforce_list`_ . Only string values are supported. For example: _`Account`_,
_`Opportunity`_, or _`CustomObject__c`_ .

`Parent Folder URL` Optional. A list of Quip folder URLs separated by commas to add the new document to.
By default, the document is added to the user’s Private folder in Quip. Valid values are:

**•** _`https://[quip_site_url]/folder/[folder1_name],`_

```
                   https://[quip_site_url]/folder/[folder2_name]

```

**•** https://[quip_site_url]/folder/[folder_name]

For example: _`https://salesforce.quip.com/folder/account-plans`_

```
Record Name

Record Type

```

Optional. Name of the record added to the document through the Salesforce Record live
app. Valid only if the `Live App Type` is set to _`salesforce_record`_ . Only string
values are supported.

Optional. Type of object used by the Salesforce Record live app. Valid only if `Live App`
`Type` is set to _`salesforce_record`_ . Only string values are supported. For example:
_`Account`_, _`Opportunity`_, or _`CustomObject__c`_ .

`Salesforce List View ID` ID of the Salesforce list view added to the document. Required if `Live App Type` is
set to _`salesforce_list`_ .


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Salesforce Org Name` Optional. Salesforce org name used in the live app. Valid only if `Content Type` is set
to _`liveapp`_ . Only string values are supported. For example: _`Acme`_ .

`Salesforce Record ID` ID of the Salesforce record added to the document. Required if `Live App Type` is
set to _`salesforce_record`_ .

Store Output Values

**Output Parameter** **Description**

`Document Title` Title of the new document

`Document ID` ID of the new document

`Document Link` URL of the new document


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: A sales manager wants to create a document at the end of each quarter to identify which accounts are at risk of attrition.
You can create a flow that uses the Create Quip Document core action to create a document called Red Accounts. Add a Salesforce
list view through the Salesforce List live app that shows all accounts in the red. Then add the document a Red Accounts folder.

SEE ALSO:

Flow Elements

Flow Core Action for Quip: Create Quip Chat

Create a chat room, and send a message to its members.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Create Quip Chat .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Message` Chat message to get the chat room started. Valid values are:

**•** String values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`@[Salesforce user ID]`_ –To @mention a Salesforce user in the chat room,
enter the Salesforce ID. If the user’s Salesforce email is connected to Quip, the user
ID is replaced with a Quip user @mention. If not, the Salesforce ID is replaced with
the user’s Salesforce email.

**•** _`@[person1@quip.com]`_ –To @mention a user by email, enter this value.

**•** _`@Everyone`_ –To send a notification to all chat room members, enter this value.

`Add Members by Email Address` Optional. A list of user emails separated by commas to add to the new chat room. Valid
values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Chat Title` The title of the chat room. Only string values are supported.

Store Output Values

**Output Parameter** **Description**

`Chat ID` ID of the new chat room

`Chat Link` URL of the new chat room

`Chat Title` Title of the new chat room

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Create Quip Folder

Create a private folder, or add it to existing folders.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Create Quip Folder .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Folder Name` Name of the new folder. Only string values are supported.

`Folder Color` Optional. Color of the new folder. Valid values are:

**•** _`yellow`_

**•** _`red`_

**•** _`orange`_


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`green`_

**•** _`blue`_

**•** _`purple`_

**•** _`manila`_

**•** _`light red`_

**•** _`light orange`_

**•** _`light green`_

**•** _`light blue`_

**•** _`light purple`_

`Parent Folder URL` Optional. A list of folder URLs separated by commas to add the new folder to. By default,
the folder is added to the user’s Private folder in Quip. Valid values are:

**•** _`https://[quip_site_url]/folder/[folder1_name],`_

```
                      https://[quip_site_url]/folder/[folder2_name]

```

**•** https://[quip_site_url]/folder/[folder_name]

For example: _`https://salesforce.quip.com/folder/account-plans`_

Store Output Values

**Output Parameter** **Description**

`Created Folder Title` Title of the new folder

`Folder ID` ID of the new folder

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Copy Quip Document

To use a document as a template, create a copy. By default, copied documents are added to the
running user’s Private folder in Quip.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Copy Quip Document .

Important: Newly copied documents aren’t automatically attached to the record. To attach
the newly created document to the record and use Synced Sharing, use the Attach Document
to Record action after the Copy Quip Document action and set the Salesforce Record ID to
be the ID of the variable.

Set Input Values

Use values from earlier in the flow to set the inputs for the action.


EDITIONS

Available in: **Lightning**
**Experience**

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Document URL` The URL of the document that you want to copy. For example:

```
                    https://salesforce.quip.com/GVnGbtEasAGa

```

`Company Link Access` Optional. Link sharing settings for the copied document. By default, copied documents
are set to edit-access. Valid values are:

**•** _`view`_ –To let users view the copied document, enter this value.

**•** _`edit`_ –To let users view and edit the copied document, enter this value.

**•** _`none`_ –To block user access to the copied document, enter this value.

```
Context Record ID

```

Optional. ID of the record that you want to update with the copied document’s URL.
Including the Context Record ID doesn’t attach the document to a record.

Valid only if the Quip Document component is set up on the record layout. The `Target`
`Record URL Field` is required to use `Context Record ID` .

`Copy comments to new` Optional. This input determines whether to copy comments from the source document
`document` to the copied document. Valid values are:

**•** _`true`_ –To copy the source document’s comments and annotations, enter this value.

**•** _`false`_ –To copy the source document’s content without comments, enter this value.

`Member Emails` Optional. A list of user emails separated by commas to add to the copied document. Valid
values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Member Folder URLs` Optional. A list of folder URLs separated by commas to add the copied document to. Valid
values are:

**•** _`https://[quip_site_url]/folder/[folder1_name],`_

```
                   https://[quip_site_url]/folder/[folder2_name]

```

**•** https://[quip_site_url]/folder/[folder_name]

For example: _`https://salesforce.quip.com/folder/account-plans`_

```
Source Record ID

Target Record URL Field

```

Optional. ID of the record that you want to use in the place of mail merge syntax. For
example, to replace the copied document’s `Account.Name` merge field with the
record’s account name, enter the record ID.

Optional. Reference to the URL field on a record used by the `Context Record ID` .
This field is updated with the copied document URL and adds the copied document to
the record’s Quip Document component. Valid values are:

**•** _`API name of the field`_ –For example: _`QuipDocumentURL__c`_

The `Context Record ID` is required to use the `Target Record URL Field` .
Including the Target Record URL Field doesn’t attach the newly created document to the
record.

`Title` Optional. The title of the copied document. Only string values are supported.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

`Created Document Title` The title of the copied document.

`Document ID` ID of the copied document.

`Document Link` The URL of the copied document.

Example: [Watch an Account Plan Automation Demo (2 minutes)](https://salesforce.vidyard.com/watch/NzZb6RFrBmdD8yPpcPM5bH)

A sales rep wants to create an Account Plan and share it with the regional sales managers to close a large opportunity. You can
create a flow that uses the Copy Quip Document core action to copy an Account Plan template when the Opportunity stage is
set to Proposal/Quote. Configure the action to replace merge fields with data from the account, add the Account Plan to a folder,
and share the folder with the regional sales managers.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Copy Quip Content (Retired)

Copy content from a source slide deck, and paste it in a target slide.

Warning: Quip is retiring slides on January 31, 2021. After this date, the Copy Content action
in Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

###### Drag a Core Action element onto the canvas. In the Core Action field, enter Quip, and select Copy

**Quip Content** .


EDITIONS

Available in: **Lightning**
**Experience**

Automate Your Business Processes with Salesforce Flow Flow Reference

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

`Document Type` Type of document you want to copy. Valid values are:

**•** _`slides`_ –To copy slides to another slide deck, enter this value.

`Source Document URL` URL of the slide deck you want to copy content from.

`Target Document URL` URL of the slide deck where you want to add copied content.

`Slide Count Range` Optional. Number of slides to copy from the source slide deck. By default, `Slide Count`
`Range` is set to _`1`_ .

`Source Section Anchor Link` URL of a section in the source slide deck that you want to copy content from.

`Source Slide Number` Optional. The slide index to copy content from. For example, to copy content from the
first slide of a deck, enter _`1`_ .

```
Target Record ID

```

Optional. ID of the record you want to use in the place of mail merge syntax. For example,
to replace the copied document’s [[Account.Name] merge field with the record’s account
name, enter the record ID.

`Target Section Anchor Link` URL of a section in the target slide deck where you want to paste copied content.

`Target Slide Number` Optional. The slide index to copy content to. For example, to paste copied content to the
first slide of a deck, enter _`1`_ .

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the target slide deck content was copied to.

`Document Link` URL of the target slide deck content was copied to.

`Created Document Title` The title of the slide deck content was copied to. Only string values are supported.

Example: A sales rep wants to update a slide deck with the latest sales numbers to prepare for a customer pitch. The sales rep
wants to use the slides from another deck that their manager keeps up to date with the latest numbers. You can create a flow that
uses the Copy Quip Content core action to copy content slides 1 and 2 from their manager’s slide deck and replace the content
in slides 3 and 4 of the customer-facing slide deck.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Quip: Copy with Live Paste

Copy content from a source document, and paste it with Live Paste in a new document. When the
source content is updated, documents with the live pasted content stay up to date.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Copy with Live Paste .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

```
Source Section Anchor Links

```

URLs of the sections in the source document that you want to copy content from. Anchor
links must be from the same document and separated with commas. Valid only if
`Content Type` is set to anchor link.

`Content Location` Optional. Location in the document where you want to live paste your copied content.
Valid values are:

**•** _`append`_ –To live paste content to the end of the document, enter this value.

**•** _`prepend`_ –To live paste content to the beginning of the document, enter this value.

**•** _`after_section`_ –To live paste content after a designated section, enter this value.
Valid only if `Target Section Anchor Link` is specified.

**•** _`before_section`_ –To live paste content before a designated section, enter this
value. Valid only if `Target Section Anchor Link` is specified.

**•** _`replace_section`_ –To replace an existing section with live pasted content, enter
this value. Valid only if `Target Section Anchor Link` is specified.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`after_document_range`_ –To live paste content after a named document range,
enter this value. Valid only if `Target Document Range Heading Text`
is specified.

**•** _`before_document_range`_ –To live paste content before a named document
range, enter this value. Valid only if `Target Document Range Heading`
`Text` is specified.

**•** _`replace_document_range`_ –To replace a named document range with live
pasted content, enter this value. Valid only if `Target Document Range`
`Heading Text` is specified.

By default, `Content Location` is set to _`append`_ .

`Content Type` Type of content that you want to copy. Valid values are:

**•** _`anchor_link`_ –To copy content based on a section anchor link URL, enter this
value.

**•** _`document_range`_ –To copy content from a template based on a document range
name, enter this value.

`Source Document Range` Heading text from the document range that you want to copy. Valid only if `Content`
`Heading` `Type` is set to _`document_range`_ .

`Target Document URL` URL of the document that you want to copy live pasted content to.

`Target Section Anchor Link` Optional. URL of the section in the target document where you want to copy live pasted
content to.

`Target Document Range` Heading text from the document range where you want to live paste your copied content.

```
   Heading Text

```

`Update Automatically` Optional. Automatically update the target document when the source content is updated
and Live Paste is on. Valid values are:

**•** _`true`_

**•** _`false`_

By default, `Update Automatically` is set to _`false`_ .

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the document where live pasted content was added.

`Document Link` URL of the document where live pasted content was added.

`Document Title` Title of the document where live pasted content was added.


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: A sales manager wants to add instructions to all Account Plans to teach their sales reps what to do next. But the sales
manager doesn’t want to update each one individually. You can create a flow that uses the Copy with Live Paste core action to
add the updated instructions to the end of the Account Plan.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Attach Quip Document to Record

Attach a document to a Salesforce record. Linked documents show up in the Quip Associated
Documents component.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Attach Quip Document to Record .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Document URL` The URL of the document that you want to attach to a Salesforce record. For example:

```
                 https://salesforce.quip.com/GVnGbtEasAGa

```

`Salesforce Record ID` ID of the Salesforce record that you want to attach your document to.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

`Content Document Link ID` The ID of the link between the document and the record where it’s attached. The Attach
Quip Document to Record flow action creates a Content Document object that references

the document. It also creates a Content Document Link object that maps the record to
the Content Document object.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Edit Quip Document

Edit content in a document, spreadsheet, or slide. Add or replace content based on a document
section.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Edit Quip Document .

Warning: Quip is retiring slides on January 31, 2021. After this date, the Copy Content action
in Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Content Location` Location in the document where you want to add content. Valid values are:

**•** _`append`_ –To add content to the end of the document, enter this value.

**•** _`prepend`_ –To add content to the beginning of the document, enter this value.

**•** _`after_section`_ –To add content after a designated section, enter this value. Valid
only if `Section Anchor Link` is specified.

**•** _`before_section`_ –To add content before a designated section, enter this value.
Valid only if `Section Anchor Link` or `Section Match Type` is specified.

**•** _`replace_section`_ –To replace an existing section with new content, enter this
value. Valid only if `Section Anchor Link` or `Section Match Type` is
specified.

**•** _`after_document_range`_ –To add content to a template after a document
range, enter this value. Valid only if `Document Range Heading` is specified.

**•** _`before_document_range`_ –To add content to a template before a document
range, enter this value. Valid only if `Document Range Heading` is specified.

**•** _`replace_document_range`_ –To replace existing content based on a document
range, enter this value. Valid only if `Document Range Heading` is specified.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Document URL` URL of the document that you want to edit. For example:

```
                    https://salesforce.quip.com/GVnGbtEasAGa

```

`Edit Document Type` Type of document that you want to edit. Valid values are:

**•** _`document`_ –To edit a document, enter this value.

**•** _`spreadsheet`_ –To edit a spreadsheet, enter this value.

`Content` Optional. Content added to the document that you want to edit. Valid only if `Content`
`Format` is set to _`html`_ . Valid values are:

**•** String values

**•** _`@[Salesforce user ID]`_ –To @mention a Salesforce user in the document,
enter the Salesforce ID. If the user’s Salesforce email is connected to Quip, the user
ID is replaced with a Quip user @mention. If not, the Salesforce ID is replaced with
the user’s Salesforce email.

**•** _`@[person1@quip.com]`_ –To @mention a user by email, enter this value.

**•** _`@Everyone`_ –To send a notification to everyone in the document, enter this value.

`Content Format` Optional. Format of content added to the document. By default, content format is set to
html. Valid values are:

**•** _`html`_ –To format text added to `Document Content` with html, enter this value.

**•** _`liveapp`_ –To add a live app to your document, enter this value. Only valid if
`Document Type` is set to _`document`_ .

`Disable Extra Lines in Quip` Optional. Boolean parameter that prevents Quip from inserting an extra line between
paragraphs. The default is _`false`_, meaning that by default extra lines _are_ inserted.

`Document Range Heading` Optional. Heading text that marks the start of the document range.

`Element Type` Optional. The type of spreadsheet element to edit. Only valid if `Document Type` is
set to _`spreadsheet`_ . Valid values are:

**•** _`row`_ –To edit a spreadsheet row, enter this value.

**•** _`column`_ –To edit a spreadsheet column, enter this value.

`Image Number` Optional. Image index of an image on a slide. Only valid if `Document Type` is set to
_`slides`_ . Valid values are:

**•** _`Image integers`_ –Integers represent an image index on a slide. Images are
ordered from top to bottom. Images closer to the top of a slide have an image integer
of 1. Images closer to the bottom have the biggest integers. If there are multiple
images on a slide with the same vertical positions, the image numbers are ordered
from left to right. If there are multiple images on a slide with the same horizontal and
vertical positions, the image that is behind the other one has an image number of
_`1`_ . The image in front has an image number of _`2`_ .

Quip is retiring slides on January 31, 2021. After this date, the Copy Content action in
Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Image URL

```

Optional. The URL of an image in a slide deck. Only valid if `Document Type` is set to
_`slides`_ .

Quip is retiring slides on January 31, 2021. After this date, the Copy Content action in
Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

`Live App Type` Type of live app added to the document. Required if `Content Format` is set to
_`liveapp`_ . Only documents support live apps. Valid values are:

**•** _`salesforce_record`_ –To add the Salesforce Record live app to the document,
enter this value.

**•** _`salesforce_list`_ –To add the Salesforce List live app to the document, enter
this value.

```
Object Type

Record Name

Record Type

```

Type of object used by the Salesforce List live app. Required if `Live App Type` is set
to _`salesforce_list`_ . Only string values are supported. For example: _`Account`_,
_`Opportunity`_, or _`CustomObject__c`_ .

Optional. Name of the record added to the document through the Salesforce Record live
app. Valid only if the `Live App Type` is set to _`salesforce_record`_ . Only string
values are supported.

Optional. Type of object used by the Salesforce Record live app. Valid only if `Live App`
`Type` is set to _`salesforce_record`_ . Only string values are supported. For example:
_`Account`_, _`Opportunity`_, or _`CustomObject__c`_ .

`Salesforce List View ID` Optional. ID of the Salesforce list view added to the document. Valid only if `Live App`
`Type` is set to _`salesforce_list`_ .

`Salesforce Org Name` Optional. Salesforce org name used in the live app. Valid only if `Content Format` is
set to _`liveapp`_ . Only string values are supported. For example: _`Acme`_ .

`Salesforce Record ID` Optional. ID of the Salesforce record added to the document. Valid only if `Live App`
`Type` is set to _`salesforce_record`_ .

`Section Anchor Link` URL of a section in the document where you want to add or replace content. Valid only
if `Content Location` is set to _`before_section`_, _`after_section`_, or

_`replace_section`_ . For example:
_`https://[quip_site_url]/GVnGAtEawAGh/Source-Slide#JUJACAuc0ps`_,
where Source-Slide#JUJACAuc0ps is a specific slide in the slide deck.

`Section Match Type` Placement of keywords used to identify the section where you want to add or replace
content. Valid only if `Content Location` is set to _`before_section`_,

_`after_section`_, or _`replace_section`_, and the `Document Type` is
_`document`_ . Keywords aren’t case-sensitive and ignore HTML tags. Valid values are:

**•** _`prefix`_ –To find a keyword in a document based on the first part of a word, enter
this value. For example, _`hello`_ is the prefix for _`helloworld`_ .

**•** _`suffix`_ –To find a keyword in a document based on the end of a word, enter this
value. For example, _`world`_ is the suffix for _`helloworld`_ .


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Section Style` Format of the document section where you want to add or replace content. Required if
`Section Type` is set to _`textmatch`_ . Valid values are:

**•** _`paragraph`_ –To find a keyword in a paragraph, enter this value.

**•** _`heading`_ –To find a keyword in a heading, enter this value.

**•** _`list`_ –To find a keyword in a list, enter this value.

`Section Text` Keywords to identify the section where you want to add or replace content. Required if
`Section Match Type` is specified. Only string values are supported.

`Section Type` Optional. Determines how a section is edited. Valid values are:

**•** _`anchorlink`_ –To edit a document section based on its anchor link, enter this value.
Valid only if `Section Anchor Link` is set up.

**•** _`textmatch`_ –To edit a document section based on a keyword, enter this value.

`Slide Layout` Optional. The slide element to edit. Only valid if `Document Type` is set to _`slides`_ .
Valid values are:

**•** _`single_column`_ –To edit a slide column, enter this value.

**•** _`image`_ –To edit a slide image, enter this value.

Quip is retiring slides on January 31, 2021. After this date, the Copy Content action in
Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

```
Slide Number

```

Store Output Values

Optional. The slide index to edit. Only valid if `Document Type` is set to _`slides`_ . For
example, to edit the first slide of a deck, enter _`1`_ .

Quip is retiring slides on January 31, 2021. After this date, the Copy Content action in
Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

**Output Parameter** **Description**

`Document ID` ID of the edited document

`Document Link` URL of the edited document

`Document Title` Title of the edited document


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: A sales rep wants to update their Account Plan and add a list view of open opportunities related to the account. You
can create a flow that uses the Edit Document core action to add the Salesforce List live app to the end of the Account Plan.

Example: A service manager wants to update an Account Plan with an account history. The account is up for renewal and the
service manager wants to make sure that the sales rep has the necessary background on past cases before contacting the customer.
You can create a flow that uses the Edit Document core action to add an account history to an Account Plan and place it before
the placeholder lorem.


Automate Your Business Processes with Salesforce Flow Flow Reference

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Lock Quip Document

To mark a document as complete, lock document edits.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Lock Quip Document .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

`Document URL` URL of the document that you want to lock.

EDITIONS

Available in: **Lightning**
**Experience**

`Lock Operation` Action of locking or unlocking the document. Only a user with full access to the document
can lock or unlock it. Valid values are:

**•** _`lock`_ —To lock edits to the document, enter this value.

**•** _`unlock`_ —To let users edit a locked document, enter this value.

Store Output Values

**Output Parameter** **Description**

`Document Lock Operation` Success marker of whether the document was locked or unlocked. Possible results are
`Result` `true` or `false` .


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: A sales manager wants to lock edits to their reps’ Account Plans after a deal is closed. You can create a flow that uses
the Lock Quip Document core action to lock edits to Account Plans when the Opportunity stage is set to Closed Won.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Lock Quip Section

To mark sections of a document as complete or to keep them safe from accidental edits, lock them.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Lock Quip Section .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Section Anchor Link` Anchor link URL of the document section that you want to lock.

`Lock Operation` The action of locking or unlocking a document section. Only a user with full access to the
document can lock or unlock its sections. Valid values are:

**•** _`lock`_ —To lock edits to the document, enter this value.

**•** _`unlock`_ —To let users edit a locked document, enter this value.

Store Output Values

**Output Parameter** **Description**

`Section Lock Operation` Success marker of whether the section was locked or unlocked. Possible results are `true`
`Result` or `false` .

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Export Quip Document to PDF

To mark a document as complete and to keep a copy for your records, export it as a PDF. You can
attach the exported PDF to a document or to a Salesforce record.

Set Input Values

Use values from earlier in the flow to set the inputs for the action.


EDITIONS

Available in: **Lightning**
**Experience**

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Source Document URL` URL of the document you want to export to PDF. Valid values are:

**•** String values

**•** Field references—To pull a document housed in a custom URL field, enter the field
API name.

`Sheet Name` Name of the sheet in a spreadsheet that you want to export to a PDF. Valid only for
spreadsheet files. If no sheet name is entered, defaults to the first sheet.

`Target Document URL` Optional. URL of the document where you want to attach the created PDF. The PDF is
added to the end of the document.

```
Salesforce Organization ID

Target Record ID

```

Store Output Values

ID of the Salesforce org where you want to attach your new PDF. You can use the same
Salesforce org ID of the triggering record, or attach the PDF to a different org. Valid only
if `Target Record ID` is specified.

Optional. ID of the Salesforce record you want to attach your document to. PDFs attached
to a record are added to the record’s Files component and Notes and Attachments
component, and are visible to any user with access to the record. Valid values are:

**•** Alphanumeric series of numbers and letters for a specific Salesforce record.

**•** _`{!$Record.Id}`_ To attach the PDF to the same record that triggered the flow,
enter this value.

**Output Parameter** **Description**

`Request ID` ID to check the status of the PDF export.

`Status message` Error message that explains why the document wasn’t exported to a PDF.

`Status of the request` Success marker of whether the document was exported to a PDF. Can be `success`,
`failure`, or `pending` .

SEE ALSO:

Flow Elements

Flow Core Action for Quip: Send Message in Quip Chat

Send a message in a chat room.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Send Message in Quip Chat .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.


EDITIONS

Available in: **Lightning**
**Experience**

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Chat URL` URL of the chat room where you want your message to appear.

`Message` Chat message sent to the chat room. Valid values are:

**•** String values

**•** _`@[Salesforce user ID]`_ –To @mention a Salesforce user in the chat room,
enter the Salesforce ID. If the user’s Salesforce email is connected to Quip, the user
ID is replaced with a Quip user @mention. If not, the Salesforce ID is replaced with
the user’s Salesforce email.

**•** _`@[person1@quip.com]`_ –To @mention a user by email, enter this value.

**•** _`@Everyone`_ –To send a notification to all chat room members, enter this value.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Send a Message in a Document

Add a message to the conversations pane of a document.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Send Message in Document .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Document URL` URL of the document where you want to add a comment.

`Message` Message added to the document. Valid values are:

**•** String values

**•** _`@[Salesforce user ID]`_ –To @mention a Salesforce user in the document,
enter the Salesforce ID. If the user’s Salesforce email is connected to Quip, the user
ID is replaced with a Quip user @mention. If not, the Salesforce ID is replaced with
the user’s Salesforce email.

**•** _`@[person1@quip.com]`_ –To @mention a user by email, enter this value.

**•** _`@Everyone`_ –To send a notification to everyone in the document, enter this value.

`Section Anchor Link` Optional. URL of a section in the document where you want the message to appear.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Quip: Add Quip Document to Folder

Add a document to a folder to organize and share your documents.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Add Quip Document to Folder .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

`Document URL` URL of the document that you want to add to a folder.

`Folder URL` URL of the folder where you want to add the document.

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the added document

`Document Link` URL of the document added to the folder

`Document Title` Title of the added document

Example: [Watch an Account Plan Automation Demo (2 minutes)](https://salesforce.vidyard.com/watch/NzZb6RFrBmdD8yPpcPM5bH)

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Add Members to Document

Add members with different levels of access to a document.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Add Members to Document .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

`Document URL` URL of the document that you want to add members to.

EDITIONS

Available in: **Lightning**
**Experience**

EDITIONS

Available in: **Lightning**
**Experience**

`Add Comment-Access Members` Optional. A list of user emails separated by commas that can view and comment on the
`by Email Address` document. Valid values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`person1@quip.com`_

`Add Edit-Access Member by` Optional. A list of user emails separated by commas that can view, comment on, and edit
`Email Address` the document. Valid values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Add Full-Access Members by` Optional. A list of user emails separated by commas that can view, comment on, edit,
`Email Address` and share the document. Valid values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Add View-Access Members by` Optional. A list of user emails separated by commas that can view the document. Valid
`Email Address` values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the document

`Document Link` URL of the document

`Document Title` Title of the document

Example: A service manager wants to add Tier 3 service reps to a Case Swarm document to solve a customer case. The service
manager also wants to keep sales reps with open opportunities related to the account up to date. You can create a flow that uses
the Add Members to Document core action to add Tier 3 reps to the Case Swarm document and grant the service reps edit-access
to the document. Then you can add the sales reps with open opportunities to the document with comment-access so that they
can see what’s happening and ask questions.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Add Members to Quip Chat

Add users to a chat room.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Add Members to Quip Chat .


EDITIONS

Available in: **Lightning**
**Experience**

Automate Your Business Processes with Salesforce Flow Flow Reference

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

`Add Members by Email Address` A list of user emails separated by commas to add to the chat room. Valid values are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Chat URL` URL of the chat room that you want to add members to.

Store Output Values

**Output Parameter** **Description**

`Chat ID` ID of the chat room

`Chat Link` URL of the chat room

`Chat Title` Title of the chat room

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Remove Quip Document from Folder

Remove a document from a folder. Make a shared document private again.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Remove Quip Document from Folder .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Document URL` URL of the document that you want to remove from a folder.

`Folder URL` URL of the folder that you want to remove the document from.

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the removed document

`Document Link` URL of the removed document


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

`Document Title` Title of the removed document

SEE ALSO:

Add and Edit Elements

Flow Core Action for Quip: Remove Members from Quip Document

To rescind access to a document for certain users, remove them from the document.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Remove Members from Quip Document .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Document URL` URL of the document that you want to remove members from.

`Remove Members by Email` A list of user emails separated by commas to remove from the document. Valid values
`Address` are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

Store Output Values

**Output Parameter** **Description**

`Document ID` ID of the document

`Document Link` URL of the document

`Document Title` Title of the document

Example: A service manager previously added Tier 3 service reps and sales reps to a Case Swarm document to solve a customer
case. Now that the case is closed, the service manager wants to remove user access to the document to preserve its integrity. You
can create a flow that uses the Remove Members from Quip Document core action to remove Tier 3 reps and sales reps from the
document.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Quip: Remove Members from Quip Chat

Remove users from a chat room.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Quip`_, and select
###### Remove Members from Quip Chat .

Set Input Values

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

`Remove Members by Email` A list of user emails separated by commas to remove from the chat room. Valid values
`Address` are:

**•** _`person1@quip.com, person2@quip.com, person3@quip.com`_

**•** _`person1@quip.com`_

`Chat URL` URL of the chat room that you want to remove members from.

Store Output Values

**Output Parameter** **Description**

`Chat ID` ID of the chat room

`Chat Link` URL of the chat room

`Chat Title` Title of the chat room

SEE ALSO:

Add and Edit Elements

B2B Commerce Checkout Flow Core Actions

The B2B Commerce Checkout Flow provides several core actions for implementing a successful
checkout process within your Commerce org. To add one of these actions to your flow, add an
##### Action element. Then select the B2B Commerce category, and search for the appropriate action.

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex `ConnectApi` namespace. For more information on using Apex-defined variables in
flows, see Considerations for the Apex-Defined Data Type on page 260.

Flow Core Action for Checkout Flow: Activate Order
Activates a Salesforce standard draft order.

Flow Core Action for Checkout Flow: Calculate Cart Promotions
Request a full calculation of all line items in the cart that have a promotion.

Flow Core Action for Checkout Flow: Calculate Cart Shipment Costs
Request the shipping costs of all line items within the cart.


EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Checkout Flow: Calculate Cart Taxes
Request a tax cost calculation for all line items within the cart.

Flow Core Action for Checkout Flow: Cancel Cart Async Operation
Cancel the current checkout so the user can return to an unlocked cart. This operation automatically executes when cart changes
are invoked, such as add to cart.

Flow Core Action for Checkout Flow: Cart to Order
Create a Salesforce standard order in draft mode.

Flow Core Action for Checkout Flow: Check Cart Inventory
Request a full inventory availability check of all line items in the cart.

Flow Core Action for Checkout Flow: Checkout Session Action
Get or create a checkout session, and return the ID of the session to the caller.

Flow Core Action for Checkout Flow: Price Cart
Request a reprice of all line items in a cart.

Flow Core Action for Checkout Flow: Update Checkout Session Action
The Update Checkout Session action updates the checkout session state if the current state matches the expected state. This action
provides consistency during checkout handling and guarantees that if two browsers attempt to update the state, one succeeds and
the other fails validation.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Activate Order

Activates a Salesforce standard draft order.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Activate Order . To access this action from the API, use the name

`activateOrderAction` .

Set Input Values:

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

`orderStatus` A DynamicEnum with the OrderTypeEnum value.

Store Output Values:

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

The Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

CartValidationOutput
Object Has Errors

The CartValidationOutput object has errors that are related to the cart and must be cleared before order
activation.

Error Code: INVALID_INPUT

HTTP Status Code: 403

CheckoutSession Isn’t
Checkout Session state must be in the Activate state for the order activation to go forward.
in the Activate State
Error Code: INVALID_INPUT

HTTP Status Code: 403


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

CheckoutSession Is in
the Processing State

CheckoutSession can’t be in the Processing state. Processing indicates a separate integration is already running.

Error Code: INVALID_INPUT

HTTP Status Code: 403

Invalid Order Status
The Order status input that is passed to the API must be the `ACTIVATE` status code.
Input
Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

OrderSummary
The OrderSummary wasn’t created due to an internal error.
Wasn’t Created
Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 403

Usage:

To use the B2B Commerce Activate Order action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The buyer has edit access to the cart.

**•** An order in `Draft` status is generated from the cartToOrder action, and the `orderId` is in CartCheckoutSession.

**•** The cart status is `CartStatusEnum.CHECKOUT` .

**•** `Session.IsProcessing` isn’t set to `False` .

**•** `Session.NextState` is set to `activateOrder` .

**•** `Session.State` can’t be empty.

**•** `backgroundOperationId` can’t be `New` or `Running` .

When the Activate Order action runs, these API interactions occur.

**1.** The order item is activated, making it read-only.

**2.** The order summary is generated asynchronously.

**3.** The CheckoutSession is archived.

**4.** The cart is archived.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Checkout Flow: Calculate Cart Promotions

Request a full calculation of all line items in the cart that have a promotion.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Calculate Cart Promotions . To access this action from the API, use the name

`calcCartPromotionsAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that you want to reprice.

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

Usage

[This action is executed asynchronously using the pricing service configured in StoreIntegratedService.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_storeintegratedservice.htm)

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Calculate Cart Shipment Costs

Request the shipping costs of all line items within the cart.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Calculate Cart Shipment Costs . To access this action from the API, use the name

`calcCartShipmentAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

Usage

[This action is executed asynchronously using the pricing service configured in StoreIntegratedService.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_storeintegratedservice.htm)

To use the B2B Commerce Check Cart Shipment Cost action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The buyer has edit access to the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** The cart status isn’t `Closed` .

**•** `Session.IsProcessing` isn’t set to `False` .

**•** `Session.NextState` is set to `DeliveryMethod` .

**•** `Session.State` can’t be empty.

**•** `backgroundOperationId` can’t be `New` or `Running` .

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Calculate Cart Taxes

Request a tax cost calculation for all line items within the cart.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Calculate Cart Taxes . To access this action from the API, use the name

`calcCartTaxesAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

Usage

[This action is executed asynchronously using the pricing service configured in StoreIntegratedService.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_storeintegratedservice.htm)

To use the B2B Commerce Calculate Cart Taxes action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The buyer has edit access to the cart.

**•** The cart status isn’t `Closed` .

**•** `Session.IsProcessing` isn’t set to `False` .

**•** `Session.NextState` is set to `ComputeTaxes` .

**•** `Session.State` can’t be empty.

**•** `backgroundOperationId` can’t be `New` or `Running` .

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Checkout Flow: Cancel Cart Async Operation

Cancel the current checkout so the user can return to an unlocked cart. This operation automatically
executes when cart changes are invoked, such as add to cart.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Cancel Cart Async Operation . To access this action from the API, use the name

`cancelCartAsyncOperation` .

Set Input Values:

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

Error Conditions:

**Error Condition** **Description**

Cancel a Closed Cart
A cart can’t be canceled after it’s closed.

Error Code: INVALID_OPERATION

HTTP Status Code: 403

Usage:

To use the B2B Commerce Cancel Cart Async Operation, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The cart status can’t be `Closed` .

**•** There’s an active CartCheckoutSession associated with the cart.

**•** There’s a valid `BackgroundOperationId` .

When the Cancel Cart Async Operation runs, these API interactions occur.

**1.** The background operation is marked as canceled.

**2.** The cart transitions to the Active state, unlocking the cart for more updates.

**3.** If it exists, the CartCheckoutSession object is archived.

SEE ALSO:

Add and Edit Elements


EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Checkout Flow: Cart to Order

Create a Salesforce standard order in draft mode.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
search for **Cart To Order** . To access this action from the API, use the name
`cartToOrderAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

`runAsync` Execute the Cart to Order action asynchronously.

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or
B2BCommerceIntegrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

Usage

To use the B2B Commerce Cart to Order action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The buyer has edit access to the cart.

**•** The cart status is `CartStatusEnum.CHECKOUT` .

**•** `Session.IsProcessing` isn’t set to `False` .

**•** `Session.NextState` is set to `cartToOrder` .

**•** `Session.State` can’t be empty.

**•** `backgroundOperationId` can’t be `New` or `Running` .

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Check Cart Inventory

Request a full inventory availability check of all line items in the cart.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Check Cart Inventory . To access this action from the API, use the name

`checkCartInventoryAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`cartId` The ID of the cart that transitions into a checkout.

Store Output Values

**Output Parameter** **Description**

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

The Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State
Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

HTTP Status Code: 500

Usage

[This action is executed asynchronously using the pricing service configured in StoreIntegratedService.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_storeintegratedservice.htm)

To use the B2B Commerce Check Cart Inventory action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The buyer has edit access to the cart.

**•** The cart status isn’t `Closed` .

**•** `Session.IsProcessing` isn’t set to `False` .

**•** `Session.NextState` is set to `CheckInventory` .

**•** `Session.State` can’t be empty.

**•** `backgroundOperationId` can’t be `New` or `Running` .

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Checkout Session Action

Get or create a checkout session, and return the ID of the session to the caller.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Checkout Session Action . To access this action from the API, use the name

`checkoutSessionAction` .

Set Input Values:

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart that transitions into a checkout.

Store Output Values:

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`requestId` The ID of the request that processes and then either creates or returns the Checkout Session.

Error Conditions:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have

The user doesn’t have access to the effective account either because it isn’t a buyer account or they don’t have

Access to the Effective

permission to buy for the account.

Account
Error Code: BAD_REQUEST

HTTP Status Code: 400

User Account Isn’t
The current logged-in buyer account isn’t associated with the store and therefore isn’t a store member.
Associated With the
Error Code: BAD_REQUEST
Store

HTTP Status Code: 400

Cart Is Already in
The requested cart is already being processed.
Progress
Error Code: BAD_REQUEST

HTTP Status Code: 400

The Session Wasn’t
The session wasn’t created due to an internal service error.
Created
Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

Usage:

To use the B2B Commerce Checkout Session Action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The cart status is set to `Active` or `Checkout` .

**•** The cart must not have any current, active session.

When the Checkout Session Action runs, these API interactions occur.

**1.** The cart transitions to the Checkout state, preventing more updates to the cart.

**2.** If it doesn’t exist already, the CartCheckoutSession object is created.


Automate Your Business Processes with Salesforce Flow Flow Reference

**3.** All errors that are mapped to the input `cartId` [, on the CartValidationOutput object, are cleared.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_cartvalidationoutput.htm)

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Price Cart

Request a reprice of all line items in a cart.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Price Cart . To access this action from the API, use the name priceCart .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`cartId` The ID of the cart containing the items that you want to reprice.

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

`backgroundOperationId` The ID of the background operation that processes the total price of all items in the cart.

Error Conditions

**Error Condition** **Description**

Invalid CartId Input
The cart ID value isn’t accepted.

Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 500

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

User Doesn’t Have
The buyer doesn’t own the cart, doesn’t have read access to the cart, or the cart isn’t shared with the buyer.
Access to the Cart
Error Code: BAD_REQUEST

HTTP Status Code: 400

Cart Isn’t in the
The cart status isn’t in the Checkout state and can’t continue.
Checkout State


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

Error Code: INVALID_OPERATION

HTTP Status Code: 403

Integration Is Already
Only one integration can be processed at a time. This error indicates when an integration is already running.
in Progress
Error Code: ALREADY_IN_PROCESS

HTTP Status Code: 400

Account Associated
The effective account listed isn’t valid.
With the Cart Isn’t
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Valid or Accessible

HTTP Status Code: 500

User Isn’t a Member of
The user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 500

Usage

[This action is executed asynchronously using the pricing service configured in StoreIntegratedService.](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_storeintegratedservice.htm)

SEE ALSO:

Add and Edit Elements

Flow Core Action for Checkout Flow: Update Checkout Session Action

The Update Checkout Session action updates the checkout session state if the current state matches
the expected state. This action provides consistency during checkout handling and guarantees that
if two browsers attempt to update the state, one succeeds and the other fails validation.

In Flow Builder, add an Action element to your flow. Select the **B2B Commerce** category, and
###### search for Update Checkout Session Action . To access this action from the API, use the name

`updateCheckoutSessionAction` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`checkoutSessionId` The ID of the checkout session.

EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions with B2B Commerce

```
nextState

```

The state the session moves to after it completes the tasks included in the current state.

This input is an Apex-defined variable of enum `CheckoutStateEnum` .


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
expCurrentState

```

Store Output Values

The current state of the session.

This input is an Apex-defined variable of enum `CheckoutStateEnum` .

**Output Parameter** **Description**

`requestId` The ID of the request that processes and then either creates or returns the Checkout Session.

Error Conditions

**Error Condition** **Description**

Expected Validation
Error

The current state of the checkout session, identified by `checkoutSessionId` parameter, doesn’t match
the `expectedState` parameter, so the validation fails.

HTTP Status Code: 4XX

Invalid Checkout
Invalid input for the Checkout Session ID.
Session ID
Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 403

Invalid Session or
Either the session doesn’t exist or the user doesn’t have the required permissions.
Inadequate User
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Access

HTTP Status Code: 400

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

Account Associated
The effective account associated with the cart isn’t a valid account.
With Cart Is Invalid or
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Inaccessible

HTTP Status Code: 400

User Isn’t a Member of
The buyer user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

To use the B2B Commerce Update Checkout Session Action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The cart status isn’t set to `Closed` or `Processing` .

**•** The `CartcheckoutSession.IsProcessing` field is `false` .

SEE ALSO:

Add and Edit Elements

Commerce Checkout Flow Core Actions

The Commerce Checkout Flow provides several core actions for implementing a successful checkout
process within your Commerce org. To add one of these actions to your flow, add an Action element.
##### Then select the Commerce category, and search for the appropriate action. Cart actions aren’t

available in flows for B2B stores built on an Aura template.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex `ConnectApi` namespace. For more information on using Apex-defined variables in
flows, see Considerations for the Apex-Defined Data Type on page 260.

Flow Core Action for Commerce Checkout Flow: Add Cart Item
Add an item to a cart.

Flow Core Action for Commerce Checkout Flow: Create Cart
Create a cart.

Flow Core Action for Commerce Checkout Flow: Delete Cart
Delete a cart.

Flow Core Action for Commerce Checkout Flow: Get Cart Items
Get items in a cart.

Flow Core Action for Commerce Checkout Flow: Get Cart Promotions
Get promotions associated with a cart.

Flow Core Action for Commerce Checkout Flow: Add Cart Item

Add an item to a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

##### In Flow Builder, add an Action element to your flow. Select the Commerce category, and search
###### for Add Cart Item . To access this action from REST API, use the name addCartItem .


EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Cart State or` ID of the cart or state of the cart to add an item to. Valid state values are: _`active`_ and _`current`_ . A current
`ID` cart is not closed or pending deletion.

`effectiveAccountId` (Optional) ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
default value is determined from context.

`Web Store ID` The ID of the web store.

`Cart Item` [This input is an Apex-defined variable of class ConnectApi.CartItemInput, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_cart_item.htm)

```
   Input
```

**•** `productId`            - ID of the product.

**•** `quantity`            - Quantity of the cart item. Use a value that can be converted to BigDecimal.

**•** `type`            - Type of the cart item. The only valid value is _`Product`_ .

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Added Cart` [This output is an Apex-defined variable of class ConnectApi.CartItem, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_cart_item.htm)

```
   Item
```

**•** `itemizedAdjustmentAmount`            - Total itemized adjustment amount for the item, including
promotions and excluding taxes.

**•** `listPrice`            - List price for the item.

**•** `salesPrice`            - Sales price for the item.

**•** `totalAdjustmentAmount`            - Adjustments made to the unit price for the item. This value is
informational only and isn’t used in pricing calculations.

**•** `totalAmount`            - Total amount for the item.

**•** `totalListPrice`            - Total list price for the item.

**•** `totalPrice`            - Total price for the item including adjustments but excluding taxes.

**•** `totalTax`            - Total tax for the item.

**•** `unitAdjustedPrice`            - Unit price, including adjustments, for the item. This value is informational
only and isn’t used in pricing calculations.

**•** `unitAdjustmentAmount`            - Total amount including discounts, but excluding shipping and tax, for
product items in the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to the cart.
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400

Flow Core Action for Commerce Checkout Flow: Create Cart

Create a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Create Cart . To access this action from REST API, use the name createCart .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Web Store ID` The ID of the web store.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Cart Input` [This input is an Apex-defined variable of class ConnectApi.CartInput, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_cart.htm)

**•** `effectiveAccountId`         - (Optional) ID of the buyer account or guest buyer profile for which the
request is made. If unspecified, the default value is determined from context.

**•** `isSecondary`         - (Optional) Specifies whether the cart is secondary ( _`true`_ ) or not ( _`false`_ ). If
unspecified, defaults to _`false`_ .

**•** `name`         - (Optional) Name of the cart. The name can have up to 250 Unicode characters. If unspecified,
defaults to the generated name.

**•** `type`         - (Optional) Type of cart. The only valid value is _`Cart`_ . If unspecified, defaults to _`Cart`_ .

Store Output Values

Use output values later in the flow. The values are assigned when the cart is created.

**Output Parameter** **Description**

`Cart Summary` [This output is an Apex-defined variable of class ConnectApi.CartSummary, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_cart_summary.htm)

**•** `accountId`          - ID of the account for the cart.

**•** `cartId`          - ID of the cart.

**•** `currencyIsoCode`          - Three-letter ISO 4217 currency code associated with the cart.

**•** `grandTotalAmount`          - Grand total amount including shipping and tax for items in the cart, in the
currency of the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `isSecondary`            - Specifies whether the cart is secondary ( _`true`_ ) or not ( _`false`_ ).

**•** `name`            - Name of the cart.

**•** `purchaseOrderNumber`            - Purchase order for the cart.

**•** `status`            - Status of the cart. Possible values are:

**–** _`Active`_              - Cart is active.

**–** _`Checkout`_              - Cart is in checkout.

**–** _`Closed`_              - Cart is closed.

**–** _`PendingDelete`_              - Cart is pending deletion; for example, a user deleted the cart but the job hasn’t
completed yet.

**–** _`Processing`_              - Cart is processing.

**•** `totalChargeAmount`            - Total amount for shipping and other charges in the currency of the cart.

**•** `totalListPrice`            - Total list price for the cart.

**•** `totalProductAmount`            - Total amount including discounts, but excluding shipping and tax, for
product items in the cart.

**•** `totalProductAmountAfterAdjustments`            - Total product amount, including promotions.

**•** `totalProductCount`            - Total count of items in the cart.

**•** `totalPromotionalAdjustmentAmount`            - Total promotional adjustment amount for items in
the cart.

**•** `totalTaxAmount`            - Total tax amount for the cart, including tax on shipping, if applicable.

**•** `type`            - Type of cart. Value is always _`Cart`_ .

**•** `uniqueProductCount`            - Total count of unique items, or SKUs, in the cart.

**•** `webstoreId`            - ID of the web store of the cart.

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to create a cart. Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Commerce Checkout Flow: Delete Cart

Delete a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Delete Cart . To access this action from REST API, use the name deleteCart .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Cart State or` ID of the cart or state of the cart to delete. Valid state values are: _`active`_ and _`current`_ . A current cart is
`ID` neither closed nor pending deletion.

`effectiveAccountId` (Optional) ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
default value is determined from context.

`Web Store ID` ID of the web store associated with the cart.

Store Output Values

Output values aren’t available for this action.

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to the cart.
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400

Flow Core Action for Commerce Checkout Flow: Get Cart Items

Get items in a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Get Cart Items . To access this action from REST API, use the name getCartItems .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Cart ID` The ID of the cart owned by the user.

`Effective` (Optional) The ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
`Account ID` default value is determined from context.

`User ID` The ID of the buying user who owns the cart.

`Web Store ID` The ID of the store associated with the cart.

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Cart Items` [An Apex ConnectApi.CartItemCollection record that includes a collection of line items in a cart.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cart_item_collection.htm)

Error Conditions

**Error Condition** **Description**

A required parameter Error Message: You must specify a value for the {0} parameter. <!--Where 0 is the API name of the parameter
hasn't been specified. that requires input.-->

Error Code: REQUIRED_FIELD_MISSING

HTTP Status Code: 400

The specified ID is Error Message: Something's not right with the ID "{0}" specified for the {1} parameter. Check it and try again.
invalid. <!--Where 0 is the invalid ID, and 1 is the API name of the input parameter with the invalid ID.-->

Error Code: INVALID_INPUT

HTTP Status Code: 400

The specified effective Error Message: The ID "{0}" specified for the {1} parameter isn't a valid {2} record. <!--Where 0 is the specified
account ID is invalid ID, and 1 is the API name of the parameter with the specified ID, and 2 is the name of the valid record type.-->
for the account or
Error Code: INVALID_TYPE
guest buyer profile.

HTTP Status Code: 400

The specified store or
cart doesn’t exist.

Error Message: We couldn't find a record with the ID "{0}" specified for the {1} parameter. Check the record and
try again. <!--Where 0 is the ID of the record that doesn't exist, and 1 is the parameter that the ID was specified
for–>

Error Code: RECORD_NOT_FOUND

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Commerce Checkout Flow: Get Cart Promotions

Get promotions associated with a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Get Cart Promotions . To access this action from REST API, use the name

`getCartPromotions` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Cart ID` The ID of the cart owned by the user.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Effective` (Optional) The ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
`Account ID` default value is determined from context.

`User ID` The ID of the buying user who owns the cart.

`Web Store ID` The ID of the store associated with the cart.

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Cart` [An Apex ConnectApi.CartPromotionCollection record that includes a collection of line items in a cart.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cart_promotion_collection.htm)

```
Promotions

```

Error Conditions

**Error Condition** **Description**

A required parameter Error Message: You must specify a value for the {0} parameter. <!--Where 0 is the API name of the parameter
hasn't been specified. that requires input.-->

Error Code: REQUIRED_FIELD_MISSING

HTTP Status Code: 400

The specified ID is Error Message: Something's not right with the ID "{0}" specified for the {1} parameter. Check it and try again.
invalid. <!--Where 0 is the invalid ID, and 1 is the API name of the input parameter with the invalid ID.-->

Error Code: INVALID_INPUT

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

The specified effective Error Message: The ID "{0}" specified for the {1} parameter isn't a valid {2} record. <!--Where 0 is the specified
account ID is invalid ID, and 1 is the API name of the parameter with the specified ID, and 2 is the name of the valid record type.-->
for the account or
Error Code: INVALID_TYPE
guest buyer profile.

HTTP Status Code: 400

The specified store or
cart doesn’t exist.

Error Message: We couldn't find a record with the ID "{0}" specified for the {1} parameter. Check the record and
try again. <!--Where 0 is the ID of the record that doesn't exist, and 1 is the parameter that the ID was specified
for–>

Error Code: RECORD_NOT_FOUND

HTTP Status Code: 400

##### Salesforce Order Management Flow Core Actions

Salesforce Order Management provides several core actions for implementing order management
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the **Order Management** category, and search for the appropriate action.

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex ConnectApi namespace. For more information on using Apex-defined variables in flows,
see Considerations for the Apex-Defined Data Type on page 260.

Flow Core Action for Order Management: Add Order Item Summary
Add up to 100 order product summaries to an order summary. This action creates a change
order record, an order product record, and an order product summary record. It also creates
any supporting adjustment, tax, and summary records.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Flow Core Action for Order Management: Adjust Order Item Summaries Preview
Preview the expected results of adjusting the price of one or more order product summaries on an order summary, without executing
the adjustment. You can only apply a discount, not an increase. The output of this action contains the values that would be set on
the change orders created by submitting the proposed adjustment.

Flow Core Action for Order Management: Adjust Order Item Summaries Submit
Adjust the price of one or more order product summaries on an order summary. You can only apply a discount, not an increase. This
action creates one or more change order records.

Flow Core Action for Order Management: Authorize Payment
Authorize a payment on a credit card. You can include details for a new credit card or reference an existing PaymentMethod.

Flow Core Action for Order Management: Cancel Fulfillment Order Item
Cancel fulfillment order products from a fulfillment order. You can cancel more than one product and specify a quantity to cancel
for each of them. This action doesn’t cancel the associated order product summaries, it only reduces their allocated quantities.
Usually, you reallocate the canceled quantities to a new fulfillment order.

Flow Core Action for Order Management: Cancel Order Item Summaries Preview
Preview the expected results of canceling one or more order product summaries from an order summary without executing the
cancel. The output of this action contains the values that would be set on the change order created by submitting the proposed
cancel.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Cancel Order Item Summaries Submit
Cancel one or more order product summaries from an order summary. This action creates a change order record.

Flow Core Action for Order Management: Cancel Order Summary Preview
Preview the expected results of canceling all order product summaries for an order summary without executing the cancel. The
output of this action contains the values that would be set on the change order created by submitting the proposed cancel.

Flow Core Action for Order Management: Cancel Order Summary Submit
Cancel all order product summaries for an order summary. This action inserts a background operation into an asynchronous job
queue and returns the ID of that operation.

Flow Core Action for Order Management: Confirm Held Fulfillment Order Capacity
Confirm held fulfillment order capacity at one or more locations. This action decreases a location’s held capacity and increases its
assigned fulfillment order count. Confirm held capacity when you assign a fulfillment order to a location.

Flow Core Action for Order Management: Create Credit Memo
Create a credit memo to represent the refund for one or more change orders associated with an order summary.

Flow Core Action for Order Management: Create Fulfillment Order
Create one or more fulfillment orders and fulfillment order products for an order delivery group summary, which defines a recipient
and delivery method. You specify the order product summaries to fulfill and the fulfillment locations to handle them. If you specify
multiple fulfillment locations, a fulfillment order is created for each one.

Flow Core Action for Order Management: Create Fulfillment Orders
Create fulfillment orders and fulfillment order products for multiple order delivery group summaries, each of which defines a recipient
and delivery method. You specify the order product summaries to fulfill and the fulfillment locations to handle them. If you specify
multiple fulfillment locations for one order delivery group summary, a fulfillment order is created for each one.

Flow Core Action for Order Management: Create an Invoice from Change Orders
Create an invoice to represent the charges for one or more change orders. Create invoices for change orders that increase order
amounts, such as return fees. When you ensure the refund for a return, include the invoices for the associated return fees in the
input.

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order
Create an invoice for a fulfillment order that doesn’t have one.

Flow Core Action for Order Management: Create Order Payment Summary
Create an order payment summary for a payment authorization or payments that use the same payment method and are attached
to the same order summary.

Flow Core Action for Order Management: Create Order Summary
Create an order summary based on an order. That order is considered the original order for the order summary. Subsequent change
orders that apply to the order summary are also represented as order records.

Flow Core Action for Order Management: Create Return Order
Create a return order and return order items for order items belonging to an order summary. You can add return fees for any of the
order items.

Flow Core Action for Order Management: Ensure Funds Async
Ensure funds for an invoice, and apply them to it. If needed, capture authorized funds by sending a request to a payment provider.
This action inserts a background operation into an asynchronous job queue and returns the ID of that operation so you can track its
status. Payment gateway responses appear in the payment gateway log and don’t affect the background operation status.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Ensure Refunds Async
Ensure refunds for a credit memo or excess funds by sending a request to a payment provider. This action inserts a background
operation into an asynchronous job queue and returns the ID of that operation so you can track its status. Payment gateway responses
appear in the payment gateway log and don’t affect the background operation status.

Flow Core Action for Order Management: Find Routes with Fewest Splits
Evaluate ordered product quantities against available inventory to determine the smallest combination of locations that can fulfill
the order. If multiple combinations of the minimum number of locations can fulfill the order, the action returns multiple options.
Optionally, you can specify a maximum allowable number of locations. By default, the action executes up to 1,000,000 times, stopping
when it hits 10,000 results.

Flow Core Action for Order Management: Use OCI to Find Routes with Fewest Splits
Evaluate ordered product quantities against available inventory to determine the smallest combination of locations that can fulfill
the order. If multiple combinations of the minimum number of locations can fulfill the order, the action returns multiple options.
Optionally, you can specify a maximum allowable number of locations and a list of locations to exclude from the calculation. This
action combines the Omnichannel Inventory Get Availability action and the Order Management Find Routes with Fewest Splits
actions. Instead of calling Get Availability and including the output in the Find Routes with Fewest Splits input, call this action and
specify a location or location group to fulfill each ordered product. By default, this action executes up to 1,000,000 times, stopping
when it hits 10,000 results. This action handles the inventory check.

Flow Core Action for Order Management: Get Fulfillment Order Capacity Values
Get information about the current fulfillment order capacity of one or more locations.

Flow Core Action for Order Management: Hold Fulfillment Order Capacity
Hold capacity to process fulfillment orders at one or more locations. This action increases a location’s held capacity. Hold capacity
when you plan to assign a fulfillment order to a location.

Flow Core Action for Order Management: Order Routing Rank by Average Distance
Calculate the average distance from sets of inventory locations to an order recipient, and return the sets sorted by that average
distance. Use this action to compare the average shipping distances for different sets of locations that can fulfill an order.

Flow Core Action for Order Management: Release Held Fulfillment Order Capacity
Release held fulfillment order capacity at one or more locations. This action decreases a location’s held capacity without increasing
its assigned fulfillment order count. Release held capacity when you cancel assigning a fulfillment order to a location.

Flow Core Action for Order Management: Return Order Item Summaries Preview
Preview the expected results of a simple return of one or more order product summaries from an order summary without executing
the return. The output of this action contains the values that would be set on the change order created by submitting the proposed
return.

Flow Core Action for Order Management: Return Order Item Summaries Submit
Return one or more order product summaries from an order summary. This action is a simple return that creates a change order but
not a return order.

Flow Core Action for Order Management: Return Return Order Items
Process one or more return order line items belonging to a return order. This action creates a change order record for the returned
items and makes the processed return order line items read-only. You can include return order fees associated with the return order
line items. If you do, a change order record is created for the return fees. If a processed return order line item has a remaining expected
quantity, the action creates a separate return order line item representing that quantity.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Add Order Item Summary

Add up to 100 order product summaries to an order summary. This action creates a change order
record, an order product record, and an order product summary record. It also creates any supporting
adjustment, tax, and summary records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Add Order Item Summary .

Important: Don’t call this action via REST API. Use it only in flows.

Set Input Values

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Create record variables to use in the input. Use values from earlier in the flow to set their values.
The action generates records based on those values. Remember to include all required values for
each object type. For example, the order item summary record variable must include an order delivery group summary ID.

Note: For this action’s input values, use record variables, not existing records or record IDs.

**Input Parameter** **Description**

```
Order Item

Summary Input

```

Store Output Values

This input is an Apex-defined variable of class runtime_commerce_oms.AddOrderItemSummaries.

For information on setting up the input data, see the Usage section of this topic.

The variable has one field: `newItems` . This field is a list of one or more Apex-defined variables of class
runtime_commerce_oms.AddItem. Each of the variables includes these fields.

**•** `orderItemSummary` - An order product summary record variable representing the order product
to add.

**•** `reasonCode` - Reason for the addition. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

**•** `orderItemTaxLineItemSummaries` - A list of zero or more order product tax line item summary
record variables associated with the order product summary.

**•** `orderItemAdjustmentLineSummaries` - A list of zero or more Apex-defined variables of class
runtime_commerce_oms.AddItemAdjustment that has these fields.

**–** `orderItemAdjustmentLineSummary`  - An order product adjustment line summary record
variable associated with the order product being added.

**–** `orderItemTaxLineItemSummaries`  - A list of zero or more order product tax line item
summary record variables associated with the order product adjustment line summary.

**Output Parameter** **Description**

```
Order Item

Summary Output

```

This output is an Apex-defined variable of class ConnectApi.AddOrderItemSummaryOutputRepresentation. It
includes these fields.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `changeBalances` [— An Apex-defined variable of class ConnectApi.ChangeItemOutputRepresentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)
that has these fields.

**–** `grandTotalAmount`              - Change to the total with tax.

**–** `totalAdjDeliveryAmtWithTax`              - Change to the adjusted delivery subtotal, including tax.

**–** `totalAdjDistAmountWithTax`              - Change to the total order adjustments, including tax.

**–** `totalAdjProductAmtWithTax`              - Change to the adjusted product subtotal, including tax.

**–** `totalAdjustedDeliveryAmount`              - Change to the adjusted delivery subtotal.

**–** `totalAdjustedDeliveryTaxAmount`              - Change to the adjusted delivery subtotal tax.

**–** `totalAdjustedProductAmount`              - Change to the adjusted product subtotal.

**–** `totalAdjustedProductTaxAmount`              - Change to the adjusted product subtotal tax.

**–** `totalAdjustmentDistributedAmount`              - Change to the total order adjustments.

**–** `totalAdjustmentDistributedTaxAmount`              - Change to the total order adjustments tax.

**–** `totalAmount`              - Change to the pretax total.

**–** `totalExcessFundsAmount`              - The amount of excess funds available on the order payment
summaries related to the order summary. It’s equal to the captured amount that is owed as a refund
but isn’t associated with an invoice or credit memo. Excess funds normally occur when order products
are canceled before fulfillment but after payment has been captured. This situation isn’t common in
the US, where funds are normally authorized but not captured until the fulfillment process begins. This
value includes all excess funds related to the order summary, not only the funds related to the current
action.

**–** `totalRefundableAmount`              - The total amount available to be refunded. It’s the sum of the
excess funds and any outstanding change order grand total amounts that apply to post-fulfillment
changes. This value includes all refundable amounts related to the order summary, not only the amount
related to the current action.

**–** `totalRequiredFundsAmount`              - The total amount associated with the order products added
in the current action.

This amount isn’t necessarily the amount that must be captured. For example, in an even exchange
flow, the order amount reduction from canceling the exchanged products offsets the required funds
amount of the replacement products.

**–** `totalTaxAmount`              - Change to the total tax.

**•** `changeOrderId`            - ID of the change order generated by the action.

**•** `newItems`            - A list of one or more Apex-defined variables of class
ConnectApi.AddItemOutputRepresentation, each of which represents an added order product, and has
these fields.

**–** `id`              - ID of the order product summary.

**–** `name`              - Name of the order product summary.

**–** `orderItemAdjustmentLineSummaries`              - A list of zero or more Apex-defined variables of
class ConnectApi.AddItemAdjustmentOutputRepresentation, each of which represents an order product
adjustment line summary associated with the added order product summary, and has these fields.

**•** `id`               - ID of the order product adjustment line summary.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `name`               - Name of the order product adjustment line summary.

**•** `orderItemTaxLineItemSummaries`               - A list of zero or more Apex-defined variables of
class ConnectApi.AddItemTaxOutputRepresentation, each of which represents an order product
tax line item summary associated with the order product adjustment line summary, and has these
fields.

**–** `id`                 - ID of the order product tax line item summary.

**–** `name`                 - Name of the order product tax line item summary.

**–** `orderItemTaxLineItemSummaries`              - A list of zero or more Apex-defined variables of class
ConnectApi.AddItemTaxOutputRepresentation, each of which represents an order product tax line
item summary associated with the added order product summary, and has these fields.

**•** `id`               - ID of the order product tax line item summary.

**•** `name`               - Name of the order product tax line item summary.

**•** `orderSummaryId`            - ID of the order summary specified in the input.

To set up the Order Item Summary Input:

**1.** Use record variables to define the order product summaries, order product adjustment line summaries, and order product tax line
item summaries. Sending an Id isn’t required.

**•** Required fields for an order product summary:

**–** ListPrice (Only if Order Summary Pricebook2Id is NULL or empty)

**–** Name

**–** OrderDeliveryGroupSummaryId

**–** OrderSummaryId

**–** PricebookEntryId (Only if Order Summary Pricebook2Id is set)

**–** Product2Id

**–** Quantity

**–** TotalLineAmount

**–** UnitPrice

**–** TypeCode

**–** Type

**•** Required fields for an order product adjustment line summary:

**–** Amount

**–** Name

**–** OrderSummaryId

**•** Required fields for an order product tax line item summary:

**–** Amount

**–** Name

**–** OrderSummaryId


Automate Your Business Processes with Salesforce Flow Flow Reference

**–** TaxEffectiveDate

**–** Type

**2.** Use an assignment element to set the `orderItemSummary` field on a runtime_commerce_oms.AddItem variable to the order
product summary record variable.

**3.** For each adjustment to the product being added, use an assignment element to set the `orderItemAdjustmentLineSummary`
field on a runtime_commerce_oms.AddItemAdjustment variable to the corresponding order product adjustment line summary
record variable. Use assignment elements to add the order product tax line summary record variables associated with it to the
`orderItemTaxLineItemSummaries` field on the same runtime_commerce_oms.AddItemAdjustment variable.

**4.** Use an assignment element to add the runtime_commerce_oms.AddItemAdjustment variables to the
`orderItemAdjustmentLineSummaries` field on the runtime_commerce_oms.AddItem variable.

**5.** For each tax on the product being added, use an assignment element to add the corresponding order product tax line summary
record variable to the `orderItemTaxLineItemSummaries` field on the runtime_commerce_oms.AddItem variable.

**6.** Use an assignment element to set the `reasonCode` field on the runtime_commerce_oms.AddItem variable to a valid reason.

**7.** Use an assignment element to add the runtime_commerce_oms.AddItem variable to the `newItems` field on a
runtime_commerce_oms.AddOrderItemSummaries variable.

**8.** Repeat steps 1 through 6 for each order product that you want to include in the action, adding the inputs to the same
runtime_commerce_oms.AddOrderItemSummaries variable. You can add up to five order products at a time.

**9.** Use the runtime_commerce_oms.AddOrderItemSummaries variable in the action input.

Flow Core Action for Order Management: Adjust Order Item Summaries Preview

Preview the expected results of adjusting the price of one or more order product summaries on an
order summary, without executing the adjustment. You can only apply a discount, not an increase.
The output of this action contains the values that would be set on the change orders created by
submitting the proposed adjustment.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Adjust Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

`Order Summary` ID of the order summary associated with the order product summaries that you want to preview adjusting the
`Id` prices of.

###### Adjust Order This input is an Apex-defined variable of class ConnectApi.AdjustOrderItemSummaryInputRepresentation,

`Product` which includes these fields:

```
Summaries
```

**•** `adjustItems` —This field is a list of Apex-defined variables of class

`Input` [ConnectApi.AdjustItemInputRepresentation. Each of the variables includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_item.htm)

**–** `orderItemSummaryId` —ID of an order product summary to preview a price adjustment for.

**–** `description` —Optional description of the adjustment.

**–** `adjustmentType` —Specifies how to calculate the adjustment amount from the
`discountValue` field. It can have one of these values:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithTax`_ —The value of `discountValue` is the adjustment, including tax.

**•** _`AmountWithoutTax`_ —The value of `discountValue` is the adjustment, not including tax.
Tax is calculated on the value and added.

**•** _`Percentage`_ —The value of `discountValue` is a percentage discount. It’s divided by 100,
and then multiplied by the total price and total tax amount of the order product summary to
determine the adjustment amount.

**–** `discountValue` —The value used to calculate the adjustment amount, as specified by the
`adjustmentType` . It must be a negative value.

**–** `reason` —Adjustment reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `allocatedItemsChangeOrderType` —Specifies how change orders would be created for order
product summary quantities that are currently being fulfilled, defined as QuantityAllocated - QuantityFulfilled.
It can have one of these values:

**–** _`Disallowed`_ —When distributing the adjustment, ignore any quantities being fulfilled. If an order
product summary’s entire quantity is being fulfilled, return an error. This value is the default.

**–** _`InFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Submitting
the adjustment would create a separate change order for the adjustments made to those quantities.

**–** _`PreFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Submitting
the adjustment would include the adjustments made to those quantities in the change order for
pre-fulfillment quantity adjustments.

Store Output Values

Use output values later in the flow.

**Output Parameter** **Description**

```
Adjust Order

Product

Summary Output

```

[This output is an Apex-defined variable of class ConnectApi.AdjustOrderSummaryOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_adjust_output.htm)
contains the financial changes that would result from the proposed adjustment. Most of the values represent
the deltas of the values on the associated order summary.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment has been captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `postFulfillmentChangeOrderId` field is always null for a preview action.

The `preFulfillmentChangeOrderId` field is always null for a preview action.

The `inFulfillmentChangeOrderId` field is always null for a preview action.

Usage

When a price adjustment is applied to an order product summary, its quantities are considered in three groups:

**•** Pre-fulfillment—QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**•** In-fulfillment—QuantityAllocated - QuantityFulfilled

**•** Post-fulfillment—QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the `allocatedItemsChangeOrderType`
input property:

**•** Distribute the adjustment evenly between pre-fulfillment and post-fulfillment quantities. Ignore in-fulfillment quantities. Submitting
the adjustment would create one change order for the adjustments to pre-fulfillment quantities and one change order for the
adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Submitting the adjustment
would create one change order for the adjustments to both pre-fulfillment and in-fulfillment quantities, and one change order for
the adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Submitting the adjustment
would create one change order for the adjustments to pre-fulfillment quantities, one change order for the adjustments to in-fulfillment
quantities, and one change order for the adjustments to post-fulfillment quantities.

To set up the Adjust Order Product Summaries Input:

**•** Use Assignment elements to set the `orderItemSummaryId`, `description`, `adjustmentType`, `discountValue`,
and `reason` field values on one or more `ConnectApi.AdjustItemInputRepresentation` variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Use an Assignment element to add the `ConnectApi.AdjustItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use an Assignment element to set the `allocatedItemsChangeOrderType` field on the
`ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use the `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable and the order summary ID in
the action input.

In a flow for adjusting the prices of order product summaries, display the output of this action for the user to review before executing
the adjustment. When the user verifies the expected results, pass the same input to an Adjust Order Item Summaries Submit action.

SEE ALSO:

Flow Core Action for Order Management: Adjust Order Item Summaries Submit

Add and Edit Elements

Flow Core Action for Order Management: Adjust Order Item Summaries Submit

Adjust the price of one or more order product summaries on an order summary. You can only apply
a discount, not an increase. This action creates one or more change order records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Adjust Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` ID of the order summary associated with the order product summaries that you
`Summary` want to adjust the prices of.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Adjust`

```
Order

Product

Summaries

Input

```

This input is an Apex-defined variable of class
[ConnectApi.AdjustOrderItemSummaryInputRepresentation, which includes these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_order_item_summary.htm)
fields:

**•** `adjustItems` —This field is a list of Apex-defined variables of class
[ConnectApi.AdjustItemInputRepresentation. Each of the variables includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_item.htm)
these fields:

**–** `orderItemSummaryId` —ID of an order product summary to adjust
the price of.

**–** `description` —Optional description of the adjustment.

**–** `adjustmentType` —Specifies how to calculate the adjustment
amount from the `discountValue` field. It can have one of these
values:

**•** _`AmountWithTax`_ —The value of `discountValue` is the
adjustment, including tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithoutTax`_ —The value of `discountValue` is the adjustment, not including tax.
Tax is calculated on the value and added.

**•** _`Percentage`_ —The value of `discountValue` is a percentage discount. It’s divided by 100,
and then multiplied by the total price and total tax amount of the order product summary to
determine the adjustment amount.

**–** `discountValue` —The value used to calculate the adjustment amount, as specified by the
`adjustmentType` . It must be a negative value.

**–** `reason`              - Adjustment reason.The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `allocatedItemsChangeOrderType` —Specifies how to create change orders for order product
summary quantities that are currently being fulfilled, defined as QuantityAllocated - QuantityFulfilled. It can
have one of these values:

**–** _`Disallowed`_ —When distributing the adjustment, ignore any quantities being fulfilled. If an order
product summary’s entire quantity is being fulfilled, return an error. This value is the default.

**–** _`InFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Create a
separate change order for the adjustments made to those quantities.

**–** _`PreFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Include
the adjustments made to those quantities in the change order for pre-fulfillment quantity adjustments.

Store Output Values

Use output values later in the flow. The values are assigned when the change orders are created.

**Output Parameter** **Description**

`Adjust Order` [This output is an Apex-defined variable of class ConnectApi.AdjustOrderSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_adjust_output.htm)
`Product` Depending on the order product summaries included in the adjustment, one or more change orders are
`Summary Output` generated. If multiple change orders are generated, then the `changeBalances` values combine the values
from both of them.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment has been captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `postFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that have been fulfilled.

The `preFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that haven’t been fulfilled. If the input
specified an `allocatedItemsChangeOrderType` of _`PreFulfillment`_, this change order also
includes the changes applicable to order product summary quantities that are in the process of being fulfilled.

The `inFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that are in the process of being fulfilled.
This change order is only created for an input that specified an `allocatedItemsChangeOrderType`
of _`InFulfillment`_ .

Usage

When a price adjustment is applied to an order product summary, its quantities are considered in three groups:

**•** Pre-fulfillment—QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**•** In-fulfillment—QuantityAllocated - QuantityFulfilled

**•** Post-fulfillment—QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the `allocatedItemsChangeOrderType`
input property:

**•** Distribute the adjustment evenly between pre-fulfillment and post-fulfillment quantities. Ignore in-fulfillment quantities. Create one
change order for the adjustments to pre-fulfillment quantities and one change order for the adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to both pre-fulfillment and in-fulfillment quantities, and one change order for the adjustments to post-fulfillment
quantities.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to pre-fulfillment quantities, one change order for the adjustments to in-fulfillment quantities, and one change
order for the adjustments to post-fulfillment quantities.

To set up the Adjust Order Product Summaries Input:

**•** Use Assignment elements to set the `orderItemSummaryId`, `description`, `adjustmentType`, `discountValue`,
and `reason` field values on one or more `ConnectApi.AdjustItemInputRepresentation` variables.

**•** Use an Assignment element to add the `ConnectApi.AdjustItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use an Assignment element to set the `allocatedItemsChangeOrderType` field on the
`ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use the `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable and the order summary ID in
the action input.

In a flow for adjusting the prices of order product summaries, run an Adjust Order Item Summaries Preview action before running this
action. Then display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

After submitting a price adjustment, process refunds as appropriate:

**•** If the discount only applied to order product summaries for which payment hasn’t been captured, it doesn’t require a refund. This
situation normally applies to order products in the US that haven’t been fulfilled.

**•** If the discount applied to order product summaries that haven’t been fulfilled and for which payment has been captured, process
a refund. In this case, pass the `totalExcessFundsAmount` from `changeBalances` to the Ensure Refunds Async action.

**•** If the discount applied to order product summaries that have been fulfilled, process a refund. Pass the
`postFulfillmentChangeOrderId` to the Create Credit Memo action, then pass the credit memo to the Ensure Refunds
Async action.

**•** If the discount applied to both fulfilled and unfulfilled order product summaries for which payment has been captured, process both
refunds. Pass the `postFulfillmentChangeOrderId` to the Create Credit Memo action, then pass the credit memo and
the `totalExcessFundsAmount` from `changeBalances` to the Ensure Refunds Async action.

Important: Excess funds aren’t reduced until the payment processor issues a refund. If you don’t process refunds promptly,
subsequent refunds can be inaccurate. Consider this example.

**•** An order with a total amount of $100 is placed, and the amount is captured immediately.

**•** A product is canceled from the order, resulting in $20 of excess funds.

**•** Before the excess funds are sent to the payment provider in an ensure refunds action, another product is canceled. This
cancellation adds another $20 of excess funds. However, because the original $20 hasn’t been refunded yet, the cancel action
returns a total excess funds amount of $40.

**•** The first excess funds amount ($20) is sent to the payment provider in an ensure refunds request.

**•** The second excess funds amount ($40) is sent to the payment provider in an ensure refunds request.

**•** The payment provider receives requests for $60 of refunds, when the correct refund total is $40. Because the total refund
amount is less than the total captured amount of $100, the payment provider issues $60 in refunds.

SEE ALSO:

Flow Core Action for Order Management: Adjust Order Item Summaries Preview

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Authorize Payment

Authorize a payment on a credit card. You can include details for a new credit card or reference an
existing PaymentMethod.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Authorize Payment . To access this action from REST API, use the name

`authorizePayment` .

Note: This action is available with the PaymentsAPIUser user permission.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

`Payment` [This input is an Apex-defined variable of class ConnectApi.AuthorizationRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_authorization.htm)

```
Authorization
```

**•** `accountId` —ID of the account that contains the payment transaction being authorized.
```
Request

```

**•** `accountId` —ID of the account that contains the payment transaction being authorized.

**•** `amount` —Authorization amount.

**•** `comments` —(Optional) Comments for the payment authorization.

**•** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group record.

**•** `effectiveDate` —Date that the authorization is applied to the transaction.

**•** `paymentGatewayId` —Payment gateway that processes the authorization.

**•** `paymentGroup` —(Optional) Payment group for the authorization. The payload must reference either
a paymentGroup or a paymentGroupId, but not both. This field is an Apex-defined variable of class
[ConnectApi.PaymentGroupRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_payment_group.htm)

**–** `createPaymentGroup` —(Optional) Specifies whether to create a payment group ( _`true`_ ) or not
( _`false`_ ).

**–** `currencyIsoCode` —(Optional) Three-letter ISO 4217 currency code associated with the payment
group record.

**–** `id` —(Optional) ID of the payment group record.

**–** `sourceObjectId` —(Optional) Source object ID of the payment group record. Supports only OrderId.

**•** `paymentMethod` —Payment method for the authorization. The payload must either reference an
existing payment method or include details for a new payment method, but not both. This field is an
[Apex-defined variable of class ConnectApi.AuthApiPaymentMethodRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_auth_api_payment_method.htm)

[This input includes the fields from the parent class, ConnectApi.BaseApiPaymentMethodRequest.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_base_api_payment_method.htm)

**–** `address` —Address for the payment method. This field is an Apex-defined variable of class
[ConnectApi.AddressRequest. It includes these fields, all of which are optional:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_address.htm)

**•** `city`

**•** `companyName`

**•** `country`

**•** `postalCode`

**•** `state`

**•** `street`


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `cardPaymentMethod` —(Optional) When using a new payment method, the details of that method.
[This field is an Apex-defined variable of class ConnectApi.CardPaymentMethodRequest, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_card_payment_method.htm)
these fields:

**•** `accountId` —Salesforce account to which this payment method is linked.

**•** `cardCategory` —Valid values are _`CreditCard`_ and _`DebitCard`_ .

**•** `cardHolderFirstName` —First name of the card holder.

**•** `cardHolderLastName` —Last name of the card holder.

**•** `cardHolderName` —Full name of the card holder.

**•** `cardNumber` —Card number.

**•** `cardType` —Valid values are:

**–** _`AmericanExpress`_

**–** _`DinersClub`_

**–** _`JCB`_

**–** _`Maestro`_

**–** _`MasterCard`_

**–** _`Visa`_

**•** `comments` —(Optional) Comments for the payment method.

**•** `cvv` —CVV.

**•** `email` —Email of the card holder.

**•** `expiryMonth` —Card expiration month.

**•** `expiryYear` —Card expiration year.

**•** `nickName` —(Optional) Nickname for the payment method.

**•** `startMonth` —(Optional) Start month of the card.

**•** `startYear` —(Optional) Start year of the card.

**–** `id` —(Optional) When using an existing payment method, the ID of that method.

**–** `saveForFuture` —Whether to save the payment method for future use.

Store Output Values

Use output values later in the flow. The values are assigned when a response is received from the payment gateway.

**Output Parameter** **Description**

`Payment` [This output is an Apex-defined variable of class ConnectApi.AuthorizationResponse, which includes these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_authorization_output.htm)
`Authorization` fields:

```
   Response
```

**•** `error` —If an error is returned, details about that error. This field is an Apex-defined variable of class
[ConnectApi.ErrorResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)

**–** `errorCode` —Error code.

**–** `message` —More detail, if available.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `gatewayResponse` —Response from the payment gateway. This field is an Apex-defined variable of
[class ConnectApi.AuthorizationGatewayResponse, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_authorization_gateway_response.htm)

**–** `gatewayAuthorizationCode` —Payment authorization code.

**•** `paymentAuthorization` —Details about the payment authorization. This field is an Apex-defined
[variable of class ConnectApi.PaymentAuthorizationResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_authorization_output.htm)

**–** `accountId` —ID of the account that contains the payment transaction being authorized.

**–** `amount` —Amount that the gateway authorized for the payment transaction.

**–** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group
record.

**–** `effectiveDate` —Date that the authorization becomes effective.

**–** `expirationDate` —Date that the authorization expires.

**–** `id` —ID of the payment authorization record.

**–** `paymentAuthorizationNumber` —System-defined number for the payment authorization
record.

**–** `requestDate` —Date that the authorization occurred.

**–** `status` —Status of the payment authorization as returned by the gateway.

**•** `paymentGatewayLogs` —Payment gateway log information about the authorization transaction.
[This field is a list of Apex-defined variables of class ConnectApi.GatewayLogResponse, each of which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_gateway_log_output.htm)
includes these fields:

**–** `createdDate` —Date when the gateway log was created.

**–** `gatewayResultCode` —Result codes that show the status of a transaction as it is passed to the
financial institution and then returned to the client.

**–** `id` —ID of the gateway log record.

**–** `interactionStatus` —Gateway interaction status. It can be `SUCCESS`, `FAILED`, or `TIMEOUT` .

**•** `paymentGroup` —Details about the payment group. This field is an Apex-defined variable of class
[ConnectApi.PaymentGroupResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_group.htm)

**–** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group
record.

**–** `id` —ID of the payment group record.

**–** `sourceObjectId` —Source object ID of the payment group record.

**•** `paymentMethod` —Details about the payment method. This field is an Apex-defined variable of class
[ConnectApi.PaymentMethodResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_method_output.htm)

**–** `accountId` —ID of the account for the payment method.

**–** `id` —ID of the payment method.

**–** `status` —Status of the payment method.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

Use this action in custom flows that require payment authorization, such as adding an item to an order or an uneven exchange. Before
using it, verify with your payment provider that it supports payment authorization calls from Salesforce Order Management.

Flow Core Action for Order Management: Cancel Fulfillment Order Item

Cancel fulfillment order products from a fulfillment order. You can cancel more than one product
and specify a quantity to cancel for each of them. This action doesn’t cancel the associated order
product summaries, it only reduces their allocated quantities. Usually, you reallocate the canceled
quantities to a new fulfillment order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Fulfillment Order Item .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Cancel`

```
Fulfillment

Order Items

Input

```

[This input is an Apex-defined variable of class ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order_line_items_to_cancel.htm)

The variable has one field, `fulfillmentOrderLineItemsToCancel`, which is a list of Apex-defined
[variables of class ConnectApi.FulfillmentOrderLineItemInputRepresentation. Each of those variables includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order_line_item.htm)
these fields:

**•** `fulfillmentOrderLineItemId` - Reference to the fulfillment order product to cancel.

**•** `quantity` - Quantity to cancel.

`Fulfillment` Reference to the fulfillment order that you want to cancel fulfillment order items from.

```
Order Id

```

Store Output Values

**Output Parameter** **Description**

###### `Cancel`

```
Fulfillment

Order Items

Output

```

Usage

This value is an Apex-defined variable of class
[ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_cancel_line_items_output.htm)

This action doesn’t return any data.

To set up the Cancel Fulfillment Order Items Input, first use Assignment elements to set the `fulfillmentOrderLineItemId`
and `quantity` field values on one or more `ConnectApi.FulfillmentOrderLineItemInputRepresentation`
variables. Then use an Assignment element to add those variables to the `FulfillmentOrderLineItemsToCancel` field on


Automate Your Business Processes with Salesforce Flow Flow Reference

a `ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation` variable. Use that variable in the
action input.

SEE ALSO:

Add and Edit Elements

Add and Edit Elements

Flow Core Action for Order Management: Cancel Order Item Summaries Preview

Preview the expected results of canceling one or more order product summaries from an order
summary without executing the cancel. The output of this action contains the values that would
be set on the change order created by submitting the proposed cancel.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Cancel`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not
including tax. Tax is calculated on the value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is
`amount` divided by 100 and then multiplied by the `TotalPrice`
and `TotalTaxAmount` of the associated order product summary,
prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount
is `amount` divided by 100 and then multiplied by the
`TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to cancel. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to cancel.

**•** `reason` —Required. Cancel reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

`Order Summary` Reference to the order summary that you want to preview canceling order product summaries from.

```
   Id

```

Store Output Values

**Output Parameter** **Description**

```
Cancel Order

Product

Summary Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed cancel.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Cancel Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for canceling order product summaries, display the output of this action for the user to review before executing the cancel.
When the user verifies the expected results, pass the same input to a Cancel Order Item Summaries Submit action.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Cancel Order Item Summaries Submit

Cancel one or more order product summaries from an order summary. This action creates a change
order record.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Cancel Order

Product

Summary Items

Input

```

[This input is an Apex-defined variable of class ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemInputRepresentation. Each variable includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)

**–** `amount` —Required. Value used to calculate the fee amount, as described by the amountType. It must
be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated. It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not including tax. Tax is calculated on the
value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is `amount` divided by 100 and then
multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated order product
summary, prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount is `amount` divided by 100
and then multiplied by the `TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to cancel. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to cancel.

**•** `reason` —Required. Cancel reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

`Order Summary` Reference to the order summary that you want to cancel order product summaries from.

```
Id

```

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Cancel Order

Product

Summary Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.SubmitCancelOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_submit_cancel_output.htm)

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `changeOrderId` field is the ID of the change order record created for the canceled items. Use this
change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for any cancel fees. Use this
change order to create an invoice.

To set up the Cancel Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for canceling order product summaries, run a Cancel Order Item Summaries Preview action before running the action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

SEE ALSO:

Flow Core Action for Order Management: Cancel Order Item Summaries Preview

Add and Edit Elements

###### Flow Core Action for Order Management: Cancel Order Summary Preview

Preview the expected results of canceling all order product summaries for an order summary without
executing the cancel. The output of this action contains the values that would be set on the change
order created by submitting the proposed cancel.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Cancel Order Summary Preview** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Cancel

All Order

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CancelAllOrderItemsInputRepresentation, which contains details](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_cancel_all_order_items.htm)
about the order summary to preview canceling all order products for.

The `changeItemFees` field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeWithTaxInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_change_item_fee_with_tax.htm)
includes these fields:

**•** `amount` —Positive value used to calculate the fee amount.

**•** `changeItemFees` —List of taxes associated with the change item fees.

**•** `description` —Description of the fee.

**•** `orderDeliveryGroupSummaryId` —ID of the order delivery group
summary.

**•** `priceBookEntryId` —ID of the price book entry associated with the
fee product.

**•** `product2Id` —ID of the product representing the fee.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `reason` —Reason for the cancellation. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

The `excludedItems` field is a list of items to exclude from the cancellation preview.

The `orderSummaryId` field is the ID of the order summary to preview canceling all order products summaries
for.

The `reason` field is the reason for the cancellation. The value must match one of the picklist values on the
Reason field of the Order Product Summary Change object.

The `reasonText` field is the reason text used for the return insights. The value has a max of 255 characters.

Store Output Values

**Output Parameter** **Description**

```
Preview Cancel

Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed cancel.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Cancel All Order Items Input:

**1.** Use Assignment elements to set the `amount`, `amountType`, `changeItemFees`, `description`,
`orderDeliveryGroupSummaryId`, `priceBookEntryId`, `product2Id`, and `reason` field values on one or more
`ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables.

**2.** Use an Assignment element to add the `ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables to
the `changeItemFees` field on a `ConnectApi.CancelAllOrderItemsInputRepresentation` variable.

**3.** Use the `ConnectApi.CancelAllOrderItemsInputRepresentation` variable and the order summary ID in the
action input.

In a flow for canceling all product summaries for an order, display the output of this action for the user to review before executing the
cancel. When the user verifies the expected results, pass the same input to a Cancel Order Summary Submit action.

###### Flow Core Action for Order Management: Cancel Order Summary Submit

Cancel all order product summaries for an order summary. This action inserts a background operation
into an asynchronous job queue and returns the ID of that operation.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Cancel Order Summary Submit** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Cancel

All Order

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CancelAllOrderItemsInputRepresentation, which contains details](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_cancel_all_order_items.htm)
about the order summary to preview canceling all order products for.

The `changeItemFees` field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeWithTaxInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_change_item_fee_with_tax.htm)
includes these fields:

**•** `amount` —Positive value used to calculate the fee amount.

**•** `changeItemFees` —List of taxes associated with the change item fees.

**•** `description` —Description of the fee.

**•** `orderDeliveryGroupSummaryId` —ID of the order delivery group
summary.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `priceBookEntryId` —ID of the price book entry associated with the fee product.

**•** `product2Id` —ID of the product representing the fee.

**•** `reason` —Reason for the cancellation. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

The `excludedItems` field is a list of items to exclude from the cancellation preview.

The `orderSummaryId` field is the ID of the order summary to preview canceling all order products summaries
for.

The `reason` field is the reason for the cancellation. The value must match one of the picklist values on the
Reason field of the Order Product Summary Change object.

The `reasonText` field is the reason text used for the return insights. The value has a max of 255 characters.

Store Output Values

**Output Parameter** **Description**

`Cancel All` [This output is an Apex-defined variable of class ConnectApi.CancelAllOrderItemsAsyncOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cancel_all_order_items_async_output.htm)
`Order Items` which contains the ID of the asynchronous background operation.

```
   Async Output

```

Usage

To set up the Cancel All Order Items Input:

**1.** Use Assignment elements to set the `amount`, `amountType`, `changeItemFees`, `description`,
`orderDeliveryGroupSummaryId`, `priceBookEntryId`, `product2Id`, and `reason` field values on one or more
`ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables.

**2.** Use an Assignment element to add the `ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables to
the `changeItemFees` field on a `ConnectApi.CancelAllOrderItemsInputRepresentation` variable.

**3.** Use the `ConnectApi.CancelAllOrderItemsInputRepresentation` variable and the order summary ID in the
action input.

In a flow for canceling all product summaries for an order, run a Cancel Order Summary Preview action before running this action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action. When the action
completes, it generates OSAsyncChgCompletedEvent if successful and ProcessExceptionEvent if not.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Confirm Held Fulfillment Order Capacity

Confirm held fulfillment order capacity at one or more locations. This action decreases a location’s
held capacity and increases its assigned fulfillment order count. Confirm held capacity when you
assign a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Confirm Held Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.ConfirmHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_confirm_held_f_o_capacity_request.htm)
these fields:

###### Confirm This input is an Apex-defined variable of class

`Held` [ConnectApi.ConfirmHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_confirm_held_f_o_capacity_request.htm)
`Fulfillment` these fields:

```
Order
```

**•** `allOrNothing` —(Optional) Controls whether a single failed request
```
Capacity
```
cancels all other requests in the list ( _`true`_ ) or some requests can succeed
```
Input
```
if others fail ( _`false`_ ). The default value is _`false`_ .

```
Capacity

Input

```

**•** `capacityRequests` —This field is a list of Apex-defined variables of
[class ConnectApi.CapacityRequestInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
represents a request to confirm one fulfillment order assigned to one location,
and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can
be a UUID. To identify which requests succeeded or failed, use the action
request IDs in response data.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.

**Output Parameter** **Description**

###### Confirm Held This output is an Apex-defined variable of class

`Fulfillment` [ConnectApi.ConfirmHeldFOCapacityResponseOutputRepresentation, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_confirm_held_f_o_capacity_response_output.htm)

```
Order Capacity
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class

`Output` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Credit Memo

Create a credit memo to represent the refund for one or more change orders associated with an
order summary.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Credit Memo .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Credit

Memo

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CreateCreditMemoInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_credit_memo.htm)

The variable has one field, `changeOrderIds`, which is a list of IDs of the
change orders to create a credit memo for.

`Order` Reference to the order summary associated with the change orders.

```
Summary

Id

```

Store Output Values

**Output Parameter** **Description**

```
Credit Memo

Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.CreateCreditMemoOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_create_credit_memo_output.htm)

The `creditMemoId` field contains the ID of the created credit memo.

To set up the Credit Memo Input, first use Assignment elements to add the change order IDs to a list of strings variable. Then use that
variable in the action input.

SEE ALSO:

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Fulfillment Order

Create one or more fulfillment orders and fulfillment order products for an order delivery group
summary, which defines a recipient and delivery method. You specify the order product summaries
to fulfill and the fulfillment locations to handle them. If you specify multiple fulfillment locations, a
fulfillment order is created for each one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Fulfillment Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Fulfillment

Order

Input

```

This input is an Apex-defined variable of class
[ConnectApi.FulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)

The variable has three fields:

**•** `fulfillmentGroups` - A list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupInputRepresentation. A fulfillment order is](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
created for each fulfillment group. A group represents a set of order product
summaries to fulfill from a single location, using the same fulfillment type.
Each fulfillment group variable has these fields:

**–** `fulfilledFromLocationId`  - Reference to the fulfillment
location.

**–** `fulfillmentType`  - The fulfillment type. Specify one of the values
that you defined for the `Type` field picklist on the Fulfillment Order
object.

**–** `orderItemSummaries`  - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)
these fields:

**•** `orderItemSummaryId`    - Reference to an order product
summary.

**•** `quantity`    - The quantity of the order product summary to
allocate to the fulfillment order.

**–** `referenceId`  - Reference to the fulfillment group input. This action
doesn’t use this value.

**•** `orderDeliveryGroupSummaryId` - Reference to the order delivery
group summary associated with the order product summaries.

**•** `orderSummaryId` - Reference to the order summary associated with
the order product summaries.

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Fulfillment

Order Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.FulfillmentOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_output.htm)

The `fulfillmentOrderIds` field is a list of IDs of the created fulfillment orders.

To set up the Fulfillment Order Input:

**1.** Use Assignment elements to set the `orderItemSummaryId` and `quantity` field values on one or more
`ConnectApi.OrderItemSummaryInputRepresentation` variables for each fulfillment group.

**2.** Use Assignment elements to add the `ConnectApi.OrderItemSummaryInputRepresentation` variables to the
`orderItemSummaries` fields on one or more `ConnectApi.FulfillmentGroupInputRepresentation` variables,
one for each fulfillment group.

**3.** Use Assignment elements to set the `fulfilledFromLocationId` and `fulfillmentType` field values on the fulfillment
group variables.

**4.** Use Assignment elements to add the fulfillment group variables to the `fulfillmentGroups` field on a
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**5.** Use Assignment elements to set the `orderDeliveryGroupSummaryId` and `orderSummaryId` field values on the
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**6.** Use the `ConnectApi.FulfillmentOrderInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Create Fulfillment Orders

Create fulfillment orders and fulfillment order products for multiple order delivery group summaries,
each of which defines a recipient and delivery method. You specify the order product summaries
to fulfill and the fulfillment locations to handle them. If you specify multiple fulfillment locations
for one order delivery group summary, a fulfillment order is created for each one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Fulfillment Orders .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Fulfillment

Orders

Input

```

This input is an Apex-defined variable of class
[ConnectApi.MultipleFulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_multiple_fulfillment_order.htm)

The variable has one field: `fulfillmentOrders` . This field is a list of
[Apex-defined variables of class ConnectApi.FulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
Each variable has three fields:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `fulfillmentGroups`            - A list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupInputRepresentation. A fulfillment order is created for each fulfillment group.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
A group represents a set of order product summaries to fulfill from a single location using the same fulfillment
type. Each fulfillment group variable has these fields:

**–** `fulfilledFromLocationId`              - Reference to the fulfillment location.

**–** `fulfillmentType`              - The fulfillment type. Specify one of the values that you defined for the
`Type` field picklist on the Fulfillment Order object.

**–** `orderItemSummaries`              - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)

**•** `orderItemSummaryId`               - Reference to an order product summary.

**•** `quantity`               - The quantity of the order product summary to allocate to the fulfillment order.

**–** `referenceId`              - Reference to the fulfillment group input. Use this value to troubleshoot a failure.

**•** `orderDeliveryGroupSummaryId`            - Reference to the order delivery group summary associated
with the order product summaries.

**•** `orderSummaryId`            - Reference to the order summary associated with the order product summaries.

Store Output Values

**Output Parameter** **Description**

```
Fulfillment

Orders Output

```

[This value is an Apex-defined variable of class ConnectApi.MultipleFulfillmentOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_multiple_fulfillment_order_output.htm)

The variable has one field: `fulfillmentOrders` . This field is a list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupOutputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_group_output.htm)

**•** `fulfilledFromLocationId` - Reference to the fulfillment location. This value is included so that
you can resubmit the creation if it fails.

**•** `fulfillmentOrderId` - Reference to the created fulfillment order.

**•** `fulfillmentType` - The fulfillment type. This value is included if the creation failed, so you can
resubmit it.

**•** `orderDeliveryGroupSummaryId` - Reference to the order delivery group summary associated
with the order product summaries. This value is included if the creation failed, so you can resubmit it.

**•** `orderItemSummaries` - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. This value is included if the creation failed, so you](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)
can resubmit it. Each variable has these fields:

**–** `orderItemSummaryId`  - Reference to an order product summary.

**–** `quantity`  - The quantity of the order product summary to allocate to the fulfillment order.

**•** `orderSummaryId` - Reference to the order summary associated with the order product summaries.
This value is included if the creation failed, so you can resubmit it.

**•** `referenceId` - Reference to the fulfillment group input. Use this value to troubleshoot a failure.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

To set up the Fulfillment Orders Input:

**1.** For each order delivery group:

**a.** Use Assignment elements to set the `orderItemSummaryId` and `quantity` field values on one or more
`ConnectApi.OrderItemSummaryInputRepresentation` variables.

**b.** Use Assignment elements to add the `ConnectApi.OrderItemSummaryInputRepresentation` variables to the
`orderItemSummaries` fields on one or more `ConnectApi.FulfillmentGroupInputRepresentation`
variables, one for each fulfillment group.

**c.** Use Assignment elements to set the `fulfilledFromLocationId`, `fulfillmentType`, and `referenceId` field
values on the `ConnectApi.FulfillmentGroupInputRepresentation` variables.

**d.** Use Assignment elements to add the `ConnectApi.FulfillmentGroupInputRepresentation` variables to the
`fulfillmentGroups` field on a `ConnectApi.FulfillmentOrderInputRepresentation` variable.

**e.** Use Assignment elements to set the `orderDeliveryGroupSummaryId` and `orderSummaryId` field values on the
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.FulfillmentOrderInputRepresentation` variables to the
`fulfillmentOrders` field on a `ConnectApi.MultipleFulfillmentOrderInputRepresentation` variable.

**3.** Use the `ConnectApi.MultipleFulfillmentOrderInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Create an Invoice from Change Orders

Create an invoice to represent the charges for one or more change orders. Create invoices for change
orders that increase order amounts, such as return fees. When you ensure the refund for a return,
include the invoices for the associated return fees in the input.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create an Invoice from Change Orders .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Required. This input is an Apex-defined variable of class
[ConnectApi.CreateInvoiceFromChangeOrdersInputRepresentation. It has two](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_invoice_from_change_orders.htm)
fields.

###### Create Required. This input is an Apex-defined variable of class

`Invoice` [ConnectApi.CreateInvoiceFromChangeOrdersInputRepresentation. It has two](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_invoice_from_change_orders.htm)
`From` fields.

```
Change
```

The `changeOrderIds` field is a list of IDs of the change orders to create an

`Order` invoice for.
```
Input
```

The `orderSummaryId` field is the ID of the order summary associated with
the change orders.

The `changeOrderIds` field is a list of IDs of the change orders to create an
invoice for.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
Invoice Output

```

SEE ALSO:

[This value is an Apex-defined variable of class ConnectApi.ChangeOrdersInvoiceOutputRepresentation. It has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_orders_invoice_output.htm)
three fields.

The `errors` [field is a list of Apex-defined variables of class ConnectApi.ErrorResponse containing any errors](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
that were returned.

The `invoiceId` field contains the ID of the created invoice.

The `success` field indicates whether the transaction was successful.

Flow Core Action for Order Management: Create Return Order

Flow Core Action for Order Management: Return Return Order Items

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order

Create an invoice for a fulfillment order that doesn’t have one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create an Invoice from Fulfillment Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Fulfillment` Reference to the fulfillment order that needs an invoice.

```
Order Id

```

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Invoice

creation

output

```

SEE ALSO:

[This value is an Apex-defined variable of class ConnectApi.FulfillmentOrderInvoiceOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_invoice_output.htm)

The `invoiceId` field contains the ID of the created invoice.

Flow Core Action for Order Management: Ensure Funds Async

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Order Payment Summary

Create an order payment summary for a payment authorization or payments that use the same
payment method and are attached to the same order summary.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Order Payment Summary .

Set Input Values

Use values from earlier in the flow to set the inputs. Include at least one payment authorization or
list of payments. You don’t need both.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.CreateOrderPaymentSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_order_payment_summary.htm)

`Order` This input is an Apex-defined variable of class
`Payment` [ConnectApi.CreateOrderPaymentSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_order_payment_summary.htm)
`Summary` The variable includes these fields:
###### `Create`

**•** `orderSummaryId`       - Reference to the order summary associated with
```
Input
```
the payments. In orgs with the multicurrency feature enabled, the order
payment summary inherits the `ISO Currency` value from the order
summary.

The variable includes these fields:

**•** `paymentAuthorizationId`       - Reference to the payment
authorization to associate with the summary.

**•** `paymentIds`       - List of IDs of the payments to associate with the summary.

Store Output Values

**Output Parameter** **Description**

```
Order Payment

Summary Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.CreateOrderPaymentSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_create_order_payment_summary_output.htm)

The `orderPaymentSummaryId` field contains the ID of the created order payment summary.

To set up the Order Payment Summary Create Input for payments, first use Assignment elements to add the payment IDs to a list of
strings variable. Then use that variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Order Summary

Create an order summary based on an order. That order is considered the original order for the
order summary. Subsequent change orders that apply to the order summary are also represented
as order records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Order Summary .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Order

Summary

###### `Create`

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OrderSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_summary.htm)

The variable has these fields:

**•** `businessModel` —The order’s business model. It can have one of these
values:

**–** B2B

**–** B2C

**•** `externalReferenceIdentifier` —Used to prevent duplicate
records. This value is case-sensitive.

**•** `name` —Order summary number to assign to the order summary.

**•** `orderId` —Required. The ID of the original order to create an order
summary for.

**•** `orderLifeCycleType` —Specifies whether the order is managed in
Salesforce Order Management or by an external system. It can have one of
these values:

**–** _`MANAGED`_ —The order is managed in Salesforce Order Management. If
no value is specified, the default is _`MANAGED`_ .

**–** _`UNMANAGED`_ —The order is managed by an external system.

**•** `sourceProcess` —Describes the order process creating the order
summary. It can have one of these values:

**–** _`OrderOnBehalf`_ —An Order on Behalf Of process.

**–** _`Standard`_ —Any process other than Order on Behalf Of.

**•** `status` —Status to assign to the order summary. The value must match
one of the picklist values on the `Status` field of the Order Summary object.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
Order Summary

Output

```

SEE ALSO:

[This value is an Apex-defined variable of class OrderSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_order_summary_output.htm)

The `orderSummaryId` field contains the ID of the created order summary.

Add and Edit Elements

Flow Core Action for Order Management: Create Return Order

Create a return order and return order items for order items belonging to an order summary. You
can add return fees for any of the order items.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Return Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management and
Returns

```
Return

Order

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ReturnOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order.htm)

The variable has four fields:

**•** `orderSummaryId` —ID of the order summary containing the items to
be returned. The order summary’s order lifecycle type must be Managed.

**•** `returnOrderLifeCycleType` —The LifeCycleType of the return
order. Possible values are:

**–** _`Managed`_ —Process the return order using the actions and APIs. It can
generate change orders and affects financial fields and rollup calculations.

**–** _`Unmanaged`_ —The return order is for tracking purposes only. It isn’t
involved in any financial calculations and doesn’t generate any change
orders. The system doesn’t prevent the creation of duplicate return order
line items in an unmanaged return order for the same order item.

**•** `returnOrderLineItems` —A list of Apex-defined variables of class
[ConnectApi.ReturnOrderLineItemInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_line_item.htm)
these fields:

**–** `canReduceShipping` —Whether the associated shipping charge
can be refunded.

**–** `orderItemSummaryId` —ID of the associated OrderItemSummary.
If the OrderItemSummary already has an associated ReturnOrderLineItem,
then you must specify a different `reasonForReturn` . Duplicating
the reason breaks the financial calculations.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `quantityExpected` —Quantity expected to be returned.

**–** `quantityReceived` —(Optional) Quantity already physically returned. This value isn’t used by any
standard features, but it’s provided for use in customizations.

**–** `reasonForReturn` —(Optional) Reason for the return. The value must match an entry in the
ReturnOrderLineItem object’s ReasonForReturn picklist.

**–** `returnOrderLineItemFees` —(Optional) A list of Apex-defined variables of class
[ConnectApi.ReturnOrderLineItemFeeInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_line_item_fee.htm)

**•** `amount` —Value used to calculate the fee amount, as described by the amountType. It must be a
positive value.

**•** `amountType` —Describes how the fee amount is calculated. It can have one of these values:

**–** _`AmountWithTax`_                - `amount` is the fee amount, including tax.

**–** _`AmountWithoutTax`_                - `amount` is the fee amount, not including tax. Tax is calculated on
the value and added.

**–** _`Percentage`_                - `amount` is a percentage. The fee amount is `amount` divided by 100 and
then multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated
OrderItemSummary, prorated for the quantity being returned.

**–** _`PercentageGross`_                - `amount` is a percentage. The fee amount is `amount` divided by
100 and then multiplied by the `TotalLineAmountWithTax` of the associated
OrderItemSummary, prorated for the quantity being returned.

**•** `description` —(Optional) Description of the fee.

**•** `product2Id` —ID of the product representing the fee.

**•** `reason` —Reason for the fee. The value must match an entry in the ReturnOrderLineItem object’s
`ReasonForReturn` picklist.

**•** `status` —Status to assign to the return order. The value must match one of the picklist values on the
Status field of the Return Order object.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.ReturnOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_order_output.htm)

The `returnOrderId` field contains the ID of the created return order.

To set up the Create Return Order Input:

**1.** Use Assignment elements to set the `canReduceShipping`, `orderItemSummaryId`, `quantityExpected`,
`quantityReceived`, and `reasonForReturn` field values on one or more
`ConnectApi.ReturnOrderLineItemInputRepresentation` variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** If you want to add any return fees, use Assignment elements to set the `amount`, `amountType`, `description`, `product2Id`,
and `reason` field values on one or more `ConnectApi.ReturnOrderLineItemFeeInputRepresentation`
variables. The `product2Id` points to a fee product that you created.

**3.** Use Assignment elements to add the `ConnectApi.ReturnOrderLineItemFeeInputRepresentation` variables
to the `returnOrderLineItemFees` fields on the `ConnectApi.ReturnOrderLineItemInputRepresentation`
variables representing the associated return order items.

**4.** Use an Assignment element to add the `ConnectApi.ReturnOrderLineItemInputRepresentation` variables to
the `returnOrderLineItems` field on a `ConnectApi.ReturnOrderInputRepresentation` variable.

**5.** Use Assignment elements to set the `orderSummaryId`, `returnOrderLifeCycleType`, and `status` field values on
the `ConnectApi.ReturnOrderInputRepresentation` variable.

**6.** Use the `ConnectApi.ReturnOrderInputRepresentation` variable in the action input.

SEE ALSO:

Flow Core Action for Order Management: Return Return Order Items

Add and Edit Elements

Flow Core Action for Order Management: Ensure Funds Async

Ensure funds for an invoice, and apply them to it. If needed, capture authorized funds by sending
a request to a payment provider. This action inserts a background operation into an asynchronous
job queue and returns the ID of that operation so you can track its status. Payment gateway responses
appear in the payment gateway log and don’t affect the background operation status.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Ensure Funds Async .

Note: If the action creates a payment, the payment record’s ClientContext value isn’t
predictable. Don't use it in custom logic.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Ensure Funds`

```
Async Input

```

[This input is an Apex-defined variable of class ConnectApi.EnsureFundsAsyncInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_ensure_funds_async.htm)

The variable has one field: `invoiceId`, which is the ID of the invoice to ensure funds for and apply them to.

`Order Summary` Reference to the order summary associated with the invoice.

```
Id

```

Store Output Values

**Output Parameter** **Description**

###### `Ensure Funds`

```
Async Output

```

[This value is an Apex-defined variable of class EnsureFundsAsyncOutputRepresentation. It only returns the ID](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_ensure_funds_async_output.htm)
of the asynchronous background operation, regardless of whether a call is made to an external payment
gateway. It doesn’t include any errors from the operation.

The `backgroundOperationId` field contains the ID of the background operation.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

This action applies funds to the invoice balance from order payment summaries associated with the specified order summary following
this logic:

Note: If multiple order payment summaries have equal `BalanceAmount` values, their order of selection is random.

**1.** Verify that the invoice balance doesn’t exceed the total `BalanceAmount` of all the order payment summaries associated with
the order summary.

**2.** If an order payment summary has a `BalanceAmount` equal to the invoice balance, apply the funds from that order payment
summary.

**3.** If no exact match was found, apply funds from the order payment summary with the largest `BalanceAmount` .

**4.** If the invoice still has a balance to ensure, repeat steps 2 and 3 until the full balance is ensured or no captured funds remain.

**5.** If the invoice still has a balance, look for an order payment summary with an authorized amount equal to the remaining invoice
balance. If one exists, capture and apply the funds from that order payment summary.

**6.** If no exact match was found, capture and apply funds from the order payment summary with the largest authorized amount.

**7.** If the invoice still has a balance to ensure, repeat steps 5 and 6 until the full balance is ensured.

SEE ALSO:

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

Flow Core Action for Order Management: Ensure Refunds Async

Ensure refunds for a credit memo or excess funds by sending a request to a payment provider. This
action inserts a background operation into an asynchronous job queue and returns the ID of that
operation so you can track its status. Payment gateway responses appear in the payment gateway
log and don’t affect the background operation status.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Ensure Refunds Async .

Note: If the action creates a refund, the refund record’s ClientContext value isn’t predictable.
Don't use it in custom logic.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Ensure`

```
Refunds Async

Input

```

[This input is an Apex-defined variable of class ConnectApi.EnsureReundsAsyncInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_ensure_refunds_async.htm)

The variable has these fields. You must specify `creditMemoId` or `excessFundsAmount` . You can
specify both.

**•** `creditMemoId` —The ID of the credit memo to ensure refunds for.

**•** `excessFundsAmount` —The amount of excess funds to apply the refunds against.

**•** `invoicesToPay` —List of invoices for fees that reduce the refund, such as return fees.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `isAllowPartial` —This value controls the behavior when the amounts included in the `sequences`
list don’t cover the entire refund amount. If this value is false, the default refund logic is applied to ensure
the remaining refund amount. If this value is true, the unrefunded balance remains on the credit memo. If
you don’t specify a `sequences` list, this value is ignored, and the default refund logic is applied. The
default is false.

**•** `sequences` —This input is an ordered list of refund amounts and the OrderPaymentSummaries to apply
them to. The process traverses this list in order and stops when it has refunded the full amount. It’s a list of
Apex-defined variables of class SequenceOrderPaymentSummaryInputRepresentation. It contains these
fields:

**–** `amount` —Amount of the refund to apply to the OrderPaymentSummary.

**–** `orderPaymentSummaryId` —ID of the OrderPaymentSummary to apply the Amount to.

`Order Summary` Reference to the order summary associated with the credit memo.

```
   Id

```

Store Output Values

**Output Parameter** **Description**

```
Ensure Refunds

Async Output

```

Usage

[This value is an Apex-defined variable of class EnsureRefundsAsyncOutputRepresentation. It only returns the](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_ensure_refunds_async_output.htm)
ID of the asynchronous background operation, regardless of whether a call is made to an external payment
gateway. It doesn’t include any errors from the operation.

The `backgroundOperationId` field contains the ID of the background operation.

This action applies the refund to order payment summaries associated with the specified order summary following this logic.

Note: If multiple order payment summaries have equal `AvailableToRefund` amounts, their order of selection is random.

**1.** Verify that the credit memo balance and excess funds amount don't exceed the total `AvailableToRefund` amount of all the
order payment summaries associated with the order summary.

**2.** If `sequences` is specified, follow these steps.

**a.** Traverse the `sequences` list in order and apply the specified refund amounts to the specified order payment summaries.

**b.** If the specified credit memo and excess funds are fully refunded, or if `isAllowPartial` is true, then the action stops here.

**3.** If a credit memo is specified, follow these steps.

**a.** If an order payment summary has an `AvailableToRefund` amount matching the credit memo’s remaining balance, apply
the refund to that payment.

**b.** If no exact match was found, apply the refund to the order payment summary with the largest `AvailableToRefund`
amount.

**c.** If the credit memo has any remaining balance, repeat steps a and b until that balance is fully refunded.

**4.** If only one OrderPaymentSummary is specified but has multiple payments, follow these steps.


Automate Your Business Processes with Salesforce Flow Flow Reference

**a.** If a payment has an amount matching the CreditMemo’s remaining balance, apply the refund to that payment.

**b.** If no exact match was found but one or more payment has a large enough amount to cover the balance, use the payment with
the smallest amount.

**c.** If no single payment has a large enough amount, use multiple payments in descending order of amount. This ensures the fewest
payments are used.

**5.** If an excess funds amount is specified, follow these steps.

**a.** Examine those order payment summaries. If one has an `AvailableToRefund` amount matching the excess funds amount,
apply the refund to that payment.

**b.** If no exact match was found, apply the refund to the order payment summary with the largest `AvailableToRefund`
amount.

**c.** If any excess funds amount remains, repeat steps a and b until it’s fully refunded.

SEE ALSO:

Flow Core Action for Order Management: Create Credit Memo

Flow Core Action for Order Management: Create an Invoice from Change Orders

Flow Core Action for Order Management: Return Return Order Items

Flow Core Action for Order Management: Ensure Funds Async

Add and Edit Elements

Flow Core Action for Order Management: Find Routes with Fewest Splits

Evaluate ordered product quantities against available inventory to determine the smallest
combination of locations that can fulfill the order. If multiple combinations of the minimum number
of locations can fulfill the order, the action returns multiple options. Optionally, you can specify a
maximum allowable number of locations. By default, the action executes up to 1,000,000 times,
stopping when it hits 10,000 results.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Find Routes With Fewest Splits** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Order Routing

Minimize

Shipments

Input

```

[This input is an Apex-defined variable of class ConnectApi.FindRoutesWithFewestSplitsInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits.htm)

The `locationAvailableInventory` field is a list of Apex-defined variables of class
[ConnectApi.LocationAvailabilityInputRepresentation. Each of the variables represents a fulfillment location to](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_location_availability.htm)
consider and includes these fields:

**•** `externalReferenceId` - External reference ID of the inventory location.

**•** `quantity` - Available quantity of the product.

**•** `stockKeepingUnit` - Stock Keeping Unit (SKU) of the product.

The `maximumNumberOfSplits` field is the maximum allowable number of shipment splits. The action
doesn’t return routing options that involve more than this number of splits.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

Each split represents an additional shipment. Specifying a maximum of 0 returns only locations that can fulfill
the entire order in a single shipment. A maximum of 1 returns combinations of locations that can fulfill the
order in one or two shipments, and so on.

The `orderedQuantities` field is a list of Apex-defined variables of class
[ConnectApi.QuantityWithSkuInputRepresentation. Each of the variables represents an ordered product quantity](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_quantity_with_sku.htm)
to fulfill, and includes these fields:

**•** `quantity`            - Ordered quantity of the product.

**•** `stockKeepingUnit`            - SKU of the product.

Store Output Values

**Output Parameter** **Description**

```
Order Routing

Minimize

Shipments

Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_output.htm)
which contains the sets of fulfillment locations that meet the requirements.

The variable has one field: `targetLocations` . This field is a list of Apex-defined variables of class
[ConnectApi.AvailableLocationOutputRepresentation, each of which represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_available_location_output.htm)
that can combine to fulfill the ordered products.

Each of the variables includes one field: `locations` . This field is a list of the locations in the set.

To set up the Order Routing Minimize Shipments Input:

**1.** Use Assignment elements to set the `externalReferenceId`, `quantity`, and `stockKeepingUnit` field values on one
or more `ConnectApi.LocationAvailabilityInputRepresentation` variables.

**2.** Use Assignment elements to set the `quantity` and `stockKeepingUnit` field values on one or more
`ConnectApi.QuantityWithSkuInputRepresentation` variables.

**3.** Use an Assignment element to add the `ConnectApi.LocationAvailabilityInputRepresentation` variables to
the `locationAvailableInventory` field on a
`ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable.

**4.** Optionally, use an Assignment element to set the `maximumNumberOfSplits` field on the
`ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable.

**5.** Use an Assignment element to add the `ConnectApi.QuantityWithSkuInputRepresentation` variables to the
`orderedQuantities` field on the `ConnectApi.FindRoutesWithFewestSplitsInputRepresentation`
variable.

**6.** Use the `ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Use OCI to Find Routes with Fewest Splits

Evaluate ordered product quantities against available inventory to determine the smallest
combination of locations that can fulfill the order. If multiple combinations of the minimum number
of locations can fulfill the order, the action returns multiple options. Optionally, you can specify a
maximum allowable number of locations and a list of locations to exclude from the calculation.
This action combines the Omnichannel Inventory Get Availability action and the Order Management
Find Routes with Fewest Splits actions. Instead of calling Get Availability and including the output
in the Find Routes with Fewest Splits input, call this action and specify a location or location group
to fulfill each ordered product. By default, this action executes up to 1,000,000 times, stopping when
it hits 10,000 results. This action handles the inventory check.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Find Routes With Fewest Splits Using OCI** .

Note: Set the flow’s runtime API version to 54.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Find Routes`

```
With Fewest

Splits Using

OCI Input

```

Store Output Values

This input is an Apex-defined variable of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_using_o_c_i.htm)

The `findRoutesWithFewestSplitsUsingOCIInputs` field is a list of Apex-defined variables of
[class ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_group_using_o_c_i.htm)
represents one order and includes these fields:

**•** `excludeLocations` —List of locations to exclude from the routing calculations.

**•** `maximumNumberOfSplits` —Maximum allowable number of shipment splits. The action doesn’t
return routing options that involve more than this number of splits.

Each split represents an additional shipment. Specifying a maximum of 0 returns only locations that can
fulfill the entire order in a single shipment. A maximum of 1 returns combinations of locations that can fulfill
the order in one or two shipments, and so on.

**•** `orderedItems` —A list of Apex-defined variables of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation. Each of the variables represents](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_using_o_c_i_item.htm)
an ordered product quantity to fulfill and a location or location group, and includes these fields:

**–** `locationGroupIdentifier` —External reference ID of the inventory location or location group.

**–** `quantity` —Ordered quantity of the product.

**–** `stockKeepingUnit` —Stock Keeping Unit (SKU) of the product.

Use output values later in the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Find Routes

With Fewest

Splits Using

OCI Output

```

Usage

This output is an Apex-defined variable of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation, which contains inventory availability](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_using_o_c_i_output.htm)
data and the sets of fulfillment locations that meet the requirements.

The variable has one field: `results` . This field is a list of Apex-defined variables of class
[ConnectApi.FindRoutesWithFewestSplitsWithInventoryOutputRepresentation, each of which represents the](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_with_inventory_output.htm)
output for one order, and includes these fields:

**•** `inventory` —Inventory availability data for the location groups and locations specified in the input.

**•** `targetLocations` —A list of Apex-defined variables of class
[ConnectApi.AvailableLocationOutputRepresentation, each of which represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_available_location_output.htm)
that can combine to fulfill the ordered products. Each of the variables includes one field `locations` .
This field is a list of the locations in the set.

To set up the Find Routes With Fewest Splits Using OCI Input:

**1.** Use assignment elements to set the values for the `locationGroupIdentifier`, `quantity`, and `stockKeepingUnit`
field values on one or more ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation variables.

**2.** Use assignment elements to add the ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation variables to the
`orderedItems` field on a ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable.

**3.** Optionally, use an assignment element to set the value for the `maximumNumberOfSplits` field on the
ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable.

**4.** Use an assignment element to add the ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable to the
`findRoutesWithFewestSplitsUsingOCIInputs` field on a
ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable.

**5.** Repeat steps 1–4 for each order that you want to include in the action, adding the inputs to the same
ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable.

**6.** Use the ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable in the action input.

Flow Core Action for Order Management: Get Fulfillment Order Capacity Values

Get information about the current fulfillment order capacity of one or more locations.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Get Fulfillment Order Capacity Values .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Get` [This input is an Apex-defined variable of class ConnectApi.GetFOCapacityValuesRequestInputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_get_f_o_capacity_values_request.htm)
`Fulfillment` which includes this field:

```
   Order
```

**•** `locationIds` —List of IDs of the locations to get fulfillment order capacity information for.
```
   Capacity

   Values Input

```

Store Output Values

Use output values later in the flow.

**Output Parameter** **Description**

`Get` [This output is an Apex-defined variable of class ConnectApi.GetFOCapacityValuesOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_get_f_o_capacity_values_output.htm)
`Fulfillment` includes this field:

```
   Order Capacity
```

**•** `locations` —This field is a list of Apex-defined variables of class

`Values Output` [ConnectApi.LocationCapacityOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_location_capacity_output.htm)

**–** `assigned` —Value of the location’s Assigned Fulfillment Order Count.

**–** `capacity` —Value of the location’s Fulfillment Order Capacity. This property represents the location’s
maximum capacity.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `heldCapacity` —Number of fulfillment orders that the location is holding capacity for.

**–** `locationId` —ID of the location.

Flow Core Action for Order Management: Hold Fulfillment Order Capacity

Hold capacity to process fulfillment orders at one or more locations. This action increases a location’s
held capacity. Hold capacity when you plan to assign a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Hold Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Hold` [This input is an Apex-defined variable of class ConnectApi.HoldFOCapacityRequestInputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_hold_f_o_capacity_request.htm)
`Fulfillment` includes these fields:

###### `Order`

**•** `allOrNothing` —(Optional) Controls whether a single failed request cancels all other requests in the
```
   Capacity
```
list ( _`true`_ ) or whether some requests can succeed if others fail ( _`false`_ ). The default value is _`false`_ .
```
   Input
```

**•** `capacityRequests` —This field is a list of Apex-defined variables of class
[ConnectApi.CapacityRequestInputRepresentation. Each of the variables represents a request to hold capacity](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
for one fulfillment order at one location, and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can be a UUID. Use the action
request IDs in response data to identify which requests succeeded or failed.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.

**Output Parameter** **Description**

`Hold` [This output is an Apex-defined variable of class ConnectApi.HoldFOCapacityResponseOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_hold_f_o_capacity_response_output.htm)
`Fulfillment` which includes this field:

```
   Order Capacity
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class

`Output` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).

Flow Core Action for Order Management: Order Routing Rank by Average Distance

Calculate the average distance from sets of inventory locations to an order recipient, and return
the sets sorted by that average distance. Use this action to compare the average shipping distances
for different sets of locations that can fulfill an order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Order Routing Rank By Average Distance .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

[This input is an Apex-defined variable of class ConnectApi.RankAverageDistanceInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_rank_average_distance.htm)

`Order Routing` [This input is an Apex-defined variable of class ConnectApi.RankAverageDistanceInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_rank_average_distance.htm)

```
Rank By
```

The `deliveryCountryCode` field is the country code of the order recipient.
```
Average
```

The `deliveryPostalCode` field is the postal code of the order recipient.
```
Distance
```

`Input` The `distanceUnit` field specifies whether to return average distances in miles or kilometers, respectively.
The value can be _`mi`_ or _`km`_ .

The `deliveryCountryCode` field is the country code of the order recipient.

The `sortResult` field specifies whether to sort the location sets in ascending or descending order by average
distance. The value can be _`ASC`_ or _`DESC`_ .

The `targetLocations` field is a list of Apex-defined variables of class
[ConnectApi.TargetLocationInputRepresentation. Each of the variables represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_target_location.htm)
that can fulfill an order together, and includes one field: `locations` . This field is a list of Apex-defined variables
[of class ConnectApi.LocationInputRepresentation, each of which represents one location in the list and contains](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_location.htm)
these fields:

**•** `countryCode`         - Country code of the location.

**•** `locationIdentifier`         - ID of the location.

**•** `postalCode`         - Postal code of the location.

Store Output Values

**Output Parameter** **Description**

[This output is an Apex-defined variable of class ConnectApi.RankAverageDistanceOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_rank_average_distance_output.htm)
contains the list of fulfillment location sets, sorted by average distance to the order recipient.

`Order Routing` This output is an Apex-defined variable of class
`Rank By` contains the list of fulfillment location sets, sorted by average distance to the order recipient.

```
Average
```

The `distanceUnit` field is the specified unit of distance. It can be _`miles`_ or
```
Distance
```

The `results` field is a list of Apex-defined variables of class
```
Output
```
[ConnectApi.AverageDistanceResultOutputRepresentation, each of which includes one field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)
`distanceCalculation` . It’s an Apex-defined variable of class
[ConnectApi.DistanceCalculationOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_distance_calculation_output.htm)

The `distanceUnit` field is the specified unit of distance. It can be _`miles`_ or _`kilometers`_ .

**•** `averageDistance`          - Average distance from the locations to the order recipient.

**•** `locations` [— A list of Apex-defined variables of class ConnectApi.LocationOutputRepresentation, each](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_location_output.htm)
of which represents a location in the set and includes two fields:

**–** `distance`           - Distance from the location to the order recipient.

**–** `locationIdentifier`           - ID of the location.

**•** `rank`          - This result’s rank among all results by average distance to the order recipient.

Usage

To set up the Order Routing Rank By Average Distance Input:

**1.** Use Assignment elements to set the `countryCode`, `locationIdentifier`, and `postalCode` field values on one or
more `ConnectApi.LocationInputRepresentation` variables to represent the locations in a set.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** Use an Assignment element to add the `ConnectApi.LocationInputRepresentation` variables to the `locations`
field on a `ConnectApi.TargetLocationInputRepresentation` variable.

**3.** Repeat the previous two steps for each set of fulfillment locations.

**4.** Use an Assignment element to add the `ConnectApi.TargetLocationInputRepresentation` variables to the
`targetLocations` field on a `ConnectApi.RankAverageDistanceInputRepresentation` variable.

**5.** Use Assignment elements to set the `deliveryCountryCode`, `deliveryPostalCode`, `distanceUnit`, and
`sortResult` field values on the `ConnectApi.RankAverageDistanceInputRepresentation` variable.

**6.** Use the `ConnectApi.RankAverageDistanceInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Release Held Fulfillment Order Capacity

Release held fulfillment order capacity at one or more locations. This action decreases a location’s
held capacity without increasing its assigned fulfillment order count. Release held capacity when
you cancel assigning a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Release Held Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.ReleaseHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_release_held_f_o_capacity_request.htm)
these fields:

`Fulfillment` This input is an Apex-defined variable of class
`Order` [ConnectApi.ReleaseHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_release_held_f_o_capacity_request.htm)
`Location` these fields:

###### `Release`

**•** `allOrNothing` —(Optional) Controls whether a single failed request
```
Held
```
cancels all other requests in the list ( _`true`_ ) or whether some requests can
```
Capacity
```
succeed if others fail ( _`false`_ ). The default value is _`false`_ .

```
Held
```

cancels all other requests in the list ( _`true`_ ) or whether some requests can
```
Capacity
```
succeed if others fail ( _`false`_ ). The default value is _`false`_ .
```
Input
```

**•** `capacityRequests` —This field is a list of Apex-defined variables of
[class ConnectApi.CapacityRequestInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
represents a request to release capacity for one fulfillment order at one
location, and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can
be a UUID. Use the action request IDs in response data to identify which
requests succeeded or failed.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

`Fulfillment` This output is an Apex-defined variable of class
`Order Location` [ConnectApi.ReleaseHeldFOCapacityResponseOutputRepresentation, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_release_held_f_o_capacity_response_output.htm)

```
   Release Held
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class
`Capacity` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)
```
   Output
```

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).

Flow Core Action for Order Management: Return Order Item Summaries Preview

Preview the expected results of a simple return of one or more order product summaries from an
order summary without executing the return. The output of this action contains the values that
would be set on the change order created by submitting the proposed return.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` Reference to the order summary that you want to preview returning order product
`Summary` summaries from.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Return`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithoutTax`_               - `amount` is the fee amount, not including tax. Tax is calculated on the
value and added.

**•** _`Percentage`_               - `amount` is a percentage. The fee amount is `amount` divided by 100 and then
multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated order product
summary, prorated for the quantity being returned.

**•** _`PercentageGross`_               - `amount` is a percentage. The fee amount is `amount` divided by 100
and then multiplied by the `TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to return. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to return.

**•** `reason` —Required. Return reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Product

Summary Items

Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed return.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund, but it isn’t
associated with an invoice or credit memo. Excess funds normally occur when order products are canceled
before fulfillment but after payment is captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the return.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the return.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Return Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for returning order product summaries, display the output of this action for the user to review before executing the return.
When the user verifies the expected results, pass the same input to a Return Order Item Summaries Submit action.

SEE ALSO:

Flow Core Action for Order Management: Return Order Item Summaries Submit

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Return Order Item Summaries Submit

Return one or more order product summaries from an order summary. This action is a simple return
that creates a change order but not a return order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` Reference to the order summary that you want to return order product summaries
`Summary` from.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Return`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not
including tax. Tax is calculated on the value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is
`amount` divided by 100 and then multiplied by the `TotalPrice`
and `TotalTaxAmount` of the associated order product summary,
prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount
is `amount` divided by 100 and then multiplied by the
`TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in
the org. ID of the price book entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry
in the Order Product Summary Change object’s `Reason` picklist.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `orderItemSummaryId` —Required. ID of an order product summary to return. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to return.

**•** `reason` —Required. Return reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Product

Summary Items

Output

```

[This output is an Apex-defined variable of class ConnectApi.SubmitReturnOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_submit_return_output.htm)

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that’s owed as a refund, but it’s not
associated with an invoice or credit memo. Excess funds normally occur when order products are canceled
before fulfillment but after payment is captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the return.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the return.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalTaxAmount` —Change to the total tax.

The `changeOrderId` field is the ID of the change order record created for the returned items. Use this
change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for any return fees. Use this
change order to create an invoice.

Usage

To set up the Return Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for returning order product summaries, run a Return Order Item Summaries Preview action before running this action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

SEE ALSO:

Flow Core Action for Order Management: Return Order Item Summaries Preview

Add and Edit Elements

Flow Core Action for Order Management: Return Return Order Items

Process one or more return order line items belonging to a return order. This action creates a change
order record for the returned items and makes the processed return order line items read-only. You
can include return order fees associated with the return order line items. If you do, a change order
record is created for the return fees. If a processed return order line item has a remaining expected
quantity, the action creates a separate return order line item representing that quantity.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Return Order Items .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management and
Returns

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Return Order` Reference to the return order that you want to process return order line items from.

```
   Id

```

```
Return Items

Input

```

Store Output Values

[This input is an Apex-defined variable of class ConnectApi.ReturnItemsInputRepresentation. It has three fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_items.htm)

The `returnOrderItemDeliveryCharges` field is an optional list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation. Each variable includes one field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item_delivery_charge.htm)

**•** `returnOrderLineItemId` —ID of a return order line item representing a shipping charge to return.

The `returnOrderItemFees` field is an optional list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemFeeInputRepresentation. Each variable includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item_fee.htm)

**•** `quantityReturned` —The quantity of the ReturnOrderLineItem to process. The amount of the fee to
charge is determined by multiplying the total fee amount by this value, divided by the quantityExpected.
For example, if the fee amount is $10 and the quantityExpected is 2, if the quantityReturned is 1, $5 is
charged. This value normally equals the quantity returned of the ReturnOrderLineItem for the returned item
that the fee applies to. The value must be greater than 0. If this value plus quantityToCancel is less than the
expected return quantity, the remaining quantity to be returned is added to a new ReturnOrderLineItem.

**•** `quantityToCancel` —The quantity of the ReturnOrderLineItem to remove. This value normally equals
the quantity canceled of the ReturnOrderLineItem for the returned item that the fee applies to. This value
can also be used to cancel a portion of the fee. The value must be 0 or greater. If this value plus
quantityReturned is less than the expected return quantity, the remaining quantity to be returned is added
to a new ReturnOrderLineItem.

**•** `returnOrderLineItemId` —ID of a return order line item representing a return fee to charge.

The `returnOrderItems` field is a list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemInputRepresentation. Each of the variables includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item.htm)

**•** `quantityReceived` —(Optional) The quantity of the return order line item that has been received.
The value must be zero or greater. This value isn’t used by any standard features, but is provided for use in
customizations.

**•** `quantityRejected` —(Optional) The quantity of the return order line item that has been rejected for
return. The value must be zero or greater. This value isn’t used by any standard features, but is provided for
use in customizations.

**•** `quantityReturned` —The quantity of the return order line item that has been returned. The value
must be greater than zero. If this value plus quantityToCancel is less than the expected return quantity,
then the remaining quantity to be returned is added to a new return order line item.

**•** `quantityToCancel` —(Optional) The quantity of the return order line item to remove because it’s not
being returned. The value must be zero or greater. If this value plus quantityReturned is less than the
expected return quantity, then the remaining quantity to be returned is added to a new return order line
item.

**•** `reasonForRejection` —(Optional) The reason why the rejected quantity, if any, was rejected. This
value isn’t used by any standard features, but is provided for use in customizations.

**•** `returnOrderLineItemId` —The return order line item ID.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Return Items

Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.ReturnItemsOutputRepresentation. It has three](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_items_output.htm)
fields.

The `changeOrderId` field is the ID of the change order record created for the returned item and delivery
charges. Use this change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for the return fees. Use this
change order to create an invoice.

The `returnLineItemSplits` field is a list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemSplitLineOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_order_item_split_line_output.htm)

After a change order is created for a return order line item, the return order line item is read-only. If this action
is used to return a partial quantity, it creates a new “split” return order line item to hold the remaining quantity
to be returned. In that case, it returns the IDs of the original and split return order line items in an element of
the `returnLineItemSplits` output list property.

**•** `newReturnOrderItemId` —ID of the new return order line item that holds the remaining return
quantity.

**•** `originalReturnOrderItemId` —ID of the original return order line item.

To set up the Return Return Order Items Input:

**1.** Use Assignment elements to set the `quantityReceived`, `quantityRejected`, `quantityReturned`,
`quantityToCancel`, `reasonForRejection`, and `returnOrderLineItemId` field values on one or more
`ConnectApi.ReturnOrderItemInputRepresentation` variables.

**2.** If you want to include a delivery charge, use Assignment elements to set the `returnOrderLineItemId` field value on one
or more `ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation` variables.

**3.** If you want to include a return fee, use Assignment elements to set the `quantityReturned`, `quantityToCancel`, and
`returnOrderLineItemId` field values on one or more
`ConnectApi.ReturnOrderItemFeeInputRepresentation` variables.

**4.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemInputRepresentation` variables to the
`returnOrderItems` field on a `ConnectApi.ReturnItemsInputRepresentation` variable.

**5.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation`
variables to the `returnOrderItemDeliveryCharges` field on a
`ConnectApi.ReturnItemsInputRepresentation` variable.

**6.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemFeeInputRepresentation` variables to the
`returnOrderItemFees` field on a `ConnectApi.ReturnItemsInputRepresentation` variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

**7.** Use the `ConnectApi.ReturnItemsInputRepresentation` variable and the return order ID in the action input.

SEE ALSO:

Flow Core Action for Order Management: Create Return Order

Flow Core Action for Order Management: Create Credit Memo

Flow Core Action for Order Management: Create an Invoice from Change Orders

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

##### Salesforce Omnichannel Inventory Flow Core Actions

Salesforce Omnichannel Inventory provides several core actions for implementing inventory
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the **Omnichannel Inventory Service** category, and search for the appropriate action.

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex ConnectApi namespace. For more information on using Apex-defined variables in flows,
see Considerations for the Apex-Defined Data Type on page 260.

Important: A flow that uses Omnichannel Inventory actions must have a runtime API version
of 52.0 or later. If possible, always use the latest API version in your flows.

Flow Core Action for Omnichannel Inventory: Create Reservation
Create one or more inventory reservations at a location or location group.

Flow Core Action for Omnichannel Inventory: Fulfill Reservation
Fulfill one or more inventory reservations at a location.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

Flow Core Action for Omnichannel Inventory: Get Availability
Get inventory availability data for one or more products at one or more inventory locations or location groups.

Flow Core Action for Omnichannel Inventory: Release Reservation
Release one or more inventory reservations.

Flow Core Action for Omnichannel Inventory: Transfer Reservation
Transfer one or more inventory reservations between locations or location groups. This action reduces the reserved quantity at the
source and increases it at the destination. It doesn’t change physical quantities.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Omnichannel Inventory: Create Reservation

Create one or more inventory reservations at a location or location group.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Create Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

###### `Create`

Service

Reservation

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OCICreateReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_create_reservation.htm)

The variable has these fields.

**•** `actionRequestId` —A UUID that identifies the request. To identify
which actions succeeded or failed, use the action request IDs in the output
variables.

**•** `allowPartialReservations` —Optional. When _`true`_, if the system
can’t create the entire reservation, then it attempts to create a partial
reservation.

**•** `createRecords` —A list of up to 100 Apex-defined variables of class
[ConnectApi.OCICreateReservationSingleInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_create_reservation_single.htm)
has these fields.

**–** `locationGroupIdentifier` —Identifier of the location group
at which to reserve inventory. Either `locationGroupIdentifier`
or `locationIdentifier` is required, but not both.

**–** `locationIdentifier` —Identifier of the location at which to
reserve inventory. Either `locationIdentifier` or
`locationGroupIdentifier` is required, but not both.

**–** `quantity` —The quantity of the product to reserve.

**–** `stockKeepingUnit` —The Stock Keeping Unit (SKU) of the product
to reserve.

**•** `expirationSeconds` —Optional. A length of time in seconds. If the
reservation isn’t fulfilled within this amount of time after the reservationTime,
then it expires. The maximum value is 14400.

**•** `externalRefId` —Optional The external reference ID.

**•** `reservationTime` —Optional The time at which to record the
reservation. Example: 2020-07-24T21:13:00Z

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service Create

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCICreateReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_output.htm)

The variable has these fields.

**•** `details` —A list of Apex-defined variables of class
[ConnectApi.OCICreateReservationSingleOutputRepresentation. Each variable represents one product being](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_single_output.htm)
reserved and has these fields.

**–** `errorCode` —The error code, if any.

**–** `locationGroupIdentifier` —Identifier of the location group where the inventory is reserved.

**–** `locationIdentifier` —Identifier of the location where the inventory is reserved

**–** `quantity` —The reserved quantity of the product.

**–** `stockKeepingUnit` —The SKU of the reserved product.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCICreateReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_error_output.htm)
and has these fields.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `expirationTime` —The time at which the reservation would expire.

**•** `reservationTime` —The time when the reservation was recorded.

**•** `success` —Indicates whether the reservation succeeded.

To set up the Omnichannel Inventory Create Service Reservation Input:

**1.** For each product to reserve, use Assignment elements to set the `locationGroupIdentifier` or `locationIdentifier`
field, `quantity` field, and `stockKeepingUnit` field values on a
`ConnectApi.OCICreateReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCICreateReservationSingleInputRepresentation`
variables to the `createRecords` field on a `ConnectApi.OCICreateReservationInputRepresentation`
variable.

**3.** Use Assignment elements to set the `actionRequestId`, `allowPartialReservations`, `expirationSeconds`,
`externalRefId`, and `reservationTime` field values on the
`ConnectApi.OCICreateReservationInputRepresentation` variable.

**4.** Use the `ConnectApi.OCICreateReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Omnichannel Inventory: Fulfill Reservation

Fulfill one or more inventory reservations at a location.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Fulfill Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

###### `Fulfill`

Reservation

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OCIFulfillReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_fulfill_reservation.htm)

The variable has one field: `fulfillmentRecords` . This field is a list of up
to 100 Apex-defined variables of class

[ConnectApi.OCIFulfillReservationSingleInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_fulfill_reservation_single.htm)
these fields.

**•** `actionRequestId` —A UUID that identifies the request. To identify
which actions succeeded or failed, use the action request IDs in the output
variables.

**•** `externalRefId` —Optional. The external reference ID.

**•** `locationIdentifier` —Identifier of the location at which to fulfill the
reserved inventory.

**•** `quantity` —The quantity of the product to fulfill.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to fulfill.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

###### `Fulfill`

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCIFulfillReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCIFulfillReservationErrorOutputRepresentation. Each variable represents a returned error and](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_error_output.htm)
has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCIFulfillReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_single_output.htm)
error and includes the values from the input so you can resubmit them:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `locationIdentifier` —Identifier of the location at which to fulfill the reserved inventory.

**•** `quantity` —The quantity of the product to fulfill.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to fulfill.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the fulfillment succeeded.

To set up the Omnichannel Inventory Service Fulfill Reservation Input:

**1.** For each reservation to fulfill, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`locationIdentifier`, `quantity`, and `stockKeepingUnit` field values on a
`ConnectApi.OCIFulfillReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCIFulfillReservationSingleInputRepresentation`
variables to the `fulfillmentRecords` field on a `ConnectApi.OCIFulfillReservationInputRepresentation`
variable.

**3.** Use the `ConnectApi.OCIFulfillReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Get Availability

Get inventory availability data for one or more products at one or more inventory locations or
location groups.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Get Availability** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

###### `Get`

```

This input is an Apex-defined variable of class
[ConnectApi.OCIGetInventoryAvailabilityInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_get_inventory_availability.htm)

The variable has these fields.

**•** `locationGroupIdentifier` —Optional. Can’t combine with
```
Availability
```
`locationGroupIdentifiers` or `locationIdentifiers` . The
```
Input
```
identifier of a location group to retrieve inventory availability data for.
Specifying this value retrieves inventory data for all locations belonging to
this group.

**•** `locationGroupIdentifiers` —Optional; can’t combine with
`locationGroupIdentifier` or `locationIdentifiers` . A list


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

of up to 100 identifiers of location groups to retrieve inventory availability data for.

**•** `locationIdentifiers` —Optional; can’t combine with `locationGroupIdentifier` or
`locationGroupIdentifiers` . A list of up to 100 identifiers of locations to retrieve inventory
availability data for.

**•** `stockKeepingUnit` —Optional; can’t combine with `stockKeepingUnits` . The SKU of a product
to retrieve inventory availability data for. Specifying a SKU with no locations or location groups returns
availability data for that SKU at all inventory locations that aren’t assigned to location groups.

**•** `stockKeepingUnits` —Optional; can’t combine with `stockKeepingUnit` . A list of up to 100
SKUs of products to retrieve inventory availability data for.

**•** `useCache` —Optional. Fetch the inventory data from the cache. The default value is `true` .

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service Get

Availability

Output

```

[This input is an Apex-defined variable of class ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_get_inventory_availability_output.htm)

The variable has these fields.

**•** `locationGroups` —A list of Apex-defined variables of class
[ConnectApi.OCILocationGroupAvailabilityOutputRepresentation. Each variable represents availability data](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_location_group_availability_output.htm)
for one location group and has these fields.

**–** `inventoryRecords` —A list of Apex-defined variables of class
[ConnectApi.OCIInventoryRecordOutputRepresentation. Each variable represents the availability of one](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_inventory_record_output.htm)
product and has these fields.

**•** `availableToFulfill` —The Available To Fulfill quantity.

**•** `availableToOrder` —The Available To Order quantity.

**•** `effectiveDate` —The effective date of the inventory.

**•** `futures` —A list of Apex-defined variables of class
[ConnectApi.OCIFutureInventoryOutputRepresentation. Each variable represents one future restock](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_future_inventory_output.htm)
and has these fields.

**–** `expectedDate` —Date when the future inventory is expected.

**–** `quantity` —Quantity of the future inventory.

**•** `onHand` —The On Hand quantity.

**•** `reserved` —The Reserved quantity.

**•** `safetyStockCount` —The Safety Stock Count.

**•** `stockKeepingUnit` —The SKU of the product.

**–** `locationGroupIdentifier` —The identifier of the location group.

**•** `locations` —A list of Apex-defined variables of class
[ConnectApi.OCILocationAvailabilityOutputRepresentation. Each variable represents availability data for](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_location_availability_output.htm)
one location and has these fields.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**–** `inventoryRecords` —A list of Apex-defined variables of class
[ConnectApi.OCIInventoryRecordOutputRepresentation. Each variable represents the availability of one](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_inventory_record_output.htm)
product and has these fields.

**•** `availableToFulfill` —The Available To Fulfill quantity.

**•** `availableToOrder` —The Available To Order quantity.

**•** `effectiveDate` —The effective date of the inventory.

**•** `futures` —A list of Apex-defined variables of class
[ConnectApi.OCIFutureInventoryOutputRepresentation. Each variable represents one future restock](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_future_inventory_output.htm)
and has these fields.

**–** `expectedDate` —Date when the future inventory is expected.

**–** `quantity` —Quantity of the future inventory.

**•** `onHand` —The On Hand quantity.

**•** `reserved` —The Reserved quantity.

**•** `safetyStockCount` —The Safety Stock Count.

**•** `stockKeepingUnit` —The SKU of the product.

**–** `locationIdentifier` —The identifier of the location.

To set up the Omnichannel Inventory Service Get Availability Input:

**1.** Use Assignment elements to set the `locationGroupIdentifier`, `locationGroupIdentifiers`, or
`locationIdentifiers` field value, `stockKeepingUnit` or `stockKeepingUnits` field value, and `useCache`
field value on a `ConnectApi.OCIGetInventoryAvailabilityInputRepresentation` variable.

**2.** Use the `ConnectApi.OCIGetInventoryAvailabilityInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Release Reservation

Release one or more inventory reservations.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Release Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Omnichannel

Inventory

Service

Release

```

[This input is an Apex-defined variable of class ConnectApi.OCIReleaseReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_release_reservation.htm)

The variable has one field: `releaseRecords` . This field is a list of up to 100 Apex-defined variables of class
[ConnectApi.OCIReleaseReservationSingleInputRepresentation. Each variable has these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_release_reservation_single.htm)

**•** `actionRequestId` —A UUID that identifies the request. To identify which actions succeeded or failed,
```
Reservation
```
use the action request IDs in the output variables.
```
Input

```

**•** `externalRefId` —Optional. The external reference ID.

**•** `locationGroupIdentifier` —Identifier of the location group at which to release the reserved
inventory. Either `locationGroupIdentifier` or `locationIdentifier` is required, but not
both.

**•** `locationIdentifier` —Identifier of the location at which to release the reserved inventory. Either
`locationIdentifier` or `locationGroupIdentifier` is required, but not both.

**•** `quantity` —The quantity of the product to release.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to release.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

Release

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCIReleaseReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCIReleaseReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_error_output.htm)
and has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCIReleaseReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_single_output.htm)
error and includes the values from the input so you can resubmit them:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `locationGroupIdentifier` —Identifier of the location group at which to release the
reserved inventory.

**•** `locationIdentifier` —Identifier of the location at which to release the reserved inventory.

**•** `quantity` —The quantity of the product to release.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to release.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the release succeeded.

To set up the Omnichannel Inventory Service Release Reservation Input:


Automate Your Business Processes with Salesforce Flow Flow Reference

**1.** For each reservation to release, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`locationGroupIdentifier` or `locationIdentifier`, `quantity`, and `stockKeepingUnit` field values on a
`ConnectApi.OCIReleaseReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCIReleaseReservationSingleInputRepresentation`
variables to the `releaseRecords` field on a `ConnectApi.OCIReleaseReservationInputRepresentation`
variable.

**3.** Use the `ConnectApi.OCIReleaseReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Transfer Reservation

Transfer one or more inventory reservations between locations or location groups. This action
reduces the reserved quantity at the source and increases it at the destination. It doesn’t change
physical quantities.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Transfer Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

```

[This input is an Apex-defined variable of class ConnectApi.OCITransferReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_transfer_reservation.htm)

The variable has these fields.

**•** `allOrNothingTransferId` —Optional. Controls whether a single failed transfer cancels all other
###### `Transfer`
transfers in the transferRecords list.
```
Reservation
```

`Input` **–** To allow some transfers in the transferRecords list to succeed when others fail, don’t set this value.

**–** To cancel all the transfers in the transferRecords list when any of them fail, set this value to a UUID. The
ID must be unique, but isn’t otherwise used.

**•** `transferRecords` —A list of up to 100 Apex-defined variables of class
[ConnectApi.OCITransferReservationSingleInputRepresentation. Each variable represents an inventory transfer](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_transfer_reservation_single.htm)
and has these fields.

**–** `actionRequestId` —A UUID that identifies the request. To identify which actions succeeded or
failed, use the action request IDs in the output variables.

**–** `externalRefId` —Optional. The external reference ID.

**–** `fromLocationGroupIdentifier` —The identifier of the location group transferring the
reservation. Either `fromLocationGroupIdentifier` or `fromLocationIdentifier` is
required, but not both.

**–** `fromLocationIdentifier` —The identifier of the location transferring the reservation. Either
`fromLocationIdentifier` or `fromLocationGroupIdentifier` is required, but not
both.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `ignoreAvailabilityCheck` —If true, force the transfer even if the receiving location doesn’t
have sufficient available inventory. The default value is false.

**–** `quantity` —The quantity of the product reservation to transfer.

**–** `stockKeepingUnit` —The Stock Keeping Unit (SKU) of the product reservation to transfer.

**–** `toLocationGroupIdentifier` —The identifier of the location group receiving the reservation.
Either `toLocationGroupIdentifier` or `toLocationIdentifier` is required, but not
both.

**–** `toLocationIdentifier` —The identifier of the location receiving the reservation. Either
`toLocationIdentifier` or `toLocationGroupIdentifier` is required, but not both.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

Transfer

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCITransferReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCITransferReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_error_output.htm)
and has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCITransferReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_single_output.htm)
error and includes the fields from the input:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `fromLocationGroupIdentifier` —The identifier of the location group transferring the
reservation.

**•** `fromLocationIdentifier` —The identifier of the location transferring the reservation.

**•** `ignoreAvailabilityCheck` —Whether this call ignored availability data at the location
that received the reservation.

**•** `quantity` —The quantity of the product reservation to transfer.

**•** `stockKeepingUnit` —The SKU of the product reservation to transfer.

**•** `toLocationGroupIdentifier` —The identifier of the location group intended to receive
the reservation.

**•** `toLocationIdentifier` —The identifier of the location intended to receive the reservation.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the transfer succeeded.

To set up the Omnichannel Inventory Service Transfer Reservation Input:


Automate Your Business Processes with Salesforce Flow Flow Reference

**1.** For each reservation to transfer, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`fromLocationGroupIdentifier` or `fromLocationIdentifier`, `quantity`, `stockKeepingUnit`, and
`toLocationGroupIdentifier` or `toLocationIdentifier` field values on a
`ConnectApi.OCITransferReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCITransferReservationSingleInputRepresentation`
variables to the `transferRecords` field on a `ConnectApi.OCITransferReservationInputRepresentation`
variable.

**3.** Use an Assignment element to set the `allOrNothingTransferId` field on the
`ConnectApi.OCITransferReservationInputRepresentation` variable.

**4.** Use the `ConnectApi.OCITransferReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Actions: Send Conversation Messages

Send a messaging component to one or more messaging users in enhanced WhatsApp, enhanced
Apple Messages for Business, enhanced SMS, or Messaging for In-App.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Messages`_, and
##### select Send Conversation Messages .

Set Input Values


EDITIONS

Available in: Lightning
Experience

Available
in: Enterprise, Unlimited,
and Developer Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

Here’s an example of the Send Conversation Messages action in a simple flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

To track messages sent by this action, query the ConvMessageSendRequest object.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Send Custom Notification

Add the Send Custom Notification action to a flow, then add recipients and content.

Important: The Send Custom Notifications user permission is enforced in orgs created in
Winter ’21 or later.

The Send Custom Notifications user permission isn’t required to trigger the Send Custom
Notification action in processes or flows that run in system context.

Tip:

**•** Before you begin, make sure that the custom notification type you want to call from your
[process exists. If not, create the notification type.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_custom_type.htm&language=en_US)

**•** To query for the Notification Type ID directly from a flow, add the Get Record element to
your flow and filter by API name. If you’ve installed a notification type via a managed
package, filter by the namespace prefix as well as the API name.

**•** To add recipients, define Recipient ID as a resource. Then add values to your Recipient ID
collection by adding the Assignment element to your flow.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Notifications`_,
##### and select Send Custom Notification .

Set Input Values

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To trigger the Send Custom
Notification action in flows
that run in user context, REST
API calls, and Apex callouts:
##### • Send Custom

Notifications

Use values from earlier in the flow to set the inputs for the email. Specify at least one recipient for the email.

**Field** **Description**

`Custom Notification` The ID of the Custom Notification Type being used for the notification.
```
Type ID
```

This parameter accepts single-value resources of any type. That value is treated as text.

`Notification Body` The body of the notification that recipients see.

[The content of mobile push notifications depends on the Display full content push notifications](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)
[setting.](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)

This parameter accepts single-value resources of any type. That value is treated as text and is limited
to 750 characters.

`Notification Title` The title of the notification as seen by recipients.

This parameter accepts single-value resources of any type. That value is treated as text and is limited
to 250 characters.

`Recipient IDs` The ID of the recipient or recipient type of the notification.

Valid values are:

**•** _`User ID`_ —The notification is sent to this user, if this user is active.

**•** _`Account ID`_ —The notification is sent to all active users who are members of this account’s
Account Team. Valid only if account teams are enabled for your org.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

**•** _`Opportunity ID`_ —The notification is sent to all active users who are members of this
opportunity’s Opportunity Team. Valid only if team selling is enabled for your org.

**•** _`Group ID`_ —The notification is sent to all active users who are members of this group.

**•** _`Queue ID`_ —The notification is sent to all active users who are members of this queue.

This parameter accepts collection variables of type Text and is limited to 500 values. The values that
you enter for an individual Send Custom Notification action can represent a total of up to 10,000 users
as recipients.

`Target ID` Optional. The Record ID for the target record of the notification.

Specify either a Target ID or a Target Page Reference.

This parameter accepts single-value resources of any type. That value is treated as text.

`Target Page` Optional. The Page Reference for the navigation target of the notification.
```
   Reference
```

Specify either a Target ID or a Target Page Reference.

This parameter accepts single-value resources of any type. That value is treated as text.

[To see how to specify the target using JSON, see pageReference.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_navigation_page_definitions.htm)

`Sender ID` Optional. The User ID of the sender of the notification.

This parameter accepts single-value resources of any type. That value is treated as text.

Usage

**•** Each notification can have up to 10,000 users as recipients. However, you can add an action to the same process within Process
Builder or to the same flow in Flow Builder to have more recipients.

**•** Your org saves your most recent 1 million custom notifications for view in notification trays. Your org can save up to 1.2 million
custom notifications, but it trims the amount to the most recent 1 million notifications when you reach the 1.2 million limit.

**•** An org can execute up to 10,000 notification actions per hour. When you exceed this limit, no more notifications are sent in that
hour, and all unsent notifications are lost. Notification actions resume in the next hour.

For example, your notification action processes are triggered 10,250 times between 4:00 and 4:59. Salesforce executes the first 10,000
of those actions. The remaining 250 notifications aren’t sent and are lost. Salesforce begins executing notification actions again at
5:00.

SEE ALSO:

[Create and Send Custom Desktop or Mobile Notifications](https://help.salesforce.com/s/articleView?id=sf.notif_builder_custom.htm&language=en_US)

Flow Run Context

Flow Elements

Add and Edit Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Send Email

Send and optionally log an email by specifying the email content and recipients in a flow. If you’re
using Marketing Cloud Growth, use the Send Email Message on page 377 element to send an email
to your audience segment.

Note: If you're using Marketing Cloud Growth, use the Send Email Message action instead
of the Send Email action. The Send Email action doesn't work with audience segments.

Before you begin:

**•** Use a Get Records element to get the email template to use, using the Email Template object
and filtering by the **Name** (Email Template Name) field.

**•** Then, in `Email Template ID`, select the ID of the record found by the Get Records. For
example, if you labeled your Get Records element _`Get Email Template`_, select **Email**
**Template from Get_Email_Template** .

**•** Then, select **Id** (Email Template ID).

##### In Flow Builder, search for Send Email in the element menu, and select Send Email .

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Important: If the Sender Type is OrgWideEmailAddress, ensure that the user running the flow has the proper profile configurations
required by the specific org-wide email address being used. Proceeding without the proper configuration results in an error.

Set Input Values

To set the inputs for the email, use values from earlier in the flow. Specify at least one recipient for the email.

Example: You want to send and log an email to a contact record, and also log to its related account record. For the email content,
you want to use an email template with Contact and Account merge fields. Set `Email Template ID` to the ID of the email
template to use. Next, set `Log Email on Send` to **{!$GlobalConstant.True}** . Then, set `Recipient ID` to the contact
record’s ID and `Related Record ID` to the account record’s ID.

**Input Parameter** **Description**

```
Add Threading Token

to Body

Add Threading Token

to Subject

```

Optional. Indicates whether to create a unique token for the related record and add it to the email
body.

When the related record is a case record, Email-to-Case uses the token to link future email responses
to that case.

To link future email responses to other records, create an Apex Email Service and use the
`EmailMessages.getRecordIdFromEmail` function to find the record that matches the
token.

Optional. Indicates whether to create a unique token for the related record and add it to the email
subject.

When the related record is a case record, Email-to-Case uses the token to link future email responses
to that case.

To link future email responses to other records, create an Apex Email Service and use the
`EmailMessages.getRecordIdFromEmail` function to find the record that matches the
token.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
BCC Recipient

Address List

Body

CC Recipient Address

List

Email Template ID

```

Optional. A comma-delimited list of recipient email addresses to send a copy of the email to. Email
addresses in the BCC list are hidden from all recipients.

This parameter accepts single-value resources of any type. The value is treated as text.

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

The body of the email.

Optional if you’re using an email template. The email template overrides the entry in this field.

Required if you’re not using an email template.

Enter text or select a single-value resource of any type that contains your content, for example, a Text
Template resource.

If entering text, the value is treated as plain text. If you’re using a resource, the value can be treated
as plain text or rich text, depending on your selection in `Rich-Text-Formatted Body` .

Optional. A comma-delimited list of recipient email addresses to send a copy of the email to.

This parameter accepts single-value resources of any type. The value is treated as text.

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of the Classic or Lightning email template to use for the email subject and body.

If the email template has merge fields from an object other than the one associated with `Recipient`
`ID`, specify the record used to supply those merge fields in `Related Record ID` .

If you’re using this parameter, `Recipient ID` is required.

This parameter can be used with `Log Email on Send` .

Using email templates in the Send Email action changes the API called by the action, which changes
[the daily email send limit to the General Email Limit instead of the Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)

`Log Email on Send` Optional. Indicates whether to log the email on the specified records’ activity timelines and activity
history. Valid values are:

**•** **{!$GlobalConstant.True}** —Log the email to the record associated with `Recipient ID`,
`Related Record ID`, or both.

**•** **{!$GlobalConstant.False}** —Don’t log the email to a record. This value is the default.

To log an email, you must specify a value for `Recipient ID`, `Related Record ID`, or both.

This parameter can be used with `Email Template ID` .

Logging emails with the Send Email action changes the API called by the action, which changes the
[daily email send limit to the General Email Limit instead of the Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Recipient Address

Collection

Recipient Address

List

Recipient ID

Related Record ID

```

Optional. A collection of the recipients' email addresses.

This parameter accepts collection variables of type Text.

If `Log Email on Send` is set to **{!$GlobalConstant.True}**, the email is logged to the ID specified
for `Recipient ID`, not the records associated with the email addresses in `Recipient`
`Address Collection` .

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. A comma-delimited list of the recipients' email addresses.

This parameter accepts single-value resources of any type. The value is treated as text.

If `Log Email on Send` is set to **{!$GlobalConstant.True}**, the email is logged to the ID specified
for `Recipient ID`, not the records associated with the email addresses in `Recipient`

```
Address List

```

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of a lead or a contact record.

Required if `Email Template ID` is specified.

If `Log Email on Send` is included, this parameter is the ID of the person to send and log the
email to.

If `Email Template ID` is included, this parameter is the ID of the person to send an email to
and populate recipient merge fields with.

If the ID entered in this parameter is a lead record, you can’t use `Related Record ID` .

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of a non-recipient record. For example, the ID of a case record.

If `Log Email on Send` is included, this parameter is the ID of a secondary record to log the
email to.

If `Email Template ID` is included, this parameter is the ID of the non-recipient record used
to populate email template merge fields.

You can’t use this parameter if the ID entered in `Recipient ID` is a lead record.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Rich-Text-Formatted` Optional. Indicates whether you want the resource specified for the `Body` parameter to use rich
`Body` text. Valid values are:

**•** **{!$GlobalConstant.True}** —Use rich text for the email body.

**•** **{!$GlobalConstant.False}** —Use plain text for the email body. This value is the default.

```
Sender Email Address

```

Optional. The organization-wide email address that’s used to send the email.

Required when `Sender Type` is set to _`OrgWideEmailAddress`_ .

Required when the running flow user is the guest user.

This parameter accepts a single-value resource of any type. The value is treated as text.

`Sender Type` Optional. The type of sender that the email is sent from. Valid values are:

**•** _`CurrentUser`_ —The email address of the user running the flow. This value is the default.

**•** _`DefaultWorkflowUser`_ —The email address of the default workflow user.

**•** _`OrgWideEmailAddress`_ —The organization-wide email address that is specified in `Sender`
`Email Address` . When the running flow user is the guest user, the `Sender Email`
`Address` must be set to a verified organization-wide email. Emails sent from the guest user
and not using a verified organization-wide email are blocked.

```
Subject

```

The subject of the email.

Optional if you’re using an email template. The email template overrides the entry in this field.

Required if you’re not using an email template.

Enter text or select a single-value resource of any type that contains your content, for example, a Text
Template resource. The value is treated as plain text.

`Use Line Breaks` Optional. Indicates whether to render the line breaks in the rich-text-formatted body text template.
Valid values are true and false. The default value is false.

Usage

At run time, the email isn’t sent until the interview’s transaction completes. Transactions are complete when the interview either finishes
or executes a Screen, Local Action, or Wait element. Before activating your flow, confirm that your org can send email in **Setup** **Deliverability** - **Access to Send Email (All Email Services)** - **All email** .

If you set Email Deliverability to No Access and:

**•** If you don't set `Email Template ID` or `Log Email on Send` fields, the flow runs but doesn't send the email.

**•** If you do set `Email Template ID` or `Log Email on Send` fields, the flow returns an error when it sends the email.

Setup Configurations for Scheduled Flows

If you use the Send Email action element in a Scheduled-Triggered flow, you must configure the organization-wide email address in
Setup.

**•** Set the organization-wide email address in **Setup** - **Email** - **Organization-Wide Email Addresses**

**•** Add the organization-wide email address in **Setup** - **Process Automation Settings** - **Automated Process User Email Address**


Automate Your Business Processes with Salesforce Flow Flow Reference

Email Sending Limits

**•** If you’re using `Log Email on Send` or `Email Template ID`, the daily email send limit is based on the single email limit.
[For details, see General Email Limits.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)

**•** If you’re not using `Log Email on Send` or `Email Template ID`, the daily email send limit is based on the daily workflow
[email limit. For details, see Proactive Alert Monitoring: Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000382442&type=1&language=en_US)

Considerations

**•** Emails sent using the Send Email action don't include email signatures from My Email Settings. To include a signature, add one to
the email template, flow text template, or other resource used in the Send Email action.

**•** If the `Related Record ID` is set as a Case ID by the flow, Customer Community users can't create an `EmailMessage`
[record. For details, see Experience Cloud User Licenses.](https://help.salesforce.com/s/articleView?id=sf.users_license_types_communities.htm&language=en_US)

SEE ALSO:

Add and Edit Elements

Options for Sending Emails from Flows

Flow Resource: Text Template

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Options for Sending Emails from Flows

Flow Core Action: Send Notification Actions

Call a notification type to send. Each Send Notification action corresponds to a supported notification
type. Send Notification actions are available only for Slack-enabled custom notification types and
certain Slack-enabled standard notification types.

Note: [To send notifications for Slack, enable Salesforce for Slack Integrations.](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

[To create a custom Slack notification type supported by a Send Notification action, see Create](https://help.salesforce.com/s/articleView?id=sf.notif_builder_create_send_slack.htm&language=en_US)
[and Send Custom Slack Notifications.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_create_send_slack.htm&language=en_US)

Add an Action element to the flow. In the Action field, select the Send Notification-supported
notification type that you want to configure. Each Send Notification action corresponds to a
supported notification type. For example, if you created a custom notification type named My
Opportunity Notification, look for the My Opportunity Notification action in the Notifications category.

Set Input Values

Use values from earlier in the flow to set the inputs for the notification type.

**Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To trigger a Send Notification
action in flows that run in
user context and REST API
calls:

**•** Send Custom
Notifications

```
Recipient IDs

```

Required. The IDs of the notification recipients or recipient types.

[The value must be a collection variable that represents one or more](https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_variable_populate.htm&language=en_US)
Salesforce User IDs or Collaboration Room IDs.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

Some Salesforce features link standard objects to Collaboration Room through the Swarm object. For
these features, you can find an existing Collaboration Room ID from the Swarm object.

The collection variable’s Data Type must be Text. The collection can have up to 500 values.

```
Record ID

```

Required. The ID of the record that the notifications are about. The record ID must be an ID from the
Salesforce object related to the notification type. For example, enter the record ID for an opportunity
when configuring a notification type associated with the Opportunity object.

For custom notification types, you can find the related object by viewing the notification type's
settings from Custom Notifications in Setup. For supported standard notification types, refer to the
Standard Notification Types and Related Objects table.

Enter a record ID or select a variable that identifies the record.

This parameter accepts single-value resources of any type. That value is treated as text.

Standard Notification Types and Related Objects

Use this table to identify which object applies to each standard notification type that’s supported by a Send Notification action. The
object determines the value that you enter for `Record Id` .

**Standard Notification Type** **Related Salesforce Object**

`Amount Updated` Opportunity

`Close Date Reminder` Opportunity

`Close Date Updated` Opportunity

`Deal Won` Opportunity

`Deals to Watch` Opportunity

`High Priority Case` Case

`New Allergy` Allergy Intolerance
```
Intolerance

```

`New Child` Opportunity
```
Opportunity

```

`New Care Determinant` Care Determinant

`New Health Condition` Health Condition

`New or Updated Care` Task
```
Plan Task

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Standard Notification Type** **Related Salesforce Object**

`Next Step Reminder` Opportunity

`Stage Reminder` Opportunity

`Stage Updated` Opportunity

`Updated Care Plan` Case

Usage

**•** Each notification can have up to 10,000 users as recipients. However, you can add another action to the same flow in Flow Builder
to have more recipients.

**•** You can save up to 1.2 million custom notifications, but notification trays show only your most recent 1 million custom notifications.

**•** You can execute up to 10,000 notification actions per hour. When you exceed this limit, no more notifications are sent in that hour,
and all unsent notifications are lost. Notification actions resume in the next hour.

**•** The sending rates of Slack notifications are also subject to the limits of the Slack service.

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_collaborationroom.htm)_ : CollaborationRoom

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_swarm.htm)_ : Swarm

Flow Core Action: Send Surveys

Create an action to send an active survey by specifying the name, subject, recipients, and invitation
link options in the flow.

In Flow Builder, add an Action element to your flow. In the Action field, enter the name of an active
survey. Or, in the left navigation, click **Survey**, and then in the Action field, select an active survey.
Define the name of the action and the survey recipients.

Note: If you deactivate a survey after it’s added to a flow and then activate it, the Flow Builder
renders an incorrect Action layout for that survey.

Example: You want to collect feedback from all the participants when a case is closed. First,
create a flow and get all records where the status of the case object is closed. Then, create
an action that selects the survey to send to the participants for feedback.

Set Input Values

Specify at least one recipient for the survey.

**Field** **Description**

`Label` Name for the action.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

```
API Name

```

Associate an API name for the action.

This parameter auto-generates the API name based on the label, which you can edit, if necessary.

`Description` Optional. Description about the purpose of the action.

```
Survey Subject

Recipient Type

```

Optional. Select a survey subject that you want to perform the action on. For example, to get all case
records, select the survey subject as Case, or create a required resource for the subject.

This parameter accepts flow variables of type Text.

Select the type of recipient of the survey. Choose the Lead or Contact recipient type only when there’s
a default Experience Cloud site selected for sending public surveys.

This parameter accepts flow variable of type Text.

`Unique link` Optional. Each participant receives a unique survey invitation. The responses are mapped to the
participant name.

`Anonymize responses` Optional. The responses received aren’t mapped to any participant.

`Don’t require` Optional. By default, surveys sent to lead or contact require authentication. However, you can enable
`authentication` this option to allow access to the survey without any authentication.

`Invitation expires` Optional. Define the number of days after which the access to the survey is restricted.

```
in days

```

SEE ALSO:

Add and Edit Elements

Flow Core Action: Perform Survey Sentiment Analysis

Get insights into the sentiments that underlie survey responses.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Sentiment`_, and
##### select Perform Survey Sentiment Analysis . Or, in the left navigation, click Survey, enter Sentiment in the Action field, and select Perform Survey Sentiment Analysis . Define the

name of the action and the survey recipients.

To access this action from the API, use the name `performSurveySentimentAnalysis` .

Set Input Values

**Field** **Description**

`End Date` Required. The date until when participant responses are processed to get
sentiment insights.

`Operation` Required. The action performed on the AI Sentiment Result records.

**•** **Create** : Use the create operation when sentiment analysis is yet to
be done on survey responses and there are no associated AI Sentiment


EDITIONS

Available in: both Salesforce
Classic (not available in all
orgs) and Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Available with Survey
Response Pack, Feedback
Management - Starter, and
Feedback Management Growth licenses

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

Result records, or to analyze the sentiment again. After the processing is completed, AI Sentiment
Result records are created with the sentiment of the survey responses and with the Submitted
status.

**•** **Update** : Use the update operation to bulk process survey responses that have associated AI
Sentiment Result records in Draft status. After the processing is completed, the AI Sentiment
Result records are updated with the sentiment of the survey responses and their status is changed
to Submitted.

`Question IDs` Required. The IDs of the questions for whose responses you want to get sentiment insights.

`Start Date` Required. The date from when participant responses are processed to get sentiment insights.

`Survey ID` Required. The ID of the survey containing the questions for whose responses you want to get sentiment
insights.

Usage

At run time, the AI Sentiment Result record isn’t created until the interview’s transaction is completed. After the transactions are completed,
AI Sentiment Result records are created with Completed status.

Flow Core Action: Get Assessment Response Summary

Create a printable summary view of assessments taken. This action enables you to extract responses
saved in an assessment and create a flow to generate a document.

In Flow Builder, add an Action element to your flow. In the Action field, search for Get Assessment
Response Summary invocable action to configure.

Set Input Values

**Field** **Description**

`assessmentId` Required. The ID of the assessment record for which to summarize responses.

Set Output Values

**Set Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`assessmentResponseSummary` A JSON string containing the summary assessment question texts and responses for the specified assessment
record.

Usage

##### Get Assessment Response Summary makes it easy to use a flow to trigger server-side document generation using Docgen. You can use

this invocable action to pass assessment summary data to the downstream processes. This invocable action provides a summary JSON
that can be consumed in Docgen workflows to generate documents.


Automate Your Business Processes with Salesforce Flow Flow Reference

The Get Assessment Response Summary invocable action takes assessment ID as the input to get the OmniProcess ID, which is used to
retrieve the OmniProcess elements. The assessment ID also retrieves the assessment response and merges the response with the
OmniProcess elements to create an assessment summary response in JSON.

DocGen Limitations

OmniScript doesn’t provide a modification history of the same OmniScript form, such as the addition or removal of questions. It’s
recommended that you trigger the document generation when you submit an assessment. The summary API fetches the layout data
from the active version of the OmniScript.

DocGen has the following limits:

**•** Token data is limited to 131,072 characters.

**•** Server-side document generation - Maximum supported document size is 1 MB.

**•** Client-side document generation - Maximum supported document size is 10 MB.

**•** There’s no image-type support for server-side document generation. Image-type support is only available on the client-side.

##### Slack Flow Core Actions

Manage Slack channels, channel members, and messages from flows. As your Salesforce records
change, a flow can trigger changes in Slack.

Important: Slack core actions execute in user context. The flow has access to whatever the
running user of the flow has access to.

Before using a core action for Slack, enable Salesforce for Slack integrations.

##### In Flow Builder, add an Action element to your flow. Select the Slack category, and search for an

action.

Flow Core Actions for Slack: Archive Slack Channel
Archive a Slack channel in a Slack workspace.

Flow Core Actions for Slack: Check If Users Are Connected to Slack
Determine whether a collection of Salesforce users is connected to a given Slack workspace.

Flow Core Actions for Slack: Create Slack Channel
Create a Slack channel in a Slack workspace.

Flow Core Actions for Slack: Edit Slack Message
Edit a message that was previously sent to Slack.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow Core Actions for Slack: Get Information About Slack Conversation
Retrieve the name of a Slack channel and find out whether it’s archived. Archived channels are closed to new activity, but users can
still view and search an archived channel’s message history.

Flow Core Actions for Slack: Invite Users to Slack Channel
Add users who are connected to a given Slack app to a Slack channel or direct message.

Flow Core Actions for Slack: Pin or Unpin Slack Message
Pin or unpin a message in a Slack channel or direct message. Pin messages so that they’re readily available from the conversation
header.

Flow Core Actions for Slack: Send Slack Message
Send a message to a Slack channel, direct message, or the Messages tab of a Slack app.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Message to Launch Flow
Send a message to a Slack channel, direct message, or the Messages tab of a Slack app that includes a button that a recipient can
use to launch a screen flow.

Flow Core Actions for Slack: Archive Slack Channel

Archive a Slack channel in a Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Archive Slack Channel .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Channel

**Input Parameter** **Description**

```
Slack Channel ID

```

Required. The ID of the channel to archive.

Get the Slack channel ID by logging in to Slack.com and launching Slack in your browser.
The channel ID is the last parameter in the URL. For example, in this URL, the channel ID
is `C56789FGHIJ` :


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
                    https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Check If Users Are Connected to Slack

Determine whether a collection of Salesforce users is connected to a given Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Check If Users Are Connected to Slack .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com
and launching Slack in your browser. The workspace ID is the
penultimate parameter in the URL. For example, in this URL, the
workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Salesforce User ID` Required. The collection resource that contains the Salesforce
`Collection Resource` user IDs to check. The maximum number of user IDs is 1,000.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

`Collection of Salesforce` A collection resource that contains the Salesforce user IDs connected to Slack.

```
   User IDs Connected to Slack

```

`Collection of Salesforce` A collection resource that contains the Salesforce user IDs not connected to Slack.

```
   User IDs Not Connected to

   Slack

```

Usage

This action is available only if you enable the connection to Slack in Setup. Otherwise, the action fails. Additionally, the user that initiates
the flow and any users impacted by the action must have logged in to a Salesforce Slack app at least once.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Create Slack Channel

Create a Slack channel in a Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Create Slack Channel .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Slack Channel Details

**Input Parameter** **Description**

`Slack Channel Name` Required. The name of the new channel. Specify a value or select a resource.

`Channel Type` Select a value or Boolean resource. Valid values are:

**•** Public

**•** Private

**•** Resource

If you select a Boolean resource that evaluates to true, the channel type is private. If you
select a Boolean resource that evaluates to false, the channel type is public. The default
channel type is public.

`Slack Workspace ID for` Indicates whether to associate the new channel with a different workspace ID than the
`Channel` workspace ID of the Slack app. If you turn on this option, select a value or resource.

Store Output Values

**OUTPUT Parameter** **Description**

`Slack Channel ID` The ID of the new channel.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Edit Slack Message

Edit a message that was previously sent to Slack.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Edit Slack Message .

Set Input Values

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App ID for

Token

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

The Slack app must be a member of the conversation that
contains the message to edit.

`Slack Conversation` Required. The ID of the channel or the direct message to send
`ID` the message to. Alternatively, specify a Slack user ID if the
message was sent to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to
Slack.com and launching Slack in your browser. The conversation
ID is the last parameter in the URL. For example, in this URL, the
conversation ID is `C56789FGHIJ` :

```
            https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Slack Message` Required. The message to send. Use alongside Post Message
action. For best results, include no more than 4,000 characters.

Slack truncates messages containing more than 40,000
characters. Enter a value or select a resource. This action only
supports editing messages with standard markdown formatting.

Slack supports text formatting with Slack `mrkdown` . To disable
formatting for a plain text message that contains Slack
`mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders
rich text messages as plain text.

```
Slack Message

Timestamp

```

Required. The timestamp of the message sent. Enter a value or
select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix
timestamp. The numerals after the period character specify
microseconds.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

```
Slack Workspace ID for Token

```

Usage

Required. The Slack workspace where the Slack app is installed. Select a value or resource.
The input value evaluates to the Slack workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com and launching Slack
in your browser. The workspace ID is the penultimate parameter in the URL. For example,
in this URL, the workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Get Information About Slack Conversation

Retrieve the name of a Slack channel and find out whether it’s archived. Archived channels are
closed to new activity, but users can still view and search an archived channel’s message history.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Get Information About Slack Conversation .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

The Slack app must be a member of the conversation to execute the action on.

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Slack Conversation

**Input Parameter** **Description**

```
Slack Conversation ID

```

Store Output Values

Required. The ID of the channel to retrieve information about.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

**Output Parameter** **Description**

`Conversation Is Archived` Indicates whether the conversation is archived.

`Conversation Is Shared` Indicates whether the conversation is shared with people outside of your org that aren't
`Externally` part of your Enterprise Grid in Slack.

`Slack Conversation ID` The ID of the Slack conversation that you retrieved information about.

`Slack Conversation Name` The name of the Slack conversation that you retrieved information about.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Invite Users to Slack Channel

Add users who are connected to a given Slack app to a Slack channel or direct message.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Invite Users to Slack Channel .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Channel Details

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

```
Slack Channel ID

```

Required. The ID of the channel or direct message to invite users to.

You can obtain the Slack channel ID by logging in to Slack.com and launching Slack in
your browser. The channel ID is the last parameter in the URL. For example, in this URL,
the channel ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Slack Workspace ID for

Channel

```

Required. The Slack workspace that contains the channel. Select a value or resource. The
input value evaluates to the Slack workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com and launching Slack
in your browser. The workspace ID is the penultimate parameter in the URL. For example,
in this URL, the workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Salesforce User ID` The collection resource that contains the Salesforce user IDs to invite to the channel. The
`Collection Resource` maximum number of user IDs is 1,000.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails. Additionally, the user that initiates the flow and any users impacted by the action must have logged in to a Salesforce
Slack app at least one time.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Pin or Unpin Slack Message

Pin or unpin a message in a Slack channel or direct message. Pin messages so that they’re readily
available from the conversation header.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Pin or Unpin Slack Message .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

The Slack app must be a member of the conversation to execute the action on.

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

Slack Message Timestamp

Pin or Unpin Message

```

Usage

Required. The ID of the channel or group direct message to send the message to. Enter
a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

Required. The timestamp of the sent message. Enter a value or select a resource. For
example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

Select a value or Boolean resource. Valid values are:

**Pin**
Pins the message to the conversation header.

**Unpin**
Unpins the message from the conversation header.

If you select a Boolean value that evaluates to true, the action pins the message. If you
select a Boolean value that evaluates to false, the action unpins the message. The default
is Pin.

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Slack Message

Send a message to a Slack channel, direct message, or the Messages tab of a Slack app.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Send Slack Message .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

```

Required. The ID of the channel or direct message to send the message to. Alternatively,
specify a Slack user ID to send the message to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Slack Message

```

Required. The message to send. For best results, include no more than 4,000 characters.
Slack truncates messages containing more than 40,000 characters. Enter a value or select
a resource.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

`Salesforce Record ID` [The record ID to send to the view. Defining a view is a pilot feature. For more information,](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views.html)
[see Define a View in the](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views_create.html) _Apex SDK for Slack (Pilot) Guide_ .

```
Slack Message Timestamp

```

The timestamp of the Slack message. Specify a timestamp to start a Slack thread. Enter a
value or select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

`View API Name` [The API name of the view that the Slack message is sent with. Defining a view is a pilot](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views.html)
[feature. For more information, see Define a View in the](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views_create.html) _Apex SDK for Slack (Pilot) Guide_ .

Store Output Values

**OUTPUT Parameter** **Description**

`Slack Message Timestamp` The timestamp of the sent message.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Message to Launch Flow

Send a message to a Slack channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
then select the name of the flow to send.

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com
and launching Slack in your browser. The workspace ID is the
penultimate parameter in the URL. For example, in this URL, the
workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set Slack Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

```

Required. The ID of the channel or the direct message to send the message to. Alternatively,
specify a Slack user ID to send the message to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Slack Message` Required. The message to send. For best results, include no more than 4,000 characters.
Slack truncates messages containing more than 40,000 characters. Enter a value or select

a resource. The message to send can’t be edited. Using the Edit Message action or manual
editing results in process failures.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

```
Button Label

```

Required. The label for the button that appears below the message. The user clicks the
button to launch the flow from Slack.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

`Slack Bot Name` The name of the bot that sends the message in Slack. Enter a value or select a resource.

```
Slack Message Timestamp

```

Store Output Values

The timestamp of the Slack message. Specify a timestamp to start a Slack thread. Enter a
value or select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

**Input Parameter** **Description**

`Slack Message Timestamp` The timestamp of the message sent.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Action: Submit for Approval

Submit one Salesforce record for approval.

Tip: Before you begin, store the ID for the record that you want to submit for approval in a
variable.

##### In Flow Builder, add an Action element to your flow. In the Action field, enter Submit, and select Submit for Approval .

Set Input Values

Use values from earlier in the flow to set the inputs for the approval request.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Record ID

Approval Process

Name or ID

Next Approver IDs

Skip Entry Criteria

```

The ID of the record that you want to submit for approval.

This parameter accepts single-value resources of any type. That value is treated as text.

The unique name or ID of the approval process that you want to submit the record to. The process
must have the same object type as the record you specified in `Record ID` .

Required if `Skip Entry Criteria` is set to _`true`_ .

If this parameter and `Submitter ID` aren’t set, the flow succeeds only when: Make sure that:

**•** The approver on submit is determined automatically, and

**•** The user who launched the flow is an allowed initial submitter

**•** The approver on submit is determined automatically.

**•** The initial submitters for the approval processes related to this object include all users who could
launch this flow.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the user to be assigned the approval request when the approval process doesn’t assign the
approver.

This parameter accepts collection variables of type Text that include exactly one item.

If set to _`true`_, the record isn’t evaluated against the entry criteria set on the process that is defined
in `Approval Process Name or ID` .

This parameter accepts any single-value resource of type Boolean.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Submission Comments

Submitter ID

```

Store Output Values

Text that you want to accompany the submission. Don’t reference merge fields or formula expressions.

Submission comments appear in the approval history for the specified record. This text also appears
in the initial approval request email if the template uses the `{!ApprovalRequest.Comments}`
merge field.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID for the user who submitted the record for approval. The user receives notifications about
responses to the approval request.

The user must be one of the allowed submitters for the process.

If you don’t set this field, the user who launched the flow is the submitter. If a workflow rule triggers
a flow that includes this element, the submitter is the user who triggered the workflow rule. Workflow
rules can be triggered when a user creates or edits a record. When the record is approved or rejected,
the user who launched the flow or triggered the workflow rule is notified.

This parameter accepts single-value resources of any type. That value is treated as text.

To use the approval request’s outputs later in the flow, store them in variables. The values are assigned when the approval request is
created.

**Optional Output** **Description**
**Parameter**

```
Instance ID

Instance Status

New Work Item IDs

Next Approver IDs

Record ID

```

The ID of the approval request that was submitted.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.

The status of the current approval request. Valid values are Approved, Rejected, Removed, or Pending.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.

The IDs of the new items submitted to the approval request. There can be 0 or 1 approval processes.

This parameter accepts collection variables of type Text.

The IDs of the users who are assigned as the next approvers.

This parameter accepts collection variables of type Text.

The ID of the record that the flow submitted for approval.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

At run time, the approval request isn’t created until the interview’s transaction is completed. Transactions are complete when the
interview either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Flow Elements

Add and Edit Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

##### Salesforce Anywhere Core Flow Actions (Beta)

Salesforce Anywhere provides several core actions for implementing Salesforce Anywhere
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the Salesforce Anywhere category, and search for the appropriate action.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

These actions are available when you enable Salesforce Anywhere.

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

Flow Core Action for Salesforce Anywhere: Create a Salesforce Anywhere Chat (Beta)
Create a Salesforce Anywhere chat by specifying participants, and optionally, an initial message and chat title.

Flow Core Action for Salesforce Anywhere: Add a Message to a Salesforce Anywhere Chat (Beta)
Add a message to an existing Salesforce Anywhere chat by specifying the chat URL and message content.

Flow Core Action for Salesforce Anywhere: Add Users to a Salesforce Anywhere Chat (Beta)
Add users to an existing Salesforce Anywhere chat by specifying the chat URL and the users to be added.

Flow Core Action for Salesforce Anywhere: Send Salesforce Anywhere Alerts to Users (Beta)
Notify users about Salesforce Anywhere chat by specifying the chat URL and the users to be added.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Salesforce Anywhere: Create a Salesforce Anywhere Chat (Beta)

Create a Salesforce Anywhere chat by specifying participants, and optionally, an initial message
and chat title.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`chat`_ . Select **Create Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the chat.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatMessage

userEmails

```

Store Output Values

The first message sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

A comma-separated list of email addresses belonging to one or more users getting added to the chat. Must
list at least two email addresses and no more than 50 email addresses.

Email addresses must be part of your Salesforce Anywhere organization. If an email address isn’t included in
your Salesforce Anywhere organization, the user isn’t included in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
chatId

chatTitle

chatUrl

```

Usage

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The name users see at the top of the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.

In Flow Builder, this action doesn’t check the number of email addresses or the validity of the email addresses. When either criteria is
invalid, the flow fails at run time.


Automate Your Business Processes with Salesforce Flow Flow Reference

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Add a Message to a Salesforce Anywhere Chat (Beta)

Add a message to an existing Salesforce Anywhere chat by specifying the chat URL and message
content.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`message`_ . Select **Add Message to Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the message.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatUrl

chatMessage

recordId

```

Store Output Values

The chat's URL.

This parameter accepts single-value resources of any type. That value is treated as text.

The message to send to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the Salesforce record to send to the chat. The record's compact layout is displayed in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
chatId

chatMessage

chatUrl

```

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The message sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
recordId

```

Usage

The ID of the record sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

Only existing chat members can trigger this action. For example, only an existing chat member can successfully run a flow that sends a
message to a chat about a service case when that case record is updated.

A flow can’t create a record and then reference that new record ID as an input for this action.

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Add Users to a Salesforce Anywhere Chat (Beta)

Add users to an existing Salesforce Anywhere chat by specifying the chat URL and the users to be
added.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`users`_ . Select **Add Users to Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the new users.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatUrl

userEmails

```

The chat's URL.

This parameter accepts single-value resources of any type. That value is treated as text.

Required. A comma-separated list of email addresses belonging to up to 50 users getting added to the chat.

Email addresses must be part of your Salesforce Anywhere organization. If an email address isn’t included in
your Salesforce Anywhere organization, the user isn’t be included in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
chatId

chatUrl

chatTitle

```

Usage

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.

The name users see at the top of the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

In Flow Builder, this action doesn’t check the number of email addresses or the validity of the email addresses. When either criteria is
invalid, the flow fails at run time.

Only existing chat members can trigger this action. For example, only an existing chat member can successfully run a flow that adds
new users to a chat about a service case when that case record is updated.

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Send Salesforce Anywhere Alerts to Users (Beta)

Notify users about Salesforce Anywhere chat by specifying the chat URL and the users to be added.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`alert`_ . Select **Send Alert** .

Set Input Values

Use values from earlier in the flow to set the inputs for the alert.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
alertMessage

```

The message sent in the alert.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
userEmails

recordId

```

Store Output Values

A comma-separated list of the users’ email addresses.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the Salesforce record to send to the chat. The record's compact layout is displayed in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
eventOperationId

```

SEE ALSO:

The unique ID generated for the alert.

This parameter accepts single-value resources of any type. That value is treated as text.

_Platform Events Developer Guide_ [: Platform Events Considerations](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_event_extras.htm)

Add and Edit Elements

Standard Flow Screen Components

Salesforce provides several standard screen components that extend the types of input fields
available in screens.

If you need more functionality, for example, to install a custom screen component from an external
[library, have a developer build one for you.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_config_for_flow_screens_intro.htm)

Flow Screen Input Component: Action Button
Use the Action Button component so the running user can trigger a screen action with the click
of a button on a screen. The screen action runs an active autolaunched flow, and the results of
the autolaunched flow can be shown on the same screen as the button. Using this component
means that you need fewer screens so users can complete screen flows more quickly.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow Screen Input Component: Address
Simplify gathering address information by adding the Address component to a flow screen. The Address screen component displays
a complete address form that’s customized to your settings. It can also use state and country/territory picklists.

Flow Screen Input Component: Checkbox
Offer flow users a yes-or-no choice with a checkbox.

Flow Screen Input Component: Checkbox Group
Let users choose multiple options in a checkbox format.

Flow Screen Input Component: Choice Lookup
Let users search for and select one option from a set of choices on a flow screen. The component supports only Text values.

Flow Screen Input Component: Currency
Let users enter currency values from a flow screen.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Data Table
Let users select records from a table in a flow.

Flow Screen Input Component: Date
Let users enter date values from a flow screen.

Flow Screen Input Component: Date & Time
Let users enter date and time values from a flow screen, such as to request an appointment.

Flow Screen Input Component: Dependent Picklists
Display picklists in a flow screen in which the options for one picklist depend on the selected value of another picklist. The Dependent
Picklists screen component determines which options to display in each picklist by using an existing field dependency in your org.
A _field dependency_ connects two picklist fields on the same object.

Flow Screen Input Component: Display Image
Easily insert images in flow screens. Upload images to Salesforce as static resources and then you can reference them while configuring
the component.

Flow Screen Input Component: Email
Let users enter email address values from a flow screen.

Flow Screen Input Component: Enhanced Message
Let users send a messaging component in an enhanced Messaging session.

Flow Screen Input Component: File Upload
Let users upload files from a flow screen.

Flow Screen Input Component: Long Text Area
Let users enter a paragraph or two of text from a flow screen.

Flow Screen Input Component: Lookup
Let users search for and select one or more records in a flow.

Flow Screen Input Component: Multi-Select Picklist
Let users choose multiple options in a picklist format.

Flow Screen Input Component: Name
Let users enter multiple name values with one screen component. Instead of the Name screen component, you can use Text input
fields to capture name information, but it takes a lot more configuration.

Flow Screen Input Component: Number
Let users enter number values from a flow screen.

Flow Screen Input Component: Order Management Product Selector
Let users select which fields show in columns during product selector for various transaction types, such as returns or exchanges.

Flow Screen Input Component: Password
Let users enter sensitive information in a flow screen, such as a social security number. Text entered by the user is masked.

Flow Screen Input Component: Phone
Let users enter phone values from a flow screen.

Flow Screen Input Component: Picklist
Let users choose from a list of options in a picklist format.

Flow Screen Input Component: Radio Buttons
Let users choose from a list of options in a radio button format.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slack Channel Selector
Let users select a Slack channel to send a Slack message from a flow screen.

Flow Screen Input Component: Slack Workspace Selector
Let users select a Slack workspace to send a Slack message to from a flow screen.

Flow Screen Input Component: Slider
Let users visually specify number values from a flow screen.

Flow Screen Input Component: Text
Let users enter text from a flow screen, such as the name of the user’s company.

Flow Screen Input Component: Toggle
Let users flip a toggle in a flow screen.

Flow Screen Input Component: URL
Let users enter URL values in a flow screen.

Flow Screen Output Component: Display Text
Display information in a flow screen.

Flow Screen Display Component: Repeater
Collect information about multiple items of the same type on a screen with the Repeater component. To use the output of the
component elsewhere in the flow, loop over the output and save the relevant data in a variable. Use the variable to build a list of
records.

Flow Screen Output Component: Section
Organize screen components and record fields to give your users a better experience.

Flow Screen Input Component: Action Button

Use the Action Button component so the running user can trigger a screen action with the click of
a button on a screen. The screen action runs an active autolaunched flow, and the results of the
autolaunched flow can be shown on the same screen as the button. Using this component means
that you need fewer screens so users can complete screen flows more quickly.

For example, you can make it possible for users to select an account record in a Lookup component,
click a button to retrieve the contact records associated with the account record, and then display
the contact records in a Data Table component on the same screen.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Action Button Name

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

`Label` If you select Use Label as the table title, the user-friendly text that appears above the component.

```
Disabled

```

Configure the Action

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

**Attribute** **Description**

`Action` The screen action that launches the autolaunched flow. This is the flow that runs when the user clicks
the button rendered by the Action Button component. The autolaunched flow must be active.

`Label` The user-friendly name for the action associated with the component. This value can be different than
the label of the flow that you select as the action.

```
API Name

Set Input Values

View Output Values

```

The API name for the action associated with the component. This value can be different than the API
name of the flow that you select as the action.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

Specify the value of each input field required by the action associated with the component. For
example, if you select an autolaunched flow that requires an Account ID as an input, provide the
Account ID. Variables that are available for input in the autolaunched flow appear in this area.

View the outputs created by the action. To reference an output elsewhere in the flow, first reference
the Results field, for example, `actionButtonApiName. Results.output` . Variables that
are available for output in the autolaunched flow appear in this area. Output values include:

**•** ErrorMessage—Description of an error that occurred while executing the invocable action

**•** IsSuccess—If true, indicates that the invocable action ran without errors

**•** Action.Results.Flow__InterviewGuid—Unique identifier of the flow interview

**•** Action.Results.Flow__InterviewStatus—The status of the flow interview

**•** InProgress—If true, indicates that the screen action is running.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Specify Another Component’s Behavior with the In Progress Output Attribute

When a user clicks an action button, the In Progress attribute for the associated screen action is set to `true` . When the action completes,
the In Progress attribute is set back to `false` .

Use the In Progress attribute to specify another component’s behavior. For example, use it to disable a screen component while the
action is running. Set the value of the Disabled field on the component to the In Progress attribute. When In Progress is `true` the
Disabled field is also set to `true` . When the action completes and In Progress is set to `false`, the disabled field is also set to false.

Considerations

**•** If a user runs a flow with an Action Button component in a web browser, the outputs of the action associated with the component
are available to the browser. Don’t share sensitive information as the output of an Action Button component.

**•** Autolaunched flows that include Wait elements or subflows with Wait elements aren’t supported as Action Button actions because
the flow won’t resume after a Wait element.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Action Buttons aren’t supported in Repeater components.

**•** Launching a flow with an asynchronous path isn’t supported.

**•** If a flow launched from the action button doesn't have fault paths, and an error occurs, a generic error message shows under the
action button. To show a helpful error message to users instead, add fault paths to the launched flow. On each fault path, set an
output variable to `{!$Flow.FaultMessage}` . Then, on the flow screen with the action button, add a Display Text component
that's conditionally hidden and contains a helpful error message along with the fault message variable.

Note: Even if a Display Text component content contains an error message, screen readers don’t announce the content as
an error message.

**•** If an input or output variable in the screen action’s autolaunched flow is a record variable, and you change a field name on the object,
the new field name isn’t reflected when you refresh the inputs and outputs.

**•** If an input or output variable in the screen action’s autolaunched flow is an Apex variable, and you change the structure of the Apex
type, those changes aren't reflected when you refresh the inputs and outputs.

SEE ALSO:

Data Safety When Running Screen and Autolaunched Flows in System Context

_Video_ [: Action Button in Salesforce Flow](https://www.youtube.com/watch?v=GS5GAFHpVGk)

Flow Screen Actions

Flow Screen Input Component: Address

Simplify gathering address information by adding the Address component to a flow screen. The
##### Address screen component displays a complete address form that’s customized to your settings.

It can also use state and country/territory picklists.

For information about adding screen components to your flow screen, see Flow Element: Screen.

Note: This screen component requires Lightning runtime.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Address Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
City Value

Country Code

Country Options

Country Value

Disabled

Label

Postal Code Value

Required

Show Google Maps

Search Field

```

To give City a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The code for the country in the address. To give Country a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The active countries and territories configured in state and country/territory picklists. To override the
options, set this attribute to a comma-delimited set of countries and territories. This field populates a
dropdown menu of options.

This attribute accepts single-value resources. The value is treated as text.

The value for the country in the address. To give Country a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The label for the heading that appears above the group of address fields.

This attribute accepts single-value resources. The value is treated as text.

To give Postal Code a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

Indicates whether to include a search field powered by Google Maps in the component. To include
a search field, enter `true` as a boolean value. When a user selects an address in the search field, the
flow populates the other fields in the component.

The default value is `false` .

`Google Maps Search` The label that appears above the Google Maps search field.

```
Field Label

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
State or Province

Code

State or Province

Options

State or Province

Value

Street Value

```

The code for the state or province in the address. If `State/Province Options` is configured,
this value is selected by default. To give State a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The active states configured in state and country/territory picklists. To override the options, set this
attribute to a comma-delimited set of states. This field populates a dropdown menu of options.

This attribute accepts single-value resources. The value is treated as text.

The value of the state or province in the address. If `State/Province Options` is configured,
this value is selected by default. To give State a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

To give Street a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Store the Address Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
City Value

Country Code

Country Value

Postal Code Value

State or Province

Code

State or Province

Value

Street Value

```

What the user entered in the City Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Country Code field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Country Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Postal Code Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the State or Province Code field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the State of Province Value field. To update records in orgs with the State
and Country/Territory Picklists setting enabled, use State or Province Code instead.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Street Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
##### Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio

Buttons, and Text components.

**•** To update records in orgs with the State and Country/Territory Picklists setting enabled, use the Country Code and State or Province
Code outputs instead of the Country Value and State or Province Value outputs.

**•** The Google Maps search fields isn’t supported in Playground, Experience Builder sites, Lightning Out, Lightning Components for
Visualforce, and standalone apps.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Checkbox

Offer flow users a yes-or-no choice with a checkbox.

Configure the Checkbox Component

**Attribute** **Description**

```
API Name

Default Value

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Usage

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
##### Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio

Buttons, and Text components.

When the user selects the checkbox, the screen component evaluates to `true` . If the user doesn’t select the checkbox, the screen
component evaluates to `false` . If the associated screen isn’t executed, the screen component evaluates to `null` .

Example: Let users opt into a marketing campaign, agree to a follow-up call after a purchase, or confirm that they understand
an important policy.

SEE ALSO:

Flow Resource: Global Constant

Standard Flow Screen Components

Flow Screen Input Component: Checkbox Group

Let users choose multiple options in a checkbox format.

Configure the Checkbox Group Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become available:

**•** Checkbox Group

**•** Multi-select Picklist

`Data Type` Only Text choices are supported for this component.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

When a user clicks the info bubble for a Checkbox Group component, the help text appears in a separate window. For other types of
Salesforce-provided components, the help text appears in a popover.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Choice Lookup

Let users search for and select one option from a set of choices on a flow screen. The component
supports only Text values.

Configure the Choice Lookup Component

**Attribute** **Description**

`Label` User-friendly text that appears above the component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

`Require` Requires users to select a value before they can move to the next screen.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

Placeholder Text

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

`Let Users Select` Specifies whether the user can choose only one option or multiple options. The user can select up to
`Multiple Options` 25 options.

```
Choice

```

Add at least one Choice resource such as a record choice set or picklist choice set to this component.
Available only when you add a choice component to the screen component.

If you select a dynamic Choice resource such as a collection choice set or record choice set, ensure
that each value in the Choice resource is unique. Otherwise, if a user selects a duplicate value, the
value is set incorrectly in Salesforce.

You can’t reorder choices or select the same choice twice. Choices must be compatible with the
component’s `Data Type` setting.

Access the Choice Lookup Component’s Values in the Flow

The flow stores these attributes automatically. You can’t store output values for the Choice Lookup component manually.

**Attribute** **Description**

```
selectedChoiceLabels

selectedChoiceValues

```

If users can select only one option, the label of the choice option that the user running the flow
selected.

If users can select multiple options, the semi-colon separated labels of all the choice options the user
running the flow selected.

Reference the value later in the flow as `{!choiceLookup.selectedChoiceLabels}` .

If users can select only one option, the value of the choice option that the user running the flow
selected.

If users can select multiple options, the semi-colon separated values of all the choice options the user
running the flow selected.

Reference the value later in the flow as `{!choiceLookup.selectedChoiceValues}` .

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Choice Lookup flow screen component isn’t compatible with mobile devices or standalone Aura apps.

**•** The component searches for matches only in the Choice Label field of the Choice resource that you specify.

**•** Like other Choice fields, the Choice Lookup component supports the Was Selected operator.

**•** The search is case-sensitive.

**•** Initially, 20 choice options display. As you scroll, more choice options load in groups of 100, up to the maximum of 1,020.

**•** If you apply a filter after loading your initial choices, the display resets, showing the new 20 choices.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** The Choice Lookup component doesn’t support the Display text input field for Choice resources. For example, if you select the
Display text input checkbox when you configure a Choice resource and add the resource to the Choice Lookup component, the
component doesn’t display a text input field when the user selects the corresponding choice at run time.

SEE ALSO:

Choose a Lookup Option for a Flow Screen

Flow Screen Input Component: Currency

Let users enter currency values from a flow screen.

Configure the Currency Component

**Attribute** **Description**

```
API Name

Decimal Places

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Controls the number of digits to the right of the decimal point up to 17
places. If you leave this field blank or set it to zero, only whole numbers
appear when your flow runs.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The
default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Data Table

Let users select records from a table in a flow.

Configure the Data Table Name

**Attribute** **Description**

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` If you select Use Label as the table title, the user-friendly text that appears
above the component.

`Use Label as` Indicates whether to display the Label value above the table when you
`the table` run the flow.

```
title

```

Configure the Data Table Source

**Attribute** **Description**

`Source Collection` A collection of records to use to populate the table.

`Show search bar` Enables users to search and filter their record results.

Configure the Data Table Rows

**Attribute** **Description**

```
Row Selection Mode

```

Indicates how many rows the user can select in the table. You can set the value to:

**Multiple**
The user can select any number of rows between the Minimum Row Selection and Maximum
Row Selection values.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**Single**
The user can select up to one row.

**View only**
The user can’t select any rows.

`Minimum Row` Specifies the minimum number of rows that the user must select.

```
   Selection

```

`Maximum Row` Specifies the maximum number of rows that the user can select.

```
   Selection

```

`Default Selection` Collection that specifies which records to preselect in the table.

`Require user to make` Specifies whether the user must select a row before navigating to the next screen.

```
   a selection

```

Configure the Data Table Columns

To add the first column to the table, configure these fields. To add subsequent columns, click **Add column** . Drag and drop the columns
to reorder them.

**Attribute** **Description**

```
Source Field

```

Field from the Source Collection object to display in the column.

Fields with the anyType data type such as the NewValue field of the AccountHistory object aren’t
supported.

`Custom column label` Indicates whether to display the column Label value you specify as the column header.

`Label` If Custom column label is selected, the text to display as the column header. The text is also read by
screen readers.

```
Default Text

Overflow Mode

```

Specifies how text that is longer than the width of the column appears. You can set the value to:

**Wrap Text**
The screen displays the text on multiple lines.

**Clip Text**
The screen truncates the text to fit.

Note: If you're using a field that has a namespace, add the namespace to the beginning of the source field. For example, if your
field's namespace is Acme, enter _`Acme__FieldName__c`_ .

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Store the Data Table Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but most likely you must store these attributes.

**Attribute** **Description**

`First Selected Row` First record in the table selected by the flow user. If a user selects two records, this record is the first
selected record from top to bottom.

`Selected Rows` The list of records that the user selects. The records are ordered according to their position in the table
from top to bottom.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Data Table flow screen component isn’t compatible with mobile devices.

**•** If you use the Get Records flow element to retrieve the records to display in the Data Table, select Choose fields and let Salesforce
do the rest for the best performance.

**•** The maximum height of a Data Table is 400 pixels.

**•** If you choose to wrap the text in a Data Table, ensure that the text doesn’t overflow when you test your flow. Wrapped text can
overflow when a Data Table is compressed on a screen, for example, when it’s in one of multiple columns.

**•** A Data Table can display up to 1,500 records. However, your search is performed on the entire dataset.

**•** You can select up to 200 records in a Data Table.

**•** If you apply a filter after loading your initial records, only the new results are shown. The initial records are no longer included in the
display.

**•** If a Data Table includes a formula field and records or updates to records that haven’t been committed to the database, the table
doesn’t evaluate the formula properly.

For records that don’t exist in the database, update the value of the formula field with an assignment using a static value or Formula
resource. Doing so doesn’t affect any subsequent Create or Update operations in the flow.

For existing records that have been updated, use an invocable action to reevaluate the formula, or use the IN operator to refresh the
records and formula field values.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** If you include a lookup or master-detail relationship field in a Data Table, the table doesn’t display the field value. For example, a
Data Table can’t display the Name field of a related record. To display field values from related records, use object formula fields. You
can also use object formula fields to link to related record fields, for example:

```
    HYPERLINK( "/" & CASESAFEID(Id), Related_Record__r.Name, "_self" )

```

**•** You can’t search the Time field.

**•** In multi-currency orgs, the Data Table component doesn’t support records that are in a different currency from the user’s personal
currency.

**•** To display multilingual column header labels in the Data Table component, use the `$Label` global variable to specify custom
[labels. For more information about creating and translating custom labels, see Custom Labels.](https://help.salesforce.com/s/articleView?id=sf.cl_about.htm&type=5&language=en_US)

**•** [Data Table selections at runtime are subject to the client payload data limit described in Lightning Aura Components Developer](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_actions_call.htm)
[Guide. If you exceed this limit, the flow returns a generic error message. For example, if you include file data that exceeds the limit,](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_actions_call.htm)
the flow generates an error. We recommend avoiding fields like the VersionData field of ContentVersion records in your source
collection.

**•** If you rename a field in Object Manager that’s mapped to a column in a Data Table, Salesforce doesn’t update the column name. To
see the new name in the Data Table, remove the column and then add it again.

**•** If you have a flow open that has a Data Table component, and you update your user settings time zone on another page, refresh
the flow page to show the updated date and time fields in the Data Table component.

**•** When you set the row selection, be careful if you want to use the row selection of another Data Table component. Salesforce doesn’t
support the use of row selections that have duplicate record variables without record IDs.

**•** If you set the row-selection mode to single and make it required, or if you set the minimum and maximum row selection to 1,
Salesforce uses a radio button at run time. Otherwise, we use checkboxes at run time.

**•** If you package a flow that has a Data Table component, the fields used in the Data Table aren't automatically added to the package.
If you use a field in the Data Table component, you must manually add it to the package.

**•** If you delete a custom field that a Data Table component uses, you must also remove the field from the screen flow where the Data
Table component is used.

**•** If you use a Data Table component that uses a custom object or custom field in an org without a namespace, and then later add a
namespace to the org, you must also add that namespace to the associated column fields in the Data Table.

SEE ALSO:

Use Multilingual Labels in Data Table Column Headers

Data Safety When Running Screen and Autolaunched Flows in System Context

Flow Screen Input Component: Date

Let users enter date values from a flow screen.

Configure the Data Component

**Attribute** **Description**

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Default Value` Pre-populated value for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Date & Time

Let users enter date and time values from a flow screen, such as to request an appointment.

Configure the Date & Time Component

**Attribute** **Description**

```
API Name

Default Value

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Dependent Picklists

Display picklists in a flow screen in which the options for one picklist depend on the selected value
of another picklist. The Dependent Picklists screen component determines which options to display
in each picklist by using an existing field dependency in your org. A _field dependency_ connects two
picklist fields on the same object.

Note: This screen component requires Lightning runtime.

Configure the Dependent Picklists Component

Tip: Before you add a Dependent Picklists screen component to your flow, define field
dependencies for the appropriate picklist fields in your org.

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

**Attribute** **Description**

`API Name` The API name of the component.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Object API Name

Picklist 1 API Name

Picklist 1 Label

Picklist 1 Required

Picklist 1 Value

Picklist 2 API Name

Picklist 2 Label

Picklist 2 Required

Picklist 2 Value

Picklist 3 API Name

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The API name of the object. The picklist fields that you identify in Picklist 1 API Name, Picklist 2 API
Name, and Picklist 3 API Name must be associated with this object.

This attribute accepts single-value resources. The value is treated as text.

The API name of the first picklist field. For the specified object, this picklist field must be the controlling
field in a field dependency between Picklist 1 and Picklist 2.

This attribute accepts single-value resources. The value is treated as text.

The label for the first picklist field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the first picklist field. Configuring this attribute pre-selects an option for the
field.

This attribute accepts single-value resources. The value is treated as text.

The API name of the second picklist field. For the specified object, this picklist field must be the
dependent field in a field dependency between Picklist 1 and Picklist 2. If you display a third picklist
field, Picklist 2 must be the controlling field in a field dependency between Picklist 2 and Picklist 3.

This attribute accepts single-value resources. The value is treated as text.

The label for the second picklist field.

This attribute accepts single-value resources. That value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the second picklist field. Configuring this attribute pre-selects an option for
the field.

This attribute accepts single-value resources. The value is treated as text.

The API name of the third picklist field. For the specified object, this picklist field must be the dependent
field in a field dependency between Picklist 2 and Picklist 3.

This attribute accepts single-value resources. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Picklist 3 Label

Picklist 3 Required

Picklist 3 Value

```

The label for the third picklist field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the third picklist field. Configuring this attribute pre-selects an option for the
field.

This attribute accepts single-value resources. The value is treated as text.

Note: If your org has a namespace, add the namespace to the beginning of the object's API name, and each picklist API Name.
For example, if you have a custom object called Insurance_Agent__c, and your org's namespace is Acme,
enter _`Acme__Insurance_Agent__c`_ .

Store the Dependent Picklists Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
Picklist 1 Value

Picklist 2 Value

Picklist 3 Value

```

What the user selected for the first picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

What the user selected for the second picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

What the user selected for the third picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Example: For example, in a Dinner Order flow, users select a specific dessert. Each dessert comes in different flavors, and the
flavor options change based on the dessert that the user selects.

**•** On the Guest Order custom object, define two picklist fields: Dessert and Flavor.

**•** Define a field dependency between Dessert and Flavor, where Dessert is the controlling picklist. Identify which Flavor options
apply to each Dessert option.

**•** In your flow screen, add a Dependent Picklists screen component. Configure the component with these values.

**Attribute** **Value**

`Object API Name` Guest_Order__c

`Picklist 1 API` Dessert__c

```
  Name

```

`Picklist 1 Label` Dessert

`Picklist 2 Value` Flavor__c

`Picklist 2 Label` Flavor

When a user runs the flow, the options for Flavor change based on what’s selected for Dessert.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

Screen input component values are set to null when they’re hidden by conditional visibility. But hidden picklists in a Dependent Picklists
component aren’t set to null unless the entire Dependent Picklists component is hidden.

SEE ALSO:

Standard Flow Screen Components

[Define Dependent Picklists](https://help.salesforce.com/s/articleView?id=sf.fields_defining_field_dependencies.htm&language=en_US)

Flow Screen Input Component: Display Image

Easily insert images in flow screens. Upload images to Salesforce as static resources and then you
can reference them while configuring the component.

For information about adding screen components to your flow screen, see Flow Element: Screen.

Note: This screen component requires Lightning runtime.

Configure the Display Image Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Horizontal

Alignment

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

If you don't want the browser to determine the image's horizontal
alignment, enter a specific alignment value. Valid values are: left, center,
or right.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Image Alt Text

Image CSS

Image Height

Image Name

Image Width

```

Alternative text for screen readers and other assistive technology and for browsers that can’t load the
image. Provide a meaningful description unless the image is purely decorative or redundant.

To have assistive technology skip the image, set `Image Alt Text` to `{`
`!$GlobalConstant.EmptyString}` .

If you don't set this attribute, assistive technology reads the file path from the image source ( `img`
`src` ), which can confuse your users and potentially create an accessibility compliance issue.

This attribute accepts single-value resources. The value is treated as text.

Override the CSS for your image by providing your own CSS string. Example: `border-radius:`

```
8px; box-shadow: 10px 5px 5px blue; opacity: 0.75;

```

This attribute accepts single-value resources. The value is treated as text.

If you don't want the browser to determine the image height, enter a specific height value. Valid values
are a number and unit, or a percentage of the container. Examples: 200 px, 2 cm, 50%. If you enter a
number value and don’t enter a unit value, the unit value defaults to pixels.

This attribute accepts single-value resources. The value is treated as text.

Required. The name of a static resource that contains an image file. The image must be a `.png` or
`.jpg` file.

This attribute accepts single-value resources. The value is treated as text.

If you don't want the browser to determine the image width, enter a specific width value. Valid values
are a number and unit, or a percentage of the container. Examples: 200 px, 2 cm, 50%. If you enter a
number value and don’t enter a unit value, the unit value defaults to pixels.

This attribute accepts single-value resources. The value is treated as text.

Store the Display Image Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Email

Let users enter email address values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Email Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Label

Placeholder Text

Read Only

Required

Value

```

The label that appears above the email field.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the email field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Email Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the email address that the user entered, store the Value attribute in a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Enhanced Message

Let users send a messaging component in an enhanced Messaging session.

Configure the Enhanced Message Component

EDITIONS

Messaging is available in:
Lightning Experience with
the Digital Engagement
add-on SKU

Messaging is available in:
**Enterprise**, **Unlimited**, and
**Developer** Editions with
Service Cloud or Sales Cloud


Automate Your Business Processes with Salesforce Flow Flow Reference

SEE ALSO:

Standard Flow Screen Components

_Salesforce Help_ [: Send Structured Content with Messaging Components](https://help.salesforce.com/s/articleView?id=sf.messaging_components_parent.htm&language=en_US)

Flow Screen Input Component: File Upload

Let users upload files from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the File Upload Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

```
Accepted Formats

```

Using the format _`.ext`_, enter a comma-separated list of the file extensions that the user can upload.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Allow Multiple Files

```

If set to _`$GlobalConstant.True`_, the user can upload multiple files.

This attribute accepts single-value Boolean resources.

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

File Upload Label

Hover Text

Related Record ID

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Required. Label that appears above the upload button.

This attribute accepts single-value resources. The value is treated as text.

Tooltip that appears when the user hovers over the component.

This attribute accepts single-value resources. The value is treated as text.

Required. ID of the record to associate the files with. If no value is passed, the component is disabled.

This attribute accepts single-value resources. The value is treated as text.

Note: Custom fields added to the ContentVersion object page are rendered in Experience Cloud sites through the
contentVersionEditWizard. The contentVersionEditWizard is supported on desktop, but not mobile. Since there’s no screen in
mobile to edit or add details to custom fields, file uploads fail when custom fields are marked as required.

Store the File Upload Component’s Values in the Flow

All attributes are available to store in flow variables, but usually you must store one of these attributes. The values are assigned to the
flow variables when the user navigates to the next screen.

**Attribute** **Description**

```
Content Document IDs

Uploaded File Names

```

The IDs of the uploaded files.

You can store this value in a Text collection variable.

The names of the uploaded files.

You can store this value in a Text collection variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

File Upload Limits

By default, you can upload up to 10 files simultaneously, unless Salesforce changed that limit. The org limit for the number of files
simultaneously uploaded is 25 files with a minimum of one file. The maximum file size you can upload is 2 GB. In Experience Cloud sites,
the file size limits and types allowed follow the settings determined by site file moderation. By default, guest user files are blocked from
being uploaded. Admins can change the settings to let guest users upload files. From **Setup**    - **, select**    - **General Settings**, and then
select **Allow site guest users to upload files** . This setting is only valid if the Secure guest user record access setting is enabled in the
org.

Note: The file upload component isn’t supported on mobile app or browser when used with flows that are accessed through
URLs. This restriction doesn’t apply when the file upload component is used in Lightning App Builder or Experience Builder.

Lightning Out doesn’t support the File Upload component.

Considerations

If a user doesn’t upload any files, the value of the `Content Document IDs` and `Uploaded File Names` outputs is an empty
collection, represented as `“[]”` . If you check the ISBLANK or ISNULL operator, the value is always `false` .

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Long Text Area

Let users enter a paragraph or two of text from a flow screen.

Configure the Long Text Area Component

**Attribute** **Description**

```
API Name

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Lookup

Let users search for and select one or more records in a flow.

Configure the Lookup Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Field API Name

Label

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The API name of a lookup field on the source object referenced in Object
API Name.

The lookup field referenced in Field API Name must be a field on the object
referenced in Object API Name.

For example, if you want to add a lookup for an account, find an object
that has an account lookup field on it. In this case, let’s use the account
lookup field on the Contact object. The API name of the account lookup
field on the Contact object is AccountId, so enter _`AccountId`_ for Field
API Name, then enter _`Contact`_ for Object API Name.

The text that shows at the top of the component that tells the running
user how to use the screen component. For example, if you’re adding an
account lookup, the label could be Select Account.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Object API Name` The API name of the source object that has the lookup field referenced in Field API Name.

The source object can be any object that has the type of lookup field that you want to use.

The lookup field referenced in Field API Name must be a field on the object referenced in Object AI
Name.

To use the Lookup component, the running user of the flow must have the Create permission on the
source object.

For example, if you want to add a lookup for a contact, find an object that has a contact lookup field
on it. In this case, let’s use the contact lookup field on the Case object. The API name of the Case object
is Case, so enter _`Case`_ for Object API Name, then enter _`ContactId`_ for Field API Name.

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Maximum Selections` The maximum number of records that the user can select. The default value is 1.

```
Record Id

Record Id Collection

Required

```

Initially, if Maximum Selections is _`1`_ or Maximum Selections is greater than 1 and the Record ID
Collection field is _`null`_, the record ID selected by default for the lookup.

When a user runs the flow, the value changes to the flow user’s selection.

Initially, if Maximum Selections is greater than 1, the default record IDs for the lookup.

If Maximum Selections is greater than 1 and the Record ID field is _`null`_, the first value is the record
IDs selected by default for the lookup.

You can specify any number of record IDs up to the Maximum Selections value.

When a user runs the flow, the value changes to the flow user’s selections.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

Note: If your org has a namespace, add the namespace to the beginning of the object's API name, and field's API Name. For
example, if you have a custom object called Insurance_Agent__c, and your org's namespace is Acme,
enter _`Acme__Insurance_Agent__c`_ .

Store the Lookup Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but most likely you must store these attributes.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Record ID

Record ID Collection

Record Name

```

If the Maximum Selections value is 1, the ID of the record that the user selects.

You can store this value in a Text variable.

If the Maximum Selections value is greater than 1, the list of IDs of the records that the user selects.

If the Maximum Selections value is 1 and Record ID is null, the first value in the collection is the ID of
the record that the user selects.

You can store this value in a Text collection variable.

If the Maximum Selections value is 1, the value of the Name field of the record that the user selects.

If the Maximum Selections value is greater than 1, the value of the Name field of the first record that
the user selects.

You can store this value in a Text variable.

This value isn’t populated when the Name field of the record is an external object.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Lookup flow screen component isn’t compatible with mobile devices or standalone Aura apps.

**•** Dependent lookup filters aren’t enforced for the Lookup component in a flow. Other lookup filters are enforced the same as they
are in Lightning Experience record pages. When the flow accesses the Salesforce database, lookup filters are enforced. For example,
when the flow executes the Create Records element, the flow fails if the value of the lookup field doesn’t meet the lookup filter
requirements.

**•** To filter records based on resources and information from the flow, consider using a Choice Lookup component.

**•** A custom lookup field to a user record isn’t supported.

Tip: To let a flow user choose from a list of user records, employ a standard User lookup field like `CreatedById` or
`LastModifiedById` . `OwnerId` isn’t supported.

**•** At run time, when the flow user types two characters in the field, it shows up to five recent records whose `Name` field matches the
query.

**•** Dependent lookup filters aren’t supported.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** During run time, if the lookup field defined in `Field API Name` isn’t on an assigned page layout, the lookup component displays
`Search undefined...` . To display the correct text, add the defined lookup field to all of the source object’s page layouts that
are assigned to running users.

**•** Invalid Record IDs are ignored. A Record ID is invalid if it isn’t a valid Salesforce Record ID or its key prefix doesn’t match with the field
API name object.

**•** If the Maximum Selections value is 1 and the Record ID Collection and Record ID are both changed, the Record ID takes precedence.
The Record ID Collection is ignored.

**•** If the Maximum Selections value is greater than 1, the Record ID Collection takes precedence when Record ID is populated. But, if
Record ID Collection isn’t populated, the Record ID is used to populate Record ID Collection as a single it

**•** Relationship fields that are related to more than one object, also known as polymorphic fields, aren’t supported. For example, because
a task record’s WhoId field can be related to a contact or a lead, it isn’t supported for this component.

**•** `Field API Name` and `Object API Name` are case-sensitive.

**•** The Lookup flow screen component doesn’t support filtering by the source object record type.

SEE ALSO:

Standard Flow Screen Components

[Considerations for Lookup Filters](https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters_notes.htm&language=en_US)

[The Enhanced Page Layout Editor](https://help.salesforce.com/s/articleView?id=sf.customize_layoutcustomize_pd.htm&language=en_US)

Flow Screen Input Component: Multi-Select Picklist

Let users choose multiple options in a picklist format.

Configure the Multi-Select Picklist Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become
available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become
available:

**•** Checkbox Group


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**•** Multi-select Picklist

`Data Type` Only Text choices are supported for this component.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** Rich text isn’t supported in the Multi-Select Picklist component.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Name

Let users enter multiple name values with one screen component. Instead of the Name screen
component, you can use Text input fields to capture name information, but it takes a lot more
configuration.

Note: This screen component requires Lightning runtime.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Name Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Fields to Display

First Name

Informal Name

Label

Last Name

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

By default, the component displays only the First Name and Last Name fields, but other fields are
available. To customize which fields to display at run time, set this attribute to a comma-separated
list of the field names.

**•** For First Name, use firstName

**•** For Last Name, use lastName

**•** For Middle Name, use middleName

**•** For Informal Name, use informalName

**•** For Salutation, use salutation

**•** For Suffix, use suffix

This attribute doesn’t control the order that the fields display in.

For example, to display all the fields, set this attribute to _`firstName, lastName,`_
_`middleName, informalName, salutation, suffix`_ .

This attribute accepts single-value resources. The value is treated as text.

The value of the First Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

The value of the Informal Name field. Setting this attribute prepopulates the field. To use the value
that the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

The label that appears above the name fields.

This attribute accepts single-value resources. The value is treated as text.

The value of the Last Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Middle Name

Read Only

Salutation

Salutation Options

Suffix

```

The value of the Middle Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The value of the Salutation field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

By default, the options for Salutation are Mr., Mrs., and Ms. To override these options, set this attribute
to a comma-separated list of values.

This attribute accepts single-value resources. The value is treated as text.

The value of the Suffix field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Name Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
First Name

Informal Name

Last Name

Middle Name

Salutation

```

What the user entered in the First Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Informal Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Last Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Middle Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Salutation field.

This value can be stored in a single-value Text variable or a Text field on a record variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Suffix

```

What the user entered in the Suffix field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Number

Let users enter number values from a flow screen.

Configure the Number Component

**Attribute** **Description**

```
API Name

Decimal Places

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Controls the number of digits to the right of the decimal point up to 17
places. If you leave this field blank or set it to zero, only whole numbers
appear when your flow runs.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Order Management Product Selector

Let users select which fields show in columns during product selector for various transaction types,
such as returns or exchanges.

Configure the Order Management Product Selector Component

[Note: This screen component requires Lightning runtime.](https://help.salesforce.com/s/articleView?id=sf.flow_distribute_runtime.htm&language=en_US)

Set the product fields by using data in the flow.

**Attribute** **Description**

Configure Columns Required. Select up to ten columns to display.

Order Product Required. A collection of product summaries.
Summaries

Selected Order Required. The subset collection of product summaries being changed.
Product Summaries

Selected Order Required. The order summary that the product summaries belong to.
Summary


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

Transaction Type Optional. The type of transaction. Valid values are Cancel, RMS, Return, Reship, Discount, and Exchange.

Attributes to Output

**Attribute** **Description**

Order Product Summaries A collection of product summaries.

Selected Order Summary The selected order summary.

Selected Order Product The subset collection of product summaries being changed.
Summaries

Transaction Type The type of transaction.

Flow Screen Input Component: Password

Let users enter sensitive information in a flow screen, such as a social security number. Text entered
by the user is masked.

Note: This screen component doesn’t encrypt the value entered by the user. When the flow
references a Password screen component, such as in an Assignment element or a Display
Text screen component, the value isn’t masked.

Configure the Password Component

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Default Value

Disabled

```

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Phone

Let users enter phone values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Phone Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Label

Disabled

Pattern

Placeholder Text

Read Only

Required

Value

```

The label that appears above the phone field.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Determines whether the value is valid. By default, there’s no pattern.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the phone field. Setting this attribute prepopulates the field. To use the value that the
user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Phone Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the phone number that the user entered, map the Value attribute to a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Picklist

Let users choose from a list of options in a picklist format.

Starting with Flow Run-time API version 52, the first option listed for all picklists is --None--. If you
don’t set a default value for a picklist in Flow Builder, the --None-- option is automatically selected
at run time. --None-- is treated as a null value. If you set the picklist as required and the user selects
--None--, then the flow run time prevents the user from proceeding to the next screen.

Configure the Picklist Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become
available:

##### • Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become
available:

**•** Checkbox Group

**•** Multi-select Picklist


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Data Type` Controls which choices are available for this component. For example, if you choose Number, you
can’t select a Text choice.

```
Decimal Places

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your flow runs.

Available only when the data type is Number or Currency.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** Rich text isn’t supported in the Picklist component.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Radio Buttons

Let users choose from a list of options in a radio button format.

Configure the Radio Buttons Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.

All multi-select choice components use a text data type, but radio buttons
and picklists can also use numbers or Boolean choices.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Component Type` Modify a choice component type.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

If the user can select only one option, these component types become available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become available:

**•** Checkbox Group

**•** Multi-select Picklist

`Data Type` Controls which choices are available for this component. For example, if you choose Number, you
can’t select a Text choice.

```
Decimal Places

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your flow runs.

Available only when the data type is Number or Currency.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Slack Channel Selector

Let users select a Slack channel to send a Slack message from a flow screen.

Configure the Slack Channel Selector Component

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

Note: This screen component requires Lightning runtime.

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Slack app id` The ID of the Slack app connected to Salesforce. This attribute accepts Text variables.

[Only the Slack app owner can get the app ID. From https://api.slack.com, go to your apps, then Basic](https://api.slack.com)
Information, and find the app’s ID.

`Slack workspace id` The ID of the Slack workspace where the Slack app is installed. This attribute accepts Text variables.

To get the ID, open the web version of Slack and copy the alphanumeric section of the Slack URL
starting with T.

`Use Bot Token` Fetches a list of Slack channels based on the Slack app’s bot token.

This attribute accepts Boolean resources. If set to `$GlobalConstant.False`, the Slack app uses
the user token instead of the bot token.

`Use Channel Search` Indicates whether to use type-ahead Slack channel search to fetch a list of Slack channels.
```
   API
```

This attribute accepts Boolean resources. Requires that the Slack app be registered with Slack to use
the private API.

```
Label for dropdown

Placeholder for

dropdown

Required

```

Text that appears in the selector heading. Use text to give users a hint of what the Slack channel
selector is for.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

`Selected channel id` The ID of the selected Slack channel.

To get the channel ID, right-click the channel and select **View channel details** . The Channel ID is on
the About tab.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slack Workspace Selector

Let users select a Slack workspace to send a Slack message to from a flow screen.

Configure the Slack Workspace Selector Component

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

Note: This screen component requires Lightning runtime.

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Slack appID

Workspace ID

Select...

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The ID of the Slack app connected to Salesforce. This attribute accepts
Text variables.

[Only the Slack app owner can get the app ID. From https://api.slack.com,](https://api.slack.com)
go to your apps, then Basic Information, and find the app’s ID.

The ID of the Slack workspace where the Slack app is installed. This
attribute accepts Text variables.

To get the ID, open the web version of Slack and copy the alphanumeric
section of the Slack URL starting with T.

Text that appears in the field when it’s empty. Use placeholder text to
give users a hint about what to enter in the field.

This attribute accepts single-value resources. The value is treated as text.

`Workspace Name` The name of the Slack workspace where the Slack app is installed.

This attribute accepts single-value resources. The value is treated as text.

```
Required

```

If set to true, the running user must enter a value. The default value is
false.

This attribute accepts a resource with a Boolean value.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slider

Let users visually specify number values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Slider Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Label

Disabled

Range Maximum

Range Minimum

##### `Slider Size`

```

This label appears above the slider.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The maximum value of the slider range. The default is 100.

This parameter accepts single-value Number resources.

The minimum value of the slider range. The default is 0.

This parameter accepts Number resources.

Controls the size of the slider. The accepted values are x-small, small, medium, or large.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Step Size

Value

```

Divides the slider into a set of steps. The default is 1.

For example, for a range of 0–100, set the Step Size to 10 to let the user select every 10th value. Other
example step sizes are 0.1 and 5.

This parameter accepts single-value Number resources.

The default value represented by the slider position. Setting this attribute from the Inputs tab pre-sets
the value.

This parameter accepts single-value Number resources.

Store the Slider Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the value that the user selected, map the Value attribute to a Number flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Text

Let users enter text from a flow screen, such as the name of the user’s company.

Configure the Text Component

**Attribute** **Description**

```
API Name

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The
default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Toggle

Let users flip a toggle in a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Toggle Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

```
Active Label

```

When the toggle is active, this label appears underneath the toggle. Use it to clarify what active means.
The default label is “Active.”

This attribute accepts single-value resources. The value is treated as text.

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Inactive Label

Label

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

When the toggle is inactive, this label appears underneath the toggle. Use it to clarify what inactive
means. The default label is “Inactive.”

This attribute accepts single-value resources. The value is treated as text.

This label appears next to the toggle and describes what the user is enabling.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Value

```

Whether the toggle is active ( _`$GlobalConstant.True`_ ) or inactive
( _`$GlobalConstant.False`_ ). Setting this attribute from the Inputs tab controls the default state
of the toggle. To store the user’s selection in a flow variable, set this attribute from the Outputs tab.

This parameter accepts single-value Boolean resources.

Store the Toggle Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the user’s selection, map the Value attribute to a Boolean flow variable or a checkbox field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: URL

Let users enter URL values in a flow screen.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Flow Reference

Note: This screen component requires Lightning runtime.

Configure the URL Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Label

Pattern

Read Only

Required

Value

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The label that appears above the URL field.

This attribute accepts single-value resources. The value is treated as text.

Determines whether the value is valid. The default pattern verifies that the first character is a letter
and that the value includes a colon (:).

To force the user to enter a value in a specific format, use a regular expression. Make sure that your
regular expression checks for a valid protocol in the URL, such as https:// or file:///.

This example expression checks for a secure HTTP protocol (https://) and a specific domain
(acmewireless.com).

```
^https?://(?:www\.)?acmewireless\.com/?.*

```

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the URL field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store the URL Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the URL that the user entered, map the Value attribute to a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

_StackOverflow_ [: Sample Regular Expressions for Valid URLs](https://stackoverflow.com/questions/161738/what-is-the-best-regular-expression-to-check-if-a-string-is-a-valid-url)

_MDN_ [: What is a URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

Flow Screen Output Component: Display Text

Display information in a flow screen.

Configure the Display Text Component

**Attribute** **Description**

```
API Name

```

Text box

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The text to display to the flow user.

If you include a uniform resource identifier (URI), use one of these
supported URI prefixes:

**•** `http:`


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**•** `https:`

**•** `//`

**•** `/`

**•** `file:`

**•** `ftp:`

**•** `mailto:`

**•** `sfdc:`

**•** `data:`

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Example: Display a confirmation message that summarizes what the flow did on the user’s behalf.

SEE ALSO:

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Display Component: Repeater

Collect information about multiple items of the same type on a screen with the Repeater component.
To use the output of the component elsewhere in the flow, loop over the output and save the
relevant data in a variable. Use the variable to build a list of records.

For the best performance, we recommend setting the flow and runtime to API version 58.0 and
later.

Configure the Repeater Component

**Attribute** **Description**

`API Name` The API name of the component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

Screen readers use the API name to announce the Repeater component and its child components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Configure Data Source

Select the collection of items that prepopulates the Repeater component at run time. The Repeater’s child components can reference
values from this collection.

**Attribute** **Description**

`Collection for` Fields from the selected collection become available to child components in the Repeater.
```
   Prepopulated Items

```

`Unique Identifier` The unique identifier for items is the API name of the field that contains a unique identifier for each
`for Items` item in the collection. This field is set automatically to the object’s ID field.

Configure Display Options

**Attribute** **Description**

```
Let Users Add or

Remove Items

```

Choose whether screen flow end users can add new items or remove prepopulated items in your
Repeater instance. End users can remove items that they added manually.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Usage

After you configure the Repeater component, add and configure one or more child components inside the Repeater. The flow stores
user input for the Repeater component in the `AllItems` attribute of the component. You can loop over the items in this collection
to create a collection variable that you can use later in the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

**•** You can’t include the Action Button (Beta) component or record fields in a Repeater.

**•** The output of Repeater components isn’t supported in Transform, Collection Filter, or Collection Sort elements.

**•** You can’t reference the output of a different Repeater component in a Repeater child component.

**•** Choice components that reference a collection choice set resource in the Choice field aren’t reactive inside Repeater components.

**•** When you create or update a screen, you can move a component on the same screen into the Repeater component. You can also
move a component from inside a Repeater component to a different place on the screen. However, any references to the moved
component are broken.

**•** If you move a component with the Manually Assign Variables checkbox selected into a Repeater component, any manual assignments
are removed and the checkbox is deselected. However, the variables still exist in the flow. We recommend reviewing the component
after a move to ensure that it doesn’t include broken references.

**•** Users can add up to 30 instances of the Repeater component to the screen at runtime.

**•** The format for a reference to a Repeater component within the component itself is `{!` _**`repeaterAPIName`**_ `.` _**`fieldName`**_ `}` . In
validation messages and the flow metadata package, the format for the same reference is
`{!` _**`repeaterAPIName`**_ `.AllItems[$` _**`Items`**_ `].` _**`fieldName`**_ `}` .

**•** The `AllItems` attribute is empty when:

**–** The Repeater component contains only child components that don’t accept user input such as the Display Text component.

**–** A user doesn’t add Repeater instances to the screen.

**•** The `AllItems` attribute is null when all the child components are hidden by conditional field visibility.

Example: This example shows a screen that includes a Repeater component with Text, Date, Toggle, and Checkbox Group child
components to collect information about subscribers.

SEE ALSO:

Modify Records from User Input in Screens

Flow Example: Create a Contact for Each Beneficiary on a Policy


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Output Component: Section

Organize screen components and record fields to give your users a better experience.

Note: This screen component requires Lightning runtime.

Usage

Use sections to organize screen components and fields to give users context and easier navigation.
The Section component contains an optional header and up to four side-by-side columns. Each
column can contain multiple components and fields. You can place multiple sections on a screen,
each with its own header and number of columns.

Tip: Apply conditional visibility rules to a section to affect all components and fields in that
section. Use this method to set visibility rules one time for a large number of components,
even if you want only one column.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
