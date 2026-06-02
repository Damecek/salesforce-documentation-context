there’s no need to add a Get Records element to obtain the record data. And, no flow variables have to be created to store the record
data.

If you have a workflow rule similar to this example, use the migration tool. The migration tool does a great job and even adds the workflow
rule name and description in the details of the new flow.


### Automate Your Business Processes with Salesforce Flow Process Builder Process Builder

Many of the tasks you assign, the emails you send, and other record updates are vital parts of your
standard processes. Instead of doing this repetitive work manually, you can configure flows or
processes to do it automatically. We strongly recommend using Flow Builder, but Process Builder
can also help you automate your business processes and give you a graphical representation as
you build it.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

### Process Builder supports three types of processes for your automation needs. The type determines

what triggers the process.

**•** A record change process starts when a record is created or updated.

**•** An event process starts when a platform event message is received.

**•** An invocable process starts when something else, like another process, invokes it.

Each process consists of:

**•** Criteria that determine when to execute an action group.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Action groups, which consist of immediate or scheduled actions. Only record change processes support scheduled actions.

If you need an existing process to do more than what process actions allow, don’t worry. You can also call a flow or Apex from a process.

Examples of Processes
See how Process Builder can make automating your business processes super easy.

Process Limits and Considerations
Before you start creating, managing, and activating processes, understand the limits and considerations.


Automate Your Business Processes with Salesforce Flow Process Builder

Setting Values in the Process Builder
Throughout the Process Builder, you must set values, for example, to set conditions in a criteria node, to set the fields on a new case
in a Create a Record action, or to specify an Apex method to reference.

Setting Advanced Options in the Process Builder
The Process Builder lets you choose some advanced options for executing actions in your processes.

Create a Process
To create a process, define its properties and which records it evaluates, and then add criteria nodes and actions.

Troubleshoot Processes
Use the error messages that appear in the Process Builder and the emails you receive when a process fails to help solve problems
that arise when you’re working with processes. When all else fails, look at the Apex debug logs for your processes.

SEE ALSO:

Choose Which Salesforce Flow Feature to Use

#### Examples of Processes

See how Process Builder can make automating your business processes super easy.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Sample Process: Opportunity Management
This example automates a single business process by using the Process Builder instead of
workflow rules.

Sample Process: Printer Management
The example demonstrates how you can use Process Builder to subscribe to and evaluate a
platform event.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Sample Process: Managing Documents
This example uses Process Builder to manage documents in Salesforce. The example moves a document to a shared folder in Quip
whenever the record that the document is associated with is created or updated. This process ensures that the documents associated
with a Salesforce record object are always available to users who have access to the shared folder.

Sample Process: Opportunity Management

This example automates a single business process by using the Process Builder instead of workflow
rules.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

The example demonstrates how you can use the Process Builder to automate a single process by
adding multiple groups of criteria and then associating individual actions with those criteria. In
addition, some actions are available with the Process Builder that you can’t perform with workflow
rules, such as creating records.

In this example, the process is defined to start when an opportunity record (1) is created or edited.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

Three criteria nodes are then set up to check whether a high-value deal was won (2), a high-value deal was lost (3), or a quote was given
(4). For the first criteria node that evaluates to true, the associated action group is executed.

The High Value Deal Won criteria checks whether the opportunity’s stage is closed and won and also whether the opportunity’s amount
is greater than $1,000,000.00. If both of these conditions are met, the associated action group is executed. For this criteria node, three
immediate actions (5) and one scheduled action (6) are defined.

These actions:

**•** Create a draft contract record that's associated with the opportunity’s account.

**•** Congratulate the opportunity owner for closing and winning the opportunity by posting to the Sales Chatter group.

**•** Notify the VP of sales via email that the opportunity was closed and won.

**•** Create a high priority follow-up task for the associated account’s owner, which is scheduled to execute six days after the opportunity’s
`Close Date` .

If the High Value Deal Won criteria conditions aren’t met, the associated group of actions doesn’t execute and the next criteria node
(High Value Deal Lost) is evaluated.

The High Value Deal Lost criteria node checks whether the opportunity stage is closed and lost and whether the opportunity amount
is greater than or equal to $1,000,000.00. If these conditions are true, we’ve set up an action (7) to notify the VP of sales by creating a
chatter post on the opportunity record. The post identifies the opportunity and the opportunity amount that was lost.

If neither of the previous criteria conditions are met, the next criteria node defined in this process checks whether the opportunity stage
is set to “Proposal/Quote Given.” If this condition is true, a scheduled action (8) is executed three days after the record is updated. The
scheduled action creates a follow-up task for the opportunity owner to call to inquire about the opportunity.

Using the Process Builder, we’ve combined three criteria nodes and associated actions into a single, automated process. To automate
the same business process with workflow, you would have to create three different workflow rules and use Apex triggers to create the
contract record and post to the Sales Chatter group.


Automate Your Business Processes with Salesforce Flow Process Builder

Sample Process: Printer Management

The example demonstrates how you can use Process Builder to subscribe to and evaluate a platform
event.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Using platform events and the Salesforce REST API, your printer publishes a Printer Status event at
the end of each work day. This event includes the printer’s serial number, how much ink and paper
it has, and how many pages it has printed in total.

When Salesforce receives the Printer Status event, your Printer Management process uses the serial
number to find a matching asset in your Salesforce org.

If the process finds a match, it evaluates the event’s data.

**•** The first criteria always update the asset’s print count.

EDITIONS

Available in both Salesforce
Classic and Lightning
Experience

Available in: **Performance**,
**Unlimited**, **Enterprise**, and
**Developer** Editions

**•** The second criteria checks if the ink is low. If so, it launches a flow that orders more ink and assigns a service technician to install the
ink cartridge.

**•** The third criteria checks if the paper is low. If so, it launches a flow that orders more paper and assigns a service technician to add
the paper.


Automate Your Business Processes with Salesforce Flow Process Builder

SEE ALSO:

_Platform Events Developer Guide_ [: Considerations for Defining and Publishing Platform Events](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_considerations.htm)

Sample Process: Managing Documents

This example uses Process Builder to manage documents in Salesforce. The example moves a
document to a shared folder in Quip whenever the record that the document is associated with is
created or updated. This process ensures that the documents associated with a Salesforce record
object are always available to users who have access to the shared folder.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

In the example, it’s assumed that:


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

**•** The Account object has a custom field labeled Quip Account Plan Doc (API name Quip_Account_Plan_Doc__c). For each account,
the custom field stores the URL of an associated document that contains a plan for the account.

**•** All the Account Plan documents are in a shared folder. The folder’s URL is `https://acme.quip.com/123FakeURL456` .

The process starts when an Account record (1) is created or updated.

The criteria (2) checks whether the value of the Quip Account Plan Doc custom field has changed and whether the field isn't null. If both
conditions are true, an immediate action (3) moves the Quip Account Plan doc to the specified shared folder. Let’s dig a little deeper
into the criteria and action in this sample process.

The criteria’s Set Conditions section defines which conditions must be met in the Quip Account Plan Doc field to move a document.
There are two conditions: the Quip Account Plan Doc field isn’t null and that it’s changed. The Field column requires the full API name
of the field, in this case, `[Account].Quip_Account_Plan_Doc__c` . The Conditions section specifies that all the conditions
must be met to execute the action.


Automate Your Business Processes with Salesforce Flow Process Builder

For the action definition, you select **Quip** for Action Type to view the Quip-related actions. Enter an Action Name ( _`Move Doc to`_
_`Folder`_ in our example) then select the action ( **Add Document to Folder** ). The Document URL is a field reference to the custom field
([Account].Quip_Account_Plan_Doc__c) that contains the URL of the document to move. The Folder URL is a String type that specifies
the URL of the shared folder.


Automate Your Business Processes with Salesforce Flow Process Builder

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

#### Process Limits and Considerations

Before you start creating, managing, and activating processes, understand the limits and considerations.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate, deactivate, and edit any existing
processes. To migrate existing processes, use the Migrate to Flow tool on page 894. For new automations, create flows in Flow
Builder on page 16.

#### Process Limits

When building processes, keep shared limits and Apex governor limits in mind. In addition, a process’s API name must be unique
across all processes and flows in your Salesforce org.

Process Usage-Based Entitlements
Like feature licenses, usage-based entitlements don’t limit what you can do in Salesforce; they add to your functionality. If your usage
exceeds the allowance, Salesforce contacts you to discuss additions to your contract. In the meantime, your processes continue to
run as usual.

When Do Processes Evaluate Record Changes?
Processes start automatically and are invisible to the user. Before you design or activate a process, understand which changes trigger
processes.

Considerations for Designing Processes
Before you design a process, understand the limitations and guidelines.

Considerations for Managing Processes
Understand what happens when you install, activate, or delete processes.

Considerations for Deploying Processes
Keep these considerations in mind when deploying processes, such as when using packages or change sets.

Considerations for Processes in Transactions
Each process runs in the context of a transaction. A transaction represents a set of operations that are executed as a single unit. When
a process is triggered more than one time in a single transaction, Salesforce executes similar actions in one batch.

#### Process Limits

When building processes, keep shared limits and Apex governor limits in mind. In addition, a
process’s API name must be unique across all processes and flows in your Salesforce org.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Limits Shared with Other Features

Processes share some limits with rules and flows.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

**Essentials or**
**Professional**
**Per-Org Limit**
**Edition**

**Enterprise,**
**Unlimited,**
**Performance, or**
**Developer Edition**

Active record change processes and rules per object 50 50

Rules include workflow rules, escalation rules, assignment rules, and auto-assignment
rules.

Total processes 5 per process type 4,000 per process
type

Active processes 5 per process type 2,000 per process
type

Criteria nodes that are evaluated and actions that are executed at runtime per process None [1] None [1]

Groups of scheduled actions that are executed or flow interviews that are resumed per 1,000 1,000
hour

Combined total of these automations that start or resume based on a record’s field value. 20,000 20,000

**•** Resume events that are defined in active flows

**•** Groups of scheduled actions that are defined in active processes

**•** Time triggers that are defined in active workflow rules

**•** Inactive flow interviews that are resumed

The daily limit for emails sent from email alerts is 1,000 per standard Salesforce license per org, except for Developer Edition orgs. For a
Developer Edition org, the daily workflow email limit is 15 per standard Salesforce license. The overall org limit is 2,000,000, which is
shared across all features that use workflow email alerts: workflow rules, approval processes, flows, and processes.

1In API version 57.0, the limit of 2000 flow elements was removed. In API version 56.0 and earlier, flows could have a maximum of 2000
flow elements.

Apex Governors and Limits for Processes

Salesforce strictly enforces limits to ensure that runaway processes don’t monopolize shared resources in the multitenant environment.
Processes are governed by the per-transaction limits that are enforced by Apex. If a process launches other automation in the same
transaction, that automation shares the process transaction’s limits. If the process or its launched automation causes the transaction to
exceed governor limits, the system rolls back the entire transaction. For details about the operations that are included in the transaction,
see Triggers and Order of Execution in the _Apex Developer Guide_ .

**Description** **Per-Transaction Limit**

Total number of SOQL queries issued 100

Total number of records retrieved by SOQL queries 50,000

Total number of DML statements issued 150

Total number of records processed as a result of DML statements 10,000

Maximum CPU time on the Salesforce servers 10,000 milliseconds


Automate Your Business Processes with Salesforce Flow Process Builder

Each Create a Record action uses one DML statement. Each Quick Action action uses one DML statement. Each Update Records action
uses one SOQL query and one DML statement. Each Flows action can use multiple SOQL queries and DML statements, depending on
the elements that the flow executes. For details, see Per-Transaction Flow Limits on page 246.

Limits for Creating and Managing Processes

Consider these limits when creating and managing processes.

**Per-Process Limit** **Value**

Total characters in a process name 255

Total characters in a process’s API name 79

Total versions of a process 50

Total criteria nodes in a process 200

##### Process Usage-Based Entitlements

Like feature licenses, usage-based entitlements don’t limit what you can do in Salesforce; they add
to your functionality. If your usage exceeds the allowance, Salesforce contacts you to discuss
additions to your contract. In the meantime, your processes continue to run as usual.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

For per-month entitlements, your contract determines the start and end of the month. You can
view the start and end dates for your org’s usage-based entitlements on the Company Information
page in Setup.

Note:

**•** When a process built in Process Builder launches a flow, both the process and the flow
count toward your allocation of flow interviews.

**•** If you enable recursion for a process built in Process Builder, a separate flow interview
starts each time the process evaluates a record. Each flow interview counts toward your
allocation of flow interviews.

This table describes the free allocations that are granted based on your org’s edition.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Process Builder

If you have questions about increasing your allocation, contact your Salesforce account executive.

SEE ALSO:

