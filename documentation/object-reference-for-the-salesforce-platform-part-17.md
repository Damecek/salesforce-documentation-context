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

```
RecurrenceStartDateOnly

RecurrenceTimeZoneSidKey

RecurrenceType

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


Standard Objects Task

**Field** **Field Type**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the task repeats. For example, daily, weekly, or every nth month (where
“nth” is defined in `RecurrenceInstance` ).

```
ReminderDateTime

Status

Subject

TaskSubtype

```

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

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

This field can’t be updated for recurring tasks ( `IsRecurrence` is `true` ).

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the task, such as “Call” or “Send Quote.” Limit: 255 characters.

**Type**
picklist


Standard Objects Task

**Field** **Field Type**

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

```
TaskWhoIds

Type

WhatCount

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs related to this task. This `JunctionIdList` field is
linked to the `TaskWhoRelations` child relationship. `TaskWhoIds` is only available
when the shared activities setting is enabled. The first contact or lead ID in the list becomes
the primary `WhoId` if you don’t specify a primary `WhoId` . If you set the `EventWhoIds`
field to null, all entries in the list are deleted and the value of `WhoId` is added as the first
entry.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

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


Standard Objects Task

**Field** **Field Type**

**Description**
Available to organizations that have Shared Activities enabled. Count of related TaskRelations
pertaining to `WhatId` . Count of the `WhatId` must be _`1`_ or less.

```
WhatId

```

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


Standard Objects Task

**Field** **Field Type**

```
WhoCount

WhoId

```

Usage

**Recurring Tasks**

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

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

**•** Recurring tasks are available in API version 16.0 and later.

**•** After a task is created, it can’t be changed from recurring to nonrecurring or vice versa.

**•** When a user creates a series of recurring tasks, Salesforce creates a main record and subsequent occurrences. For the main record,
`IsRecurrence` is set to `true` and other fields that define the recurrence pattern are populated. The ID of the main record of
the recurring task is saved in the subsequent occurrences, in the `RecurrenceActivityId` field.


Standard Objects Task

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

```


Standard Objects Task

```
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


### Standard Objects TaskPriority

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

Fields

**Field** **Details**

```
ApiName

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


Standard Objects TaskPriority

**Field** **Details**

**Description**
Indicates whether the status is the default task priority value ( `true` ) or not ( `false` ) in the
picklist. Only one value in the picklist can be the default value.

```
 IsHighPriority

 MasterLabel

 SortOrder

```

Usage

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

This object represents a value in the task priority picklist. The task priority picklist provides additional information about the importance
of a task, such as whether a given priority value represents a high priority. Your client application can query on this object to retrieve
the set of values in the task priority picklist, and then use that information while processing task objects to determine more information
about a given task. For example, the application could test whether a given task is high priority based on its `Priority` value and the
value of the `IsHighPriority` field in the associated TaskPriority object.

SEE ALSO:

Overview of Salesforce Objects and Fields


### Standard Objects TaskRelation TaskRelation

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

RelationId

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

**Description**
Indicates whether the relation is an Account, Opportunity, Campaign, Case, other
standard object, or a custom object. Value is `false` if `RelationId` is a
contact or lead and `true` otherwise.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Indicates the `WhatId` or `WhoId` in the relationship. For more information, see
### Task .

For information on IDs, see ID Field Type.


### Standard Objects TaskStatus

**Field Name** **Details**

```
TaskId

```

Usage

**See contacts associated with a task**

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

**TaskRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

### Task

TaskWhoRelation

### TaskStatus

Represents the status of a task, such as Not Started, Completed, or Closed.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Standard Objects TaskStatus

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

MasterLabel

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

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task status value ( `true` ) or not ( `false` ) in the
picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task status value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.


### Standard Objects TaskTag

**Field** **Details**

```
 SortOrder

```

Usage

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

Fields

**Field Name** **Details**

```
ItemId

Name

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string


### Standard Objects TaskWhoRelation

**Field Name** **Details**

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

```
TagDefinitionId

Type

```

Usage

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

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### TaskWhoRelation

Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.

### TaskWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared

Activities for your organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects TaskWhoRelation

Fields

**Field Name** **Details**

```
AccountId

RelationId

TaskId

Type

```

Usage

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

**Description**
Indicates whether the person related to the task is a lead or contact.

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

```


### Standard Objects TaxEngine

```
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

Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. If your org has Subscription Management
and Commerce Subscriptions enabled, then Subscription Management takes precedence.

Special Access Rules

This object is available with Subscription Management, Commerce Subscriptions, and Billing (Revenue Cloud). If your org has Subscription
Management and Commerce Subscriptions enabled, then Subscription Management takes precedence.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects TaxEngine

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider and merchant credential.

```
ExternalReference

LastReferencedDate

LastViewedDate

MerchantCredentialId

```

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

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

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


Standard Objects TaxEngine

**Field** **Details**

**Refers To**
NamedCredential

```
SellerCode

Status

TaxEngineAddress

TaxEngineCity

TaxEngineCountry

```

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

**Description**
[The compound form of the tax engine address. Read-only. See Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/compound_fields_address.htm)
for details on compound address fields.

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


Standard Objects TaxEngine

**Field** **Details**

```
TaxEngineGeocodeAccuracy

TaxEngineLatitude

TaxEngineLongitude

TaxEngineName

TaxEnginePostalCode

TaxEngineProviderId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
[Accuracy level of the geocode for the tax engine address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLongitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLatitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

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


Standard Objects TaxEngine

**Field** **Details**

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

```
TaxEngineState

TaxEngineStreet

TaxPrvdAccountIdentifier

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. State maximum size is 80 characters.

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


### Standard Objects TaxEngineInteractionLog

**Field** **Details**

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

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)

Fields

**Field** **Details**

```
Description

DocumentCode

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


Standard Objects TaxEngineInteractionLog

**Field** **Details**

```
EffectiveDate

InteractionHttpStatusCode

InteractionType

LastReferencedDate

LastViewedDate

