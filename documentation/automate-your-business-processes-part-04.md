[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Headers (1)—Use section headers to create a visual hierarchy to guide your users to the most important items on a screen. All
sections with headers are collapsible and open by default each time a user visits the screen. Also, section header labels can be
translated.

**•** Columns (2)—Use columns to organize your screen and save your users from unnecessary scrolling.

**•** Column Width (3)—When you add or delete a new column, Flow Builder sets the width of all columns in that section to be equal.
To change a column’s width, select a width from the predefined options.

**•** Column Deletion (4)—When you delete a column, all components and fields in that column are deleted.

Tip: To center or indent your components and fields, or add padding, include empty columns on your screen.

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

Considerations

**•** Sections are responsive to the size of the window that’s showing the flow. On small form factor devices, columns are stacked vertically
instead. However, it isn’t responsive to the width of Lightning page columns and utility bars. For example, if a Lightning page shows
a flow in a sidebar, the width of the entire window determines how the columns appear, even though the sidebar is narrower.

**•** If a screen contains a Section screen component, the screen ignores the Layout property when the flow is distributed in Experience
Builder, the Lightning App Builder, or the utility bar. Screens with a Section screen component also ignore the `flowLayout` URL
parameter when the flow is distributed via URL.

SEE ALSO:

Customize a Flow URL to Render Two-Column Screens

Set the Runtime Experience for URL-Based Flows

Flow Connectors

A connector determines the path that a flow takes at run time.

**Type** **Label** **Example** **Description**

Default _Unlabeled_ Identifies which element to execute
_(Free-Form)_ next.

Default _Unlabeled_ Identifies which element to execute
_(Auto-Layout)_ next.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Decision

```
Decision

outcome

label

```

Identifies which element to execute
when the criteria of a Decision
element outcome are met.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Type** **Label** **Example** **Description**

Wait

_`Wait`_ Identifies which element to execute when an event
_`configuration`_ that’s defined in a Wait element occurs.

```
label

```

Fault Fault Identifies which element to execute when the
previous element results in an error.

Loop For each item Identifies the first element to execute for each
iteration of a Loop element.

Loop After last item Identifies which element to execute after a Loop
element finishes iterating through a collection.

Outgoing Go To _`Destination`_ Identifies which element to go to and execute next.

```
         element

```

Incoming Go To + _`x`_ connections Identifies how many incoming go to connections
an element has.

SEE ALSO:

Flow Elements

Move and Connect Elements to Change a Flow Route

Flow Operators

#### Operators behave differently, depending on what you’re configuring. In Assignment elements,

operators let you change resource values. In conditions and filters, operators let you evaluate
information and narrow the scope of a flow operation.

Flow Operators in Assignment Elements
Use Assignment element operators to change the value of a selected resource.

Flow Operators in Decision, Wait, and Collection Filter Elements
Use condition operators to verify the value of a selected resource. Conditions are used in Decision,
Wait, and Collection Filter elements.


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

Flow Operators in Data Elements and Record Choice Sets
Filter conditions narrow the scope of records that the flow operates on. For example, use filter conditions to update only the contacts
that are associated with the Acme Wireless account. When you add an Update Records element, use filter conditions to narrow the
scope to just the contacts whose parent account is Acme Wireless. The In and Not In operators are available only in Create Records,
Get Records, and Update Records elements.

Flow Operators in Assignment Elements

Use Assignment element operators to change the value of a selected resource.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource.

Note: Looking for the sObject data type from Cloud Flow Designer? In Flow Builder, we
replaced sObject with the Record data type. So your sObject collection variables are now
record collection variables.

Apex-Defined

Match the _`@AuraEnabled`_ attribute’s Apex data type with a flow data type in this reference to
determine which operators are supported.

Boolean

Replace a Boolean resource with a new value.

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

Collection

Update or replace the value of a collection variable or record collection variable.


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference

Currency and Number

Replace (Equals), add to (Add), or subtract from (Subtract) the value of a currency or number resource. Count (Equals Count) the number
of active stages or the number of items in a collection.

Date

Replace (Equals), add to (Add), or subtract from (Subtract) the value of a date/time resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date/Time

Replace a date/time resource with a new value (Equals).

Picklist

Replace a picklist resource with a new value (Equals) or concatenate a value onto the original value (Add).

Note: Before values are assigned or added to a picklist resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist

Replace a multi-select picklist resource with a new value (Equals), concatenate a value onto the original value (Add), or add a selection
to the resource (Add Item).

Note: Before values are assigned or added to a multi-select picklist resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Record

Replace a record variable with a new value (Equals).

Stage

You can’t update the value of a stage, but you can update the values of the stage global variables: `$Flow.CurrentStage` and
`$Flow.ActiveStages` .

Note: Assignments use the stage’s fully qualified name: _`namespace`_ `.` _`flowName`_ `:` _`stageName`_ or _`flowName`_ `:` _`stageName`_ .

```
$Flow.CurrentStage

```


Automate Your Business Processes with Salesforce Flow Flow Reference

Replace the stage selected in `$Flow.CurrentStage` .

```
$Flow.ActiveStages

```

Add or remove active stages in the `$Flow.ActiveStages` global variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Text

Replace a text resource with a new value (Equals) or concatenate a value onto the end of the original value (Add).

Note: Before values are assigned or added to a text resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Operators in Decision, Wait, and Collection Filter Elements

Use condition operators to verify the value of a selected resource. Conditions are used in Decision,
Wait, and Collection Filter elements.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource,

Note: Looking for the sObject data type from Cloud Flow Designer? In Flow Builder, we
replaced sObject with the Record. So your sObject collection variables are now record collection
variables.

Apex-Defined

Match the _`@AuraEnabled`_ attribute’s Apex data type with a flow data type in this reference to
determine which operators are supported.


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

Boolean

Check whether a Boolean resource’s value matches another value or resource.

Choice

Every choice resource has a data type and obeys the operator rules for that data type. However, choice resources support one extra
operator that other resources don’t, no matter what their data type is.


Automate Your Business Processes with Salesforce Flow Flow Reference

Collection

Check whether a Collection resource’s value contains or matches another value or resource.

Currency and Number

Check whether a Currency or Number resource’s value matches, is larger than, or is smaller than another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date and Date/Time

Check whether a Date or Date/Time resource’s value matches, is before, or is after another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Picklist

Check whether a Picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value.


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist

Check whether a multi-select picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value. If the resource’s value includes multiple items, the operators treat
the value as one string that happens to include semi-colons. It doesn’t treat each selection as a different value. For example, the
operators treat `red; blue; green` as a single value rather than three separate values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Record

Check whether a record resource’s value matches another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Stage

Note: Stages resolve to the fully qualified stage name: `namespace.flowName:stageName` or `flowName:stageName` .

Check whether a Stage resource or the `$Flow.CurrentStage` global variable matches, ends with, or starts with another value or
resource.

Check whether `$Flow.ActiveStages` contains a particular stage, matches the value of a Text collection, or is null.

Text

Check whether a Text resource’s value matches, contains, ends with, or starts with another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Note:

**•** Before values are compared to a text resource, they’re converted into string values.

**•** Stages resolve to the fully qualified stage name: `namespace.flowName:stageName` or `flowName:stageName` .


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Operators in Data Elements and Record Choice Sets

Filter conditions narrow the scope of records that the flow operates on. For example, use filter
conditions to update only the contacts that are associated with the Acme Wireless account. When
you add an Update Records element, use filter conditions to narrow the scope to just the contacts
whose parent account is Acme Wireless. The In and Not In operators are available only in Create
Records, Get Records, and Update Records elements.

Use this reference, organized by the data type of the field that you select, to understand the
supported operators.


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

Checkbox Fields

When you select a checkbox field under Field, these operators are available. A flow treats `null` as a different value than `false` . If you
filter for records whose checkbox field is null, no records are returned.

Currency, Number, and Percent Fields

When you select a currency, number, or percent field under Field, these operators are available.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date and Date/Time

When you select a date or date/time field under Field, these operators are available.


Automate Your Business Processes with Salesforce Flow Flow Reference

Picklist and Text Fields

When you select a picklist or text field under Field, these operators are available. The In and Not In operators don’t support picklist fields.


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist Fields

When you select a multi-select picklist field under Field, these operators are available.

Tip: Be careful when using these operators to filter records based on a multi-select picklist field. Even if two resources have the
same items in a multi-select picklist, they can be mismatched if these cases differ.

**•** The spacing before or after the semi-colon. For example, one resource’s value is “red; green; blue” and the other’s value is
“red;green;blue”

**•** The order of the items. For example, one resource’s value is “red; green; blue” and the other’s value is “red; blue; green”

For best results, use the INCLUDES function in a flow formula.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Version Properties

A flow version’s properties consist of its label, description, interview label, and type. These properties
drive the field values that appear on the flow’s detail page.

To change the properties of a flow version, open it in Flow Builder. Then click .

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


## Automate Your Business Processes with Salesforce Flow Automate Complex Processes with Orchestrations

SEE ALSO:

Change the Flow Run Context

API Version for Running a Flow

## Automate Complex Processes with Orchestrations

As your company grows, so does the complexity of your workflows. Processes often require input from multiple users in multiple
departments across multiple time zones. This increased complexity results in an increased amount of time spent waiting for each person
to complete their task in the proper order. Flow Orchestration helps you streamline this process with orchestrations: multi-step processes
that interact with multiple users and systems.

What Is Flow Orchestration?

An orchestration is a sequence of stages, each comprised of one or more steps. A stage can contain background, interactive, and MuleSoft
steps.

Interactive steps have an assigned user and execute a designated screen flow. An admin places the Flow Orchestration Work Guide
Lightning App Builder component on the page layout for the type of record where a person can complete the interactive step assigned
to them. When an orchestration runs an interactive step, the designated user receives an email with a link to their assigned action. The
assigned user clicks the link to go to the record where they complete their action in the Work Guide.

Background steps call an autolaunched flow that Salesforce executes. They can run synchronously or asynchronously and have no user
interaction.

MuleSoft steps call a MuleSoft action that Salesforce executes. They run asynchronously and have no user interaction.

When Should You Use Flow Orchestration?

Use Flow Orchestration to create advanced approval processes, task lists for groups, or any other processes that require multiple interrelated
steps. For example, consider employee onboarding that requires a new employee to go through a multi-level, multi-user, multi-system
approval process to get equipment and access to digital company resources. Use Flow Orchestration to compose and orchestrate that
complex process, and enjoy a top-level experience to manage and monitor every onboarding.

Flow Builder for Flow Orchestration
Get to know the Flow Builder requirements and user interface for Flow Orchestration.

Flow Orchestration Concepts
Learn about what an orchestration is made of and how it relates to flows.

Build an Orchestration
Use Flow Orchestration to build sophisticated business processes by combining and coordinating flows.


### Automate Your Business Processes with Salesforce Flow Flow Builder for Flow Orchestration

Deploy an Orchestration
After you design and test your orchestration, it’s time to put it to work!

Orchestration Run
An orchestration run is created for each instance of an orchestration.

Manage Orchestrations and Work Items
Manage orchestrations and work items with list views. Cancel or suspend a running orchestration. Resume an orchestration run that
failed within the previous 14 days because of an error in an action or flow called by a step. Or resume an orchestration run that was
manually suspended. Reassign work items that have been assigned, but not completed.

Troubleshoot Orchestrations
To troubleshoot a failed orchestration run, use the orchestration fault email. To test an orchestration and observe what happens as
it runs, use the debug option.

Flow Orchestration Limits and Considerations
When designing, managing, and running orchestrations, consider these issues.

Flow Orchestration Entitlements
Flow Orchestration has usage-based entitlements. An orchestration _run_ is a running instance of an orchestration. An _orchestration_
is an application built by your admin that uses stages, steps, and decisions to organize a complex business process.

Flow Orchestration Reference
Bookmark this page for quick access to information about orchestration elements, resources, events, and more.

### Flow Builder for Flow Orchestration

Get to know the Flow Builder requirements and user interface for Flow Orchestration.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Tour the Flow Builder User Interface for Flow Orchestration

Flow Orchestration uses the Auto-Layout canvas in Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Button Bar (1)—Manage your orchestration as you build it.

**•** To run the most recent saved version of the orchestration that’s open, click **Run** .

Note: The Run button is only available for autolaunched orchestrations.

**•** To the left of the buttons, you can see the version’s active or inactive status and when it was last saved.

**•** If the orchestration has warnings or errors, the Show Warnings icon ( ) or the Show Errors ( ) icon appears. To see their details,
click the icon.

Toolbox (2)—Create variables, constants, formulas, or text templates to use in your orchestration. Or view a list of all resources and
elements that you added.

Canvas (3)—Build an orchestration on the canvas. As you add elements to the canvas and connect them, you can see a diagram of your
orchestration.

Note: To insert an element, in the desired location, click . Flow Builder then shows the options and possible elements for this
location.

Details (4)—Set attributes for the element selected in the canvas. The Details panel closes when no element is selected.

Keyboard Shortcuts

Use these handy keyboard shortcuts for macOS and Windows to quickly navigate orchestrations.

Flow Orchestration Concepts

Learn about what an orchestration is made of and how it relates to flows.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

#### Orchestrations

An orchestration uses stages, steps, and decisions to organize complex business processes.

Building Blocks of Orchestrations
Stages and steps are the building blocks of an orchestration.

Anatomy of an Orchestration
Combine elements, connectors, and resources to build orchestrations.

Orchestration Types
An orchestration’s type determines how the orchestration can be distributed.

Triggers for Orchestrations
Creating or updating a record can trigger an orchestration that requires additional input from users, approval from assigned users,
other updates to the record, or changes to related records. In the Start element of a record-triggered orchestration, you can specify
new and changed records of a specific object. Autolaunched orchestrations don’t use triggers. Use another mechanism to launch
an autolaunched orchestration, such as custom Apex classes or custom URLs. Use Flow Orchestration to automate complex processes,
and use Flow Trigger Explorer to order record-triggered flows.

What’s the Difference Between a Flow and an Orchestration?
Salesforce offers several features that automate internal procedures and business processes to save time across your org.

Advanced Orchestration Concepts
After you understand the basics, you’re ready for a closer look at the context in which orchestrations run and how they perform work
items at the same time.

#### Orchestrations

An orchestration uses stages, steps, and decisions to organize complex business processes.

Build orchestrations using the Flow Orchestration tiles in Flow Builder. Flow Orchestration tiles limit
the available elements and available resources in your orchestration and include Stage elements
and Step resources that aren’t available in flows. Flow Orchestration always uses Auto-Layout in
Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration Run Life Cycle

Flow Orchestration Types

The Flow Orchestration tiles are Autolaunched Orchestration (No Trigger) and Record-Triggered Orchestration and can be found on the
All+Templates tab of the New Flow window. Trigger an autolaunched orchestration using a custom Apex class or a custom URL. The
creation or update of a record can trigger a record-triggered orchestration, but only after the record is saved.

Variables in Orchestrations

Autolaunched orchestrations can use input variables to require input from a process that calls it.

To reference output values from flows called by orchestration steps, use the step’s automatic output.

Record Refresh in Orchestrations

When you reference a record variable or a record collection in an orchestration configured to run on API version 58.0 and later, records
are refreshed with their latest values each time the orchestration run resumes. In an autolaunched orchestration run, all referenced
records are refreshed. In a record-triggered orchestration, all referenced records except $Record_Prior are refreshed.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Run Record Ownership

For flow orchestration run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

SEE ALSO:

Use Automatic Output in Orchestrations

Flow Orchestration Resource: Global Variables

#### Building Blocks of Orchestrations

##### Stages and steps are the building blocks of an orchestration.

Orchestration Stages
A stage groups related steps, organizing them into a logical phase. Stages are executed sequentially, and only one stage in an
orchestration can be in progress at a time. You configure the conditions that must be met for the stage to be considered complete.

Orchestration Steps
Steps are grouped in stages and can be run sequentially or concurrently. Interactive steps assign the completion of an active screen
flow to a person, group, or queue and require user intervention. Background steps run an active autolaunched flow synchronously
or asynchronously and have no user interaction. MuleSoft steps run an action imported from a MuleSoft operation and have no user
interaction.

Flows in Orchestrations
Each background and interactive step in an orchestration runs an associated flow. If the logic for controlling stage and step execution
calls for more than 3 requirements, use an evaluation flow to create more complex criteria.

Flow Orchestration Work Items
When an interactive step in an orchestration runs, it creates a work item and assigns it to a user, group, or queue. The orchestration
run then sends an email with a link to the specified record page to all assigned users. They complete the work in the Orchestrator
Work Guide component on the specified record page.

Orchestration Stages

A stage groups related steps, organizing them into a logical phase. Stages are executed sequentially,
and only one stage in an orchestration can be in progress at a time. You configure the conditions
that must be met for the stage to be considered complete.

General

An orchestration must contain at least one stage. You can’t control when a stage starts because
stages run sequentially. To control when a stage completes, select one of the exit conditions.

Note: The Stage element in Flow Orchestration isn’t related to the Stage resource in Flow
Builder.

Exit Condition

To control when a stage completes, select an exit condition.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Automatic Output

An orchestration has access to a stage’s status after it’s in progress. At design time, however, automatic output resources are available
throughout an orchestration, even before associated orchestration runs have access to the automatic output. This capability means that
when you create an orchestration you must reference automatic output resources only when associated orchestration runs have access
to it.

Status

When an orchestration is running, it manages the status for each stage. Because stages run sequentially and have no entry conditions,
they only have a status after they’re in progress. The corresponding orchestration stage run record is created after the stage is in progress.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

History

In history, an orchestration stage has several possible milestones.

Flow Orchestration Stage Run Record Ownership

For flow orchestration stage run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

SEE ALSO:

Evaluation Flows in Orchestrations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration Steps

##### Steps are grouped in stages and can be run sequentially or concurrently. Interactive steps assign

the completion of an active screen flow to a person, group, or queue and require user intervention.
Background steps run an active autolaunched flow synchronously or asynchronously and have no
user interaction. MuleSoft steps run an action imported from a MuleSoft operation and have no
user interaction.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Automatic Output

At design time, automatic output resources are available throughout an orchestration, even before
associated orchestration runs have access to the automatic output. This capability means that when
you create an orchestration you must reference automatic output resources only when associated
orchestration runs have access to it.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Note: To allow an orchestration access to a user-defined output variable in a flow called by a step, mark it as **Available for output**
in the flow.

Note: An orchestration uses the isOrchestrationConditionMet output variable in evaluation flows. All other user-defined output
variable values are discarded.

**Table 2: Orchestration Run Access to Automatic Output**


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Status

When an orchestration is running, it manages the status for each step.

History

In history, a step in an orchestration has several possible milestones.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Step Run Record Ownership

For flow orchestration step run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

Flow Orchestration Background Steps
A background step launches an active autolaunched flow and has no user interaction. You can control when a background step is
ready to start.

Flow Orchestration Interactive Steps
An interactive step launches an active screen flow and requires user interaction. You can control when an interactive step is ready
to start or when its status is set to completed.

Flow Orchestration MuleSoft Steps
A MuleSoft step asynchronously runs an operation imported from a MuleSoft API and has no user interaction. You can control when
a MuleSoft step is ready to start.

Flow Orchestration Background Steps

A background step launches an active autolaunched flow and has no user interaction. You can
control when a background step is ready to start.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Background Step Work Cycle


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Asynchronous Background Step

By default, background steps are processed synchronously. When you select **Contains external callouts or wait elements**, a background
step is processed asynchronously. Use an asynchronous background step when the background step calls an autolaunched flow that
contains a Pause or Wait element or an external callout.

When the autolaunched flow called by an asynchronous step is completed, it publishes a Flow Orchestration Event platform event. That
event causes the orchestration to evaluate the status of the current stage and each step with a status of Not Started or In Progress
contained within the stage.

When to Start the Step

To control when a background step starts, select a condition.

Running Context of an Action Called by a Background Step

For API version 60.0 and later, by default, an active autolaunched flow called by a background step runs in the context of the Automated
Process User. To run a background step in the context of a different user, use the Select Who to Run the Action As section in the background
step's Properties panel. To control the system context’s record-level access, use the How to Run the Flow advanced option of the
autolaunched flow.

For API version 59.0 and earlier, an active autolaunched flow called by a background step runs in the same context that the orchestration
runs in.

**Table 3: Running Contexts of Background Steps in API Version 59.0 and Earlier**

For API version 59.0 and earlier, the context that an active autolaunched flow called by an asynchronous background step runs in depends
on the context of the parent orchestration run


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

**Table 4: Running Contexts of Asynchronous Background Steps in API Version 59.0 and Earlier**

SEE ALSO:

Evaluation Flows in Orchestrations

Flow Orchestration Interactive Steps

An interactive step launches an active screen flow and requires user interaction. You can control
when an interactive step is ready to start or when its status is set to completed.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Interactive Step Work Cycle

For flows running in version 57.0 and earlier, after an interactive step is marked as complete, an orchestration run resumes in the context
of the user who completed the associated work item. If the person who completed a work item has granular access to specific flows
without the Run Flows permission, the orchestration run can’t resume. To resume the orchestration, someone with the Run Flows
permission can run another work item or an admin can trigger a Flow Orchestration Event with the ID of the paused orchestration run.

When to Start the Step

To control when an interactive step starts, select a condition.

When to Complete the Step

To control when an interactive step completes, select a condition.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Who Completes the Step

When an orchestration is designed, an interactive step is assigned to a user, group, or queue.

**Table 5: Interactive Step Assignees**

At run time, assigned users, groups, and queues receive a notification email with a link to their assigned work by default. You can stop
Flow Orchestration from sending these email notifications, but you can’t customize the default email. See Disable Default Email Notifications
for Work Item Assignments.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Where to Complete the Step

The assignee or a person from the assigned group or queue completes the associated screen flow on a related record page. A link to
this related record page is included in the email sent to the assigned person, group, or queue.

Running Context of a Flow Called by an Interactive Step

An active screen flow called by an interactive step runs in the context of the person who’s completing it.

SEE ALSO:

Running Context of an Orchestration

Evaluation Flows in Orchestrations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration MuleSoft Steps

A MuleSoft step asynchronously runs an operation imported from a MuleSoft API and has no user
interaction. You can control when a MuleSoft step is ready to start.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

MuleSoft Step Work Cycle

When to Start the Step

To control when a MuleSoft step starts, under Select When to Start the Step, select a condition.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Running Context of a MuleSoft Action Called by a MuleSoft Step

For API version 60.0 and later, by default, a MuleSoft action called by a MuleSoft step runs in the context of the Automated Process User.
To run a MuleSoft action in the context of a different user, use the Select Who to Run the Action As section in the MuleSoft step's Properties
panel.

For API version 59.0 and earlier, a MuleSoft action called by a MuleSoft step runs in the context of the user that the orchestration ran as
before the MuleSoft step starts.

SEE ALSO:

Evaluation Flows in Orchestrations

##### Flows in Orchestrations

Each background and interactive step in an orchestration runs an associated flow. If the logic for
controlling stage and step execution calls for more than 3 requirements, use an evaluation flow to
create more complex criteria.

Background Steps

Each background step calls an autolaunched flow.

Interactive Steps

Each interactive step assigns a screen flow to a user, group, or queue.

When to Start the Step

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Each step can call an evaluation flow to determine whether the step can be started. An evaluation flow is a flow with a process type of
Evaluation Flow. It’s an autolaunched flow that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` . To indicate that the custom entry conditions are met, the output variable must be set to
true.

Note: The Boolean `isOrchestrationConditionMet` variable defined in an evaluation flow must be initialized to false.

When to Complete the Step

An interactive step or a stage can call an evaluation flow to determine whether the step can be considered complete. An evaluation
flow is a flow with a process type of Evaluation Flow. It’s an autolaunched flow that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` . To indicate that the custom exit conditions are met, the output variable must be set to true.

Note: The Boolean `isOrchestrationConditionMet` variable defined in an evaluation flow must be initialized to false.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Variables

Flows can have internal-only, input, and output variables.

If the combined input values for a flow called by an orchestration step is more than 32,768 characters, the orchestration fails. This error
can be caused by passing one or more records to a flow called by a step. To avoid this error, pass a record ID to the referenced flow, and
use a Get Records element in the flow with the passed ID. Using a passed ID with a Get Records element also means that you always
have the latest version of the record.

Evaluation Flows in Orchestrations
When you need more than 3 requirements to control stage and step execution, use an evaluation flow. Select the Evaluation Flow
tile in the New Flow window to create an evaluation flow.

SEE ALSO:

Flow Types

Automate Tasks with Flows


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

###### Evaluation Flows in Orchestrations

When you need more than 3 requirements to control stage and step execution, use an evaluation
flow. Select the Evaluation Flow tile in the New Flow window to create an evaluation flow.

Variables in Evaluation Flows

When you select the Evaluation Flow tile in the New Flow window, you create an evaluation flow
that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` .

Initialize `isOrchestrationConditionMet` to false, and to indicate that the custom
conditions are met, set `isOrchestrationConditionMet` to true.

Evaluation flows only return a value for `isOrchestrationConditionMet` . Values for any
other output variables are discarded.

Evaluation Flow Execution

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Every time an asynchronous background step, an interactive step, or a MuleSoft step within the current stage is completed, the orchestration
evaluates the conditions for that stage and its steps. To trigger an evaluation of conditions for the current stage and its steps, publish
an orchestration event with $Orchestration.Instance

The status of each stage or step determines which conditions the orchestration checks. If the condition being checked relies on an
evaluation flow, the evaluation flow runs.

**•** When a stage is in progress, the orchestration determines whether it can be completed.

**•** For each not started step within the current stage, the orchestration determines whether the step is ready to start.

**•** For each in progress interactive step within the current stage, the orchestration determines whether the step can be marked complete.

Running Context of an Evaluation Flow

In API version 60.0 and later, evaluation flows can be run only in system context without sharing and have access to all data.

In API version 58.0 and 59.0, evaluation flows always run in system context.

In API version 57.0 and earlier, evaluation flows run as specified in the flow’s How to Run the Flow advanced option.

SEE ALSO:

Trigger an Evaluation of Orchestration Stage and Step Conditions


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Work Items


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

When Assignment Notifications Are Made with the Omni-Channel Widget

When an interactive step is assigned to a queue associated with the Orchestration Work Item object, the queue members receive
notifications based on your defined routing logic in the Omni-Channel widget. The notification by Omni-Channel widget is in addition
to the default email notification sent to queue members.

Internal User Access to Work Items

Internal users get a link in their email notification to the related record page where they can complete their assigned work item. They
can also view and access their assigned work in the Flow Orchestration Work Items list view or in their To Do List. To allow internal users
to complete assigned work, before the orchestration runs, place the Flow Orchestration Work Guide component on the related record
page layout in Lightning App Builder.

Experience Cloud Site Visitor Access to Work Items

Credentialed Experience Cloud site visitors usually get a link in their email notification to the related record page of the oldest live
Experience Cloud site that they’re a member of. They can also view and access their assigned work in the Orchestration Work Item object
list view.

Before the orchestration runs, in Experience Builder, the admin sets up site visitor access to orchestration work items.

**•** In Experience Builder, the admin places the Flow Orchestration Work Guide component on the related record page in Aura and LWR
sites.

**•** In Experience Builder, the admin adds the Orchestration Work Item List object page to Aura and LWR sites.

Work Assigned to an Internal User

When an interactive step runs, the orchestration creates a work item and assigns it to the specified internal user. The assigned user
receives an email with a link to the internal related record page notifying them that they have a work item to complete. The work item
also appears in the assigned user's To Do List. When the user clicks the link to the work item, they then can complete the screen flow
associated with the interactive step in the Work Guide on the internal related record page.

Work Assigned to a Credentialed Experience Cloud Site Visitor

When an interactive step runs, the orchestration creates a work item and assigns it to the specified credentialed Experience Cloud site
visitor. The assignee receives an email that notifies them that they have a work item to complete. The email contains a link to the related
record page on the oldest live site that they’re a member of. When the site visitor clicks the email link, they then complete the associated
screen flow in the Work Guide on the related record page that they’ve been directed to.

Work Assigned to an Internal Group or Queue

When the interactive step runs, the orchestration creates a work item and assigns it to the specified group or queue. All users in the
assigned internal group or internal queue receive an email with a link to the internal related record page notifying them that they have
an action to complete. When a user clicks the link in the email and the work item opens, the user can run the screen flow in the Work
Guide on the internal related record page.

An assigned work item is completed by the first user to complete the screen flow. If two users execute the screen flow simultaneously,
the user who completes the flow second receives an error. After the work item is completed, other users from the assigned group or
queue see no related work in the Work Guide component on the internal related record page.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Work Assigned to a Group or Queue of Credentialed Experience Cloud Site Visitors

When the interactive step runs, the orchestration creates a work item and assigns it to the specified group or queue of credentialed
Experience Cloud site visitors. Site visitors in an assigned group or queue receive an email notifying them that they have an action to
complete. The email usually contains a link to the related record page of the oldest live Experience Cloud site that the visitors are all
members of. When a group or queue member clicks the link, the visitor is taken to the related record page of the oldest live Experience
Cloud site that all group or queue members are credentialed for. From that related record page, the site visitor can complete the associated
screen flow in the Work Guide.

Experience Cloud site visitors can also view work items assigned to them in the Orchestration Work Item List object page. From the
Orchestration Work Item List, they can also access their assigned work. When the credentialed site visitor goes to the related record page
of the Aura or LWR site that they’re a member of, the visitor can run the screen flow in the Work Guide.

An assigned work item is completed by the first credentialed site visitor to complete the screen flow. If two credentialed site visitors
execute the screen flow simultaneously, the one who completes the flow second receives an error. After the work item is completed,
other site visitors from the assigned group or queue see no related work in the Work Guide component on the related record page.

Work Items Reassigned to a User, Group, or Queue

You can reassign open work items for a running orchestration to a different user, group, or queue. After reassignment, a work item is
processed like it was after the running orchestration created it.

Work Item Statuses


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

History

In history, an orchestration work item has several possible milestones.

Flow Orchestration Work Item Record Ownership

For flow orchestration work item records created in Winter ’23 or later, the owner is either the assigned user or the automated process
user.

For flow orchestration work items created before Summer ’24 and assigned to a queue, the owner is the automated process user.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

SEE ALSO:

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Anatomy of an Orchestration

Combine elements, connectors, and resources to build orchestrations.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**•** Each element (1) represents an action that the flow can execute. Orchestrations use Stage and Decision elements.

**•** Each connector (2) defines an available path that the orchestration can take at run time.

**•** Each stage consists of one or more steps (3).


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

**•** Each resource (4) represents a value that you can reference through a stage, step, or decision.

#### Orchestration Types

An orchestration’s type determines how the orchestration can be distributed.

All orchestrations are made up of steps grouped within a series of stages. Interactive steps contain
a screen flow and require user interaction. Background steps contain an autolaunched flow and
don’t require user interaction. An orchestration’s type affects how an orchestration is launched.

#### Triggers for Orchestrations

Creating or updating a record can trigger an orchestration that requires additional input from users,
approval from assigned users, other updates to the record, or changes to related records. In the
Start element of a record-triggered orchestration, you can specify new and changed records of a
specific object. Autolaunched orchestrations don’t use triggers. Use another mechanism to launch
an autolaunched orchestration, such as custom Apex classes or custom URLs. Use Flow Orchestration
to automate complex processes, and use Flow Trigger Explorer to order record-triggered flows.

In Flow Orchestration, the trigger occurs after a record is saved.

#### What’s the Difference Between a Flow and an Orchestration?

Salesforce offers several features that automate internal procedures and business processes to save
time across your org.

Flow

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

A _flow_ is an application that automates a business process by collecting data and doing something in your Salesforce org or an external
system. Flows can provide screens to guide users through your business process.

Flows aren’t tied to any one object, but they are record-centric. Flows can look up, create, update, and delete records for multiple objects.
You can build flows with Flow Builder, a point-and-click tool.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration

An _orchestration_ is an application that builds sophisticated business processes by combining and coordinating a series of flows.
Orchestrations are user-centric. You can manage processes that involve different users and different parts of your organization through
one orchestration. Flow Orchestration lets you monitor operations and improve efficiency.

Advanced Orchestration Concepts

After you understand the basics, you’re ready for a closer look at the context in which orchestrations run and how they perform work
items at the same time.

Running Context of an Orchestration
The running context determines the access that an orchestration has to Salesforce data and the context used by a paused orchestration
to resume. By default, the running context of an orchestration is the Automated Process User in system context.

Orchestration Versioning
Flow Orchestration has two levels of versioning: the version of the orchestration and the version of a flow called by an orchestration.

Running Context of an Orchestration

The running context determines the access that an orchestration has to Salesforce data and the
context used by a paused orchestration to resume. By default, the running context of an orchestration
is the Automated Process User in system context.

The default running user for an orchestration depends on the type of orchestration and the API
version that it runs in.

Autolaunched Orchestration

For API version 60.0 and later, an autolaunched orchestration always launches and resumes in the
context of the Automated Process User in system context.

For API version 59.0 and earlier, an autolaunched orchestration usually launches in the context of
the user who launched the orchestration. If the orchestration is launched from Apex, it runs in a
system context. Control the context that an autolaunched orchestration launches and resumes in
with the How to Run the Orchestration advanced option.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

For API version 59.0 and earlier, the context that a paused, autolaunched orchestration resumes in depends on how it was launched or
what caused it to resume.

**Table 6: Resume Contexts for Autolaunched Orchestrations in API Version 59.0 and API Version 58.0**


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Record-Triggered Orchestration

For API version 60.0 and later, a record-triggered orchestration always launches and resumes in the context of the Automated Process
User in system context.

For API version 59.0 and earlier, a record-triggered orchestration always launches in the context of the user who triggered the orchestration
in system context.

For API version 59.0 and earlier, the context that a paused, record-triggered orchestration resumes in a user in system context. The user
that the record-triggered orchestration resumes as depends on what caused it to resume.

**Table 7: User Contexts of Record-Triggered Orchestrations in API Version 59.0 and Earlier**

##### Orchestration Versioning

Flow Orchestration has two levels of versioning: the version of the orchestration and the version of
a flow called by an orchestration.

Orchestration Definition Versioning

An orchestration definition can have 1 active version at a time. The orchestration definition version
used by an orchestration run is the version that’s active at the time the run starts.

**•** If you activate a new version of an orchestration’s definition after an orchestration run based
on that definition starts, the orchestration run continues to run the definition version that it
started in.

**•** Only orchestration runs that start after the new version was activated use the new active version.

Flow Definition Versioning

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Interactive and background steps call flows. A step uses the definition version of the flow that’s active when the step starts.

**•** If you activate a new definition version of a referenced flow after the orchestration run starts and the associated step run is created,
the old version of the flow runs.


### Automate Your Business Processes with Salesforce Flow Build an Orchestration

**•** If you activate a new definition version of a referenced flow after the orchestration run starts but before the associated step run is
created, the new version of the flow runs.

### Build an Orchestration

Use Flow Orchestration to build sophisticated business processes by combining and coordinating
flows.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
### Builder:

It’s easier to automate a business process when you understand how the pieces fit. Before you
create your orchestration, talk to your stakeholders to understand the requirements. You can save
draft orchestrations without knowing all the required information, but you must specify all associated
flows and details before you can activate and run your orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Orchestrations are made up of Stage elements and Decision elements. Stages contain at least one step, each step calling an action to
run. Background and interactive steps call flows. MuleSoft steps call MuleSoft actions imported from MuleSoft APIs. Whenever possible,
create the flows and import the MuleSoft actions that you need before you build your orchestration.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start from Scratch**, and then click **Next** .

**3.** Select the orchestration type, and then click **Create** .

**4.** (Optional) To configure the Start element for a record-triggered orchestration, click **Edit** .

**5.** To add an element between the Start and End elements, click, and select the element.

**6.** To add steps to a stage, click **Add Step** .

**7.** To create a loop or connect to a different element, after the stage, click, click **Connect to element**, and then click on the
desired element.

**8.** Save your orchestration.

After you build an orchestration, activate it, and then test it to make sure that it’s working as you expect. You’re then ready to use it.

Use Decision Elements in an Orchestration
Control when an orchestration takes a specific decision outcome.

Define Requirements for Stages and Steps in an Orchestration
Use requirements to resume an orchestration when a record changes. Define up to three requirements to determine when a step
is ready to start or when to mark an interactive step or stage complete.

Assign an Interactive Step in an Orchestration
When you create an interactive step, you assign it to a user, group, or queue. A user can be an internal user or a credentialed Experience
Cloud site visitor. Groups or queues can include internal users, credentialed Aura site visitors, or credentialed LWR site visitors. You
can also assign an interactive step to a resource that contains a username, group API name, or queue API name when the orchestration
runs. When the active screen flow associated with the interactive step runs, an assigned user completes the flow on the related
context record.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

Route Orchestration Work Items with Omni-Channel
To use Omni-Channel routing in Service Cloud with orchestration work items, you must have at least one queue associated with the
Orchestration Work Item. When you assign an interactive step to that queue, members of the queue receive notifications via the
Omni-Channel widget based on your routing logic. Unless you disable default email notifications for work items, queue members
also receive email notifications.

Redirect an Orchestration Path
Flow Orchestration uses Auto-Layout in Flow Builder. In Auto-Layout, elements on the canvas are spaced and connected automatically.
Use Go To connectors when you have elements that don’t follow the usual consecutive auto-layout path.

Add an End Element to an Orchestration Path
All elements in an orchestration are connected automatically or connected by Go To connectors that you add manually. To finish a
path in your orchestration, add an End element.

Use Automatic Output in Orchestrations
An orchestration has access to output for its stages, steps, and decisions. Query the status of any stage or step in the orchestration.
Use output parameters from any step’s associated flow. In an orchestration configured to run on API version 58.0 and later, referenced
automatic outputs that contain a record or a record collection are refreshed with their latest values each time the orchestration run
resumes.

Trigger an Evaluation of Orchestration Stage and Step Conditions
Every time a step within the current stage completes, the orchestration evaluates the conditions for that stage and its steps. You
can also publish an orchestration event from a flow to trigger an evaluation of orchestration stage and step conditions.

Integrate an Orchestration with External Systems
Add a MuleSoft step to your orchestration to call an imported MuleSoft action. You can also use the
`$Orchestration.Instance` system variable to integrate external systems with your orchestration.

Create an Orchestration Template
You can save a new or existing orchestration as a template, and then use it as a starting point for creating other orchestrations in
Flow Builder. You can also distribute the template via a managed package so that subscribers can create orchestrations based on
the template.

Make Work Accessible to Assigned Users
When an orchestration runs an interactive step, it emails a notification to the assigned user, group, or queue. Credentialed Experience
Cloud site visitors can see and access their assigned Flow Orchestration work items on the Orchestration Work Item List object page.
Internal users and credentialed Experience Cloud site visitors complete their assigned work in the Work Guide.

#### Use Decision Elements in an Orchestration

Control when an orchestration takes a specific decision outcome.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Before you begin, add the Decision element to your orchestration.

**1.** Set up the conditions.

At run time, the conditions are evaluated in the order you specify.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Build an Orchestration

**2.** Identify the logic between the conditions.

**Column Header** **Description**

**Resource**
Options:

**•** Select an input variable or automatic output from a stage or step.

**•** Select a Decision element.

**•** Select a global variable.

**Operator** The available operators depend on the data type selected for `Resource` . See Flow Orchestration
Operators in Decision Elements.

```
Value

```

**Resource** and **Value** in the same row must have compatible data types.

Options:

**•** Select an orchestration resource, such as an input variable or automatic output from a stage
or step.

**•** Select a global variable.

**•** Manually enter a literal value.

When you add or subtract a number from a date value, the date adjusts in days, not hours.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Define Requirements for Stages and Steps in an Orchestration

Use requirements to resume an orchestration when a record changes. Define up to three
requirements to determine when a step is ready to start or when to mark an interactive step or
stage complete.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Before you begin, add a Stage element to your orchestration or a Step resource to a stage.

**1.** In the Properties panel, select the condition that allows you to create up to three requirements
to start a step or complete a stage or interactive step.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**2.** Set up the logic for the requirements.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**3.** Define up to three requirements.

A change to a record referenced in a requirement can trigger the orchestration to evaluate the status of the current stage and the
outstanding steps within it. Some requirement resources don’t trigger condition evaluations.

**Column Header** **Description**

**Resource**
Options:

**•** Select an orchestration resource

**–** Select a variable

**–** Select a record variable field

**–** Select automatic output from a step.

**•** Select a Stage element’s status

**•** Select a Step resource’s status.

**•** For record-triggered orchestrations, select the $Record global variable.

**•** Select a global variable.

**Operator** The available operators depend on the data type selected for **Resource** and work the same as
operators used for Decision elements. See Flow Orchestration Operators in Decision Elements.

**Value**

SEE ALSO:

**Resource** and **Value** in the same row must have compatible data types.

Options:

**•** Select an orchestration resource, such as a variable or automatic output from a step.

**•** Select a global constant

**•** Select a global variable.

**•** Manually enter a literal value.

When you add or subtract a number from a date value, the date adjusts in days, not hours.

Considerations for Orchestrations

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.244.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)_ : StandardObjectNameChangeEvent


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Assign an Interactive Step in an Orchestration

When you create an interactive step, you assign it to a user, group, or queue. A user can be an
internal user or a credentialed Experience Cloud site visitor. Groups or queues can include internal
users, credentialed Aura site visitors, or credentialed LWR site visitors. You can also assign an
interactive step to a resource that contains a username, group API name, or queue API name when
the orchestration runs. When the active screen flow associated with the interactive step runs, an
assigned user completes the flow on the related context record.

The User field for an interactive step’s assigned user includes internal users and credentialed
Experience Cloud site visitors. Whenever you assign an interactive step to a user or a credentialed
site visitor, ensure that they have the required access to the related record.

For an internal user to complete an interactive step, they must have access to the associated internal
Salesforce Lightning record page. For a credentialed Experience Cloud site visitor to complete an
interactive step, they must have access to the associated related record page in an Aura or LWR
site.

To use Omni-Channel routing with Flow Orchestration, set up Omni-Channel and associate at least
one queue with the Orchestration Work Item object. Then, to notify assigned users with the
Omni-Channel widget based on your defined routing logic, assign an interactive step to a queue
that’s associated with the Orchestration Work Item object.

**1.** Add an interactive step to a stage in your orchestration.

**2.** In the Properties panel for the interactive step, under Select Someone to Complete the Action,
select an assignment type.

**•** To specify a user, select **User** .

**•** To specify a regular public group, select **Group** .

**•** To specify a group that’s a queue, select **Queue** .

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To open, edit, or create an
orchestration in Flow Builder:

**•** Manage Flow

To complete assigned work
and resume a paused
orchestration

**•** Run Flows

**•** To specify a resource that contains a user’s username when the orchestration runs, select **User Resource** .

**•** To specify a resource that contains a group’s API name when the orchestration runs, select **Group Resource** .

**•** To specify a resource that contains a queue’s API name when the orchestration runs, select **Queue Resource** .

**3.** Specify the assigned user, group, or queue.

**•** If you selected User, search for the name of an internal user or a credentialed Experience Cloud site visitor, and select it from the
list.

**•** If you selected Group, search for a group’s label, and select it from the list.

**•** If you selected Queue, search for a queue’s label, and select it from the list.

**•** If you selected User Resource, specify the API name of the variable that contains the assignee’s username when the orchestration
runs.

Important: Don’t select $User for User Resource. The $User global variable evaluates to the system user when the orchestration
is running in system context and an interactive step can’t be assigned to the system user.

**•** If you selected Group Resource, specify the API name of the variable that contains the group API name when the orchestration
runs.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**•** If you selected Queue Resource, specify the API name of the variable that contains the assigned queue’s API name when the
orchestration runs.

SEE ALSO:

Flow Orchestration Interactive Steps

Running Context of an Orchestration

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Route Orchestration Work Items with Omni-Channel

To use Omni-Channel routing in Service Cloud with orchestration work items, you must have at
least one queue associated with the Orchestration Work Item. When you assign an interactive step
to that queue, members of the queue receive notifications via the Omni-Channel widget based on
your routing logic. Unless you disable default email notifications for work items, queue members
also receive email notifications.

When you assign an interactive step to a group or queue, each group or queue member receives
an email notification by default. The email notification contains a link to the record where one of
the members can complete the assigned work.

When a queue associated with the Orchestration Work Item object is assigned to an interactive
step, the work item owner is the queue.

**1.** [Set up Omni-Channel.](https://help.salesforce.com/s/articleView?id=sf.service_presence_intro.htm&language=en_US)

**2.** Associate a queue with the Orchestration Work Item object.

**3.** Assign an interactive step to a queue associated with the Orchestration Work Item object.

SEE ALSO:

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Redirect an Orchestration Path

Flow Orchestration uses Auto-Layout in Flow Builder. In Auto-Layout, elements on the canvas are
spaced and connected automatically. Use Go To connectors when you have elements that don’t
follow the usual consecutive auto-layout path.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

To add a Go To connector, you must have at least two elements in your orchestration.

**1.** Directly after the element that you want to change the connector for, click .

**2.** Click **Connect to element** .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To open, edit, or create an
orchestration in Flow Builder:

**•** Manage Flow

To complete assigned work
and resume a paused
orchestration

**•** Run Flows

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Build an Orchestration

**3.** Click on the element that you want to connect to.

The original element now has a dotted line connection to the specified element.

#### Add an End Element to an Orchestration Path

All elements in an orchestration are connected automatically or connected by Go To connectors
that you add manually. To finish a path in your orchestration, add an End element.

To add an End element, you must have at least one Decision element and two paths in your
orchestration.

**1.** After the last element in the path where you want to add the End element, click .

**2.** Select **End** .

The path now ends execution when this element is reached.

#### Use Automatic Output in Orchestrations

An orchestration has access to output for its stages, steps, and decisions. Query the status of any
stage or step in the orchestration. Use output parameters from any step’s associated flow. In an
orchestration configured to run on API version 58.0 and later, referenced automatic outputs that
contain a record or a record collection are refreshed with their latest values each time the
orchestration run resumes.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Add an element or resource to your orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

When you build an orchestration, automatic outputs for every stage and step in that orchestration are universally available. This universal
availability means that you can potentially use automatic output in your designed orchestration before it’s available in an orchestration
run. So, when using automatic output, consider the order in which an orchestration executes its elements and resources.

**1.** In a resource, value, or input parameter field, select a stage or step from the dropdown list.

**2.** Select the automatic output field from the dropdown list.

**3.** Save your work.

#### Trigger an Evaluation of Orchestration Stage and Step Conditions

Every time a step within the current stage completes, the orchestration evaluates the conditions for that stage and its steps. You can
also publish an orchestration event from a flow to trigger an evaluation of orchestration stage and step conditions.

SEE ALSO:

Publish an Orchestration Event


Automate Your Business Processes with Salesforce Flow Build an Orchestration

Integrate an Orchestration with External Systems

Add a MuleSoft step to your orchestration to call an imported MuleSoft action. You can also use the `$Orchestration.Instance`
system variable to integrate external systems with your orchestration.

##### Publish an Orchestration Event

To allow an external system to make a paused orchestration evaluate its stage and step conditions, publish an orchestration event
from a record-triggered orchestration.

SEE ALSO:

Flow Orchestration MuleSoft Steps

##### Publish an Orchestration Event Publish an Orchestration Event

To allow an external system to make a paused orchestration evaluate its stage and step conditions,
publish an orchestration event from a record-triggered orchestration.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Add a custom field to the object to hold an orchestration run ID.

Create an autolaunched flow with an input variable that accepts an orchestration run ID and passes
it to the action that invokes an external system.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Add logic at the end of the action invoking the external system. After the external system finishes
its task, it must update the custom orchestration run ID field on the affected record with the orchestration run ID it was passed.

Call the autolaunched flow from an asynchronous background step in an orchestration, and pass $Orchestration.Instance to the appropriate
input parameter.

**1.** Create a record-triggered flow that runs when the custom orchestrator run ID field is updated on a record. If you have records of
more than one object affected by an external system, create a record-triggered flow for each object.

**2.** Add a Create Records element to the record-triggered flow.

**3.** Enter a label, API name, and description for the element.

**4.** Select **Use separate resources, and literal values.**

**5.** For Object, search for and select _`Orchestration Event`_ .

**6.** For Field, enter _`Orchestration`_, and then select **OrchestrationInstanceId** .

**7.** For Value, enter _`$Record`_, and then select **$Record** . Then select the name of the custom orchestration run ID field on the triggering
record.

**8.** Click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**9.** Save and activate the new record-triggered flow.

SEE ALSO:

_[Extend Salesforce with Clicks, Not Code](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&language=en_US)_ : Create Custom Fields

_[Automate Your Business Processes](https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_variable.htm&language=en_US)_ : Flow Resource: Variable

#### Create an Orchestration Template

You can save a new or existing orchestration as a template, and then use it as a starting point for
creating other orchestrations in Flow Builder. You can also distribute the template via a managed
package so that subscribers can create orchestrations based on the template.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

**1.** To create an orchestration template from an orchestration:

**a.** Open an orchestration and click **Save As** .
The Save as dialog opens

.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**b.** Click **A New Orchestration** and enter a label, API name, and description for your orchestration template.

The description appears under the orchestration template’s name in the New Flow dialog and gives users information about
what your template does.

**c.** Click **Show Advanced** .

**d.** Select **Template** and click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**2.** To make an orchestration into a template.

**a.** Open an orchestration and click .
The Edit version properties dialog opens.

**b.** Ensure that the orchestration has a description.

The description appears under the orchestration template’s name in the New Flow dialog and gives users information about
what your template does.

**c.** Click **Show Advanced** .

**d.** Select **Template** and click **Done** .

**3.** To use the new template, select it in the New Flow dialog. .

**a.** In Setup, from the Flows listview, click **New Flow** .

**b.** In the New Flow dialog, click **All + Templates**, and then click **Flow Orchestration** .
The new orchestration template is shown in the Flow Orchestration category on the All + Templates tab of the New Flow dialog.

**c.** Select the new template and click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Make Work Accessible to Assigned Users

When an orchestration runs an interactive step, it emails a notification to the assigned user, group, or queue. Credentialed Experience
Cloud site visitors can see and access their assigned Flow Orchestration work items on the Orchestration Work Item List object page.
Internal users and credentialed Experience Cloud site visitors complete their assigned work in the Work Guide.

Add an Orchestration Work Item List Object Page to an Experience Cloud Site
Internal users can see and access their assigned work in the Flow Orchestration Work Items list view. Add the Orchestration Work
Item List object page to your Aura or LWR site so that credentialed site visitors can see and access their assigned Flow Orchestration
work items.

Add the Work Guide to a Record Page Layout
Add the Flow Orchestration Work Guide Lightning App Builder component to the page layouts for record types referenced by
interactive steps.

Add the Work Guide to an Experience Cloud Site
Add the Flow Orchestration Work Guide component to the related record page in your Aura and LWR sites for record types referenced
by interactive steps.

SEE ALSO:

Flow Orchestration Work Items


Automate Your Business Processes with Salesforce Flow Build an Orchestration

##### Add an Orchestration Work Item List Object Page to an Experience Cloud Site

Internal users can see and access their assigned work in the Flow Orchestration Work Items list view.
Add the Orchestration Work Item List object page to your Aura or LWR site so that credentialed site
visitors can see and access their assigned Flow Orchestration work items.

**1.** In Experience Builder, select **Pages** - **New Page** .

**2.** Select **Object Pages** .

**3.** In the New Object Pages dialog box, enter _`work item`_ in the Search box.

**4.** Select **Orchestration Work Item**, and click **Create** .

**5.** In the dialog box, click **Create** .

**6.** Select **Pages** - **Orchestration Work Item List** .

**7.** Preview and publish your site.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create an Experience
Cloud site:

**•** Create and Set Up
Experiences AND View
Setup and Configuration

To customize an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

**•** OR

**•** Be a member of the site
AND an experience
admin, publisher, or
builder in that site

To publish an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

**•** OR

**•** Be a member of the site
AND an experience
admin or publisher in
that site

To run a flow in an
Experience Builder site:

**•** Run Flows

Automate Your Business Processes with Salesforce Flow Build an Orchestration

##### Add the Work Guide to a Record Page Layout

Add the Flow Orchestration Work Guide Lightning App Builder component to the page layouts for
record types referenced by interactive steps.

**1.** To add the component to an existing page layout, on a page for a record type associated with
an interactive step, click, and then select **Edit Page** .

**2.** To create a page layout for a record type associated with an interactive step, from Setup, in the
Quick Find box, enter _`App Builder`_, and then select **Lightning App Builder** .

**a.** Click **New**

**b.** Select **Record Page**, and then click **Next** .

**c.** Give your record page a label, and then click **Next** .

The label can be up to 80 characters.

**d.** Select a page template, and click **Finish** .

**3.** Under Components, drag **Flow Orchestration Work Guide** onto the page layout.

If this page layout is new, add other components as needed.

**4.** Save your work.

**5.** If the page layout isn’t already activated, the Page Saved window appears and asks if you want
to activate the page.

Activate your orchestration.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

### Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

##### Add the Work Guide to an Experience Cloud Site

Add the Flow Orchestration Work Guide component to the related record page in your Aura and
LWR sites for record types referenced by interactive steps.

Your org must have Flow Orchestration enabled.

**1.** In Experience Builder, navigate to the related record page.

**2.** From the Components panel, drag **Flow Orchestration Work Guide** onto the page.

**3.** Save your work.

Add the Orchestration Work Item Object List page to your Aura or LWR site and ensure that the site
is published. Then activate the orchestration.

### Deploy an Orchestration

After you design and test your orchestration, it’s time to put it to work!


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create an Experience
Cloud site:

**•** Create and Set Up
Experiences AND View
Setup and Configuration

To customize an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

OR

**•** Be a member of the site
AND View Setup and
Configuration AND an
experience admin,
publisher, or builder in
that site

To publish an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

OR

**•** Be a member of the site
AND an experience
admin or publisher in
that site

Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

#### Set Up an Org-Wide Email Address

To receive emails from Flow Orchestration, create an org-wide email address.

Activate or Deactivate an Orchestration
You can have multiple versions of an orchestration in Salesforce, but only one version of each orchestration can be active at a time.
You can activate or deactivate an orchestration in Flow Builder or from the orchestration’s detail page in Setup.

Deploy Orchestrations with Change Sets
Create, test, and debug your orchestrations in a sandbox. Use a change set to send the orchestration and its associated flows to
production when you’re ready to deploy.

#### Set Up an Org-Wide Email Address

To receive emails from Flow Orchestration, create an org-wide email address.

The email address you set up in this step acts as the From address in your emails from Flow
Orchestration. If you don’t have a From address, your notification emails don’t send.

Note: If you have an existing org-wide email address, you don’t have to set up a new one,
but make sure you’ve specified it as your Email Approval Sender in Process Automation
Settings in Setup.

**1.** From Setup, in the Quick Find box, enter _`Email`_, and select **Organization-Wide Address** .

**2.** Select **Add** .

**3.** Fill in the Organization-wide address form.

**a.** For **Display Name**, enter a name that labels your org-wide address.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**b.** For **Email Address**, enter a company email address that can be used as the **From Address** in your email alert.

**c.** Select **Allow All Profiles to Use this From Address** .

**d.** Save your work.

**4.** View your org-wide address and the status, which reads **Verification Request Sent** .

**5.** Navigate to the email address you specified in the Email Address field.

**6.** When Salesforce sends an email to the company address you entered previously, approve and verify the company email address.

**7.** Navigate back to Salesforce, and check to make sure that the status of your address is **Verified** .

**8.** From Setup, in the Quick Find box, enter _`automation settings`_, and then select **Process Automation Settings.** .

**9.** For **Email Approval Sender**, specify your org-wide email address.

**10.** Save your changes.

Activate your orchestration.

Important: If the Sender Type is OrgWideEmailAddress, ensure that the user running the flow has the proper profile configurations
required by the specific org-wide email address being used. Proceeding without the proper configuration results in an error.


Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

#### Activate or Deactivate an Orchestration

You can have multiple versions of an orchestration in Salesforce, but only one version of each
orchestration can be active at a time. You can activate or deactivate an orchestration in Flow Builder
or from the orchestration’s detail page in Setup.

When you activate an orchestration version, the previously activated version, if one exists, is
deactivated. Any running orchestration continues to run using the version that it started with.

**1.** In Flow Builder, open the orchestration version.

#### 2. On the button bar, click Activate or Deactivate .

Deploy Orchestrations with Change Sets

Create, test, and debug your orchestrations in a sandbox. Use a change set to send the orchestration
and its associated flows to production when you’re ready to deploy.

**User Permissions Needed**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To activate or deactivate an
orchestration:

**•** Manage Flow

To activate a
record-triggered
orchestration:

**•** View All Data

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

To create, edit, or view processes:

To edit deployment connections:

Manage Flow

AND

View All Data

Deploy Change Sets

AND

Modify Metadata Through Metadata API
Functions

To use outbound change sets: Create and Upload Change Sets

To use inbound change sets: Deploy Change Sets AND Modify Metadata
Through Metadata API Functions

Create and upload the outbound change set in your sandbox, and deploy the inbound change set in production.


### Automate Your Business Processes with Salesforce Flow Orchestration Run

**1.** Ensure that all group names and queue names used in the source org to assign interactive steps to users duplicate the names used
in the target org.

**2.** Ensure that no interactive steps are directly assigned to a specific user.

**a.** Create constants for each assigned user who’s directly assigned to an interactive step in the orchestration.

**b.** Assign each interactive step to the appropriate assigned-user constant.

**3.** Activate your orchestration and all its referenced flows.

**4.** Create an outbound change set.

**5.** Add components to the new change set. These components include the orchestration, its associated flows, and any new custom
actions or new custom flow screen components that the associated flows depend on.

**6.** Upload your outbound change set.

**7.** Deploy your inbound change set in your target org.

**8.** Update any assigned-user constants in the orchestration, and save a new version of the orchestration.

**9.** Activate the new version of the orchestration.

Ensure that the page layouts for each context record referenced in the orchestration include the Orchestrator Work Guide Lightning
App Builder component.

SEE ALSO:

_[Sandboxes: Staging Environments for Customizing and Testing](https://help.salesforce.com/s/articleView?id=sf.changesets.htm&language=en_US)_ : Change Sets

### Orchestration Run

An orchestration run is created for each instance of an orchestration.

An _orchestration_ is an application built by your admin that uses stages, steps, and decisions to
organize a complex business process.An orchestration _run_ is a running instance of an orchestration.
The context an orchestration run uses depends on the orchestration type. You can also specify a
context with the How to Run the Orchestration advanced option.

Resuming a Failed Orchestration

If an orchestration run fails because of an error in an action called by one of its steps, you have up
to 14 days to fix the error in the action and resume the orchestration. If the orchestration run failed
because of some other type of error, it can’t be resumed. If the orchestration run failed but wasn’t
resumed within 14 days, it can no longer be resumed.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Orchestration Run

Statuses and Milestones

After it’s created, an orchestration run has an associated status.

In logging, an orchestration run has several milestones.


### Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

SEE ALSO:

Running Context of an Orchestration

### Manage Orchestrations and Work Items

### Manage orchestrations and work items with list views. Cancel or suspend a running orchestration.

Resume an orchestration run that failed within the previous 14 days because of an error in an action
or flow called by a step. Or resume an orchestration run that was manually suspended. Reassign
work items that have been assigned, but not completed.

View All Orchestration Work Items
Use the All Work Items list view to see all work items. Use the All Open Orchestration Work
Items list view to see all assigned but not completed work items. Assigned users can see and
access only their pending work items in the All Open Orchestration Work Items list view.

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

View Orchestration Work Items on a Record

Government Cloud Plus.

To see your assigned work items for a specific record, go to the associated record page. If you
have multiple work items assigned to you for that record, you can see them all in the
Orchestration Work Guide component. You can sort the work item list by last-modified date or select the item you want to complete
first. When you complete a work item, the work item list refreshes automatically.

View Orchestration Runs
Use the Orchestration Runs list view to see all in-progress, canceled, and completed orchestration runs in your org. Access orchestration
details and history through the orchestration runs list view.

Reassign an Orchestration Work Item
Reassign an assigned work item to a different user, group, or queue.

Disable Default Email Notifications for Work Item Assignments
By default, an orchestration sends an email notification when an orchestration work item is assigned or reassigned to a user, group,
or queue. Disable default work item notifications to stop sending emails to internal users and credentialed Experience Cloud site
visitors.

Suspend an In-Progress Orchestration
Suspend an orchestration run to wait until you’re ready to continue. When you suspend a running orchestration, the current stage
is also suspended. In-progress steps continue to run, but no new steps are started. If an in-progress step has output, it’s stored so it
can be processed when the orchestration is resumed.

Resume a Suspended Orchestration
Resume a suspended orchestration run to continue its processing. When a suspended orchestration run is resumed, the suspended
stage is also resumed. When the orchestration run is resumed, it evaluates the status of in-progress steps and updates the step status
where appropriate. Stored outputs from steps that were in progress when the orchestration run was suspended are processed.

Resume a Failed Orchestration
When an orchestration run failed within the previous 14 days because of an error in an action called by a step, you can fix the error
and resume the orchestration.


Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

Cancel a Running Orchestration
Cancel an in-progress orchestration from the orchestration runs list view.

Use Orchestration Reports
Use sample flow orchestration reports to track orchestration usage. Sample reports include Orchestration Runs, Orchestration Stage
Runs, Orchestration Step Runs, Orchestration Work Items, and Orchestration Run Logs. These sample reports are based on the
Orchestration Runs Spring ’24, Orchestration Stage Runs Spring ’24, Orchestration Step Runs Spring ’24, Orchestration Work Items
Spring ’24, and Orchestration Run Logs Spring ’24 custom report types.

Orchestration Statuses and Milestones
Each part of an orchestration has a status assigned when an orchestration runs.

View All Orchestration Work Items

Use the All Work Items list view to see all work items. Use the All Open Orchestration Work Items
list view to see all assigned but not completed work items. Assigned users can see and access only
their pending work items in the All Open Orchestration Work Items list view.

**1.** In the App Launcher, find and select **Orchestration Work Items** .

**2.** To see assigned and completed orchestration work items, from the dropdown list, select **All**
**Work Items** .

**3.** To see assigned orchestration work items, from the dropdown list, select **All Open Work Items** .

**4.** To see an assigned work item on its associated record page, click the assigned work item record
in the list view.

Note: Only the assigned user or a member of the assigned group or queue can see an
assigned work item on its associated record page.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To view all orchestration
work items:

**•** View access is based on
sharing settings

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

View Orchestration Work Items on a Record

To see your assigned work items for a specific record, go to the associated record page. If you have
multiple work items assigned to you for that record, you can see them all in the Orchestration Work
Guide component. You can sort the work item list by last-modified date or select the item you want
to complete first. When you complete a work item, the work item list refreshes automatically.

Assigned orchestration work items are shown in the Work Guide on the record page of their
associated record.

**1.** Go to a record that you have assigned work items for.

**2.** To sort orchestration work items in the Work Guide, click and then select how you want
to sort your assigned work.

**3.** To filter displayed orchestration work items in the Work Guide, click, and enter the term to
search for.
The Word Guide lists only those work items with labels that include the specified search term.

**4.** To complete a work item:

**a.** In the Work Guide, click for the item you want to complete.
The screen flow opens in the Work Guide.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To run a flow:

**•** Run Flows

**b.** After you’ve finished the screen flow, click **Finish** .
The work item status is set to Completed, and you’re returned to the refreshed list of work items in the Work Guide.

**c.** If you select an item that you don’t want to complete, click, and then click **OK** .
You return to the list of work items in the Work Guide.

SEE ALSO:

Make Work Accessible to Assigned Users

#### View Orchestration Runs

Use the Orchestration Runs list view to see all in-progress, canceled, and completed orchestration
runs in your org. Access orchestration details and history through the orchestration runs list view.

**1.** In the App Launcher, find and select **Orchestration Runs** .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To view orchestration runs:

**•** View access is based on
sharing settings

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**2.** To see details for a specific orchestration run, on the All Orchestration Runs list view, click the link for an orchestration, and then click
the **Related** tab.

**3.** To see the full orchestration run history, under **Orchestration Run Log**, click **View All** .

##### Add Comments to the Orchestration Run Log

Add custom comments to the Orchestration Run Log using variables in flows called by orchestration steps.

Add a Comments Column to the Orchestration Run Log
Add comments from flows called by orchestration steps to the Orchestration Run Log to customize log information.

##### Add Comments to the Orchestration Run Log

Add custom comments to the Orchestration Run Log using variables in flows called by orchestration
steps.

**1.** In a flow called by an orchestration step, add a variable named Comments.

**a.** For Resource Type, select **Variable** .

**b.** For API name, enter _`Comments`_ .

**c.** For Description, enter _`Stores custom text to be added to the`_
_`Comments field in the Flow Orchestration Log`_ .

**d.** Select **Available for output** .

**e.** For Data Type, select **Text** .

**2.** In an Assignment element in your flow, set the `Comments` variable to a string.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

##### Add a Comments Column to the Orchestration Run Log

Add comments from flows called by orchestration steps to the Orchestration Run Log to customize
log information.

**1.** From the Orchestration Run List View, click and select **Edit Object** .

**2.** In the Orchestration Run setup page, click **Page Layouts**, and select **Orchestration Instance**
**Layout** .

**3.** In the Related Lists section, click the for Orchestration Run Log.

**4.** In the Related List Properties - Orchestration Run Log window, under Available Fields, select
**Comments** and click .
The Comments field is added to the Selected Fields list.

**5.** To change the Comments field’s location in the Orchestration Run Log, use the up and down
arrows.

**6.** Click **OK**, and then click **Save** .

Reassign an Orchestration Work Item

Reassign an assigned work item to a different user, group, or queue.

You can reassign an assigned work item for an orchestration that’s still in progress.

**1.** In the App Launcher, find and select **Orchestration Work Items** .

**2.** On the All Open Work Items page, from the dropdown for the assigned work item, select
**Reassign Orchestration Work Item** .

**3.** In the Reassign Orchestration Work Item window, select the user, group, or queue to reassign
the work item to.

**4.** Click **Reassign Orchestration Work Item** .

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To reassign a work item

**•** Reassign Orchestration
Work Items

OR

**•** Manage Orchestration
Runs and Work Items

To complete assigned work

**•** Run Flows

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Disable Default Email Notifications for Work Item Assignments

By default, an orchestration sends an email notification when an orchestration work item is assigned
or reassigned to a user, group, or queue. Disable default work item notifications to stop sending
emails to internal users and credentialed Experience Cloud site visitors.

**1.** From Setup, in the Quick Find box, enter _`process automation`_, and then select **Process**
**Automation Settings** .

**2.** On the Process Automation Settings page, select **Stop Sending Orchestration Work Item**
**Default Email Notifications** .

#### Suspend an In-Progress Orchestration

Suspend an orchestration run to wait until you’re ready to continue. When you suspend a running
orchestration, the current stage is also suspended. In-progress steps continue to run, but no new
steps are started. If an in-progress step has output, it’s stored so it can be processed when the
orchestration is resumed.

You can suspend only an in-progress orchestration.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the in-progress orchestration, select
#### Suspend . 3. Click Suspend .

When you’re ready, resume the orchestration run.

SEE ALSO:

Resume a Suspended Orchestration


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To edit process automation
settings:

**•** Customize Application

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Resume a Suspended Orchestration

Resume a suspended orchestration run to continue its processing. When a suspended orchestration
run is resumed, the suspended stage is also resumed. When the orchestration run is resumed, it
evaluates the status of in-progress steps and updates the step status where appropriate. Stored
outputs from steps that were in progress when the orchestration run was suspended are processed.

You can resume a suspended orchestration or an orchestration that failed within the previous 14
days because of an error in an action or flow called by a step.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the suspended orchestration, select
#### Resume . 3. Click Resume . Resume a Failed Orchestration

When an orchestration run failed within the previous 14 days because of an error in an action called
by a step, you can fix the error and resume the orchestration.

You can resume a failed orchestration if it failed within the previous 14 days because of an error in
an action called by a step.

Remember to fix the error in the called flow or action before resuming the failed orchestration run.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the orchestration with a status of Error,
#### select Resume . 3. Click Resume .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Cancel a Running Orchestration

Cancel an in-progress orchestration from the orchestration runs list view.

You can only cancel an in-progress orchestration.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the in-progress orchestration, select
#### Cancel . 3. Click Cancel .

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)

#### Use Orchestration Reports

Use sample flow orchestration reports to track orchestration usage. Sample reports include
Orchestration Runs, Orchestration Stage Runs, Orchestration Step Runs, Orchestration Work Items,
and Orchestration Run Logs. These sample reports are based on the Orchestration Runs Spring ’24,
Orchestration Stage Runs Spring ’24, Orchestration Step Runs Spring ’24, Orchestration Work Items
Spring ’24, and Orchestration Run Logs Spring ’24 custom report types.

Note: Orchestration reports aren’t added to your org when it has the maximum number of
defined custom reports.

Note: If a sample report is deleted, you can’t regenerate it.

Sample orchestration reports are public reports. The reports only show work items assigned directly
to a user. To view work assignments for the groups or queues the user belongs to, change the filter
to view all work items assigned to the user’s groups or queues.

**1.** In the Reports list view, click **Public Reports** .

**2.** In the Search public reports box, enter _`orchestration`_ .
The five sample orchestration reports are listed.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To cancel a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create, edit, and delete
reports in public and private
folders:

**•** Report Builder

OR

**•** Report Builder (Lightning
Experience)

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**3.** To customize a sample report, edit the desired report.

SEE ALSO:

_Salesforce Help_ [: Build a Report in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.reports_build_lex.htm&language=en_US)

_Salesforce Help_ [: What are some common report limits?](https://help.salesforce.com/s/articleView?id=sf.faq_reports_common_limits.htm&language=en_US)

#### Orchestration Statuses and Milestones

Each part of an orchestration has a status assigned when an orchestration runs.

Orchestration Details

The orchestration details page gives the status of an orchestration that’s currently running.

#### Orchestration Status

When an orchestration runs, it can be completed, it can be canceled, it can end due to an error
with a flow, or it can remain in progress. Orchestration stages, steps, and work items statuses are
situation-dependent.

**Statuses of Items in a Completed Orchestration**

**Statuses of Items in a Canceled Orchestration**


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**Statuses of Items in an Orchestration Stopped by Orchestration Error**

**Statuses of Items in an Orchestration Stopped by Stage Error**

**Statuses of Items in an Orchestration Stopped by Interactive Step Error**


Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

Note: These statuses apply when the interactive step fails. When the screen flow associated with the interactive step fails, the
status for running stage and failed step is In Progress and the status for not started work items is Assigned.

**Statuses of Items in an Orchestration Stopped by Background Step Error**

Orchestration Run Milestones

When an orchestration runs, it logs milestones to the orchestration history.


### Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations Troubleshoot Orchestrations

To troubleshoot a failed orchestration run, use the orchestration fault email. To test an orchestration
and observe what happens as it runs, use the debug option.

#### Emails about Orchestration Errors

When an orchestration run fails, Salesforce sends an error email. The email is sent to either the
admin who last modified the associated orchestration or the Apex exception email recipients.

Debug an Orchestration
You can view debug information for in-progress and failed orchestrations.

#### Emails about Orchestration Errors

When an orchestration run fails, Salesforce sends an error email. The email is sent to either the
admin who last modified the associated orchestration or the Apex exception email recipients.

The email includes the error message with details about the:

**•** Orchestration

**•** Executed orchestration elements

**•** Flows called from orchestration steps

For activated orchestrations, the error email also has a link to show the failed orchestration run
details in Flow Builder.

If an orchestration fails because of a flow it calls, then the recipients receive an error email for the
orchestration failure and an error email for the flow failure.

Example:

```
   Error element Stage_1 (FlowOrchestratedStage).

   An error occurred when executing a flow interview.

   Flow Details

   Flow API Name: Create_Customer_Record

   Type: Orchestrator

   Version: 1

   Status: Inactive

```


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

```
      Org: signup.org.test.1640285093849 (00DRM000000G0SV)

      Flow Interview Details

      Interview Label: Create New Customer 2/11/2022, 1:57 PM

      Interview GUID: 1fb36a45416070aa772cba20517eea2a1236-7f18

      Current User: Test User (005RM0000025zTa)

      Start time: 2/11/2022, 1:57 PM

      Duration: 3 seconds

      How the Interview Started

      Orchestration Run ID: 0jERM0000004CQT

      Test User (005RM0000025zTa) started the flow interview.

      API Version for Running the Flow: 54

      ENTER STAGE: Stage 1

      ID: 0jFRM0000004CQY

      Status: Error

      BACKGROUND STEP: Create Account for New Customer

      ID: 0jLRM0000004Cfd

      Status: Error

      Entry Condition:

      When the stage starts, the step starts = true

      Flow (Create_Account_for_New_Customer)

      Inputs:

      None.

      Outputs:

      None.

      Error Occurred: An error occurred when executing a flow interview.

      Salesforce Error ID: 904995012-1848 (1749972898)

#### Debug an Orchestration

```

You can view debug information for in-progress and failed orchestrations.

How Does Debugging Work for Orchestrations?

View debug details in Flow Builder for only in-progress and failed orchestrations runs. View debug
details in error emails for failed flows.

Note: When an orchestration fails, it doesn’t necessarily roll back record additions, changes,
or deletions that were made before the orchestration failed. As a result, we recommend that
you design and debug your orchestration in a sandbox environment before deploying it to
production.

The debug information for in-progress and failed orchestrations is similar to the information displayed
for flow. In addition, orchestration debug details show milestones for orchestrations, stages, steps,
and work items.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

Milestones

Orchestration milestones are a part of orchestration debugging details.

Stage milestones are a part of orchestration debugging details.

Step milestones are a part of orchestration debugging details.


Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

Work item milestones are a part of orchestration debugging details.

Debug an In-Progress Orchestration
Debug an in-progress orchestration to better understand the path an orchestration takes with different scenarios and the variable
values at points in the automation

Debug a Failed Orchestration
Troubleshoot a failed orchestration, and gain insights about why it failed. You can debug a failed orchestration within 14 days of it
failing.


Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

##### Debug an In-Progress Orchestration

Debug an in-progress orchestration to better understand the path an orchestration takes with
different scenarios and the variable values at points in the automation

Sharing must be enabled for orchestration runs and flow interviews.

**•** The orchestration run to be debugged must be shared with the user.

**•** The flow interview associated with the orchestration run to be debugged must be shared with
the user.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the desired in-progress orchestration,
select **Debug Orchestration** .

Note: If you started running an orchestration before upgrading to Spring ’22, stage and
step instance IDs are shown as null in orchestration debug information. Evaluation flow
output is also shown as null.

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)

##### Debug a Failed Orchestration

Troubleshoot a failed orchestration, and gain insights about why it failed. You can debug a failed
orchestration within 14 days of it failing.

**1.** From Setup, in the Quick Find box, enter, and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the desired failed orchestration, select
##### Debug .

Note: If you started running an orchestration before upgrading to Spring ’22, stage and
step instance IDs are shown as null in orchestration debug information. Evaluation flow
output is also shown as null.

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To access the debug action
for a running orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To debug a failed
orchestration:

**•** Manage Flow

Automate Your Business Processes with Salesforce Flow Flow Orchestration Limits and Considerations

Flow Orchestration Limits and Considerations

When designing, managing, and running orchestrations, consider these issues.

General Flow Orchestration Limits
When using orchestrations, keep orchestration limits, flow limits, and Apex governor limits in
mind.

Considerations for Orchestrations
Keep these considerations in mind when designing and using orchestrations.

Considerations for Evaluation Flows
Keep these considerations in mind when using evaluation flows as entry or exit conditions.

Security Considerations for Orchestrations
When designing orchestrations, keep these security considerations in mind.

General Flow Orchestration Limits

When using orchestrations, keep orchestration limits, flow limits, and Apex governor limits in mind.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**Per-Org Limit**

**Enterprise,**
**Unlimited,**
**Performance,**
**or Developer**
**Editions**

Versions per orchestration 50

Active flows plus orchestrations 2,000

Total flows plus orchestrations 4,000

SEE ALSO:

_[Automate Your Business Processes](https://help.salesforce.com/s/articleView?id=sf.flow_considerations_usage_entitlements.htm&language=en_US)_ : Flow Usage-Based Entitlements

_Sales Productivity_ [: Email Allocations per Edition](https://help.salesforce.com/s/articleView?id=sf.allocations_email_general.htm&language=en_US)

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_event_limits.htm)_ : Platform Event Allocations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Limits and Considerations

#### Considerations for Orchestrations

Keep these considerations in mind when designing and using orchestrations.

Entry and Exit Condition Requirements

Resources selected for a requirement for a step entry condition or a stage or step exit condition can
contain orchestration resources or global variables. There are limitations for what can be included
in a requirement.

**•** To use a record for the Resource or Value fields, you must select a field on the record.

**•** The referenced record must use fields from its object, not fields from a related record.

Record-Change-Triggered Flow Orchestration Events

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

A requirement for a step entry condition or a stage or step exit condition can contain a reference
to a record. Changes to that record can trigger the orchestration to evaluate the status of the current stage and the outstanding steps
within it. There are limitations for when the record can trigger condition evaluations.

**•** The referenced record’s parent object must support change events.

**•** The referenced record fields aren’t IsDeleted, SystemModeStamp, or any field that’s derived from a related record or a formula.

**•** The referenced record is null or has an invalid ID.

**•** The referenced record is a global variable in an autolaunched orchestration.

**•** The referenced record is a global variable other than $Record in a record-triggered orchestration.

Input Values for Flows

If the combined input values for a flow called by an orchestration step is more than 32,768 characters, the orchestration fails. This error
can be caused by passing one or more records to a flow called by a step. To avoid this error, pass a record ID to the referenced flow, and
use a Get Records element in the flow with the passed ID. Using a passed ID with a Get Records element also means that you always
have the latest version of the record.

Email Notifications

When a flow called by a step fails and causes an orchestration to fail, two email notifications are sent.

**•** A flow error notification

**•** An orchestration error notification

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)_ : StandardObjectNameChangeEvent


Automate Your Business Processes with Salesforce Flow Flow Orchestration Entitlements

#### Considerations for Evaluation Flows

Keep these considerations in mind when using evaluation flows as entry or exit conditions.

An evaluation flow is a flow with a process type of Evaluation Flow. It’s an autolaunched flow that
contains a predefined Boolean output variable named `isOrchestrationConditionMet` .

General Guidelines

Use an evaluation flow to pause an orchestration until a specific field update occurs.

Don’t loop through records or make external callouts in evaluation flows.

To pass variables from the orchestration into an evaluation flow, use evaluation flow input variables.

Output Variable

An evaluation flow has one output variable named `isOrchestrationConditionMet` .

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

The `isOrchestrationConditionMet` output variable must be Boolean and initialized to false.

The values of all output variables other than `isOrchestrationConditionMet` are discarded and not used by the orchestration.

#### Security Considerations for Orchestrations

When designing orchestrations, keep these security considerations in mind.

Shield Platform Encryption

For enhanced security, enable Shield Platform Encryption for the `Screen Flow Inputs` field
of the `Flow Orchestration Work Item` object.

SEE ALSO:

_Salesforce Help_ [: Strengthen Your Data's Security with Shield Platform Encryption](https://help.salesforce.com/s/articleView?id=sf.security_pe_overview.htm&language=en_US)

Flow Orchestration Entitlements

Flow Orchestration has usage-based entitlements. An orchestration _run_ is a running instance of an
orchestration. An _orchestration_ is an application built by your admin that uses stages, steps, and
decisions to organize a complex business process.

Flow Orchestration is automatically enabled for the editions listed in the Required Editions table.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Reference

Bookmark this page for quick access to information about orchestration elements, resources, events,
and more.

Flow Orchestration Resources
Each _resource_ represents a value that you can reference throughout the orchestration.

Flow Orchestration Elements
Each _element_ represents an action that the orchestration can execute. Orchestrations can contain
Decision and Stage elements.

Flow Orchestration Connectors
_Connectors_ determine the available paths that an orchestration can take at run time. On the
canvas in Flow Builder, a connector looks like an arrow that points from one element to another.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Flow Orchestration Operators
In conditions and filters, operators let you evaluate information and narrow the scope of an orchestration operation.

Flow Orchestration Version Properties
An orchestration version’s properties consist of its label and description. These values drive the field values that appear on the
orchestration’s detail page.

Flow Orchestration Resources

Each _resource_ represents a value that you can reference throughout the orchestration.

In Flow Builder, the Manager tab shows the resources that are available in the orchestration.

You can create some resources by clicking **New Resource** . The system providers certain resources,
such as global constants and global variables. Other resources are created when you add an element
to an orchestration. For example, when you add a Decision element, a resource for each decision
outcome is created.

#### **Resource Description Creatable from**

**the Resources Tab**

Constant Store a fixed value that you can use throughout an
orchestration.

Decision When you add a Decision element to an orchestration, its
Outcome outcomes are available as Boolean resources. If an outcome


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Resource** **Description** **Creatable from the**
**Resources Tab**

path has already been executed in the running orchestration, the resource’s value is
`True` .

```
Element

```

Any element that you add to an orchestration is available as a resource with the `was`
`visited` operator in decision outcome criteria. An element is considered visited
when it’s executed in a running orchestration.

Formula Calculate a value when the formula is used in the orchestration.

Flow Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .
Orchestration
Resource:
Global
ConstantsGlobal
Constant

Global Variable Use system-provided variables that reference information about the Salesforce org
or running user, such as the user’s ID or the API session ID.

Flow Organize the work done in an orchestration stage.
Orchestration
Resource: Step

Text Template Store text that can be changed and used throughout the orchestration. To format the
text, use HTML tags.

Variable Store a value that can be changed throughout the orchestration.

Flow Orchestration Resource: Constant
Store a fixed value that you can use throughout an orchestration.

Flow Orchestration Resource: Formula
Calculate a value when the formula is used in the orchestration.

Flow Orchestration Resource: Global Constants
Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .

Flow Orchestration Resource: Global Variables
Use system-provided variables that reference information about the Salesforce org or running user, such as the user’s ID or the API
session ID.

Flow Orchestration Resource: Step
Organize the work done in an orchestration stage.

Flow Orchestration Resource: Text Template
Store text that can be changed and used throughout the orchestration. To format the text, use HTML tags.

Flow Orchestration Resource: Variable
Store a value that can be changed throughout the orchestration.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Resource: Constant

Store a fixed value that you can use throughout an orchestration.

**Field** **Description**

```
API Name

```

The requirement for uniqueness applies only to elements within the
current orchestration. Two elements can have the same API name,
provided they’re used in different orchestrations.An API name can include
underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two
consecutive underscores.

`Description` Helps you differentiate the constant from other resources.

`Data Type` Determines the type of value that the constant can store. You can’t change
the data type of a previously saved constant.

`Value` The constant’s value. This value doesn’t change throughout the
orchestration.

Flow Orchestration Resource: Formula

Calculate a value when the formula is used in the orchestration.

**Field** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within
the current orchestration. Two elements can have the same API
name, provided they’re used in different orchestrations. An API
name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

`Description` Helps you differentiate this formula from other resources.

`Data Type` The data type for the value returned by the formula. You can’t
change the data type of a previously saved variable.

```
Decimal Places

##### `Formula`

```

Controls the number of digits to the right of the decimal point up
to 17 places. If you leave this field blank or set it to zero, only whole
numbers appear when your orchestration runs.

Available only when the data type is Number or Currency.

The formula expression that the orchestration evaluates at run
time. The returned value must be compatible with `Data Type` .

Some formula functions aren’t supported in Flow Builder.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Resource: Global Constants

Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .

Example: When you create a Boolean variable, `$GlobalConstant.True` and
`$GlobalConstant.False` are supported. When you create a Currency variable, no
global constants are supported.

Null Versus Empty String

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

At run time, `{!$GlobalConstant.EmptyString}` and `null` are treated as separate, distinct values. For example:

**•** When you leave a text field or resource value blank, the value is `null` at run time. If you want the value to be treated as an empty
string, set it to `{!$GlobalConstant.EmptyString}` .

**•** For an orchestration condition, use the `is null` operator to check whether a value is `null` . If the condition compares two text
variables, make sure that their default values are correctly set to `{!$GlobalConstant.EmptyString}` or left blank ( `null` ).

Flow Orchestration Resource: Global Variables

Use system-provided variables that reference information about the Salesforce org or running user,
such as the user’s ID or the API session ID.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Global Variable Considerations for Flows

**•** In a record-triggered orchestration, the `$Record` global variable doesn’t contain the triggering record’s values for fields whose
values are derived from other records. Examples of derived fields include `Contact.Name` and `User.MediumPhotoUrl` .

**•** Multi-select picklist, time, and location global variables are available only in formulas.

**•** If a field in the database has no value, the corresponding merge field returns a blank value. For example, if no value is set for your
org’s Country field, `{!$Organization.Country}` returns no value.

Flow Orchestration Resource: $Flow Global Variables
###### A $Flow global variable provides information about the running orchestration. Some variables contain system-provided values.

You can update the other variables throughout the orchestration by storing output values in the variables.

###### Flow Orchestration Resource: $Flow Global Variables

###### A $Flow global variable provides information about the running orchestration. Some variables

contain system-provided values. You can update the other variables throughout the orchestration
by storing output values in the variables.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**Global Variable**

**Supported** **Description** **Value Set By**
**Resource**
**Types**

###### $Flow.ActiveStages Stage $Flow.CurrentDate Text, Date, and

Date/Time

A collection of stages that are Assignment
relevant to the current path of the
flow.

This system variable references the
flow Stage resource, not the

orchestration Stage element. It can
only be used in flows, including
those flows called by an
orchestration step, but it isn’t
supported for orchestrations.

Date when the flow interview System
executes the element that
references the global variable.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Global Variable** **Supported** **Description** **Value Set By**
**Resource Types**

`$Flow.CurrentRecord` Text

`$Flow.CurrentStage` Stage

ID of a related record. The value must be a single Assignment
ID for a valid object. All custom objects and most
standard objects are valid.

When a user pauses the flow interview or the
interview executes a Wait element, the interview

is associated with this record by creating a
FlowRecordRelation record. If the ID isn’t valid,
the interview fails to pause.

The currently selected stage. Assignment

This system variable references the flow Stage
resource, not the orchestration Stage element.

It can only be used in flows, including those
flows called by an orchestration step, but it isn’t
supported for orchestrations.

`$Flow.CurrentDateTime` Text, Date, and Date and time when the flow interview executes System
Date/Time the element that references the global variable.

`$Flow.FaultMessage` Text System fault message that can help flow System
administrators troubleshoot runtime issues.

`$Flow.InterviewGuid` Text Unique identifier for the interview. System

`$Flow.InterviewStartTime` Text, Date, and Date and time when the flow interview started. System
Date/Time For a flow launched by a Subflow element,

`$Flow.InterviewStartTime` indicates
when the initial parent flow started.

Flow Orchestration Resource: Step

Organize the work done in an orchestration stage.

Orchestrations have background steps and interactive steps.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Background Steps

Background steps call autolaunched flows and run without user interaction.

**Field** **Description**

`Label` Helps you identify the element on the canvas.

`API Name` Automatically populated if empty when you fill out the `Label` field and
press TAB.The requirement for uniqueness applies only to elements within

the current orchestration. Two elements can have the same API name,


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

provided they’re used in different orchestrations. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and can’t end with an underscore.
It also can’t have two consecutive underscores.

```
   Description
```

Helps you remember what this resource does. When editing an element, appears after you click .

`Condition` Identifies the method used to determine whether a step is ready to start.

`Step Name` Specifies a step that must be marked complete before the current step can start. Available when the
entry condition is set to When another step is marked complete the step starts.

`Evaluation Flow` Specifies the flow that determines if the step can start. Available when the entry condition is set to
When the specified evaluation flow returns True, the step starts.

`Flow` Specifies which autolaunched flow to run for a step.

Interactive Steps

Interactive steps call screen flows and require user interaction.

**Field** **Description**

`Label` Helps you identify the element on the canvas.

`API Name` Automatically populated if empty when you fill out the `Label` field and press TAB.The requirement
for uniqueness applies only to elements within the current orchestration. Two elements can have the

same API name, provided they’re used in different orchestrations.An API name can include underscores
and alphanumeric characters without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

```
   Description
```

Helps you remember what this resource does. When editing an element, appears after you click .

`Condition` Identifies the method used to determine whether a step is ready to start or can be considered complete.

`Step Name` Specifies a step that must be marked complete before the current step can start. Available when the
entry condition is set to When another step is marked complete the step starts.

`Evaluation Flow` Specifies the flow that determines if the step can start or be marked complete. Available when the
entry condition is set to When the specified evaluation flow returns True, the step starts. Also available

when the exit condition is set to When the specified evaluation flow returns True, the step is marked
Completed.

`Flow` Specifies which screen flow to run for a step.

`Record ID` Specifies the ID of the record where the Work Guide displays the screen flow to the assigned user.

`Username` Specifies the user assigned to complete the screen flow.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Step Status

Flow Orchestration Resource: Text Template

Store text that can be changed and used throughout the orchestration. To format the text, use
HTML tags.

**Field** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within the current
orchestration. Two elements can have the same API name, provided they’re
used in different orchestrations.An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate this text template from other resources.

##### Text Template The text for the template. To reference information from other resources,

use merge fields.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

Rich Text

Plain Text

Control the text font, size, color, and alignment. Add HTML links, bullet points, or numbered lists. Rich

text is on by default. To change to rich text, click .

Send email core actions use plain text. Some custom actions from AppExchange or built by Salesforce

developers also expect plain text. To change to plain text, click .

Flow Orchestration Resource: Variable

Store a value that can be changed throughout the orchestration.

**Field** **Description**

`Apex Class` Defines fields for the Apex-defined data type. Only fields with the
@AuraEnabled annotation are available in an orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within the
current orchestration. Two elements can have the same API name,
provided they’re used in different orchestrations. An API name can include
underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two
consecutive underscores.

`Description` Helps you differentiate this variable from other resources.

```
Data Type

```

Determines the types of values that the variable can store. You can’t
change the data type of a previously saved variable.

The Record data type can store multiple field values for one record. The
Apex-defined data type can store multiple field values for one Apex class.

Looking for sObject? In Flow Builder, that data type changed to Record.

`Allow multiple` When selected, the resource is a collection variable. You can store a list
`values` of values in collection variables. Collection variables can store only values
`(collection)` that are compatible with their data type. When the data type is Record,
the collection variable can only store values for the associated object’s
records.

For example, store multiple email addresses in a collection variable, and
reference the collection variable to send an email.

```
Object

```

The object whose field values you can store in the variable. You can’t
change the object of a previously saved variable.

Available only when the data type is Record.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

```
Decimal Places

Availability Outside

the Flow

Default Value

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your orchestration runs.

Available only when the data type is Number or Currency.

When a variable is available for input, it can be set at the start of the orchestration, such as when an
orchestration is started from a Lightning page.

Disabling input or output access for an existing variable can break the functionality of applications
and pages that call the orchestration and access the variable. For example, you can access variables
from URL parameters, processes, and other flows.

This field doesn’t affect how variables are assigned or used within the same orchestration.

Determines the variable value when the orchestration starts. If you leave this field blank, the value is
`null` .

Not available for Picklist and Multi-Select Picklist variables.

Flow Orchestration Elements

Each _element_ represents an action that the orchestration can execute. Orchestrations can contain
##### Decision and Stage elements.

In Flow Builder, the Add Element menu shows the types of elements that you can add to the flow
by selecting them. For a list of all elements already added to the orchestration, see the Elements
section of the Manager tab in the Toolbox.

Flow Orchestration Element: Decision
Evaluate a set of conditions, and then route users through the orchestration based on the
outcomes of those conditions. This element performs the equivalent of an if-then statement.

Flow Orchestration Element: Stage
Group a series of related steps in an orchestration.

Flow Orchestration Element: Decision

Evaluate a set of conditions, and then route users through the orchestration based on the outcomes
of those conditions. This element performs the equivalent of an if-then statement.

Outcomes

For each path that the orchestration can take, create an outcome. For each outcome, specify the
conditions that must be met for the orchestration to take that path. To relabel the path that the
flow takes if no outcome’s conditions are met, click **Default Outcome** .

**Field** **Description**

`Label` Identifies the connector for this outcome on the canvas.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

`Outcome API` The requirement for uniqueness applies only to elements within the current orchestration. Two elements can
`Name` have the same API name, provided they’re used in different orchestrations.An API name can include underscores
and alphanumeric characters without spaces. It must begin with a letter and can’t end with an underscore. It
also can’t have two consecutive underscores.

`Condition` Determines whether the orchestration takes this outcome’s path. Sets logic and conditions for each outcome
`Requirements` that determine if the orchestration follows its path.

```
   to Execute

   Outcome

```

`When to` Available on record-triggered orchestrations. Determines whether this outcome’s path is taken based on
`Execute` whether the triggering record is updated to meet the condition requirements. For example, the opportunity
`Outcome` update that triggered the orchestration to run changed its stage to Closed Won from any value that isn’t Closed
Won.

Flow Orchestration Element: Stage

Group a series of related steps in an orchestration.

##### Stages run sequentially, one stage at a time, and contain steps.

Note: The Stage element in Flow Orchestration isn’t related to the Stage resource in Flow
Builder.

**Field** **Description**

`Label` Identifies the name for this stage on the canvas.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

Set Exit

Condition

```

The requirement for uniqueness applies only to elements within the current
orchestration. Two elements can have the same API name, provided they’re
used in different orchestrations. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and can’t
end with an underscore. It also can’t have two consecutive underscores.

Determines when a stage can be considered complete.

**When all steps have been marked Complete, the stage is marked**
**Complete**
The stage is marked complete and the orchestration moves to the next
element when every step in a stage is marked complete.

**When the specified evaluation flow returns True, the stage is marked**
**Complete**
The orchestration runs a specified evaluation flow to determine if the stage
can be marked complete. The orchestration doesn’t mark the stage complete
and move to the next element until the specified evaluation flow’s
`isOrchestrationConditionMet` output variable returns true.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Stage Status

Flow Orchestration Connectors

#### Connectors determine the available paths that an orchestration can take at run time. On the canvas

in Flow Builder, a connector looks like an arrow that points from one element to another.

**Label** **Example** **Description**

_Unlabeled_ Identifies which element to execute next.

_`Decision`_ Identifies which element to execute when
_`outcome`_ the criteria of a Decision outcome are met.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

_Go To_

Identifies which element to go to and
execute next. Use to create loops in an
orchestration.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Operators

In conditions and filters, operators let you evaluate information and narrow the scope of an
orchestration operation.

Flow Orchestration Operators in Decision Elements
Use condition operators to verify the value of a selected resource. Conditions are used in Decision
elements.

Flow Orchestration Operators in Decision Elements

Use condition operators to verify the value of a selected resource. Conditions are used in Decision
elements.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource.

**•** Apex-Defined

**•** Boolean

**•** Collection

**•** Currency

**•** Date

**•** Date/Time

**•** Multi-Select Picklist

**•** Number

**•** Picklist

**•** Record

**•** Text

Apex-Defined

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

To determine which operators are supported, match the _`@AuraEnabled`_ attribute’s Apex data type with the Flow Orchestration data
type in this reference.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Boolean

Check whether a Boolean resource’s value matches another value or resource.

Collection

Check whether a Collection resource’s value contains or matches another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Currency and Number

Check whether a Currency or Number resource’s value matches, is larger than, or is smaller than another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Date and Date/Time

Check whether a Date or Date/Time resource’s value matches, is before, or is after another value or resource.

Picklist

Check whether a Picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Multi-Select Picklist

Check whether a multi-select picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value. If the resource’s value includes multiple items, the operators treat
the value as one string that happens to include semicolons. It doesn’t treat each selection as a different value. For example, the
operators treat `red; blue; green` as a single value rather than three separate values.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Record

Check whether a record resource’s value matches another value or resource.

Text

Check whether a Text resource’s value matches, contains, ends with, or starts with another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


## Automate Your Business Processes with Salesforce Flow Suggest Options to Users with Recommendation Strategies

Flow Orchestration Version Properties

An orchestration version’s properties consist of its label and description. These values drive the field
values that appear on the orchestration’s detail page.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

## Suggest Options to Users with Recommendation Strategies

Display the right recommendations to the right people at the right time with Einstein Next Best
Action. Create and display offers and actions for your users that are tailored to meet your unique
criteria. Develop a strategy that applies your business logic to refine those recommendations. Your
strategy distills your recommendations into a few key suggestions, like a repair, a discount, or an
add-on service. Display the final recommendations in your Lightning app or Experience Builder site.

Note: Where possible, we recommend building strategies in Flow Builder using the
Recommendation Strategy flow type, but you can also create them in Strategy Builder.

Get Started with Einstein Next Best Action
Just getting started with Einstein Next Best Action? Follow these steps to complete each phase
of the Next Best Action setup process, create personalized recommendations for your users,
and put decisions into action.

Einstein Next Best Actions Considerations
Keep these considerations in mind when working with strategies and recommendations.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Einstein Next Best Action Entitlements
Einstein Next Best Action has usage-based entitlements. All orgs receive a free monthly allowance of Next Best Action requests. If
your usage exceeds your allowance of free monthly requests or any entitlements that you purchase, Salesforce contacts you to
discuss additions to your contract. To track your usage, from Setup, navigate to **Company Information** .


### Automate Your Business Processes with Salesforce Flow Get Started with Einstein Next Best Action

Create Recommendations
Create offers or actions to recommend to users using Einstein Next Best Action. Recommendations are standard Salesforce records,
similar to accounts and contacts, that are processed by strategies and associated with flows. Strategies determine which
recommendation records are surfaced using business rules, predictive models, and other data sources. The result of this process is
context-specific recommendations that you present to your users.

Building a Strategy
A strategy determines when and how to present an Einstein Next Best Action recommendation on a Salesforce Lightning record
page. For example, if you want to offer a discount to a subset of customers, create a strategy that collects the appropriate customer
records and identifies the discount option to present. To create a strategy, you can use Flow Builder (recommended) or Strategy
Builder.

Display Recommendations
After creating a strategy, choose a page to run your strategy and display your recommendations. You can use a Lightning record
page, an app’s home page, an Experience Cloud site page, a Visualforce page, or an external site, depending on where you want
recommendations to appear.

Report On and Track a Recommendation
Create a custom report type to report on and track recommendation data and strategy metrics. You can see the monthly total
recommendations that a Salesforce org’s strategies served. And you can analyze which recommendations are accepted and rejected,
who responds to them, and more.

SEE ALSO:

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

### Get Started with Einstein Next Best Action

Just getting started with Einstein Next Best Action? Follow these steps to complete each phase of
the Next Best Action setup process, create personalized recommendations for your users, and put
decisions into action.

Einstein Next Best Action is a solution that uses flows, strategies, and the Recommendation object
to recommend actions to users. You can display these recommendations on many different types
of pages, including Lightning pages in your Salesforce org, Experience Cloud sites, or external sites.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Get Started with Einstein Next Best Action

Recommendations are displayed to users with the option to accept or reject the recommended action. Each recommendation contains
an image, important text values such as button text and a description, and an assigned flow that runs when a user responds. They can
be stored and referenced in the Recommendation standard object, or they can be manually assembled when building a strategy.

Strategies determine which recommendations to display to users, based on your data and business processes. When you set up Einstein
Next Best Action on a page, you assign a strategy to that location, which then defines the recommendations that appear there.

You can control which recommendations are displayed in any situation, even if your org has a large number of recommendation records.
Strategies can filter recommendations based on any available value, including recommendation fields, fields related to the running user,
and fields related to the record that’s currently displayed.

Important: In Flow Builder, you define which recommendations are displayed by making sure that they’re in the
outputRecommendations collection variable at the end of the flow. In Strategy Builder, you define which recommendations are
displayed by making sure that they’re not filtered out when they reach the Output element.

**1.** Plan Your Recommendations and Automation

Decide where the recommendation appears, who it appears to, and the conditions in which it appears. Create a plan for the automation
that you want to run when a user accepts the recommendation.

**2.** Build a Flow

In Flow Builder, design and build the flow that runs when a user accepts or rejects the recommendation. You can assign only screen
flows and autolaunched flows to a recommendation. If an inactive or invalid flow is assigned, the recommendation isn’t displayed
to users.

**3.** Create Recommendations

Recommendations are standard Salesforce records, similar to accounts and contacts. To create recommendations, you can:

**•** Create recommendation records on the Recommendation object.

**•** Build recommendations from other data when creating your strategy. In Flow Builder, use the Recommendation Assignment
element or a custom Apex invocable action.

**•** [Generate recommendations automatically through AI with Einstein Recommendation Builder.](https://help.salesforce.com/s/articleView?id=sf.custom_ai_recommendation_builder.htm&language=en_US)

**4.** Create a Strategy

After you create a flow and make a plan for your recommendation records, use Flow Builder or Strategy Builder to create your strategy.
Where possible, we recommend building strategies in Flow Builder using the Recommendation Strategy flow type, but you can also
create them in Strategy Builder.

Some features can be used only in strategies created in Strategy Builder.

**•** Limiting repeated showings of some recommendations

**•** Displaying recommendations on an Experience Cloud site or external site

**•** Displaying AI-generated recommendations from Einstein Recommendation Builder

To build a strategy in Flow Builder, follow these steps.

**a.** Go to the Flows page in Setup, and click `New Flow` .

**b.** Select **Use a Template**, and then click **Next** .

**c.** Select the **Recommendation Strategy** flow type, and then click **Create** .

**d.** To retrieve data from Salesforce records, such as the Recommendations object or an object related to the currently displayed
record, add Get Records elements. To filter which recommendations are stored in the element’s collection, use condition
requirements in the Get Records element. Or you can build recommendations from other data with the Recommendation
Assignment element or a custom Apex invocable action.


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**e.** To limit the number of recommendations that users see, add logic elements. Use Collection Sort and Collection Filter elements
to arrange and reduce the recommendations from the Get Records collection. If needed, you can also add other Flow elements
such as Decision and Loop to create more complex, branching logic.

**f.** To set recommendations in the `outputRecommendations` collection, add the Assignment element. When running a
strategy built in Flow Builder, Einstein Next Best Action displays only recommendation records in the
`outputRecommendations` collection.

**5.** Display Next Best Actions

After creating a strategy, choose a page to run your strategy and display your recommendations. You can use a Lightning record
page, an app’s home page, an Experience Cloud site page, a Visualforce page, or an external site, depending on where you want
recommendations to appear.

**•** Einstein Next Best Action Component

Use the Einstein Next Best Action component to display recommendations to users on most Lightning pages within your
Salesforce org, including record pages, home pages, and app pages.

**•** [Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

Use the Suggested Actions component to display recommendations on Experience Cloud sites. This component can run only
strategies created in Strategy Builder.

SEE ALSO:

Build a Flow

Create Recommendations

Strategy Builder Strategies

Display Recommendations

Launch a Flow When a Recommendation Is Accepted or Rejected

Einstein Next Best Action Component

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

### Einstein Next Best Action Examples

These examples walk you through the process of creating Einstein Next Best Action components.


EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

#### Offer a Gift Basket to Each Account

Use a Next Best Action component on the Lightning Account record page to offer a gift basket to
each of your accounts. When a customer accepts the offer, a form opens to collect the recipient’s
name and shipping address. After the form is submitted, a request email is sent to the shipping
department.

To configure this Einstein Next Best Action recommendation:

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**1.** Create an action flow on page 753 that executes when the gift basket recommendation is accepted.

**2.** Create a recommendation on page 755 that specifies how to present the gift basket offer.

**3.** Create a recommendation strategy flow on page 756 that determines when and how the recommendation is presented.

**4.** Add a Next Best Action component on page 757 that displays the recommendation on the Account record page and executes the
strategy.

Create an Action Flow

Create a flow that collects the recipient’s name and address and sends an email to the shipping department.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start From Scratch** and then click **Next** .

**3.** Select the **Screen** flow type and then click **Create** .

**4.** To collect the recipient’s name and address, add a Screen element to the flow.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**a.** Enter a label and API name.

**b.** Drag the **Name** and **Address** components to the canvas and assign an API name to each.

**c.** Click **Done** .

**5.** To create the text of the email message to send to the shipping department, click **New Resource** in the Flow Builder Toolbox. If the
toolbox isn’t visible, toggle the toolbox icon in the upper left corner of the Flow Builder canvas.

**a.** Add a Text Template resource type.

**b.** Enter _`EmailBody`_ as the API name.

**c.** In the Body area, enter the email text, inserting the name and address resources.

**d.** Click **Done** .

**6.** To create a task for the shipping department, click below the Screen element and add an Action element to the flow.

**a.** In the Action dropdown list, enter _`Send Email`_ and select the **Send Email** action.

**b.** Enter a label and API name.

**c.** For Body, select the **EmailBody** text element.

**d.** Enter a subject line.

**e.** For Recipient Email Addresses (comma-separated), select **Include** and add the email address of the shipping department.

**f.** To allow rich text formatting for the message, select Include and select the **True** global constant.

**g.** Set any other values as needed.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**h.** Click **Done** .

**7.** Save the flow and name it _`Gift Basket Offer`_ .

**8.** Activate the flow.

**9.** To return to the Flows page, click **Back** .

Create a Recommendation Record

Create a recommendation that specifies how to present the gift basket offer.

**1.** From the App Launcher ( ), in the Quick Find box, enter _`Recommendations`_, and select **Recommendations** .

**2.** Click **New** .

**3.** Enter a name and description for the recommendation.

The description appears in the Next Best Action component on the Lightning record page.

**4.** For **Action**, select the action flow that you created.

**5.** To add an image (optional), click **Upload Image** and follow the instructions.

For best results, use a 1000 px x 380 px image at 72 dpi or one with a similar ratio.

**6.** Enter text for the acceptance and rejection buttons.

**7.** Select the target audiences for the recommendation.

**8.** Click **Save** .

The Is Action Active checkbox is automatically selected, which makes the recommendation available to Einstein Next Best Action.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

Create a Recommendation Strategy Flow

The recommendation strategy flow determines when and how the recommendation is presented.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Use a Template** and then click **Next** .

**3.** Select the **Recommendation Strategy** flow type and then click **Create** .

**4.** To specify which records to use for the recommendation, add a Get Records element to the flow.

**a.** Enter a label and API name.

**b.** Select the **Account** object.

**c.** In the Filter section, add the condition _`Id equals recordId`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

**5.** To load possible recommendations into the strategy, add a Get Records element.

**a.** Enter the label _`Get Gift Recommendation`_ and the API name. _`Get_Gift_Recommendation`_ .

**b.** Select the **Recommendation** object.

**c.** In the Filter section, add the condition _`Name contains Gift Basket`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

In Flow Builder, you define which recommendations are displayed by making sure that they’re in the outputRecommendations
collection variable at the end of the strategy flow. The next step uses the Assignment element to add the recommendations to
outputRecommendations. To learn how to use the Limit Repetition element to assign the outputRecommendation variable while
also limiting the number of times that the user sees the recommendation, see Create Recommendations Based on Customer
Satisfaction Scores on page 758.

**6.** To move the recommendation output out of this flow so it becomes available to Einstein Next Best Action, click **+** below the
Recommendation Assignment element and add an Assignment element.

**a.** Enter a label and API name.

**b.** For Variable, select **outputRecommendations** .

**c.** For Operator, select **Equals** .


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**d.** For Value, select **Recommendations from Get Gift Recommendation** .

**e.** Click **Done** .

**7.** Save the flow and name it _`Gift Strategy`_ .

**8.** Activate the flow.

**9.** To return to the Flows page, click **Back** .

Display the Next Best Action Recommendation

Display the Next Best Action recommendation on the Account record page.

**1.** Open an Account record page.

**2.** Click the Setup icon ( ), and select **Edit Page** .

**3.** Drag the Einstein Next Best Action component to the desired location on the page layout.

**4.** Add _`Gift Basket Offer`_ as the component title.

**5.** For Strategy Source, select **Flow Builder** and then select the name of the recommendation strategy.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**6.** Save your changes.

**7.** Return to the Account record and refresh the page.

The recommendation is displayed. If the account rep clicks **Yes**, a form opens with entries for name and address. Completing the form
generates an email request for the shipping department to fulfill the order.

#### Create Recommendations Based on Customer Satisfaction Scores

This example lets a customer service or account rep base a Next Best Action recommendation on
whether a customer has a high or low customer satisfaction (CSAT) score. For customers with a low
CSAT, a rep can offer the customer a discount on their service contract renewal. For customers with
a high CSAT score, the rep can offer a new product preview.

Preparation

To record customer satisfaction scores and use them to determine which recommendation to
display, this example includes two custom fields. To follow along with the example, set up these
two fields before you begin.

Contact object custom field:

**•** Field Label: CSAT score

**•** API Label: CSAT_score

**•** Field type: Number (length 2, decimal places 0)

Recommendation object custom field:

**•** Field Label: Category

**•** API Label: category_c

**•** Field type: Text (length 18)

To set up these Next Best Action recommendations:

**1.** Create action flows on page 759 for the high and low CSAT recommendations.

**2.** Create recommendation records on page 759 for the high and low CSAT recommendations.

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**3.** Create a strategy flow on page 760 that determines how the recommendations are presented to the customer service or account
rep.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**4.** On the Contact record page, add the Next Best Strategy component on page 763 that displays the recommendations and executes
the strategy.

Create Action Flows

Create two simple screen flows, one to execute an action for the low CSAT recommendation and one to execute an action for the high
CSAT recommendation.

This example keeps things simple by displaying a different text message for each recommendation but not incorporating other automation.
For a real-world application, you can add additional elements to implement the service contract discount and the new product preview.
For an example of using an action flow to send an email request, see Offer a Gift Basket to Each of Your Accounts on page 753.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start from Scratch**, and then click **Next** .

**3.** Select **Screen Flow**, and then click **Create** .

**4.** Add a Screen element to the flow.

**5.** Enter a label and API name.

**6.** Drag a **Display Text** component to the canvas.

**7.** Enter an API name for the component.

**8.** Add text for the high or low CSAT recommendation.

**9.** Click **Done**

**10.** Save the flow and name it _`CSAT Action Flow - Discount`_ or _`CSAT Action Flow - Product Preview`_ .

**11.** Activate the flow.

**12.** Repeat these steps to create the second action flow.

Create Recommendation Records

Create records for the low CSAT and high CSAT recommendations.

**1.** From the App Launcher ( ), in the Quick Find box, enter _`Recommendations`_, and select **Recommendations** .

**2.** Click **New** .

**3.** Enter a name and description for the recommendation.

The description appears in the Next Best Action component on the Lightning record page. Make the description specific to the
particular recommendation (low CSAT or high CSAT).


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**4.** For **Action**, select the low CSAT or high CSAT action flow.

**5.** To add an image (optional), click **Upload Image** and follow the instructions.

For best results, use a 1000 px x 380 px image at 72 dpi or one with a similar ratio.

**6.** Enter text for the acceptance and rejection buttons.

**7.** Select the target audiences for the recommendation.

**8.** Click **Save** .

The Is Action Active checkbox is automatically selected, which makes the recommendation available to Einstein Next Best Action.

**9.** Repeat these steps to create the second recommendation record.

Create a Recommendation Strategy Flow

The recommendation strategy flow specifies when and how the recommendations are presented on the Contact record page.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Click **Use a Template**, and then click **Next** .

**3.** Click **Recommendation Strategy**, select a template, and then click **Create** .

**4.** Load the Contact records that you want to use for your recommendations by adding a Get Records element to the flow.

**a.** Enter a label and API name.

**b.** Select the **Contact** object.

**c.** In the Filter section, add the condition _`Id equals recordId`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

**5.** To accommodate different recommendations based on the customer’s CSAT score, add a decision step after the Get Records step.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**a.** Enter the label _`CSAT Score?`_ and the API name _`CSAT_score`_ .

**b.** Create a _`Low CSAT`_ outcome with the condition that the value of the CSAT Score field on the Contact record is 3 or lower.

**c.** Create a _`High CSAT`_ outcome with the condition that the value of the CSAT Score field on the Contact record is 4 or higher.

**d.** Keep the Default outcome as-is for customers who don’t have a CSAT score.

**e.** Click **Done** .

**6.** Bring in the appropriate recommendation for the low and high CSAT conditions by adding a Get Records element for each.

**a.** Enter a label and API name.

**b.** Select the **Recommendation** object.

**c.** In the Filter section, add the appropriate condition by selecting the API name of the Category field in the Recommendation
object and specifying the low or high condition.

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**7.** To show the recommendation only one time for each Account record and to assign the flow output, add a Limit Repetition element
for the low and high score paths.

**a.** Enter a label and API name.

**b.** For Recommendation Collection, select the low score or high score recommendation.

**c.** For Look for These Records, select **Accepted or Rejected** .

**d.** For Look for This Many Messages, keep the default setting of _`1`_ .

**e.** To make the output from this path available to Next Best Action, click **Advanced**, select **Manually assign variables**, and then
select **outputRecommendations** .

**f.** Click **Done** .

**8.** Save the flow and name it _`CSAT Strategy Flow`_ .


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Actions Considerations

**9.** Activate the flow.

**10.** To return to the Flows page, click **Back** .

Display the Next Best Action Recommendations

To make the recommendations available to the customer service or account rep, display the Next Best Action component on the Contact
record page.

**1.** Open a Contact record page.

**2.** Click the Setup icon ( ), and select **Edit Page** .

**3.** Drag the Einstein Next Best Action component to the desired location on the page layout.

**4.** Add _`CSAT Recommendations`_ as the component title.

**5.** For Strategy Source, select **Flow Builder** and then select the name of the recommendation strategy.

**6.** Save your changes.

**7.** Return to the Contact record and refresh the page.

Based on the contact’s CSAT score, the correct recommendation is displayed. When the customer accepts the offer and the account rep
clicks **Yes I Accept**, a form opens with the appropriate confirmation message.

### Einstein Next Best Actions Considerations

Keep these considerations in mind when working with strategies and recommendations.

Einstein Next Best Action relies on flows, recommendations, strategies, and components, and has
standard objects for reporting.

Flows

**•** All Recommendation objects reference a flow. If you don’t have any flows, you can’t surface a
recommendation.

**•** Strategies only load recommendations with active flows.

**•** When a flow is executed via REST API, the flow runs in the context of the user who is
authenticated via REST API. The running user’s profile and permission sets determine the object


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Actions Considerations

permissions and field-level access of the flow. We recommend that you create a profile and permission sets for users who run the
flow.

Recommendations

**•** Consider adding a custom category field to the recommendation object and layout. A category field gives you more control when
loading, sorting, and filtering recommendations and more options when creating flows.

**•** Create names, descriptions, acceptance labels, and rejection labels that are appropriate for your intended audience.

**•** Reusing a recommendation name creates a recommendation. It doesn’t overwrite an existing recommendation. Duplicated names
can cause strategies to display duplicate recommendations to customers.

**•** All flows, both inactive and active, display in the Action dropdown list. After you save your recommendation, you can see if the flow
is active.

**•** You can create a recommendation based on a flow that isn’t active, but no strategy loads it until the flow is activated.

Strategies

**•** All strategies require at least one recommendation.

**•** In Strategy Builder, you can load and filter the records of a Recommendation object. Or load and filter the records of any object, and
convert them into recommendations at the end of the strategy using the Map element.

**•** Load elements require at least one criteria.

**•** Strategies only load recommendations that are based on active flows.

**•** The Limit Reoffer element in Strategy Builder lets you hide a recommendation from all users based on its responses. A recommendation
is hidden if users respond more than a defined number of times within a defined number of days. For limit reoffers to work,
recommendations must have a unique record ID. If you want to continue to test a recommendation as a flow-entry point, delete
individual records from the Recommendations Reaction table with Rest API calls:

```
     GET /connect/recommendation-strategies/reactions

     { onBehalfOf: “005B00000018jK4IAI” }

     //Returns a list of reactions

     //For each result, if the reaction matches the strategyId of the strategy you’re testing:

     DELETE /connect/recommendation-strategies/reactions/${reactionId}

```

**•** Strategy Builder is available only in Lightning Experience.

Tracking and Reporting Reactions

**•** For strategies created in Flow Builder, create custom report types using the Recommendation Strategy Metrics and Recommendation
Responses primary objects. For strategies created in Strategy Builder, create custom report types using the Recommendation Strategy
Metrics and Recommendation Reactions primary objects.

**•** For reports created from the Recommendation Reactions primary object to correctly display the recommendation source name and
ID for limit reoffers, recommendations must have a unique record ID.


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Entitlements

```
   Rights of ALBERT EINSTEIN are used with permission of The Hebrew University of Jerusalem.

   Represented exclusively by Greenlight.

```

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Write a Strategy Builder Expression

_Apex Reference Guide_ [: NextBestAction Class](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_static_methods)

### Einstein Next Best Action Entitlements

Einstein Next Best Action has usage-based entitlements. All orgs receive a free monthly allowance
of Next Best Action requests. If your usage exceeds your allowance of free monthly requests or any
entitlements that you purchase, Salesforce contacts you to discuss additions to your contract. To
track your usage, from Setup, navigate to **Company Information** .

Note: Next Best Action entitlement usage is based on a rolling 30-day period, beginning
when the org is created. Entitlement usage listed on the Company Information page in Setup
is based on the calendar month's usage, not the rolling 30-day usage.

Einstein Next Best Action is automatically enabled for the editions listed in the Required Editions
table.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Entitlements

#### Next Best Action Request

A _request_ is a call to the Next Best Action engine that causes a strategy to run and return recommendations.

#### Next Best Action Request

A _request_ is a call to the Next Best Action engine that causes a strategy to run and return
recommendations.

Each time a page with an Einstein Next Best Action component is loaded or refreshed in a browser,
Salesforce generates a new request. For example, when a case status changes from New to In
Progress, the data change on the page triggers a refresh. This action also applies to the Actions &
Recommendations and Suggested Actions components.

Requests are also made when:

**•** A field is updated on a record detail page that includes the Next Best Action component.

**•** A user enters data in the Subject or Description field of a site contact support page that includes
the Next Best Action component.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Another way to make a request is to call a Next Best Action REST API resource from your own web app. You can also call Next Best Action
REST API resources from an iOS or an Android app. The app can make requests in response to a custom UI and return recommendations.

Paying customers can see the number of requests their org has made by navigating from Setup to **Company Information**, **Usage-based**
**Entitlements**, **Maximum Next Best Action Requests available** .

SEE ALSO:

Display Recommendations

Einstein Next Best Action Entitlements


### Automate Your Business Processes with Salesforce Flow Create Recommendations Create Recommendations

Create offers or actions to recommend to users using Einstein Next Best Action. Recommendations
are standard Salesforce records, similar to accounts and contacts, that are processed by strategies
and associated with flows. Strategies determine which recommendation records are surfaced using
business rules, predictive models, and other data sources. The result of this process is context-specific
recommendations that you present to your users.

Note:

**•** Salesforce has both a Recommendation object for Einstein Next Best Action (that’s this
page) and a Recommendation component for Experience Builder sites. The
Recommendation component isn’t related to Next Best Action.

**•** If you don't see Recommendations in the App Launcher, in Setup, select Default On in
the Recommendations tab settings for your user profile or permission set.

**•** You can load and filter the records of a Recommendation object. Or load and filter the
records of any object, and convert them into recommendations at the end of a strategy
using the Map element.

Before creating recommendations, create the action flow that runs when a customer accepts the
recommendation. For examples of action flows for Next Best Action, see Einstein Next Best Action
Examples on page 752.

**1.** In the Recommendations tab, click **New Recommendation** .

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage
recommendations:

**•** Modify All Data

OR

Manage Next Best
Action
Recommendations

**2.** Enter a friendly name (1) and a brief description (2) for your recommendation. The description appears on the recommendation that
is surfaced to users.

**3.** Optionally, click to upload an image (3) that you can display as a header for your recommendation. For best results, use a 1000 by
380 pixel image at 72 DPI, or an image with a similar ratio. You can choose whether the image displays using component properties.
After it’s uploaded, a thumbnail of your image displays on the Recommendations page. Customers can see the full image as a header
for your recommendation in either the Lightning App Builder or Experience Builder component.

**4.** Enter an acceptance label (4) and a rejection label (5) for the buttons that customers click to, respectively, accept and reject the
recommendation.

**5.** Create a flow. When a user accepts your recommendation, they’re taken to the flow specified in Action (6).


Automate Your Business Processes with Salesforce Flow Create Recommendations

**6.** Choose the flow that runs when a customer accepts the recommendation (6) and click **Save** . You can also choose a flow that runs
when a customer accepts or rejects the recommendation. The Action list displays both active and inactive flows. Choosing a flow
that isn't active hides the recommendation. When you’ve saved your recommendation, you can see if the flow is active from **Is**
**Action Active** (7).

**7.** Create a recommendation strategy in Strategy Builder that determines how your recommendations surface.

**8.** Optionally add a custom Category field to the Recommendation object and the Recommendation Layout. Adding a custom Category
field can simplify loading, filtering, and sorting recommendations in Strategy Builder.

Recommendation Fields
Recommendations are suggested actions that users see and interact with through Einstein Next Best Action strategies. When creating
a recommendation, use these fields to define its look and feel.

Launch a Flow When a Recommendation Is Accepted
Each recommendation is associated with a single flow. By default, Next Best Action launches a flow when a user accepts a
recommendation. The flow then performs an action, such as updating a case or sending an email.

Launch a Flow When a Recommendation Is Accepted or Rejected
Each recommendation is associated with a single flow. By default, Next Best Action launches a flow when a user accepts a
recommendation. The flow then performs an action, such as updating a case or sending an email. But you can also launch a flow
when a user rejects a recommendation, which gives you more flexibility. For example, a flow could run an automated process, write
to another system, or create a reminder email when a recommendation is rejected.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Add a Limit Repetitions Element to a Next Best Action Flow
You can add a Limit Repetitions element to your Recommendation Strategy flow to limit the number of times that the same
recommendation or offer appears on the same record or for the same user during a time period.

SEE ALSO:

Build a Flow

Strategy Builder Strategies

Display Recommendations

[View and Edit Tab Settings in Permission Sets and Profiles](https://help.salesforce.com/s/articleView?id=sf.users_tab_visibility.htm&language=en_US)

Get Started with Einstein Next Best Action

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

#### Recommendation Fields

Recommendations are suggested actions that users see and interact with through Einstein Next
Best Action strategies. When creating a recommendation, use these fields to define its look and
feel.

You can use these methods to create recommendations.

**•** Assemble recommendations as needed in Flow Builder or Strategy Builder.

**•** Create recommendations as standard Salesforce records, similar to accounts and contacts, in
the Recommendation object. You can create recommendation records on the Recommendations
tab in the App Launcher.

**•** [Generate recommendations automatically through AI with Einstein Recommendation Builder.](https://help.salesforce.com/s/articleView?id=sf.custom_ai_recommendation_builder.htm&language=en_US)

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Image (1)—The image that is shown in the recommendation. To display this image with the Einstein Next Best Action Lightning
page component, select `Show Image` when configuring the Lightning page component.

**•** Name (2)—The header text at the top of the recommendation. To display this text with the Einstein Next Best Action Lightning page
component, select `Show Title` when configuring the Lightning page component.

**•** Description (3)—Additional descriptive text displayed in the recommendation. To display this text with the Einstein Next Best Action
Lightning page component, select `Show Description` when configuring the Lightning page component.

**•** Acceptance Label (4)—The text of the button that accepts the recommendation. This option is always displayed.

**•** Rejection Label (5)—The text of the button that rejects the recommendation. To display this option with the Einstein Next Best
Action Lightning page component, select `Show Reject Option` when configuring the Lightning page component.

Use these fields to define how the recommendation runs.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Action

The flow that runs when a user selects the Accept option. To run this flow when the user accepts or rejects the recommendation, select
`Launch Flow on Rejection` when configuring the Einstein Next Best Action Lightning page component. If the referenced
flow is inactive, invalid, or has an unsupported Flow Type, the recommendation isn’t displayed to users. The supported flow types are
screen flows and autolaunched flows.

SEE ALSO:

Create Recommendations

Get Started with Einstein Next Best Action

#### Launch a Flow When a Recommendation Is Accepted

Each recommendation is associated with a single flow. By default, Next Best Action launches a flow
when a user accepts a recommendation. The flow then performs an action, such as updating a case
or sending an email.

For example, on a case, display a recommendation to the service agent to upsell a premium service
to the customer. When the agent accepts the recommendation, an autolaunched flow updates the
case and the customer’s order history and sends a receipt via email.

Or say that you have an autolaunched flow that sends a templated marketing campaign email to
a customer. Your service agents have to determine whether your customers are eligible for this
campaign. Doing so involves several clicks and complex calculations. Instead use Next Best Action
to check the customer’s eligibility and prompt the agent to accept the recommendation and launch
the flow.

**1.** In Flow Builder, configure a flow that’s associated with a recommendation. Be sure to activate
the flow because Next Best Action can’t call an inactive flow from a recommendation.

**2.** Add a flow action.

**3.** To add the flow, edit the recommendation.

SEE ALSO:

#### Launch a Flow When a Recommendation Is Accepted or Rejected


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Create Recommendations

#### Launch a Flow When a Recommendation Is Accepted or Rejected

Each recommendation is associated with a single flow. By default, Next Best Action launches a flow
when a user accepts a recommendation. The flow then performs an action, such as updating a case
or sending an email. But you can also launch a flow when a user rejects a recommendation, which
gives you more flexibility. For example, a flow could run an automated process, write to another
system, or create a reminder email when a recommendation is rejected.

For example, at a telecommunications company, the admin configures the Next Best Action
component to display recommendations to its customer service representatives (CSRs). When a
CSR accepts a recommendation for a customer who wants to purchase a discounted service, a flow
is launched to calculate the discount. The admin analyzes the reactions to the recommendation,
and is confused about why the CSRs are rejecting it. To help get answers, the admin uses Next Best
Action to launch a questionnaire flow every time the recommendation is rejected.

This feature is available for:

**•** The Einstein Next Best Action component used with Lightning record pages

**•** The Suggested Actions component used in Experience Builder

**•** The Actions and Recommendations component used with Lightning console apps

To assign a flow that runs when a customer accepts or rejects the recommendation, create an input
variable in the flow to accept the `isRecommendationAccepted` value. Then add a Decision
element to the flow that’s based on that value.

**1.** In Flow Builder, configure a flow that’s associated with a recommendation. Be sure to activate
the flow because Next Best Action can’t call an inactive flow from a recommendation.

**2.** Create the Boolean `isRecommendationAccepted` input variable.

**3.** Create a Decision element and use the `isRecommendationAccepted` variable in your
outcome conditions.

**4.** Create a decision outcome for what the flow does when the recommendation is accepted.

**5.** Create a decision outcome for what the flow does when the recommendation is rejected.


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Create Recommendations

**6.** Add any additional flow elements to handle each outcome path.

**7.** Add a flow action.

**8.** To add the flow, edit the recommendation.

**9.** When you add the Next Best Action component to a Lightning record page, select **Launch Flow on Rejection** .


Automate Your Business Processes with Salesforce Flow Create Recommendations

SEE ALSO:

Launch a Flow When a Recommendation Is Accepted

Flow Resource: Variable

Flow Element: Decision

Einstein Next Best Action Component


Automate Your Business Processes with Salesforce Flow Create Recommendations

#### Add a Limit Repetitions Element to a Next Best Action Flow

You can add a Limit Repetitions element to your Recommendation Strategy flow to limit the number
of times that the same recommendation or offer appears on the same record or for the same user
during a time period.

**•** You must have a collection of recommendations that has a valid value in the ID or
RecommendationKey fields. The RecommendationKey value must be a database ID or have
the syntax _`DYNAMIC_<custom id>`_ .

**•** If you include an Assignment element, from Actions, choose **Output from limit** . Or you can
skip this step and add the output from the Limit Repetitions element.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, and then select **Flows** .

**2.** Open or create a Recommendation Strategy.

**3.** After the collection of recommendations, add a Limit Repetitions element.

**4.** Enter a label and an API Name.

**5.** Add a description.

**6.** Search for and select the Recommendation Collection that you want to filter.

**7.** Select the responses that you want, and then enter the number of responses and days as whole
numbers.

Look Within This Many Days is based on days, not hours. If the number of days is set to 1 for an
accepted response, and the user accepts the recommendation at any time on Monday, the
recommendation doesn’t display again until the start of Wednesday. So a one-day time period
could be as few as 25 hours in duration or as many as 48 hours.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage
recommendations:

**•** Modify All Data

OR

Manage Next Best
Action
Recommendations

**8.** If you didn’t include an Assignment element, you can search for and select the collection that includes the limit repetition output.

**a.** In Advanced, select **Manually assign variables** .

**b.** From the Store Output Variables field, search for and select the output variable.

**9.** Click **Done** .

**10.** Save your work.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Example:

**•** If you want one accepted response over 90 days, such as a password reset recommendation, and the user accepts one time
over 90 days, they don’t see the message again for 90 days. But if the user rejects the recommendation, they see the message
every time they reload the page until they accept it.

**•** If you want two accepted or rejected responses over 1 day, and a user accepts or rejects the recommendation only one time
every day, they still see the recommendation.

**•** If you want two accepted or rejected responses over 1 day, and a user accepts or rejects the recommendation twice on day
one, they don’t see the recommendation on day two. They see the recommendation again on day three.

If you add an Assignment element after the Limit Repetitions element and change the label for accept or reject, you must update the
limit repetitions output.

SEE ALSO:

Create Recommendations

Display Recommendations


### Automate Your Business Processes with Salesforce Flow Building a Strategy Building a Strategy

A strategy determines when and how to present an Einstein Next Best Action recommendation on
a Salesforce Lightning record page. For example, if you want to offer a discount to a subset of
customers, create a strategy that collects the appropriate customer records and identifies the
discount option to present. To create a strategy, you can use Flow Builder (recommended) or
Strategy Builder.

Note: When possible, we recommend building a strategy in Flow Builder using the
Recommendation Strategy flow type.

Why Choose Flow Builder Instead of Strategy Builder?

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow builder is a unified, feature-rich Salesforce tool for building business process automations and
is the home for all future flow automation features and enhancements. Strategy Builder is a legacy tool and no updates are planned for
it.

Strategy Builder Strategies
You can create strategies for Einstein Next Best Action using Strategy Builder or Flow Builder. Flow Builder is the recommended
method.

#### Flow Builder Strategies

A Flow Builder strategy specifies business logic and generates output for an Einstein Next Best
Action component on a Salesforce Lightning record page.

In a Flow Builder strategy, you generate recommendations in either of the following ways:

**•** Use predefined recommendations created in the Recommendations object on page 777. With
this method, you create recommendations individually in the Recommendation object and
then use them in one or more Next Best Action components. This method is best if you’re
creating a small number of recommendations.

**•** Create recommendations on the fly without using separate recommendation records on page
778. With this method, you create multiple recommendations dynamically in the strategy flow.
This method is best if you’re creating a large number of recommendations. For example, if you
have an extensive product list, you can create a different upsell recommendation for each
product in the list.

SEE ALSO:

Add and Edit Elements

Flow Element: Get Records

Flow Element: Assignment

Flow Element: Recommendation Assignment


EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Build a Strategy Flow Using Predefined Recommendations

Build a strategy flow based on predefined recommendations. This method works best if you have
a small number of recommendations and want to make them available to multiple Einstein Next
Best Action components. For example, you can create a recommendation that offers a discount to
a customer. You can then use the same recommendation when creating a strategy for birthday
discounts and for new customer discounts.

Before building your strategy flow, create recommendations in the Recommendations object on
page 767.

Note: If you want to create a large number of recommendations dynamically at one time,
you can build a strategy flow with on-the-fly recommendations on page 778 without creating
separate records in the Recommendation object.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** On the **Alt + Templates** tab, select the **Recommendation Strategy** flow type, and click
**Create** .

**3.** Load the records you want to use for your recommendation by adding a Get Records element
to the flow.

**a.** Enter a label and API name.

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

**b.** Select the object to use for the recommendations, such as the Accounts, Cases, or Contacts object.

**c.** In the Filter section, add conditions to limit which records from the object are used in your strategy.

**4.** Bring a predefined recommendation into the strategy by adding a Get Records element.

**a.** Enter a label and API name.

**b.** Select the **Recommendations** object.

**c.** In the Filter section, use conditions to specify the recommendation that you want to use.

**5.** Add other flow elements as needed to define the strategy.

**6.** Make your recommendation available for use in an Einstein Next Best Action component.

**a.** Add an Assignment element.

**b.** For Variable, select **outputRecommendations** .

**c.** For operator, select **Equals** .

**d.** For Value, select the predefined recommendation.

**7.** Save your flow.

**8.** Activate your flow.

You’re now ready to add a Next Best Action component to a Lightning record page. on page 807


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Build Strategy Using On-the-Fly Recommendations

Build a strategy flow with multiple recommendations that you create dynamically in bulk. For
example, you can create a strategy that offers a different upsell recommendation for each product
in your product list. With this method, you create recommendations directly in the strategy flow
without using separate Recommendation records.

Note: If you want to reuse recommendations in multiple Einstein Next Best Action
components, use pre-defined recommendations created in the Recommendations object
on page 777.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** On the **Alt + Templates** tab, select the **Recommendation Strategy** flow type, and click
**Create** .

**3.** Load the records you want to use for your recommendations by adding a Get Records element
to the flow.

**a.** Enter a label and API name.

**b.** Select the object to use for the recommendations, such as the Product object.

**c.** In the Filter section, add conditions to limit which records from the object are used in your
strategy.

**4.** Add a Recommendation Assignment element.

**a.** Enter a label and API name.

**b.** For Record Collection Variable, select the variable that you generated with Get Records.

When you select the variable, the target fields are populated automatically.

**c.** Set values for the target fields:

**•** AcceptanceLabel—Button label to accept the offer.

**•** RejectionLabel—Button label to reject the offer.

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

**•** ActionFlow—API name of the flow that performs an action when the offer is accepted or rejected.

**•** Description—Text that appears above the buttons in the Next Best Action component.

**5.** Make your recommendation available for use in an Einstein Next Best Action component.

**a.** Add an Assignment element.

**b.** For Variable, select **outputRecommendations** .

**c.** For operator, select **Equals** .

**d.** For Value, select the recommendation from the Recommendation Assignment step.

**6.** Save your flow.

**7.** Activate your flow.

You’re now ready to add a Next Best Action component to a Lightning record page on page 807.


Automate Your Business Processes with Salesforce Flow Building a Strategy

#### Strategy Builder Strategies

You can create strategies for Einstein Next Best Action using Strategy Builder or Flow Builder. Flow
Builder is the recommended method.

##### Tour the Strategy Builder Interface

Before you start building your strategy, learn about the primary pieces of Strategy Builder and
how they work together.

Create a Strategy with Strategy Builder
Once you’ve created flows and recommendation records, use Strategy Builder to funnel the
correct recommendations to your users at the right time.

Manage Strategy Builder Action Strategies
Test, troubleshoot, and create strategies using Strategy Builder management tools.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Strategy Builder Elements
Use this page to quickly access a list of Strategy Builder elements and learn how they work together to create unique strategies.

##### Tour the Strategy Builder Interface

Before you start building your strategy, learn about the primary pieces of Strategy Builder and how
they work together.

Find Strategy Builder in Setup by typing _`Strategies`_ or _`Next Best Action`_ in the Quick
Find box. Select **Next Best Action** .


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

Button Bar (1)

Manage your strategies with basic functions like Test and Save.

**•** **Test** runs the most recently saved version of your strategy and displays the recommendations that are surfaced for your users. Testing
your strategy allows you to determine if there are errors that must be fixed and confirms the recommendations that your users see.

**•** **Save** your strategies before you test them and before you leave Strategy Builder so you don’t lose your work.

**•** **Save As** allows you to duplicate a strategy and your currently saved work.

Elements, Manager, and Inspector Tabs (2)

Use the Toolbox to create the substance of your strategy. Add elements, connect external sources, and troubleshoot errors in your
strategy.

**•** From the **Elements** tab, drag new elements onto the canvas and create the building blocks of your strategy.

**•** From the **Manager** tab, add new connections from external sources or other Salesforce products.

**•** Use the **Inspector** tab to isolate specific elements and troubleshoot errors that appear during testing.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Canvas (3)

The canvas is a visual representation of your strategy. From here, you can rearrange elements and see how your recommendations are
flowing from one branch to the next and finally into the output.

SEE ALSO:

##### Create a Strategy with Strategy Builder

Manage Strategy Builder Action Strategies

Inspect Strategy Builder Element Results

##### Create a Strategy with Strategy Builder

Once you’ve created flows and recommendation records, use Strategy Builder to funnel the correct
recommendations to your users at the right time.

Before you start creating strategies, make sure that you create flows and recommendation records
that you can use in your strategy.

**1.** Open Strategy Builder. From Setup, enter _`Strategies`_ or _`Next Best Action`_ in the
Quick Find box, select **Next Best Action**, and click **New Strategy** .

**2.** Give your strategy a name and a description.

**3.** Select a context object from **Object Where Recommendations Display** .

Note: The object that you choose here provides the context for your entire strategy.

For example, if you plan to use this strategy on Case pages, select Case. When the strategy
executes and resolves your expressions, the Next Best Action engine interprets the
incoming recordId as a case object. The engine has to know to what type of object the
pages belong to resolve expressions correctly. Linking your strategy to a specific object
also enables Strategy Builder to provide intelligent assistance in other areas, such as the
Test feature.

**4.** Drag the appropriate elements onto the canvas.

Note: It’s best to start by adding a Load element, as loading recommendations is the
first step in any strategy.

**5.** Order your elements to make sure that recommendations are flowing through the correct
branches.

Note: Elements are divided into two main categories: Recommendation Logic and
Branch Logic. Recommendation Logic elements act directly on the recommendations
flowing into the element by filtering, sorting and limiting. Branch Logic elements act as
gates, using context information, such as the recordId of the page the user is viewing, to
decide which sets of recommendations to allow.

**6.** Save any changes to your strategy.

**7.** To make sure it’s working as expected, test your strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Note: If your strategy isn’t running properly or you see an unexpected error, try using the **Inspector** tab to find the problem.


Automate Your Business Processes with Salesforce Flow Building a Strategy

**8.** Display your strategy using the Suggested Actions component in Experience Builder or the Einstein Next Best Action component in
Lightning App Builder.

###### Write a Strategy Builder Expression

Create unique expressions using logic from the Salesforce expression builder to filter recommendations, select or deselect branches,
and determine which recommendations are available for consideration in a strategy.

Create a Strategy Builder Action Strategy Connection
Use Apex actions to integrate external data sources and information from your Salesforce org into your strategies.

Create a Custom Notification Flow for Next Best Action
Create a trigger in Process Builder to receive direct notifications about errors occurring in your strategies. Launch a flow to send error
information to your desired targets.

Create, Package, and Distribute a Strategy Builder Template
Enterprise developers can create and package strategy templates from Developer Edition orgs for use in multiple Salesforce orgs.
Independent software vendors can also publish templates on AppExchange for distribution to their subscribers. Strategies not
marked as templates in managed packages have intellectual property (IP) protection and can’t be edited or cloned. IP protection
safeguards proprietary information in your strategies.

SEE ALSO:

Test Strategy Builder Action Strategies

Inspect Strategy Builder Element Results

Create a Strategy with Strategy Builder

Build a Flow

###### Write a Strategy Builder Expression

Create unique expressions using logic from the Salesforce expression builder to filter
recommendations, select or deselect branches, and determine which recommendations are available
for consideration in a strategy.

Strategy Builder expressions, found on the Filter and Branch Selector elements, use standard
[Salesforce formula functions. To learn more about creating formulas in Salesforce, see Formula](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)
[Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

Strategies are designed to work with a particular object like Case or Contact. Strategy Builder
elements use `$Record` as a placeholder for the actual record that gets passed in when a strategy
runs.

**1.** Select the element you need for your strategy: **Filter** or **Branch Selector** .

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**2.** Enter your expression. You can build expressions in two different modes: standard and advanced. Standard is declarative: search
and select to build your formula. Use advanced mode for more complex expressions, when a given operator is unavailable in standard
mode, or when you use concatenation.

**3.** In standard mode, set up conditions. At run time, the conditions are evaluated in the order you specify.

**Column Header** **Description**

```
Resource

```

Recommendation resource whose value you want to evaluate, such as acceptance or rejection label,
action, ID, name. For example, a strategy is associated with a Case. Your resource can be
`$Record.Account.Type` or `$Record.Account.Contact.Name` .


Automate Your Business Processes with Salesforce Flow Building a Strategy

**Column Header** **Description**

`Operator` Select an appropriate operator for that resource, for example `Equals`, `Does Not Equal`,
`Starts With`, `Contains`, `Less Than Or Equal To`, and `Is Blank` . The available

operators depend on the data types associated with that resource. Data types include text, number,
Boolean, or picklist.

`Value` Options:

**•** Select a value that’s appropriate for the recommendation resource and the operator. For example,
if you enter `$Record.Status` as the resource and `Does Not Equal` as the operator,
available values are `On Hold`, `Escalated`, `Closed`, and `New` .

**•** Manually enter a literal value.

`Resource` and `Value` in the same row must have compatible data types.

When you add or subtract a number from a date value, the date adjusts in days, not hours.

**Option** **Behavior for Decision Outcomes**

`All Conditions Are Met` If one of the conditions is false, the recommendation evaluates the next outcome’s
conditions.

`Any Condition Is Met` If one of the conditions is true, the recommendation immediately takes this outcome’s
path.


Automate Your Business Processes with Salesforce Flow Building a Strategy

For example, say you create the custom field `Has_Mobile_Service__c` on the contact record. If you use
`$Record.Contact.Has_Mobile_Service__c = false` in a Strategy Builder expression, and you’re working with a case
record, the recordID provided with the request replaces `$Record` when the expression resolves. The recordID replaces `$Record`
because case records have a lookup relationship with contacts.

**•** Reference the context object in your formula using the _`$Record`_ function.

For example, _`ISPICKVAL($Record.Account.Tier__c, 'Premium')`_

Note: The Context object is the object where you plan to surface your recommendations. Choose the Context object, or change
it, by editing your strategy and choosing an object under **Object Where Recommendations Display** .

**•** Reference fields from the Recommendation object using the plain text label name. This option is available only in Filter and Load
elements, not Branch Selector elements.

For example, `AcceptanceLabel = =‘Yes, please’`


Automate Your Business Processes with Salesforce Flow Building a Strategy

**•** Access fields returned from external connections using
_`$nameOfExternalConnection.dataFromExternalConnection`_ syntax. Manage your external connections through
the **Manage** tab in the Toolbox.

For example, `$GetCreditScoreContext.output >= 760`

**•** Use _`$Request`_ to access information the user types into forms and use that information to request specific recommendations.
This option is available only on the Search and Contact Support pages in Experience Builder sites.

For example, `CONTAINS($Request.search, 'paperless billing') || CONTAINS($Request.search,`

```
   'order checks') || CONTAINS($Request.search, 'new address')

```

For multi-select picklist fields, enter values like `Includes ($Record.CarType__c, ‘Audi,’‘BMW’)`

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Create a Strategy Builder Action Strategy Connection

Use Apex actions to integrate external data sources and information from your Salesforce org into
your strategies.

Use Apex invocable actions to pull sources of data into your strategy.

**1.** In Strategy Builder, click the **Manager** tab.

**2.** Click **New Connection** .

**3.** Enter a label to visually identify the connection (1).

**4.** Enter an API name. This name is used in Strategy Builder elements that require conditional
statements, such as Branch Selector and Filter (2).

**5.** Enter a brief description for the connection (3).

**6.** Choose the action to use in logic elements’ conditions (4).

**7.** Enter any parameters for the selected action (5) and click **Done** .


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

**8.** Click the connection label to edit its associated information.

**9.** Click the **>** to the right of the connection label to edit or view its details or to delete it.

**Element** **Description**

**Apex Action** Assigns the invocable action that runs when the connection is referenced in elements’ conditions.

**API Name** Specifies the connection name to use in logic elements’ conditions. For example,
`$GetCreditScoreContext.output >= 760` .

Note: **API Name** is set to **Label** with underscores replacing spaces by default.

**Argument** Specifies one or more parameters that the selected invocable action requires. This textbox appears
only when the action has one or more arguments.

**Description** Specifies the description shown in the connection details.

**Label** Specifies the label displayed in the **Manager** pane for your connection.

SEE ALSO:

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

Strategy Builder Strategies

_[Actions Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro_overview.htm)_ Overview


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Create a Custom Notification Flow for Next Best Action

Create a trigger in Process Builder to receive direct notifications about errors occurring in your
strategies. Launch a flow to send error information to your desired targets.

A custom notification flow allows you to choose how you want to be informed when errors happen
during Next Best Action strategy executions. It consists of two parts. First, a process created in
Process Builder that subscribes to the Platform Status Alert Event, which is generated when the
error occurs. Second, a notification flow that passes the information to your intended destination.
Add input variables to your flow to receive the expected variables.

**1.** In Flow Builder, create a flow. You can direct your notifications to different places, including
[Chatter posts, SMS text messages, and emails. Make sure to define input variables for payload](https://appexchange.salesforce.com/servlet/servlet.FileDownload?file=00P3A00000gAwX0UAK)
event fields that you want to use in your notifications. Input variables are flow variable resources,
type text, with **Available for Inputs** checked.

Note: A simple way to create your notification is to create a flow with the Send Email
core action. From there, manually add the email address where you want the notification
sent.

**2.** In Process Builder, create a process and for **The process starts when** select **A platform event**
**occurs** .

**3.** Add a trigger. Under **Platform Event** select **Platform Status Alert Event** .

**4.** Select an object that allows you to define matching conditions that produce a single result.

Note: For example, you could choose the User object and set **User ID** equal to the
**Created By** ID in the event payload.

**5.** Add other criteria.

**6.** Add an immediate action and select **Flows** .

**7.** Name your action and select the flow you created in step one.

**8.** Add mappings to connect data from the payload of your event to flow inputs.

**9.** Save and activate your process.

SEE ALSO:

Automate Tasks with Flows

[Configure the Process Trigger](https://help.salesforce.com/articleView?id=process_start.htm&language=en_US)

_[Object Reference Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_platformstatusalertevent.htm)_ : PlatformStatusAlertEvent


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create, edit, or view
processes in Process
Builder:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Create, Package, and Distribute a Strategy Builder Template

Enterprise developers can create and package strategy templates from Developer Edition orgs for
use in multiple Salesforce orgs. Independent software vendors can also publish templates on
AppExchange for distribution to their subscribers. Strategies not marked as templates in managed
packages have intellectual property (IP) protection and can’t be edited or cloned. IP protection
safeguards proprietary information in your strategies.

You distribute changes to strategy templates via a managed package. Subscribers who install a
strategy template can open it in Strategy Builder and clone it to customize it for their own use.
When you publish updates to strategy templates via a package upgrade, template updates don’t
affect subscribers’ copies.

**1.** In Strategy Builder, create the strategy that you want to make into a template.

**2.** Open the strategy’s properties and select **Template** .

**3.** If you must, create your managed package.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create a strategy:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To create a managed
package:

**•** Create AppExchange
Packages

**4.** Distribute the strategy template in the managed package and let your subscribers know it’s available.

Example: Suppose you build and package strategies for insurance companies. Because insurance laws and regulations can vary
by location, your subscribers want the ability to modify your strategies when needed. They can do this using strategy templates
you create.

SEE ALSO:

Create a Strategy with Strategy Builder

_[First-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)_

[Create a First-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Manage Strategy Builder Action Strategies

Test, troubleshoot, and create strategies using Strategy Builder management tools.

###### Save Strategy Builder Action Strategies

Save your strategies or use Save As to create new a new strategy based on an existing one.

Test Strategy Builder Action Strategies
Test your strategy within Strategy Builder to see what recommendations display, given different
inputs.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: Salesforce
Classic

Troubleshoot Strategy Builder Action Strategies
Strategies can be complex, which means it’s sometimes difficult to know where you went
wrong when you encounter unexpected results. Use this page to determine the best tool for troubleshooting your strategy.

Inspect Strategy Builder Element Results
View the full details of each step of your strategy’s execution from Strategy Builder’s **Inspector** tab. Trace the path of recommendations
through your strategy and identify problems in individual elements. Debug errors and see how your strategy is working behind the
scenes.

###### Save Strategy Builder Action Strategies

Save your strategies or use Save As to create new a new strategy based on an existing one.

###### Save your new or updated action strategy by clicking Save . Create a strategy based on an existing

one using **Save As** .

###### 1. To save your action strategy click Save .

**2.** To create an action strategy based on an existing one, click **Save As** .

**3.** Replace the existing name in **Name** .

**4.** Replace the existing API name in **API Strategy** .

You can have duplicate strategy names but we don’t recommend it. The API name must be
unique.

To automatically generate a new API name, delete the existing API name after you rename the
strategy. Click the **Name** textbox, and either tab over to or click the **API Name** textbox.

**5.** Optionally, replace the existing description.

**6.** If you want to base your strategy on a different object, click the **Object Where**
**Recommendations Display** textbox and choose a new object.

**7.** Click **Done** .

SEE ALSO:

Strategy Builder Strategies

Suggest Options to Users with Recommendation Strategies


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Test Strategy Builder Action Strategies

Test your strategy within Strategy Builder to see what recommendations display, given different
inputs.

In Strategy Builder, you can test the strategies underlying your recommendations.

**1.** Create or edit a strategy.

**2.** To save your changes, click **Save** .

Note: Always save before testing to test the most recent version of your strategy.

###### 3. Click Test .

**4.** Select an object for the test.

If you don’t see the object that you want to test the strategy against, close the Test Strategy
window. Select the properties wheel above the left pane. Change the object that the strategy
is linked to by selecting an object from **Object Where Recommendations Display** . If you
don’t see an object listed, the strategy hasn’t been linked to a specific object.

**5.** To test the underlying flow, choose a recommendation.

EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Note: Images associated with recommendations aren’t displayed when testing in Strategy Builder.

The Test Strategy window doesn’t show all possible error messages. Strategies are executed from right to left, starting at Output. If
a particular Branch Selector expression results in a closed branch, the child elements of that branch (the elements to the left) are
not executed. This process makes strategy evaluation faster, but it also means that any branches with false expressions could have
errors that aren’t exposed. The Test button shows what the user sees. To get a complete view of any errors occurring at run-time,
use the Inspector tab in the Toolbox. Inspector highlights errors from all elements.

SEE ALSO:

Inspect Strategy Builder Element Results

Strategy Builder Strategies


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Troubleshoot Strategy Builder Action Strategies

Strategies can be complex, which means it’s sometimes difficult to know where you went wrong
when you encounter unexpected results. Use this page to determine the best tool for troubleshooting
your strategy.

If something goes wrong with your strategy, you have several troubleshooting options.

**•** Start by using the basic test function in Strategy Builder. After you create and save a strategy,
click **Test** in the menu bar.

**•** For a more detailed view of your strategy execution, see the **Inspector** tab in the Strategy
Builder Toolbox. The Inspector tab lists specific errors and gives you a detailed view of how your
strategy executes.

**•** If you can’t find the problem in the **Inspector** tab, or you want to troubleshoot for a specific
[user, try using the Apex debug log. Next Best Action has a specific debug log category.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_debugging_system_log_console.htm)

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** To receive full error reports sent directly to your email, a Chatter post, a text message, or other outlet, try creating a custom notification
[flow and a Process Builder trigger. Using a Platform Status Alert Event, you can subscribe to Next Best Action events and respond](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_platformstatusalertevent.htm)
when errors occur.

SEE ALSO:

###### Inspect Strategy Builder Element Results Inspect Strategy Builder Element Results

View the full details of each step of your strategy’s execution from Strategy Builder’s **Inspector** tab.
Trace the path of recommendations through your strategy and identify problems in individual
elements. Debug errors and see how your strategy is working behind the scenes.

When testing your strategy doesn’t return the recommendations you expect, investigate the
execution details of the strategy or a selected element using the **Inspector** tab.

**1.** Click the **Inspector** tab.

**2.** Click **Test** and select an object.

Note: Provide a sample _`recordId`_ to test your strategy in the inspector. You can do
so in either of the following ways:

**•** While Inspector is open, click **Test** and select a record. The _`recordId`_ of the selected
record is pasted into the **Record ID** field of the inspector. Close the Test window and
click **Run** in the inspector.

**•** Copy a record ID from the URL of a record page and paste it into the RecordId field
manually.

**3.** Click **Run** .


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

Note: Inspector can show a single element’s results, or the results for all elements in the strategy. If you select an element,
you see recommendations surfaced by that element. If you have no elements selected, you see recommendations surfaced
by the strategy.

Note: To see accurate results, you have to save your strategy before testing it. If you change the strategy or an element, **Run**
becomes **Save and Run** .

**4.** To scroll right, use the horizontal scroll bar at the bottom of the Inspector pane.

**5.** If you want to view recommendations for a different object, click **Test**, clear your current selection, and choose a new object from
the dropdown. To update the recommendations in the inspector, click **Run** .

SEE ALSO:

Test Strategy Builder Action Strategies

Strategy Builder Strategies


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Strategy Builder Elements

Use this page to quickly access a list of Strategy Builder elements and learn how they work together
to create unique strategies.

Use elements to create your strategies by opening Strategy Builder and selecting Elements in the
Toolbox. Drag elements onto the canvas to get started.

Strategy Builder Enhance Element
Get AI-driven predictions from services such as Einstein Discovery and Einstein Prediction Builder
to enhance Next Best Action recommendations with additional information, such as propensity
scores. The Enhance element allows you to modify a set of recommendations on the fly, every
time a strategy is executed. These recommendations can be static and live as records in
Salesforce, or dynamic and sourced from external data sources or other Salesforce objects.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Strategy Builder Generate Element
With the Generate element, you can dynamically generate personalized recommendations where a large number of possibilities
makes it inconvenient to create recommendations manually. The Generate element allows you to create in-memory, on-the-fly
recommendations, either from an external data source or from other Salesforce objects.

Strategy Builder Load Element
Load is the first element in a strategy branch. Load and filter the records of a Recommendation object. Or load and filter the records
of any object, and convert them into recommendations at the end of the strategy using the Map element. Your load elements
determine which of your recommendations are evaluated when your strategy executes.

Strategy Builder Filter Element
Create an expression that allows you to block or filter out undesirable recommendations, depending on the context. The expression
is evaluated for every recommendation that passes through the branch.

Strategy Builder Limit Reoffers Element
Determine how often a user sees the same recommendation. You can decide how many times the user must react to a
recommendation and how many days to wait before displaying the recommendation again.

Strategy Builder Map Element
The Map element lets you use formulas to create Recommendation fields and modify existing fields without Apex code. Instead, it
relies on expressions and formulas. Use the Map element to pass data from a Recommendation field with one name to a Flow input
with a different name. Or use it to modify current values for Description, Name, and other fields and personalize them with
context-specific data.

Strategy Builder Sort Element
Choose how recommendations are ordered within a branch and reorder them using Recommendation fields.

Strategy Builder Branch Merge Element
Combine recommendations from multiple branches into a single branch.

Strategy Builder Branch Selector Element
Filter multiple branches through a branch selector and create unique expressions for each branch. If the expression is true,
recommendations in the branch are allowed through and combined into a single branch.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Strategy Builder First Non-Empty Branch Element
The first non-empty branch element allows you to filter branches in the order they appear on the canvas. The first branch that
contains recommendations is allowed through, all other branches are blocked.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

###### Strategy Builder Enhance Element

Get AI-driven predictions from services such as Einstein Discovery and Einstein Prediction Builder
to enhance Next Best Action recommendations with additional information, such as propensity
scores. The Enhance element allows you to modify a set of recommendations on the fly, every time
a strategy is executed. These recommendations can be static and live as records in Salesforce, or
dynamic and sourced from external data sources or other Salesforce objects.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Apex

Action

```

Search or select an Apex action, which calls an Apex class. An Apex class must
have a method marked as an invocable method to appear as an Apex action in
declarative tools like Strategy Builder.

`Argument` Specify one or more parameters for the selected Apex action.

Example: Assume that your company integrates separate data sources from the manufacturers of products your business sells.
Those data sources include information about the current availability of each item (in stock, back ordered, or unavailable). You can
connect an Enhance element to your strategy’s Load or Generate element to provide that information to users in the
recommendation.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: You can use the Enhance element to calculate a discount percentage for your customers based on how long your
company has managed their account. Or you can use it to A/B test two branches of recommendations.

Example: Suppose you use Next Best Action to provide upsell recommendations. You want to add a 5% discount to your product
recommendations for those customers who have been with your company for more than one year. Customers of more than two
years get a 10% discount, customers of more than five years get a 20% discount, and so on. Use the Enhance element to call an
Apex action that performs a SOQL query. The query retrieves the Account age and appends it to the description of all incoming
recommendations.

The strategy used with an Enhance element can be as simple as Load -> Enhance -> Output. All recommendations the Load
element retrieves or loads are passed as a list of recommendations to the underlying invocable method.

When configuring the Enhance element, select **Enhance with Discounts Based on Age** as the Apex action and specify **$Record.id**
as the input parameter.


Automate Your Business Processes with Salesforce Flow Building a Strategy

The Enhance element in turn calls the `getDiscounts` invocable method in the `Enhance_GetAccountDiscount` class.
Notice how the description of each recommendation has a discount value appended to it `(r.Description + ‘ with`
`a 5% discount’)` .

```
      global class Enhance_GetAccountDiscount {

        @InvocableMethod(label='Enhance with Discounts Based on Age' description='Returns

      an enhanced set of recommendations with appropriate discounts')

        global static List<List<Recommendation>> getDiscounts(List<DataContainer> inputData){

           List<Recommendation> recommendations = inputData[0].recommendations;

           List<List<Recommendation>> outputs = new List<List<Recommendation>>();

           Account[] accounts = [SELECT Name, Description,CreatedDate, id FROM Account

      WHERE id = :inputData[0].accountId];

            Double ageAccountMonths =

      accounts[0].CreatedDate.date().monthsBetween(date.today());

           Double ageAccount = ageAccountMonths/12;

           List<Recommendation> returnedRecommendations = new List<Recommendation>();

           for (Recommendation r:recommendations){

             if(ageAccount > 1){

               r.Description = r.Description + ' with a 5% discount' ;

             }

             else if (ageAccount > 2){

               r.Description = r.Description + ' with a 10% discount ';

             }

             else if (ageAccount > 5){

               r.Description = r.Description + ' with a 20% discount ';

             }

             returnedRecommendations.add(r);

           }

           outputs.add(returnedRecommendations);

           return outputs;

```


Automate Your Business Processes with Salesforce Flow Building a Strategy

```
        }

      }

```

Usage

The Enhance element requires an Apex action marked as an invocable method.

```
   @InvocableMethod(

   label='Enhance with Discounts Based on Age'

   description='Returns an enhanced set of recommendations with appropriate discounts')

```

Use the Enhance element in combination with the Strategy Builder Load or Generate element.

The Enhance element can pass any number of inputs to the Apex action. The input parameter must be a list or a list of lists of a user-defined
Apex object (for example, a custom class called `DataContainer` ). The user-defined Apex object must include a
`List<Recommendation>` variable. The `List<Recommendation>` variable is automatically defined with the recommendations
that pass into the Enhance element.

```
   global class DataContainer {

      @InvocableVariable

      public string accountId;

      @InvocableVariable

      public List<Recommendation> recommendations;

   }

   ________

   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

The Enhance element returns a list of recommendations, `List<List<Recommendation>>` . These recommendation enhancements
exist only in memory and don’t persist after the strategy is executed.

```
   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

SEE ALSO:

###### Strategy Builder Generate Element

Strategy Builder Load Element

Flow Element: Apex Action

###### Strategy Builder Generate Element

With the Generate element, you can dynamically generate personalized recommendations where
a large number of possibilities makes it inconvenient to create recommendations manually. The
Generate element allows you to create in-memory, on-the-fly recommendations, either from an
external data source or from other Salesforce objects.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

**Field** **Description**

`Description` Optional description of the element and how it works within the strategy.

`Apex Action` Search or select an Apex action, which calls an Apex class. An Apex class must have a method marked as an
invocable method in order to appear as an Apex action in declarative tools like Strategy Builder.

`Argument` Specify one or more parameters for the selected Apex action.

Example: Assume that your company has a large catalog of products and you use a screen flow to recommend accessories to
your customers based on their past product purchases. Instead of creating a single, static recommendation for each individual
accessory, you can maintain that information in the Account or Product object in Salesforce. Or you can store information in external
data sources like Commerce Cloud or a SQL database. Use a Generate element with an Apex invocable action to call the Apex class
and generate accessory recommendations dynamically for your strategy.

Example: Suppose you want to show a service agent a list of key accounts to follow up with after a set number of days has passed
since the previous contact. With the Generate element, you can call an Apex action that makes a SOQL query for Account where
the Owner is the logged-in user (the agent). This query identifies the accounts who were last contacted more than, say, 90 days
ago. Next Best Action returns the relevant accounts in the form of recommendations. The strategy can be as simple as the Generate
element with an Output element.

When you configure the Generate element, select **Accounts to Follow Up Today** as the Apex action and specify **$User.id** as an
input parameter.


Automate Your Business Processes with Salesforce Flow Building a Strategy

The Generate element calls the `getAccounts` invocable method in the `Generate_GetAccountsToFollowUp` Apex
class. This method retrieves the relevant accounts and creates a list of recommendations. The recommendation description includes
the name of the account ( `account.Name` ) and the number of days since the last contact ( `daysSinceLastContact` ).

```
      global class Generate_GetAccountsToFollowUp {

        @InvocableMethod(label='Accounts to Follow Up Today'

                  description='Recommend accounts the current user should follow

      up on today')

        global static List<List<Recommendation>> getAccounts(List<String> inputData){

           List<List<Recommendation>> outputs = new List<List<Recommendation>>();

           Integer daysSinceLastContact;

           Account[] accounts = [SELECT Name, Description, LastContactDate__c, OwnerId

      FROM Account WHERE OwnerId = :inputData[0]];

           List<Recommendation> recs = new List<Recommendation>();

           for (Account account:accounts) {

             if (account.LastContactDate__c != null){

               daysSinceLastContact =

      account.LastContactDate__c.daysBetween(date.today());

               if (daysSinceLastContact > 90){

                  Recommendation rec = new Recommendation(

                    Name = account.Name,

                    Description = 'Connect with the ' + account.Name + ' account,

      the last interaction was '+ daysSinceLastContact + ' days ago.',

                    //Pre-req: Create a screen flow with the name simpleFlow

                    ActionReference = 'simpleFlow',

                    AcceptanceLabel = 'View'

                  );

                  recs.add(rec);

               }

             }

           }

           outputs.add(recs);

           return outputs;

        }

      }

```

When you execute the strategy, the resulting recommendation includes the name of the account and the number of days since
the last contact with them.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Usage

The Generate element requires an Apex action marked as an invocable method.

```
   @InvocableMethod(

   label='Related Wikipedia Pages'

   description='Recommend wikipages that are related to the named input wikipage')

```

The Generate element can pass any number of inputs to the Apex action, either as lists or a list of lists of primitives, sObjects, and
user-defined Apex objects. To provide more than one input, the input parameter must be a list or a list of lists of a user-defined Apex
object (for example, a custom class called `DataContainer` ).

```
   List<String> relatedTo

```

OR

```
   global class DataContainer {

   @InvocableVariable

   public string accountId;

   }

   ____

   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

The Generate element returns a list of recommendations. Invocable methods support returning either a list of an sObject type or a list
of lists of an sObject type. Since the Enhance element operates not on a single recommendation but on a list of recommendations, the
method must return a `List<List<Recommendation>>` .

```
   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

SEE ALSO:

Strategy Builder Enhance Element

Flow Element: Apex Action

###### Strategy Builder Load Element

Load is the first element in a strategy branch. Load and filter the records of a Recommendation
object. Or load and filter the records of any object, and convert them into recommendations at the
end of the strategy using the Map element. Your load elements determine which of your
recommendations are evaluated when your strategy executes.

Load recommendations from the records of any standard or custom object. You can use objects
such as Recommendation, Account, Product, and Opportunity when you build a strategy. Choose
criteria for when to load a recommendation. Filter out certain records from a strategy. Sort your
records by selecting an object value.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

A strategy treats another object the same as it does a Recommendation object until the end, when
it converts it into a recommendation. If you choose an object other than Recommendation, add a
Map element after the Load element. Use the Map element to map fields from the object’s records to required fields on the
Recommendation object.

In Strategy Builder, you can load up to 1,000 records in a strategy. A Strategy Builder strategy has a limit of 100 Load elements on the
canvas. To load more than 1,000 records, create your recommendation strategy in Flow Builder, which has a load limit of 50,000 records.


Automate Your Business Processes with Salesforce Flow Building a Strategy

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Object` The object whose records are loaded, filtered, and converted into recommendations.

```
Condition

Requirements

```

Determines the logic to evaluate conditions. To load the recommendation if it meets all the specified criteria,
select **All Conditions are Met** . To load the recommendation if it meets any listed criteria, select **Any Condition**
**is Met** .

`Field` Choose a field from the Recommendation object to evaluate whether the recommendation is loaded into the
strategy.

`Operator` Choose an operator.

`Value` Enter a value for your chosen field. Values can be simple numbers, string phrases, or formulas that use Salesforce
formula support. Don’t enclose string or number values with quotes. Picklists aren’t supported.

`Add Condition` Creates an extra set of conditions.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

Strategy Builder Enhance Element

###### Strategy Builder Filter Element

Create an expression that allows you to block or filter out undesirable recommendations, depending
on the context. The expression is evaluated for every recommendation that passes through the
branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Filter` Create an expression that is evaluated for each recommendation that you load
`Expression` into your strategy. If the expression is true, the recommendation is allowed
through. If false, the recommendation doesn’t progress further through the
strategy. Filter Expression accepts Standard Salesforce formulas. For more
[information, see Formula Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

Note: Use _`$Record`_ to reference fields from the context object. The context object is the object where you intend to surface
your recommendations and can be changed by editing your strategy and choosing an object under **Object Where**
**Recommendations Display** . Use plain text field labels to reference Recommendation object fields. Examples: _`$Record.status`_
!= _`'New'`_, _`RejectionLabel`_ == _`‘No, thanks.’`_ For more information, see Write a Strategy Builder Expression.

Example: Suppose that you want to surface recommendations on the Case object so your service agents can suggest offers to
your customers. If you want to suggest only credit card offers, create a _`Category`_ field for the Recommendation object. Add a
Credit Card Offer category to your field. Add a filter element and use the formula _`Category_c`_ = _`‘CreditCardOffer’`_
in **Filter Expression** .

Usage

Filter is the best way to remove certain recommendations from a strategy branch. Add the element to a branch and create an expression
to evaluate every recommendation that passes through the branch.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Strategy Builder Limit Reoffers Element

Determine how often a user sees the same recommendation. You can decide how many times the
user must react to a recommendation and how many days to wait before displaying the
recommendation again.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To view a recommendation
strategy with a Limit Reoffers
element on a Lightning
record page:

**•** Run Flows

```
User

Reaction

```

Choose a user reaction to base your limits on. For example, if you select **User**
**Rejects the Recommendation**, your element only limits repeat offers after
the recommendation is rejected.

`Number of` Choose how many times you want the user to react before the recommendation
`Reactions` is limited.

```
Time

Period in

Days

```

Choose how many days the system waits after the user has reacted the specified
number of times before a repeat offer is shown to the same user.

Time Period in Days is based on days, not hours. If the time period is set to 1,
and the user accepts the recommendation at any time on Monday, the offer

doesn’t display again until the start of Wednesday. So a one-day time period
could be as few as 25 hours in duration or as many as 48 hours.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: Let’s say you have a renewal offer that you want to surface at most one time per year. If a user has already accepted
the offer and filled out the renewal, you don’t want to show the same offer again. For this example, for User Reaction, select **User**
**Accepts the Recommendation** . For Number of Reactions, select **1**, and set the time period for 365 days for an annual renewal.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

###### Strategy Builder Map Element

The Map element lets you use formulas to create Recommendation fields and modify existing fields
without Apex code. Instead, it relies on expressions and formulas. Use the Map element to pass
data from a Recommendation field with one name to a Flow input with a different name. Or use it
to modify current values for Description, Name, and other fields and personalize them with
context-specific data.

If you load an object other than Recommendation, add a Map element after the Load element and
before the Output element in your strategy. Use the Map element to map fields from the records
to required fields on the Recommendation object. For example, map the product Title field to the
recommendation Name field. Mapping fields converts the filtered records into recommendations
that are surfaced via the Next Best Action component and your own apps.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: You can include the name of a contact in a recommendation, and further personalize the recommendation with text.
Suppose that you have a recommendation with the description, “Thank you for being a loyal customer. We truly appreciate your
business!” Using the Map element, you can personalize the description. Add the name of the contact to the description, for example,
“Lauren Boyle, Thank you for being a loyal customer. We truly appreciate your business!”

**•** Use a Load element to load all the recommendations you want to change. Or you can add a Generate element and pass in
dynamically generated recommendations.

**•** Add a Map element. In the Name field, select **Description** and in the Value field, enter this expression:

`$Record.Contact.Name+ “, ” + Description` . Leave the Type field as `Text` .


Automate Your Business Processes with Salesforce Flow Building a Strategy

**•** Place the “Personalized Thank You” Map element after the Load element. It modifies the descriptions of all recommendations
that pass through it.

**•** When you execute the strategy, your recommendations include the contact name for the current case.

###### Strategy Builder Sort Element

Choose how recommendations are ordered within a branch and reorder them using
Recommendation fields.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Recommendation` Choose a field from the Recommendation object to sort on.

```
Field

```

`Sort` Choose whether you want to sort your recommendations in an ascending or
`Direction` descending order.

`Sort Empty` Recommendations that don’t contain information in the field you chose in
`Values to` Recommendation Field are sorted to the top when selected.

```
Top

```

`Maximum` Limits the number of recommendations allowed to pass through the element.

```
Recommendations

```

Usage

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Sort the order of your recommendations in a branch by choosing a value from the Recommendation object to sort on. Choose whether
you want to sort in an ascending or descending order, and decide how many recommendations to allow through.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Strategy Builder Branch Merge Element

Combine recommendations from multiple branches into a single branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Maximum` Determines the maximum number of recommendations allowed through the
`Recommendations` branch where the sort element is placed.

Usage

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Merge multiple branches into a single branch and limit the number of recommendations allowed through the branch with the branch
merge element.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

###### Strategy Builder Branch Selector Element

Filter multiple branches through a branch selector and create unique expressions for each branch.
If the expression is true, recommendations in the branch are allowed through and combined into
a single branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Condition` Create an expression for each branch that flows through the element. If the
expression is true, the recommendations in the branch are allowed through. If

false, the recommendations in the branch don’t progress any further through
the strategy. Condition accepts standard Salesforce formula functions. For more
[information, see Formula Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Note: Use _`$Record`_ to reference fields from the context object. The context object is the object where you intend to surface
your recommendations and can be changed by editing your strategy and choosing an object under **Object Where**
**Recommendations Display** . Example: _`ISPICKVAL($Record.status, 'New')`_ . For more information, see Write a
Strategy Builder Expression.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: Suppose that you want to surface recommendations on the Case object so your service agents can suggest offers to
your customers. If a case has been escalated, you want to offer a special discount. To do so you, create a load element that loads
the recommendations associated with your offer. Create a branch selector that only allows recommendations from the branch if
the case has an escalated status. Make your offer load element a child of the branch selector element. In **Condition** on the branch
selector element, use the following formula: _`ISPICKVAL($Record.status, 'Escalated')`_ .

Usage

Branch selector is an important element when you want to weed out entire branches at once. Unlike a filter element, it can’t filter based
on individual recommendations.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Strategy Builder First Non-Empty Branch Element

The first non-empty branch element allows you to filter branches in the order they appear on the
canvas. The first branch that contains recommendations is allowed through, all other branches are
blocked.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: Let’s say you have five different types of credit card offers that could be surfaced to a single user. Although each offer
type is unique and must have its own branch, you only want to surface one type. To do so, filter all of your branches that contain
credit card offers through a first non-empty branch, in priority order from top to bottom. Your element only allows the first branch
that contains recommendations.

Usage

Branches are filtered through the first non-empty branch element in the order that they appear on the canvas, moving from top to
bottom. The element evaluates each branch until it finds one that contains recommendations. When the element recognizes that a
branch contains recommendations, it allows those recommendations through and blocks recommendations from all other branches.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations


### Automate Your Business Processes with Salesforce Flow Display Recommendations Display Recommendations

After creating a strategy, choose a page to run your strategy and display your recommendations.
You can use a Lightning record page, an app’s home page, an Experience Cloud site page, a
Visualforce page, or an external site, depending on where you want recommendations to appear.

Lightning Page (Lightning App Builder)

**•** On a Lightning page in Lightning App Builder, create, edit, or clone a record page.

**•** Drag Einstein Next Best Action from the component list to the location on the page where you
want to display it.

**•** Choose an action strategy and the number of recommendations that you want the component
to display.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you want to show users flows and quick actions in addition to recommendations, use the Actions & Recommendations component
on your Lightning record page. You can create an Actions & Recommendations deployment that specifies action strategies and how
you want your recommendations to appear.

App Home Page

**•** Create a strategy for the Next Best Action component. Use global variables such as $User.Id when you create the strategy. Use global
variables because the home page isn’t a record page and isn’t associated with objects, like Case, Account, or Product.

**•** Navigate to your org’s Home page.

**•** Click, and select Edit Page.

**•** From the list of Lightning components on the left (1), drag the Einstein Next Best Action component to the home page (2).

Experience Builder Site Page (Experience Builder)

**•** In Experience Builder, create or edit a site page.

**•** Drag Suggested Actions from the component list to the location on the page where you want to display it.

Visualforce Page: Use Lightning Out to add the lightning:nextBestAction component.

Custom Apps: Add Einstein Next Best Action functionality into your app with the global lightning:nextBestAction component.


Automate Your Business Processes with Salesforce Flow Display Recommendations

#### Einstein Next Best Action Component

Einstein Next Best Action uses strategies that apply your org’s business rules to display context-sensitive suggested offers and actions
on your Lightning record pages.

SEE ALSO:

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

[Flow Builder for Service and the Actions & Recommendations Component](https://help.salesforce.com/s/articleView?id=sf.console_lex_guided_action_list_component.htm&language=en_US)

_Lightning Aura Components Developer Guide:_ [Add Aura Components to Any App with Lightning Out (Beta)](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/lightning_out.htm)

Einstein Next Best Actions Considerations

#### Einstein Next Best Action Component

Einstein Next Best Action uses strategies that apply your org’s business rules to display
context-sensitive suggested offers and actions on your Lightning record pages.

**1.** Create a recommendation strategy in Strategy Builder.

**2.** Drag the Einstein Next Best Action component onto your record page.

Note: In Experience Builder, the component is called Suggested Actions.

**3.** In the property editor, select the strategy you want to display (1). Enter the maximum number
of recommendations to display (2) and choose where recommendations open when accepted
(3).


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

OR

For Experience Cloud,
the FlowSites perm
provides org-wide
access. To restrict access
to users by profile or
permission set, add a
component visibility filter
to the Suggested Actions
component.

Automate Your Business Processes with Salesforce Flow Display Recommendations

**Component** **Description**

Title Displays the title for the component on the
Record page.

Hide Einstein Header Hides the Einstein Recommendations graphical
header.

Strategy Displays all available strategies created in Strategy
Builder.

Maximum Recommendations Displayed Displays up to four recommendations.

Hide Empty Component Displays the component only when there are
recommendations available initially.

Launch Recommended Action In Specifies whether recommendations open in a
display window or a new browser window.

Show Image

Shows images associated with each displayed
recommendation. If there isn’t an image, a
placeholder displays.

Show Description Displays the recommendation descriptions.

Show Reject Option Displays the reject option.

Set Component Visibility

[Allows Dynamic Lightning Pages by adding filter](https://help.salesforce.com/s/articleView?id=sf.lightning_page_components_visibility.htm&language=en_US)
conditions and logic to the component properties
in the Lightning App Builder.

Here’s how a strategy looks with the Einstein header and no images in the Service console:


### Automate Your Business Processes with Salesforce Flow Report On and Track a Recommendation Report On and Track a Recommendation

Create a custom report type to report on and track recommendation data and strategy metrics.
You can see the monthly total recommendations that a Salesforce org’s strategies served. And you
can analyze which recommendations are accepted and rejected, who responds to them, and more.

Salesforce updates recommendation strategy metrics each time a strategy is executed or a
recommendation is accepted or rejected. Analyze usage metrics to better understand how your
strategies are performing. Use this knowledge to improve your strategies’ logic and increase their
effectiveness.

For example, run A/B tests on two different strategies and compare their relative performance. If
your service agents accept more recommendations served from Strategy B, use metrics to discover
why.

**1.** For complete instructions on creating custom report types, search for Create a Custom Report
Type in Salesforce Help.

**2.** For strategy-level data that’s aggregated for each calendar month, use the Recommendation
Strategy Metrics primary object. For recommendation-level details, use the Recommendation
Reactions primary object instead.

**3.** Using the Recommendation Strategy Metrics primary object, combine fields from it (like
Recommendation Source ID) and the related strategy (like Context Record Type). Using the
Recommendation Reactions primary object, include fields to report on, such as Context Record
ID, Created Date, Last Modified Date, Recommendation Score, and Source ID.

To view recommendation
metrics data:

**•** Modify All Data or
Manage Next Best
Action Strategies

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create, edit and delete
custom report types:

**•** Manage Custom Report
Types

**4.** To analyze a strategy’s performance, group your strategy executions by recommendation source
ID, and the number of times a recommendation was served, accepted, and rejected. To compare
performance between two different strategies, group your strategy executions by recommendation source ID. Add useful metadata
to your report, such as recommendation description and create date.

**5.** Deploy the report types you want to make available to users.

**6.** Let users know that they can create reports using these custom report types.

**7.** Users can also create dashboards from the custom report type.


## Automate Your Business Processes with Salesforce Flow Automated Actions

SEE ALSO:

[Create a Custom Report Type](https://help.salesforce.com/s/articleView?id=sf.reports_defining_report_types.htm&language=en_US)

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_responses_n_b_a_reaction.htm)_ Recommendation Reaction

## Automated Actions

An automated action is a reusable component that performs some sort of action behind the
scenes—like updating a field or sending an email. After you create an automated action, add it to
a process, milestone, or other automated process.

EDITIONS

Available in: both Lightning
Experience and Salesforce
Classic

Flow triggers are available
in: Salesforce Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Outbound messages are
available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Email alerts are available in:
**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

Considerations for Automated Actions
Before you start working with automated actions, familiarize yourself with relevant limits and
special behaviors.

[Manage Automated Actions in Workflow Rules](https://help.salesforce.com/apex/HTViewHelpDoc?id=managing_workflow_actions.htm&language=en_US#managing_workflow_actions)


### Automate Your Business Processes with Salesforce Flow Task Actions Task Actions

Task actions determine the details of an assignment given to a specified user by an automated
process. You can associate task actions with workflow rules, approval processes, or entitlement
processes.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

From Setup, enter _`Tasks`_ in the `Quick Find` box, and select **Tasks** . Then use these settings
to configure your task.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


### Automate Your Business Processes with Salesforce Flow Email Alert Actions

Notice that all your tasks include a **Created By** field. For tasks, this field contains the name of the person who saved the record that
triggered the rule to assign the task.

Tasks don't trigger task-based workflow rules if they’re created automatically, such as by clicking the **Send An Email** button or by using
the Email to Salesforce BCC address field.

SEE ALSO:

Associate Actions with Workflow Rules or Approval Processes

### Email Alert Actions

An email alert is an email generated by an automated process and sent to the designated recipients.
The action consists of the standard text and the list of recipients. You can use an email alert in an
automation, such as a flow, approval process, or entitlement process. Legacy workflow rules and
processes built in Process Builder or through the Invocable Actions REST API endpoint also use
email alerts.

From Setup, enter _`Email Alerts`_ in the Quick Find box, and select **Email Alerts** . Then use
these settings to configure your email alert.

Tip: Create a standardized letterhead to use for all email templates that you use for email
alert actions.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Email Alert Actions


Automate Your Business Processes with Salesforce Flow Email Alert Actions

The daily allocation for emails sent through email alerts is 1,000 per standard Salesforce license per org—except for free Developer
Edition and trial orgs, where the daily email allocation is 15. The overall org allocation is 2,000,000. This allocation applies to emails sent
through email alerts in automations or REST API. Single emails sent to external email addresses are also limited, and how those limits
are enforced depends on when your org was created.

SEE ALSO:

Recipient Types for Email Alerts

Daily Allocations for Email Alerts

Recipient Types for Email Alerts

When you configure an email alert, you identify who receives the email. The options available vary
based on your Salesforce settings and the object that you selected.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


### Automate Your Business Processes with Salesforce Flow Field Update Actions

The Recipient merge field isn’t supported in either Classic or Lightning email templates used for automations.

### Field Update Actions

Field update actions let you automatically update a field value. You can associate field updates with
workflow rules, approval processes, or entitlement processes.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

From Setup, enter _`Field Updates`_ in the `Update` box, and select **Field Updates** . Then use
these settings to configure your field update.

Before you begin, check the type of the field you want to update. Read-only fields like formula or
auto-number fields aren’t available for field updates.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Field Update Actions

SEE ALSO:

Associate Actions with Workflow Rules or Approval Processes

Cross-Object Field Updates

Considerations for Field Update Actions

#### Value Options for Field Update Actions

When you create a field update action, specify the new value of the field.

Available field update options depend on the type of field you’re updating.

**•** Choose **A specific value**, and enter the value in the space provided.

**•** Choose **A blank value (null)** if you want Salesforce to remove any existing value and leave
the field blank. This option isn't available for required fields, checkboxes, and some other types
of fields.

**•** For record owners, choose a user to assign to the record. For case, lead, and custom object
records, you can also choose a queue for this field. To send an email to the new record owner,
select `Notify Assignee` . (This option is unavailable when user control over task assignment
notifications is enabled.)

**•** For checkboxes, choose `True` to select the checkbox and `False` to deselect it.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

### Automate Your Business Processes with Salesforce Flow Outbound Message Actions

**•** For picklists, select a specific value from the dropdown list, or select the value above or below the current value based on the sorting
specified in the picklist definition. If you sort values alphabetically, the values above or below the current value can be different for
users in other languages.

**•** To calculate the value based on an expression, merge fields, or other values, select **Use a formula to set the new value** . For more
[information about using formulas in Salesforce, see Calculate Field Values with Formulas.](https://help.salesforce.com/s/articleView?id=sf.customize_formuladef.htm&language=en_US)

### Outbound Message Actions

An outbound message sends information to a designated endpoint, like an external service. You
configure outbound messages from Setup. You must configure the external endpoint and create
a listener for the messages using SOAP API. You can associate outbound messages with flows,
workflow rules, approval processes, or entitlement processes.

Note: Previously, outbound messages were available in Professional Edition with the purchase
of an add-on. The add-on is no longer available for Professional Edition.

For example, automatically initiate the reimbursement process for an approved expense report by
triggering an outbound API message to an external HR system.

### From Setup, in the Quick Find box, enter Outbound Messages, and then select Outbound

**Messages** . Then use these settings to configure your outbound message.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Outbound Message Actions

If your endpoint URL uses a client certificate, see Import a Client Certificate for Your Endpoint URL on page 821.

SEE ALSO:

Track the Delivery Status of an Outbound Message

Considerations for Outbound Messages

[SOAP API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/)

Associate Actions with Workflow Rules or Approval Processes

Considerations for Outbound Messages

#### Outbound Message Notifications

You can request that up to 5 users receive a notification listing all outbound messages that have
failed for at least 24 hours. A fresh notification is sent every 24 hours until you cancel the request.
Failed messages are deleted from the failed outbound messages related list after 7 days. Before
they’re removed, you can delete them yourself or request that they be retried again.

Note: Previously, outbound messages were available in Professional Edition with the purchase
of an add-on. The add-on is no longer available for Professional Edition. If outbound messages
are available in your Salesforce edition but you don’t see the Outbound Message Notifications
page, your org doesn’t have notifications for outbound messages enabled. Contact Salesforce
to enable notifications for outbound messages.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Create an Outbound Message Notification
You can request that up to five users receive a notification listing all outbound messages that have failed for at least 24 hours. A fresh
notification is sent every 24 hours until you cancel the request.

View an Outbound Message Notification Request
View or edit outbound message notification requests.


Automate Your Business Processes with Salesforce Flow Outbound Message Actions

##### Create an Outbound Message Notification

You can request that up to five users receive a notification listing all outbound messages that have
failed for at least 24 hours. A fresh notification is sent every 24 hours until you cancel the request.

Note: If you don’t see the Outbound Message Notifications page, your org doesn’t have
notifications for outbound messages enabled. Contact Salesforce to enable notifications for
outbound messages.

**1.** From Setup, enter _`Outbound Message Notifications`_ in the Quick Find box, then
select **Outbound Message Notifications** .

**2.** Click **New** .

**3.** Enter a full username, or click the icon to select it from a list of usernames.

**4.** Save the request.

##### View an Outbound Message Notification Request

View or edit outbound message notification requests.

From the detail page of an outbound message notification request:

**•** To change the username for a notification request, click **Edit** . It’s simpler than deleting the
request and then creating a one.

**•** To delete the notification request, click **Delete** .

**•** To create a notification request with the same username, click **Clone** .


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create an outbound
message notification:

**•** Modify All Data

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To view or edit outbound
message notification
request:

**•** Modify All Data

### Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

#### Track the Delivery Status of an Outbound Message

To track the status of an outbound message, from Setup, enter _`Outbound Messages`_ in the
`Quick Find` box, then select **Outbound Messages** .

**•** _Next items for delivery_ are awaiting delivery.

**•** _Oldest failures_ haven’t yet been deleted because they haven’t been delivered and aren’t 24
hours old.

**•** _Failed outbound messages_ failed to be delivered and are no longer being retried. Messages are
listed here only if you configure the message when you create it by selecting `Add failures`
`to failed outbound message related list` . If you don’t see this related list,
it hasn’t been enabled for your organization.

You can perform several tasks here.

**•** To view the action that triggered it, click any workflow or approval process action ID.

**•** To change the **Next Attempt** date to now, click **Retry** . This option causes the message delivery
to be immediately retried. If you select **Retry** in the **Failed outbound messages** related list,
the outbound message moves to the **Next items for delivery** related list and is retried for
another 24 hours.

**•** To permanently remove the outbound message from the queue, click **Del** .

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To track outbound
messages:

**•** Modify All Data

Note: If you don’t have this option, your org doesn’t have outbound messages enabled. Contact Salesforce to enable outbound
messages.

#### Import a Client Certificate for Your Endpoint URL

If the endpoint URL of your outbound message uses a client certificate, import it to put your
outbound message into action.

**1.** From Setup, enter _`API`_ in the `Quick Find` box, then select **API**

**2.** Click **Generate Client Certificate** .

**3.** Save the certificate to the appropriate location.

**4.** Import the downloaded certificate into your application server and configure your application
server to request the client certificate.

### Considerations for Automated Actions

Before you start working with automated actions, familiarize yourself with relevant limits and special
behaviors.

Considerations for Field Update Actions
Learn how to use field update actions to their full potential in workflow.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Considerations for Outbound Messages
Review the considerations for using outbound message actions before implementing them in your workflows.

SEE ALSO:

Daily Allocations for Email Alerts

#### Considerations for Field Update Actions

Learn how to use field update actions to their full potential in workflow.

[other]: Where possible, we changed noninclusive terms to align with our company value
of Equality. We maintained certain terms to avoid any effect on customer implementations.

When creating field updates for workflow rules or approval processes, consider the following:

Field Update Processing

**•** Field updates occur before email alerts, tasks, and outbound messages.

**•** Field updates occur after case assignment, lead assignment, and auto-response rules.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Field updates function independently of field-level security. Therefore, a workflow rule can update fields even though they’re hidden
on the user's page layout.

**•** The result of a field update is unpredictable when a single workflow rule includes multiple field updates that apply different values
to the same field.

**•** Field updates can affect the information in a related list. For example, if a field such as the `Amount` or `Close Date` of an
opportunity is set to be updated, it affects the Stage History related list on opportunities.

**•** If a user gets a field update error when saving a record, you can use the debug log to see which field update failed. The debug log
stops when a failure occurs.

**•** For reminder fields on tasks and events:

**–** Field updates can set the reminder for a task or event but they can't use the due date of a task or the scheduled time of an event.

**–** Formulas for date/time values are calculated in days. Divide the value by 1440—the number of minutes in a day—to express
the value in minutes. For example, the formula `Now()-7` means seven _days_ ago, while `Now()-7/1440` means seven
_minutes_ ago.

**•** If your organization uses multiple currencies, currency fields are updated using the record's currency. If you choose to update a field
based on a formula, any values in your formula are interpreted in the currency of the record.

**•** Field updates are tracked in the History related list if you have set history tracking on those fields.

**•** Workflow rules and some processes can invalidate previously valid fields. Invalidation occurs because updates to records based on
workflow rules and also on process-scheduled actions don’t trigger validation rules.

**•** If you have person accounts enabled, you can use the `Is Person Account` field as part of the evaluation criteria for workflow
rules. However, because the `Is Person Account` field is read-only, any field updates set up to modify it fails.

Tip: Salesforce processes rules in the following order:

**•** Validation rules

**•** Assignment rules

**•** Auto-response rules

**•** Workflow rules (with immediate actions)


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

**•** Escalation rules

Notes on Cross-Object Field Updates

**•** For all custom objects and some standard objects, you can create workflow and approval actions where a change to a detail record
updates a field on the related main record. Cross-object field updates work for custom-to-custom master-detail relationships,
custom-to-standard master-detail relationships, and a few standard-to-standard master-detail relationships. For more information,
see Cross-Object Field Updates on page 11.

**•** Approval processes can't use cross-object field update actions.

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** To create workflow rules so that case comments or emails automatically update fields on associated cases, select **Case Comment**
or **Email Message** in the Object dropdown list when creating a workflow rule and select **Case** in the Field to Update list. Email-to-Case
or On-Demand Email-to-Case must be enabled for your organization to use the Email Message in a workflow rule.

When cases are updated by an email-triggered workflow rule, the updated case can trigger:

**–** Workflow rules

**–** Validation rules

**–** Updates to roll-up summary fields

**–** Escalation rules

**–** Apex triggers

**–** Entitlement processes

The updated case can't trigger:

**–** Assignment rules

**–** Auto-response rules

Field Update Actions and Custom Fields

**•** Before changing a custom field’s type, make sure it isn’t the target of a workflow field update or referenced in a field update formula
that’s invalidated by the new type.

**•** You can't delete a custom field that is referenced by a field update.

**•** You can use field updates on encrypted custom fields, but if you try to use a formula to set the new value, the encrypted field isn't
available in the formula editor.

Field Update Actions on Opportunities and Contracts

**•** You can define field updates for the `Stage` field on opportunities, but be aware of how this field affects the `Type` and `Forecast`
`Category` fields.

**•** You can define field updates using the `Amount` field on opportunities but it only applies to those opportunities that don't have
products. Adding products to an opportunity changes the `Amount` field to a read-only field that is automatically calculated and
not affected by that field update.

**•** You can define field updates for the `Status` field on contracts. However, the value of this field can affect the value of the `Status`
`Category` field as well.

**•** Avoid creating a field update for contracts or orders that changes the `Status` field to any value other than Approved.


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Field Update Action Limitations

**•** The results of a field update can't trigger additional rules such as validation, assignment, auto-response, or escalation rules.

**•** The results of a field update can trigger additional workflow rules if you’ve flagged the field update to do so. For more information,
see Field Updates That Reevaluate Workflow Rules on page 826.

**•** Field updates that are executed as approval actions don’t trigger workflow rules or entitlement processes.

**•** These fields aren’t available for field update actions:

**–** Read-only fields like formula or auto-number fields

**–** The `Language` picklist field on multilingual solutions

**–** Some activity fields, such as `Related To` and `Private`

**•** Email message workflow rules can only be associated with field updates.

**•** If a field update references a specific user, you can't deactivate that user. For example, if your field update is designed to change the
owner of a record to Bob Smith, change the field update before deactivating Bob Smith.

**•** You can update long text area fields, but the option to insert `A specific value` restricts you to entering up to the maximum
number of characters allowed in the destination field.

**•** You can't make a field universally required if it's used by a field update that sets the field to a blank value.

**•** Workflow rules that update owners _don’t_ also transfer associated items. To ensure transfer, click **Change** next to the owner’s name
in a record and make your transfer selections.

##### Cross-Object Field Updates

For all custom objects and some standard objects, you can create actions where a change to a detail record updates a field on the
related main record. Cross-object field updates work for custom-to-custom master-detail relationships, custom-to-standard
master-detail relationships, and a few standard-to-standard master-detail relationships.

Field Updates That Reevaluate Workflow Rules
If `Re-evaluate Workflow Rules After Field Change` is enabled for a field update action, and a field update
results in a change to the value of the field, Salesforce reevaluates all workflow rules on the object.

SEE ALSO:

##### Cross-Object Field Updates Cross-Object Field Updates

For all custom objects and some standard objects, you can create actions where a change to a detail
record updates a field on the related main record. Cross-object field updates work for
custom-to-custom master-detail relationships, custom-to-standard master-detail relationships, and
a few standard-to-standard master-detail relationships.

[other]: Where possible, we changed noninclusive terms to align with our company value
of Equality. We maintained certain terms to avoid any effect on customer implementations.

For example, in a custom recruiting application, create a workflow rule that sets the status of an
application (the main object) to “Closed” when a candidate (the detail object) accepts the job. Or,
for standard objects, create a rule to change the status of a case from “Awaiting Customer Response”
to “In Progress” when a customer adds a case comment.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Custom Object to Custom Object

Cross-object field updates are supported for all custom objects that are children of custom objects in a master-detail relationship.

Custom Object to Standard Object

Cross-object field updates are supported for custom objects that are children of certain standard objects in a master-detail relationship.
The standard objects that support cross-object field updates from custom objects are:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contact

**•** Contract

**•** Contract Line Item

**•** Entitlement

**•** Opportunity

**•** Order

**•** Question

**•** Quote

**•** Service Contract

**•** Solution

Standard Object to Standard Object

Cross-object field updates are supported for standard objects that are children of standard objects in a master-detail relationship. However,
only these standard-to-standard relationships are supported.

Note: If you have workflow rules on converted leads and want to use cross-object field updates on the resulting accounts and
opportunities, you must enable the lead setting `Require Validation for Converted Leads` .

**•** Case Comments updating Case

**•** Email updating Case

Tip: To create workflow rules so that case comments or emails automatically update fields on associated cases, select **Case**
**Comment** or **Email Message** in the Object dropdown list when creating a workflow rule and select **Case** in the Field to Update
list. Email-to-Case or On-Demand Email-to-Case must be enabled for your organization to use the Email Message in a workflow
rule.

**•** Opportunity Product updating Opportunity

Note: Cross-object field updates to a parent opportunity's `Amount` and `Quantity` fields only work if the opportunity
has no opportunity products associated with it.

**•** Opportunity updating Account—Supported for both business accounts and person accounts.

Standard-to-standard cross-object field update actions:

**•** Can’t be used in, or assigned to, approval processes.

**•** Update a parent record even if the user doesn’t have edit access to it.


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Note: If you have Apex code that updates parent fields in the same relationships as a cross-object field update action, consider
replacing your code with cross-object field updates. Otherwise, both will fire, and since workflow rules run after Apex triggers, the
workflow field update will override any change made by your Apex code.

SEE ALSO:

Considerations for Field Update Actions

[Object Relationships Overview](https://help.salesforce.com/s/articleView?id=sf.overview_of_custom_object_relationships.htm&language=en_US)

##### Field Updates That Reevaluate Workflow Rules

If `Re-evaluate Workflow Rules After Field Change` is enabled for a field
update action, and a field update results in a change to the value of the field, Salesforce reevaluates
all workflow rules on the object.

**•** If the field update changes the field’s value, all workflow rules on the associated object are
reevaluated. Any workflow rules whose criteria are met as a result of the field update are
triggered.

**•** If any of the triggered workflow rules result in another field update that’s also enabled for
workflow rule reevaluation, a domino effect occurs, and more workflow rules can be reevaluated
as a result of the newly triggered field update. This cascade of workflow rule reevaluation and
triggering can happen up to five times after the initial field update that started it.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Make sure that your workflow rules aren’t set up to create recursive loops. For example, if a field update for Rule1 triggers Rule2, and
a field update for Rule2 triggers Rule1, the recursive triggers can cause your organization to exceed its limit for workflow time triggers
per hour.

**•** In a batch update, workflow is only retriggered on the entities where there’s a change.

**•** Only workflow rules on the same object as the initial field update are reevaluated and triggered.

**•** Only workflow rules that didn’t fire before are retriggered.

**•** Cross-object workflow rules aren’t candidates for reevaluation.

**•** Cross-object field updates that cause a field value to change don’t trigger workflow rule reevaluation on the associated object.

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** Time-dependent actions aren't executed for a reevaluated workflow rule in the following situations:

**–** The reevaluated workflow rule’s immediate actions cause the record to no longer meet the workflow rule criteria.

**–** An Apex `after` trigger that is executed as a result of a workflow or approvals action causes the record to no longer meet the
workflow rule criteria.

SEE ALSO:

Considerations for Field Update Actions


## Automate Your Business Processes with Salesforce Flow Approval Processes

#### Considerations for Outbound Messages

Review the considerations for using outbound message actions before implementing them in your
workflows.

When creating outbound messages for workflow rules or approval processes, keep these
considerations in mind.

**•** A single SOAP message can include up to 100 notifications. Each notification contains an ID
that uniquely identifies a record, and a reference to the data in the record. If the information in
the record changes after the notification is sent, but before the notification is delivered, only
the updated information is delivered. If the record is deleted before the notification is delivered,
the notification contains no data.

**•** Messages are queued until they’re sent, to preserve message reliability.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If the endpoint is unavailable, messages stay in the queue until sent successfully or until they’re 24 hours old. After 24 hours, messages
are dropped from the queue.

**•** If a message can't be delivered, the interval between retries increases exponentially, up to a maximum of two hours between retries.

**•** Messages are retried independent of their order in the queue, which can result in messages being delivered out of order.

**•** A message can be delayed by other, long-running messages in the queue. The queue can also contain messages that originate from
other Salesforce orgs that are hosted on the same Salesforce instance. The system attempts to optimize the execution of messages
that historically have fast run times so that they aren’t delayed by slow-running messages. To get the best performance, make sure
that the message endpoint runs efficiently. For slow-running messages, consider using asynchronous processes, such as platform
events or Apex future methods.

**•** You can't build an audit trail using outbound messages. While each message is delivered at least one time, it can be delivered more
than one time. Also, if delivery can’t be done within 24 hours, the message doesn’t get delivered at all. Finally, as noted above, the
source object can change after a notification is sent but before it’s delivered, so the endpoint will only receive the latest data, not
any intermediate changes.

SEE ALSO:

_[Platform Events Developers Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm)_

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm)_ : Future Annotation

## Approval Processes

It’s likely that you’re familiar with process automation in the form of workflow rules. Approval
processes take automation one step further, letting you specify a sequence of steps that are required
to approve a record.

An approval process automates how records are approved in Salesforce. An approval process
specifies each step of approval, including from whom to request approval and what to do at each
point of the process.

Example: Your org has a three-tier process for approving expenses. This approval process
automatically assigns each request to right person in your org, based on the amount requested.

If an expense record is submitted for approval, lock the record so that users can’t edit it and
change the status to Submitted.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

### Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

If the amount is $50 or less, approve the request. If the amount is greater than $50, send an approval request to the direct manager.
If the amount is greater than $5,000 and the first approval request is approved, send an approval request to the vice president.

If all approval requests are approved, change the status to Approved and unlock the record. If any approval requests are rejected,
change the status to Rejected and unlock the record.

### Set Up an Approval Process

If Approvals is the right automation tool for your business process, follow these high-level steps to create one for your org.

Prepare Your Org for Approvals
Make sure that your users can submit their records for approval, and consider how you can make it easy for approvers to respond
to approval requests.

Limits and Considerations for Approvals
Before you automate something with an approval process, be aware of the limits and considerations.

Sample Approval Processes
Review samples of common approval processes to help you get started creating your own.

Approval History Reports
If you create a custom report type for approval process instances, users can view the historical details of completed and in-progress
approval processes and their individual steps.

Manage Multiple Approval Requests
Transfer multiple approval requests from one user to another or remove multiple approval requests from the approval process.

Approval Requests for Users
Your admin can set up approval processes that let you and other users submit records for approval, which results in _approval requests_ .

Approval Process Terminology
Salesforce uses this terminology for approval processes.

### Set Up an Approval Process

If Approvals is the right automation tool for your business process, follow these high-level steps to
create one for your org.

1. Prepare to Create an Approval Process
Plan each approval process carefully to ensure a successful implementation.

2. Choose the Right Wizard to Create an Approval Process
Before you create an approval process, determine which wizard is best for your needs.

3. Add an Approval Step to an Approval Process
Approval steps define the chain of approval for a particular approval process. Each step
determines which records can advance to that step, who to assign approval requests to, and
whether to let each approver’s delegate respond to the requests. The first step specifies what
to do if a record doesn’t advance to that step. Later steps specify what happens if an approver
rejects the request.

4. Add Automated Actions to an Approval Process
You can associate actions to approval steps, initial submission, final approval, final rejection, or
recall. Approval processes support four automated actions.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

5. Activate an Approval Process
After you’ve created at least one step for the approval process, activate the process.

SEE ALSO:

Approval Process Terminology

Sample Approval Processes

Prepare Your Org for Approvals

#### Prepare to Create an Approval Process

Plan each approval process carefully to ensure a successful implementation.

Review the following checklist before creating your approval process.

**•** Prepare an approval request email template.

**•** Prepare an approval request post template.

**•** Determine the approval request sender.

**•** Determine the assigned approver.

**•** Determine the delegated approver.

**•** Decide if your approval process needs a filter.

**•** Design initial submission actions.

**•** Decide if users can approve requests from a wireless device.

**•** Determine if users can edit records that are awaiting approval.

**•** Decide if records should be auto-approved or rejected.

**•** Determine how many levels your process has.

**•** Determine the actions when an approval request is approved or rejected.

Which email template do you want to use for approval requests?

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

The email template you specify on an approval process is used when notifying users that an approval request is assigned to them. You
can use the Salesforce default email template or create your own template. Include the appropriate approval process merge fields to
link directly to the approval request. Does your org have email approval response enabled? If so, the default email template includes
instructions for replying to an approval request. Type _`approve`_, _`approved`_, _`yes`_, _`reject`_, _`rejected`_, or _`no`_ in the first line of
the email body and add comments in the second line.

Which Chatter post template do you want to use for approval requests?

If your org has Approvals in Chatter enabled, specify an approval post template to use when notifying a user via Chatter about an assigned
approval request. You can use the Salesforce default post template or create your own.

Who is the sender of approval requests?

Approval request notifications are sent from the user who submitted the record for approval. When you configure an email alert, you
can add a different return email address for these notifications. You can choose the email address of the default workflow user or a
previously configured and verified org-wide address. Determine which email address to use.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Who can approve requests?

Any of the following can approve or reject a request.

**•** A user or queue that the approval request submitter chooses.

**•** A queue specified by the administrator.

**•** A user listed in the `Manager` standard field on the submitter’s user detail page.

**•** A user listed in a custom hierarchy field on the submitter’s user detail page.

**•** Any combination of users and related users (users listed in a standard or custom field on the submitted record) specified by the
administrator.

Do you want approval requests delegated to another user for approval?

An approver can designate a delegate to approve requests, but you can disable this option. To assign delegates, populate the `Delegated`
`Approver` field for each user’s detail page.

Note: Internal Salesforce users are listed by and can be added using the Delegated Approver lookup field. Use Data Loader and
a comma-delineated (CSV) file to add users with communities licenses as Delegated Approvers. The CSV uses the

`CommunityUserId` rather than the `UserId` for `DelegatedApproverId` . Communities licenses are used with Experience
Cloud sites and legacy portals.

Which records are included in this process?

Determine what attributes a record must have to be included in your approval process. If necessary, create the custom fields to store
this information so that you can use it in your filter criteria. For example, if you want to include expense records from your headquarters
office only, create a custom picklist field called `Office Location` that has two options: “HQ” and “Field.” Then, you would specify
in your filter criteria that records must have “HQ” in the `Office Location` field to be included in the approval process.

What happens when a record is first submitted for approval?

When users submit a record for approval, Salesforce automatically locks the record so that other users can’t change it while it’s awaiting
approval. You can still add campaign members to campaigns locked for approval.

Decide if you want other workflow actions to happen when a record is first submitted, such as email alerts, tasks, field updates, and
outbound messages. These actions become your initial submission actions.

Can users approve requests from a mobile device?

Determine if you want to require users to log in to Salesforce to approve requests. You can also set up your approval process to allow
users to approve requests remotely using a mobile browser.

Who can edit records that are awaiting approval?

Records submitted for approval are locked. Users with the “Modify All” object-level permission for the given object or the “Modify All
Data” permission can always unlock a record and edit it. You can also specify that the currently assigned approver can edit the record.
You can still add campaign members to campaigns locked for approval.

Can records be automatically approved, rejected, or skipped based on certain criteria?

You can set entry criteria for each step of your process. Configure Salesforce to approve, reject, or skip the process if a record doesn’t
meet the criteria. For example, all expenses submitted with an `Amount` less than $15 are automatically approved.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

How many people have to approve these requests?

An approval process can have several layers of approvals. Determine how many users have to approve requests and in what order.

What happens when a request is approved or rejected?

When a request is recalled, approved, or rejected, Salesforce can perform up to 10 instances of each of the following types of actions—up
to 40 actions total. You can also configure up to 40 actions to occur when a record has received all necessary approvals or is rejected.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals

Sample Approval Processes

#### Choose the Right Wizard to Create an Approval Process

Before you create an approval process, determine which wizard is best for your needs.

##### Create an Approval Process with the Jump Start Wizard

For approval processes that use a single step, use the jump start wizard. This wizard chooses
some default options for you.

Default Selections for the Approval Process Jump Start Wizard
To make it easier for you to get started with a simple approval process, the jump start wizard
automatically chooses some default options for you.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Create an Approval Process with the Standard Wizard
When your approval process is more complex and you want to define specific steps, use the standard wizard.

SEE ALSO:

Set Up an Approval Process

##### Create an Approval Process with the Jump Start Wizard

For approval processes that use a single step, use the jump start wizard. This wizard chooses some
default options for you.

**1.** From Setup, enter _`Approval Processes`_ in the `Quick Find` box, then select **Approval**
**Processes** .

**2.** Select an object.

**3.** Select **Create New Approval Process** - **Use Jump Start Wizard** .

**4.** Configure the approval process by following the wizard.

**a.** Default Selections for the Approval Process Jump Start Wizard

**b.** Choose Approval Request Notification Templates

**c.** Design the Approval Request Page

**d.** Control Which Records Apply to an Approval Process


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

**e.** Identify Assigned Approvers for an Approval Step

SEE ALSO:

##### Default Selections for the Approval Process Jump Start Wizard

Considerations for Configuring Approvals

Considerations for Setting Approvers

Set Up an Approval Process

Choose the Right Wizard to Create an Approval Process

##### Default Selections for the Approval Process Jump Start Wizard

To make it easier for you to get started with a simple approval process, the jump start wizard
automatically chooses some default options for you.

After creating an approval process using the jump start wizard, you can modify these default options
and add more steps from the approval process detail page. Exception: you can’t modify the Record
Lock action on the Initial Submission Actions list.

**•** To edit records awaiting approval in the approval process, users must have the “Modify All”
permission for the given object or the Modify All Data permission.

**•** The page layout for the approval request includes the record name (or number), owner, date
created, and approval history.

**•** The security settings require approvers to log in to Salesforce to view the approval page.

**•** Only the owner of the record can submit the record for approval.

**•** Records are locked when submitted for approval.

**•** Records remain locked until approved or rejected.

**•** Rejected records are unlocked.

**•** Only admins can recall a record after it’s submitted.

**•** There are no auto-approve or auto-reject actions.

**•** No email notification is sent upon approval or rejection.

**•** No field values are automatically updated during the approval process.

**•** An approver can’t automatically delegate another user to approve the approval requests.

**•** The **Allow submitters to recall approval requests** option isn’t selected.

SEE ALSO:

Create an Approval Process with the Jump Start Wizard

Choose the Right Wizard to Create an Approval Process


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

##### Create an Approval Process with the Standard Wizard

When your approval process is more complex and you want to define specific steps, use the standard
wizard.

From Setup, enter _`Approval Processes`_ in the `Quick Find` box, then select **Approval**
**Processes** .

Select an object, and then select **Create New Approval Process** - **Use Standard Setup Wizard** .
Configure the approval process.

###### 1. Control Which Records Apply to an Approval Process

Narrow down the list of records that can be part of the approval process by specifying criteria.
You can either use filters or write a formula.

2. Choose Approval Request Notification Templates
When an approval process assigns an approval request to a user, Salesforce sends the user an
approval request email. If Approvals in Chatter is enabled, Salesforce also posts the approval
request to Chatter. Choose templates for each of these notifications.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

3. Choose an Automated Approver Throughout an Approval Process
Associate a hierarchy field—such as the user’s manager—with an approval process. When selected, the field is available as an
assigned approver option for approval steps. You can always select a hierarchy field here but not use it for any approval steps.

4. Specify Who Can Edit Locked Records
When a record is submitted for approval, it’s locked to prevent users from editing it during the approval process. Use the record
editability properties to determine who can edit records that are locked in this approval process.

5. Design the Approval Request Page
The approval page is where an approver responds to an approval request. Customize which fields appear on that page and in which
order. This page is used only for this approval process.

6. Specify Who Can Submit Records to an Approval Process
Only specified individuals or roles can submit a record for approval. You can also let submitters recall an approval request.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals

###### Control Which Records Apply to an Approval Process

Narrow down the list of records that can be part of the approval process by specifying criteria. You
can either use filters or write a formula.

If you want all records to pass through the approval process, click Next. If only certain types of
records are considered, use one of the following options.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Example: This filter lets an expense report enter this approval process only if the employee who submitted the report is at
headquarters.

```
   Current User: Office Location Equals Headquarters

```

This formula lets a record enter this approval process only if its discount approval cutoff date is less than 30 days away.

```
   (Discount_Approval_CutoffDate__c < (CloseDate - 30)

```

SEE ALSO:

Considerations for Configuring Approvals

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Choose Approval Request Notification Templates

When an approval process assigns an approval request to a user, Salesforce sends the user an
approval request email. If Approvals in Chatter is enabled, Salesforce also posts the approval request
to Chatter. Choose templates for each of these notifications.

These fields are available from both the jump-start and standard wizards.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Note: If email approval response is enabled, be sure that the email template you use describes how to correctly use both response
options: clicking the link and replying by email. If the user doesn’t respond correctly (for example, if the user misspells _`approve`_
or types it on the wrong line), Salesforce doesn’t register the user’s response.

SEE ALSO:

Chatter Post Templates for Approval Requests

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Merge Fields for Approvals

###### Choose an Automated Approver Throughout an Approval Process

Associate a hierarchy field—such as the user’s manager—with an approval process. When selected,
the field is available as an assigned approver option for approval steps. You can always select a
hierarchy field here but not use it for any approval steps.

Set **Next Automated Approver Determined By** with one of the following options.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: If you select the `Manager` field, you can configure any step in this process to route approval requests to the submitting
user’s manager.

If you select **Use Approver Field of** _`Object`_ **Owner**, the first step that isn’t skipped is routed to the owner’s manager. All other
steps are routed to the previous approver’s manager.

SEE ALSO:

[Custom Field Types](https://help.salesforce.com/s/articleView?id=sf.custom_field_types.htm&language=en_US)

Considerations for Setting Approvers


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

###### Specify Who Can Edit Locked Records

When a record is submitted for approval, it’s locked to prevent users from editing it during the
approval process. Use the record editability properties to determine who can edit records that are
locked in this approval process.

Note:

**•** Even when a campaign is locked for approval, users can add campaign members to it.

**•** In Lightning Experience, you can't unlock Knowledge articles during an approval process.

###### Design the Approval Request Page

The approval page is where an approver responds to an approval request. Customize which fields
appear on that page and in which order. This page is used only for this approval process.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

###### Specify Who Can Submit Records to an Approval Process

Only specified individuals or roles can submit a record for approval. You can also let submitters
recall an approval request.

Initial Submitters

Page Layout Settings

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Submission Settings

#### Add an Approval Step to an Approval Process

Approval steps define the chain of approval for a particular approval process. Each step determines
which records can advance to that step, who to assign approval requests to, and whether to let
each approver’s delegate respond to the requests. The first step specifies what to do if a record
doesn’t advance to that step. Later steps specify what happens if an approver rejects the request.

You can add steps to an approval process only if it’s inactive.

From the approval process, click **New Approval Step**, and follow the wizard.

Steps are executed in the order specified.

1. Control Which Records Apply to an Approval Step
Control which records are part of the approval step by setting the step’s criteria. You can also
specify what happens to records that don’t meet the step’s criteria.

2. Identify Assigned Approvers for an Approval Step
Specify who to send an approval request for this step to.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval steps:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

3. Specify Rejection Behavior for an Approval Step
Configure what happens if an approver rejects a request. The final rejection actions for the approval process determine the first step’s
rejection behavior.

SEE ALSO:

Set Up an Approval Process

Enable Email Approval Response

##### Control Which Records Apply to an Approval Step

Control which records are part of the approval step by setting the step’s criteria. You can also specify
what happens to records that don’t meet the step’s criteria.

Criteria Options

If all records go through this approval step, leave **All records should enter this step** selected.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If only certain types of records are supposed to enter this process, select **Enter this step if the following...** and choose the appropriate
option (1). For details on the options, see Control Which Records Apply to an Approval Process.

(2) Else Options for Approval Step Criteria

If you specified filter criteria or entered a formula, choose what happens to records that don’t meet the criteria or if the formula doesn’t
return `True` .

Note: You can’t change your selection after the approval process has been activated, even if you deactivate the approval process.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

SEE ALSO:

Set Up an Approval Process

Enable Email Approval Response

##### Identify Assigned Approvers for an Approval Step

Specify who to send an approval request for this step to.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

SEE ALSO:

Considerations for Setting Approvers

##### Specify Rejection Behavior for an Approval Step

Configure what happens if an approver rejects a request. The final rejection actions for the approval
process determine the first step’s rejection behavior.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

#### Add Automated Actions to an Approval Process

You can associate actions to approval steps, initial submission, final approval, final rejection, or
recall. Approval processes support four automated actions.

Example: When expenses are approved, you want to print checks for payment. To do so, you add an outbound message, which
sends the appropriate information to your Oracle accounting service, as a Final Approval action.

Groups of Automated Actions in an Approval Process
Each approval process is organized into groups of actions based on when the actions occur, such as initial submission. To add an
automated action to your approval process, determine which group of actions to add it to.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Add an Automated Action to Your Approval Process
If you didn’t create an automated action before configuring your approval process, you can create one directly from the approval
process.

Add an Existing Automated Action to Your Approval Process
If you’ve already created an automated action, you can add it to your approval process.

SEE ALSO:

Set Up an Approval Process

Automated Actions

Considerations for Automated Actions

##### Groups of Automated Actions in an Approval Process

Each approval process is organized into groups of actions based on when the actions occur, such
as initial submission. To add an automated action to your approval process, determine which group
of actions to add it to.

SEE ALSO:

Considerations for Automated Actions


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

##### Add an Automated Action to Your Approval Process

If you didn’t create an automated action before configuring your approval process, you can create
one directly from the approval process.

**1.** Open the approval process that you want to add an action to.

**2.** From the appropriate related list, click **Add New** . For an approval step where the Approval
Actions and Rejection Actions are hidden, click **Show Actions** .

**3.** Choose the type of action.

The list of available actions differs depending on your settings and whether you’ve reached the
limit for a type of action.

**4.** Configure the action.

SEE ALSO:

Set Up an Approval Process

Considerations for Automated Actions

Groups of Automated Actions in an Approval Process

##### Add an Existing Automated Action to Your Approval Process

If you’ve already created an automated action, you can add it to your approval process.

**1.** Open the approval process that you want to add an action to.

**2.** From the appropriate related list, click **Add Existing** . If that button is hidden, click **Show Actions** .

**3.** Choose the type of action.

**4.** Move the action from Available Actions to Selected Actions.

**5.** Save your changes.

SEE ALSO:

Groups of Automated Actions in an Approval Process

Considerations for Automated Actions


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval actions:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To select approval actions:

**•** Customize Application

### Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

#### Activate an Approval Process

After you’ve created at least one step for the approval process, activate the process.

**1.** Open the approval process.

**2.** Make sure that it’s configured correctly.

#### 3. Click Activate .

SEE ALSO:

### Prepare Your Org for Approvals

Considerations for Managing Approvals

### Prepare Your Org for Approvals

Make sure that your users can submit their records for approval, and consider how you can make
it easy for approvers to respond to approval requests.

Let Users Submit for Approval
After you activate an approval process for an object, customize the object’s page layouts to
support record submission.

Override the Sender for Email Approval Notifications
By default, the sender for email approval notifications is the user who submitted the record for
approval. You can override the sender with an organization-wide address, like
approval@acmewireless.com.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To activate approval
processes:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Let Users Respond to Approval Requests from Your Org
Give your users an instant view of their approval requests by customizing the Home page or navigation bar.

Let Users Respond to Approval Requests by Email
If the email notification includes all the information that an approver must decide, enable email approval response. That way, a user
can simply reply to the email notification.

Let Users Respond to Approval Requests from Chatter
If your users don’t need in-depth information to decide how to respond to an approval request, enable Approvals in Chatter. That
way, they don’t have to leave their feed to continue with their day-to-day tasks.

Let Users Respond to Approvals Requests in Slack
If your users don’t need in-depth information to decide how to respond to an approval request, and they have a connection to Slack,
enable Approvals in Slack. That way, a user can simply respond to the Slack notification.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

#### Let Users Submit for Approval

After you activate an approval process for an object, customize the object’s page layouts to support
record submission.

Add the following components to your page layouts.

**•** Submit for Approval button

**•** Approval History related list

The Approval History related list lets users submit approval requests and track a record’s progress
through an approval process from the record detail page.

SEE ALSO:

[Page Layouts](https://help.salesforce.com/s/articleView?id=sf.customize_layout.htm&language=en_US)

Prepare Your Org for Approvals

#### Override the Sender for Email Approval Notifications

By default, the sender for email approval notifications is the user who submitted the record for
approval. You can override the sender with an organization-wide address, like
approval@acmewireless.com.

**User Permissions Needed**

To edit process automation settings: Customize Application

To create, update, and delete flow list views: Manage Flow

After you add an organization-wide address to your org:

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To modify page layouts:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**1.** From Setup, enter _`Process Automation Settings`_ in the Quick Find box, then select **Process Automation Settings** .

**2.** For Email Approval Sender, select the organization-wide address.

**3.** Save your changes.

#### Let Users Respond to Approval Requests from Your Org

Give your users an instant view of their approval requests by customizing the Home page or
navigation bar.

Lightning Experience:

**•** Add the Items to Approve component to the appropriate Lightning Home pages.

This component is available only for Home pages. To add it to a Home page, use the Lightning
App Builder in Setup.

**•** Add the Approval Requests navigation item to the appropriate Lightning apps.

This item is available only for Lightning apps. To add it to a Lightning app, use the App Manager
in Setup.

Salesforce mobile app:


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

Add the Approvals item to the navigation items of any Lightning app.

Salesforce Classic:

Add the Items to Approve related list to the appropriate home page layouts.

SEE ALSO:

[Create Lightning Apps](https://help.salesforce.com/s/articleView?id=sf.apps_lightning_create.htm&language=en_US)

[Set Up the Lightning Experience Home Page](https://help.salesforce.com/s/articleView?id=sf.admin_home_lex_intro.htm&language=en_US)

[Salesforce Classic Home Tab Page Layouts](https://help.salesforce.com/s/articleView?id=sf.customize_homepage.htm&language=en_US)

Prepare Your Org for Approvals

#### Let Users Respond to Approval Requests by Email

If the email notification includes all the information that an approver must decide, enable email
approval response. That way, a user can simply reply to the email notification.

##### Considerations for Email Approval Response

Before you enable the ability to act on approvals via email, review how email works with your
approval processes.

Default Template for Email Approval Response
When you enable email approval response, Salesforce uses a default email template for approval
processes—unless you specify a custom email template.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Enable Email Approval Response
After you’ve reviewed the considerations and prepared the right template, flip the switch that lets users respond to approval requests
directly from their email.

SEE ALSO:

Prepare Your Org for Approvals

Let Users Respond to Approval Requests from Chatter

##### Considerations for Email Approval Response

Before you enable the ability to act on approvals via email, review how email works with your
approval processes.

Compatibility with Approval Processes

Email approval response isn’t supported for approval processes that:

**•** Assign approval to a queue

**•** After the first step, let the approver manually select the next approver

Implicit Agreement with Salesforce

By enabling the email approval response feature, you agree to let Salesforce:

**•** Process email approval responses


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** Update approval requests for all active users in your org

**•** Update the approval object on behalf of your org’s users

SEE ALSO:

Limits and Considerations for Approvals

Let Users Respond to Approval Requests by Email

##### Default Template for Email Approval Response

When you enable email approval response, Salesforce uses a default email template for approval
processes—unless you specify a custom email template.

Example: _`Requesting User`_ has requested your approval for the following item.

To approve or reject this item, reply to this email with the word APPROVE, APPROVED, YES,
REJECT, REJECTED, or NO in the first line of the email message, or click this link:

```
  Link to approval request page

```

If replying via email you can also add comments on the second line. The comments are stored
with the approval request in Salesforce CRM.

Note: For Salesforce to process your response the word APPROVE, APPROVED, YES, REJECT,
REJECTED, or NO must be in the first line of the reply email. Also, any comment must be in
the second line.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If your org has Approvals in Chatter enabled and the approver opted to receive notifications as Chatter posts, the default email template
is appended with:

Example: You can also approve, reject, and comment on this request from your Chatter feed:

```
  Link to approval post in Chatter

```

Note: If you use a custom email template for your approval process, make sure that it explains both response options: clicking
the link and replying by email. If the user doesn’t respond correctly (for example, if the user misspells approve or types it on the
wrong line), Salesforce doesn’t register the response.

SEE ALSO:

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Merge Fields for Approvals

Let Users Respond to Approval Requests by Email


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

##### Enable Email Approval Response

After you’ve reviewed the considerations and prepared the right template, flip the switch that lets
users respond to approval requests directly from their email.

Before you begin, give the appropriate users the “API Enabled” user permission so that they can
respond to approval requests by email.

**1.** From Setup, enter _`Process Automation Settings`_ in the `Quick Find` box, then
select **Process Automation Settings** .

**2.** Select **Enable email approval response** .

**3.** Save your changes.

SEE ALSO:

Considerations for Email Approval Response

Let Users Respond to Approval Requests by Email

#### Let Users Respond to Approval Requests from Chatter

If your users don’t need in-depth information to decide how to respond to an approval request,
enable Approvals in Chatter. That way, they don’t have to leave their feed to continue with their
day-to-day tasks.

Prepare to Enable Approvals in Chatter
Because Approvals in Chatter relies on both Chatter and the Approvals feature, getting your
org set up involves more than just turning on the feature. Before you enable Approvals in
Chatter, understand the limitations and considerations for Approvals in Chatter and post
templates.

Considerations for Approvals in Chatter
Find out more about Approvals in Chatter, before you enable it.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable Email Approval
Response:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Enable Approvals in Chatter
If your organization has both Approvals and Chatter enabled, administrators can turn on Approvals in Chatter. Users then receive
approval requests as posts in their Chatter feeds.

Where Do Approval Request Posts Appear?
When your org has Approvals in Chatter enabled, approval request posts appear in various Chatter feeds. To see the approval request
post, you must have access to the approval record.

Chatter Post Templates for Approval Requests
Approval post templates for Chatter let you customize the information that is included in the approval request post when it displays
in a Chatter feed.


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

##### Prepare to Enable Approvals in Chatter

Because Approvals in Chatter relies on both Chatter and the Approvals feature, getting your org
set up involves more than just turning on the feature. Before you enable Approvals in Chatter,
understand the limitations and considerations for Approvals in Chatter and post templates.

Do the following for each object for which you want approval requests to appear in Chatter.

**1.** Enable feed tracking.

**2.** Create an approval post template.

Tip: For each object, create one post template that works for all approval processes. Mark
that post template the default for the object.

SEE ALSO:

[Feed Tracking](https://help.salesforce.com/s/articleView?id=sf.collab_feed_tracking_overview.htm&language=en_US)

Chatter Post Templates for Approval Requests

Where Do Approval Request Posts Appear?

##### Considerations for Approvals in Chatter Considerations for Approvals in Chatter

Find out more about Approvals in Chatter, before you enable it.

**•** When you enable Approvals in Chatter in your org, it’s turned on for all users. Users can then
update their own Chatter settings to opt out of receiving approval requests as posts in their
Chatter feeds.

**•** Chatter post approval notifications are available only for approval processes associated with an
object that has been enabled for feed tracking.

**•** If the approval object is a detail object in a master-detail relationship, `Owner` isn’t available
for approval page layouts or approval post templates.

Limitations

**•** Approvals in Chatter doesn't support delegated approvers or queues.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** You can’t recall or reassign an approval request from a post. Instead, perform these actions from the approval record.

**•** Approval requests from Sites or portal users aren’t supported.

Approval Posts

**•** Approval posts can't be deleted in the Salesforce user interface; you can only delete them through the API.

**•** If you don’t select an approval post template, the approval post uses the system default template or the default template for the
object, if available.

**•** Only users with access to the approval record can see the approval request post. Comments on approval posts aren’t persisted to
the approval record.

**•** Different users see different configurations of the approval request post.

**–** Only approvers see approval action buttons on their posts, and then only in their profile feed or their news feed.

**–** Only approvers see approver names in the header.


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** If you change the approver, step name, or the routing type on an approval process while it’s in progress, existing approval posts
aren’t updated.

**•** When an approval request is recalled, a new post is generated. It appears on the news feeds of the submitter, all approvers, and
followers of the object. It also appears on the record feed.

**•** If a step requires unanimous approval from multiple approvers, the approval request post for that step doesn’t list all selected
approvers in its header. Approvers see only their own name in the post header.

SEE ALSO:

Let Users Respond to Approval Requests by Email

Prepare to Enable Approvals in Chatter

##### Where Do Approval Request Posts Appear?

Limits and Considerations for Approvals

##### Enable Approvals in Chatter

If your organization has both Approvals and Chatter enabled, administrators can turn on Approvals
in Chatter. Users then receive approval requests as posts in their Chatter feeds.

Before you begin, make sure that all approval processes in your org are properly configured to take
advantage of Approvals in Chatter. After turning on this feature, all existing active approval processes
start generating Chatter posts.

**1.** From Setup, enter _`Chatter Settings`_ in the `Quick Find` box, then select **Chatter**
**Settings** .

**2.** Click **Edit** .

**3.** Select **Allow Approvals** .

**4.** Save your changes.

SEE ALSO:

Prepare to Enable Approvals in Chatter

Considerations for Approvals in Chatter

##### Where Do Approval Request Posts Appear? Where Do Approval Request Posts Appear?

When your org has Approvals in Chatter enabled, approval request posts appear in various Chatter
feeds. To see the approval request post, you must have access to the approval record.

Approval request posts show up in these feeds.

**•** Chatter feed of the assigned approver

**•** Submitter’s profile

**•** Chatter feed of the submitter if the submitter is following the approval request record

**•** Chatter feed of the approval request record

**•** Chatter feed of anyone following the approval request record

**•** Object-specific filter on the Chatter feed of anyone following the approval record


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable Approvals in
Chatter:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** Company filter of every user with access to the approval record

SEE ALSO:

What Happens When You Opt Out of Chatter Approval Requests?

Considerations for Approvals in Chatter

Let Users Respond to Approval Requests from Chatter

##### Chatter Post Templates for Approval Requests

Approval post templates for Chatter let you customize the information that is included in the
approval request post when it displays in a Chatter feed.

###### Considerations for Chatter Post Templates for Approval Requests

Keep these limitations and dependencies in mind when working with post templates.

Create a Chatter Post Template
Identify which fields to display in an approval request post.

SEE ALSO:

[Manage Deleted Custom Fields](https://help.salesforce.com/s/articleView?id=sf.fields_managing_deleted_fields.htm&language=en_US)

###### Considerations for Chatter Post Templates for Approval Requests

Keep these limitations and dependencies in mind when working with post templates.

Limitations

**•** The associated object must be enabled for approvals and feed tracking.

**•** If an approval post template is in use by an approval process, you can't delete it.

**•** Chatter posts for approval requests only appear in Salesforce Classic. To respond to approval
requests in Lightning Experience, users go to the Approval Requests tab.

Dependencies

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Deleting a custom field removes it from any approval post template that references it. Existing posts aren't affected. Undeleting the
custom field restores it to the available fields list, but doesn't restore it to any approval post templates that previously contained it.

**•** Deleting (or undeleting) a custom object also deletes (or undeletes) its associated approval post templates and any of its approval
request posts that are already in Chatter feeds.

**•** If you rename a custom object, approval post templates associated with it update accordingly.

SEE ALSO:

Create a Chatter Post Template

Limits and Considerations for Approvals


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

###### Create a Chatter Post Template

Identify which fields to display in an approval request post.

**1.** From Setup, enter _`Post Templates`_ in the `Quick Find` box, then select **Post**
**Templates** .

**2.** Click **New Template** .

**3.** Select the object for your template.

**4.** Click **Next** .

**5.** Give the template a name and description.

**6.** If you want this template to be the default for the associated object, select **Default** .

**7.** Add up to four fields to display on the approval request post.

We recommend putting any text-heavy fields—such as Comments or Description—at the
bottom.

**8.** Save your changes.

SEE ALSO:

Choose Approval Request Notification Templates

Considerations for Chatter Post Templates for Approval Requests

#### Let Users Respond to Approvals Requests in Slack

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval request
post templates:

**•** Customize Application

If your users don’t need in-depth information to decide how to respond to an approval request, and they have a connection to Slack,
enable Approvals in Slack. That way, a user can simply respond to the Slack notification.

##### Considerations for Approvals in Slack

Find out more about Approvals in Slack, before you enable it.

Enable Approval Notifications in Slack
If your org uses both Approvals and Salesforce Digital HQ app, approval notifications are automatically enabled in Slack. Users receive
approval requests as messages on the Salesforce Digital HQ’s Messages tab.

Where Do Slack Approval Notifications Appear?
When you have Approvals in Slack enabled, approval notifications are sent to the approver via the Salesforce Digital HQ app as a
direct message in Slack. To see the approval request post, you must have access to Slack.

##### Considerations for Approvals in Slack

Find out more about Approvals in Slack, before you enable it.

Users must have the Salesforce Digital HQ app in Slack. When you enable Approvals in Slack in your
org, it’s turned on for all users. Before you use Approvals in Slack, make sure you understand the
limitations.

**•** You can connect the Salesforce Digital HQ app to only one Salesforce org.

**•** The only available actions are Approve and Reject.

**•** The Show More link doesn’t work for Salesforce Classic users.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** If the approver has to manually select the next approver, they must log in to the full Salesforce site to complete the approval request.

**•** Users can respond only to approval requests without comments.

**•** Up to four fields only of an approval request can appear in a Slack notification.

##### Enable Approval Notifications in Slack

If your org uses both Approvals and Salesforce Digital HQ app, approval notifications are automatically
enabled in Slack. Users receive approval requests as messages on the Salesforce Digital HQ’s Messages
tab.

Note: Slack notifications are turned on automatically. Admins can turn off Slack notifications
from Setup on the Notification Delivery Settings page.

**1.** From Setup, in the Quick Find box, enter _`Notification Delivery Settings`_, and
select **Notification Delivery Settings** .

**2.** From the Approval requests dropdown menu, select **Edit** .

**3.** Select **Slack**, and enable **Salesforce Digital HQ** .

SEE ALSO:

[Salesforce for Slack](https://help.salesforce.com/s/articleView?id=sf.slack_apps_digital_hq.htm&language=en_US)

##### Where Do Slack Approval Notifications Appear?

When you have Approvals in Slack enabled, approval notifications are sent to the approver via the
Salesforce Digital HQ app as a direct message in Slack. To see the approval request post, you must
have access to Slack.

**•** Users review the request, and select **Approve** or **Reject**, or select **Show More** to be directed
to the Salesforce app to view details.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable approvals in
Slack:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Users can continue to receive email, Lightning Experience, and mobile notifications about approval requests.


### Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals Limits and Considerations for Approvals

Before you automate something with an approval process, be aware of the limits and considerations.

Users can’t see which approval process is triggered when they click **Submit for Approval** . Familiarize
users on the criteria for each approval process and what each approval process does. If the record
doesn’t meet the entry criteria or if they’re not an allowed submitter for any approval processes,
Salesforce displays an error.

#### Approval Limits

Salesforce limits the number of approval processes in your org, as well as the number of steps
and actions in each approval process.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Considerations for Configuring Approvals
When creating or editing an approval process, keep in mind how approvals are compatible with other features. Before you start,
draw out the steps of your approval process.

Merge Fields for Approvals
Approval merge fields include _`{!ApprovalRequest.fieldName}`_ and
_`{!Approval_Requesting_User.fieldName}`_ . They’re supported in certain email templates and return different values
based on the status of the approval process instance.

Considerations for Setting Approvers
When you specify approvers for a given approval step—or for the only step if you’re using the jump start wizard—keep these
considerations in mind.

Considerations for Managing Approvals
Keep these things in mind when maintaining existing approval processes—including activating and deleting them.

Considerations for the Salesforce Mobile App
Learn about the approvals functionality in Lightning Experience on desktop that isn’t available or that works differently in the
Salesforce mobile app.

SEE ALSO:

Considerations for Email Approval Response

Considerations for Approvals in Chatter

[Approvals: What’s Different or Not Available in the Salesforce Mobile App](https://help.salesforce.com/s/articleView?id=sf.limits_mobile_sf1_approvals.htm&language=en_US)

Considerations for Approval History Reports

[Restrictions for Approval Processes in Change Sets](https://help.salesforce.com/s/articleView?id=sf.changesets_restrictions_approval_process.htm&language=en_US)

#### Approval Limits

Salesforce limits the number of approval processes in your org, as well as the number of steps and
actions in each approval process.

**Per-Org Limit** **Value**

Active approval processes 1,000

Total approval processes 2,000

Active approval processes per object 300


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

**Per-Org Limit** **Value**

Total approval processes per object 500

Steps per approval process 30

Approvers per step 25

Initial submission actions per approval process [2] 40

Final approval actions per approval process [2] 40

Final rejection actions per approval process [2] 40

Recall actions per approval process [2] 40

Maximum characters in approval request comments

#### Considerations for Configuring Approvals

4,000

In Chinese, Japanese, or Korean, the limit is 1,333 characters.

When creating or editing an approval process, keep in mind how approvals are compatible with
other features. Before you start, draw out the steps of your approval process.

Associated Object

If the approval object is a detail object in a master-detail relationship, `Owner` isn’t available for
approval page layouts or approval post templates.

Approval Criteria

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

In approval criteria—either the entry criteria or step criteria—don’t reference expressions that
resolve to random values. That way, if the criteria must be evaluated again, the record is evaluated the same every time.

Compatibility with Other Features

**•** Flows can delete records that are pending approval.

**•** Design automated actions so that you can use them for both workflow rules and approval processes.

Field Update Actions in Approvals

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** Field updates that are executed as approval actions don’t trigger workflow rules or entitlement processes.

Anticipate Errors

Consider reviewing the content on approvals errors. That way, you can anticipate common issues and configure your approval process
so that the error is less likely.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Approvals in Unlocked Packages

**•** Unlocked packages can include Approvals with steps that reference related users or queues as approvers; users aren’t supported.

**•** Queues and related user fields (lookup fields) referenced by the approval steps must be included in the unlocked package.

**•** An Approval Process can only be included in unlocked packages that don’t have a specified namespace.

SEE ALSO:

What Does This Approvals Error Mean?

Set Up an Approval Process

Considerations for Automated Actions

Considerations for Chatter Post Templates for Approval Requests

#### Merge Fields for Approvals

Approval merge fields include _`{!ApprovalRequest.fieldName}`_ and
_`{!Approval_Requesting_User.fieldName}`_ . They’re supported in certain email
templates and return different values based on the status of the approval process instance.

Tip: The submitter isn’t always the current user. For custom email templates, use
_`{!Approval_Requesting_User.fieldName}`_ instead of
_`{!User.fieldName}`_ .

Where Are Approval Merge Fields Supported?

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can use approval process merge fields in email templates, but not mail merge templates. Except
for `{!ApprovalRequest.Comments}`, approval merge fields named `{!ApprovalRequest.field_name}` in email
templates return values only in approval assignment emails and email alerts for approval processes. When used in other emails—including
email alerts for workflow rules—the approval merge field returns `null` .

What Values Does a Merge Field Provide?

The generated value of an ApprovalRequest merge field depends on which step the approval process is in.

**•** In the approval request email, a merge field returns the submitter’s name and the name of the first step.

**•** When the request is approved, the merge field returns the most recent approver’s name and the name of the second step, if applicable.

**•** For subsequent actions, a merge field value returns the previous completed step.

**•** For an approval step that requires unanimous approval from multiple approvers, _`{!ApprovalRequest.Comments}`_ returns
only the most recently entered comment in emails.

SEE ALSO:

Default Template for Email Approval Response

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

#### Considerations for Setting Approvers

When you specify approvers for a given approval step—or for the only step if you’re using the jump
start wizard—keep these considerations in mind.

**•** Users with these permissions can respond to approval requests, even if they aren’t designated
approvers.

**–** Modify All Data

**–** Modify All for an object

**•** Make sure that the assigned approver has access to read the records for the approval requests.
For example, a user who can’t view expense records can’t view expense approval requests.

**•** Approval processes that let users select an approver manually also let users select themselves
as the approver.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** You can assign an approval request to the same user multiple times in a single step. However, Salesforce sends the user only one
request.

**•** In Lightning Experience, when an approval request has more than one assigned approvers, a `ProcessInstanceStep` is created
for each assigned approver. When the approval request has the Approval based on first response setting enabled, the values displayed
in `Assigned To` and `Actual Approver` are affected.

**–** Assigned to is set to an approver assigned to the record

**–** Actual Approver is set to the approver who approved the request

**•** Here’s what happens to the list of approvers after a record enters an approval step and the approval process later returns to that
step.

**–** If the user who responded isn’t in the designated approvers list and has either Modify All Data or Modify All permissions for the
object, that user replaces the original approver in the list of approvers.

**–** If a user who responded is in the designated approvers list, the list of approvers for that step doesn’t change. This behavior occurs
even if the field values that designate the approvers have changed.

For example, an approval process’s first step requests approval from a user’s manager. If the approval request is rejected in the second
step, the approval request returns to the first step. This table explores what happens to the list of approvers.

**•** A manager's manager is not an option for a designated approver.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Assigning Approval Steps to Queues

You can assign approval requests to a queue only if the associated object supports queues. Email approval response isn’t supported for
approval processes that assign approval to a queue.

When the assigned approver is a queue:

**•** Any queue member can approve or reject an approval request that is assigned to the queue.

**•** Approval request emails are sent to the queue email address. If the queue is set up to send email to members, approval request
emails get sent to the queue members, unless their approval user preferences are set to never receive approval request emails.

**•** Because email notifications to a queue aren’t intended for an external audience, `{!ApprovalRequest.External_URL}`
returns the equivalent internal URL.

**•** Salesforce mobile app notifications for approval requests aren’t sent to queues. For each approval step involving a queue, we
recommend adding individual users as assigned approvers, so at least those individuals can receive the approval request notifications
in the Salesforce mobile app. To have both queues and individual users as assigned approvers, select `Automatically assign`
`to approver(s)` instead of `Automatically assign to queue` in the approval step.

**•** When an approval request is rejected and returned to the previous approver and the previous approver was a queue, the approval
request is assigned to the user who approved it instead of the queue.

**•** The Approval History related list displays the queue name in the `Assigned To` column and the actual user who approved or
rejected the approval request in the `Actual Approver` column.

SEE ALSO:

Identify Assigned Approvers for an Approval Step

Limits and Considerations for Approvals

#### Considerations for Managing Approvals

Keep these things in mind when maintaining existing approval processes—including activating
and deleting them.

Admin Permissions

Users with one of these permissions are considered approval admins.

**•** Modify All object-level permission for the given object

**•** Modify All Data user permission

Approval admins can:

**•** Approve or reject pending approval requests without being part of the approval process

**•** Edit records that have been locked for approval

Activating Approval Processes

**•** An approval process must have at least one step before you can activate it.

**•** Before you activate your approval process, test it in your Salesforce sandbox.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** After an approval process is activated, you can’t add, delete, or change the order of the steps or change its reject or skip behavior,
even if the process is inactive.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Monitoring In-Flight Approval Processes

Standard reports for approval requests are included in both the Administrative Reports folder and the Activity Reports folder.

Deploying over Existing Approval Processes

When you deploy an approval process with no entry criteria to overwrite an existing approval process with entry criteria, then the entry
criteria from the existing process are applied to the deployed process.

Deleting Approval Processes

Before you delete an approval process:

**•** Make sure it’s inactive.

**•** Delete all approval requests that are associated with it, and remove them from the Recycle Bin.

**•** Delete all records, for example, accounts that were submitted through the approval process regardless of status. By deleting the
records, the associated _`ProcessInstanceWorkitem`_ and _`ProcessInstance`_ records are also deleted automatically.

**•** If you can't delete the approval process, try again after 2 days. Salesforce can take up to 2 days to delete the files that you removed
from the recycle bin.

SEE ALSO:

Activate an Approval Process

Manage Multiple Approval Requests

Limits and Considerations for Approvals

#### Considerations for the Salesforce Mobile App

Learn about the approvals functionality in Lightning Experience on desktop that isn’t available or
that works differently in the Salesforce mobile app.

Approval Responses

You can’t unlock a record that’s locked for approval.

Salesforce Mobile App Notifications for Approval Requests

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Notifications for approval requests aren’t sent to queues or delegates. For each approval step
involving a queue, add individual users as assigned approvers, so those individuals can receive the approval request notifications in
the mobile app. To have both queues and individual users as assigned approvers, select **Automatically assign to approver(s)**
instead of **Automatically assign to queue** in the approval step.

**•** Notifications for approval requests are sent only to users who have access to the record being approved. Assigned approvers who
don’t have record access can receive email approval notifications, but they can’t complete the approval request until someone grants
record access.

Approvals in Chatter

In the Salesforce mobile app, you can’t respond to approval requests from Chatter. To respond to approval requests, go to the Approvals
navigation item.


### Automate Your Business Processes with Salesforce Flow Sample Approval Processes

Approval Comments

**•** The Salesforce mobile app prompts you for comments after you tap Approve or Reject.

**•** The Approval History related list displays truncated comments. To see the full comment for a given approval instance, tap the instance,
then tap **Comments** .

Approval History Related List

**•** The Approval History related list doesn’t include the Submit for Approval button.

**•** When working with approvals in Experience Cloud sites, role-based external users can see and take action from the Approval History
related list, but they can’t submit requests for approval.

### Sample Approval Processes

Review samples of common approval processes to help you get started creating your own.

#### Sample Approval Process: PTO Requests

Most companies require employees to file a PTO (Paid Time Off) request and have their manager approve it. In three phases, here's
how to automate a simple one-step PTO request process using Salesforce.

Sample Approval Process: Expense Reports
If your company requires that employees file expense reports for managers to approve, you can automate this process in Salesforce.

Sample Approval Process: Discounting Opportunities
Opportunities that are discounted more than 40% require a CEO approval. Use this example to create a one-step approval process.

Sample Approval Process: Job Candidates
When your company interviews candidates for a position, you can have several levels of approval before you can send an offer letter.
Use this example to create a three-step approval process that requires approval from multiple management levels.

#### Sample Approval Process: PTO Requests

Most companies require employees to file a PTO (Paid Time Off) request and have their manager
approve it. In three phases, here's how to automate a simple one-step PTO request process using
Salesforce.

Prep Your Organization

Before creating the approval process:

**•** If you don’t yet have a custom object to track your PTO requests, create a custom object and
tab called PTO Requests. Add the appropriate fields for your PTO Requests such as `Start`
`Date`, `End Date`, and `Employee Name` .

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** To notify approvers about a pending approval request, create an email template. To direct users to the approval page in Salesforce,
include approval process merge fields.

Create the Approval Process

Use the jump start wizard to create an approval process for the PTO Request custom object and specify the following:


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

Tip: To let the submitter withdraw a submitted PTO request, click **Edit** and choose **Initial Submitters** . Then select `Allow`
`submitters to recall approval requests` .

**•** Select the email template you created for this approval process.

**•** Don't specify filter criteria. That way, PTO requests are included in this approval process regardless of their attributes.

**•** Select the `Automatically assign an approver using a standard or custom hierarchy field`
option, then choose `Manager` .

**•** The jump start wizard automatically chooses the record owner as the only person who can submit PTO requests.

Wrap Things Up

**•** After you created the approval process, add the Approval History related list to the PTO Request object page layout.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Create a Custom Object](https://help.salesforce.com/s/articleView?id=sf.dev_objectcreate_task_parent.html&language=en_US)

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Create an Approval Process with the Jump Start Wizard

Prepare Your Org for Approvals

#### Sample Approval Process: Expense Reports

If your company requires that employees file expense reports for managers to approve, you can
automate this process in Salesforce.

Use this example to create a two-step expense report approval process for all employees in your
headquarters office. It specifies that expenses less than $50 are automatically approved, expenses
$50 and over require manager approval, and expenses over $5,000 require additional approval from
two VPs. This example highlights a parallel approval process and the “else” option.

Prep Your Organization:

Before creating the approval process:

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If you don’t yet have a custom object to track your expenses, create a custom object and tab
called Expense Reports. Add the appropriate fields such as `Amount`, `Description`, `Status`, `Start Date`, and `End`
`Date` .

**•** Create a custom field on the user object `Office Location` . Assign the “HQ” value to users in the headquarters office location.

Create the Approval Process:

Create an approval process using the Expense Report custom object and specify the following:

**•** The filter criteria for this approval process is _`Current User: Office Location equals HQ`_ . Records must meet this
criteria before they can be submitted to this approval process.

**•** Choose the `Manager` field as the next automated approver.

**•** To notify approvers that their approval is requested, create an email template. To direct users to the approval page in Salesforce,
include approval process merge fields.

**•** Choose the record owner or any other user who you want to be able to submit expense reports.


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

**•** Create these approval steps.

**1.** Create a step named _`Step 1: Manager Approval`_ with these specifications:

**–** Name this step _`Step 1: Manager Approval`_ .

**–** Select `Enter this step if the following` and choose **criteria are met** . Also, choose **approve record** for
the `else` option.

**–** Set the filter criteria to: _`Expense: Amount greater or equal 50`_ .

**–** In the `Automatically assign to approver(s)` option, select the manager of the user submitting the request.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**2.** Create an approval step named _`Step 2: Multiple VP Approval`_ and specify these attributes.

**–** Use the filter criteria _`Expense Amount greater or equal 5000`_ .

**–** Choose `Automatically assign to approver(s)` and select two users with a VP role.

**–** Select the `Require UNANIMOUS approval from all selected approvers` option. The request isn’t
approved unless both designated users approve.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**–** Choose `Perform ONLY the rejection actions for this step...` so that the request returns to the
manager for changes if one of the VPs rejects the request.

Tip: Consider creating these final approval actions:

**•** Define a field update to automatically change the `Status` field to “Approved.”

**•** Send an approval notification to the user who submitted the expense report.

**•** To print a reimbursement check, send an outbound message to your back-office financial system.

Wrap Things Up:

**•** After you created the approval process, add the Approval History related list to the Expense Report object page layout.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Create a Custom Object](https://help.salesforce.com/s/articleView?id=sf.dev_objectcreate_task_parent.html&language=en_US)

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

[Create Custom Fields](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&language=en_US)

Set Up an Approval Process

Prepare Your Org for Approvals


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

#### Sample Approval Process: Discounting Opportunities

Opportunities that are discounted more than 40% require a CEO approval. Use this example to
create a one-step approval process.

Prep Your Organization

Before creating the approval process:

**•** To notify approvers about a pending approval request, create an email template. To direct users
to the approval page in Salesforce, include approval process merge fields.

**•** Create the following custom fields for opportunities:

**–** A percent field called `Discount Percent` so that users can enter a percentage
discount.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**–** A checkbox field called `Discount Approved` to indicate whether the CEO approved the discount.

Create the Approval Process

Create an approval process on the Opportunity object and specify the following:

**•** The filter criteria for this approval process is _`Discount Percent greater or equal 0.4`_ . Records must meet this
criteria before they can be submitted to this approval process.

**•** You don't need to choose a custom field as the next automated approver because you specify later that the CEO must approve all
requests.

**•** Select the email template you created for this approval process.

**•** Choose the record owner as the only user who can submit a discount request for approval.

**•** Create one approval step with no filter criteria since all records submitted must be approved or rejected.

**•** Choose `Automatically assign to approver(s)` and select the name of your CEO.

**•** If appropriate, choose `The approver's delegate may also approve this request` if you want to allow the
user in the `Delegated Approver` field to approve requests.

**•** Consider creating the following final approval actions:

**–** Email alert to notify the user who submitted the discount request.

**–** Field update to automatically select the opportunity `Discount Approved` checkbox.

Wrap Things Up

**•** After you created the approval process, add the Approval History related list to the appropriate opportunity page layouts.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

[Create Custom Fields](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&language=en_US)

Set Up an Approval Process

Prepare Your Org for Approvals

#### Sample Approval Process: Job Candidates

When your company interviews candidates for a position, you can have several levels of approval
before you can send an offer letter. Use this example to create a three-step approval process that
requires approval from multiple management levels.

Prep Your Organization:

Before creating the approval process:

**•** If you don't yet have a custom object to track candidates, create a custom object and tab called
Candidates. Add the appropriate fields such as `Salary`, `Offer Extended` (checkbox),
and `Date of Hire` .

**•** To notify approvers about a pending approval request, create an email template. To direct users
to the approval page in Salesforce, include approval process merge fields.

Create the Approval Process:

Create an approval process on the Candidate custom object using the following specifications:

**•** Don't enter filter criteria because you want all submitted offers to be approved.

**•** Choose the `Manager` field as the next automated approver.

**•** Select the email template you created for this approval process.

**•** Choose the record owner or any other user that you want to be able to submit offer letters.

**•** Create these approval steps.

**1.** Create a step named _`Step 1: Manager Approval`_ :

**–** No filter is necessary as you want all records to advance to this step.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**–** In the `Automatically assign to approver(s)` option, select the manager of the user submitting the request.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**2.** Create a step named _`Step 2: VP Approval`_ :

**–** No filter is necessary as you want all records to advance to this step.

**–** To allow the manager to select the appropriate VP to approve the request, choose `Let the user choose the`
`approver` .

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**–** Choose `Perform ONLY the rejection actions for this step...` so that the request returns to the
manager for changes if the VP rejects the request.

**3.** Create a step named _`Step 3: CFO Approval`_ :


### Automate Your Business Processes with Salesforce Flow Approval History Reports

**–** No filter is necessary as you want all records to advance to this step.

**–** Choose `Automatically assign to approver(s)` and select the name of your CFO.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**–** Choose `Perform all rejection actions for this step AND all final rejection actions.`
`(Final Rejection)` so that offer letters rejected by your CFO are completely rejected.

Tip:

**•** Consider creating the following final approval actions:

**–** Email alert to notify the user who submitted the offer letter request.

**–** Field update to select the `Offer Extended` checkbox.

**•** Consider creating this final rejection action:

**–** Email alert to notify the manager that the offer can’t be extended.

Wrap Things Up:

**•** After you created the approval process, add the Approval History related list to the Candidates object page layout.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Create a Custom Object](https://help.salesforce.com/s/articleView?id=sf.dev_objectcreate_task_parent.html&language=en_US)

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Set Up an Approval Process

Prepare Your Org for Approvals

### Approval History Reports

If you create a custom report type for approval process instances, users can view the historical
details of completed and in-progress approval processes and their individual steps.

Fields Available for Approval History Reports
If you create a custom report type with Process Instance as the primary object and Process
Instance Node as the related object, you can create approval history reports with various
combinations of fields that enable you to view a detailed history of executed and in-progress
approval processes and their individual steps.

Examples of Approval History Reports
See sample reports to learn how you can obtain approval history data.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Approval History Reports

Considerations for Approval History Reports
Understand the limitations and special behaviors when you create or view approval history reports, which provide a detailed history
of approval processes and steps.

SEE ALSO:

[Create a Custom Report Type for Approval History](https://help.salesforce.com/s/articleView?id=sf.approval_history_custom_report_type.html&language=en_US)

#### Fields Available for Approval History Reports

If you create a custom report type with Process Instance as the primary object and Process Instance
Node as the related object, you can create approval history reports with various combinations of
fields that enable you to view a detailed history of executed and in-progress approval processes
and their individual steps.

Process Instance

A process instance represents one instance of an approval process. A new process instance is created
each time a record is submitted for approval.

#### **Field Description**

`Approval Process:` Name of the approval process.

```
Name

```

`Approval Process` ID of the approval process instance.

```
Instance ID

```

EDITIONS

Available in: Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Group** (View Only),
**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

Available in: Enhanced
Folder Sharing and Legacy
Folder Sharing

```
Completed Date

Elapsed Days

Elapsed Hours

Elapsed Minutes

Last Actor: Full

Name

```

Date and time when the approval process instance was
completed or recalled.

If no step criteria are met and the record is auto-approved or
auto-rejected, `Completed Date` and `Submitted Date`
have the same values.

Length of time between when the record was submitted for
approval and when the approval process was completed or
recalled.

Full name of the user who most recently participated in the
approval process instance.

If no step criteria are met and the record is auto-approved or
auto-rejected, `Last Actor: Full Name` and
`Submitter: Full Name` have the same values.

`Object Type` Object type of the record that was submitted for approval.

`Pending Step Name` Name of the approval step at which the record is awaiting
approval or rejection.

`Record Name` Name of the record that was submitted for approval.


Automate Your Business Processes with Salesforce Flow Approval History Reports

**Field** **Description**

`Status` Status of the approval process instance.

`Submitted Date` Date and time when the record was submitted for approval.

`Submitter: Full Name` Full name of the user who submitted the record for approval.

Process Instance Node

A process instance node represents an instance of an approval step. A new process instance node is created each time a record enters
a step in an approval process. No process instance node is created when the record doesn’t meet the step criteria or if the approval
process instance is otherwise completed without entering the step.

**Field** **Description**

`Step: Name` Name of the approval step.

`Step: Completed Date` Date and time when the approval step instance was completed or recalled.

`Step Elapsed Days` Length of time between when the record entered the approval step and when the
approval step instance was completed or recalled.
```
   Step Elapsed Hours

   Step Elapsed Minutes

```

`Step Last Actor: Full Name` Full name of the user who most recently participated in the approval step instance.

`Step Start Date` Date and time when the record entered the approval step.

`Step Status` Status of the approval step instance.

SEE ALSO:

Approval History Reports

Considerations for Approval History Reports

#### Examples of Approval History Reports Examples of Approval History Reports

See sample reports to learn how you can obtain approval history data.

Report Example: Opportunity Approvals Submitted Within a Date Range

This sample report displays approval process instances that were submitted within a specified date
range (1) for the Opportunity object (2). The results are sorted by status (3) and include the last
actor (4), submitted date (5), completed date (6), record name (7), approval process instance ID (8),
and approval process name (9).


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Approval History Reports

Report Example: Approvals—Elapsed Times

This sample report displays all approval process instances (1) and groups results by the approval process name (2). The results include
the record name (3), approval process instance ID (4), status (5), submitted date (6), elapsed minutes (7), and completed date (8).


Automate Your Business Processes with Salesforce Flow Approval History Reports

Report Example: Approval Steps—Elapsed Times

This sample report displays all approval process instances (1) and groups results by approval process name (2) and record name (3). The
results are sorted by step name (4) and include step status (5), step start date (6), step elapsed minutes (7), step completed date (8), and
approval process instance ID (9).


Automate Your Business Processes with Salesforce Flow Approval History Reports

Notice that the previous sample report doesn't include the approvers for each step and the elapsed time for each approval request. To
get this information, run a SOQL query by using the approval process instance ID from the report. The following sample SOQL query
obtains the `ActorID` (user or queue that received the approval request) and the `ElapsedTimeInHours` (elapsed time since the
approval request was sent) for the first pending step in the report.

```
   SELECT ActorId,ElapsedTimeInHours FROM ProcessInstanceWorkitem where processInstanceId =

   '04gD0000000LvIV'

```


Automate Your Business Processes with Salesforce Flow Approval History Reports

The sample query has only one result, and you can view that approver's user profile page by appending the resulting `ActorID` to the
organization's base URL ( `https://` _`MyDomainName`_ `.my.salesforce.com/005D00000015vGGIAY` ), which gets redirected
to the user profile page.

SEE ALSO:

Approval History Reports

#### Considerations for Approval History Reports

Understand the limitations and special behaviors when you create or view approval history reports,
which provide a detailed history of approval processes and steps.

Considerations for Approval Processes That Were Completed Before or
Pending during the Summer '14 Rollout

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,

When Summer ’14 became available for your organization, the approval history data was

**Performance**, **Unlimited**,

automatically populated for completed and pending approval processes. However, some approval

and **Developer** Editions

history field values are never populated or are populated only after the approval process instance
is next acted upon—such as when a user approves, rejects, or reassigns an approval request—after
the Summer ’14 rollout. Additional exceptions apply to approval history data that is available only
via SOQL queries of certain objects. See ProcessInstance, ProcessInstanceNode, ProcessInstanceStep, and ProcessInstanceWorkitem in
the _Object Reference for Salesforce_ .

**Object** **When Fields are Populated**

Process Instance

For approval process instances that were completed before the Summer ’14 rollout, all Process Instance
fields are automatically populated, with one exception: `Completed Date` is never populated for
approval process instances that were completed before January 1, 2013.

For approval process instances that were pending during the Summer ’14 rollout, all Process Instance
fields are automatically populated, with two exceptions: `Completed Date` and `Last Actor:`
`Full Name` are populated only after the approval process instance is complete.


### Automate Your Business Processes with Salesforce Flow Manage Multiple Approval Requests

**Object** **When Fields are Populated**

Process Instance Node

Never populated for approval process instances that were completed before the Summer ’14 rollout.

For approval process instances that were pending during the Summer ’14 rollout, all Process Instance
Node fields are populated only after the approval process instance is next acted upon after the Summer
’14 rollout.

Considerations for the Sandbox Environment

If you copy approval history data to a sandbox, some field values are overwritten and don't reflect the actual approval history.

**Object** **Field** **When an existing process instance or process instance node record is copied**
**to a sandbox...**

Process Instance `Submitted` This value is overwritten by the date and time when the process instance record is copied
`Date` to the sandbox.

`Submitter:` This value is overwritten by the name of the user who copied the process instance record
`Full Name` to the sandbox.

Process Instance `Step Start` This value is overwritten by the date and time when the process instance node record is
Node `Date` copied to the sandbox.

SEE ALSO:

Fields Available for Approval History Reports

Approval History Reports

### Manage Multiple Approval Requests

Transfer multiple approval requests from one user to another or remove multiple approval requests
from the approval process.

Transfer Pending Approval Requests
If users move to a new role before they complete all their pending approval requests, transfer
the remainder to another user.

Remove Pending Approval Requests
If you want to clean up old approval requests—such as to delete an approval process—remove
them from your Salesforce org. After approval requests are removed, the associated records
are unlocked and removed from all approval processes, so they no longer appear on the
approver’s list of pending approval requests.

SEE ALSO:

Considerations for Managing Approvals


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Manage Multiple Approval Requests

#### Transfer Pending Approval Requests

If users move to a new role before they complete all their pending approval requests, transfer the
remainder to another user.

**1.** From Setup, enter _`Mass Transfer Approval Requests`_ in the `Quick Find`
box, then select **Mass Transfer Approval Requests** .

**2.** Search for the approval requests to transfer.

**3.** Select **Mass transfer outstanding approval requests to a new user** .

**4.** Look up and select the user to transfer the requests to.

Make sure that the user can view the records that are associated with the approval requests.

**5.** Add comments.

The comments you enter display on the Approval History related list.

**6.** Select each approval request that you want to transfer.

#### 7. Click Transfer .

SEE ALSO:

#### Remove Pending Approval Requests

Considerations for Managing Approvals

Manage Multiple Approval Requests

#### Remove Pending Approval Requests

If you want to clean up old approval requests—such as to delete an approval process—remove
them from your Salesforce org. After approval requests are removed, the associated records are
unlocked and removed from all approval processes, so they no longer appear on the approver’s list
of pending approval requests.

**1.** From Setup, enter _`Mass Transfer Approval Requests`_ in the `Quick Find`
box, then select **Mass Transfer Approval Requests** .

**2.** Search for the approval requests that you want to remove.

**3.** Select **Mass remove records from an approval process** .

**4.** Add comments.

The comments you enter display on the Approval History related list.

**5.** Select each approval request to remove from the approval process.

#### 6. Click Remove .

SEE ALSO:

#### Transfer Pending Approval Requests

Considerations for Managing Approvals

Manage Multiple Approval Requests


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To transfer multiple approval
requests:

**•** Transfer Leads

AND

Transfer Record

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To remove multiple approval
requests:

**•** Transfer Leads

AND

Transfer Record

### Automate Your Business Processes with Salesforce Flow Approval Requests for Users Approval Requests for Users

Your admin can set up approval processes that let you and other users submit records for approval,
which results in _approval requests_ .

#### Submit a Record for Approval

Depending on your org’s customizations, you can submit a record for approval directly from
that record.

Withdraw an Approval Request
If you submitted a record for approval but suddenly must update information in the record,
recall the approval request. However, whether you can recall an approval request depends on
how your admin configured the approval process that the record was submitted to.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Respond to an Approval Request
When you receive an approval request, respond to it by approving, rejecting, or reassigning it. Depending on which Salesforce
experience you’re using, you have different options. Approval request comments are limited to 4,000 characters. In Chinese, Japanese,
or Korean, the limit is 1,333 characters.

What Does This Approvals Error Mean?
Here are some errors that you can come across when you submit a record for approval or respond to an approval request.

Approval History Status
To track where a record is in an approval process, view its Approval History related list.

Approval User Preferences
Identify a delegated approver and control whether you receive approval request emails.

#### Submit a Record for Approval

Depending on your org’s customizations, you can submit a record for approval directly from that
record.

**1.** Go to the record that you want to submit for approval.

**2.** Make sure it’s ready to be submitted.

Before you can submit a record for approval, it must meet the criteria for an active approval
process. If you’re not sure what the requirements are, ask your admin.

**3.** Click **Submit for Approval** .

If an approval process applies to the record, Salesforce begins the approval process. This button
isn’t available after the record has been submitted.

To keep tabs on the progress of your submitted approval, we recommend following the approval
record in Chatter.

SEE ALSO:

Withdraw an Approval Request

Approval User Preferences

### Approval Requests for Users


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To submit a record for
approval:

**•** Read on the record

Automate Your Business Processes with Salesforce Flow Approval Requests for Users

#### Withdraw an Approval Request

If you submitted a record for approval but suddenly must update information in the record, recall
the approval request. However, whether you can recall an approval request depends on how your
admin configured the approval process that the record was submitted to.

**1.** Go to the detail page for the record associated with the approval request.

**2.** In the Approval History related list, recall the approval request.

SEE ALSO:

Submit a Record for Approval

Approval User Preferences

Approval Requests for Users

#### Respond to an Approval Request

When you receive an approval request, respond to it by approving, rejecting, or reassigning it.
Depending on which Salesforce experience you’re using, you have different options. Approval
request comments are limited to 4,000 characters. In Chinese, Japanese, or Korean, the limit is 1,333
characters.

In-App Notification

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To withdraw an approval
request:

**•** Read on the Record

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To respond to an approval
request from within
Salesforce:

**•** Read on the associated
record

To respond to an approval
request from an email:

**•** API Enabled

Depends on the `Receive Approval Request Emails` field in your approver preferences.
If notifications are enabled for your org, you receive a notification whenever you receive an approval request email.

**•** Respond from the notification if your admin enabled actionable notifications.

**•** To open the approval request, click the notification.

Email Notification

Depends on the `Receive Approval Request Emails` field in your approver preferences.


Automate Your Business Processes with Salesforce Flow Approval Requests for Users

**•** To open the approval request, click the link in the email.

**•** Reply to the email if your admin enabled email approval response.

Record

Respond from the Approval History related list.

Chatter

Depends on if your admin has enabled Approvals in Chatter and you haven’t opted out of receiving approval requests through Chatter
posts.

**•** Respond from the post if your admin enabled actionable notifications.

**•** Click the name of the record, then respond from the Approval History related list.

Home

Depends on if your admin added the Items to Approve component to your home page. From the Home tab, respond from the Items to
Approve component.

Tip: From this component in Salesforce Classic, you can respond to multiple requests at once.

Slack

Slack notifications are enabled by default. If your admin hasn't disabled Slack notifications, an approver can respond to a request from
the **Messages** tab on the Salesforce Digital HQ app in Slack. A **Show More** link opens the details of the approval request in Salesforce.

Respond to an Approval Request via Email
If your admin enabled email approval response, you can approve or reject requests by responding to the email notification. It doesn’t
matter which Salesforce experience or mobile email client you’re using. Delegated approvers can also respond to approval requests
by email.

Troubleshoot Email Responses to Approval Requests
When email responses aren’t working correctly, review these common issues.

SEE ALSO:

Approval User Preferences

Approval Requests for Users


Automate Your Business Processes with Salesforce Flow Approval Requests for Users

##### Respond to an Approval Request via Email

If your admin enabled email approval response, you can approve or reject requests by responding
to the email notification. It doesn’t matter which Salesforce experience or mobile email client you’re
using. Delegated approvers can also respond to approval requests by email.

Email approval response works in all languages that Salesforce supports. The response word or
phrase is checked using the current user language dictionary. If no matches are found, the response
word or phrase is checked in all other language dictionaries.

**1.** In the first line of your reply to the email notification, enter one of the supported response
words.

Periods and exclamation marks are allowed at the end of the word.

**2.** Optionally, in the second line of your reply, add comments.

**3.** Send the email.

SEE ALSO:

Approval User Preferences

Approval Requests for Users

##### Troubleshoot Email Responses to Approval Requests

When email responses aren’t working correctly, review these common issues.

I’m not receiving approval requests by email.

Here are a few possible reasons why.

**•** Your approval preferences opt you out of approval request emails.

**•** Your mail server thinks the approval request email is spam. Contact your email admin, who can
check the logs of all inbound email to see if it’s being delivered, rejected, or marked as spam.

**•** Your email admin has to add the Salesforce email addresses that the approval requests come
from to the allowed email addresses for your mail server.

**•** Email delivery time can vary based on your ISP or connection.

My response wasn’t delivered.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To respond to an approval
request via email:

**•** API Enabled

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** An email approval request can only be processed one time. If another user has responded to the approval request before you do,
you get an error.

**•** You must have the “API Enabled” user permission to respond to approval requests by email.


Automate Your Business Processes with Salesforce Flow Approval Requests for Users

I received an email that said, “ **`The word used to approve or reject the item was not`**
**`understood.`** ”

Salesforce doesn’t process replies to error emails. Reply again to the original email notification, but this time use one of the supported
response words on page 876.

I received an email that said, “ **`You are not authorized to update the referenced object.`** ”

The approval request email is tied to your email address. If you forward the request to another email address, or if your email client lets
you respond from multiple email addresses, you receive this error. Reply again to the original email notification, but this time reply from
the same email address that received the email approval request.

SEE ALSO:

#### What Does This Approvals Error Mean?

Respond to an Approval Request via Email

Approval Requests for Users

#### What Does This Approvals Error Mean?

Here are some errors that you can come across when you submit a record for approval or respond
to an approval request.

Manager undefined

This approval request requires the next approver to be determined by
the _`Field Name`_ field.

This value is empty.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Salesforce tried to route the approval request based on a hierarchical field, such as `Manager` . However, the field has no value or specifies
an inactive user. This error can occur when someone submits a record for approval or when an approver responds to an approval request.

Required fields are missing: [ _`FieldName`_ ].

The approval process includes a field update that fails standard validation rules for the identified field. This error can occur even if the
field isn’t visible on your page layout.

Note: Salesforce doesn’t check whether field updates pass _custom_ validation rules on fields.

SEE ALSO:

Troubleshoot Email Responses to Approval Requests

Approval Requests for Users


Automate Your Business Processes with Salesforce Flow Approval Requests for Users

#### Approval History Status

To track where a record is in an approval process, view its Approval History related list.

**Status** **Definition**

Submitted The record has been submitted for approval.

Pending The record has been submitted for approval and is awaiting approval or
rejection.

Approved The record has been approved.

Rejected The record has been rejected.

Reassigned The record has been submitted for approval but assigned to a different
approver.

Recalled The record was submitted for approval but recalled from the approval
process.

SEE ALSO:

Approval Processes

Submit a Record for Approval

Respond to an Approval Request

Approval Requests for Users

#### Approval User Preferences

Identify a delegated approver and control whether you receive approval request emails.

From your personal settings, enter _`Approver Settings`_ in the `Quick Find` box, then
select **Approver Settings** . No results? Enter _`Personal Information`_ in the `Quick Find`
box, then select **Personal Information** .

EDITIONS

Available in: Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs)](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Approval Requests for Users

##### Opt Out of Approval Request Posts in Chatter

By default, after your org enables Approvals in Chatter, you’re notified about approval requests by email and a Chatter post. To stop
seeing the Chatter posts, opt out. If you do opt out, the posts don’t appear in your feed but they do appear in the associated record’s
feed.

What Happens When You Opt Out of Chatter Approval Requests?
By default, when your org has Approvals in Chatter enabled, you receive approval request notifications by email and Chatter. Here’s
what happens when you opt out of the Chatter posts.

SEE ALSO:

Approval Requests for Users

[Personalize Your Salesforce Experience](https://help.salesforce.com/s/articleView?id=sf.user_overview.htm&language=en_US)

##### Opt Out of Approval Request Posts in Chatter

By default, after your org enables Approvals in Chatter, you’re notified about approval requests by
email and a Chatter post. To stop seeing the Chatter posts, opt out. If you do opt out, the posts
don’t appear in your feed but they do appear in the associated record’s feed.

USER PERMISSIONS

To view an approval request
post for a record:

**•** Read on the record

**1.** In the page banner, click your profile avatar, and select **My Settings** (Salesforce Classic) or **Settings** (Lightning Experience).

**2.** Enter _`My Feeds`_ in the `Quick Find` box, then select **My Feeds** .

**3.** Deselect **Receive approval requests as posts.**

You see this setting only when approvals are enabled in your org.

**4.** Save your changes.

SEE ALSO:

Approval User Preferences

[Personalize Your Salesforce Experience](https://help.salesforce.com/s/articleView?id=sf.user_overview.htm&language=en_US)


### Automate Your Business Processes with Salesforce Flow Approval Process Terminology

##### What Happens When You Opt Out of Chatter Approval Requests?

By default, when your org has Approvals in Chatter enabled, you receive approval request notifications by email and Chatter. Here’s what
happens when you opt out of the Chatter posts.

**•** If you opt out while an approval that you’re assigned to is in progress, you see notification posts if you’re following the approval
record.

**•** If you’re following the approval record, you see approval posts from the record with non-approver content.

**•** For approval notification posts that you’ve already received, you see non-approver content.

**•** The Approve and Reject buttons are removed from existing approval posts in your feed.

SEE ALSO:

Approval User Preferences

Opt Out of Approval Request Posts in Chatter

### Approval Process Terminology

Salesforce uses this terminology for approval processes.

Approval Actions

An approval action occurs when all required approvers approved a step.

### Approval Process

An approval process automates how records are approved in Salesforce. An approval process
specifies each step of approval, including from whom to request approval and what to do at each
point of the process.

Approval Request

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

An approval request is an email, Salesforce app notification, Lightning Experience notification, or Chatter post. The approval request
notifies the recipients that a record was submitted for them to approve.

Approval Steps

Approval steps define the chain of approval for a particular approval process. Each step determines:

**•** Which records can advance to that step

**•** To whom to assign approval requests

**•** Whether to let each approver’s delegate respond to the requests

The first step specifies what to do if a record doesn’t advance to that step. Later steps specify what happens if an approver rejects the
request.


Automate Your Business Processes with Salesforce Flow Approval Process Terminology

Assigned Approver

The assigned approver is the user responsible for responding to an approval request.

Delegated Approver

A delegated approver is someone appointed by an assigned approver as an alternate for approval requests.

Note: Internal Salesforce users are listed by and can be added using the Delegated Approver lookup field. Use Data Loader and
a comma-delineated (CSV) file to add users with communities licenses as Delegated Approvers. The CSV uses the

`CommunityUserId` rather than the `UserId` for `DelegatedApproverId` . Communities licenses are used with Experience
Cloud sites and legacy portals.

Email Approval Response

Email approval response lets users respond to approval requests by replying to an email notification.

Initial Submission Actions

An initial submission action occurs when a user first submits a record for approval. By default, the record is locked.

Final Approval Actions

Final approval actions occur when all required approvals were obtained.

Final Rejection Actions

A final rejection action occurs when an approver rejects the request and it moves to the final rejection state.

Outbound Message

An outbound message sends information to a designated endpoint, like an external service. You can configure outbound messages
from Setup. Configure the external endpoint and use SOAP API to create a listener for the messages.

Process Instance

A process instance represents one instance of an approval process. A new process instance is created each time a record is submitted
for approval.

Process Instance Node

A process instance node represents an instance of an approval step. The system creates a process instance node each time a record
enters a step in an approval process. The system doesn’t create a process instance node when the record doesn’t meet the step criteria,
or the approval process instance is completed without entering the step.

Recall Actions

A recall action occurs when a submitted approval request is recalled. By default, the record is unlocked.


Automate Your Business Processes with Salesforce Flow Modify Process Automation Settings

Record Locking

Record locking prevents users from editing a record, regardless of field-level security or sharing settings. By default, Salesforce locks
records that are pending approval. Only admins can edit locked records.

SEE ALSO:

Approval Processes

Automated Actions

Set Up an Approval Process

Modify Process Automation Settings

Enable or disable features related to flows, processes, workflow rules, and approval processes.

**User Permissions Needed**

To edit process automation settings: Customize Application

To create, update, and delete flow list views: Manage Flow

**•** Identify Your Salesforce Org’s Default Workflow User

**•** Override the Sender for Email Approval Notifications

**•** Let Users Respond to Approval Requests via Email

**•** Let Users Pause Flow Interviews

**•** Restrict Who Can Resume Shared Flow Interviews

**•** Enable Lightning Runtime for Custom Buttons and Links

**•** Require Access to Automation Home Charts (Beta)

**•** Control What Happens When a Flow Tries to Set Values for Read-Only Fields

**•** Select Flow and Process Error Email Recipients

**•** Deploy Processes and Flows as Active

## Legacy Salesforce Flow Features

Legacy Salesforce Flow features include Process Builder and Workflow Rules.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Processes and flows are
available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Approvals and Workflow are
available in **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Important: Starting in Winter ’23, you can’t create new processes or workflow rules. You can still activate, deactivate, and edit
any existing processes and workflow rules. To migrate existing processes or workflow rules, use the process in Move Processes
and Workflows to Flow Builder with the Migrate to Flow Tool on page 894. For new automations, create flows in Flow Builder on
page 16.

Switch to Flow Builder Learning Map
Flow Builder combines the capabilities of workflow rules and Process Builder in a single point-and-click tool, making it easier to
create a triggered process. If you created triggered processes with workflow rules or Process Builder, use the Migrate to Flow tool
to move them to Flow Builder. Start by migrating and testing in a sandbox environment before moving your new flows to production.


### Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Process Builder
Many of the tasks you assign, the emails you send, and other record updates are vital parts of your standard processes. Instead of
doing this repetitive work manually, you can configure flows or processes to do it automatically. We strongly recommend using
Flow Builder, but Process Builder can also help you automate your business processes and give you a graphical representation as
you build it.

Workflow Rules
Workflow rules let you automate standard internal procedures and processes to save time across your org. A workflow rule is the
main container for a set of workflow instructions. These instructions can always be summed up in an if/then statement.

### Switch to Flow Builder Learning Map

Flow Builder combines the capabilities of workflow rules and Process Builder in a single point-and-click tool, making it easier to create
a triggered process. If you created triggered processes with workflow rules or Process Builder, use the Migrate to Flow tool to move them
to Flow Builder. Start by migrating and testing in a sandbox environment before moving your new flows to production.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

#### Equivalent Features in Flows and Workflow Rules

Features and fields in workflow rules correspond to certain things in flows. Use the equivalent features and fields to build flows that
can replace your workflow rules.

Planning Your Switch to Flow Builder
Workflow Rules and Process Builder are no longer the preferred tools for automating your business processes. With their pending
retirement, now is the time to go with Flow Builder as the future of automated processes. Flow Builder is a foundation for the future
and offers built-in extensibility, application lifecycle management, and faster performance.

Migrate to Flow Tool Considerations
Review considerations and supported workflow rules and processes for the Migrate to Flow tool.

Move Processes and Workflows to Flow Builder with the Migrate to Flow Tool
Use the Migrate to Flow tool to convert your Process Builder processes and workflow rules into Flow Builder, including scheduled
actions. The tool also supports partial migration of processes for most actions.

Sample Migration to a Flow: Workflow Rule with an Email Alert
The majority of workflow rules are used to send email alerts or perform same-record field updates. While these types of workflow
rules have a reputation for being fast, triggered flows are even faster. It’s time to migrate your workflow rules to Flow Builder.

#### Equivalent Features in Flows and Workflow Rules

Features and fields in workflow rules correspond to certain things in flows. Use the equivalent
features and fields to build flows that can replace your workflow rules.

General


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Evaluation Criteria

In flows, evaluation criteria are defined in the Start element, in the Set Entry Conditions section.

To manually convert workflow rules with unsupported use cases in entry criteria, create a Decision element inside the Flow. Then recreate
the workflow rule steps with the condition builder.

Rule Criteria

In flows, rule criteria are defined in the Start element, in the Set Entry Conditions section.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Field Updates

In flows, field updates are done using the Update Records element. In the Update Records element, for How to Find Records to Update
and Set Their Values, select **Use the {object name} record that triggered the flow** . In flows, you can enter values directly, or use
formulas or references for field values. You can also update multiple fields in a single flow. To improve performance, place field updates
in a flow optimized for fast field updates (before-save).

Flows don’t support field update notifications for the Owner field.

A Get Records element can be required to reference certain elements, like users or groups.

Task Fields

To create a task in a flow, use the Create Records element.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Operators

Flow Builder shows only the operators that are relevant to the field. `Less Than`, `Greater Than`, `Less Than or Equal`,
and `Greater Than or Equal`, appear only for number fields.

To manually convert workflow rules that use the `does not contain` operator, use custom condition logic. For example, create a
condition that uses the `Contains` operator in the first condition, and in the condition logic, enter **NOT 1** .

SEE ALSO:

Migrate to Flow Tool Considerations


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

#### Planning Your Switch to Flow Builder

Workflow Rules and Process Builder are no longer the preferred tools for automating your business
processes. With their pending retirement, now is the time to go with Flow Builder as the future of
automated processes. Flow Builder is a foundation for the future and offers built-in extensibility,
application lifecycle management, and faster performance.

There are several areas to focus your efforts as plan your switch to Flow Builder.

Analyze Your Automation

To start your migration journey, analyze your existing automation.

**•** Categorize your most commonly used automation types.

**•** Observe your org’s flow activity in reports and dashboards, such as total errors and total started
automations.

**•** View your Flow Interview Logs and Flow Interview Log Entries.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Run the Sample Flow Report: Screen Flows report. Use the reports to examine run-time details about your screen flows.

**•** Use the metrics to discover usage patterns and in turn to optimize your screen flows for users.

Migrate in a Sandbox First

It’s critical to keep your existing data safe before you make any changes. Working in a sandbox ensures that no data is harmed as you
make you move to Flow Builder.

Catalog Your Current Automation

There are many ways to create a catalog. You can create a spreadsheet. Organize your automations by Object. Include the Category,
Entry Criteria, and Related Actions as you catalog. You can create a diagram to aid in your visualization.

Identify and Remove Redundant Processes

Evaluate whether processes are still needed or can be improved. Common culprits of redundancy can include:


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Prioritize Which Processes to Migrate First

Migrate the processes that speed up the record updates and take less time and effort to migrate. Start with a Single Object. Pick the
object that has the least number of Workflow Rules and processes associated with it. Processes that send email alerts or perform
same-record field updates are good beginner options for migration.

Structure Your Automation

As you think about your business needs, here are some common considerations:

**•** Performance: Can you use Entry Conditions or other optimizations to reduce unnecessary operations?

**•** Maintenance and Change Management: Who is responsible for this business process? What is the likelihood of change or iteration?

**•** Migration from Workflow Rules and processes to flows isn’t one to one. You don’t always have to create a flow for each process
you’re migrating.

**•** Analyze your existing flows and see if there are corresponding elements that you can update, or incorporate new actions in an
existing flow.

**•** Consider whether the more complex automation processes can be reused and implemented as subflows.

**•** Review whether there’s a better solution that doesn’t involve automation.

Example: A Workflow Rule or process only updates a field on the Case object after it’s created. Replace it with a formula field instead.

Think Beyond One Flow Per Object

You can design your automation to have multiple flows per object. For a more scalable future, order your flows with the Trigger Order
option. Use Flow Trigger Explorer to assign priority values to your flows. With this tool, multiple flows per object are manageable.

Optimize Your Record-Triggered Automations

Building efficient record-triggered flows can help minimize some flow limits. Here are the options you can select to improve efficiency
as you build your flows.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Optimize Your Entry Conditions

Set Entry Conditions to decrease the performance impact. Used effectively, Entry Conditions prevent automation from running unnecessarily
and improve performance. Set entry conditions to run a flow when a record is created or edited and a field has a specific value. Or set
entry conditions when a record is created or edited and a field IS CHANGED to a specified value. If you only check the field values when
the record is created or edited, there are no additional steps beyond creating the entry conditions. To create entry conditions that check
what the field values are changed to when the record is created or edited, enable the Run When Conditions Met setting. Enabling this
setting prevents repeat operations and maintains consistency.

Replace Time-Dependent Workflow Rules with Scheduled Paths

Add a Scheduled Path to a record-triggered flow. Scheduled Paths occur in the future, after the trigger has fired, based on dates and
times. You can schedule such actions as reminders or follow-ups based on dates in the record that triggered the automation, such as
Close Date. This feature also rechecks the entry conditions.

Example: Set your entry condition to Status = Escalated and then have an automation that sends a reminder two days before close. The
reminder only sends if the status remains escalated.

Order Your Automation

You can use Flow Trigger Explorer to view the order in which your automation runs or to reorder flows. The flow executes in the order
described to minimize disruption from other automation, managed packages, or movement between orgs. With flow trigger ordering,
you can assign a priority value to your flows. To see all of the associated flows that run when a record is created, updated, or deleted,
select an object. This action allows for easy navigation between flows that run under the same circumstances.

Add Descriptions to Your Flows

It’s important to remember that documentation is as important as automation. When building new flows, document your work. Enter
clear, unique names for objects. To describe your intent, use the Description field on every element in all of your flows. This documentation
helps to avoid any confusion as to the purpose of the automation.

Test in a Sandbox

To protect the data in your org, always test in a sandbox before moving any changes to production.

Deactivate Old Automations as You Rebuild

By default, active processes and flows are deployed as inactive. After deployment, manually reactivate the new versions and deactivate
the old.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Resources

[The Salesforce Admins: Automation page is a great resource to help you start automating business processes. You can explore flow](https://admin.salesforce.com/automation)
templates on AppExchange, or navigate to an automation tool directly.

SEE ALSO:

_Video_ [: Automate This: Migrate Workflow Rules and Processes to Flow](https://admin.salesforce.com/blog/2022/automate-this-migrate-workflow-rules-and-processes-to-flow)

_Success Events_ [: Implement: Platform: Transition to Salesforce Flow](https://cs.salesforce.com/portraits/aCe3y000000bmdbCAA)

Move Processes and Workflows to Flow Builder with the Migrate to Flow Tool

Equivalent Features in Flows and Workflow Rules

#### Migrate to Flow Tool Considerations

_Developer Guide_ [: Triggers and Order of Execution](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

#### Migrate to Flow Tool Considerations

Review considerations and supported workflow rules and processes for the Migrate to Flow tool.

Considerations for Migrating a Process to a Flow

Review considerations and supported Process Builder processes for the Migrate to Flow tool.

Considerations

Processes with recursion aren’t fully supported. When a process with recursion is migrated, the
record is evaluated only one time. Test and make sure that any processes with recursion work as
intended after migration.

Processes are migrated as Actions and Related Record-optimized (after-save) flows. If necessary,
you can edit and optimize the flow for Fast Field Updates (before-save) after the flow is migrated.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

The invoke flow action is migrated as a subflow element instead of an invocable flow action. Subflows run in the same transaction as
the parent flow. Any processes with invoke flow actions involving external callouts, external actions, or pauses must be redesigned using
an asynchronous path.

You can migrate Process Builder’s scheduled actions only if you select the single criteria associated with the scheduled action. If multiple
criteria are selected, no scheduled actions are migrated. After migration, scheduled actions become Flow Builder’s scheduled paths. In
the flow, migrated scheduled actions follow the naming convention `ScheduledPath__#` . At run time, the new flow checks for
pending actions from the original migrated process and then deletes them. If a record is updated, any pending scheduled actions are
moved to the proper scheduled path or canceled if the record no longer meets the criteria. If a record isn't updated when the scheduled
[action is executed, it executes the process’ scheduled action. See Monitor Your Processes’ Pending Scheduled Actions.](https://help.salesforce.com/s/articleView?id=sf.process_monitor_instance.htm&language=en_US)

You can’t migrate a cross-object reference in a formula.

You can migrate a process that uses a custom metadata reference in a formula. After the migration, the custom metadata reference is
used in flow formulas, but you can’t configure it by using the resource picker.

When migrating a time-based process, you must migrate each outcome to its own scheduled action flow. Then activate the new flows
and deactivate the process.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Supported Processes

The Migrate to Flow tool supports only record-triggered processes. Custom event and custom invocable type processes aren’t supported.
The tool also doesn’t support processes that contain custom metadata types or criteria that contain a field that’s from a related object
(field traversals). For supported processes, you can migrate these action types without additional configuration.

**•** Record update

**•** Record create

**•** Invoke flow

**•** Invoke Apex

**•** Email alert

After migration, these action types retain their original positions in the flow, but they require additional configuration to function as
expected.

**•** Post to Chatter

**•** Quick Action

**•** Submit for Approval

**•** Send Custom Notification

**•** Live Message Notification

**•** Send Surveys

**•** Quip-related action types

Considerations for Migrating a Workflow to a Flow

Review considerations and supported workflow rules for the Migrate to Flow tool. Learn manual conversion methods for specific workflow
rules.

Considerations

If a workflow rule contains only field updates, the tool converts it into a fast field update (before-save) flow.

Due to their position in the order of execution, record-triggered flows can behave differently from similar workflow rules.

An at-rest pending time-based action is migrated to a scheduled path when the associated record is changed.

Supported Workflow Rules

The Migrate to Flow tool supports workflow rules that contain these items.

**•** Field-based criteria

**•** Field updates

**•** Email alerts

**•** Outbound messages

**•** Time-dependent workflow actions

**•** Rule criteria formulas that are set to true (unless the evaluation criteria are also set to created, and anytime it’s edited to subsequently
meet the criteria)

**•** `Equal to` null

**•** `Not equal` to null

**•** Rule criteria formulas


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Workflow rules that contain the following can't migrate with the Migrate to Flow tool.

**•** Criteria with no defined workflow actions

**•** Global variable fields

**•** Fields on related records

**•** Record types

**•** The `does not contain`, `includes`, `excludes`, or `within` operators

**•** The `greater than`, `greater or equal`, `less than`, `less or equal` operators on picklist fields

**•** Formulas that use `Hour`, `Minute`, `Second`, `TimeNow`, `TimeValue`, `IsClone`, or `$RecordType`

**•** Tasks

**•** Relative date values in date fields

**•** Multiple currencies

Manual Conversion Methods

Certain features are unsupported by the Migrate to Flow tool, but you can manually convert them.

To manually convert workflow rules with unsupported use cases in entry criteria, create a Decision element inside the Flow. Then recreate
the workflow rule steps with the condition builder.

Note: With this method, the flow will always run and check on the decision after entering. This method can impact performance
or prevent time-based workflow triggers from migrating.

To manually convert workflow rules that use the `does not contain` operator, use custom condition logic. For example, create a
condition that uses the `Contains` operator in the first condition, and in the condition logic, enter **NOT 1** .

To manually convert workflow rules that use tasks, use the Create Records option and create a record of the Task object.

Flows support workflow actions for Email Alerts and Outbound Messages. To add these workflow actions to a flow, use the Action
element.

To replicate relative date values, such as `TODAY` or `NEXT WEEK`, use the Decision element.

SEE ALSO:

Equivalent Features in Flows and Workflow Rules

Move Processes and Workflows to Flow Builder with the Migrate to Flow Tool

Planning Your Switch to Flow Builder


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Move Processes and Workflows to Flow Builder with the Migrate to Flow Tool

Use the Migrate to Flow tool to convert your Process Builder processes and workflow rules into
Flow Builder, including scheduled actions. The tool also supports partial migration of processes for
most actions.

Before moving your new flows to production, start with migrating and testing in a sandbox
environment.

**1.** From Setup, in the Quick Find box, enter _`Migrate to Flow`_, and then select **Migrate to**
**Flow** .

**2.** Select the process that you want to convert to a flow.

**3.** Click **Migrate to Flow** .

**4.** Select the criteria that you want to migrate.

If it’s a process, the Migratable column indicates whether you can fully or partially migrate the
process.

**5.** Click **Migrate to Flow** .

**6.** If this is a partial migration of a process, click **Needs Review** when the migration is complete
to see the list of actions that require additional configuration.

**7.** After you migrate a process or workflow rule, test the flow in Flow Builder.


EDITIONS

Available in: all editions
except **Starter**

USER PERMISSIONS

To open, edit, create,
activate, or deactivate a flow
in Flow Builder:

**•** Manage Flow

To create, change, activate,
or deactivate workflow rules
and actions:

**•** Customize Application

To create, edit, or view
processes:

**•** Manage Flow

AND

View All Data

To activate or deactivate
processes:

**•** Manage Flow

AND

View All Data

AND

Customize Application

Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

**8.** If everything works as expected, activate the flow.

**9.** Deactivate the process or workflow rule you migrated to Flow Builder.

Sample Migration to a Flow: Workflow Rule with an Email Alert

The majority of workflow rules are used to send email alerts or perform same-record field updates.
While these types of workflow rules have a reputation for being fast, triggered flows are even faster.
It’s time to migrate your workflow rules to Flow Builder.

Let’s look at a common workflow rule. This rule sends an email alert when an Opportunity is
Closed-Won and the Amount is more than $500.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Processes and flows are
available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Workflow is available in
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

This workflow rule can be built easily in Flow Builder. Here are the elements in a workflow rules and their flow equivalent.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Evaluation Criteria

When you build a flow, the evaluation criteria are defined in the Start element, in the Set Entry Conditions section. Use as specific as
possible Entry Criteria. This way you don’t run a flow when you don’t need to.

Workflow Rule

Flow:


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

When to Run/Trigger (1)

Our example Workflow Rule uses created, and any time it's edited to subsequently meet criteria. For the flow, select “A record is created
or updated under Configure Trigger”. And select “Only when a record is updated and meets the condition requirements” for When to
Run the Flow for Updated Records. You choose this option in the Set Entry Conditions.

Rule Criteria/Set Entry Conditions (2)

The criteria/conditions are similar in both the WFR and the flow. The Condition Requirements field is set to “conditions are met”. The
Field, Operator, and Value are almost identical. The field names are slightly different, as the Object isn’t included in the Field Name in a
flow.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Add an Action

When you build a workflow rule, the action is selected after the Rule Criteria is entered.

In Flow, there’s a Send Email Alert option from Add Element.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

Select the email alert by clicking in the New Action window. Choose the alert to use from the list. You can use existing Email Alerts that
you used previously in workflow rules. Configure Email Alerts to be used in flows just as you did for workflow rules. Email Alerts are
configured under Workflow Actions in Process Automation.


Automate Your Business Processes with Salesforce Flow Switch to Flow Builder Learning Map

In the flow, enter _`$Record`_ into the Record ID field. This global variable contains the values from the record that triggers it to run. So,