[Usage-Based Entitlements](https://help.salesforce.com/s/articleView?id=sf.users_understanding_tenant_usage_entitlements.htm&language=en_US)

[View Your Salesforce Org’s Usage-Based Entitlements](https://help.salesforce.com/s/articleView?id=sf.users_usagebased_entitlements_viewing.htm&language=en_US)

Reevaluate Records in the Process Builder

Flow Types

How Does Salesforce Process Scheduled Actions?

##### When Do Processes Evaluate Record Changes?

Processes start automatically and are invisible to the user. Before you design or activate a process,
understand which changes trigger processes.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

A record change can apply to more than just processes. When a record is created or edited, Salesforce
evaluates whether to run other setup items, such as validation rules on the record. Salesforce
evaluates the setup items in this order. For more information, see Triggers and Order of Execution
in the _Apex Developer Guide_ .

**•** Validation rules

**•** Assignment rules

**•** Auto-response rules

**•** Workflow rules and processes (and their immediate actions)

**•** Escalation rules

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When you create a process, you associate the process with exactly one object. You also specify whether to evaluate only created records
or both created and edited records. When you activate a process, it starts when a record change meets those settings.

Processes evaluate record changes when:

**•** A record is saved or created. Processes that are created after records are saved don’t evaluate those records retroactively.

**•** A standard object in a master-detail relationship is reparented.

**•** Users synchronize records that were changed while using Connect Offline.

**•** If the lead setting **Require Validation for Converted Leads** is enabled, leads are converted.

**•** Another process, workflow rule, or flow updates the record in the same save operation, if the process is configured to reevaluate
records.

Processes can reevaluate records up to five times in one save operation. In a batch update, processes reevaluate only changed
records.

Note: A record change can trigger more than one process. You can’t determine which process starts first.

Processes don’t evaluate record changes when:


Automate Your Business Processes with Salesforce Flow Process Builder

**•** Campaign statistic fields, such as individual campaign statistics or campaign hierarchy statistics, are updated.

**•** Picklist values are mass replaced.

**•** Address fields are mass updated.

**•** Divisions are mass updated.

**•** Territory assignments of accounts and opportunities are modified.

**•** Self-Service Portal, Customer Portal, or partner portal users are deactivated.

**•** State and country/territory data is converted with the Convert tool.

**•** Values for state and country/territory picklists are modified using `AddressSettings` in the Metadata API.

##### Considerations for Designing Processes

Before you design a process, understand the limitations and guidelines.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

We recommend that you use the most recent stable version of Google Chrome [™] .

Best Practices for Designing Processes
Before you design a process in Process Builder, understand the best practices.

Process Builder Accessibility Considerations
Process Builder is 508-compliant, with one exception. You can’t close window dialogs with your
keyboard.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Considerations for Event Processes
These considerations are specific to processes that start when a platform event message is received.

Compatibility Considerations for Processes
Before you design a process, understand how processes interact with other Salesforce features, like custom objects and fields.

Process Formula Limitations
Formulas that are used as conditions in a criteria node have some limitations. If a process contains an invalid formula, you can't save
or activate the process.

Considerations for Scheduling Process Actions
Scheduled actions are supported only in record-change processes and event processes. The scheduled time depends on the type
of schedule, whether the field changed, and whether the process was deactivated.

Considerations for Processes that Send Custom Notifications
Before you begin sending custom notifications, learn about important storage, recipient, and org limits.

Considerations for Processes That Post to Chatter
The Post to Chatter action doesn’t support Experience Cloud sites, and there are some limitations around what you put in the
message.


Automate Your Business Processes with Salesforce Flow Process Builder

Considerations for Processes That Update Records
Understand what happens when you change a record owner, update the same field multiple times, or update currency fields in a
multiple currency org.

SEE ALSO:

###### Best Practices for Designing Processes Best Practices for Designing Processes

Before you design a process in Process Builder, understand the best practices.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Build in a test environment.

To test whether a process is working properly, you must activate it. Build and test your processes
in a sandbox environment, so that you can identify any issues without affecting your production
data.

For each object, use one automation tool.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If an object has one process, one Apex trigger, and three workflow rules, you can’t reliably predict the results of a record change.

Tip: When you replace a workflow rule with a process, deactivate the workflow rule before you activate the process. Otherwise,
you can get unexpected results, such as overwritten records or redundant email messages. This best practice also applies when
you replace an Apex trigger with a process.

Have only one record-change process per object.

Each time a record is created or updated, all record-change processes for its object are evaluated. We recommend restricting your org
to one record-change process per object. Here’s why.

**•** Get a Consolidated View of Your Org’s Automation for an Object

With one consolidated record-change process for an object, you can see all the criteria that are evaluated each time that object’s
records are updated, as well as the actions that are performed when the criteria are met.

**•** Avoid Hitting Limits

When you consolidate your processes for one object into one main process, you also consolidate the actions in those processes.
With fewer actions, your org is less likely to hit limits, such as number of SOQL queries.

**•** Determine the Order of Operations

If you create multiple record-change processes for an object, Salesforce can’t guarantee the order in which those processes are
evaluated. When you automate everything in a single process, you explicitly set the order. The first criteria node is evaluated first,
the second criteria node is evaluated second, and so on.

Here are a couple features that can ease your path to one main process.


Automate Your Business Processes with Salesforce Flow Process Builder

**•** ISNEW()—Some automation applies only to created records. The rest applies to created and edited records. How could you possibly
combine all of them into one process? Meet the formula function that detects whether the record being evaluated was recently
created: `ISNEW()` .

To add a create-only automation to a process that starts when a record is created or edited, convert the associated criterion’s
conditions to a formula. Then add _`&&ISNEW()`_ to your formula.

**•** Invocable processes—Just like a process can call flows, a process can call other processes. Invocable processes are modular processes
that start only when another process tells them to.

For example, several criteria nodes in your “Account” process each evaluate some conditions, including whether the account is high
value. Move those criteria nodes, without the high-value conditions that they have in common, into a “Top Account” invocable
process. Then configure your “Account” process to invoke the “Top Account” process if the account is high value.

Combine actions when possible.

The more actions that a process executes, the more likely your org is to reach limits, such as the number of DML statements or total CPU
usage. Avoid creating multiple actions when a single action would do.

For example, a process updates an account’s address. Instead of creating a different action to update each individual field, create one
action to update all the address fields.

Build reusable actions.

Some process actions are always reusable: email alerts, quick actions, processes, flows, and Apex. But how do you reuse other types of
actions in multiple criteria groups or multiple processes?

**•** To reuse a Create a Record action or an Update Records action, build a quick action. Quick actions can be used in processes, flows,
and on record pages.

**•** To reuse other process actions, configure the actions in an invocable process. In the relevant criteria groups, add a Processes action
to call the invocable process. Invocable processes can be used only in processes.

Watch out for actions that overwrite previous changes.

Avoid having or be careful when multiple action groups update the same field.

Avoid generating infinite loops.

For example, an Update Records action in Process1 triggers Process2, and a Create a Record action in Process2 triggers Process1. The
looping causes your org to exceed its limits.

Make sure that immediate actions don’t cancel scheduled actions.

Pending scheduled actions are canceled when the associated criteria are no longer true. Make sure that the later immediate actions in
your process don’t unintentionally cancel pending scheduled actions.

Test as many permutations of your process as you possibly can.

As with all customizations in Salesforce, it’s important to test your work. Make sure that you test as many possibilities as you can think
of before you deploy the process to your production org.


###### Automate Your Business Processes with Salesforce Flow Process Builder

To access external data after changing Salesforce data, use scheduled actions.

If Salesforce creates, updates, or deletes data in your org and then accesses external data in the same transaction, an error occurs. In your
processes, we recommend using a separate transaction to access data in an external system. To do so, end the prior transaction by
adding a scheduled action. For a record-change process, don't use a field-based schedule.

For example, an event process starts when it receives a platform event message from the custom platform event, Order Status. If the
order status is new, the process creates a contact and schedules an action to update the order status in the external system. The event
process doesn’t fail because the scheduled action creates a separate transaction to access the external system.

SEE ALSO:

Considerations for Designing Processes

Considerations for the ISNEW Function

Transactions and Scheduled Actions

###### Process Builder Accessibility Considerations

Process Builder is 508-compliant, with one exception. You can’t close window dialogs with your
keyboard.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Close UI Elements with the Esc key:

You can close window dialogs using the Esc key on your keyboard, but you can’t close side panels.

Reorder Criteria Nodes:

Follow these steps to reorder criteria nodes with your keyboard.

**1.** Select a criteria node by pressing the Space key.

**2.** Change the order of a criteria node by using the Up and Down arrow keys.

**3.** Save your changes by pressing the Space key.

**4.** Cancel by pressing the Esc key.

###### Considerations for Event Processes

These considerations are specific to processes that start when a platform event message is received.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Supported Platform Events

Processes can subscribe to custom platform events and these standard platform events.

**•** AIPredictionEvent

**•** BatchApexErrorEvent

**•** FlowExecutionErrorEvent

**•** FOStatusChangedEvent


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

Available in both Salesforce
Classic and Lightning
Experience

Available in: **Performance**,
**Unlimited**, **Enterprise**, and
**Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

**•** OrderSummaryCreatedEvent

**•** OrderSumStatusChangedEvent

**•** PlatformStatusAlertEvent

Apex Actions

You can’t use an event reference to set an sObject variable in the Apex class.

Email Alerts Actions

Email alerts can’t use values from platform event messages. For the process to send an email that contains values from the platform
event message that starts the process, use this workaround.

Flows Actions

You can’t use an event reference to set a record variable in the flow, even when the platform event is specified as the record variable’s
object. To pass values into the flow from the platform event message that starts the process, use this workaround.

**•** In the flow, create a variable for each field in the platform event. Be sure to use compatible data types and make the variables available
for input.

**•** In the process, when you add the Flows action, use event references to assign each platform event field to its corresponding flow
variable.

Associating with a Record

Use the process’s matching conditions to find exactly one record. If the process can’t find one record based on your matching
conditions—because either it found multiple records or no records—the creator of the process receives an error email. If an error occurs,
adjust the conditions in the process’s trigger to be more specific.

Publishing Event Messages

With event processes, we don’t block you from publishing the same event message that starts the process. To avoid creating an endless
loop, make sure that the new event message’s field values don’t meet the filter criteria for the associated criteria node.

If a platform event is configured to publish immediately, the process publishes each event message outside of the database transaction.
If the transaction fails and is rolled back, the event message is still published and can’t be rolled back. So if you see an informational
message under the selected platform event, consider whether you want the process to publish an event message only after the transaction
commits successfully.

Subscriptions Related List

On the platform event’s detail page, the Subscriptions related list shows which entities are waiting to receive that platform event’s
messages. The related list includes a link to each subscribed process. If flow interviews are waiting for that platform event's messages,
one “Process” subscriber appears in the Subscriptions related list.

Packaging

When you package an event process, the associated object isn’t automatically included. Advise your subscribers to create the object or
manually add the object to your package. For example, when you package an event process that’s associated with the Participants
custom object, manually add the object to your package.


Automate Your Business Processes with Salesforce Flow Process Builder

Uninstalling Events

Before you uninstall a package that includes a platform event, deactivate all processes that reference the platform event.

Einstein Predictions

A prediction event is sent for each Einstein prediction result, so use process matching conditions if you want your process to be triggered
only by predictions on a specific object. For example, if your process acts only on predictions written to Lead records, add a matching
condition to check that the Lead ID field equals the AI Predicted Object ID event reference.

If your process updates a field that is used by an Einstein prediction, Einstein runs the prediction again and writes back the new results.
The new results generate a new prediction event that could trigger your process again, resulting in a loop. To avoid creating a process
loop, only update fields that aren’t used in Einstein predictions.

SEE ALSO:

_Platform Events Developer Guide_ [: Decoupled Publishing and Subscription](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_considerations_decoupled_processes.htm)

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_define_ui.htm)_ : Platform Event Fields

_Platform Events Developer Guide_ [: Subscribe to Platform Event Messages with Processes](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_process.htm)

###### Compatibility Considerations for Processes

Before you design a process, understand how processes interact with other Salesforce features, like
custom objects and fields.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Objects

Process Builder doesn’t support:

**•** Deprecated custom objects

**•** Signup Request—unsupported in schedules only

**•** Social Post

**•** Social Persona

External Objects

**•** External objects aren’t supported in record-change processes.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** When you create or update external object records, don’t set values for indirect lookup relationships that map to a different data
type on the external system. For example, don’t set a value for a Text indirect lookup relationship that maps to a Date value on the
external system.

Custom Fields

**•** Process Builder doesn’t support custom fields of type File.

**•** If a process references a custom field:

**–** You can’t delete the field.

**–** If you change the field type or name, the process breaks.


Automate Your Business Processes with Salesforce Flow Process Builder

**–** If you change the field label, the process doesn’t break. But it still uses the original label.

Derived Fields

Process Builder doesn’t support fields whose values are derived from other fields. Examples of derived fields include `Contact.Name`,
`User.MediumPhotoUrl`, and `EmailMessage.Name` .

Polymorphic Fields

Queue labels aren't supported in process criteria. For example, you can't use `[Lead].Owner:Queue.Name` in process criteria.
Instead, use `[Lead].Owner:Queue.DeveloperName` to reference the queue's API name.

Validation Rules

**•** Scheduled Update Records actions skip validation rules.

**•** Immediate Update Records actions obey validation rules.

Shield Platform Encryption

You can’t use an encrypted field as a filter in an Update Records action.

Duplicate Rules

If a duplicate is found when a process tries to create or update a record, the process fails.

Converted Leads

To evaluate records that result from converted leads, enable the lead setting **Require Validation for Converted Leads** .

Formula Field Values

If a standard formula field references a field on a related object, that field's value is always null when a process starts. This limitation
doesn’t apply to custom formula fields that reference a field on a related object. For a custom formula field that uses the same formula,
the field’s value is derived when a process starts.

For example, the RevenueShare field on Campaign Influence calculates `CampaignInfluence.Opportunity.Amount *`
`CampaignInfluence.Influence` . Because the formula references a field on Opportunity (a related object), the field’s value is
null.

Platform Cache

When a process contains a scheduled action, make sure that later actions in the process don't invoke Apex code that stores or retrieves
values from the session cache. The session-cache restriction applies to Apex actions and to changes that the process makes to the
database that cause Apex triggers to fire.


Automate Your Business Processes with Salesforce Flow Process Builder

###### Process Formula Limitations

Formulas that are used as conditions in a criteria node have some limitations. If a process contains
an invalid formula, you can't save or activate the process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

All formulas that are used in a criteria node must:

**•** Return `true` or `false` . If the formula returns `true`, the associated actions are executed.

**•** Not contain more than 3,000 characters.

**•** Not contain an unsupported function.

**•** Reference the process trigger object for that process.

**•** Use the correct capitalization when referring to the process trigger object.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Tip: Parentheses aren’t included automatically when you insert a function. Be sure to add parentheses, such as _`TODAY()`_, when
building a formula.

Unsupported Functions

If a formula in a process uses any of the following functions, the formula returns `null` .

**•** GETRECORDIDS

**•** IMAGE

**•** INCLUDE

**•** PARENTGROUPVAL

**•** PREVGROUPVAL

**•** REQUIRE SCRIPT

**•** VLOOKUP

[For a complete list of operators and functions for building formulas in Salesforce, see Formula Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

Note:

**•** If your process criteria uses a formula, don’t create a formula that always evaluates to true, such as _`2 < 5`_ .

**•** ISCHANGED is available as both a formula function and as an operator. When it’s used as a formula function in process criteria,
you can’t reference a child record’s related fields. For example, ISCHANGED isn’t supported when referencing a

_`[Case].Contact.AccountId`_ field, but it can be used when referencing _`[Case].ContactId`_ .

SEE ALSO:

[Tips for Working with Picklist and Multi-Select Picklist Formula Fields](https://help.salesforce.com/s/articleView?id=sf.tips_for_using_picklist_formula_fields.htm&language=en_US)

Process Builder Advanced Option Considerations

[Tips for Working with Picklist and Multi-Select Picklist Formula Fields](https://help.salesforce.com/s/articleView?id=sf.tips_for_using_picklist_formula_fields.htm&language=en_US)

[Custom Metadata Types and Process Builder](https://help.salesforce.com/s/articleView?id=sf.custommetadatatypes_process_builder.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

###### Considerations for Scheduling Process Actions

Scheduled actions are supported only in record-change processes and event processes. The
scheduled time depends on the type of schedule, whether the field changed, and whether the
process was deactivated.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

####### Process Schedule Limitations

Before you add a schedule to a process, understand the limits and what isn’t supported.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

####### How Does Salesforce Process Scheduled Actions?

Understand the expected behavior for processing scheduled actions based on which type of
schedule they’re associated with, whether the field changed, and whether the process was deactivated.

Transactions and Scheduled Actions
Immediate actions in processes are executed in the same transaction as the operation that triggered the process, such as when a
user creates or edits a record. Scheduled actions are included in a separate transaction.

####### Process Schedule Limitations

Before you add a schedule to a process, understand the limits and what isn’t supported.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**•** If an action group contains scheduled actions, you can’t continue evaluating the next criteria
in your process after executing those actions.

**•** SignupRequest processes don’t support scheduled actions.

**•** Field-based schedules can’t reference a Date or Date/Time field that contains automatically
derived functions, such as TODAY or NOW.

**•** Field-based schedules can’t reference a formula field that includes related-object merge fields.

**•** If you add a schedule for 0 Days Before a date, when you later reopen the process, the schedule
changes to 0 Days After the date. The process still executes at the specified time.

####### How Does Salesforce Process Scheduled Actions?

Understand the expected behavior for processing scheduled actions based on which type of
schedule they’re associated with, whether the field changed, and whether the process was
deactivated.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**Limits for Processing Scheduled Actions**

**•** An org can process up to 1,000 groups of scheduled actions per hour.


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

Automate Your Business Processes with Salesforce Flow Process Builder

Each group of scheduled actions is associated with a schedule, such as “3 days from now.” When a schedule is processed, the
associated actions are executed. If an org exceeds this limit, Salesforce processes the remaining schedules in the next hour.

For example, an org has 1,200 groups of pending actions scheduled to be processed between 4:00 and 5:00 PM. Salesforce processes
1,000 groups between 4:00 and 5:00 PM, and it processes the remaining 200 groups between 5:00 and 6:00 PM.

**Schedules Based on the Current Time**

For example: 3 days from now.

The schedule is evaluated based on the time zone of the user who created the process.

**Schedules Based on a Field Value**

For example: 3 days after a case’s `Created Date` .

Field-based schedules behave differently for record-change processes than they do for event processes.

All Processes:

These considerations apply to both record-change processes and event processes.

**•** If a schedule evaluates to a time in the past, Salesforce executes the associated actions as soon as possible. Depending on how many
actions Salesforce is processing at the time, actions are executed within 1 hour.

For example, a process emails an opportunity owner 7 days before the close date. The process starts for an opportunity with the
close date set to today, so Salesforce executes the scheduled action as soon as possible.

**•** If you set a schedule to **0 Days After** a date, Salesforce executes the associated actions as soon as possible after the time represented
by the date field. Depending on how many actions Salesforce is processing at the time, actions are executed within 1 hour.

**•** If the field referenced by a schedule has a null value, Salesforce ignores the schedule and the associated actions aren’t executed.

**•** When a process schedules an action, Salesforce creates a flow interview record and pauses the interview until the scheduled time
occurs. If the paused flow interview is deleted, Salesforce doesn’t resume the paused flow interview, and the scheduled action isn’t
executed.

Record-Change Processes:

These considerations apply only to record-change processes.

When a record-change process executes a field-based schedule, Salesforce uses the field’s current value. If the value is a date/time field,
Salesforce uses the time zone of the user who created the process. If the value is a date field, Salesforce uses the org’s time zone.

What Happens When the Field Value Changes?

**•** For processes that start when a record is created or edited:

**–** Actions remain scheduled only as long as the criteria for the actions are still valid. If a record no longer matches the criteria,
Salesforce cancels the scheduled actions for the record.

**–** If the referenced field value changes, and the schedule hasn’t been processed, Salesforce recalculates the scheduled time for
the actions using the updated field value.

For example, a process emails an opportunity owner 7 days before the opportunity close date. The close date is set to 2/20/20XX,
and Salesforce schedules the email to be sent on 2/13/20XX. Before the email is sent, the close date is updated to 2/10/20XX.
Salesforce recalculates the scheduled time and schedules the email to be sent on 2/3/20XX.

**•** For processes that start when a record is created, Salesforce never reevaluates the record associated with that process. The scheduled
time for the actions stays the same, even if the record no longer meets the associated criteria when the scheduled actions are
executed.


Automate Your Business Processes with Salesforce Flow Process Builder

**•** If the record or object that the schedule is associated with is deleted, Salesforce cancels the scheduled actions for the record.

Limitations for Converted Leads:

**•** You can’t convert a lead when an unexecuted schedule is based on one of the lead’s fields.

**•** When **Validation and Triggers from Lead Convert** is enabled, scheduled actions on leads aren’t executed during lead conversion.

**•** If a lead is converted into a campaign member before the associated scheduled actions finish, Salesforce still executes the scheduled
actions.

Event Processes:

These considerations apply only to event processes.

**•** When an event process executes a field-based schedule, Salesforce uses the field’s current value in the time zone of the user who
created the process.

**•** The scheduled time for the actions stays the same, even if the field value changes, the associated record or object is deleted, or the
record no longer meets the associated criteria.

**•** If the criteria are met when the process starts, Salesforce executes the scheduled actions.

**What Happens When the Associated Process Is Deactivated?**

After you deactivate a process, the scheduled time for pending scheduled actions stays the same. If a deactivated process has pending
scheduled actions and the record whose field the schedule is based on is changed, Salesforce recalculates the schedule for those actions.

After a process is deactivated, Salesforce ignores all other changes to the associated records. Scheduled actions remain queued and
continue to be processed on time unless the schedule is recalculated.

**What Happens When Scheduled Actions Fail?**
If a scheduled action fails—for example, because the user who caused the process to start is inactive—the admin who created the
process receives an email with details about the failure. Salesforce makes additional attempts to execute a failed scheduled action before
canceling it.

####### Transactions and Scheduled Actions

Immediate actions in processes are executed in the same transaction as the operation that triggered
the process, such as when a user creates or edits a record. Scheduled actions are included in a
separate transaction.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Scheduled actions aren’t performed independently. They’re batched in one transaction with other
actions that are scheduled to execute at the same time, have the same process version ID, and are
executed by the same user ID. This behavior can cause you to exceed your Apex governor limits if
the batch’s actions execute DML operations or SOQL queries.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

A DML operation is used each time a Salesforce record is created, updated, or deleted, such as when
a process executes a Create a Record action. A SOQL query is used each time Salesforce looks up information about an existing record,
such as when a process executes an Update Records action. For details on Apex governor limits, see Process Limits on page 908.

To improve performance further and help avoid Apex governor limits, design scheduled actions to take advantage of bulkification.


Automate Your Business Processes with Salesforce Flow Process Builder

Tip: Design a process with a scheduled action so that it doesn’t execute mixed DML operations. A single transaction can’t mix
DML operations on data objects (such as Account), Setup objects (such as User Role), and external objects. For example, you can’t
update an account and a user role in a single transaction.

If a process has more than one group of scheduled actions and a group fails to execute in a batch:

**•** Prior groups of scheduled actions in that batch’s transaction are successful.

**•** The immediate actions for that process are successful.

**•** All scheduled actions in that group aren’t executed.

**•** Each remaining group of scheduled actions in that batch is executed in a separate transaction.

Example: Salesforce processes two groups of scheduled actions in the same batch. In the first group, one action fails, so the
process fails. Subsequent actions within the first group aren't tried. Salesforce processes the second group in a separate transaction.

Note: The execution time is now in the past, so Salesforce executes the second group of scheduled actions within 1 hour.

###### Considerations for Processes that Send Custom Notifications

Before you begin sending custom notifications, learn about important storage, recipient, and org
limits.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**•** You can create up to 500 custom notification types.

**•** Each notification can have up to 10,000 users as recipients. However, you can add an action to
the same process within Process Builder or to the same flow in Flow Builder to have more
recipients.

**•** Your org saves your most recent 1 million custom notifications for view in notification trays.
Your org can save up to 1.2 million custom notifications, but it trims the amount to the most
recent 1 million notifications when you reach the 1.2 million limit.

**•** An org can execute up to 10,000 notification actions per hour. When you exceed this limit, no
more notifications are sent in that hour, and all unsent notifications are lost. Notification actions
resume in the next hour.

For example, your notification action processes are triggered 10,250 times between 4:00 and
4:59. Salesforce executes the first 10,000 of those actions. The remaining 250 notifications aren’t
sent and are lost. Salesforce begins executing notification actions again at 5:00.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**•** When you send a custom notification from a process, the Target ID for the notification is the record that started the process. However,
target records that don't have their own detail page (for example, a case comment, which appears only in a Case Comment related
list) don't support direct navigation. Use Flow Builder to send the notification from a flow and specify either a different Target ID or
Target Page Reference.

[Tip: To see how to specify the target using JSON, see pageReference.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_navigation_page_definitions.htm)

**•** Custom notification title and body fields support plain text only.

**•** [The content of custom push notifications depends on the Display full content push notifications setting. If full content push notifications](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)
aren’t enabled, only the notification title is sent.


Automate Your Business Processes with Salesforce Flow Process Builder

###### Considerations for Processes That Post to Chatter

The Post to Chatter action doesn’t support Experience Cloud sites, and there are some limitations
around what you put in the message.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Unsupported Feeds

Processes can’t post to an Experience Cloud site user or group.

Chatter Message

**•** You can add up to 25 @mentions to a Chatter message.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If you use Microsoft [®] Internet Explorer [®] version 11, you can’t paste text into a message. Copy and paste actions are allowed in all
other supported browsers.

**•** Don’t start the message with a field reference, such as _`{![Account].Name}`_ . Otherwise, the action fails to save. To work around
this issue, add a space at the beginning of the message.

Deploying Processes That Post to Chatter

If your process posts to the Chatter feed of a specific user or group, the process runs only in the source org. The IDs referenced by the
Post to Chatter action don’t exist in the target org.

###### Considerations for Processes That Update Records

Understand what happens when you change a record owner, update the same field multiple times,
or update currency fields in a multiple currency org.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Updating a Record’s Owner

Processes that update owners don’t automatically transfer the associated items. Use an Update
Records action for each type of child record that you want to transfer.

For example, you want to transfer an account to a new owner. Add four Update Records actions to
your process. The first updates the account. The second updates the child contacts. The third updates
the child opportunities. And the fourth updates the child contracts.

Multiple Updates to the Same Field

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If multiple Update Records actions apply different values to the same field, the last action’s value is used.

Multiple Currencies

If your org uses multiple currencies, the currency fields are updated using the record’s currency code. If you use a formula to update a
field, the formula values use the record’s currency code.


Automate Your Business Processes with Salesforce Flow Process Builder

Inactive Users

Processes can't update records that inactive users own. When you deactivate a user, also transfer that user's records to an active user to
avoid failed processes.

SEE ALSO:

[Transferring Records](https://help.salesforce.com/s/articleView?id=sf.data_about_transfer.htm&language=en_US)

##### Considerations for Managing Processes

Understand what happens when you install, activate, or delete processes.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Installed Processes

If you install a non-template process from a managed package, you can only activate or deactivate
it. If the process is a template, you can view and clone it, and you can edit the clone.

Active Processes

After you activate a process, you can no longer edit it.

Deleting Processes

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can’t delete a process when it has unexecuted groups of scheduled actions. The workaround is to delete the unexecuted groups
of unscheduled actions on page 980.

##### Considerations for Deploying Processes

Keep these considerations in mind when deploying processes, such as when using packages or
change sets.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Processes That Reference Other Components

If you deploy a process that contains any of the following actions, the corresponding components
aren’t included in the package or change set automatically. To deploy successfully, manually add
the referenced components to the package or change set.

**•** Apex

**•** Email Alerts

**•** Launch a Flow

**•** Post to Chatter

**•** Quick Actions


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Change sets are available
in: **Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Packages are available in:
**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Process Builder

**•** Submit for Approval

Templates

If you install a process template from a package, make sure the process is inactive unless you want it to actively run in your org.

If you add a process template to a package, first deactivate the process unless you’re sure that installers want that process to be active
in their orgs.

Deploying Processes That Post to Chatter

If your process posts to the Chatter feed of a specific user or group, the process runs only in the source org. The IDs referenced by the
Post to Chatter action don’t exist in the target org.

SEE ALSO:

Deploy Processes and Flows as Active

##### Considerations for Processes in Transactions

Each process runs in the context of a transaction. A transaction represents a set of operations that
are executed as a single unit. When a process is triggered more than one time in a single transaction,
Salesforce executes similar actions in one batch.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

By default, if one process in a batch fails, it causes all the processes in the batch to fail, and the
transaction rolls back. If one process in a batch fails while executing one of these actions, Salesforce
attempts to save all successful record changes in the batch up to three times.

**•** Create a Record

**•** Flows (Create Records and Update Records elements only)

**•** Processes (Create a Record and Update Records actions only)

**•** Update Records

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: When you upload 100 cases, the flow MyProcess_2 triggers one process for each case.

**•** 50 processes stop at Create a Record action Create_Task_1.

**•** The other 50 processes stop at Create a Record action Create_Task_2.

The result? At least two groups of bulk operations to execute.

**•** One for the 50 processes that execute Create_Task_1

**•** One for the 50 processes that execute Create_Task_2


Automate Your Business Processes with Salesforce Flow Process Builder

#### Setting Values in the Process Builder

Throughout the Process Builder, you must set values, for example, to set conditions in a criteria
node, to set the fields on a new case in a Create a Record action, or to specify an Apex method to
reference.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

##### Field Picker

Use the field picker to reference fields on the record that started the process or fields on related
records.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Process Builder Value Types
When setting a value for a given field—whether on the record that started the process or a related record— the available value
types are filtered based on the field that you’ve selected.

Multi-Select Picklists in the Process Builder
The Process Builder lets you select multiple values for a multi-select picklist field.

##### Field Picker

Use the field picker to reference fields on the record that started the process or fields on related
records.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

To use fields on a related record, click a field with next to the value. For example, use the Account
ID field value on the case’s contact account.

The field picker displays only the fields that are compatible with the selected parameter.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

##### Automate Your Business Processes with Salesforce Flow Process Builder

If you see a field multiple times, it means that the field can relate to multiple objects. For example, if you created a queue for cases, a
case’s owner can be either a user or a queue. `Owner ID` is a _polymorphic field_ —a field that relates to more than one object.

To access a field on the case’s owner, choose the appropriate relationship. If you select **Owner ID (User)** and the owner of the record
is a queue, the process fails.

Note: Queue labels aren't supported in process criteria. For example, you can't use `[Lead].Owner:Queue.Name` in process
criteria. Instead, use `[Lead].Owner:Queue.DeveloperName` to reference the queue's API name.

##### Process Builder Value Types

When setting a value for a given field—whether on the record that started the process or a related
record— the available value types are filtered based on the field that you’ve selected.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

The available value types are:

**•** Currency—Manually enter a currency value.

**•** Boolean—Choose a true/false boolean value.

**•** Date/Time or Date—Manually enter a date/time or date value.

**•** Formula—Create a formula expression.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Global Constant—Choose a global constant to set a value to null or an empty string—for example, choose $GlobalConstant.Null.

Note: These global constant values aren’t supported with the `is null` operator.

**–** `$GlobalConstant.Null`

**–** `$GlobalConstant.EmptyString`

**•** ID—Manually enter a Salesforce ID value, for example, _`00300000003T2PGAA0`_ .

Note: If your process is based on a user ID (for example, when an [Event].OwnerId equals a specific ID value) make sure that
the ID value is an 18-character ID and not a 15-character ID. You can convert a 15-character ID to 18 characters at
[www.adminbooster.com/tool/15to18.](http://www.adminbooster.com/tool/15to18)

**•** Multi-Picklist—Choose one or more multi-select picklist values.

**•** Number—Manually enter a number value.

**•** Picklist—Choose a picklist value.

**•** Queue—Search for a specific queue in your org.

**•** Reference—Choose a field on the record or on a related record.

**•** String—Manually enter a string value.


Automate Your Business Processes with Salesforce Flow Process Builder

**•** User—Search for a specific user in your org.

##### Multi-Select Picklists in the Process Builder

The Process Builder lets you select multiple values for a multi-select picklist field.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

For example, set multiple values for the `Country` field for a company record that operates in
Ireland, the UK, and France.

You can use multi-select picklists in:

**•** Formulas

**•** Process criteria

**•** Create a Record actions

**•** Quick Actions

**•** Update Records actions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

In process criteria, set multiple values by creating one condition for each individual multi-select picklist value. For example, if your process
checks whether changes were made to an account’s office locations, reference multiple values by choosing the same field for each
multi-select picklist value.

[Refer to Tips for Working with Picklist and Multi-Select Picklist Formula Fields for more information.](https://help.salesforce.com/s/articleView?id=sf.tips_for_using_picklist_formula_fields.htm&language=en_US)

When you reference a multi-select picklist field in an action, enter values by clicking **Choose values…**

Add or remove values by dragging them between the Available (1) and Selected (2) columns.


Automate Your Business Processes with Salesforce Flow Process Builder

Keep these considerations in mind when using operators with multi-select picklists.

**•** If you select only one value from a multi-select picklist field, you can use the Equals operator.

**•** If you use the Equals operator with multiple multi-select picklist values and choose the **Any of the conditions are met (OR)** option,
the condition matches on one value only. For example, if your process checks whether a Region field equals West or East, the condition
evaluates to true when the value is West or when the value is East, but doesn’t evaluate to true when both West and East are selected
values.

**•** If you use **Contains** and **OR** to evaluate multiple multi-select picklist values, the condition evaluates to true on multiple values. For
example, if your process checks whether a `Region` field contains West or East, the condition evaluates to true when a `Region`
field contains West and East or when a `Region` field contains West or East values.

#### Setting Advanced Options in the Process Builder

The Process Builder lets you choose some advanced options for executing actions in your processes.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Process Builder Advanced Option Considerations
Keep these considerations in mind when choosing advanced options.

Reevaluate Records in the Process Builder
When you add objects to your process, you can choose to evaluate a record multiple times in
a single save operation.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

##### Automate Your Business Processes with Salesforce Flow Process Builder

Nest Processes in the Process Builder
_Invocable processes_ let you modularize sections of your processes and add more logic to them. An _invocable process_ is a process that
starts when another process invokes it. `The process starts when` in the process’s properties controls whether a process
is invocable.

Avoid Unwanted Actions in Processes
When you add criteria to your process, you can choose to execute actions when specified criteria change.

##### Process Builder Advanced Option Considerations

Keep these considerations in mind when choosing advanced options.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**•** Avoid creating an infinite loop when allowing your process to reevaluate records. For example,
if your process checks whether an account description changes and then updates an account
description and creates a Chatter post every time an account record is created or edited, the
process evaluates and triggers actions resulting in six Chatter posts.

**•** If you choose to evaluate a record multiple times in a single save operation when you specify
an object for your process, we recommend not setting any of your criteria to No criteria—simply
execute the actions!

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If your process uses ISCHANGED, ISNEW, or PRIORVALUE formula functions, we recommend that you don’t use the advanced options.
If you do use advanced options, keep these considerations in mind.

**–** When a record is first created, ISNEW evaluates to true. If your process uses the ISNEW formula function and reevaluates a record
multiple times in a single save operation, the process executes actions multiple times.

For example, your process checks whether an account is created or updated. Each time the criteria is evaluated, ISNEW evaluates
to true. The result is six Chatter posts. This example is true only if the process is triggered because an account record is created.

**•** When ISNEW evaluates to true, the process updates the account’s annual revenue and posts to Chatter.

**•** When the process updates the account’s annual revenue, the process then reevaluates the record (up to five additional
times) because the record was changed.

**–** When a record is created, PRIORVALUE returns the current value as the prior value. When a record is updated, PRIORVALUE
returns the field value that was set immediately before the save operation started. If your process uses the PRIORVALUE formula
function and reevaluates a record multiple times in a single operation, the process executes actions multiple times. If your process
reevaluates a record multiple times in a single save operation and executes actions only when specified criteria changes, the
prior value returns the values that existed before the record was saved.

For example, your process checks whether an account is created or updated. Each time the record is reevaluated, the prior value
of the account’s type is Prospect. The result is six Chatter posts.

**•** Wen _`PRIORVALUE([Account].Type) = 'Prospect'`_ evaluates to true, the process updates the account’s
annual revenue and posts to Chatter.

**•** When an account is created with _`Prospect`_ as the account type, the criteria is always true until the end of the process
transaction.

**•** If the process is changed to update the account type to _`Other`_ when the criteria is true, then for an account created with
_`Prospect`_ as the account type, the formula _`PRIORVALUE([Account].Type) = 'Prospect'`_ is true until
the end of the process transaction.

**–** ISCHANGED always evaluates to false when a record is first created.


Automate Your Business Processes with Salesforce Flow Process Builder

For example, your process checks whether an account description
changes— _`ISCHANGED([Account].Description)`_ —and the process also reevaluates records multiple times in a
single save operation. If an account is first created with a blank description value and another process updates the account
description in the same save operation, ISCHANGED evaluates to true every time the record is reevaluated because it compares
the account description value when the record was first created (a blank value) with whatever is set for the current value.

Let’s say this same process creates a Chatter post every time ISCHANGED([Account].Description) evaluates to true. This process
would create a recursive loop resulting in six Chatter posts because ISCHANGED evaluates to true throughout the save operation.

##### Reevaluate Records in the Process Builder

When you add objects to your process, you can choose to evaluate a record multiple times in a
single save operation.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

It's kind of like using a roundabout instead of a four-way stop to control process traffic. Instead of
stopping and waiting for separate save operations, reevaluating records helps your business traffic
flow a little more freely.

If you choose this option, the process can evaluate the same record up to five additional times in
a single save operation. It might reevaluate the record because a process, workflow rule, or flow
updated the record in the same save operation. When a record is reevaluated, the process uses the
most recent values for that record.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

For example, your sales review process includes multiple steps, approvals, notifications, and fields that need to be updated. Some of
these changes may be part of your process, or they may be managed by other workflow rules or flows in your org. If you let the process
reevaluate a record multiple times in a single save operation, you can manage and evaluate all of these changes—even changes from
other processes—in a single save operation in your process.

SEE ALSO:

Process Builder Advanced Option Considerations

##### Nest Processes in the Process Builder

_Invocable processes_ let you modularize sections of your processes and add more logic to them. An
_invocable process_ is a process that starts when another process invokes it. `The process starts`
`when` in the process’s properties controls whether a process is invocable.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

To invoke a process from another process, you configure a Processes action. That configuration
includes passing a record to the invocable process, which is how the process knows which record
to start with. Because the record is passed from one process to another, the invocable process
receives a certain version of that record. That version differs depending on when the Processes
action is executed.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

Immediate Action

When you invoke a process through an immediate action, the process receives the values that the record contained when the top-level
process starts.

Example: Process 1 updates an account and then invokes Process 2 based on that account. Process 2 receives the version of the account
when Process 1 started.

Scheduled Action

When you invoke a process through a scheduled action, the process receives the latest values for the record.

Example: Process 1 updates an account and, 15 minutes later, invokes Process 2 based on that account. Process 2 receives the latest
version of the account from the database.

When Should I Build an Invocable Process?

Do you find yourself building the exact same actions for multiple action groups? Configure those actions one time in an invocable
process, and then invoke that process from all the relevant action groups. Later, to update those actions, update the one invocable
process. Then all the other processes use the updated actions.

Another cool scenario for invocable processes: nesting simple logic. Processes handle simple “if/then” statements. But what if you must
nest some of those statements? Rather than having to build a flow or write code, build the second level of logic into another process.
Invoke the second process from the first, and voila!

Example: Let’s say you handle all of your case management in a single process. But you must treat escalated cases for high-revenue
accounts differently from escalated cases for regular accounts. If an account whose renewal date is less than a month away escalates
the case, notify the account owner, the regional manager, and the VP of that region. If an account whose renewal date is more
than a month away escalates the case, notify only the account owner and the regional manager.

To do so, you build an invocable process. Let’s call it “Escalated Cases.” The process operates on the Case object and has two criteria
nodes.

**•** The first criteria node evaluates whether the associated account’s renewal date is less than a month away. When a case meets
that criteria, the process posts to the account’s feed with a link to the case and mentions the account owner, regional manager,
and regional VP.

**•** The second criteria node has no criteria. If a case doesn’t meet the first node’s criteria, the process performs the same action,
except that it doesn’t mention the regional VP.

Now back to the process that automates your case management. You already have a criteria node that checks whether the case
is escalated. Add a Processes action to that criteria’s action group, and configure the action to invoke the “Escalated Cases” process.


Automate Your Business Processes with Salesforce Flow Process Builder

##### Avoid Unwanted Actions in Processes

When you add criteria to your process, you can choose to execute actions when specified criteria
change.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

For example, your process sends an email alert whenever a case has an Escalated status. Let’s say
your support team repeatedly updates the case description with new information. Whenever the
case is saved with a new description, your process can check specifically whether the Escalated
status changed, rather than repeatedly sending email alerts. This way, the process executes actions
only if the status was changed to Escalated during the latest update.

Tip: Check out this short video [Avoid Unwanted Actions in Your Process to learn more](https://salesforce.vidyard.com/watch/1sbznRSzxtxhzRi3Hn_9ag)
about this option.

This setting isn’t supported if:

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**If Yes is...** **Actions are executed if...** **Actions are not executed if...**

Selected

**•** The record was created. **•** The record’s current values meet the conditions, and

the record’s most recent previous values met the

**•** The record was updated. Its current values meet the

criteria.

**•** The record was created.

**•** The record was updated. Its current values meet the

criteria.

conditions, and its most recent previous values did not
meet the conditions. **•** The record’s current values don’t meet the conditions.

Deselected The record’s current values don’t meet the conditions.

**•** The record was created.

**•** The record was updated, and its current values meet
the conditions.

**•** Your process starts only when a record is created.

**•** Your process starts when a record is created or edited and the criteria node doesn’t evaluate any criteria.

**•** The criteria node evaluates a formula, but the formula doesn’t include a reference to the record that started the process.

**•** Your process uses the Is changed operator in a filter condition.

SEE ALSO:

Process Builder Advanced Option Considerations


Automate Your Business Processes with Salesforce Flow Process Builder

#### Create a Process

To create a process, define its properties and which records it evaluates, and then add criteria nodes
and actions.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

##### 1. Define the Process Properties

The process properties uniquely identify your process.

2. Configure the Process Trigger
Every process includes a trigger, which tells the process when to start. How you configure that
trigger depends on what type of process you’re creating.

3. Add Process Criteria
Define the criteria that must be true before the process can execute the associated actions.

4. Add Actions to Your Process
After you define a criteria node, define the actions that are executed when the criteria are met.
Actions are executed in the order in which they appear in the Process Builder.

5. Execute Actions for Multiple Criteria
Choose whether to stop or continue your process after specific criteria are met and associated
actions execute.

##### Define the Process Properties

The process properties uniquely identify your process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**1.** From Setup, in the Quick Find box, enter _`Builder`_, and select **Process Builder** .

**2.** Click **New**, or click the process name and then click Edit Properties.

**3.** Define the process properties by completing the fields.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

```
Process

Name

API Name

```

The name for your process, up to 255 characters.

This name appears in the process management page, so name your process
to differentiate it from other processes. To see the page in Setup, enter
_`Builder`_ in the Quick Find box, then select **Process Builder** .

The name that the API and managed packages use, up to 79 characters.

This name must be unique across all processes and flows. The name must
begin with a letter and use only alphanumeric characters and underscores.
It can't include spaces, end with an underscore, or have two consecutive
underscores.


Automate Your Business Processes with Salesforce Flow Process Builder

**Field** **Description**

After it's saved, you can’t change the process’s API name.

```
Description

```

Optional. A description for your process.

The description also appears in the process management page. It’s intended to help you differentiate
between processes, such as to explain what a process does.

`The process` Identifies when the process begins. You can set your process to start when:
`starts when` **•** A record changes

**•** A platform event message is received

**•** It’s invoked by another process

This field is available only when creating a process.

```
  Template

  API Version

  for Running

  the Process

```

**4.** Click **Save** .

Specifies whether the process is a template. When a template is installed from a managed package, the
subscriber can view and clone the process and customize the clones. Non-template processes that are
installed from managed packages can only be activated and deactivated.

Suppose that your company needs a process that differs slightly for each country where you do business.
You can create or install a template for the base process and then clone it to create each country-specific
process. Even if you don’t use managed packages, you can use this field to clearly identify the base process.

This field is available only when editing a process.

Determines which versioned run-time behavior improvements the process adopts.

Changing this field requires the Manage Flows permission. Before you select a new API version, review all
run-time improvements that were delivered between the currently selected API version and the new API

version. You can find all flow and process run-time improvements for an API version in the Salesforce Release
Notes.

By default, when you create a process, it runs in the latest API version. If you clone an existing process as a
new process or process version, the existing process’s run-time API version is used in the new process or
process version.

The run-time API version doesn’t change as future Salesforce releases roll out. You decide when, if ever, to
change the API version for running each process. This field lets you test and upgrade your processes one by
one, and at your own pace. You can even opt to never adopt versioned updates for one or all your processes.


Automate Your Business Processes with Salesforce Flow Process Builder

##### Configure the Process Trigger

Every process includes a trigger, which tells the process when to start. How you configure that
trigger depends on what type of process you’re creating.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Record Change
If the process starts when a record changes, associate the process with an object, and specify
when to start the process.

Event
If the process starts when a platform event message is received, associate the process with a
platform event and an object, and specify matching conditions. Because every process acts on
a Salesforce record, it requires a single record as a starting point. That way, the criteria and
actions know where to start evaluating and executing.

Invocable
If the process starts when another process invokes it, associate the process with an object.

Record Change

If the process starts when a record changes, associate the process with an object, and specify when
to start the process.

**1.** Click **Add Object** .

**2.** Configure the trigger.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Event processes are
available in: **Performance**,
**Unlimited**, **Enterprise**, and
**Developer** Editions

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**3.** Before saving your changes, confirm the selection because you can’t change the object after you save it.


Automate Your Business Processes with Salesforce Flow Process Builder

Event

If the process starts when a platform event message is received, associate the process with a platform event and an object, and specify
matching conditions. Because every process acts on a Salesforce record, it requires a single record as a starting point. That way, the
criteria and actions know where to start evaluating and executing.

**1.** Click **Add Trigger** .

**2.** Configure the trigger.

**3.** Before saving your changes, confirm the selection because you can’t change the platform event or object after you save it.

Invocable

If the process starts when another process invokes it, associate the process with an object.

**1.** Click **Add Object** .

**2.** Select an object to associate with the process. Type to filter the dropdown list.

This process can be invoked from any other process as long as the main process passes a record of this object type. For example, an
Account-based invocable process can be called from a Contact-based record change process, because you can pass the contact’s
account to the invocable process.


Automate Your Business Processes with Salesforce Flow Process Builder

**3.** Before saving your changes, confirm the selection because you can’t change the object after you save it.

##### Add Process Criteria

Define the criteria that must be true before the process can execute the associated actions.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

When the criteria are met, the process executes the associated action group. When criteria aren’t
met, the process skips the action group and evaluates the criteria for the next action group.

**1.** Click **Add Criteria** .

**2.** Enter a name for this criteria node.

Note: The name appears on the canvas, so use a name that helps you differentiate it
from other criteria nodes. Actions have their own names, so we recommend summarizing
only the criteria with this name. For example, if the criteria checks whether a case is
escalated, use _`Is Escalated?`_ .

**3.** Select the type of criteria that you must define. This selection determines which fields appear
later in the dialog box.

**If you need...** **Select**

The record to have certain field values. Conditions are
met

For example, to execute the associated actions on opportunity records
with an amount greater than $5,000, set the filter to:

```
  [Opportunity].Amount greater than $5000.00

```

To evaluate the record by using a formula. Formula
evaluates to true

For example, to execute the associated actions on accounts whose annual
revenue is over $1,000,000 when the account is changed by someone
other than the owner, use this formula.

```
  AND (([Account].LastModifiedBy.Id <>

  [Account].Owner.Id), ([Account].AnnualRevenue

  > 1000000) )

```

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

To simply execute the associated actions without evaluating the record.

The process executes all the actions that are associated with this criteria
node and, unless you specify otherwise, doesn’t evaluate any remaining
criteria nodes in the process. If you choose to stop your process after
executing these actions, we recommend choosing this option for only
the last criteria node in your process.

**4.** If you selected “Conditions are met”:

No
criteria—execute
the actions!

**a.** Define the filter conditions by identifying the field values that the process must evaluate.


Automate Your Business Processes with Salesforce Flow Process Builder

`Field` Select the field whose value you want to evaluate. You can also evaluate values for records that are related to

the one that started the process. To do so, click a related record with next to the ID field.

For example, if a contact record started the process, you can evaluate the value for the contact’s account’s

`Annual Revenue` field. To access that field, click `Account Id`, select **Annual Revenue**, and then
click **Choose** .

`Operator` The available operators depend on the field’s data type.

`Type` The available value types depend on the field’ data type.

`Value` Identify the value that you want to evaluate the field for. See Setting Values in the Process Builder on page 927
for details.

**b.** For `Conditions`, identify which conditions must be true for the process to execute the associated actions.

If you choose to use custom logic, enter up to 1000 characters by using:

**•** Numbers to refer to each condition

**•** _`AND`_, _`OR`_, or _`NOT`_ to identify which combination of conditions must be true

**•** Parentheses to group parts of the string together

For example, if you enter _`1 AND NOT (2 OR 3)`_, the outcome evaluates to true if the first condition is true and the second
or third outcome is false.

Tip: Ambiguous logic can cause validation errors. To avoid ambiguity, use parentheses in your custom logic. For example:

**•** _`1 AND 2 OR 3`_ results in an error

**•** _`1 AND (2 AND 3) OR 4`_ doesn't result in an error

**5.** If you selected “Formula evaluates to true,” define the formula.

**6.** Optionally, to specify whether you want to execute the actions only if the record was created or edited to meet criteria, click **Advanced**
at the bottom of the panel.

For details, see Avoid Unwanted Actions in Processes on page 934.

Note: This setting is available only if the process starts when a record is created or edited and you selected “Filter conditions
are met” or “Formula evaluates to true.”

**7.** Click **Save** .

SEE ALSO:

Execute Actions for Multiple Criteria


Automate Your Business Processes with Salesforce Flow Process Builder

##### Add Actions to Your Process

After you define a criteria node, define the actions that are executed when the criteria are met.
Actions are executed in the order in which they appear in the Process Builder.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

An action group can consist of a combination of immediate and scheduled actions. Immediate
actions are executed when evaluation criteria are met. Scheduled actions are executed at a specified
time. For example, Salesforce can automatically send an email reminder to the account team if a
high-value opportunity is still open 10 days before the specified close date.

Before you begin, consider whether you want this action to be executed immediately or at a specific
time. If you want to execute the action at a specific time, identify when those actions should be
executed.

##### 1. Click Add Action .

**2.** Select the type of action to create, and then fill out the fields to define the action.

Create a Record from a Process
Create a record by manually entering values or by using the values of related records.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Invoke a Process from Another Process
Invoke a process from another process. With invocable processes, you have the option of reuse so that you don’t spend your time
on repetitive work.

Create a Chatter Post from a Process
Post to the feed of a user, a Chatter group, or the record that started the process.

Use a Quick Action from a Process
Create a record, update a record, or log a call by using a quick action that you or another admin created for your organization.

Work with Quip from a Process
Create documents, chat rooms, and folders when important events occur. Attach a document to a record so your users have
information in context. Update your spreadsheets with the latest Salesforce data. Send a message to a chat room or document. Add
new slides to a deck, copy documents, add members to a document or chat, and more.

Launch a Flow from a Process
Start an autolaunched flow from your process to automate complex business processes. Create flows to perform logic and have
events trigger the flows via processes without writing code.

Send an Email from a Process
Easily send an email from a process by using an email alert. Email alerts are configured outside of the Process Builder and contain
the standard text, list of recipients, and template for an email.

Send a Custom Notification from a Process
Send customized notifications when important events occur. Alert an account owner if a new support case is logged while trying
to close a deal, or send a notification for a workflow built entirely with custom objects. Add recipients and content to your custom
notification, then add it to your process.

Send a Survey Invitation from a Process
Send an email invitation containing the link to a particular survey question or to launch a survey.


Automate Your Business Processes with Salesforce Flow Process Builder

Submit a Record for Approval from a Process
Submit the record that started the process for approval.

Update Records from a Process
Update one or more records that are related to the record that started the process by manually entering values or by using the values
from related records.

Call Apex Code from a Process
Add customized functionality to your process by calling Apex from the process.

###### Specify When Your Actions Execute with a Schedule

In record-change processes and event processes, you can schedule actions to execute at a specific
time. An action group that supports scheduled actions can have multiple schedules. For example,
you can schedule some actions to execute one day from now and others to execute three days
from now.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Note: Before adding scheduled actions to your process, understand how they work. Review
Scheduled Actions Considerations.

To schedule actions in a record-change process, make sure that one of the following options is true
for your action group.

**•** The process starts only when a record is created (1).

**•** The process starts when a record is created or edited (2), and the associated criteria node
executes actions only when specified changes are made (3).


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

**1.** In an action group that supports scheduled actions, click **Set Schedule** .

**2.** If you must schedule actions based on a date/time field on the record that started the process:

**a.** Leave the first radio button selected.

**b.** From the dropdown list on the right side of the panel, select the date to schedule the action.
For example, if your process is based on an account record, choose the account’s **Created Date** .

**c.** Specify the number of days or hours before or after the field.

For a record-change process, if the criteria for this action group are still met when this time occurs, Salesforce executes the
scheduled actions. For an event process, the criteria aren’t checked when this time occurs. If the criteria was met when the
process started, Salesforce executes the scheduled actions.

**3.** If you must schedule actions after a certain number of days or hours from when the process is executed:

**a.** Select the second radio button.

**b.** Specify the number of days or hours from when the process is executed.

If the criteria for this action group are still met when this time occurs, Salesforce executes the scheduled actions.

**4.** Save the schedule.

###### Create a Record from a Process

Create a record by manually entering values or by using the values of related records.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create an action and select “Create a Record” for the type, fill in the relevant fields to add
the action to your process. The new record’s `Created By` field is then set to the user who started
the process by creating or editing a record.

Warning: If you create processes to replace any workflow rules, ensure that you delete those
workflow rules when you activate the equivalent processes. Otherwise, both workflow rules
and processes fire and cause unexpected results, such as overwritten records or redundant
email messages. Do the same if you create processes to replace any Apex triggers.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** For `Record Type`, select the object that you want to create a record for. To filter the
dropdown list, type the name of the object to filter the dropdown list.

When you select an object, at least one row appears to allow you to set field values for the new
record.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Warning: Rows appear automatically for fields required by the API. If you must provide values for other fields, we recommend
that you refer to your organization's page layouts to determine which fields are required.

**3.** Set the record’s field values.

`Field` Select the field whose value you want to set. To filter the dropdown list, type the name of the field.


Automate Your Business Processes with Salesforce Flow Process Builder

`Type` Select the type of value that you want to use. The available types depend on the field that you’ve selected.

`Value` Set a value for the field. by using the text entry field to manually enter a value or the field picker to use a field value
from a related record. See Setting Values in the Process Builder on page 927 for details.

**4.** Click **Save** .

Tip:

**•** If you set up your process to create an account record, _`Name`_ appears as a required field. If you want to create a person
account, you can add _`LastName`_ as a field but it doesn’t appear as required by default. You can enter a dummy value
for the _`Name`_ field.

**•** When you create a record, required fields normally appear at the top of the list. However, if you save a Create a Record
action, close the process, and then reopen the action, required fields don’t always appear in the normal order.

**•** If a platform event is configured to publish immediately, the process publishes each event message outside of the database
transaction. If the transaction fails and is rolled back, the event message is still published and can’t be rolled back. So if you
see an informational message under the selected platform event, consider whether you want the process to publish an
event message only after the transaction commits successfully.

SEE ALSO:

_Platform Events Developer Guide_ [: Decoupled Publishing and Subscription](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_considerations_decoupled_processes.htm)

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_define_ui.htm)_ : Platform Event Fields

###### Invoke a Process from Another Process

Invoke a process from another process. With invocable processes, you have the option of reuse so
that you don’t spend your time on repetitive work.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create an action and select “Processes” for the type, fill in the relevant fields to add the
action to your process.

You can invoke processes with objects that share at least one unique ID. For example, in the Account
and Case objects, the `AccountId` field is unique to Account and also used by Case. You can
create an invocable process that updates a Case record. Then you can invoke it from:

**•** A process that updates an Account record’s owner

**•** A process that adds an Account shipping address or updates it

When you create a process that invokes another process, each one counts toward your process
and other applicable limits. DML limits in processes that invoke processes count as one transaction.

Warning: If you create processes to replace any workflow rules, delete those workflow rules
when you activate the equivalent processes. Otherwise, both workflow rules and processes
fire and cause unexpected results, such as overwritten records or redundant email messages.
Do the same if you create processes to replace any Apex triggers.

**1.** Enter a name for this action.


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

This text appears on the canvas and helps you differentiate this action from others in your process. The name truncates to fit on the
canvas.

**2.** Select an invocable process. You can only select active invocable processes.

**3.** Select your process variable. Remember that you can only select fields related to the object associated with the process you invoke.

###### Create a Chatter Post from a Process

Post to the feed of a user, a Chatter group, or the record that started the process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

This action is available only if your organization has Chatter enabled. The feed item appears as if
the user who started the process—by creating or editing a record—created the post.

Post to a User’s Chatter Feed from a Process
Post to the feed of a user by identifying a specific user in your organization or a User lookup
field on a record.

Post to a Chatter Group from a Process
Post to the feed of a specific Chatter group.

Post to a Record’s Chatter Feed from a Process
Post to the feed of the record that started the process.

Mention a User or Group in a “Post to Chatter” Process Action
When you post to a Chatter feed from a process, you can mention users if you can reference
the corresponding User ID field from the field picker.

SEE ALSO:

[Chatter Settings](https://help.salesforce.com/s/articleView?id=sf.collab_enable.htm&language=en_US)

Considerations for Processes That Post to Chatter


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

####### Post to a User’s Chatter Feed from a Process

Post to the feed of a user by identifying a specific user in your organization or a User lookup field
on a record.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created an action and selected “Post to Chatter” for the action type, fill in the relevant
fields to add the action to your process.

Warning: If the feed that the process tries to post to isn't available when the process is
triggered (for example, because the user is now inactive), the user sees an error and the
process fails.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

####### 2. In the Post to field, select User.

**3.** For `User`, select where you want to find the user.

**4.** Based on your selection for `User`, search for or browse for the user whose feed you want to
post to.

When you select a user from a record, you must ultimately select a field that contains a user’s
ID—for example, `Owner ID` or `User ID` .

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**5.** Fill out the message that you want to post. You can insert merge fields, add a topic, and mention users or groups.

The message can contain up to 10,000 characters.

You can only reference topics that exist. If you reference a merge field and that field doesn’t have a value, it appears as a blank value.

**6.** Save the action.

SEE ALSO:

[Chatter Settings](https://help.salesforce.com/s/articleView?id=sf.collab_enable.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Post to a Chatter Group from a Process

Post to the feed of a specific Chatter group.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created an action and selected “Post to Chatter” for the action type, fill in the relevant
fields to add the action to your process.

Warning: If the feed that the process tries to post to isn't available when the process is
triggered, the user sees an error and the process fails.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

####### 2. In the Post to field, select Chatter Group.

**3.** For `Group`, search for the Chatter group whose feed you want to post to.

**4.** Fill out the message that you want to post. You can insert merge fields, add a topic, and mention
users or groups.

The message can contain up to 10,000 characters.

You can only reference topics that exist. If you reference a merge field and that field doesn’t
have a value, it appears as a blank value.

**5.** Save the action.

SEE ALSO:

[Chatter Settings](https://help.salesforce.com/s/articleView?id=sf.collab_enable.htm&language=en_US)


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

####### Post to a Record’s Chatter Feed from a Process

Post to the feed of the record that started the process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

You can post to the record’s Chatter feed only if feed tracking is enabled for the object that the
process is associated with.

After you’ve created an action and selected “Post to Chatter” for the action type, fill in the relevant
fields to add the action to your process.

Warning: If the feed that the process tries to post to isn't available when the process is
triggered (for example, because the user is now inactive), the user sees an error and the
process fails.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

####### 2. In the Post to field, select This Record.

**3.** Fill out the message that you want to post. You can insert merge fields, add a topic, and mention
users or groups.

The message can contain up to 10,000 characters.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

You can only reference topics that already exist. If you reference a merge field and that field doesn’t have a value, it appears as a
blank value.

**4.** Save the action.

SEE ALSO:

[Chatter Settings](https://help.salesforce.com/s/articleView?id=sf.collab_enable.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Mention a User or Group in a “Post to Chatter” Process Action

When you post to a Chatter feed from a process, you can mention users if you can reference the
corresponding User ID field from the field picker.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

When you’re configuring the Post to Chatter action:

**1.** In the Message field, enter _`@[]`_ .

**2.** Place your cursor between the square brackets.

**3.** Click **Merge Field**, navigate to the user who you want to mention, select the corresponding
ID field, and click **Choose** .
The field reference appears between the square brackets.

```
  @[ {!fieldReference} ]

```

**4.** Save the action.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Example: To @mention a case’s account owner, navigate to the account’s fields and select **Owner ID** . Insert that field reference
between the square brackets in _`@[]`_, so that the result is:

```
@[{![Case].Account.OwnerId}]

```


Automate Your Business Processes with Salesforce Flow Process Builder

###### Use a Quick Action from a Process

details.

**•** If you selected Global actions or Type, for `Type` select the specific type of quick action that you want to use.

**•** If you selected Object, for `Object` search for and select the object that you want to filter by.

**3.** For `Action`, search for and select the action that you want to use.

**4.** Set field values for the action.

Rows that appear automatically represent the action’s required fields. To set values for the action’s optional fields, add rows.


Automate Your Business Processes with Salesforce Flow Process Builder

**5.** Save the action.

###### Work with Quip from a Process

Create documents, chat rooms, and folders when important events occur. Attach a document to
a record so your users have information in context. Update your spreadsheets with the latest
Salesforce data. Send a message to a chat room or document. Add new slides to a deck, copy
documents, add members to a document or chat, and more.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

Create a Document, Folder, or Chat Room from a Process
Use Process Builder to create documents, folders, and chat rooms.

Add a Document to a Folder from a Process
Add a document to one or more folders.

Remove a Document from a Process
Remove a document from a folder. Make a shared document private again.

Add a Live App to a Template from a Process
Keep your templates up to date with the latest Salesforce data. Add live Salesforce records and
list views to your templates using Process Builder.

Attach a Document to a Record from a Process
Keep information in context by attaching a document to a Salesforce record.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Copy a Document from a Process
To use a document as a template, create a copy. By default, copied documents are saved to the running user’s Private folder in Quip.

Add Members to a Document or Chat from a Process
Add up to 50 members to a document or chat.

Add Members with Different Access Levels to a Document from a Process
Automatically share a document with members with different permissions using Process Builder.

Remove Document Members from a Process
Trigger a process to auto-remove users from a document when the collaboration is over.

Copy Content from a Process (Retired)
Copy content from one slide deck to another.

Edit a Document from a Process
Add content to an existing document.

Update a Template Section from a Process
Edit a section of a template using text detection. Update sections of cloned documents at scale.

Copy Content with Live Paste from a Process
Copy content from a source document and paste it with Live Paste in a new document. After you update the source content, set
the content to automatically update in all documents that reference it.


Automate Your Business Processes with Salesforce Flow Process Builder

Update Content Based on a Document Range from a Process
Edit or add content to a defined template section, called a document range, when something changes in Salesforce.

Edit a Spreadsheet from a Process
Add data to an existing spreadsheet.

Edit a Slide from a Process (Retired)
Insert a new slide or change an image in an existing slide deck.

Lock Document Edits from a Process
Lock edits to mark a document as complete.

Lock Section Edits from a Process
To keep a document or template section safe from edits, lock it.

Export a Document to a PDF from a Process
To mark a document as complete or to keep a document view-only for record keeping, export it to a PDF. You can choose to attach
the PDF to a document or to a Salesforce record.

Send a Message from a Process
Send a message in a chat room or in a document. Messages sent in a document appear as inline comments or in the document
body.

Copy Comments from a Process
Copy comments from a template’s source document to the newly-created target document.

####### Create a Document, Folder, or Chat Room from a Process

Use Process Builder to create documents, folders, and chat rooms.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Create New Document**, **Create New Folder**, or
**Create Chat**, fill in the relevant fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Choose a document, folder, or chat name.

Names can be formatted as a string, field reference, global constant, or formula.

**3.** Enter the content that you want to add to your chat or document.

This step is optional for new documents.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

####### Add a Document to a Folder from a Process

Add a document to one or more folders.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Add Document to Folder**, fill in the relevant fields
to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document you want to add.

**3.** Enter the URL of the folder where you want to add your document.

Add your document to multiple folders by adding commas between each folder URL.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Remove a Document from a Process

Remove a document from a folder. Make a shared document private again.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Remove Document from Folder**, fill in the relevant fields
to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document you want to move.

**3.** Enter the URL of the folder your document is in.

To remove a document from multiple folders, separate folder URLs with commas.

Note: Removing a document from your Private folder removes your access to it.

**4.** Save the action.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Add a Live App to a Template from a Process

Keep your templates up to date with the latest Salesforce data. Add live Salesforce records and list
views to your templates using Process Builder.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Create New Document** or **Edit Document**, fill in the
relevant fields to add the action to your process.

**1.** From the Content Type dropdown, select **Quip Live App** .

**2.** To add a live Salesforce record, select **Salesforce Record** .

**a.** Enter the Salesforce Record ID.

Note: To add a dynamic Salesforce record that updates based on the record that
the document is embedded in, enter the value as a Reference. To add a specific record,
enter the numbers that appear in the record URL as a String.

**b.** These steps are optional and used as placeholders if the record can’t be found.

**c.** Optional: Enter the Salesforce record name.

**d.** Optional: Enter the record type.

**e.** Optional: Enter the name of the Salesforce org.

**3.** To add a live Salesforce list view, select **Salesforce List** .

**a.** Enter the Salesforce List View ID.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To add a dynamic Salesforce list view that updates based on the record that the document is embedded in, enter
the value as a Reference. To add a specific list view, enter the numbers that appear in the record URL as a String.

**b.** Enter the list view object type.

**c.** Optional: Enter the name of the Salesforce org.

**4.** Save the action.

Take note of these considerations to using Process Builder to add a Salesforce live app to your templates.

**•** You can’t select which record fields to display from Process Builder.

**•** The _owner_ of a live app added by Process Builder to a template is the first user to open the copied document. Only the live app _owner_
can save changes to Salesforce. Other users can edit and comment on the live app, but these changes don’t sync to Salesforce.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Attach a Document to a Record from a Process

Keep information in context by attaching a document to a Salesforce record.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Attach Document to Record**, fill in the relevant
fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** For **Document URL**, enter the URL of the document you want to attach to a record.

**3.** Select the record type that you want to attach a document to, and then click Choose.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Copy a Document from a Process

To use a document as a template, create a copy. By default, copied documents are saved to the
running user’s Private folder in Quip.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Copy Document**, fill in the relevant fields to add
the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** For Document URL, enter the URL of the document you want to copy.

By default, newly copied documents appear in the Private folder in Quip.

Note: Newly copied documents aren’t automatically attached to the record. See Step 5
for more info.

**3.** Use the Advanced section to enter a document title, add members by email address, or add
the document to a specific parent folder.

**4.** Save the action.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**5.** Optional: To attach the newly created document to the record and use Synced Sharing, use the Attach Document to Record action
after the Copy Document action.


Automate Your Business Processes with Salesforce Flow Process Builder

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

SEE ALSO:

[Automate Pricing Proposals with Flow Builder](https://help.salesforce.com/s/articleView?id=sf.quip_automate_pricing_proposal.htm&language=en_US)

[Automate Close Plans with Flow Builder](https://help.salesforce.com/s/articleView?id=sf.quip_template_lightning_flow.htm&language=en_US)

[Add Opportunity Team Members to a Close Plan](https://help.salesforce.com/s/articleView?id=sf.anywhere_add_users_to_doc_flow.htm&language=en_US)

####### Add Members to a Document or Chat from a Process

Add up to 50 members to a document or chat.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

####### After you’ve created a Quip action and selected Add Members to Document or Add Members

**to Chat**, fill in the relevant fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document or chat where you want to add members.

**3.** Enter up to 50 email addresses.

Emails must belong to Quip users in the same Quip site as the acting user.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Add Members with Different Access Levels to a Document from a Process

Automatically share a document with members with different permissions using Process Builder.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Add Members to Document** or **Add Members to Chat**,
fill in the relevant fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document or chat where you want to add members.

**3.** Enter the email addresses of the members you want to add based on the access level you want
to grant.


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

You can enter up to 50 email addresses per access level. Emails must belong to Quip members in the same Quip site as the acting
member.

**Quip Access Level** **Description**

**Full Access** Full-access members can view, comment on, edit, and share
documents that they’re added to.

**Edit Access** Edit-access members can view, comment on, and edit documents
that they’re added to.

**Comment Access** Comment-access members can view and comment on
documents that they’re added to.

**View Access** View-access members can view documents that they’re added
to.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Remove Document Members from a Process

Trigger a process to auto-remove users from a document when the collaboration is over.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Remove Members From Document**, fill in the relevant
fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document you want to manage access to.

**3.** Enter the email addresses of the members you want to remove from the document.

You can enter up to 50 email addresses. Emails must belong to Quip members in the same
Quip site as the acting member.

**4.** Save the action.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Copy Content from a Process (Retired)

Copy content from one slide deck to another.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

####### After you’ve created a Quip action and selected Copy Content, fill in the relevant fields to add the

action to your process.

Warning: Quip is retiring slides on January 31, 2021. After this date, the Copy Content action
in Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select **Slides** as your Document Type.

**3.** Enter the URL of the slide deck you want to copy.

**4.** Enter the slide number with the content you want to copy.

**5.** Enter the URL of the slide deck where you want to add content.

**6.** Enter the slide number where you want your copied content to appear.

**7.** Use the **Advanced** section to include anchor links instead of slide numbers.

**8.** Save the action.


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Edit a Document from a Process

Add content to an existing document.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Edit Document**, fill in the relevant fields to add
the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select **Document** as the Document Type.

**3.** Enter the URL of the document you want to edit.

**4.** Select the location in the document where you want to add content.

To add content after or before a section or to replace a section, enter the document section
anchor link.

**5.** Select the Content Type.

**6.** Enter the new content.

**7.** Optionally, select **Disable Extra Lines in Quip** to prevent Quip from automatically adding a
blank line after each paragraph.

**8.** Save the action.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Update a Template Section from a Process

Edit a section of a template using text detection. Update sections of cloned documents at scale.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Edit Document**, fill in the relevant fields to add the action
to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select **Document** as the Document Type.

**3.** Enter the URL of the document you want to edit.


EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

**4.** To edit a document based on a section, select **After Section**, **Before Section**, or **Replace Section** as the location for your new
content.

**5.** Use text detection to reference a document section by text. Under Section in Document, select **Text Detection** .

**6.** Enter the section text you want to reference using text detection.

**7.** Under Section Style, select whether the section text is a heading, paragraph, or list.

**8.** Select the content type.

**9.** Enter your new content.

**10.** Save your action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Copy Content with Live Paste from a Process

Copy content from a source document and paste it with Live Paste in a new document. After you
update the source content, set the content to automatically update in all documents that reference
it.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Copy with Live Paste**, fill in the relevant fields to add the
action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**2.** Enter the anchor links of the sections in the source document you want to copy with Live Paste.
To copy content from multiple sections of the same document, enter anchor links and separate
with commas. Your content appears in the order that the anchor links are entered. You can’t copy content from multiple documents
at the same time.


Automate Your Business Processes with Salesforce Flow Process Builder

**3.** Select the location in the document where you want to paste your content. Live pasted content can appear at the end or beginning
of a document, before or after a section, or can replace a document section.

**4.** To paste content at the beginning or end of a document, enter the target document URL. To paste content in a target document
based on a section, enter the anchor link of the section where you want your copied content to appear.

**5.** To have content copied with Live Paste automatically update in the target document, select **Update Automatically** .

**6.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Update Content Based on a Document Range from a Process

Edit or add content to a defined template section, called a document range, when something
changes in Salesforce.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Document ranges are supported only in documents and templates. To see your highlighted
document ranges, use a template.

After you create a Quip action and select **Edit Document** or **Copy with Live Paste**, fill in the
relevant fields to add the action to your process.

**1.** To add new content to a document based on a document range, select the Edit Document
action.

**a.** Under Location for New Content, select a document range placement. You can choose to
add content after a document range, before it, or you can replace it.


EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

**b.** Enter the document range heading. This is the heading text in your template that marks the start of a document range.

**c.** Enter your new content and save the action.

**2.** To live paste existing content to a template, select the Copy with Live Paste action.

**a.** Choose whether you want to copy content based on an anchor link or document range content type.

**b.** Enter the URL of the template or anchor link you want to copy content from.

**c.** To live paste content based on document range, select a document range placement. You can choose to paste your copied
content after a document range, before it, or you can replace it.

**d.** Enter the URL of the template where you want to paste your copied content.

**e.** Enter the document range heading of the target template that you want to use to place your copied content.

**f.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Edit a Spreadsheet from a Process

Add data to an existing spreadsheet.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Edit Document**, fill in the relevant fields to add
the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select **Spreadsheet** as the Document Type.

**3.** Enter the URL of the spreadsheet you want to edit.

**4.** Select the location in the spreadsheet where you want to add content.

**5.** To add content after a section, before a section, or to replace a section, enter the Section Anchor
Link.

**6.** Select **Row** or **Column** as the element type where you want to add content.

**7.** Enter the new content.

**8.** Save the action.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Edit a Slide from a Process (Retired)

Insert a new slide or change an image in an existing slide deck.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Edit Document**, fill in the relevant fields to add
the action to your process.

Warning: Quip is retiring slides on January 31, 2021. After this date, the Copy Content action
in Process Builder and Flow Builder no longer works, and Slides isn’t a valid document type
[for the Edit Document and Create Document actions. Tell Me More](https://help.salesforce.com/articleView?id=000355252&language=en_US&mode=1&type=1)

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select **Slides** as the Document Type.

**3.** Enter the URL of the slide deck you want to edit.

**4.** Select **Insert New Slide** or **Change Image In Slide** .

**5.** Select the location in the slide deck where you want to add content.

**6.** To add content before or after a section, enter the slide number.


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

**7.** Use the **Advanced** section to include anchor links instead of slide numbers.

**8.** To add text to a slide, select **Text Layout** and add your content.

**9.** To add an image, select **Image Layout** and enter the URL of the image you want to add.

**10.** Save the action.

####### Lock Document Edits from a Process

Lock edits to mark a document as complete.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

####### After you create a Quip action and select Lock Document Edits, fill in the relevant fields to add

the action to your process.

**1.** Enter a name for this action.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

This text appears on the canvas and helps you differentiate this action from others in your process. The name truncates to fit on the
canvas.

**2.** Enter the URL of the document you want to lock.

####### 3. To lock document edits, select Lock . To unlock document edits, select Unlock .

Note: Only users with full access to a document can lock or unlock edits.

**4.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Process Builder

####### Lock Section Edits from a Process

To keep a document or template section safe from edits, lock it.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Lock Document Section Edits**, fill in the relevant fields
to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the anchor link URL of the section you want to lock.

####### 3. To lock section edits, select Lock . To unlock section edits, select Unlock .

Note: Only users with full access to a document can lock or unlock section edits.

**4.** Save the action.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Export a Document to a PDF from a Process

To mark a document as complete or to keep a document view-only for record keeping, export it
to a PDF. You can choose to attach the PDF to a document or to a Salesforce record.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you create a Quip action and select **Export to PDF**, fill in the relevant fields to add the action
to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Optional. Enter the URL of the document you want to export to a PDF. To use a document
housed in a URL field, set Type to **Field Reference**, and select the object’s field.

**3.** Optional: To attach the PDF to a document, enter a target document URL. The PDF is added to
the end of the document.

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**4.** To attach the PDF to a Salesforce record, enter the record’s Salesforce Organization ID and the Target Record ID. PDFs attached to a
record are added to the record’s Files component and Notes and Attachments component, and are visible to any user with access
to the record.

**5.** Save the action.


Automate Your Business Processes with Salesforce Flow Process Builder

Note: To replace the existing Process Builder processes and Workflow Rules with flows before Process Builder and Workflow Rules
[reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

SEE ALSO:

[Automate Pricing Proposals with Flow Builder](https://help.salesforce.com/s/articleView?id=sf.quip_automate_pricing_proposal.htm&language=en_US)

####### Send a Message from a Process

Send a message in a chat room or in a document. Messages sent in a document appear as inline
comments or in the document body.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created a Quip action and selected **Send Message in Document** or **Send Message**
**in Chat**, fill in the relevant fields to add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Enter the URL of the document or chat where you want to send your message.

**3.** To send a message in a specific section of the document body, enter the Document Section
Anchor Link.

**4.** Enter the message you want to send.

**5.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)

####### Copy Comments from a Process

Copy comments from a template’s source document to the newly-created target document.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**1.** Create a Quip action in Process Builder and select **Copy Document** .

**2.** Under Advanced, select **Copy comments to new document** .

**3.** Save the action.

Note: To replace the existing Process Builder processes and Workflow Rules with flows before
[Process Builder and Workflow Rules reach end of support, see Quip Actions in Flow Builder.](https://help.salesforce.com/s/articleView?id=001096524&type=1&language=en_US)


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

EDITIONS

Available in: Lightning
Experience

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

###### Launch a Flow from a Process

Start an autolaunched flow from your process to automate complex business processes. Create
flows to perform logic and have events trigger the flows via processes without writing code.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

To launch a flow from a process, you must create and activate the flow. The flow must be
autolaunched.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** For Flow, search for and select the flow that you want to launch from this process.

Only active, autolaunched flows are available.

**3.** Optionally, click **Add Row** to set values for the flow’s variables.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**4.** Save the action.


Automate Your Business Processes with Salesforce Flow Process Builder

###### Send an Email from a Process

Easily send an email from a process by using an email alert. Email alerts are configured outside of
the Process Builder and contain the standard text, list of recipients, and template for an email.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Before you begin:

**•** Make sure that the email alert you want to call from your process exists. If not, create the email
alert on page 813.

**•** Understand the daily limits for emails sent from email alerts.

You can use only email alerts that are associated with the same object that the process is associated
with. The record that started the process is used as the starting point for any merge fields that are
used in the email alert.

After you’ve created an action and selected “Email Alerts” for the type, fill in the relevant fields to
add the action to your process.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** For `Email Alert`, type two or more letters to search for the email alert that you want to
use to send an email.

**3.** Save the action.

###### Send a Custom Notification from a Process

Send customized notifications when important events occur. Alert an account owner if a new
support case is logged while trying to close a deal, or send a notification for a workflow built entirely
with custom objects. Add recipients and content to your custom notification, then add it to your
process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Before you begin, make sure that the notification type you want to call from your process exists. If
[not, create a custom notification type.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_custom_type.htm&language=en_US)

After you’ve created an action and selected **Send Custom Notification** for the type, fill in the
relevant fields to add the action to your process.

**1.** Enter an easily recognizable name for this action. The name appears on the canvas and helps
you differentiate this action from others in your process. The name truncates to fit on the canvas.

**2.** Select a notification type.

**3.** Select a recipient category, and designate or find a recipient ID.

**•** Current User — The user who initiated the record change, platform event, or process that
triggered the process. This option is useful for confirmation notifications, such as a successful
submission of a form.


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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

**•** Find User — The user who receives the notification each time this action is executed.

**•** User Field from a Record — A user referenced via UserId on the record that initiated the process or on a related record.

**•** Find Group — All users in the group that receives the notification each time this action is executed.

**•** Find Queue — All users in the queue that receives the notification each time this action is executed.

**•** Account Field from a Record — All users on the account team for an account referenced via AccountId on the record that initiated
the process or on a related record. This option is available if you’ve enabled account teams for your org.

**•** Opportunity Field from a Record — All users on the opportunity team for an opportunity referenced via OpportunityId on the
record that initiated the process or a related record. This option is available if you’ve enabled team selling for your org.

**•** Owner Field from a Record — An owner or queue referenced via OwnerId on the record that initiated the process or a related
record. With this option, you can send a notification to all record owners, regardless of whether the owner is an individual owner
or a queue.

**4.** Write a helpful notification title and body using text and merge fields.

[Note: The content of custom push notifications depends on the Display full content push notifications setting. If full content](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)
push notifications aren’t enabled, only the notification title is sent.

**5.** Save the action.

###### Send a Survey Invitation from a Process

Send an email invitation containing the link to a particular survey question or to launch a survey.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you select **Send Survey Invitation** as the action, fill in the relevant fields.

**1.** Enter a name for this action.

This text appears on the canvas and helps you differentiate this action from others in your
process. The name truncates to fit on the canvas.

**2.** Select an active survey.

**3.** Select a question or the survey link.

Note: You can send email invitations for questions of the following types: Like or Dislike,
Net Promoter Score (NPS), Rating, and Score.

**4.** Select the email template used to send the invitation.

Important: The available templates depend on whether you choose to send a question
or the survey link.

**5.** Select the recipient type.

You can only send survey invitations to leads, contacts, and users in your org.

**6.** Select the recipient based on the object that's associated with the process.

**7.** Select your invitation settings.

**8.** Click **Save** .


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Developer**,
**Enterprise**, **Performance**,
and **Unlimited** Editions.

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

Example: If you want to send an invitation to a case's contact, select Case as the object for the process, Contact as the recipient
type, and Contact ID as the recipient.

SEE ALSO:

[Customize the Survey Invitation Email Templates](https://help.salesforce.com/s/articleView?id=sf.concept_send_email_template.htm&language=en_US)

###### Submit a Record for Approval from a Process

Submit the record that started the process for approval.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created an action and selected “Submit for Approval” for the type, fill in the relevant
fields to add the action to your process.

Only the record that started the process is submitted. You can’t submit any related records for
approval.

**1.** Enter a name for this action. This text appears on the canvas and helps you differentiate this
action from others in your process. The name truncates to fit on the canvas.

**2.** For `Approval Process`, indicate whether to submit the record through the default
approval process or through a specific approval process.

The process fails if:

**•** The record is submitted to the default approval process, and there are no active approval
processes for the record’s object type.

**•** The record is submitted to the default approval process, and it doesn’t meet the criteria for
any of the approval processes for the record’s object type.

**•** The record is submitted to a specific approval process, and it doesn’t meet the entry criteria.

**3.** To submit the record to a specific approval process:

**a.** Search for and select the approval process.

**b.** Indicate whether to skip the entry criteria for the approval process.

**4.** For `Submitter`, identify who receives notifications about the approval request.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

If the submitter isn’t an allowed initial submitter on the approval process that runs, the process fails. Make sure that the initial
submitters for the approval processes that are related to this object include all users who could trigger this process. For details about
setting the initial submitters for an approval process, see Create an Approval Process with the Standard Wizard on page 833.


Automate Your Business Processes with Salesforce Flow Process Builder

Any user with the "Modify All" permission to the object is allowed to submit a record for approval. They’re permitted to submit the
record, even if they aren’t listed as initial submitter.

**5.** If necessary, enter submission comments. Don’t reference merge fields or formula expressions.

Submission comments appear in the approval history for the specified record. This text also appears in the initial approval request
email if the template uses the `{!ApprovalRequest.Comments}` merge field.

**6.** Save the action.

###### Update Records from a Process

Update one or more records that are related to the record that started the process by manually
entering values or by using the values from related records.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created an action and selected “Update Records” for the action type, fill in the relevant
fields to add the action to your process. The records’ `Last Modified By` field is set to the
user who started the process by creating or editing a record.

**1.** Enter a name for this action. This text appears on the canvas and helps you differentiate this
action from others in your process. The name truncates to fit on the canvas.

**2.** For `Record Type`, select the record or records that you must update, and then click **Choose** .

You can update only the record that started the process or records that are related to it. For
example, you can reference _`[Case].ContactId`_, but not

_`[Case].Contact.AccountId`_ .

**•** To update the record that started the process, click the appropriate radio button. For
example, if your process is based on a case record, click next to **Select the Case record**
**that started your process** .

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**•** To update a record that’s related to the record that started the process, click the appropriate radio button and select one of the
field names in the dropdown list.


Automate Your Business Processes with Salesforce Flow Process Builder

If you select a field that ends in “ID,” you’re selecting a single record. This field name corresponds to a lookup field on the original
[record. For details on lookup fields, see Custom Field Types.](https://help.salesforce.com/s/articleView?id=sf.custom_field_types.htm&language=en_US)

For example, if a case record started the process and you select `Account Id`, this action updates the account that’s associated
with the case.

If you select a plural item that doesn’t end in “ID,” you’re updating all the records of that object type that are related to the record
that started the process. This plural item corresponds to child records of the original record, which can appear in a related list
on the original record.

For example, if you select CaseComments, this action updates all the case comments that are related to the case.

**•** To update fields on a related record, click a field with next to it (ending in “ID”) to access that record’s fields.

For example, let’s say that, for a process that evaluates a case record (1), you want to update all contacts that are related to the

case’s parent account. Click **Account ID** (2), then **Contacts** (3), and then **Choose** .


Automate Your Business Processes with Salesforce Flow Process Builder

**3.** Optionally, specify conditions to filter the records you’re updating. For example, if your process updates the status of a parent case,
specify conditions so that you don’t update the parent case if its status is set to On Hold.

When you define conditions for updating records, you can’t:

**•** Reference a Long Text Area field

**•** Reference a Rich Text field

**•** Reference a child record’s related fields.

For example, you can reference _`[Case].ContactId`_, but not _`[Case].Contact.AccountId`_ .

When you define multiple filters, the filter logic usually defaults to `AND` . However, if multiple filters have the same field selected
and use the equals operator, the filters are combined with `OR` . For example, your filters check whether a case’s Type equals
Problem (1), Type equals Feature Request (2), and Escalated equals `true` (3). At run time, the filters are combined to `(1 OR`
`2) AND 3` .

If you’re updating the record that started the process, Process Builder adds an implicit filter for you in the background:

`[` _**`Object`**_ `].Id equals myCurrentVariable.Id` . If you add filter criteria that set the record’s ID to a value using
the equals operator, at runtime the `[` _**`Object`**_ `].Id equals` filters are combined using `OR` filter logic. For example, you
update the case that started the process and add this filter: `[Case].Id equals 500D00000044XgV` . At runtime, your
filter is combined with the implicit filter ( `[Case].Id equals myCurrentVariable.Id` ) with `OR` .

**a.** Select **Updated records meet all conditions** .

**b.** Set the conditions that you want to use to filter the updated records.

`Field` Select the field whose value you want to evaluate.

`Operator` The available operators depend on the field’s data type.

`Type` The available value types depend on the field’ data type. See Process Builder Value Types on page 928 for details.

`Value` Identify the value that you want to evaluate the field for.

For example, if your process updates account records, you can choose to update only accounts with an annual revenue (1)
greater than (2) $1,000,000 (3).


Automate Your Business Processes with Salesforce Flow Process Builder

**4.** Specify the new field values.

```
Field

```

Select the field whose value you want to set. To filter the dropdown list, type the name of the field.

You can assign values to fields only on the record or records that you identified in the `Object` field. Use a separate
Update Records action to update fields on related records.

`Type` Select the type of value that you want to use. The available types depend on the field that you’ve selected.

`Value` Set a value for the field. For example, if you select a Formula value type, click **Build a formula...** to create a formula
value for the field.

**5.** Save the action.

###### Call Apex Code from a Process

Add customized functionality to your process by calling Apex from the process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you’ve created an action and selected “Apex” for the type, fill in the relevant fields to add the
action to your process.

Important: To use this action in a process, ask your developer to annotate the appropriate
method with `@InvocableMethod` . For details, see “ `InvocableMethod` Annotation”
in the _Apex Developer Guide_ .

The Apex class and the process are executed by the user whose action triggered the process.

**1.** Enter a name for this action. This text appears on the canvas and helps you differentiate this
action from others in your process. The name truncates to fit on the canvas.

**2.** Choose an Apex class by entering the name of the class to filter results or select a class from
the dropdown list.

**3.** If the class includes an invocable variable, you can manually enter values or reference field
values from a related record.

The value must match the variable’s data type. You can set values for sObject and primitive
type list variables only.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**•** To set values for sObject variables and sObject list values, reference an object’s related records, for example, all child contact
records associated with the Account object that started the process.


Automate Your Business Processes with Salesforce Flow Process Builder

**•** To set a value for a primitive list variable (String, Integer, Time, and so on), select the String value type and enter a value in the
text input field. You can’t pass multiple values to lists.

**4.** Click **Save** .

Note: If you define an Apex action in your process and then modify the Apex class by adding a standard field reference (for
example, _`User.Phone`_ ), the Apex action is no longer visible in the process and must be added again.

##### Execute Actions for Multiple Criteria

Choose whether to stop or continue your process after specific criteria are met and associated
actions execute.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

For each criteria node and associated action group, choose whether to stop the process after
executing the actions or to continue the process and evaluate the next criteria node.

Important: When a process continues to the next criteria node, it evaluates the values that
the record had at the beginning of the process. For example:

**1.** The status of a case is New.

**2.** The case is edited.

**3.** The process evaluates Criteria 1. The conditions are met, so the process updates the case’s
status to Escalated.

**4.** The process evaluates Criteria 2 using the record values from step 2.

If you want a process to react to changes that occur in the process, select the advanced option
in the object node.

**1.** Make sure you’ve defined the next criteria and that your action group includes only immediate
actions. You can’t evaluate the next criteria when an action group contains scheduled actions.

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

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

**2.** To change what happens after actions execute, click **STOP** (1) or **EVALUATE THE NEXT CRITERIA** (2). Initially, each action group
is set to stop after executing actions.


Automate Your Business Processes with Salesforce Flow Process Builder

**3.** Save your changes, and your choice appears on the canvas.

SEE ALSO:

Reevaluate Records in the Process Builder

#### Process Management

Process Builder allows you to see and manage all your processes in one place.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

#### To manage a process, from Setup, enter Builder in the Quick Find box, then select Process

**Builder** .

From the process management page, you can:

**•** Create a process

**•** Edit a process

**•** Delete an inactive process

**•** See the status of your existing processes

**•** Sort your processes by name, description, object, last modified date, or status

When you open a process, you can:

**•** Clone the process

**•** Activate or deactivate the process

**•** Edit the process properties


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

To manage processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

From the list of paused flow interviews in Setup, you can:

**•** Monitor scheduled actions that haven’t yet been executed

**•** Delete groups of scheduled actions that you no longer must wait for

##### Process Status

Each process has a status that determines whether the process can be edited, activated, or deleted.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**Status** **Description** **Editable?**

Active

The process has been activated. No

You can’t edit an active process. However, you can clone it. Make
any necessary changes to the cloned process and then activate it.
Don't forget to deactivate the original process if appropriate.

Inactive The process is inactive and can be activated. Yes

##### Clone a Process

If you want to change an existing process, save a clone of that process. You can save the clone as
either a new inactive process with its own version history, or as a new inactive version of the existing
process.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

To change an active process, you have a few options.

**•** Deactivate it, make changes, and then reactivate it.

**•** Clone it as an inactive version, make changes, and then activate the new version. The original
version is automatically deactivated.

**•** Clone it as a new inactive process, make changes and then activate it. The original process isn’t
automatically deactivated, so consider whether it’s appropriate for both processes to be active.

You can create up to 50 versions of a process, but only one version of a given process can be active.

**1.** From Setup, enter _`Builder`_ in the `Quick Find` box, then select **Process Builder** .

**2.** Open the process or process version that you want to activate.

##### 3. Click Clone .

**4.** You can create a version of the current process or a new process with its own version history.

**5.** Enter a name, API name, and description.

**6.** Click **Save** .


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

USER PERMISSIONS

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

##### Activate a Process

Salesforce doesn't start using a new or revised process to evaluate records until you activate it.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

After you activate a process, you can no longer edit it. However, you can click **Clone** to save the
process as a new inactive process.

You can't activate a process unless it has:

**•** At least one defined criteria node

**•** At least one defined immediate or scheduled action

**1.** From Setup, enter _`Builder`_ in the `Quick Find` box, then select **Process Builder** .

**2.** Open the process version that you want to activate.

##### 3. Click Activate .

If you activate a version of a process that already has an active version, the previously active
version is automatically deactivated. To see that version later, refer to the process's version
history.

After you've activated your process, consider creating or editing test records that will start the
process to make sure it's working correctly. If you do, remember to delete those test records or
return them to their previous values after you've confirmed that your process works as designed.

If you later want Salesforce to stop using a process to evaluate records as they're created or edited,
open the active process and click **Deactivate** .

##### Delete a Process Version

If you no longer require a process version that you’ve defined, delete it.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

To delete an active process, you must first deactivate it. You can’t delete process versions with an
Active status. If another process references your invocable process, you can’t delete the invocable
process. If a process has any scheduled actions, it can’t be deleted until those pending actions have
been executed or deleted.

**1.** In Setup, enter _`Builder`_ in the Quick Find box, then select **Process Builder** .

**2.** Next to the appropriate process, click to view all versions.

##### 3. For the version that you want to delete, click Delete .

If your process has only one version and you delete that version, the entire process is deleted.

**4.** Click **OK** .


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

To activate or deactivate
processes:

**•** Manage Flow

AND

View All Data

AND

Customize Application

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

To delete processes:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Process Builder

##### Monitor Your Processes’ Pending Scheduled Actions

You can check which of your processes are waiting to execute scheduled actions.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**1.** From Setup, enter _`Flow`_ in the Quick Find box, then select **Paused And Failed Flow**
**Interviews**

Note: If Paused Flow Interviews isn’t available as its own page, select **Flows** and scroll
down to the list of paused interviews.

**2.** To see scheduled actions in the list of paused interviews, create a view.

Note: We recommend displaying these fields.

**•** `Flow API Name` or `Flow Name` —Contains the process name.

**•** `Paused Date` —When the schedule started for the action group.

**•** `Current Element` —Identifies the group of scheduled actions that the process
is waiting to execute.

The format of a `Current Element` value is `myWait_myRule_` _`N`_, where _`N`_
is the number of the associated criteria and action group. For example,
`myWait_myRule_2` indicates that the scheduled action is associated with the
second criteria node in the process.

**•** `Type` —Processes that are waiting to execute scheduled actions are of type Record
Change Process.

SEE ALSO:

Delete Unexecuted Scheduled Actions


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

To see unexecuted
scheduled actions:

**•** View Setup and
Configuration

Automate Your Business Processes with Salesforce Flow Process Builder

##### Delete Unexecuted Scheduled Actions

If you no longer want to execute a process's scheduled actions, you can delete them from the list
of paused flow interviews in Setup.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**1.** From Setup, enter _`Flow`_ in the Quick Find box, then select **Paused Flow Interviews** .

If Paused Flow Interviews isn’t available as its own page, select **Flows** and scroll down to the
list of paused interviews.

**2.** In the Flow API Name or Flow Name column, find the process whose scheduled actions you
want to delete.

##### 3. For each unexecuted group of scheduled actions that you want to delete, click Del, or click and select Delete .

SEE ALSO:

Monitor Your Processes’ Pending Scheduled Actions

#### Troubleshoot Processes

Use the error messages that appear in the Process Builder and the emails you receive when a process
fails to help solve problems that arise when you’re working with processes. When all else fails, look
at the Apex debug logs for your processes.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Common Reasons Why Processes Fail
Here are some common design problems that cause processes to fail.

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

To delete unexecuted
scheduled actions:

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

Errors in the Process Builder
The API names for criteria nodes and actions are created in the background. When you create
or update processes, you can see error messages that reference those names to help you identify specifically where the problem
occurred.

What Happens When a Process Fails?
When a user does something that triggers a process, such as create a record, and the process fails, the user gets an error message.
The error message includes the process name, error ID, and sometimes technical information that the user can give to you, the
Salesforce admin. You can use the error ID to locate the detailed error email that is sent when the process failed.

#### Troubleshoot Processes with Apex Debug Logs

Use debug logs to find detailed information about your running processes after they finish running. For example, investigate why
a process doesn’t to trigger when a record meets the process’s criteria, or explore the sequence of processes being executed.


Automate Your Business Processes with Salesforce Flow Process Builder

Send Alerts When a Screen Flow Fails
To save time troubleshooting screen flows that fail, subscribe to the Flow Execution Error Event platform event. When a flow interview
fails, Salesforce publishes a platform event message. In Process Builder, you can subscribe to the platform event and perform actions,
such as posting to Chatter or sending custom notifications.

SEE ALSO:

##### Common Reasons Why Processes Fail Common Reasons Why Processes Fail

Here are some common design problems that cause processes to fail.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**•** A user creates or edits a person account. An Account-based process evaluates the record. The
process’s criteria node references an account field, for example, _`[Account].Name Equals`_
_`Acme`_ .

**•** The process references a field that hasn’t been set. For example, you reference

_`[Contact].Account.Description`_ in your process. If the Account lookup field isn’t
set on the contact, the process fails because it doesn’t know which account to reference.

The workarounds for this issue depend on where the reference exists in the process.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**–** If you reference it in filter conditions, add another filter condition that checks whether the lookup field is set. You can do the
same workaround if it’s referenced in a formula, for example, _`[Contact].AccountId Is null False`_ .

**–** Otherwise, consider making the fields required.

SEE ALSO:

Troubleshoot Processes

##### Errors in the Process Builder

What Happens When a Process Fails?

##### Errors in the Process Builder

The API names for criteria nodes and actions are created in the background. When you create or
update processes, you can see error messages that reference those names to help you identify
specifically where the problem occurred.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

**API Name** **Description**

```
myVariable_current. field

myVariable_old. field

```

Example:

_`field`_ is the name of the field that’s referenced. `myVariable_current` refers
to the field values that the record had when it started the process.

For example, `myVariable_current.Id` corresponds to the record’s field
value for `Id` when the record started the process.

_`field`_ is the name of the field that’s referenced. `myVariable_old` refers to
the most recent previous values of the record that started the process.

For example, `myVariable_old.Id` corresponds to the record’s field value for
`Id` immediately before the record started the process.

```
   The element has an invalid reference to “myVariable_current.AnnualRevenue”.

```

`myVariable_current.AnnualRevenue` refers to the value for the field `AnnualRevenue` when the record started
the process.

Note: Error or warning messages can refer to a “flow” instead of a “process”. Those messages still apply to your process.

SEE ALSO:

Common Reasons Why Processes Fail

##### What Happens When a Process Fails?

When a user does something that triggers a process, such as create a record, and the process fails,
the user gets an error message. The error message includes the process name, error ID, and
sometimes technical information that the user can give to you, the Salesforce admin. You can use
the error ID to locate the detailed error email that is sent when the process failed.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

The email includes the element that failed, the error message from that failure, and details about
the criteria and actions that the process tried to execute. The subject line is `Error Occurred`
`During Flow “` _`Process_Name`_ `”:` _`Error`_ .

Example:

```
   Error Occurred During Flow "Opportunity_Management": No

   applicable approval process was found.

   // The error occurred when the LeadConvertEmail process was

   triggered.

   An error occurred at element myRule_1_A1 (FlowActionCall).

   No applicable approval process was found.

   // The error occurred at the first action (A1) that’s

   associated with the

```


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Process Builder

```
      // first criteria node (myRule_1).

      Flow Details

      Flow Name: Opportunity_Management

      Type: Workflow

      Version: 3

      Status: Active

      Org: Acme (00DR00000000o82)

      // The user triggered version 3 of the Opportunity_Management process.

      Flow Interview Details

      Interview Label: Opportunity_Management-3_Opportunity

      Current User: Madison Rigsby (0051a000000qJXL)

      Start time: 2/2/2017 11:21 AM

      Duration: 0 seconds

      // The process was triggered by user Madison Rigsby.

      How the Interview Started

      Madison Rigsby (0051a000000qJXL) started the flow interview.

      Some of this flow's variables were set when the interview started.

      myVariable_old = 0061a00000D3ibfAAB

      myVariable_current = 0061a00000D3ibfAAB

      ASSIGNMENT: myVariable_waitStartTimeAssignment

      {!myVariable_waitStartTimeVariable} Equals {!Flow.CurrentDateTime}

      Result

      {!myVariable_waitStartTimeVariable} = "2/2/2017 11:21 AM"

      DECISION: myDecision

      Executed this outcome: myRule_1

      Outcome conditions: and

      1. {!myVariable_current.StageName} (Proposal/Price Quote) Equals Proposal/Price Quote

      Logic: All conditions must be true (AND)

      // The first criteria node (myRule_1) checks whether the opportunity’s StageName

      // is “Proposal/Price Quote”. It is, so the process moves on to execute the associated

      // actions.

      SUBMIT FOR APPROVAL : myRule_1_A1

      Inputs:

      objectId = {!myVariable_current.Id} (0061a00000D3ibfAAB)

      comment = null

      Error Occurred: No applicable approval process was found.

      // The process tries to execute the first associated action.

      // The action fails because no approval processes exist that

      // the record can be submitted to. Maybe the org doesn’t include

      // any active Opportunity approval processes. Or maybe it does, but the

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
      // record doesn’t meet the entry criteria for any of them.

      Salesforce Error ID: 593281227-1030 (-1996259564)

```

SEE ALSO:

Select Flow and Process Error Email Recipients

Common Reasons Why Processes Fail

Send Alerts When a Screen Flow Fails

##### Troubleshoot Processes with Apex Debug Logs

Use debug logs to find detailed information about your running processes after they finish running.
For example, investigate why a process doesn’t to trigger when a record meets the process’s criteria,
or explore the sequence of processes being executed.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

Tip: Make sure that your filters include FINER events in the WORKFLOW category. For details,
[see Debug Log Levels.](https://help.salesforce.com/s/articleView?id=sf.code_setting_debug_log_levels.htm&language=en_US)

When using debug logs to troubleshoot a process, consider the following.

**•** Processes created in the Process Builder appear as flows and workflow rules in debug logs. The
generated names have some resemblance to the process names, but they don’t map one-to-one.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Record change processes appear as flows of type Workflow. Invocable processes appear as flows of type InvocableProcess. Event
processes appear as flows of type CustomEvent.

**•** Immediate actions that are executed in a block are strung together in the flow. If one action fails in the middle, then the following
actions aren’t executed.

**•** Scheduled actions are executed after a `FLOW_WAIT` element. The actions are executed similarly to immediate actions after the
process resumes.

**•** `WF_CRITERIA_BEGIN` and `WF_CRITERIA_END` refer to the workflow rule criteria that are always set to true and not the
criteria defined in your process.

**•** Here’s how elements in the Process Builder correspond to flow debug events.


Automate Your Business Processes with Salesforce Flow Process Builder

Example: **Debugging Immediate Actions**

This example covers a process with an immediate Post to Chatter action.

Here’s what you can tell from this first snippet.

**•** A lead named “Madison Rigby” triggers the process.

**•** The name of the process is `Hello_World` . The number appended to the name is the process version’s ID:
`301R000000009n0` .

**•** The process is set to trigger when a record is created ( `ON_CREATE_ONLY` ).

```
      10:11:26.594 (595241802)|EXECUTION_STARTED

      10:11:26.594 (595255829)|CODE_UNIT_STARTED|[EXTERNAL]| Workflow:Lead

      10:11:26.594 (685753138)|WF_RULE_EVAL_BEGIN|Workflow

      10:11:26.594 (686312384)|WF_CRITERIA_BEGIN|

        [Lead: Ms. Madison Rigsby 00QR0000001HqC4]|Hello_World301R000000009n0|

        01QR00000000Nz8| ON_CREATE_ONLY |0

```

In this snippet, the process compares the record’s current values to the values it had before it was changed.
`myVariable_current` contains all the record’s current field values. `myVariable_old` contains all the field values of
the record immediately before it was changed. In this example, `myVariable_old` has no values (null), because the process is
evaluating a newly created lead.

```
      10:11:26.594 (688919502)|WF_FORMULA|

        Formula:ENCODED:[treatNullAsNull]true|Values:

      10:11:26.594 (689128428)|WF_CRITERIA_END|

        true

      10:11:26.594 (695758445)|WF_SPOOL_ACTION_BEGIN|

        Workflow

      10:11:26.594 (714823342)|WF_ACTION|

        Flow Trigger: 1;

      10:11:26.594 (714900811)|WF_RULE_EVAL_END

      10:11:26.594 (719777561)|WF_FLOW_ACTION_BEGIN|

        09LR000000005Td10:11:26.594 (720281142)|WF_FLOW_ACTION_DETAIL|

        09LR000000005Td|[Lead: Ms. Madison Rigsby 00QR0000001HqC4]|Id=09LR000000005Td|

        CurrentRule:Hello_World301R000000009n0 (Id=01QR00000000Nz8)

      10:11:26.722 (722465931)|FLOW_CREATE_INTERVIEW_BEGIN|

        00DR00000000o82|300R00000004PQB|301R000000009n0

      10:11:26.722 (740702983)|FLOW_CREATE_INTERVIEW_END|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|Hello World

      10:11:26.594 (748183550)|WF_FLOW_ACTION_DETAIL|

        Param Name: myVariable_current,

        Param Value: ENCODED:{![treatNullAsNull]{!ID:this}},

        Evaluated Param Value: {Entity type: Lead, id: 00QR0000001HqC4MAK}|

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
        Param Name: myVariable_old,

        Param Value: {!old},

        Evaluated Param Value: null

```

When the process started:

**•** This instance of the process starts with the `FLOW_START_INTERVIEW_BEGIN` event.

**•** Each `FLOW_START_INTERVIEW_LIMIT_USAGE` event displays the usage of a given limit when the process started.
In this example, the transaction hasn't done anything that counts toward a limit.

**•** A handful of variables are set. The process uses these variables to perform logic later.

**–** `myVariable_old` is set to nothing because the record didn't exist before this transaction.

**–** `myVariable_current` is set to the current values of the lead record.

**–** `myVariable_waitStartTimeVariable` is set to the current time.

```
      10:11:26.750 (750700361)|FLOW_START_INTERVIEWS_BEGIN|1

      10:11:26.750 (751285739)| FLOW_START_INTERVIEW_BEGIN |

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        Hello World

      10:11:26.750 (751341782)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        SOQL queries: 0 out of 100

      10:11:26.750 (751367432)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        SOQL query rows: 0 out of 50000

      10:11:26.750 (751384035)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        SOSL queries: 0 out of 20

      10:11:26.750 (751397896)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        DML statements: 0 out of 150

      10:11:26.750 (751412225)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        DML rows: 0 out of 10000

      10:11:26.750 (751427529)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        CPU time in ms: 0 out of 15000

      10:11:26.750 (751472968)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Heap size in bytes: 0 out of 6000000

      10:11:26.750 (751490226)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Callouts: 0 out of 100

      10:11:26.750 (751505266)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Email invocations: 0 out of 10

      10:11:26.750 (751519128)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Future calls: 0 out of 50

      10:11:26.750 (751533892)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Jobs in queue: 0 out of 50

      10:11:26.750 (751547542)| FLOW_START_INTERVIEW_LIMIT_USAGE|

        Push notifications: 0 out of 10

      10:11:26.750 (752380627)|FLOW_VALUE_ASSIGNMENT|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        myVariable_old |

      10:11:26.750 (754872639)|FLOW_VALUE_ASSIGNMENT|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        myVariable_current |

        {LastModifiedDate=2018-02-28 18:11:26, Company=Acme Wireless, Email=null,

        HasOptedOutOfFax=false, Latitude=null, MobilePhone=null, Industry=Apparel,

        CreatedById=005R0000000J01RIAS, Street=null, PhotoUrl=null,

        ConvertedOpportunityId=null, MasterRecordId=null,

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
        LastModifiedByID=005R0000000J01RIAS, Status=Contacted, IsDeleted=false,

        ConvertedAccountId=null, IsConverted=false, HasOptedOutOfEmail=false,

        LastViewedDate=null, City=null, Longitude=null, LeadSource=External Referral,

        CreatedByID=005R0000000J01RIAS, GeocodeAccuracy=null, State=null,

        CreatedDate=2018-02-28 18:11:26, Country=null, Id=00QR0000001HqC4MAK,

        LastName=Rigsby, AnnualRevenue=500000.0, Jigsaw=null, EmailBouncedDate=null,

        Description=null, ConvertedDate=null, DoNotCall=false, Rating=null,

        PostalCode=null, Website=null, LastReferencedDate=null, NumberOfEmployees=5,

        Salutation=Ms., ConvertedContactId=null, OwnerId=005R0000000J01RIAS,

        Phone=null, EmailBouncedReason=null, FirstName=Madison, IsUnreadByOwner=true,

        Title=null, SystemModstamp=2018-02-28 18:11:26, LastActivityDate=null,

        Fax=null, LastModifiedById=005R0000000J01RIAS,

        LastTransferDate=2018-02-28 18:11:26, JigsawContactId=null}

      10:11:26.750 (755116990)|FLOW_ELEMENT_BEGIN|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        FlowAssignment|myVariable_waitStartTimeAssignment

      10:11:26.750 (755457410)|FLOW_ASSIGNMENT_DETAIL|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        myVariable_waitStartTimeVariable|ASSIGN|2/28/2018, 10:11 AM

      10:11:26.750 (756105710)|FLOW_VALUE_ASSIGNMENT|

      2416dcc6212273331b3d50a38a161dd464e3e-7fdd| myVariable_waitStartTimeVariable |2018-02-28T18:11:27Z

      10:11:26.750 (756182849)|FLOW_ELEMENT_END|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        FlowAssignment|myVariable_waitStartTimeAssignment

```

The process evaluates the first criteria.

In debug logs, a `FLOW_RULE_DETAIL` event represents a process criteria node. `myRule_1` corresponds to the first criteria
node in the process. Because the result of `myRule_1` is true, the process executes the actions associated with the first criteria.

```
      10:11:26.750 (757306870)|FLOW_ELEMENT_BEGIN|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        FlowDecision|myDecision

      10:11:26.750 (757582110)| FLOW_RULE_DETAIL |

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        myRule_1|true

      10:11:26.750 (757616076)|FLOW_VALUE_ASSIGNMENT|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        myRule_1|true

      10:11:26.750 (757683580)|FLOW_ELEMENT_END|

        2416dcc6212273331b3d50a38a161dd464e3e-7fdd|

        FlowDecision|myDecision

```

In this snippet, the immediate actions for the first criteria are executed. In the name `myRule_1_A1`, “A1” indicates that this
element corresponds to the first action in the action group, which creates a task. The `FLOW_BULK_ELEMENT_LIMIT_USAGE`
events indicate that the action increased the transaction's usage count toward two limits: the number of DML statements issued
and the number DML rows processed.

```
      10:11:26.750 (1898050716)|FLOW_ELEMENT_BEGIN|

        68211d9d9f918ee32db47d21247161de215ce5-7d38|

        FlowRecordCreate| myRule_1_A1

      10:11:26.750 (1898121764)|FLOW_ELEMENT_DEFERRED|

        FlowRecordCreate|myRule_1_A1

      10:11:26.750 (1898261705)|FLOW_ELEMENT_END|

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
        68211d9d9f918ee32db47d21247161de215ce5-7d38|

        FlowRecordCreate|myRule_1_A1

      10:11:26.750 (1345712687)|FLOW_START_INTERVIEW_END|

        68211d9d9f918ee32db47d21247161de215ce5-7d38|Hello World

      10:11:26.750 (1898350543)|FLOW_BULK_ELEMENT_BEGIN|

        FlowRecordCreate|myRule_1_A1

      10:11:26.750 (1928183118)|FLOW_BULK_ELEMENT_DETAIL|

        FlowRecordCreate|myRule_1_A1|1

      10:11:26.750 (2267557291)|FLOW_VALUE_ASSIGNMENT|

        68211d9d9f918ee32db47d21247161de215ce5-7d38|

        myRule_1_A1|true

      10:11:26.750 (2267878414)| FLOW_BULK_ELEMENT_LIMIT_USAGE|

        1 DML statements, total 1 out of 150

      10:11:26.750 (2267929106)| FLOW_BULK_ELEMENT_LIMIT_USAGE|

        1 DML rows, total 1 out of 10000

      10:11:26.750 (2268002776)|FLOW_BULK_ELEMENT_END|

        FlowRecordCreate|myRule_1_A1|1|370

```

Then the process finishes.

```
      10:11:27.977 (1978733709)|FLOW_START_INTERVIEWS_END|1

      10:11:27.989 (1989764561)|WF_FLOW_ACTION_END|09LR000000005Td

      10:11:27.989 (1998560773)|WF_ACTIONS_END| Flow Trigger: 1;

      10:11:27.989 (1998600044)|CODE_UNIT_FINISHED|Workflow:Lead

      10:11:27.989 (2000437095)|EXECUTION_FINISHED

```

Example: Debugging Scheduled Actions

Scheduled actions are logged separately from immediate actions. After the scheduled time occurs, an automated process executes
the scheduled actions. However, the actions are still executed as the user who originally caused the process to run. The log uses
coordinated universal time (UTC) instead of the user’s time zone.

This example walks you through a debug log for a process with a scheduled Create a Record action.

Any events that start with `FLOW_WAIT_` provide information about a process schedule. `myWait_myRule_` _**`int`**_ always
indicates a schedule, where _`int`_ identifies which criteria node the schedule is associated with.

In this snippet:

**•** The schedules that are associated with the first criteria node ( `myWait_myRule_1` ) are evaluated.

**•** The defined time for the first schedule has passed ( `myWaitEvent_myWait_myRule_1_event_0` ).

**•** `FLOW_WAIT_RESUMING_DETAIL` indicates that the interview is resumed so that the process can execute its scheduled
actions.

**•** The `myVariable_current` variable is updated with the latest values from the record that started the process originally.

```
      10:21:35.461 (1461109547)|FLOW_BULK_ELEMENT_BEGIN|

        WaitInfo| myWait_myRule_1

      10:21:35.461 (1467206801)|FLOW_WAIT_EVENT_RESUMING_DETAIL|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWait_myRule_1| myWaitEvent_myWait_myRule_1_event_0 |DateRefAlarmEvent

      10:21:35.461 (1467428864)| FLOW_WAIT_RESUMING_DETAIL |

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWait_myRule_1|0FoRM0000004C9I

      10:21:35.461 (1503485017)|FLOW_VALUE_ASSIGNMENT|

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWaitEvent_myWait_myRule_1_event_0|true

      10:21:35.461 (1509382975)|FLOW_VALUE_ASSIGNMENT|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myVariable_current|{Id=00QRM000003abIU2AY, IsDeleted=false,

        MasterRecordId=null, Salutation=null, FirstName=Another, LastName=Lead,

        Title=null, Company=Acme, Street=null, City=null, State=null, PostalCode=null,

        Country=null, Latitude=null, Longitude=null, GeocodeAccuracy=null, Phone=null,

        MobilePhone=null, Fax=null, Email=null, Website=null, PhotoUrl=null,

        Description=null, LeadSource=Advertisement, Status=New, Industry=null,

        Rating=null, AnnualRevenue=null, NumberOfEmployees=null, InternalSource=null,

        OwnerId=005RM000001cEmFYAU, HasOptedOutOfEmail=false, IsConverted=false,

        ConvertedDate=null, ConvertedAccountId=null, ConvertedContactId=null,

        ConvertedOpportunityId=null, IsUnreadByOwner=false,

        CreatedDate=2018-03-01 18:12:05, CreatedById=005RM000001cEmFYAU,

        LastModifiedDate=2018-03-01 18:12:05, LastModifiedById=005RM000001cEmFYAU,

        SystemModstamp=2018-03-01 18:12:05, LastActivityDate=null, DoNotCall=false,

        CreatedByID=005RM000001cEmFYAU, LastModifiedByID=005RM000001cEmFYAU,

        CampaignId=null, CampaignMemberStatus=null, HasOptedOutOfFax=false,

        LastViewedDate=null, LastReferencedDate=null,

        LastTransferDate=2018-03-01 18:12:05, Jigsaw=null, JigsawContactId=null,

        ConnectionReceivedDate=null, ConnectionSentDate=null, EmailBouncedReason=null,

        EmailBouncedDate=null}

      10:21:35.461 (1512457819)|FLOW_BULK_ELEMENT_END|

        WaitInfo|myWait_myRule_1|0|47

```

In this snippet, the process makes sure that the record's date field isn't null. Specifically, it checks the date field that's referenced
in the schedule.

```
      10:21:35.461 (1514489368)|FLOW_ELEMENT_BEGIN|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowDecision|myPostWaitDecision_myWaitEvent_myWait_myRule_1_event_0

      10:21:35.461 (1528928534)|FLOW_RULE_DETAIL|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myPostWaitRule_myWaitEvent_myWait_myRule_1_event_0|true

      10:21:35.461 (1529027007)|FLOW_VALUE_ASSIGNMENT|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myPostWaitRule_myWaitEvent_myWait_myRule_1_event_0|true

      10:21:35.461 (1529230456)|FLOW_ELEMENT_END|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowDecision|myPostWaitDecision_myWaitEvent_myWait_myRule_1_event_0

```

Now to execute the actions associated with the schedule. First up is `..._myRule_1_event_0_SA1` .

**•** `myRule_1` corresponds to the first criteria node

**•** `event_0` corresponds to the first schedule associated with the criteria

**•** `SA1` corresponds to the first action in the schedule.

The action creates a record. With the `FLOW_BULK_ELEMENT_LIMIT_USAGE` events, we see that action increased the
transaction's usage count toward two limits: the number of DML statements issued and the number DML rows processed.

```
      10:21:35.461 (1529433132)|FLOW_ELEMENT_BEGIN|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowRecordCreate | myWaitEvent_myWait_myRule_1_event_0_SA1

```


Automate Your Business Processes with Salesforce Flow Process Builder

```
      10:21:35.461 (1529526210)|FLOW_ELEMENT_DEFERRED|

        FlowRecordCreate|myWaitEvent_myWait_myRule_1_event_0_SA1

      10:21:35.461 (1529619300)|FLOW_ELEMENT_END|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowRecordCreate|myWaitEvent_myWait_myRule_1_event_0_SA1

      10:21:35.461 (1534801023)|FLOW_BULK_ELEMENT_BEGIN|

        FlowRecordCreate|myWaitEvent_myWait_myRule_1_event_0_SA1

      10:21:35.461 (1681358347)|FLOW_BULK_ELEMENT_DETAIL|

        FlowRecordCreate|myWaitEvent_myWait_myRule_1_event_0_SA1|1

      10:21:35.461 (1963485392)|FLOW_VALUE_ASSIGNMENT|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWaitEvent_myWait_myRule_1_event_0_SA1|true

      10:21:35.461 (1973349443)|FLOW_BULK_ELEMENT_LIMIT_USAGE|

        1 DML statements, total 1 out of 150

      10:21:35.461 (1973886332)|FLOW_BULK_ELEMENT_LIMIT_USAGE|

        1 DML rows, total 1 out of 10000

      10:21:35.461 (1974083134)|FLOW_BULK_ELEMENT_END|

        FlowRecordCreate|myWaitEvent_myWait_myRule_1_event_0_SA1|1|429

```

This snippet displays some internal logic that Process Builder performs for you. The process uses a variable to note that it has
executed the action for this schedule, so that it doesn't accidentally duplicate the action.

```
      10:21:41.527 (7529131090)|FLOW_ELEMENT_BEGIN|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowAssignment|myWaitEvent_myWait_myRule_1_event_0_postWaitExecutionAssignment

      10:21:41.527 (7529875281)|FLOW_ASSIGNMENT_DETAIL|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWaitEvent_myWait_myRule_1_event_0_postActionExecutionVariable|ASSIGN|true

      10:21:41.527 (7529943822)|FLOW_VALUE_ASSIGNMENT|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWaitEvent_myWait_myRule_1_event_0_postActionExecutionVariable|true

      10:21:41.527 (7530040052)|FLOW_ELEMENT_END|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        FlowAssignment|myWaitEvent_myWait_myRule_1_event_0_postWaitExecutionAssignment

```

Then the process evaluates whether to execute any of the other schedules. Notice that the conditions are no longer met for
`..._event_0` . Because of the variable assignment in the previous snippet, the process doesn't re-execute the actions associated
with that schedule.

There's only one schedule, so the process finishes.

```
      10:21:41.527 (7530094566)|FLOW_ELEMENT_BEGIN|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        WaitInfo|myWait_myRule_1

      10:21:41.527 (7530148328)|FLOW_ELEMENT_DEFERRED|

        WaitInfo|myWait_myRule_1

      10:21:41.527 (7530225216)|FLOW_ELEMENT_END|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        WaitInfo|myWait_myRule_1

      10:21:41.527 (7530291079)|FLOW_BULK_ELEMENT_BEGIN|

        WaitInfo|myWait_myRule_1

      10:21:41.527 (7530832531)|FLOW_WAIT_EVENT_WAITING_DETAIL|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWait_myRule_1| myWaitEvent_myWait_myRule_1_event_0|DateRefAlarmEvent|false

      10:21:41.527 (7530895796)|FLOW_WAIT_WAITING_DETAIL|

```


### Automate Your Business Processes with Salesforce Flow Workflow Rules

```
        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWait_myRule_1|0|

      10:21:41.527 (7530968776)|FLOW_VALUE_ASSIGNMENT|

        2ef1ba5afce469a1e74b7b869161e25400a2-7f29|

        myWaitEvent_myWait_myRule_1_event_0|false

      10:21:41.527 (7531068544)|FLOW_BULK_ELEMENT_END|

        WaitInfo|myWait_myRule_1|0|1

```

SEE ALSO:

Troubleshoot Processes

##### Send Alerts When a Screen Flow Fails

To save time troubleshooting screen flows that fail, subscribe to the Flow Execution Error Event
platform event. When a flow interview fails, Salesforce publishes a platform event message. In
Process Builder, you can subscribe to the platform event and perform actions, such as posting to
Chatter or sending custom notifications.

Important: Starting in Summer ’23, you can’t create new processes. You can still activate,
deactivate, and edit any existing processes. To migrate existing processes, use the Migrate
to Flow tool on page 894. For new automations, create flows in Flow Builder on page 16.

**1.** Define the process properties on page 935 to start when a platform event message is received.

**2.** Configure a process trigger for a platform event on page 938.

**3.** Add the process criteria on page 939.

**4.** Create a Chatter post on page 945, or send a custom notification on page 968.

SEE ALSO:

Create a Process

Troubleshoot Processes

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_flowexecutionerrorevent.htm)_ : FlowExecutionErrorEvent

### Workflow Rules

Workflow rules let you automate standard internal procedures and processes to save time across
your org. A workflow rule is the main container for a set of workflow instructions. These instructions
can always be summed up in an if/then statement.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

For example: If it’s raining, then bring an umbrella.

Workflow rules can be broken into two main components.

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

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Criteria: the “if” part of the “if/then” statement. In other words, what must be true of the record for the workflow rule to execute the
associated actions.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**•** Actions: the “then” part of the “if/then” statement. In other words, what to do when the record meets the criteria.

In the raining example, the criteria is “it’s raining” and the action is “bring an umbrella”. If the criteria isn’t met (“it isn’t raining”), then the
action isn’t executed (“you don’t bring an umbrella”).

When a record meets all the criteria for a workflow rule, that rule’s actions are executed. Familiarize yourself with the automated actions
that are available for workflow.

#### Create a Workflow Rule

Automate your organization’s standard process by creating a workflow rule.

Workflow Limits
Salesforce limits the number of total and active rules in your org, the number of time triggers and actions per rule. It also processes
a limited number of daily emails and hourly time triggers.

Workflow Considerations
Learn the intricacies of workflow rules and workflow actions before you begin working with them.

Workflow Rule Examples
Looking for ideas on how workflow rules can help streamline your business? Check out these examples.

Monitor Pending Workflow Actions
When a workflow rule that has time-dependent actions is triggered, use the workflow queue to view pending actions and cancel
them if necessary.

Workflow Terminology
These terms are used when describing workflow features and functionality.

SEE ALSO:

Choose Which Salesforce Flow Feature to Use

#### Create a Workflow Rule

Automate your organization’s standard process by creating a workflow rule.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Watch a Demo: [Creating a Workflow Rule (Salesforce Classic)](https://salesforce.vidyard.com/watch/IqZIFLtEx9rY7AD8QLFE3Q)

1. Set the Criteria for Your Workflow Rule
Get started with creating a workflow rule by selecting the object the rule relates to and
configuring its criteria.

2. Add Automated Actions to Your Workflow Rule
After you’ve set the criteria for your workflow rule, identify what to do when that criteria are
met.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

3. Identify Your Salesforce Org’s Default Workflow User
Select a `Default Workflow User` that you want Salesforce to display with a workflow rule when the user that triggered the
rule isn’t active.


Automate Your Business Processes with Salesforce Flow Workflow Rules

4. Activate Your Workflow Rule
Salesforce doesn’t trigger a workflow rule until you activate it.

SEE ALSO:

Workflow Considerations

Workflow Rule Examples

##### Set the Criteria for Your Workflow Rule

Get started with creating a workflow rule by selecting the object the rule relates to and configuring
its criteria.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Note:

**•** If you have a workflow action that updates a field on a related object, that target object
isn't the one that's associated with the workflow rule.

**•** To create workflow rules based on new case comments or incoming email messages that
automatically update fields on their associated cases, choose Case Comment or Email
[Message. See Workflow Considerations for more information.](https://help.salesforce.com/s/articleView?id=sf.workflow_rules_considerations.htm&language=en_US)

**•** [To create a site usage rule, choose one of the following:](https://help.salesforce.com/s/articleView?id=sf.sites_workflow.htm&language=en_US)

**–** `Organization` (for monthly page views allowed and monthly page views used
fields)

**–** `Site` (for site detail, daily bandwidth and request time, monthly page views allowed,
and other fields)

**–** `User License` (for the monthly logins allowed and monthly logins used fields)

The Organization and Site objects are only available if Salesforce Sites is enabled for your
organization. The User License object isn't dependent on sites, and is only available if you
have Customer Portals or partner portals enabled for your organization.

**•** This release contains a beta version of the workflow on the User object that is production
[quality but has known limitations.](https://help.salesforce.com/s/articleView?id=sf.workflow_user_object_limitations.htm&language=en_US)

`Evaluate the rule when a` **Description**

```
record is:

```

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

```
created

created, and every time

it’s edited

```

Evaluate the rule criteria each time a record is created. If the rule criteria is met, run the rule.
Ignore all updates to existing records.

With this option, the rule never runs more than one time per record.

Evaluate the rule criteria each time a record is created or updated. If the rule criteria is met,
run the rule.

With this option, the rule repeatedly runs every time a record is edited as long as the record
meets the rule criteria.


Automate Your Business Processes with Salesforce Flow Workflow Rules

`Evaluate the rule when a` **Description**

```
   record is:

```

If you select this option, you can't add time-dependent actions to the rule.

`created, and any time it’s` (Default) Evaluate the rule criteria each time a record is created or updated.
`edited to subsequently meet` **•** For a new record, run the rule if the rule criteria is met.
```
criteria

```

**•** For a new record, run the rule if the rule criteria is met.

**•** For an updated record, run the rule only if the record is changed from not meeting the
rule criteria to meeting the rule criteria.

With this option, the rule can run multiple times per record, but it doesn’t run when the
record edits are unrelated to the rule criteria.

For example, suppose that for an opportunity record to meet the rule criteria, the opportunity
probability must be greater than 50%. If you create an opportunity with a probability of
75%, the workflow rule runs. If you edit that opportunity by changing the probability to
25%, the edit doesn't cause the rule to run. If you then edit that opportunity by changing
the probability from 25% to 75%, the edit causes the rule to run. With this last edit, the rule
runs, because the record is changed from not meeting the rule criteria to meeting the rule
criteria.

**1.** From Setup, enter _`Workflow Rules`_ in the `Quick Find` box, then select **Workflow Rules** .

**2.** Click **New Rule** .

**3.** Choose the object to which you want this workflow rule to apply.

**4.** Click **Next** .

**5.** Give the rule a name and description.

**6.** Set the evaluation criteria. For example:

**Option** **Description**

**Evaluate the rule when a record is**
**created**

**Evaluate the rule when a record is**
**created, and every time it’s edited**

Evaluate the rule criteria each time a record is created. If the rule criteria is met, run the rule.
Ignore all updates to existing records.

With this option, the rule never runs more than one time per record.

Evaluate the rule criteria each time a record is created or updated. If the rule criteria is met,
run the rule.

With this option, the rule repeatedly runs every time a record is edited as long as the record
meets the rule criteria.

If you select this option, you can't add time-dependent actions to the rule.

**Evaluate the rule criteria each**

(Default) Evaluate the rule criteria each time a record is created or updated. For a new record,

**time a record is created, and any**

run the rule if the rule criteria is met. For an updated record, run the rule only if the record

**time it’s edited to subsequently**

is changed from not meeting the rule criteria to meeting the rule criteria.

**meet criteria**
With this option, the rule can run multiple times per record, but it doesn’t run when the
record edits are unrelated to the rule criteria.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Option** **Description**

For example, suppose that for an opportunity record to meet the rule criteria, the opportunity
probability must be greater than 50%. If you create an opportunity with a probability of
75%, the workflow rule runs. If you edit that opportunity by changing the probability to
25%, the edit doesn't cause the rule to run. If you then edit that opportunity by changing
the probability from 25% to 75%, the edit causes the rule to run. With this last edit, the rule
runs, because the record is changed from not meeting the rule criteria to meeting the rule
criteria.

**7.** Enter your rule criteria. For example:

**•** Choose `criteria are met` and select the filter criteria that a record must meet to trigger the rule. For example, set the
filter to “Opportunity: Amount greater than 5000” if you want opportunity records with an amount greater than $5,000 to trigger
the rule. If your organization uses multiple languages, enter filter values in your individual language. You can add up to 25 filter
criteria, of up to 255 characters each.

**8.** Enter your rule criteria. For example:

**•** Choose `criteria are met` and select the filter criteria that a record must meet to trigger the rule. For example, set the
filter to “Opportunity: Amount greater than 5000” if you want opportunity records with an amount greater than $5,000 to trigger
the rule. If your organization uses multiple languages, enter filter values in your individual language. You can add up to 25 filter
criteria, of up to 255 characters each.

**•** Choose `formula evaluates to true` and enter a formula that returns a value of “True” or “False.” Salesforce triggers
the rule if the formula returns “True.”

**9.** Click **Save & Next** .

Example: Examples of useful workflow formulas include:

**•** If the number of filled positions equals the number of total positions on a job, update the `Job Status` field to “Filled.”

**•** If mileage expenses associated with visiting a customer site are 35 cents per mile and exceed a $1,000 limit, automatically
update the `Approval Required` field to “Required.”

**•** If a monthly subscription-based opportunity amount is greater than $10,000, create a task for an opportunity owner to follow
up 60 days after the opportunity is closed.

The `$Label` variable isn’t supported in workflow rule formulas. Also, some functions aren't available in workflow rule formulas.

Tip: You can use merge fields for directly related objects in workflow rule formulas.

SEE ALSO:

Workflow Considerations


Automate Your Business Processes with Salesforce Flow Workflow Rules

##### Add Automated Actions to Your Workflow Rule

After you’ve set the criteria for your workflow rule, identify what to do when that criteria are met.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

###### Add an Immediate Action to Your Workflow Rule

_Immediate actions_, like their name suggests, are executed as soon as the workflow rule finishes
evaluating the record.

Add a Time-Dependent Action to Your Workflow Rule
_Time-dependent actions_ are executed at a specific time, such as 10 days before a record’s close
date. When that specific time passes, the workflow rule reevaluates the record to make sure
that it still meets the rule criteria. If the record does, the workflow rule executes those actions.

SEE ALSO:

Identify Your Salesforce Org’s Default Workflow User

Set the Criteria for Your Workflow Rule

###### Add an Immediate Action to Your Workflow Rule

_Immediate actions_, like their name suggests, are executed as soon as the workflow rule finishes
evaluating the record.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

For details on each action type, see Automated Actions .

**1.** Open a workflow rule.

**2.** In the Immediate Workflow Actions section, click **Add Workflow Action** .

**3.** Select one of the options to create an action or select an existing one.

SEE ALSO:

##### Add Automated Actions to Your Workflow Rule


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Workflow Rules

###### Add a Time-Dependent Action to Your Workflow Rule

_Time-dependent actions_ are executed at a specific time, such as 10 days before a record’s close date.
When that specific time passes, the workflow rule reevaluates the record to make sure that it still
meets the rule criteria. If the record does, the workflow rule executes those actions.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Time-dependent actions and time triggers are complex features. As you work with time-dependent
actions and time triggers, keep in mind their considerations.

If you plan on configuring workflow rules that have time-dependent actions, specify a default
workflow user. Salesforce associates the default workflow user with a workflow rule if the user who
initiated the rule is no longer active.

**1.** Open a workflow rule.

**2.** In the Time-Dependent Workflow Actions section, click **Add Time Trigger** .

Note: You can’t add a time trigger if:

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

**•** The evaluation criteria is set to `Evaluate the rule when a record is: created, and every`
`time it's edited` .

**•** The rule is activated.

**•** The rule is deactivated but has pending actions in the workflow queue.

**3.** Specify a number of days or hours before or after a date that’s relevant to the record, such as the date the record was created.

If the workflow rule is still active and valid when this time occurs, the time trigger fires the workflow action.

**4.** Save your time trigger.

**5.** In the section for the time trigger you created, click **Add Workflow Action** .

**6.** Select one of the options to create an action or select an existing one.

**7.** Click **Done** .

SEE ALSO:

Add Automated Actions to Your Workflow Rule

Considerations for Time-Dependent Actions and Time Triggers

##### Identify Your Salesforce Org’s Default Workflow User

Select a `Default Workflow User` that you want Salesforce to display with a workflow rule
when the user that triggered the rule isn’t active.

**User Permissions Needed**

To edit process automation settings: Customize Application

To create, update, and delete flow list views: Manage Flow


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Workflow Rules

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate, deactivate, and edit any existing
workflow rules. To migrate existing workflow rules, use the Migrate to Flow tool on page 894. For new automations, create flows
in Flow Builder on page 16.

If your organization uses time-dependent actions in workflow rules, you must designate a default workflow user. When the user who
triggered the rule isn’t active, Salesforce displays the username of the default workflow user in the `Created By` field for tasks, the
`Sending User` field for email, and the `Last Modified By` field for field updates. Salesforce doesn’t display this username for
outbound messages. If a problem occurs with a pending action, the default workflow user receives an email notification.

When workflow email alerts approach or exceed certain limits, Salesforce sends a warning email to the default workflow user or—if the
default workflow user isn't set—to an active Salesforce admin.

**1.** From Setup, enter _`Process Automation Settings`_ in the `Quick Find` box, then select **Process Automation Settings** .

**2.** For `Default Workflow User`, select a user.

**3.** Save your changes.

SEE ALSO:

Daily Allocations for Email Alerts

##### Associate Actions with Workflow Rules or Approval Processes

Associate actions that have already been created in your organization with a workflow rule and
approval processes.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

**1.** To associate existing workflow actions with a workflow rule:

**a.** From Setup, enter _`Workflow Rules`_ in the `Quick Find` box, then select **Workflow**
**Rules** .

**b.** Select the workflow rule.

**c.** Click **Edit** in the Workflow Actions section.

**d.** Click **Add Workflow Action** in either the Immediate Workflow Actions or Time-Dependent
Actions section, depending on when you want the action to occur, and choose **Select**
**Existing Action** .

**e.** Select the type of action to associate with the workflow rule.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To select existing actions:

**•** Customize Application

**f.** Select the actions in the **Available Actions** box and use the right arrow to move them to the **Selected Actions** box. If necessary,
select the left arrow to remove actions from the **Available Actions** box.

**g.** Save your changes.

**2.** To associate existing workflow actions with an approval process:

**a.** From Setup, enter _`Approval Processes`_ in the `Quick Find` box, then select **Approval Processes** .

**b.** Click the name of an approval process.

**c.** To have the action occur during the initial submission, final approval, final rejection, or recall, click **Add Existing** in the Initial
Submission Actions, Final Approval Actions, Final Rejection Actions, or Recall Actions section.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**d.** To have the action occur during the approval steps, click **Show Actions** in the Approval Steps section, then click **Add Existing**
in the Approval, Rejection, or Recall Actions section. See Add an Existing Automated Action to Your Approval Process on page

**e.** Select the type of action you want to associate with the approval process. The **Available Actions** box lists all existing actions
of the selected type.

**f.** Enter the name of a specific action in the text field and click **Find** .

**g.** Select the actions in the **Available Actions** box that you want to associate with the approval process, and use the right arrow
to move the actions to the **Selected Actions** box. If necessary, select the left arrow to remove actions from the **Available**
**Actions** box.

**h.** Save your changes.

SEE ALSO:

[Manage Automated Actions in Workflow Rules](https://help.salesforce.com/apex/HTViewHelpDoc?id=managing_workflow_actions.htm&language=en_US#managing_workflow_actions)

##### Define a Flow Trigger for Workflow (Pilot)

Create a flow trigger so that you can launch a flow from workflow rules. With flow triggers, you can
automate complex business processes—create flows to perform logic, and have events trigger the
flows via workflow rules—without writing code. For example, your flow looks up and assigns the
relevant entitlement for a case. Create a flow trigger to launch the flow whenever a case is created,
so that all new cases are automatically set with a default entitlement.

Note: The pilot program for flow trigger workflow actions is closed. If you've already enabled
the pilot in your org, you can continue to create and edit flow trigger workflow actions. If you
didn't enable the pilot in your org, use Flow Builder to create a record-triggered flow, or use
Process Builder to launch a flow from a process.

To get started using flow triggers, from Setup, enter _`Flow Triggers`_ in the Quick Find box,
then select **Flow Triggers** . Before you begin:

**•** Create and activate the autolaunched flow that you want this workflow action to launch.

**•** Create the workflow rule that you plan to add this workflow action to.

**•** Understand the special behavior and limitations of flow triggers. See Flow Trigger Considerations
(Pilot) on page 1010.

Complete these steps to create a flow trigger.

**1.** From Setup, enter _`Flow Triggers`_ in the Quick Find box, then select **Flow Triggers** .

**2.** Click **New Flow Trigger** .

**3.** Select the same object as the workflow rule, and then click **Next** .

**4.** Configure the flow trigger.

**Field** **Description**

`Name` Name of the flow trigger.

EDITIONS

Available in: Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To view workflow rules and
actions:

**•** View Setup and
Configuration

To create or change
workflow rules and actions:

**•** Customize Application

`Unique Name` Enter a unique name to refer to this component in the API. The **Unique Name** field can contain
only underscores and alphanumeric characters. It must be unique within the selected object type,


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Field** **Description**

begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

`Protected Component` Reserved for future use.

`Flow` Unique name of the autolaunched flow that this workflow action launches.

`Set Flow Variables` Whether to pass values into the flow’s variables.

**5.** If you select `Set Flow Variables`, specify their names and values.

Click **Set Another Value** to set up to

**Field** **Description**

```
Name

```

Select the name of the flow variable.

Only variables that allow input access can be selected.

`Value` For a flow variable, you can:

**•** Enter a literal value.

**•**
Click, select a field, and click **Insert** .

For a record variable, you can:

**•**
Click, select a record, and click **Insert** .

To help you distinguish between records and fields, all record options are marked with an
asterisk (*) and appear at the top of each list.

**•** To use the current values of the record that was created or edited to cause the workflow rule
to fire, enter _`{!this}`_ .

**•** To use the most recent previous values of the record that was edited to cause the workflow
rule to fire, enter _`{!old}`_ .

In other words, `{!old}` identifies the same record as `{!this}` but uses the record’s values
from immediately before it was edited to cause the workflow rule to fire.

**•** If the record was newly created, `{!old}` is `null` .

**•** Unlike `{!this}`, `{!old}` can’t be selected by clicking . Manually enter _`{!old}`_
in the Value column.

**6.** To put the flow trigger in test mode, select `Administrators run the latest flow version` .

When selected and an admin triggers the workflow rule, the flow trigger launches the latest version of the flow. For all other users,
the flow trigger always launches the active version of the flow.

The same values are passed into the flow variables whether the flow trigger launches the active or latest flow version.

**7.** Click **Save** .


Automate Your Business Processes with Salesforce Flow Workflow Rules

Don’t forget to associate the flow trigger to a workflow rule.

SEE ALSO:

Flow Trigger Considerations (Pilot)

##### Activate Your Workflow Rule

Salesforce doesn’t trigger a workflow rule until you activate it.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

##### To activate a workflow rule, click Activate on the workflow rule detail page. Click Deactivate to

prevent a rule from triggering or if you want to edit the time-dependent actions and time triggers
that are associated with the rule.

You can deactivate a workflow rule at any time. However, if you deactivate a rule that has pending
actions, Salesforce completes those actions as long as the record that triggered the rule isn’t updated.

Note:

**•** You can't delete a workflow rule that has pending actions in the workflow queue. Wait
until pending actions are processed, or use the workflow queue to cancel the pending
actions.

**•** You can't add time-dependent workflow actions to active workflow rules. Deactivate the
workflow rule first, add the time-dependent workflow action, and reactivate the rule.

SEE ALSO:

Set the Criteria for Your Workflow Rule

#### Workflow Limits

Salesforce limits the number of total and active rules in your org, the number of time triggers and
actions per rule. It also processes a limited number of daily emails and hourly time triggers.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

**Per-Org Limit** **Value**

Total rules across objects

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or change
workflow rules and actions:

**•** Customize Application

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

(Applies to any combination of workflow,
assignment, auto-response, and escalation rules,
_active_ and _inactive_ .)

2,000

Total rules per object 500


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Per-Org Limit** **Value**

(Applies to any combination of workflow, assignment,
auto-response, and escalation rules, _active_ and _inactive_ .)

Active rules per object

(Applies to any combination of _active_ workflow, assignment,
auto-response, and escalation rules, as well as record change
processes.)


Time triggers per workflow rule [1] 10

Immediate actions per workflow rule [1] 40

Time-dependent actions per time trigger 40

Workflow time triggers per hour 1,000

Flow trigger workflow actions: flow variable assignments [2] 25 (N/A in Professional Edition)

Combined total of these automations that start or resume based 20,000
on a record’s field value.

**•** Resume events that are defined in active flows

**•** Groups of scheduled actions that are defined in active
processes

**•** Time triggers that are defined in active workflow rules

**•** Inactive flow interviews that are resumed

1The immediate actions and each time trigger can have:

2The pilot program for flow trigger workflow actions is closed. If you've already enabled the pilot in your org, you can continue to create
and edit flow trigger workflow actions. If you didn't enable the pilot in your org, use Flow Builder to create a record-triggered flow, or
use Process Builder to launch a flow from a process.

Daily Allocations for Email Alerts
The daily allocation for emails sent through email alerts is 1,000 per standard user license per org—except for free Developer Edition
and trial orgs, where the daily workflow email allocation is 15. The overall org allocation is 2,000,000. This allocation applies to emails
sent through email alerts in workflow rules, approval processes, flows, processes, or REST API. Single emails sent to external email
addresses are also limited, and how those limits are enforced depends on when your org was created.


Automate Your Business Processes with Salesforce Flow Workflow Rules

##### Daily Allocations for Email Alerts

The daily allocation for emails sent through email alerts is 1,000 per standard user license per
org—except for free Developer Edition and trial orgs, where the daily workflow email allocation is
15. The overall org allocation is 2,000,000. This allocation applies to emails sent through email alerts
in workflow rules, approval processes, flows, processes, or REST API. Single emails sent to external
email addresses are also limited, and how those limits are enforced depends on when your org was
created.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

After your org has reached its daily workflow email allocation:

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Any emails in the workflow queue not sent that day are discarded. Salesforce doesn't try to resend them later.

**•** If a workflow rule with an action and an email alert is triggered, only the email action is blocked.

**•** Final approval, final rejection, approval, rejection, and recall email actions are blocked.

**•** An error message is added to the debug log.

These items don't count against the workflow email allocation:

**•** Approval notification emails

**•** Task assignment notifications

**•** Lead assignment rules notifications

**•** Case assignment rules notifications

**•** Case escalation rules notifications

**•** Salesforce Sites usage alerts

The allocation restriction is based on activity in the 24-hour period starting and ending at midnight GMT. Adding or removing a user
license immediately adjusts the allocation's total. If you send an email alert to a group, every recipient in that group counts against your
daily workflow email allocation.

Single Email Limits

Each licensed org can send single emails to a maximum of 5,000 external email addresses, or recipients, per day. A day is based on
Greenwich Mean Time (GMT).

Sending emails to internal email recipients doesn't count toward the org daily limit.

**•** For orgs created before Spring ’19, the org daily limit is enforced only for emails sent via Apex and Salesforce APIs, except for REST
API.

**•** For orgs created in Spring ’19 and later, the org daily limit is also enforced for email alerts, simple email actions, Send Email actions
in flows, and REST API.

**•** Each user can send emails from the email composer to a maximum of 250 external email recipients per hour.

In Developer Edition orgs and orgs evaluating Salesforce during a trial period, each user can send emails to a maximum of 50 recipients
per day, and each single email can have up to 15 recipients.


Automate Your Business Processes with Salesforce Flow Workflow Rules

Allocation Alerts

When workflow email alerts approach or exceed certain allocations, Salesforce sends a warning email to the default workflow user or—if
the default workflow user isn't set—to an active Salesforce admin.

**When...** **Salesforce Sends...** **Warning Email Includes...**

An email alert isn't sent because the number A warning email for each unsent email alert The unsent email alert’s content and
of recipients exceeds the allocation for a recipients
single email

The org reaches 90% of the allocation of One warning email The allocation and the org's usage
emails per day

The org reaches 90% of the allocation of One warning email The allocation and the org's usage
workflow emails per day

An email alert isn't sent because the org A warning email after every 100 attempted The allocation and the org's usage
reaches the allocation of emails per day email alerts over the allocation

An email alert isn't sent because the org A warning email after every 100 attempted The allocation and the org's usage
reaches the allocation of workflow emails email alerts over the allocation
per day

The org reaches the daily allocation for One warning email The allocation and the org that exceeded
single emails sent to external email the allocation
addresses

SEE ALSO:

_Salesforce Help:_ [Standard User Licenses](https://help.salesforce.com/s/articleView?id=sf.users_license_types_available.htm&language=en_US)

#### Workflow Considerations

Learn the intricacies of workflow rules and workflow actions before you begin working with them.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

**•** Each workflow rule applies to a single object.

**•** If you have workflow rules on converted leads and want to use cross-object field updates on
the resulting accounts and opportunities, you must enable the lead setting `Require`
`Validation for Converted Leads` .

**•** If the custom object is deleted, workflow rules on custom objects are automatically deleted.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** The order that individual actions and types of actions are executed in isn’t guaranteed. Field update actions are executed first, followed
by other actions.

**•** To create workflow rules that update case fields based on new case comments or incoming email messages, choose Case Comment
or Email Message from the `Select Object` dropdown list. Email Message is only available if Email-to-Case or On-Demand
Email-to-Case is enabled. You can only create email message workflow rules for field updates, and case comment workflow rules


Automate Your Business Processes with Salesforce Flow Workflow Rules

for field updates, email alerts, and outbound messages. For example, you can create a workflow rule so that an email marked as `Is`
`Incoming` changes its case's `Status` from Closed to New.

**•** Changes you make to records while using Connect Offline are evaluated by workflow rules when you synchronize.

**•** Salesforce processes rules in this order.

**–** Validation rules

**–** Assignment rules

**–** Auto-response rules

**–** Workflow rules (with immediate actions)

**–** Escalation rules

**•** If a lookup field references a record that is deleted, Salesforce clears the value of the lookup field by default. Or you can choose to
prevent record deletions if they’re in a lookup relationship.

**•** If you create workflow rules to replace any Apex triggers, make sure to delete those Apex triggers when you activate the equivalent
workflow rules. Otherwise, Apex triggers and workflow rules both fire and cause unexpected results, such as overwritten field updates
or redundant email messages.

**•** When an Account record’s owner field is changed, processes and workflows defined on the child object don’t get triggered to run.

When Do Workflow Rules Get Triggered?

**•** Workflow rules can be triggered any time a record is saved or created, depending on your rule criteria. Rules created after saving
records don’t affect those records retroactively.

**•** Workflow rules are triggered when a standard or custom object in a master-detail or lookup relationship is reparented, even if the
object's evaluation criteria is set to `Evaluate the rule when a record is: created, and any time it’s`
`edited to subsequently meet criteria` .

**•** Saving or creating records can trigger more than one rule.

**•** Workflow rules only trigger on converted leads if validation and triggers for lead convert are enabled in your Salesforce org.

**•** Workflow rules trigger automatically and are invisible to the user. Alternatively, approval processes allow users to submit records for
approval.

**•** If your organization uses multiple languages, enter filter values in your individual language. You can add up to 25 filter criteria, of up
to 255 characters each.

When you use picklists to specify filter criteria, the selected values are stored in your org's default language. If you edit or clone
existing filter criteria, first set the `Default Language` on the Company Information page to the same language that was used
to set the original filter criteria. Otherwise, the filter criteria no longer matches your picklist values and returns inaccurate results.

**•** If you use record types in your workflow rule criteria whose labels have been translated using the translation workbench, the translated
label value doesn’t trigger the workflow rule. Workflow criteria evaluate the primary label value and ignore the translated value. To
avoid this problem, set the workflow criteria to evaluate the main record type label value by entering it manually in the `Value`
field.

**•** Campaign statistic fields, such as individual campaign statistics and campaign hierarchy statistics, can’t trigger workflow rules.

**•** If its condition references a field that doesn't have a value, a workflow rule isn't triggered. For example, if a User-based workflow rule
checks “Role not equal to CEO”, the rule isn’t triggered for a user without an assigned role. Instead of conditions, use a formula to
check that the field is either null or set to something other than “CEO”:

```
     UserRoleId == null || UserRole.Name != "CEO"

```

**•** The following actions don't trigger workflow rules.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**–** Mass replacing picklist values

**–** Using the option to replace a picklist value while deleting the current value.

**–** Mass updating address fields

**–** Mass updating divisions

**–** Changing the territory assignments of accounts and opportunities

**–** Converting leads to person accounts

**–** Deactivating Self-Service Portal, Customer Portal, or Partner Portal users

**–** Converting state, country, and territory data from the State and Country/Territory Picklists page in Setup

**–** Changing state and country/territory picklists using AddressSettings in the Metadata API

Workflow Rule Limitations

**•** You can't package workflow rules with time triggers.

**•** You can't create outbound messages for workflow rules on junction objects.

Tip: Use the Developer Console to debug workflow rules. The Developer Console lets you view debug log details and information
about workflow rules and actions. For example, you can view the name of the user who triggered the workflow rule and the name
and ID of the record being evaluated.

##### Workflow for the User Object (Beta)

You can create workflow rules and actions for the User object. You can, for example, send welcome emails to new employees or
sync user data with a third-party service using outbound message actions.

Considerations for Time-Dependent Actions and Time Triggers
When creating time-dependent actions and time triggers for workflow rules, consider these factors.

Flow Trigger Considerations (Pilot)
Flow trigger workflow actions have special behaviors and limitations.

SEE ALSO:

Set the Criteria for Your Workflow Rule

##### Workflow for the User Object (Beta)

You can create workflow rules and actions for the User object. You can, for example, send welcome
emails to new employees or sync user data with a third-party service using outbound message
actions.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Note: This release contains a beta version of workflow on the User object that is production
[quality but has known limitations. To provide feedback and suggestions, go to IdeaExchange.](http://success.salesforce.com/ideaView?id=08730000000Br80AAC)


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Workflow Rules

Example Use Cases

For the User object, you can set up workflow rules to:

**•** Send welcome email messages with training resources to newly created users by using email alert actions.

**•** Send emails when users change roles or are deactivated by using email alert actions.

**•** Deactivate temporary employees after a specified period by using field update actions.

**•** Sync user data with third-party systems by using outbound messages actions.

Merge Field Types for the User Object

To use merge fields from user records in email templates, select from the following merge field types:

**•** User Fields—Use these merge fields to represent the sending user. Merge fields named {!User. _`field_name`_ } return values from
the user record of the person who created or updated the record that triggered the workflow rule.

**•** Workflow Target User Fields—Use these merge fields only in email templates for workflow rules on the User object. Merge fields
named {!Target_User. _`field_name`_ } return values from the user record that was created or updated to trigger the workflow rule.

Beta Limitations for Workflow on the User Object

Understand these limitations before you create workflow rules or workflow actions for the User object.

**•** Tasks aren’t supported as workflow actions for the User object.

**•** When setting the workflow rule criteria, you can’t select `Current User` fields using the picklists. You can, however, use a formula
to set the rule criteria and include fields from the current user. In the formula editor, click **Insert Field**, select `$User`, select the
field, and click **Insert** .

**•** Remember that custom validation rules run _before_ [workflow rules are executed. Refer to Triggers and Order of Execution in the](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm) _Apex_
_Developer Guide_ .

SEE ALSO:

Workflow Considerations

##### Considerations for Time-Dependent Actions and Time Triggers

When creating time-dependent actions and time triggers for workflow rules, consider these factors.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Defining Time Triggers

**•** When defining a time trigger, use standard and custom date and date/time fields defined for
the object. Specify time using days and hours. The valid range is 0–999 days or hours.

**•** You can modify existing time triggers by adding or removing actions.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Note: Removing all the actions from a time trigger doesn’t remove the trigger. Empty triggers are still queued and count
against your hourly workflow time trigger limit. To remove scheduled time triggers, delete them from the workflow queue.


Automate Your Business Processes with Salesforce Flow Workflow Rules

Time Trigger Processing

**•** Time-dependent actions aren’t executed independently. They’re grouped into a single batch that starts executing within one hour
after the first action enters the batch.

Note: Actual execution can be delayed based on service availability.

**•** Apex triggers that fire as a result of time-dependent actions can get executed in a single batch or independently. Follow these best
practices:

**–** In case they fire independently–Ensure that your Apex logic is scoped for a single scheduled action. For example, don't use Apex
static variables to communicate state across Apex code triggered by different scheduled actions.

**–** In case they fire in a single batch, be aware of how the combination of your time-dependent actions and Apex triggers impacts
your Apex governor limits.

**•** Salesforce evaluates time-based workflow on the organization’s time zone, not the user’s. Users in different time zones can see
differences in behavior.

**•** Salesforce doesn’t necessarily execute time triggers in the order they appear on the workflow rule detail page. Workflow rules list
time triggers that use the `Before` field first, followed by time triggers that use the `After` field.

**•** If you set the workflow rule evaluation criteria to `Evaluate the rule when created, and every time it’s`
`edited`, Salesforce doesn't display time-dependent action controls on the workflow rule edit page.

**•** If you change a date field that is referenced by an unfired time trigger in a workflow rule that has been evaluated, Salesforce recalculates
the unfired time triggers associated with the rule. For example, if a workflow rule is scheduled to alert the opportunity owner 7 days
before the opportunity close date, and the close date is set to 2/20/2011, Salesforce sends the alert on 2/13/2011. If the close date
is updated to 2/10/2011 and the time trigger hasn't fired, Salesforce reschedules the alert for 2/3/2011. If Salesforce recalculates the
time triggers to a date in the past, Salesforce triggers the associated actions shortly after you save the record.

**•** If a workflow rule has a time trigger set for a time in the past, Salesforce queues the associated time-dependent actions to start
executing within one hour. For example, if a workflow rule on opportunities is configured to update a field 7 days before the close
date, and you create an opportunity record with the close date set to today, Salesforce starts to process the field update within an
hour after you create the opportunity.

**•** Time-dependent actions remain in the workflow queue only as long as the workflow rule criteria are still valid. If a record no longer
matches the rule criteria, Salesforce removes the time-dependent actions queued for that record.

For example, an opportunity workflow rule can specify:

**–** A criteria set to “Opportunity: Status not equals to Closed Won, Closed Lost”

**–** An associated time-dependent action with a time trigger set to 7 days before the opportunity close date

If a record that matches the criteria is created on July 1 and the `Close Date` is set to July 30, the time-dependent action is
scheduled for July 23. However, if the opportunity is set to “Closed Won” or “Closed Lost” before July 23, the time-dependent action
is removed from the queue.

**•** Salesforce ignores time triggers that reference null fields.

**•** If the record is updated and the evaluation criteria is set to `Evaluate the rule when a record is: created,`
`and any time it’s edited to subsequently meet criteria`, time-dependent actions can automatically
be queued again. Using the previous example, if the opportunity status is changed from Closed Lost to Prospecting and the workflow
rule evaluation criteria is `Evaluate the rule when a record is: created, and any time it’s edited`
`to subsequently meet criteria`, Salesforce reevaluates the time triggers and adds the appropriate actions to the
workflow queue.

**•** Deleting a record that has pending actions removes the pending actions from the workflow queue. You can't restore the actions,
even if you undelete the record.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**•** If the evaluation criteria is set to `Evaluate the rule when a record is: created`, the workflow rule evaluates
its time triggers only one time. If the record that fired the rule changes to no longer meet the evaluation criteria, Salesforce removes
the pending actions from the queue and never reapplies the rule to the record.

**•** You can deactivate a workflow rule at any time. If the rule has pending actions in the workflow queue, editing the record that
triggered the rule removes the pending actions from the queue. If you don't edit the record, the pending actions are processed even
though the rule has been deactivated.

**•** Time-dependent actions aren't executed for a reevaluated workflow rule in the following situations:

**–** The reevaluated workflow rule’s immediate actions cause the record to no longer meet the workflow rule criteria.

**–** An Apex `after` trigger that is executed as a result of a workflow or approvals action causes the record to no longer meet the
workflow rule criteria.

**•** Configuring a task's `Due Date` to “Rule Trigger Date” sets time triggers and workflow task due dates based on the date that the
workflow time trigger's action is executed. For example, if the task due date is “Rule Trigger Date plus 10 days” and the time trigger
is executed on January 1, Salesforce sets the task due date to January 11.

**•** You can add a new active workflow rule with time triggers in a change set and deploy it. You can only change time triggers on a
workflow rule in a change set if it's inactive. The rule must be activated in the destination organization manually or through another
change set that only activates workflow rules and makes no time trigger changes.

For example, let’s say you have an inactive workflow rule in your destination organization, and your change set contains an active
workflow rule with the same name and new or different time triggers. The deployment fails because it activates the workflow rule
first and then tries to add or remove the time triggers.

Note: You must add time-dependent actions manually when including a workflow rule in a change set. The **View/Add**
**Dependencies** function doesn't detect time-dependent actions.

Using Time-Dependent Workflow with Leads

**•** You can’t convert a lead that has pending actions.

**•** If Validation and Triggers from Lead Convert is enabled, existing time-based workflow actions on leads aren't triggered during lead
conversion.

**•** If a campaign member based on a lead is converted before the completion of the time-based workflow actions associated with it,
Salesforce still performs the time-based workflow actions.

Limitations

**•** Time triggers don’t support minutes or seconds.

**•** Time triggers can’t reference the following:

**–** `DATE` or `DATETIME` fields containing automatically derived functions, such as `TODAY` or `NOW` .

**–** Formula fields that include related-object merge fields.

**•** Salesforce limits the number of time triggers an organization can execute per hour. If an organization exceeds the limits for its Edition,
Salesforce defers the execution of the additional time triggers to the next hour. For example, if an Unlimited Edition organization
has 1,200 time triggers scheduled to execute between 4:00 PM and 5:00 PM, Salesforce processes 1,000 time triggers between 4:00
PM and 5:00 PM and the remaining 200 time triggers between 5:00 PM and 6:00 PM.

**•** You can't archive a product or price book that has pending actions.

**•** If time-based workflow actions exist in the queue, you can’t add or remove time triggers or edit trigger dates without deleting the
actions first. Because the deleted records can’t be restored, carefully consider the implications of editing the workflow rules before
you proceed. If you decide to edit the workflow rules, deactivate the workflow that you want to edit, edit the rules as needed, and


Automate Your Business Processes with Salesforce Flow Workflow Rules

then save your changes. For information about finding and deleting time-based workflow actions in the queue, see Monitor Pending
Workflow Actions on page 1021.

You also can’t add or remove time triggers if:

**–** The workflow rule is active.

**–** The workflow rule is deactivated, but has pending actions in the queue.

**–** The workflow rule evaluation criteria is set to `Evaluate the rule when a record is: created, and`
`every time it’s edited` .

**–** The workflow rule is included in a package.

SEE ALSO:

Add Automated Actions to Your Workflow Rule

Identify Your Salesforce Org’s Default Workflow User

##### Flow Trigger Considerations (Pilot)

Flow trigger workflow actions have special behaviors and limitations.

Note: The pilot program for flow trigger workflow actions is closed. If you've already enabled
the pilot in your org, you can continue to create and edit flow trigger workflow actions. If you
didn't enable the pilot in your org, use Flow Builder to create a record-triggered flow, or use
Process Builder to launch a flow from a process.

Understand these considerations before you create flow triggers or add them to workflow rules.

**•** Flow triggers are available only for workflow rules. You can’t use them as actions elsewhere,
for example, in approval processes.

EDITIONS

Available in: Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Flow triggers are available on most—but not all—objects that are supported by workflow rules. You can see the list of supported
objects when you create a flow trigger. From Setup, enter _`Flow Triggers`_ in the `Quick Find` box, then click **Flow Triggers** .

**•** Only active, autolaunched flows can be launched by flow triggers. However, if a flow trigger is in test mode, admins run the latest
flow version while other users run the active flow version.

**•** Flows that are launched from workflow rules are run in system context, which means that user permissions, field-level security, and
sharing rules aren’t considered during flow execution.

**•** If a flow trigger fails at run time, the user who created or edited the record to meet the workflow rule criteria isn’t able to save the
record. To troubleshoot run time issues, see the flow action events in the `Workflow` category of debug logs, which show the flow
version and the values passed into flow variables.

**•** A flow trigger can set the values of up to 25 variables in the flow, with the following limitations.

**–** Flow triggers can’t use multi-select picklist fields to set flow variables.

**–** When a flow trigger uses a currency field to set a flow variable, only the amount is passed into the flow. Any currency ISO code
or locale information is ignored. If your organization uses multiple currencies, the flow trigger uses the amount in the currency
of the record that contains the specified currency field.

**–** Flow triggers can’t pass values into record collection variables in flows.

**•** Always keep one version of the flow active if it’s referenced by an active workflow rule’s flow trigger.

**•** After you activate a workflow rule using the flow trigger, don’t modify or add a version of the flow to include screens or other elements
that violate the run restrictions for an autolaunched flow. If you modify a flow to no longer autolaunch, it can’t be launched by flow
triggers. To work around this situation, you can save the non-autolaunched flow as a new flow and change the new flow to become
autolaunched. Then update the flow triggers to launch the new flow.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**•** Flow triggers aren’t available as time-dependent workflow actions. You can add flow triggers to workflow rules only as immediate
workflow actions.

**•** When the system executes a workflow rule with multiple flow triggers, those flows aren’t run in any particular order.

**•** In a transaction, flow triggers are executed after all workflow field updates, including any Apex triggers and standard validations that
are executed as a result of those workflow field updates. After executing flow triggers, the system executes escalation rules.

**•** Flows that are launched from workflow rules are governed by the per transaction limits already enforced by Apex.

**•** When flows are launched from workflow rules that are triggered by bulk loads or imports, the flows’ data manipulation language
(DML) operations are executed in bulk to reduce the number of calls required and to optimize system performance. The execution
of any of the following flow elements qualifies as a DML operation: Create Records, Update Records, or Delete Records.

For example, suppose that you use Data Loader or the Bulk API to update 50 records, and those updates meet the criteria of a
workflow rule with a flow trigger action. In response, the system executes 50 instances of the flow within the same transaction. Each
instance of a running flow is called an interview. The system attempts to execute each DML operation across all the interviews in
the transaction at the same time. Suppose that five of those interviews are executing the same branch of the flow, which has an
Update Records element called “SetEntitlement.” The system waits for all five interviews to reach that element, and then executes
all five record updates in bulk.

**•** Flow triggers aren’t available in change sets.

**•** Flow triggers aren’t packageable.

#### Workflow Rule Examples

Looking for ideas on how workflow rules can help streamline your business? Check out these
examples.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

**•** Business Processes

**–** Follow Up Before Contract Expires

**–** Follow Up when Platinum Contract Case Closes

**–** Assign Credit Check for New Customer

**–** Notify Account Owner About New, High-Priority Cases

**–** Set a Default Entitlement for Each New Case

**–** Update Shipment Status if Shipment is Delayed

**–** Automatically Activate New Users

**•** Cross-Object Processes

**–** Notify Sales VP About Cases Filed for Top Accounts

**–** Set Default Opportunity Name

**–** Set Target Resolution Date for Cases

**–** Update Application Record when Candidate Accepts Job


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Workflow Rules

**•** Deal Management

**–** Track Closed Opportunities

**–** Override Default Opportunity Close Date

**–** Report Lost Opportunities

**–** Report Unassigned Leads

**–** Send Alert if Quote Line Item Discount Exceeds 40%

**•** Notifications

**–** Notify Key People About Account Owner Changes

**–** Set Reminder for Contact Birthday

**–** Set Reminder for High-Value Opportunity Close Date

**–** Notify Account Owner of Updates by Others

Follow Up Before a Contract Expires

**Object** Contract

**Description** Email a reminder to the renewal manager 20 days before a contract’s end date.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Contract: Status equals Activated)

```

**Immediate Actions** None

**Time-Dependent Actions** 20 Days Before Contract: End Date— `Email Alert:` Email a reminder to the renewal manager to
confirm whether the client wants an extension.

Follow Up When a Platinum Contract Case Closes

This example assumes that a `Contract Type` custom picklist is used to identify the contract level on cases and that the picklist
contains the Platinum value.

**Object** Case

**Description** If the customer has a platinum contract agreement, email a feedback request to the case contact 7 days
after a high-priority case has been closed.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Case: Priority equals High) and

(Case: Closed equals True) and

(Case: Contract Type equals Platinum)

```

**Immediate Actions** None


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Time-Dependent Actions** 7 Days After Case: Date/Time Closed— `Email Alert:` Email a feedback request to the case contact.

Assign Credit Check for a New Customer

This example assumes that a `New Customer` custom field is on opportunities.

**Object** Opportunity

**Description** Assign the Accounts Receivable (AR) department a task to check the credit of a potential customer 15
days before the opportunity close date if the amount is greater than $50,000.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Opportunity: Amount greater than 50000) and

(Opportunity: Closed equals False) and

(Opportunity: New Customer equals True)

```

**Immediate Actions** None

**Time-Dependent Actions** 15 Days Before Opportunity: Close Date— `Task:` Create a task for users in the Accounts Receivable role
to run a credit check.

Notify Account Owner About New, High-Priority Cases

This example assumes that a Service Level Agreement custom picklist called SLA identifies the agreement level on accounts and contains
the Platinum value.

**Object** Case

**Description** Notify the account owner when a high-priority case is created for accounts with a platinum SLA.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Case: Priority equals High) and

(Account: SLA equals Platinum)

```

**Immediate Actions** `Email Alert:` Email the details of the high-priority case to the account owner.

**Time-Dependent Actions** None

Set a Default Entitlement for Each New Case

This example assumes that an active, autolaunched flow looks up the relevant entitlement based on the account, asset, or contact
associated with the new case and updates the case with the entitlement name.

The pilot program for flow trigger workflow actions is closed. If you've already enabled the pilot in your org, you can continue to create
and edit flow trigger workflow actions. If you didn't enable the pilot in your org, use Flow Builder to create a record-triggered flow, or
use Process Builder to launch a flow from a process.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Object** Case

**Description** Set a default entitlement on each new case.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

**Immediate Actions**

Run this rule if the following criteria are met.

```
(Case: Status not equal to Closed)

```

`Flow Trigger:` Look up and assign the relevant entitlement to the case. Pass the account, asset,
or contact associated with the new case into the relevant flow variable to enable the entitlement lookup.
Pass the case ID into the relevant flow variable to enable the case update.

**Time-Dependent Actions** None.

Update Shipment Status If Shipment Is Delayed

**Object** Shipment

**Description** Update the `Shipment Status` field to Delayed if a shipment has exceeded the expected delivery
date and hasn’t reached the customer.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Shipment: Status not equal to Delivered)

```

**Immediate Actions** None

**Time-Dependent Actions** 1 day after Shipment: Expected Delivery Date— `Field Update` : Change `Shipment Status`
field to Delayed on Shipment record.

Automatically Activate New Users

**Object** User

**Description** Make sure that each new user is active so that the user can log in to Salesforce.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(User: Active equals False)

```

**Immediate Actions** `Field Update` : Set `Active` to True.

**Time-Dependent Actions** None.


Automate Your Business Processes with Salesforce Flow Workflow Rules

Notify Sales VP About Cases Filed for Top Accounts

This workflow rule is for sales VPs who want to know about cases filed for top accounts. Top accounts are determined by size and revenue.

**Object** Case

**Description** Notify sales VP about cases filed for top accounts.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
AND(Account.AnnualRevenue > 500000, Account.NumberOfEmployees > 5000)

```

**Immediate Actions** `Email Alert:` Notify VP about cases for large accounts.

**Time-Dependent Actions** None

Set Default Opportunity Name

The opportunity naming convention for some companies is _`Account Name: Opportunity Name`_ . To automate the default
name of each opportunity in your org, create the following workflow rule.

**Object** Opportunity

**Description** Enforce opportunity naming convention.

**Evaluation Criteria** Evaluate the rule when a record is: created, and every time it’s edited

**Rule Criteria (Filter)**

**Immediate Actions**

Run this rule if the following criteria are met.

```
NOT(CONTAINS( Name, Account.Name ))

```

`Field Update` : Set opportunity name to the following formula.

```
Account.Name & ": " & Name

```

**Time-Dependent Actions** None

Set Target Resolution Date for Cases

This example sets a case resolution date based on the value of a field on the associated account. It uses a custom picklist field on accounts
called `Support Level`, which has three values: Basic, Standard, and Premium. It also has a custom date field on cases called `Target`
`Resolution Date` .

Use the following three workflow rule examples to set the target resolution date of a case based on the support level for the related
account.

Set Resolution Date for Basic Support

**Object** Case

**Description** Set the case target resolution date for accounts that have basic support level to 30 days from today.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
ISPICKVAL(Account.Support_Level__c, "Basic")

```

**Immediate Actions** `Field Update` : Set the `Target Resolution Date` to Today() + 30.

**Time-Dependent Actions** None

Set Resolution Date for Standard Support

**Object** Case

**Description** Set the case target resolution date for accounts that have standard support level to 14 days from today.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
ISPICKVAL(Account.Support_Level__c, "Standard")

```

**Immediate Actions** `Field Update` : Set the `Target Resolution Date` to Today() + 14.

Time-Dependent Actions None

Set Resolution Date for Premium Support

**Object** Case

**Description** Set the case target resolution date for accounts that have premium support level to 5 days from today.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
ISPICKVAL(Account.Support_Level__c, "Premium")

```

**Immediate Actions** `Field Update` : Set the `Target Resolution Date` to Today() + 5.

**Time-Dependent Actions** None

Update Application Record When Candidate Accepts Job

This workflow rule closes the Application record when a candidate accepts the job. Cross-object field updates to the main record are
supported between custom objects in a main detail relationship.

**Object** Candidate

**Description** Change the `Application Status` field to Closed for the custom Application object when the
`Candidate Status` field for the custom Candidate object changes to Accepted.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Candidate: Status equals Accepted)

```

**Immediate Actions** `Field Update:` Change the `Application Status` field to Closed on parent Application
record.

**Time-Dependent Actions** None

Track Closed Opportunities

This example assumes that a Closed Opportunities record type provides additional information to certain profiles. For information on
[record types, see Tailor Business Processes to Different Record Types Users.](https://help.salesforce.com/s/articleView?id=sf.customize_recordtype.htm&language=en_US)

**Object** Opportunity

**Description** Change the record type of closed-won opportunities.

**Evaluation Criteria** Evaluate the rule when a record is: created, and every time it’s edited

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Opportunity: Closed equals True) and

(Opportunity: Stage equals Closed Won)

```

**Immediate Actions** `Field Update:` Set the record type to Closed Opportunities.

**Time-Dependent Actions** None

Override the Default Opportunity Close Date

**Object** Opportunity

**Description** Override the default close date from the close of the quarter to 6 months after the opportunity is created.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

**Immediate Actions**

Run this rule if the following criteria are met.

```
(Opportunity: Closed equals False)

```

`Field Update:` Use the following formula to set the opportunity close date to 6 months after the
creation date.

```
DATE( YEAR(TODAY()), (MONTH(TODAY()) + 6), DAY(TODAY()))

```

**Time-Dependent Actions** None


Automate Your Business Processes with Salesforce Flow Workflow Rules

Report Lost Opportunities

**Object** Opportunity

**Description** Notify the VP of sales when a deal is lost if the stage was Proposal/Price Quote and the amount was
greater than $1 million.

**Evaluation Criteria** Evaluate the rule when a record is: created, and every time it’s edited

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
AND( ISCHANGED(StageName), ISPICKVAL(PRIORVALUE(StageName),

"Proposal/Price Quote"), ISPICKVAL(StageName,"Closed Lost"), (Amount

 >1000000))

```

**Immediate Actions** `Email Alert:` Notify the VP of sales role that the deal was lost.

**Time-Dependent Actions** None

Report Unassigned Leads

This example assumes that all unassigned leads are placed in an unassigned leads queue by a leads assignment rule.

**Object** Lead

**Description** Ensure that unassigned leads are tracked in a timely manner by notifying the manager if a lead isn’t
accepted in 2 days.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
Lead Owner equals Unassigned Lead Queue

```

**Immediate Actions** None

**Time-Dependent Actions** 2 Days After Lead: Last Modified Date— `Email Alert:` Notify the manager role that the queue has
unassigned leads that are older than 2 days.

Send Alert If Quote Line Item Discount Exceeds 40%

**Object** Quote Line Item

**Description** Ensure that an email alert is sent if a sales rep applies a quote line item discount that exceeds 40%.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
Quote Line Item: Discount is greater than 40

```

**Immediate Actions** `Email Alert:` Notify the manager role that the quote line item discount exceeds 40%.


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Time-Dependent Actions** None

Notify Key People About Account Owner Changes

**Object** Account

**Description** Notify key people in the sales department when the owner of an account changes if the account’s annual
revenue is greater than $1 million.

**Evaluation Criteria** Evaluate the rule when a record is: created, and every time it’s edited

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
AND( ISCHANGED(OwnerId), AnnualRevenue > 1000000 )

```

**Immediate Actions** `Email Alert:` Notify the person in the sales operations role of the change in account ownership.

**Time-Dependent Actions** None

Set Reminder for Contact Birthday

This example assumes that a `Next Birthday` custom formula field uses the following formula to calculate the date of the contact’s
next birthday on contact records.

```
IF(MONTH(Birthdate) > MONTH(TODAY()),DATE(YEAR(TODAY()),MONTH(Birthdate),DAY(Birthdate)),

IF(MONTH(Birthdate) < MONTH(TODAY()),DATE(YEAR(TODAY())+1,MONTH(Birthdate),DAY(Birthdate)),

IF(DAY(Birthdate) >= (DAY(TODAY())),DATE(YEAR(TODAY()),MONTH(Birthdate),DAY(Birthdate)),

DATE(YEAR(TODAY())+1,MONTH(Birthdate),DAY(Birthdate)))))

```

**Object** Contact

**Description** Send an email to the contact 2 days before the contact’s birthday.

**Evaluation Criteria** Evaluate the rule when a record is: created

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
(Contact: Birthdate not equal to null) and

(Contact: Email not equal to null)

```

**Immediate Actions** None

**Time-Dependent Actions** 2 Days Before Contact: Next Birthday— `Email Alert:` Send a birthday greeting to the contact’s
email address.

Set Reminder for High-Value Opportunity Close Date

**Object** Opportunity


Automate Your Business Processes with Salesforce Flow Workflow Rules

**Description**

Remind the opportunity owner and senior management when the close date is approaching for an
opportunity that has an amount greater than $100,000. Create a follow-up task for the opportunity owner
if the deal is still open when the close date passes.

**Evaluation Criteria** Evaluate the rule when a record is: created, and anytime it’s edited to subsequently meet criteria

**Rule Criteria (Filter)**

Run this rule if the following criteria are met.

```
(Opportunity: Amount greater than 100000) and

(Opportunity: Closed equals False)

```

**Immediate Actions** None

**Time-Dependent Actions**
**•** 30 Days Before Opportunity: Close Date— `Email Alert:` Notify the opportunity owner that 30
days remain.

**•** 15 Days Before Opportunity: Close Date— `Email Alert:` Notify the opportunity owner that 15
days remain.

**•** 5 Days After Opportunity: Close Date— `Task:` Create a follow-up task for the opportunity owner
to update the deal. `Email Alert:` Notify senior management to involve executives.

Notify Account Owner of Updates by Others

**Object** Account

**Description** Notify the account owner when someone else updates the account if the account’s annual revenue is
greater than $1 million.

**Evaluation Criteria** Evaluate the rule when a record is: created, and every time it’s edited

**Rule Criteria (Filter)**

Run this rule if the following formula is true.

```
AND( (LastModifiedById <> OwnerId), (AnnualRevenue > 1000000) )

```

**Immediate Actions** `Email Alert:` Notify the account owner that someone else has updated the account.

**Time-Dependent Actions** None

SEE ALSO:

Workflow Rules

Set the Criteria for Your Workflow Rule


Automate Your Business Processes with Salesforce Flow Workflow Rules

#### Monitor Pending Workflow Actions

When a workflow rule that has time-dependent actions is triggered, use the workflow queue to
view pending actions and cancel them if necessary.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

**1.** From Setup, enter _`Time-Based Workflow`_ in the `Quick Find` box, then select
**Time-Based Workflow** .

**2.** To view all pending actions for any active workflow rules, click **Search** . Or to view only the
pending actions that match the criteria, set the filter criteria and click **Search** .

The filter options are:

**•** **Workflow Rule Name** : The name of the workflow rule.

**•** **Object** : The object that triggered the workflow rule. Enter the object name in the singular
form.

**•** **Scheduled Date** : The date the pending actions are scheduled to occur.

**•** **Create Date** : The date the record that triggered the workflow was created.

**•** **Created By** : The user who created the record that triggered the workflow rule.

**•** **Record Name** : The name of the record that triggered the workflow rule.

The filter isn’t case-sensitive.

To cancel pending actions:

**•** Select the box next to the pending actions you want to cancel.

**•** Click **Delete** .


EDITIONS

Available in: Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
**Developer**, and
**Database.com** Editions

Workflow tasks and email
alerts aren’t available in
**Database.com**

USER PERMISSIONS

To manage the workflow
queue:

**•** Modify All Data

Automate Your Business Processes with Salesforce Flow Workflow Rules

#### Workflow Terminology

These terms are used when describing workflow features and functionality.

Important: Starting in Winter ’23, you can’t create new workflow rules. You can still activate,
deactivate, and edit any existing workflow rules. To migrate existing workflow rules, use the
Migrate to Flow tool on page 894. For new automations, create flows in Flow Builder on page
16.

Workflow Rule

A workflow rule sets workflow actions into motion when its designated conditions are met. You
can configure workflow actions to execute immediately when a record meets the conditions in
your workflow rule, or set time triggers that execute the workflow actions on a specific day. If a
workflow action hasn’t executed yet, you can view and modify it in the workflow queue.

Workflow Action

A workflow action, such as an email alert, field update, outbound message, or task, fires when the
conditions of a workflow rule are met.

Email Alert

Email alerts are actions that send emails, using a specified email template, to specified recipients.
Workflow alerts can be sent to any user or contact, as long as they have a valid email address.

Field Update

A field update is an action that automatically updates a field with a new value.

Flow

EDITIONS

Available in: both Lightning
Experience and Salesforce
Classic

Flow triggers are available
in: Salesforce Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Outbound messages
available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Email alerts are available in:
**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

A _flow_ is an application that can execute logic, interact with the Salesforce database, call Apex classes, and collect data from users. You
can build flows by using Flow Builder.

Flow Trigger

A _flow trigger_ is a workflow action that launches a flow. With flow triggers, you can automate complex business processes—create flows
to perform logic, and have events trigger the flows via workflow rules—without writing code.

The pilot program for flow trigger workflow actions is closed. If you've already enabled the pilot in your org, you can continue to create
and edit flow trigger workflow actions. If you didn't enable the pilot in your org, use Flow Builder to create a record-triggered flow, or
use Process Builder to launch a flow from a process.

Outbound Message

An outbound message sends information to a designated endpoint, like an external service. Outbound messages are configured from
Setup. You must configure the external endpoint and create a listener for the messages using SOAP API.


INDEX

E

Einstein Next Best Action, NBA 766
Einstein Next Best Action, NBA, Strategy Builder 749
Einstein Next Best Action, Strategy Builder, Troubleshoot 791

F

Flow
delivering to users 186
delivering to users, external 216
delivering to users, internal 196
launching from processes 219
process action 219
sharing 186, 196

N

NBA, Einstein Next Best Action, strategy builder, elements 793
NBA, Einstein Next Best Action, Strategy Builder, Expressions 782
nba, einstein next best action, strategy builder, recommendations

752–753, 758, 776, 779
Next Best Action, Setup, Implementation 750

Next Best Action, Strategy Builder, Action Strategies 781
Next Best Action, Strategy Builder, Manage Strategies 789
Next Best Action, Strategy Builder, Platform Status Alert Event 787
Next Best Action, Strategy Builder, Tour the Interface 779

S

Strategy Builder Branch Merge Element; Next Best Action 805
Strategy Builder Branch Selector Element; Next Best Action 805
Strategy Builder Enhance Element; Next Best Action 794
Strategy Builder Filter Element; Next Best Action 801
Strategy Builder First Non-empty Branch Element; Next Best Action

Strategy Builder Generate Element; Next Best Action 797
Strategy Builder Limit Reoffers Element; Next Best Action 802
Strategy Builder Load Element; Next Best Action 800
Strategy Builder Map Element; Next Best Action 803
Strategy Builder Sort Element; Next Best Action 804

V

Voice
create permission set 199