```

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

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of request made to the tax engine. In Subscription Management Summer
‘22, only `CalculateTax` is supported.

Possible values are:

**•** `CalculateTax`

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


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
ReferenceEntity

RequestBody

RequestContentType

RequestLength

RequestName

ResponseBody

```

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

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of data passed in the request. For example, `application/html` or
`text/csv` .

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


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API response.

```
ResponseContentType

ResponseLength

ResponseName

ResultCode

```

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


### Standard Objects TaxEngineProvider

**Field** **Details**

```
TaxEngineId

TaxEngineInteractionLogNumber

### TaxEngineProvider

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax engine used in the tax calculation process.

This field is a relationship field.

**Relationship Name**
### TaxEngine

**Relationship Type**
Lookup

**Refers To**
### TaxEngine

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A system-generated number for a log entry.

Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce,
and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine record
represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API version
55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)


Standard Objects TaxEngineProvider

Fields

**Field** **Details**

```
ApexAdapterId

Description

DeveloperName

Language

MasterLabel

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

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider.

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


### Standard Objects TaxGeoConfig

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label used for the tax engine’s API in Salesforce.

```
NamespacePrefix

### TaxGeoConfig

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Apex namespace prefix of the API used for the tax engine. In a packaging context, a
namespace prefix is a one to 15-character alphanumeric identifier that distinguishes your
package and its contents from packages of other developers on AppExchange.

Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxGeoConfig object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
GeoCountryId

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


Standard Objects TaxGeoConfig

**Field** **Details**

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


### Standard Objects TaxPolicy

**Field** **Details**

**Refers To**
Group, User

```
RoundingStrategyType

```

Associated Objects

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


Standard Objects TaxPolicy

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)

Fields

**Field** **Details**

```
DefaultTaxTreatmentId

Description

LastReferencedDate

LastViewedDate

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

**Refers To**
TaxTreatment

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


Standard Objects TaxPolicy

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

```
Name

Status

TreatmentSelection

```

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

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

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


### Standard Objects TaxRate TaxRate

Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxRate object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
ApplicationBasis

City

Country

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the tax rate is applied on the net or gross amount.

Possible values are:

**•** `Gross`

**•** `Net`

The default value is `Gross` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city to which the tax rate applies.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country name that’s derived from the GeoCountry field value.

This field is a calculated field.


Standard Objects TaxRate

**Field** **Details**

```
CurrencyIsoCode

EndDate

FlatTaxAmount

GeoCountryId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code that’s applicable to the tax rate.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date until when the tax rate is valid.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The flat tax amount that’s applied to the transaction.

**Type**
reference

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


Standard Objects TaxRate

**Field** **Details**

**Refers To**
GeoCountry

```
GeoStateId

LastReferencedDate

LastViewedDate

LegalEntityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the GeoState for which the tax rate applies.

This field is a relationship field.

**Relationship Name**
GeoState

**Refers To**
GeoState

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The legal entity to which the tax rate applies.

This field is a relationship field.

**Relationship Name**
LegalEntity


Standard Objects TaxRate

**Field** **Details**

**Refers To**
LegalEntity

```
Name

OwnerId

Priority

ProductCode

Rate

```

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

**Description**
The TaxRate record owner. By default, the record owner is the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The code of the product for which the tax rate applies.

**Type**
double


Standard Objects TaxRate

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The tax percentage rate that will be applied to orders.

```
RateUsageType

StartDate

State

TaxCode

ZipCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies whether the tax rate is created for Commerce or Revenue Cloud.

Possible values are:

**•** `Commerce`

**•** `RevCloud` —Revenue Cloud

The default value is `Commerce` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date from when the tax rate is valid.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state name that’s derived from the GeoState field value.

This field is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The code used to calculate the tax rate for the invoice line.

**Type**
string


### Standard Objects TaxTreatment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal or ZIP code to which the tax rate applies.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaxRateChangeEvent on page 68**
Change events are available for the object.

**TaxRateFeed on page 55**
Feed tracking is available for the object.

**TaxRateHistory on page 63**
History is available for tracked fields of the object.

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


Standard Objects TaxTreatment

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)

Fields

**Field** **Details**

```
Description

IsTaxable

LastReferencedDate

LastViewedDate

Name

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

**Description**
Determines whether Subscription Management calculates tax for order items covered by
the tax treatment. When this value is True, Subscription Management calls the CalculateTax
API for the order item during order item creation.

The default value is 'False'.

This field is available when Subscription Management is enabled.

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


Standard Objects TaxTreatment

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the tax treatment.

```
ProductCode

Status

TaxCode

TaxEngineId

```

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

**Description**
Status of the tax treatment.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

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


### Standard Objects TenantConsumptionAlert

**Field** **Details**

This field is available when Subscription Management is enabled.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

```
TaxPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax treatment’s parent tax policy. A tax policy is a group of tax treatments, where each
treatment represents a rule for how to invoice a customer for an order item. Tax policies are
related to products, which pass the policy on to the resulting order items. When you activate
an order, Subscription Management assigns a tax treatment to each order item based on
the tax policy's DefaultTaxTreatmentId, then uses the tax treatment to calculate tax.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

### TenantConsumptionAlert

Stores a record each time a utilization signal is reached for your org's consumption-based products. Each record captures the signal type,
the resource that triggered it, and the condition that was met. This object is available in API version 67.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`


Standard Objects TenantConsumptionAlert

Fields

**Field** **Details**

```
AlertScope

AlertStatus

AlertSubScope1

AlertSubScope2

AlertTimestamp

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. Identifies the top-level resource or component that the alert applies to.
`AlertScope`, `AlertSubScope1`, and `AlertSubScope2` together identify the
exact target of the alert, from broadest to most specific.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Required. Indicates whether the alert condition is still active or has resolved (Active or Cleared).
`Active` suppresses duplicate alerts while the condition persists. `Cleared` resets the
alert so it can fire again.

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
Identifies a sub-resource or sub-component beneath the alert scope. Can be empty if no
further refinement is required.

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
Identifies a sub-resource or sub-component that further refines AlertSubScope1. Can be
empty if no further refinement is required. However, if you set AlertSubScope2, we
recommend that you also set AlertSubScope1.

**Type**
dateTime

**Properties**
Filter, Group, Sort


Standard Objects TenantConsumptionAlert

**Field** **Details**

**Description**
Required. The date and time the alert was triggered.

```
AlertType

IsNotificationSent

TriggerType

TriggerValue

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. Identifies the type of signal that triggered the alert. Salesforce-managed alert types
are prefixed with `sf__` .

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Required. Indicates whether a platform notification has been sent for this alert record (true)
or not (false).

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unit or measurement type of the value that triggered the alert, such as a
percentage or unit count. Use this field to interpret the numeric value in `TriggerValue` .
Values are: `ThresholdPercent` or `ThresholdUnits` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. The numeric value that triggered the alert, which is interpreted in the context of
`TriggerType` .

TenantConsumptionAlert stores a record each time a utilization signal is reached for your org's consumption-based products or license
utilization. Each record represents a single triggered signal and is structured hierarchically:

AlertType identifies the high-level signal category.


Standard Objects TenantConsumptionAlert

**•** AlertScope (and its sub-scopes) identifies the specific resource that triggered the signal.

**•** TriggerType and TriggerValue define the condition that was met.

There are two types of alerts: Salesforce-managed and user-defined.

**•** Salesforce-managed alerts are created by Salesforce processes via invocable actions. Alert types for these alerts are prefixed with
`sf__` . Salesforce validates that the triggering condition is correct on creation and provides out-of-the-box features, including flow
templates and invocable actions, to manage the alert lifecycle. Lifecycle fields such as AlertStatus and IsNotificationSent are updated
automatically.

**•** User-defined alerts offer the flexibility to define any signal that meets your use case. However, all fields must be set manually. Lifecycle
fields like AlertStatus and IsNotificationSent aren’t updated automatically.

About Salesforce-Managed Alert Types

Consumption Threshold alerts are triggered when consumption of a Digital Wallet consumption card reaches a specified threshold. For
[setup information, see Salesforce Help: Get Digital Wallet Notifications about Your Usage.](https://help.salesforce.com/s/articleView?id=xcloud.wallet_get_notified.htm&language=en_US&type=5)

This table illustrates an alert for when the Data Services Credits consumption card exceeds 70% of its credits consumption based on its
entitlements.

Note: For this object, consumption cards are identified by their card definition developer name, which often differs from their
display name in Digital Wallet. To determine the developer name for a consumption card, see “Find the Card Definition Developer
[Name” in Salesforce Help: Change a Consumption Threshold for a Specific Card.](https://help.salesforce.com/s/articleView?id=xcloud.wallet_change_threshold_specific_card.htm&language=en_US)

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.

**[TenantConsumptionAlertOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.


### Standard Objects TenantScrAIPrmptInjection

**[TenantConsumptionAlertShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Get Digital Wallet Notifications about Your Usage](https://help.salesforce.com/s/articleView?id=xcloud.wallet_get_notified.htm&language=en_US)

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

Language

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Language of the prompt.


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

```
MaskedPrompt

MaskedResponse

MetricIdentifier

MetricsType

Name

PlannerLlm

```

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

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

**Description**
The LLM being used by the Planner.

```
Prompt

PromptTimestamp

PromptTokens

Response

Tenant

TenantName

```

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

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this triggered Transaction Security Policy event.

**Type**
string


### Standard Objects TenantSecret

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

### TenantSecret

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

**Description**

The key derivation mode applied to customer-supplied key material. Modes are:

**PBKDF2**
The customer-supplied key material is used by the Shield KMS to create a
derived data encryption key.


Standard Objects TenantSecret

**Field Name** **Details**

**NONE**
The customer-supplied key material is used by the Shield KMS as the final
data encryption key to directly encrypt and decrypt data.

Available in API version 43.0 and later.

```
RemoteKeyCertificate

RemoteKeyIdentifier

RemoteKeyServiceID

SecretValue

SecretValueCertificate

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

**Description**

The encrypted 256-bit secret value encoded in base64.

**Type**
string


Standard Objects TenantSecret

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The certificate needed to upload a customer-supplied tenant secret. Each
certificate has a unique name.

```
SecretValueHash

Source

Status

```

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

**Description**

The status of the tenant secret. Values are:

**Active**
Can be used to encrypt and decrypt new or existing data.


Standard Objects TenantSecret

**Field Name** **Details**

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

**Description**

The version number of this secret. The version number is unique within your org.


Standard Objects TenantSecret

Usage

Use this object to create or update an org-specific tenant secret or customer-supplied key material.

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_rest.htm)
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

**2.** Then upload your matching key material and key material hash. Include the unique name of the compatible certificate. The key
material is uploaded in encrypted form.

```
         TenantSecret secret = new TenantSecret ();

         secret.description = 'New uploaded secret';

         secret.type= 'Data';

         secret.SecretValue = ...

         EncodingUtil.base64Decode('...');;

         secret.SecretValueCertificate = ...;

```


Standard Objects TenantSecret

```
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


### Standard Objects TenantSecurityAIGtwyUsage

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
[or directly with Apex. Specify a BYOK-compatible certificate and an HTTPS endpoint.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Cloud

```

**Type**
string


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Cost cloud ID.

```
DetailIdentifier

Feature

MaskedPrompt

MaskedResponse

MetricIdentifier

```

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

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

```
MetricsType

Model

Name

ObjectName

Prompt

PromptTemplateDevName

```

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

**Description**
The hydrated version of prompt text before data masking is applied. The actual prompt sent
to the LLM will mask sensitive data if data masking is enabled.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

**Description**
The ID of the prompt template.

```
PromptTemplateVersionNo

PromptTokens

Response

Tenant

TenantName

```

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

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant of this AI gateway usage event.


### Standard Objects TenantSecurityAlertRuleSelectedTenant TenantSecurityAlertRuleSelectedTenant

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

Associated Objects

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

**Description**
The ID of the tenant (org) that this record is for.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects TenantSecurityApiAnomaly

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

EventDate

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


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

```
EventIdentifier

EventName

MetricIdentifier

MetricsType

Name

Operation

```

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

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API call that generated the event. For example, Query.

```
QueriedEntities

RequestIdentifier

RowsProcessed

Score

SecurityEventData

```

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

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the API activity that triggered this anomaly event.


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

For example, a user typically downloads 10 accounts at a time but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows how much as a percentage that the feature contributed to triggering this anomaly
event. The data is in JSON format.

```
Summary

Tenant

TenantName

Uri

UserAgent

```

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

**Type**
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.


### Standard Objects TenantSecurityCertificate

**Field** **Details**

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

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityCertificate

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

CertCreatedDate

DetailIdentifier

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

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects TenantSecurityCertificate

**Field** **Details**

**Description**
The ID of the individual detail record. This field is unique within your organization.

```
ExpirationDate

IsActive

IsCaSigned

IsPlatformEncrypted

IsPrivateKeyExportable

KeySize

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityCertificate

**Field** **Details**

**Description**
The length of the public key.

```
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
[field of LoginHistory in the Object Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)


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
the accounts. Available if Sales Territories has been enabled. This object is available in API versions 7.0 to 52.0. Use Territory2 instead of
### Territory in API version 52.0 and later.

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
on package installations. With this field, a developer can change the object's name
in a managed package and the changes are reflected in a subscriber's organization.
Corresponds to **Territory Name** in the user interface.


Standard Objects Territory

**Field** **Details**

This field is available in API version 24.0 and later.

When creating large sets of data, always specify a unique `DeveloperName` for
each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

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

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

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

LastRunRulesEndDate

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

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. The date when the opportunity territory assignment filter was last
run. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15
/ API version 33).

**Type**
dateTime


### Standard Objects Territory2ModelHistory

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the last rules run was completed.

```
Name

State

```

Associated Objects

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

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects Territory2ModelHistory

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

Territory2ModelId

```

Usage

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

This object is automatically generated whenever any field value changes on a territory model record. Use this object it to identify those
changes.


### Standard Objects Territory2ObjectExclusion Territory2ObjectExclusion

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

Territory2Id

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

**Refers To**
Account

**Type**
reference


### Standard Objects Territory2ObjSharingConfig

**Field** **Details**

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
### Territory2 Territory2ObjSharingConfig

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

Territory2Id

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The access level of the object for the particular territory.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects Territory2Type

**Field** **Details**

**Description**
The territory on which the access level is defined.

This field is a relationship field.

**Relationship Name**
### Territory2

**Relationship Type**
Lookup

**Refers To**
### Territory2

```
TerritoryMgmtObjectConfigId

### Territory2Type

```

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

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

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

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
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
The foreign key to the AuthProvider on page 885 of the third-party system.

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

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

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

**•** [ApiAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_apianomalyeventstore.htm)

**•** [CredentialStuffingEventStore](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_credentialstuffingeventstore.htm)

**•** [ReportAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_reportanomalyeventstore.htm)

**•** [SessionHijackingEventStore](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_sessionhijackingeventstore.htm)

For example, `0fjRM000000005p` .

This is a polymorphic relationship field.

**Relationship Name**
ThreatDetectionEvent

**Refers To**
ApiAnomalyEventStore, CredentialStuffingEventStore, GuestUserAnomalyEventStore,
LoginAnomalyEventStore, ReportAnomalyEventStore, SessionHijackingEventStore,
UniversalAnomalyEventStore

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the time sheet.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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
indirectly.

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
value is null, it's possible that the user only accessed this record or list view
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

**[TimeSlotChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
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

You can change only the spacing and capitalization of a topic name with the
update property.

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

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

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
Create, Filter, Nillable, Sort, Update

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

**•** `AdminSetupEvent` —Tracks metadata and configuration changes made by
administrators within the Setup area of your org.

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


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**•** `LoginAnomalyEventStore` —Stores the records of data access anomalies that
are caused by potentially malicious login actions.This object is available in API version
64.0 and later.

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

**•** `UniversalAnomalyEventStore` —Stores data for a broad range of system and
user activity anomalies that do not map to standard event stores.

```
EventType

ExecutionUserId

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


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**Description**
Used in Legacy Transaction Security only. The ID of an active user who is assigned the Modify
All Data and View Setup user permissions. As of Summer '20, Legacy Transaction Security is
a retired feature in all Salesforce orgs.

```
Language

MasterLabel

NamespacePrefix

ResourceName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The policy’s name.

Important: Where possible, we changed noninclusive terms to align with our
company value of Equality. We maintained certain terms to avoid any effect on
customer implementations.

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


### Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. A resource used to narrow down the conditions
under which the policy triggers. For example, with a `DataExport` event, you can select
a resource Lead to specifically monitor export activity occurring on your Lead entities. The
resources available depend on the `EventType` field.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

```
State

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the policy is active. Valid values are:

**•** `Disabled`

**•** `Enabled`

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

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects TransactionSecurityEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApexIdentifier

BotIdentifier

BotSessionIdentifier

ClientIp

CpuTime

EvaluationTime

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.

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


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds used to evaluate the policy.

```
EventName

FlowIdentifier

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
The name of the event, which is `Transaction Security Event` .

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


Standard Objects TransactionSecurityEventLog

**Field** **Details**

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

**•** `Notified` —A notification was sent to the recipient.

```
PolicyType

RequestIdentifier

Result

RunTime

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


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Description**
The amount of time that the request took in milliseconds.

```
SendEmailNotification

SendInAppNotification

SessionKey

Timestamp

TriggeredTimestamp

```

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

**Description**
Indicates whether to send an in-app notification. The default value is `false` .

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


### Standard Objects Translation

**Field** **Details**

```
Uri

UserIdentifier

### Translation

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

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects TravelMode

**Field** **Details**

**Description**
Indicates whether the language is available for translation ( `true` ) or not ( `false` ).

Specify translators for each language through the Translation Language Setup page.

```
IsActive

Language

### TravelMode

```

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

Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such as
Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is available
in API version 54.0 and later.

Fields

**Field** **Details**

```
CanUseTollRoads

IsLocked

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


Standard Objects TravelMode

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record is locked or not.

The default value is `false` .

```
IsTransportingHazmat

LastReferencedDate

LastViewedDate

MayEdit

Name

```

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


Standard Objects TravelMode

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the travel mode.

```
OwnerId

TransportType

```

Associated Objects

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

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TravelModeFeed**

Feed tracking is available for the object.

**TravelModeOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects TwoFactorInfo

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

Fields

**Field Name** **Details**

```
SharedKey

Type

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


### Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

```
UserId

### TwoFactorMethodsInfo

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the user who’s associated with the authentication secret.

Stores information about which identity verification methods a user has registered. This object is available in API version 37.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

You need the Manage MFA in API user permission to access this object. Note that multi-factor authentication (MFA) was formerly called
two-factor authentication.

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
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

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique system-generated numerical identifier for the user.

**Type**
boolean


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a built-in authenticator on their device, such as
Touch ID or Windows Hello. The user can verify their identity by using the built-in
authenticator.

This field is available in API version 53.0 and later.

```
HasSalesforceAuthenticator

HasSecurityKey

HasTempCode

HasTotp

```

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

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a WebAuthn-compatible security key. This field
includes all security keys registered or used after Summer ’22. The user can verify
their identity by inserting the security key into a USB port to generate credentials.

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


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

**Description**
If `true`, the user has connected an authenticator app that generates verification
codes, also known as time-based one-time passwords (TOTP). The user can verify
identity by entering a code generated by the app.

```
HasU2F

HasUserVerifiedEmailAddress

HasUserVerifiedMobileNumber

HasVerifiedMobileNumber

```

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


### Standard Objects TwoFactorTempCode

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who’s associated with the identity verification methods.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `[query()](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_query.htm)` call returns up to 500 rows.
A `[queryMore()](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_querymore.htm)` call returns 500 more, up to 2,500 total. No more records are returned after 2,500.

To make sure that you don’t miss any records, issue a `COUNT()` query in a SELECT clause for TwoFactorMethodInfo. This query gives
you the total number of records. If there are more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
  SELECT <desired fields> FROM TwoFactorMethodsInfo LIMIT 2000 OFFSET 0

```

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


### Standard Objects UiAgentInteractionEventLog

Fields

**Field Name** **Details**

```
Expiration

Identifier

TempCode

UserId

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

**Description**
A request for this value always returns `null` .

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


Standard Objects UiAgentInteractionEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AgentType

AppName

BotIdentifier

BotSessionIdentifier

BrowserName

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


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Description**
The name of the browser.

```
BrowserVersion

ButtonLabel

Channel

ClientGeolocation

ClientIdentifier

ClientIp

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the channel. For example, mobile, LEX, or Playground.

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


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Client IP address.

```
Components

ConnectionType

DeviceModel

DevicePlatform

DeviceSessionIdentifier

```

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


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
FeedbackIdentifier

HasToxicityWarning

IsAgentPanelExited

LightningType

LightningTypeMessage

LoginKey

```

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

**Description**
A boolean field that is true if the user clicks on a button to navigate away from an agent
panel.

The default value is `false` .

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


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the login id to allow tracking of all events from user login to logout.

```
MessageIdentifier

MobileSdkAppType

MobileSdkVersion

ObjectType

OperatingSystemName

OperatingSystemVersion

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK version.

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


Standard Objects UiAgentInteractionEventLog

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

RequestIdentifier

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object type of the page being displayed.

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


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
SdkAppVersion

SessionKey

TaskName

Timestamp

UiEventElapsedTime

UiEventTimestamp

```

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


### Standard Objects UiFormulaCriterion

**Field** **Details**

```
UiRootActivityIdentifier

UserIdentifier

UserType

VoiceOrText

### UiFormulaCriterion

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Whether the input by the user was “voice” or “text”.

Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects UiFormulaCriterion

Fields

**Field** **Details**

```
LeftHandSide

OperatorId

ParentKeyPrefix

RightHandSide

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

This is a relationship field.

**Relationship Name**
Operator

**Relationship Type**
Lookup

**Refers To**
null

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix of the parent ID.

**Type**
string


### Standard Objects UiFormulaRule

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the value used to evaluate the component’s visibility. For example, 1000000.

```
RuleId

### UiFormulaRule

```

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

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AssociatedElementId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a parent component that UiFormulaRule is associated with, such as PromptVersion.

This is a relationship field.


Standard Objects UiFormulaRule

**Field** **Details**

**Relationship Name**
AssociatedElement

**Relationship Type**
Lookup

**Refers To**
PromptVersion

```
BooleanFilter

DeveloperName

Formula

Language

MasterLabel

```

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

**Description**
Represents the formula source string of UiFormulaRule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the language of the UiFormulaRule.

**Type**
string


### Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Required. Represents the label of the UiFormulaRule.

```
ParentKeyPrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix for AssociatedElementId.

### UiTelemetryNavTmEventLog

UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from the
[UI Telemetry Resource Timing Event on page 2414 and includes requests initiated with either the Fetch API or the XMLHttpRequest API.](https://fetch.spec.whatwg.org/)
This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AppName

BrowserName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

```
BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

ConnectEnd

```

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

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as `Salesforce.com IP` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

```
ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

DevicePlatform

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
DeviceSessionIdentifier

DomComplete

DomContentLoadedEventEnd

DomContentLoadedEventStart

DomInteractive

```

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

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler starts.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The time in milliseconds when the page’s `readyState` is set to `interactive` . Indicates
that the page has finished loading, but subresources, such as images and scripts, are still
loading.

```
DomainLookupEnd

DomainLookupStart

Duration

EncodedBodySize

FetchStart

```

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

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`LOAD_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
double


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

```
FirstInterimResponseStart

InitiatorType

LoadEventEnd

LoadEventStart

```

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


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**

The time in milliseconds when the page’s `load` event handler begins.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

```
LoginKey

MobileSdkAppType

MobileSdkVersion

NavigationType

NextHopProtocol

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
The type of navigation timing data.

**Possible Values**

**•** `navigate` : a user interaction or a script initiated navigation.

**•** `reload` : a reload initiated navigation.

**•** back_forward: navigation traverses the browser’s history.

**•** `prerender` : a prerender hint initiated navigation.

**Type**
string


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Application-Layer Protocol Negotiation (ALPN) Protocol ID that fetches the resource.

**Possible Values**
`http/0.9`, `http/1.0`, `h2`, `h2c`, `h3`

```
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


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
PageUrl

RedirectCount

RedirectEnd

RedirectStart

RenderBlockingStatus

```

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


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

```
RequestIdentifier

RequestStart

ResponseEnd

ResponseStart

```

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


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
ResponseStatus

SdkAppVersion

SecureConnectionStart

ServerRequestIdentifier

SessionKey

StartTime

```

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


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

```
Timestamp

TransferSize

UiEventElapsedTime

UiEventTimestamp

UiRootActivityIdentifier

UiThreadResponseDelay

```

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

**Description**
The time at which this event occurs, measured in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the root activity when the event occurs.

**Type**
double


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

```
UnloadEventEnd

UnloadEventStart

Url

UserIdentifier

UserType

```

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

**Description**
The URL of the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Type**
string


### Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

```
WorkerStart

```

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

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

ConnectEnd

```

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

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP.”

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

```
ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

DevicePlatform

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

```
DeviceSessionIdentifier

DomainLookupEnd

DomainLookupStart

Duration

EncodedBodySize

```

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

**Properties**
Filter, Nillable, Sort

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`RESPONSE_END` time.

**Type**
double


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

```
FetchStart

FirstInterimResponseStart

InitiatorType

LoginKey

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

```
MobileSdkAppType

MobileSdkVersion

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version number.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page.

```
PageObjectIdentifier

PageObjectType

PageUrl

RedirectEnd

RedirectStart

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
Relative URL of the top-level Lightning Experience page that the user opened. The page can
contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
double


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

```
RenderBlockingStatus

RequestIdentifier

RequestStart

ResponseEnd

```

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

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

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
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The requestId for the server request that’s used to find associated server logs.

```
SessionKey

StartTime

Timestamp

TransferSize

UiEventElapsedTime

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
The difference in milliseconds between when the message was logged and when the browser
tab started meaning


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
UiEventTimestamp

UiRootActivityIdentifier

UiThreadResponseDelay

Url

UserIdentifier

UserType

```

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


### Standard Objects UndecidedEventRelation

**Field** **Details**

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

```
WorkerStart

```

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


Standard Objects UndecidedEventRelation

**Field Name** **Details**

```
RelationId

RespondedDate

Response

Type

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.


### Standard Objects UnifiedActivity

Usage

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

ActivitySubType

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


Standard Objects UnifiedActivity

**Field** **Details**

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

```
ActivityType

DetailId

InternalEventKey

```

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

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage, Event, Task, VideoCall, VoiceCall

**Type**
string


### Standard Objects UnifiedActivityInsight

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

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

Supported Calls

`describeSObjects()`, `query()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.


Standard Objects UnifiedActivityInsight

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

OwnerId

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

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UnifiedActivityParticipant

**Field** **Details**

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

```
Scope

```

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

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)


Standard Objects UnifiedActivityParticipant

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

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`


### Standard Objects UnifiedActivityRelation

**Field** **Details**

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

Fields

**Field** **Details**

```
ActivityId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UnifiedActvtyInsightKeyword

**Field** **Details**

**Description**
ID of the activity. This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedVideoCall, UnifiedVoiceCall

```
RelatedId

```

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

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)


### Standard Objects UnifiedEmail

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

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)


Standard Objects UnifiedEmail

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

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for


Standard Objects UnifiedEmail

**Field** **Details**

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

**Properties**
Defaulted on create Filter


### Standard Objects UnifiedEmailParticipant

**Field** **Details**

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UriEventLog

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


### Standard Objects UsageImpactFactor

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

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Factor is active.

The default value is `false` .


Standard Objects UsageImpactFactor

**Field** **Details**

```
Name

ShortForm

Type

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Factor.

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


### Standard Objects UsageImpactGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactFactorShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

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


Standard Objects UsageImpactGroup

**Field** **Details**

**Description**
Indicates whether the Usage Impact Group is active.

The default value is `false` .

```
Name

ShortForm

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group.

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

**[UsageImpactGroupChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.


### Standard Objects UsageImpactGroupFactor

**[UsageImpactGroupOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupFactor

Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0 and
later.

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


Standard Objects UsageImpactGroupFactor

**Field** **Details**

**Description**
The name of the Usage Impact Group Factor.

```
UnitOfMeasureId

UsageImpactFactorId

UsageImpactGroupVersionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The UnitOfMeasure object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

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


### Standard Objects UsageImpactGroupPgmMeasure

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroupVersion

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupFactorShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

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

```

**Type**
string


Standard Objects UsageImpactGroupPgmMeasure

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Program Measure.

```
Name

Product2Id

ProgramId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Program Measure.

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


### Standard Objects UsageImpactGroupVersion

**Field** **Details**

### `UsageImpactGroupVersionId`

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version associated with the Energy Saving Group Association.

This field is a relationship field.

**Relationship Name**
### UsageImpactGroupVersion

**Relationship Type**
Lookup

**Refers To**
### UsageImpactGroupVersion

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupPgmMeasureChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupPgmMeasureFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupPgmMeasureHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupPgmMeasureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupPgmMeasureShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupVersion

Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects UsageImpactGroupVersion

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
ApprovedMeasureExtlid

Description

EndDate

IsActive

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The approved Measure Category ID assigned by a regulator.

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


Standard Objects UsageImpactGroupVersion

**Field** **Details**

```
StartDate

TechResourceManualCode

UsageImpactGroupId

Version

```

Associated Objects

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

**Description**
The code and version of the Technical Reference Manual which is the source for the values
associated with this Usage Impact Group Version. This is necessary for regulatory reporting.

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


### Standard Objects User

**[UsageImpactGroupVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupVersionShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### User

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


Standard Objects User

Fields

**Field** **Details**

```
AboutMe

AccountId

```

`Address` (beta)

```
Alias

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Information about the user, such as areas of interest or skills. This field is available even if
Chatter is disabled.

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


Standard Objects User

**Field** **Details**

```
BadgeText

BannerPhotoUrl

CallCenterId

City

CommunityNickname

CompanyName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Experience Cloud site role, displayed on the user profile page just below the user name.

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


Standard Objects User

**Field** **Details**

**Description**
The name of the user’s company.

```
ContactId

Country

CountryCode

CurrentStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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


Standard Objects User

**Field** **Details**

Note: If you update this field, the API automatically adds a post of type
`UserStatus` on the user’s profile in Chatter.

This field is deprecated in API version 25.0. To achieve similar behavior, post to the
user directly by creating a FeedItem with the user’s ParentId.

```
DefaultCurrencyIsoCode

DefaultDivision

DefaultGroupNotificationFrequency

DelegatedApproverId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The user's default currency setting for new records. For example, if a user in France sets
`DefaultCurrencyIsoCode` to euros, then that’s their default currency.

Only applicable for organizations that use multiple currencies.

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


Standard Objects User

**Field** **Details**

**Description**
Id of the user who is a delegated approver for this user.

```
Department

DigestFrequency

Division

Email

EmailEncodingKey

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company department associated with the user.

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


Standard Objects User

**Field** **Details**

**Description**
Required. The email encoding for the user, such as `ISO-8859-1` or `UTF-8` .

```
EmailPreferencesAutoBcc

EmployeeNumber

EndDay

Extension

Fax

FederationIdentifier

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the user receives copies of sent emails. This option applies only if
compliance BCC emails aren’t enabled.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Indicates the value that must be listed in the `Subject` element of a Security Assertion
Markup Language (SAML) _IDP certificate_ to authenticate the user for a client application using
single sign-on. This value must be specified if the `SAML User ID Type` is Assertion
contains Federation ID from the User record. Otherwise, this field can’t be edited.

```
FirstName

ForecastEnabled

FullPhotoUrl

GeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s first name.

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


Standard Objects User

**Field** **Details**

```
HasUserVerifiedEmail

HasUserVerifiedPhone

IndividualId

IsActive

IsPartner

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's email is verified ( `true` ) or not ( `false` ). The default value is
`false` . This field is available in API version 63.0 and later.

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


Standard Objects User

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is a partner who has access to the partner portal ( `true` ) or not
( `false` ). This field isn’t available for release 9.0 and later. Instead, use `UserType` with the
value `Partner` or `Power Partner` .

```
IsPortalEnabled

IsPortalSelfRegistered

IsPrmSuperUser

IsProfilePhotoActive

```

**Type**
boolean

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


Standard Objects User

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has a profile photo ( `true` ) or not ( `false` ). This field is available
in API version 36.0 and later.

```
JigsawImportLimitOverride

LanguageLocaleKey

LastLoginDate

LastName

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data.com user’s monthly addition limit. The value must be between zero and the
organization’s monthly addition limit. Label is **Data.com Monthly Addition Limit** . This
field is available in API version 27.0 and later.

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


Standard Objects User

**Field** **Details**

**Description**
Required. The user’s last name.

```
LastReferencedDate

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
The timestamp for when the current user last viewed a record related to this record.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the geolocation of an address. Acceptable values are
numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.

```
Manager

ManagerId

MediumBannerPhotoUrl

MiddleName

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


Standard Objects User

**Field** **Details**

**Description**
The user’s middle name. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

```
MobilePhone

Name

NumberOfFailedLogins

OfflineTrialExpirationDate

PasswordExpirationDate

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s mobile device number.

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


Standard Objects User

**Field** **Details**

**Description**
The date and time when the user’s password expires. This field is available in API version 63.0
and later.

```
Phone

PortalRole

PostalCode

ProfileId

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s phone number.

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


Standard Objects User

**Field** **Details**

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

```
ReceivesAdminInfoEmails

ReceivesInfoEmails

SenderEmail

SenderName

Signature

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The signature text added to emails. This text is the same value shown in Setup on the My
Email Settings page.

```
SmallBannerPhotoUrl

SmallPhotoUrl

StartDay

State

StateCode

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the small user profile banner photo.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code associated with the user.

```
Street

SuAccessExpirationDate

Suffix

TimeZoneSidKey

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address associated with the User.

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


Standard Objects User

**Field** **Details**

```
Title

Username

UserPermissionsCallCenterAutoLogin

UserPermissionsChatterAnswersUser

UserPermissionsInteractionUser

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s business title, such as Vice President.

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


Standard Objects User

**Field** **Details**

**Description**
Indicates whether the user can run flows or not. Label is **Flow User** .

```
UserPermissionsJigsawProspectingUser

UserPermissionsKnowledgeUser

UserPermissionsLiveAgentUser

UserPermissionsMarketingUser

UserPermissionsOfflineUser

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Data.com user license ( `true` ) or not ( `false` ).
The Data.com user lets the user add Data.com contact and lead records to Salesforce in
supported editions. Label is **Data.com User** .

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


Standard Objects User

**Field** **Details**

**Description**
Required. Indicates whether the user is enabled to use Offline Edition ( `true` ) or not ( `false` ).
Label is **Offline User** .

```
UserPermissionsSFContentUser

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
Indicates whether the user is allocated one Salesforce CRM Content User License ( `true` ) or
not ( `false` ). Label is **Salesforce CRM Content User** . The Salesforce CRM Content User
license grants the user access to the Salesforce CRM Content application.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Required if the Wireless permission is enabled. Indicates whether the user is enabled to use
Wireless Edition ( `true` ) or not ( `false` ). Label is **Wireless User** .

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

UserPreferencesAgentGdprConsent

UserPreferencesAllowConversationReminders

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
When `true`, indicates that the user has consented that calls may be recorded and
transcribed, and such calls, recordings and transcripts may be analyzed for quality or training
purposes. When `false`, the user has not given that consent.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `true`, voice and call reminders are displayed as notification cards in Lightning
Experience. Corresponds to the `Show conversation reminders in Lightning`
`Experience` checkbox in the Activity Reminders page in the personal settings in the user
interface.

This field is available in API version 55.0 and later.

```
UserPreferencesApexPagesDeveloperMode

UserPreferencesAutoForwardCall

UserPreferencesContentEmailAsAndWhen

UserPreferencesContentNoEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, indicates that the user has enabled developer mode for editing Visualforce
pages and controllers.

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


Standard Objects User

**Field** **Details**

email alerts, set this field to `false` and set the
`UserPreferencesContentEmailAsAndWhen` field to `true` .

The default value is `false` .

Note: This field is only visible when Salesforce CRM Content is enabled.

```
UserPreferencesEnableAutoSubForFeeds

UserPreferencesDisableAllFeedsEmail

UserPreferencesDisableAutoSubForFeeds

UserPreferencesDisableBookmarkEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user automatically subscribes to feeds for any objects that the user creates.
This field is available in API version 25.0 and later.

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


Standard Objects User

**Field** **Details**

```
UserPreferencesDisableChangeCommentEmail

UserPreferencesDisableEndorsementEmail

UserPreferencesDisableFileShareNotificationsForApi

UserPreferencesDisableFollowersEmail

UserPreferencesDisableLaterCommentEmail

```

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

**Description**
When `false`, the member automatically receives email every time someone endorses
them for a topic.

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


Standard Objects User

**Field** **Details**

```
UserPreferencesDisableLikeEmail

UserPreferencesDisableMentionsPostEmail

UserPreferencesDisableProfilePostEmail

UserPreferencesDisableSharePostEmail

UserPreferencesDisableFeedbackEmail

```

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

**Description**
When `false`, the user automatically receives email every time they’re mentioned in posts.
This field is available in API version 24.0 and later.

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


Standard Objects User

**Field** **Details**

```
UserPreferencesDisCommentAfterLikeEmail

UserPreferencesDisMentionsCommentEmail

UserPreferencesDisableMessageEmail

UserPreferencesDisableRewardEmail

UserPreferencesDisableWorkEmail

```

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

**Description**
When `false`, the user automatically receives email every time the user is mentioned in
comments. This field is available in API version 24.0 and later.

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


Standard Objects User

**Field** **Details**

```
UserPreferencesDisProfPostCommentEmail

UserPreferencesEnableVoiceCallRecording

UserPreferencesEnableVoiceLocalPresence

UserPreferencesEventRemindersCheckboxDefault

UserPreferencesHideBiggerPhotoCallout

UserPreferencesHideChatterOnboardingSplash

```

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

**Description**
When `true`, voice call recording is enabled for the user.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
When `true`, the initial Chatter onboarding prompts don’t appear.

```
UserPreferencesHideCSNDesktopTask

UserPreferencesHideCSNGetChatterMobileTask

UserPreferencesHideEndUserOnboardingAssistantModal

UserPreferencesHideLightningMigrationModal

UserPreferencesHideSecondChatterOnboardingSplash

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Chatter recommendations panel never displays the recommendation to
install Chatter Desktop. This field is available in API version 26.0 and later.

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


Standard Objects User

**Field** **Details**

```
UserPreferencesHideS1BrowserUI

UserPreferencesHideSfxWelcomeMat

UserPreferencesJigsawListUser

UserPreferencesLightningExperiencePreferred

UserPreferencesLiveAgentMiawSetupDeflection

```

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

**Properties**
Create, Filter, Update

**Description**
Controls whether a user sees the Lightning Experience new user message. That message
welcomes users to the new interface and provides step-by-step instructions that describe
how to return to Salesforce Classic.

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


Standard Objects User

**Field** **Details**

**Description**
When `true`, disables the pop-up to deflect users on Chat setup nodes to the Messaging
setup. The default value is `false` . This field is available in API version 59.0 and later.

```
UserPreferencesNativeEmailClient

UserPreferencesOptOutOfTouch

UserPreferencesOutboundBridge

UserPreferencesPathAssistantCollapsed

UserPreferencesProcessAssistantCollapsed

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Use this field to set a default email preference for the user’s native email client. This field is
available in API version 47.0 and later. The default value is `false`, corresponding to the
Salesforce docked email composer.

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


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
When `true`, Sales Path appears collapsed or hidden to the user. This field is available in API
versions 33.0 and 34.0 only. In API versions 35.0 and later, use
`UserPreferencesPathAssistantCollapsed` .

```
UserPreferencesReceiveNoNotificationsAsApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for _approvers_ .

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


Standard Objects User

**Field** **Details**

```
UserPreferencesReceiveNotificationsAsDelegatedApprover

UserPreferencesReminderSoundOff

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

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a sound automatically plays when an activity reminder is due. Corresponds to
the `Play a reminder sound` checkbox on the Reminders page in the user interface.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowCityToExternalUsers

UserPreferencesShowCityToGuestUsers

UserPreferencesShowCountryToExternalUsers

```

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

The default value is `false` . This field is available in API version 26.0 and later.

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


Standard Objects User

**Field** **Details**

**•** This field is `false` but `UserPreferencesShowCountryToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `false` . This field is available in API version 26.0 and later.

```
UserPreferencesShowCountryToGuestUsers

UserPreferencesShowEmailToExternalUsers

UserPreferencesShowEmailToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. When `true`,
country is visible to guest users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCountryToExternalUsers`, making the user’s country
visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

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


Standard Objects User

**Field** **Details**

When `true`, this field overrides the value `false` in
`UserPreferencesShowEmailToExternalUsers`, making the user’s email address
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

```
UserPreferencesShowFaxToExternalUsers

UserPreferencesShowFaxToGuestUsers

UserPreferencesShowManagerToExternalUsers

```

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
