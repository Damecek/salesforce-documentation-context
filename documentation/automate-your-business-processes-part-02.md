If you’re troubleshooting a flow that fails, the debug option in Flow Builder can be your best friend.
See real-time details of what your flow does, set input variables, and restart the flow anytime to
debug a different branch.

Warning: If you debug a flow without choosing to run the flow in rollback mode, the flow
performs its actions, including any DML operations and Apex code execution. Remember,
closing or restarting a running flow doesn’t roll back its previously executed actions, callouts,
and changes committed to the database.

Debug isn't available with all flow types. See Considerations for Troubleshooting Flows on page
282.

**1.** Open the flow in Flow Builder.

#### 2. Click Debug .

**3.** Set the debug options and input variables.

The debug options vary depending on the flow type.


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

To debug a flow in Flow
Builder:

**•** View All Data

Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

**4.** To debug the flow as another user, enable debugging as another user.

**a.** From Setup, in the Quick Find box, enter _`Process`_, and then click **Process Automation Settings** .

**b.** Enable **Let admins debug flows as other users** .

**c.** Save your work.

Warning: When you debug a flow as another user, the flow’s record changes and actions are performed as that user.
Also, the user’s profile and permission sets determine the object permissions and field-level access of the flow. However,
flows that always run in system context ignore the user’s object permissions and field-level access.

**d.** In Debug Options, select **Run flow as another user** and search for the user that you want to debug.

You can debug a flow as another user only in a sandbox environment.

**5.** Click **Run** .


Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

The debug details for the run appear in a panel on the right.

**6.** If you selected Debug wait element behavior when you set the debug options, select a **Wait Path**, and then click **Continue the**
**Debug Run** for each Wait element in the flow.
The debug details for the run appear in a panel on the right.

**7.** (Optional) To restart the flow by using the same or different values for the input variables, click **Debug Again** .

**8.** (Optional) To convert the debug run to a test in a record-triggered flow only, click **Convert to Test** .

Flow Example: Debug a Screen Flow
Let’s debug a screen flow that creates a contact for each beneficiary on a policy by creating a registration form.


Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

Flow Example: Debug a Template-Triggered Prompt Flow
Let’s debug a prompt flow that integrates with a prompt template for generating a list of events.

SEE ALSO:

Customize What Happens When a Flow Fails

Considerations for Troubleshooting Flows

Lightning Runtime vs. Classic Runtime for Flows

Flows in Transactions

Testing Your Flow

_Trailhead_ [: Flow Troubleshooting](https://trailhead.salesforce.com/content/learn/modules/flow-troubleshooting)

##### Flow Example: Debug a Screen Flow

Let’s debug a screen flow that creates a contact for each beneficiary on a policy by creating a
registration form.

Before activating and distributing your screen flow, you debug the flow to troubleshoot any flow
failure.

**1.** Create or open the Registration forms on page 155 screen flow in Flow Builder.

**2.** Click **Debug** .

**3.** Set the debug options.

If you want to run the flow as another user, ensure that **Let admins debug flows as other**
**users** is enabled in **Process Automation**

**Settings** .

**4.** Click **Run** .
The debug details for the run appear in a panel on the right.

**5.** Enter the values in the required fields.


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

Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

**6.** Click **Next** .

**7.** Review the Debug Details to see the results.

**8.** (Optional) To restart the flow by using the same or different values for the input variables, click **Change Inputs or Run Again** .

You can’t convert the debug run to a test in the screen flow.

SEE ALSO:

Flow Example: Create a Contact for Each Beneficiary on a Policy

Considerations for Troubleshooting Flows

_Trailhead_ [: Flow Troubleshooting](https://trailhead.salesforce.com/content/learn/modules/flow-troubleshooting)

##### Flow Example: Debug a Template-Triggered Prompt Flow

Let’s debug a prompt flow that integrates with a prompt template for generating a list of events.

Template-triggered prompt flows aren’t compatible with prompt templates created in Winter ’24.

Before creating your sales email prompt template, you debug the flow to troubleshoot any flow
failure.

**1.** Create or open the Get Marketing Events on page 45 prompt flow in Flow Builder.

**2.** Click **Debug** .

**3.** Set the debug options and input variables.

If you want to run the flow as another user, ensure that **Let admins debug flows as other**
**users** is enabled in **Process Automation Settings** .

Warning: If you debug a flow without choosing to run the flow in rollback mode, the
flow performs its actions, including any DML operations and Apex code execution.
Remember, closing or restarting a running flow doesn’t roll back its previously executed
actions, callouts, and changes committed to the database.

**4.** Enable **Run flow in rollback mode** under Debug Options.


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

Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

**5.** Click **Run** .
The debug details for the run appear in a panel on the right.

**6.** Review the Debug Details to see the results.


Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

**7.** (Optional) To restart the flow by using the same or different values for the input variables, click **Debug Again** .


Automate Your Business Processes with Salesforce Flow Troubleshoot Flow Errors

You can’t convert the debug run to a test in the prompt flow.

SEE ALSO:

Example of Sales Email Template-Triggered Prompt Flow

Considerations for Troubleshooting Flows

_Trailhead_ [: Flow Troubleshooting](https://trailhead.salesforce.com/content/learn/modules/flow-troubleshooting)

#### Troubleshooting Flow URLs

If you’re distributing a flow and the custom button, custom link, or a direct flow URL isn’t working
as expected, verify the referenced flow. In addition, verify its variables if you’re passing values into
a flow from the URL.

To make sure that the URL can find the right flow, verify that:

**•** The flow that the URL references hasn’t been deleted or deactivated.

**•** The flow name is correctly spelled and capitalized. It must be an exact, case-sensitive match to
the flow’s API Name.

If your flow URL references a specific flow version, verify that the version hasn’t been deleted or
deactivated.

If you’re using the URL to pass values into the flow and the URL can’t access the variable, the
parameter that references the variable is ignored.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Make sure that the URL can find the right flow variable and that the value that you’re passing is compatible with the variable’s data type.
Verify that the URL variable:

**•** Is spelled and capitalized correctly. It must be an exact, case-sensitive match to the flow variable.

**•** Allows input access.

**•** Hasn’t been renamed in the flow.

**•** Hasn’t been removed from the flow.

**•** Doesn't have a data type of Record.

SEE ALSO:

Customize a Flow URL to Control Finish Behavior

Customize a Flow URL to Set Variable Values

Troubleshoot Flow Errors


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Select Flow and Process Error Email Recipients

When a process or flow interview fails, a detailed email is sent to the admin who last modified the
process or flow. However, sometimes the admin isn’t the best person to act on the details of what
was executed and what went wrong. In that case, you can send error emails to the Apex exception
email recipients.

**User Permissions Needed**

To edit process automation settings: Customize Application

To create, update, and delete flow list views: Manage Flow

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Process and flow error emails include the data that's involved in the process or flow, including user-entered data.

**1.** From Setup, enter _`Automation`_ in the Quick Find box, and then select **Process Automation Settings** .

**2.** For Send Process or Flow Email to, select who receives the error emails.

**•** If you select **User Who Last Modified the Process or Flow**, error emails are sent to the user who last modified the flow that
has the error.

**•** If you select **Apex Exception Email Recipients** [, error emails are sent to the addresses listed on the Apex Exception Email page](https://developer.salesforce.com/docs/atlas.en-us.250.0.apexcode.meta/apexcode/apex_exception_definition.htm#unhandled_exception_emails)
in Setup.

**3.** Save your changes.

SEE ALSO:

Troubleshoot Flow Errors

[What Happens When an Apex Exception Occurs?](https://help.salesforce.com/s/articleView?id=sf.code_apex_exceptions.htm&language=en_US)

What Happens When a Process Fails?

Customize What Happens When a Flow Fails

Flow Limits and Considerations

When designing, managing, and running flows, consider the permissions, use limits, and data issues.

Flow Usage-Based Entitlements
Like feature licenses, usage-based entitlements don’t limit what you can do in Salesforce; they
add to your functionality. If your usage exceeds the allowance, Salesforce contacts you to discuss
additions to your contract. In the meantime, your flow interviews run as usual.

General Flow Limits
When using flows, keep flow limits and Apex governor limits in mind.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Per-Transaction Flow Limits and **Developer** Editions
Salesforce strictly enforces limits to ensure that any runaway flows don't monopolize shared
resources in the multitenant environment. Per-transaction limits, which Apex enforces, govern
flows. If an element causes the transaction to exceed governor limits, the system rolls back the entire transaction. The transaction
rolls back even if the element has a defined fault connector path.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Flow Builder Considerations
When you create a flow in Flow Builder, familiarize yourself with its limitations and behaviors. For example, Flow Builder supports
only a few locales. Because of intellectual property protection, you can’t open flows installed from managed packages, unless the
flows are templates.

Salesforce Feature Considerations for Flows
When designing flows, consider these Salesforce features.

Salesforce Data Considerations for Flows
When designing flows, keep these Salesforce data considerations in mind.

Flow Feature Considerations
When designing flows, keep these flow feature considerations in mind. Also, some resources, elements, and screen components
have more considerations that are described in their reference topics.

Flow Data Considerations
When designing flows, keep these data considerations in mind.

Flow Management Considerations
When managing flows, consider the administration and activation limits.

Considerations for Packaging Flows
You can include a flow in a managed or unmanaged package. Before you create, update, or deploy a package that contains a flow,
understand the limitations and behaviors of packages.

Change Set Considerations for Flows
Before you use change sets to deploy a flow, understand the limits and behaviors that are related to component dependencies,
deployment, and flow triggers.

Considerations for Flows Installed from Packages
Keep these considerations in mind when you distribute, upgrade, or remove a flow that you installed from a package.

Considerations for Troubleshooting Flows
Keep these considerations in mind when reviewing a flow error email or using the debug option in Flow Builder.

Run-Time Changes by Release and API Version
These versioned updates affect only flows that are configured to run on specific API versions. With versioned updates you can test
and adopt run-time behavior changes for individual flows at your convenience.

SEE ALSO:

Flow Builder Tour


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Flow Usage-Based Entitlements

Like feature licenses, usage-based entitlements don’t limit what you can do in Salesforce; they add
to your functionality. If your usage exceeds the allowance, Salesforce contacts you to discuss
additions to your contract. In the meantime, your flow interviews run as usual.

For per-month entitlements, your contract determines the start and end of the month. You can
view the start and end dates for your org’s usage-based entitlements on the Company Information
page in Setup.

Note:

**•** Flows that are launched by another flow via a Subflow element don’t count toward your
allocation of flow interviews.

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

This table describes additional allocations that are granted based on purchased user licenses. These allocations apply to the org. It doesn’t
matter which users run the flows.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

If you have questions about increasing your allocation, contact your Salesforce account executive.

SEE ALSO:

[Usage-Based Entitlements](https://help.salesforce.com/s/articleView?id=sf.users_understanding_tenant_usage_entitlements.htm&language=en_US)

[View Your Salesforce Org’s Usage-Based Entitlements](https://help.salesforce.com/s/articleView?id=sf.users_usagebased_entitlements_viewing.htm&language=en_US)

Flow Types

Reevaluate Records in the Process Builder

How Does Salesforce Process Scheduled Actions?

General Flow Limits

When using flows, keep flow limits and Apex governor limits in mind.

The maximum flow interview size is 1,000,000 B (approximately 1 MB). If the interview is too large,
it can't be persisted or paused.

These limits apply to segment-triggered flows, form-triggered flows, and automation-event triggered
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

**Per-Org Limit** **Starter**
**Edition**

**Marketing**
**Cloud**
**Growth**
**Edition**

**Marketing**
**Cloud**
**Advanced**
**Edition**

Active flows per flow type 50 500 750

Total flows per flow type 2,000 50,000 50,000

These limits apply to all other flows.

**Per-Org Limit**

**Essentials or**
**Professional**
**Editions**

**Enterprise,**
**Unlimited,**
**Performance, or**
**Developer**
**Editions**

Versions per flow 50 50

Executed elements at runtime per flow None None [1]

Active flows per flow type 5 2,000

Total flows per flow type 5 4,000

Groups of scheduled actions from processes that are executed per hour based on a specific 1,000 1,000
time

Combined total of these automations that start or resume based on a record’s field value. 20,000 20,000

**•** Resume events that are defined in active flows

**•** Groups of scheduled actions that are defined in active processes

**•** Time triggers that are defined in active workflow rules


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**Per-Org Limit**

**•** Inactive flow interviews that are resumed

Schedule-triggered flow interviews per 24 hours

**Essentials or**
**Professional**
**Editions**

250,000, or the number of user licenses in
your org multiplied by 200, whichever is
greater. [2]

**Enterprise,**
**Unlimited,**
**Performance, or**
**Developer**
**Editions**

1In API version 57.0, the limit of 2000 flow elements was removed. In API version 56.0 and earlier, flows could have a maximum of 2000
flow elements.

2The license types that count toward this limit include full Salesforce and Salesforce Platform user licenses, App Subscription user licenses,
Chatter Only users, Identity users, and Company Communities users.

SEE ALSO:

Automate Tasks with Flows

Flow Limits and Considerations

Per-Transaction Flow Limits

Salesforce strictly enforces limits to ensure that any runaway flows don't monopolize shared resources
in the multitenant environment. Per-transaction limits, which Apex enforces, govern flows. If an
element causes the transaction to exceed governor limits, the system rolls back the entire transaction.
The transaction rolls back even if the element has a defined fault connector path.

**1**
#### **Per-Transaction Limit Value**

Total number of SOQL queries issued 100

(All executions of Get Records elements, and
executions of Update Records or Delete Records
elements that use filter conditions)

Total number of records retrieved by SOQL 50,000
queries

(All executions of Get Records elements, and
executions of Update Records or Delete Records
elements that use filter conditions)

Total number of DML statements issued 150

(Create Records, Update Records, and Delete
Records executions)

Total number of records processed as a result 10,000
of DML statements


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**1**
**Per-Transaction Limit** **Value**

Maximum CPU time on the Salesforce servers 10,000 milliseconds

Total number of duplicate updates allowed in one batch 12

1 Autolaunched flows are part of the larger transaction that they were launched through and share that transaction’s limits. For example,
flows launched from Apex or a process are executed with the Apex or process actions as part of the larger transaction. Flows with Screen
elements can span multiple transactions. A new transaction begins each time the user clicks **Next** in a screen. Flows with Wait elements
span multiple transactions. A transaction ends when a flow interview pauses for an event. When the flow interview resumes, a new
transaction begins. Everything after the Wait element is executed as part of a batch transaction that includes other resumed interviews.
The batch includes interviews executed by the same user ID, have the same execution time, and have the same flow version ID.

SEE ALSO:

_Apex Developer Guide_ [: Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm)

General Flow Limits

#### Flow Builder Considerations

When you create a flow in Flow Builder, familiarize yourself with its limitations and behaviors. For
example, Flow Builder supports only a few locales. Because of intellectual property protection, you
can’t open flows installed from managed packages, unless the flows are templates.

Access to Salesforce Data

#### • Flow Builder uses the permissions and locale assigned to the current user. • Flow Builder has access to information that exists when you open it. If you modify data or

metadata in your org and must refer to it in a flow, close and reopen Flow Builder. For example,
if you add a custom field or modify an Apex class with Flow Builder open, close and reopen
#### Flow Builder.

Opening Flows That were Saved in Cloud Flow Designer

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When you open a flow version created with Cloud Flow Designer in Flow Builder, the Save button is disabled. To edit that version in
#### Flow Builder, save it as a new version in Flow Builder.

Text Formatting

If you open the Display Text screen component, Choice resource labels, help text, Pause confirmation screens, or input validation, Flow
Builder converts existing HTML to rich text. Unsupported HTML is removed. The following HTML tags are converted to rich text: <a>,
<b>, <br>, <font>, <i>, <li>, <p>, <span>, <u>, and <div>. HTML that is pasted into the rich text editor isn't supported.

Rich Text

**•** Images uploaded with the rich text editor are stored in the Files tab, and are visible to everyone in your org.

**•** Images uploaded with the rich text editor aren’t visible in Experience Cloud sites.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**•** Toggle back to plain text when using a text template in a Post to Chatter action, Send Email action, or in a custom action that expects

plain text. Click and select **Plain Text** .

**•** If you include incomplete HTML symbols such as _`<`_ in rich text, Flow Builder removes the symbols and adjacent strings. For example,
Flow Builder renders _`2<3`_ as `2` . Include spaces around HTML symbols to render them. For example, _`2 < 3`_ .

Date/Time Values

At run time, time zones for date/time values can differ from what you see in Flow Builder. During run time, date/time values reflect the
time zone settings of the user who’s running the flow. In Flow Builder, date/time values reflect the time zone settings of the admin who
configures the flow.

Text Values

**•** Flow Builder doesn't support UTF-8 encoding for text in user input fields.

**•** Flow Builder contains embedded fonts for all locales it supports. The supported locales are:

**–** Chinese (Traditional)

**–** Chinese (Simplified)

**–** English (US)

**–** French (France)

**–** German (Germany)

**–** Japanese (Japan)

**–** Spanish (Spain)

If you enter unsupported characters for a supported locale, they're displayed using system fonts instead of the embedded fonts.

In unsupported locales, your system font settings are used to display all characters in Flow Builder.

**•** Don't enter the string _`null`_ as the value of a text field in Flow Builder.

Output Values

To store the same output value in multiple variables, assign the value to one variable. Then add an Assignment element after the action,
and set the other variables to the value of the first variable.

Managed Packages

Flow Builder can’t open a flow that is installed from a managed package, unless the flow is a template or overridable.

Step Elements

You can’t add or update steps to a flow in Flow Builder. You also can’t convert steps into screens. If you added a step in Cloud Flow
Designer, the step still appears on the canvas. We recommend that you remove all steps from your flows.

Action Elements

Legacy Apex actions aren’t organized by the tag in the plug-in code.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Flows Upgraded from Winter ’12 and Earlier

If you open a flow that was last opened in Winter '12 or earlier, each Boolean decision is converted to a multi-outcome Decision element
that:

**•** Uses the same label as the old decision.

**•** Takes the API name of the old decision, appended with “_switch”.

**•** Has an outcome labeled “True”. This outcome's API name matches that of the old decision, and its conditions are migrated from the
True outcome of the old decision.

**•** Has a default outcome labeled “False”.

Terminology

The terminology in some warnings, error messages, and debug details isn’t updated for Flow Builder or Cloud Flow Designer.

#### Salesforce Feature Considerations for Flows

When designing flows, consider these Salesforce features.

##### Security Considerations for Flows

When designing flows, keep these security considerations in mind.

External Object Considerations for Flows
Keep these considerations in mind when building flows that include external objects.

Lightning Component Considerations for Flows
Keep these considerations in mind when building flows that include Lightning components.

Considerations for Reactivity in Screen Flows
Review these considerations before you set up reactivity in your screen flows. Reactivity is
supported with API version 57.0 or later.

##### Security Considerations for Flows

When designing flows, keep these security considerations in mind.

Flow Interviews

When a user session expires, in-progress flow interviews are interrupted and can’t be resumed. If
the flow executed actions, such as a Create Records or Post to Chatter element, those actions aren’t
rolled back. But other progress through the interview, such as what the user entered on the screen,
is lost.

Tip:

**•** Set your session timeout settings to log out users after an appropriate period.

**•** Encourage your users to pay attention during interviews for alerts about their sessions
expiring soon.

**•** Remind users to avoid running flows during release upgrades. A typical upgrade takes
about 5 minutes.

Paused or waiting flow interviews aren’t affected by expired user sessions.


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

Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Shield Platform Encryption

You can’t filter or sort records by encrypted fields for these elements and resources.

**•** Update Records element

**•** Delete Records element

**•** Get Records element

**•** Record Choice Set resource

Screen Flow Inputs

For enhanced security, remove all HTML from publicly accessible input fields in screen flows. For example, an input field on a publicly
accessible screen flow is mapped to a rich text field in Salesforce. To prevent a malicious URL from accessing the rich text field, create a
separate flow on the object to strip out the HTML. Optimize the new flow for fast field updates, and set it to run whenever the input field
isn’t blank. Because several sources can write to a publicly accessible input field, check for HTML at the field level and not at the screen
level.

You can also use an existing Apex trigger on the object to strip out the HTML.

SEE ALSO:

[Modify Session Security Settings](https://help.salesforce.com/s/articleView?id=sf.admin_sessions.htm&language=en_US)

##### External Object Considerations for Flows

Keep these considerations in mind when building flows that include external objects.

**•** When you create or update external object records, don’t set values for indirect lookup
relationships that map to a different data type on the external system. For example, don’t set
a value for a Text indirect lookup relationship that maps to a Date value on the external system.

**•** To find the Salesforce record linked to from an external object by an indirect lookup relationship,
match the parent object’s `Id` field to the ID in the indirect lookup relationship field. Select the
indirect lookup relationship, and add _`.Id`_ before the closing curly bracket. For example, an
indirect lookup relationship connects Contact (parent standard object) to Social Media post
(child external object). In a flow, the record variable `{!socialMediaPost}` contains field
values for a social media post. To find the parent contact record, in a Get Records element, filter
by:

```
  Id Equals {!socialMediaPost.indirectLookupRelationship_c__c.Id}

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

**•** To find the parent external object record linked to by an external lookup relationship, match the parent record’s external ID to the
external lookup relationship on the child record. For example, an external lookup relationship connects Product Catalog Item (parent
external object) to Case (child standard object). In a flow, the record variable `{!case}` contains field values for a support case. To
find the parent product catalog item record, in a Get Records element, filter by:

```
  ExternalId Equals {!case.externalLookupRelationship_c__c}

```

**•** If Salesforce creates, updates, or deletes data in your org and then accesses external data in the same transaction, an error occurs.
In your flow, we recommend using a separate transaction to access data in an external system. To do so, end the prior transaction
by adding a screen or local action to a screen flow or a Wait element to an autolaunched flow. If you use a Wait element, don't use
a record-based resume time.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

For example, a screen flow creates a contact and then displays a confirmation screen. Next, the flow updates the contact in the
external system. The flow doesn’t fail because it uses a separate transaction to access the external data.

**•** Don’t update the External ID and Display URL fields in a process or flow.

**•** Record-change processes aren’t supported.

**•** A process or flow must save or commit changes to a standard or a custom object before changing an external object within the
same transaction. To commit changes to a standard or custom object, you have different options depending on the tool. After an
action that changes a standard or custom object record:

**–** In Flow Builder, add a screen, local action, or Wait element that pauses until a flow-based time occurs.

**–** In Process Builder, add a scheduled action.

##### Lightning Component Considerations for Flows

Keep these considerations in mind when building flows that include Lightning components.

Note: These topics are designed for developers that build Lightning components.

**•** [Lightning components in flows must comply with Lightning Locker restrictions.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/security_code.htm)

**•** [Flows that include Lightning components are supported only in Lightning runtime.](https://help.salesforce.com/articleView?id=flow_distribute_runtime.htm&language=en_US)

###### Which Custom Lightning Component Attribute Types Are Supported in Flows?

Not all Lightning component data types are supported in flows. You can map only these types
and their associated collection types between flows and Lightning components.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Design Attribute Considerations for Flow Screen and Action Components
To expose an attribute in Flow Builder, define a corresponding `design:attribute` in the
component bundle's design resource. Keep these guidelines in mind when defining design attributes for flows.

Runtime Considerations for Flows That Include Aura Components
Depending on where you run your flow, Aura components can look or behave differently than expected. The flow runtime app that's
used for some distribution methods doesn't include all the necessary resources from the Lightning Component framework. When
a flow is run from Flow Builder or a direct flow URL (https://yourDomain.my.salesforce.com/flow/MyFlowName), `force` and
`lightning` events aren’t handled.

###### Which Custom Lightning Component Attribute Types Are Supported in Flows?

Not all Lightning component data types are supported in flows. You can map only these types and
their associated collection types between flows and Lightning components.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**Flow Data**
**Type**

##### **Lightning Valid Values**

**Component**
**Attribute**
**Type**

Apex Custom Apex
Class

Apex classes that define `@AuraEnabled` fields. Supported
data types in an Apex class are Boolean, Integer, Long, Decimal,
Double, Date, DateTime, and String. Single values as well as Lists
are supported for each data type.

Boolean Boolean

**•** True values: _`true`_, _`1`_, or equivalent expression


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**Flow Data Type**

**Lightning** **Valid Values**
**Component**
**Attribute Type**

**•** False values: _`false`_, _`0`_, or equivalent expression

Currency Number Numeric value or equivalent expression

Date Date _`"YYYY-MM-DD"`_ or equivalent expression

Date/Time (API DateTime _`"YYYY-MM-DDThh:mm:ssZ"`_ or equivalent expression
name is DateTime)

Number Number Numeric value or equivalent expression

Multi-Select Picklist String

(API name is
Multi-Select Picklist.)

String value or equivalent expression using this format:

```
"Blue; Green; Yellow"

```

Picklist String String value or equivalent expression

Record, with a
specified object

(API name is
SObject.)

The API name of the
specified object,
such as Account or
Case

Map of key-value pairs or equivalent expression.

Flow record values map only to attributes whose type is the specific object. For example,
an account record variable can be mapped only to an attribute whose type is Account.
Flow data types aren’t compatible with attributes whose type is Object.

Text String String value or equivalent expression

(API name is Text.)

###### Design Attribute Considerations for Flow Screen and Action Components

Calculating Minimum and Maximum Values for an Attribute

To validate min and max lengths for a component attribute, use a flow formula or the component's client-side controller.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Modifying or Deleting **`design:attribute`** Nodes

If a component’s attribute is referenced in a flow, you can’t change the attribute’s type or remove it from the design resource. This
limitation applies to all flow versions, not just active ones. Remove references to the attribute in all flow versions, and then edit or delete
the attribute in the design resource.

###### Runtime Considerations for Flows That Include Aura Components

Depending on where you run your flow, Aura components can look or behave differently than
expected. The flow runtime app that's used for some distribution methods doesn't include all the
necessary resources from the Lightning Component framework. When a flow is run from Flow
Builder or a direct flow URL (https://yourDomain.my.salesforce.com/flow/MyFlowName), `force`
and `lightning` events aren’t handled.

To verify the behavior of your Aura components, test your flow in a way that handles `force` and
`lightning` events, such as `force:showToast` . You can also add the appropriate event
handlers directly to your component.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

##### Considerations for Reactivity in Screen Flows

Review these considerations before you set up reactivity in your screen flows. Reactivity is supported
with API version 57.0 or later.

For information on how to set up components for reactivity, refer to Make Your Screen Flows
Reactive

General Considerations

**•** Manual outputs of components don’t support reactivity. If you manually set a component
output, that variable doesn’t change on the same screen when referenced in other components.

**•** Help text and labels don't react to changes in other components.

**•** Data types must match when you’re mapping an output to another component’s input to
support reactivity.

**•** If validation rules exist for custom components, reactive changes don't trigger validation.

EDITIONS

Available in: Lightning
Experience, Salesforce
Classic.

Available in: All versions of
the mobile app in
Professional, Performance,
and Unlimited editions.

**•** The global variable $Flow is reactive. All other global variables such as Custom Labels, Custom Settings, $Organization, $Profile, are
not reactive.

**•** When mapping a `DateTime` field to `Time`, the value is converted to GMT and stays converted when navigating between screens.
If mapped to a `DateTime` field, the locale is preserved. For example, if the time value is 8:00 AM in your locale, the converted GMT
time could be several hours off your time locale (such as 4:00 PM). Refer to A Note About Date/Time and Time Zones for information
[about Converting Between Date/Time and Text and Date/Time in time zones: Using Date, Date/Time, and Time Values in Formulas](https://help.salesforce.com/s/articleView?id=sf.formula_using_date_datetime.htm&type=5&language=en_US)

#### Salesforce Data Considerations for Flows

When designing flows, keep these Salesforce data considerations in mind.

Setting the Record Type

For example, use a Get Records element to find the Record Type record whose name is “Reduction
Order.” Then store that record type’s ID in a variable. You can then use the variable to set the `Order`
`Record Type` field on an order record.

To set the record type for a record, use the record type’s ID. Look up the record type by its name
and then store its ID in the flow.

Working with Person Accounts

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If your org uses person accounts, reference `Contact.Salutation` instead of `Account.Salutation` .

Null Values

A flow fails when a filter condition from a Get Records element or an Update Records element references a value that is null. Before you
reference a value in a filter condition, add a Decision element to check if the value is null.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Merge Fields

A flow can reference the value of a merge field at run time only if a flow resource stores the value. For example, a flow can't reference a
merge field that a messaging template contains.

SEE ALSO:

Flow Operations and Read-Only Fields

Considerations for the Apex-Defined Data Type

External Object Considerations for Flows

Flow Operations and Read-Only Fields

Understand when flows have read-only access to field values. You can control the behavior when
a flow tries to update a read-only field and remove read-only field values from flow operations.

###### Which Fields Are Inaccessible When a Flow Creates or Updates Records?

A flow can perform an operation only if the running user has permission to do so. When a flow
tries to create or update records, fields that the running user can’t edit are considered _inaccessible_,
or read only. A field can be inaccessible because the user hasn’t been granted permission to
edit the field or because it’s a system field that’s always read only.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Control What Happens When a Flow Tries to Set Values for Read-Only Fields

and **Developer** Editions

When a flow tries to perform an action, such as create or update records, it uses a flow request
to set values for specific fields. But what happens if the running user doesn’t have edit access
to all those fields? When you use a record variable or record collection variable in Create Records
and Update Records elements, that’s up to you. To control the behavior, select or deselect the `Filter inaccessible`
`fields from flow requests` preference.

Remove Read-Only Fields from a Record Variable
If a flow tries to update fields that the running user can’t edit and `Filter inaccessible fields from flow`
`requests` is not enabled for your org, the flow fails. If your record variable includes read-only fields and you can’t grant your
running users “Edit” permissions for those fields, remove the fields from the record variable. Set the field values individually in a
Create Records or Update Records element or copy the writable field values into a new record variable.

###### Which Fields Are Inaccessible When a Flow Creates or Updates Records?

A flow can perform an operation only if the running user has permission to do so. When a flow tries
to create or update records, fields that the running user can’t edit are considered _inaccessible_, or
read only. A field can be inaccessible because the user hasn’t been granted permission to edit the
field or because it’s a system field that’s always read only.

To determine which fields are system fields, see the _Object Reference for Salesforce and Lightning_
_Platform_ . To determine which other fields aren’t editable, review the running user’s permissions.

How Did Read-Only Fields Get in My Record Variable?


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

What Do I Do When My Record Variable Includes Read-Only Fields?

For each read-only field that’s stored in your record variable:

**1.** Determine whether the flow uses that field anywhere. If it doesn’t, update the flow so that it doesn’t store a value for that field. This
suggestion applies only if an element in the flow, such as Get Records, populates the variable.

For example, a Get Records element stores `CreatedByDate`, but no other elements reference that field. You update the Get
Records element so that it’s no longer storing `CreatedByDate` .

**2.** If the read-only field is referenced in the flow, give the running users the permissions needed for the flow to execute its operations.

**3.** If you can’t give the running users the needed permissions for a field, update the flow so that it doesn’t try to update that field.

Here's an example: Using an Update Records element, a flow updates several fields on an account. While your users can edit
`Description` and `Account Rating`, they can’t edit `Owner ID` or `LastModifiedDate` . To prevent the flow from failing
at run time:

**•** Give your users “Edit” permission for `Owner ID` .

**•** Copy only the writable field values ( `Description`, `Account Rating`, and `Owner ID` ) from the original record variable
into a new record variable. Reference the new record variable in the Update Records element.

Copying only the writable field values ensures that the flow doesn’t try to set a value for `LastModifiedDate` at run time.

SEE ALSO:

Remove Read-Only Fields from a Record Variable

Control What Happens When a Flow Tries to Set Values for Read-Only Fields

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/system_fields.htm)_ : System Fields


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

###### Control What Happens When a Flow Tries to Set Values for Read-Only Fields

Tip: We recommend disabling this preference so that you always know when a flow doesn’t set all expected field values.

**1.** From Setup, enter _`Automation`_ in the `Quick Find` box, then select **Process Automation Settings** .

**2.** Select or deselect **Filter inaccessible fields from flow requests** .

If your org was created in Winter ’17 or earlier, the preference is enabled by default. Otherwise, the preference is disabled by default.

Example: A flow updates several fields on an opportunity by using a record variable in an Update Records element. At run time,
the flow tries to update the Acme account on behalf of your user. The user can edit `Stage` and `Close Date` but not `Amount` .
As a result, the flow doesn’t have permission to update `Amount` .

**•** If `Filter inaccessible fields from flow requests` is selected, the flow successfully updates the account,
but it only updates `Stage` and `Close Date` . The flow doesn’t notify anybody that `Amount` wasn’t updated.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**•** If `Filter inaccessible fields from flow requests` isn’t selected, the flow fails to update the account.
The admin receives a flow error email. The email includes this error.

```
       INVALID_FIELD_FOR_INSERT_UPDATE: Unable to create/update fields: Amount

```

That’s API-speak for “The running user doesn’t have permission to edit the Amount field.”

Warning: If you change your org’s selection for this preference, use a sandbox to test how the change impacts your flows.
Consider following the same process as you would for a critical update.

SEE ALSO:

Which Fields Are Inaccessible When a Flow Creates or Updates Records?

###### Remove Read-Only Fields from a Record Variable

If a flow tries to update fields that the running user can’t edit and `Filter inaccessible`
`fields from flow requests` is not enabled for your org, the flow fails. If your record
variable includes read-only fields and you can’t grant your running users “Edit” permissions for those
fields, remove the fields from the record variable. Set the field values individually in a Create Records
or Update Records element or copy the writable field values into a new record variable.

Note: If the read-only fields in the record variable are populated by a Get Records or
Assignment element, consider updating those elements so that they don’t populate that
field at all.

Copy Field Values from One Record Variable to Another

Record variables and record collection variables can have values set for fields that the running user
can’t edit. However, you can use the writable values to create or update records with Create Records
or Update Records elements. To do so, map the writable values from the original record variable
into a new record variable.

Note: With record collection variables, use loops to map the field values to a new collection.

**1.** Add an Assignment element to your flow. Make sure that the flow executes this element after
the original record variable has been populated but before the Create or Update element.

**2.** For each writable field in the original record variable, add a row.

Variable—Select {! _`recordVar2`_ . _`field`_ }, where _`recordVar2`_ is the name of the new
variable and _`field`_ is the field on that variable.

Operator—Select **equals** .

Value—Select {! _`recordVar1`_ . _`field`_ }, where _`recordVar1`_ is the name of the original
variable and _`field`_ is the field on that variable.

Note: If you plan to reference the variable in an Update Records element, include the
record’s ID in the new record variable. Although `Id` is read only, the flow uses the value
to determine which records to update.


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

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Example: You have a case record variable called `{!myCaseVar_all}` . It stores values for some read-only fields, so you can’t
use it in an Update Records element. Copy the fields that you want to update to a new record variable: `IsEscalated` and
`Status` . Also, copy `Id` because it’s required for an update operation. Here’s what those assignment rules look like.

The same example works for a record collection variable. However, because you can’t directly change the values of a collection
variable, you use a loop. After the flow has iterated over every item in the original collection, it exits the loop.

**•** Using a Loop element, the flow passes each item’s values into a loop variable ( `{!myCaseLoopVar_original}` ).

**•** For each iteration, an Assignment element copies the `Id`, `IsEscalated`, and `Status` fields from the loop variable to
another record variable ( `{!myCaseLoopVar_final}` ).

**•** The flow then adds the `{!myCaseLoopVar_final}` variable’s values to a new collection. The second Assignment
element includes this assignment rule.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

SEE ALSO:

Flow Element: Create Records

Flow Element: Update Records

##### Considerations for the Apex-Defined Data Type

Understand these considerations when you’re building flows that include an Apex-defined data
type.

Flow Builder

**•** Cloud Flow Designer isn’t supported.

**•** A custom component that displays a value, like the Display Text screen component, can display
all fields from an Apex-defined variable. For example, the {!Car} variable stores all field values
that are defined in the Car Apex class. If a Display Text screen component has the {!Car}
Apex-defined variable as the input attribute, the screen displays all the fields from the Car Apex
class. If the Apex class is from a managed package, only the Apex class ID is displayed.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** The first time you open an element or resource window in an org with over 200 Apex classes that have the `@AuraEnabled`
annotation, the window can take longer to load.

**•** Deprecated Apex classes in a managed package appear in Flow Builder.

**•** If a flow invokes Apex, the running user must have the corresponding Apex class assignment in their profile or permission set.

**•** A flow doesn't support a list of lists data type if it's a field on a flow variable that's an Apex-defined data type.

Apex

**•** Supported data types in an Apex class are Boolean, Integer, Long, Decimal, Double, Date, DateTime, and String. Single values and
lists are supported for each data type. Multiple Apex classes can be combined to represent complex web objects.

**•** The @AuraEnabled annotation for each field is required.

**•** A constructor with no arguments is required.

**•** Class methods aren’t supported.

**•** Getter methods for fields aren’t supported.

**•** Inner classes aren’t supported.

**•** An outer class that has the same name as an inner class isn’t supported.

**•** Referential integrity isn’t supported for Apex class fields. For example, a flow has an Apex-defined variable that represents the model
field in the Car Apex class. If the model field is modified or deleted in the class, the flow fails.

Input and Output Values

**•** An Apex-defined variable value can't be set or stored outside the flow. The value can't be passed to a Subflow element.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Local Actions

**•** An Aura component that’s used as a local action can’t set an Apex-defined attribute.

#### Flow Feature Considerations

When designing flows, keep these flow feature considerations in mind. Also, some resources,
elements, and screen components have more considerations that are described in their reference
topics.

Flow Conditional Visibility Considerations
Before you set visibility for a screen component, understand the behavior of conditional visibility
in flows.

Considerations for Flow Choice Components with Default Values
Understand how to set a default value using any flow resource for a screen flow’s choice
component, such as Radio Buttons or a Multi-Select Picklist component.

Flow Variable Considerations
Before you create a variable resource, understand the behavior of variables in flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Multi-Select Resource and Screen Field Considerations for Flows
Checkbox Group, Multi-Select Picklist, and Choice Lookup screen components let flow users select multiple choices. Before you start
using these screen components, understand how they work in flows—both when you design the flow and when your users run it.

Paused Flow Interview Considerations
Before you design flows that contain one or more Wait elements, understand the behavior and guidelines.

Flow Stage Considerations
Before you add stages to your flow, understand how stage references and default active stages work, as well as considerations for
troubleshooting stages.

Two-Column Flow Considerations
If your org has Lightning runtime enabled, you can control whether a flow displays in one column or two columns. Before you use
this feature, understand how the flow layout currently behaves.

Schedule-Triggered Flow Considerations
A schedule-triggered flow starts at the specified time and frequency for a batch of records. Understand the considerations and special
behaviors of schedule-triggered flows, also known as scheduled flows.

Record-Triggered Flow Considerations
A record-triggered autolaunched flow makes additional updates to the triggering record before or after it’s saved to the database.
Understand the considerations and special behaviors of flows that make before- and after-save updates.

SEE ALSO:

Flow Resources

Flow Elements

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

##### Flow Conditional Visibility Considerations

Before you set visibility for a screen component, understand the behavior of conditional visibility
in flows.

Null and Empty Strings

A `null` value is evaluated the same way as a `{!$GlobalConstant.EmptyString}` .

Unsupported Data Types and Operators

**•** These operators aren’t supported in conditional visibility.

**–** Was Visited

**–** Was Set

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** These data types aren’t supported in conditional visibility, but you can reference attributes and fields.

**–** Apex-defined data types

**–** Record variables

**•** You can’t reference these results in conditional visibility.

**–** Results of Apex-defined invocable actions

**–** Results of a flow referenced by the current flow with the Subflow element

**•** Any screen input component with **Manually assign variables (advanced)** selected isn’t available as a resource for conditional
visibility on the same flow screen.

**•** Text that has merge fields included isn’t supported in values. Merge fields on their own are supported.

Text Templates and Formulas

**•** Initial values are evaluated in text templates and formulas.

**•** Changes based on user input aren’t evaluated.

Hidden Screen Input Components

**•** Screen input components hidden by conditional visibility aren’t required when a user runs the flow, even if `Required` is set to
_`{!$GlobalConstant.True}`_ . When the component appears to the user, it’s treated as required.

**•** If a screen input component is hidden because it doesn’t meet conditional visibility requirements, its value is set to null. But hidden
picklists in a Dependent Picklists component aren’t set to null unless the entire Dependent Picklists component is hidden.

**•** In an Update Records element, if you update a field by using the value of a hidden screen component, the field value is set to blank.
Instead, update the field by using a Formula resource that checks if the field is blank before setting the field value. For example, use
this formula.

```
  IF( ISBLANK( {!myTextField} ), {!myOriginalFieldValue}, {!myTextField})

```

**•** When you define a condition to set component visibility, you can specify a variable as the resource value. The variable can traverse
up to three object fields, for example, _`Contact.Account.Owner`_ .


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Sections and Conditional Field Visibility

If a section’s visibility conditions reference a component contained within the section, the entire section is hidden. If a section’s visibility
conditions reference a component visibility condition and the visibility conditions evaluate as true, the section is visible.

Focus

When screen components or their parts are rendered after the screen is initially displayed, they’re never focusable. For example, if a
component asynchronously fetches a list of tasks to display, the focus can’t be set to any of the tasks. If a screen component uses
conditional visibility and appears only after user input, the focus can’t be set to any part of the screen component.

Circular Logic

Avoid circular logic in your conditions, which can result in poor performance, strange behavior, or an error when your flow is run.

Related Record Fields

Related record fields in your field visibility conditions work only for Lookup fields that have a value set when entering the screen.

Commas in Condition Values

If your condition value contains a comma, add a quotation mark at the beginning and the end of the value. For example, _`“Email,`_
_`Phone, and Social Media”`_ .

Performance

For the best performance, minimize the number and complexity of conditional visibility conditions on your screen components and
record fields. There are other ways to control what screen components and record fields your screen flow users have access to view or
update.

**•** Use a Section component. If you need multiple screen components or record fields to be visible using the same logic, put them in
a Section component. Then, set the conditional visibility on the Section component, instead of on each component or field.

**•** Use the component’s Disabled attribute instead of conditional visibility. If you don’t want your screen flow users to fill out a screen
component’s input fields, but it’s OK for them to see the fields, you can disable the component input fields. Set the screen component’s
Disabled attribute by selecting a resource with a Boolean value. For example, set the Disabled attribute to a Formula resource that
evaluates to `true` if another screen component is empty.

**•** Use reactive formulas or Screen Actions. If you want to conditionally hide and set the default value of a screen component dynamically,
depending on the value of another screen component, you don’t need to add a screen component for each value. Instead, use a
single conditionally visible screen component and use a reactive formula or screen action to populate the default value. See Reactive
Screen Flow Formula Operators.

SEE ALSO:

Make Flow Screens Dynamic with Conditional Visibility


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

##### Considerations for Flow Choice Components with Default Values

Understand how to set a default value using any flow resource for a screen flow’s choice component,
such as Radio Buttons or a Multi-Select Picklist component.

The Default Value field appears below the choice options list when you add at least one choice. For
the Default Value field, specify a picklist value or another flow resource (a variable, a field on a record
variable, a manually entered value, and so on). You can choose any compatible type reference for
the flow. You can use a value from a record as the default value, which applies to picklist choices
or record choices.

When you save and run a flow, the default value determines which options are preselected. None
of the choice options are duplicated, and the order of the choices is retained.

Flow run time behavior for a default choice option

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

At run time, Salesforce preselects a choice if its value matches the component's default value. When the default value references a flow
resource, Salesforce resolves that reference before matching. When you save and run the flow, the default value is preselected in the
resulting list of choices.

For choice components that let the user select a single option, such as Picklists and Radio Buttons, Salesforce preselects the first choice
that matches:

For choice components that let the user select multiple options, like Multi-Select Picklists and Checkbox Groups, Salesforce preselects
every choice that matches:

Multiple default values for a choice component

To specify multiple default values for choice components that let the user select multiple options, separate the values with semicolons.
If the resolved default value includes semicolons, like “Red;Blue”, Salesforce treats each value as a separate default. For example, to set
the default value to both “Red” and “Blue”, enter _`Red;Blue`_ . At run time, Salesforce preselects every choice option whose value is Red


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

or Blue. Using values that contain semicolons can cause issues with multi-select value matching behavior. If a choice's value is an exact
match, like Red;Blue, then Salesforce doesn’t select it.

If you configure a choice component with multiple records, use a variable whose value resolves to the record ID for each record, and
separate the IDs with a semicolon.

Default values from collection choice sets

If you reference a value from a collection choice set as the default value of a choice component, the default value is null when the screen
loads. To trigger the screen to reload and display the value at runtime, reference the value on the same screen or wrap the value in a
formula.

##### Flow Variable Considerations

Before you create a variable resource, understand the behavior of variables in flows.

Referring to Blank Fields or Resources

**•** If you leave a field or resource value blank, the value is `null` at run time. To treat a text value
as an empty string instead of `null`, set it to `{!$GlobalConstant.EmptyString}` .

Boolean Variables

**•** Boolean Types Treat `null` Differently than `false`

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

**•** A flow treats `null` as a different value than `false` . For example, if you try to find a record
whose checkbox field is set to `null`, no records are returned. Instead, look for records where
the checkbox field is set to `false` . If you’re using a variable (such as `myCheckbox =`
`{!varBoolean}` ), make sure that the variable isn’t set to `null` before you reference it in your record filter or condition.

Percentage Variables

**•** If a flow uses record variables to manipulate percentage values, test the flow carefully. When you insert a value into a record variable’s
percentage field and then reference that field in a formula, the value is divided by 100.

For example, an opportunity’s Probability field is set to 100. If you assign that value to the `{!Opportunity.Probability}`
record variable, the value is still 100. But if you create a formula whose expression is `{!Opportunity.Probability}`, the
value is 1.

Available for Input/Output

**•** Disabling input or output access for an existing variable can break the functionality of applications and pages that call the flow and
access the variable. For example, you can access variables from URL parameters, subflows, and processes.

Setting Input Variables

**•** Process Builder: When a process or flow launches another flow, that flow’s input variables can be assigned values during the launch.
However, for a text, picklist, or multi-select picklist variable that isn’t a collection, a value of `null` is converted to an empty string.

**•** Actions: Flow actions let you pass the value of the record's ID field into the flow, but that's it. If your flow has a Text input variable
called recordId, the action passes the record's ID into that variable at runtime. If not, it doesn't and the flow tries to run anyway.

**•** Lightning App Builder: Collection variables, record variables, and record collection variables aren’t supported. The Flow component
supports only manually entered values for input variables. Text input variables accept a maximum length of 4,000 characters.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Distributing Flows

**•** When you distribute a flow, don't pass a currency field value from a Salesforce record into a flow currency variable with a URL
parameter. When a currency field is referenced through a merge field (such as `{!Account.AnnualRevenue}` ), the value
includes the unit of currency’s symbol (for example, $). Flow currency variables can accept only numeric values, so the flow fails at
run time. Instead, pass the record's ID to a text variable with a URL parameter. Then in the flow, use the ID to look up that record’s
value for the currency field.

Number Variables

**•** Number variables are treated as integers by default.

Multi-Select Resource and Screen Field Considerations for Flows

Checkbox Group, Multi-Select Picklist, and Choice Lookup screen components let flow users select
multiple choices. Before you start using these screen components, understand how they work in
flows—both when you design the flow and when your users run it.

Configuring a Checkbox Group, Multi-Select Picklist, or Choice Lookup Screen
Component

**•** These screen components support only one default value. You can’t individually select multiple
default values. However, you can manually add a value in the default value field and separate
each value with a semicolon.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

**•** You can configure a record choice set resource to assign field values from a user-selected record
to variables in the flow. When a Checkbox Group, Multi-Select Picklist, or Choice Lookup screen
component uses a record choice set, only values from the last record that the user selects are stored in the flow variables. If multiple
Checkbox Group, Multi-Select Picklist, or Choice Lookup components on one screen use the same record choice set, the variable
assignments come from the last record selected from all of those components.

Using Values from a Checkbox Group, Multi-Select Picklist, or Choice Lookup Screen Component

**•** At run time, the value of a Checkbox Group, Multi-Select Picklist, or Choice Lookup screen component is a concatenation of the
user-selected choice values, separated by semicolons. If a selected choice’s value includes semicolons, the semicolons are removed.

**•** If you reference a Checkbox Group, Multi-Select Picklist, or Choice Lookup screen component in a flow condition:

**–** Make sure that each choice in the screen component has a choice value configured.

**–** Don’t use the same choice in multiple Checkbox Group, Multi-Select Picklist, or Choice Lookup screen components on the same
screen.

**•** If a Checkbox Group, Multi-Select Picklist, or Choice Lookup has at least one default value, at run time the choices are preselected if
the choice’s value matches the default value.

SEE ALSO:

Using Choice Resources with Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Paused Flow Interview Considerations

Before you design flows that contain one or more Wait elements, understand the behavior and
guidelines.

General Considerations

**•** After you deactivate a flow version, its paused interviews continue to wait for the configured
resume events. If a flow version has paused interviews, you can’t delete it.

**•** An interview can execute only one connector per Wait element. After one of its resume events
is processed, the remaining resume events are removed from the queue.

**•** If the user who started the interview is deactivated when Salesforce tries to execute a wait
connector, the interview fails to resume.

**•** If a flow is paused and the flow interview exceeds 1 MB, the interview fails to save and can’t be
resumed.

**•** You can’t call flows that contain wait elements as subflows.

Transactions and Paused Interviews

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Time-based resume events
are available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Platform event-based
resume events are available
in: **Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

A transaction ends as soon as a flow interview pauses for one or more resume events. When the
flow interview resumes, a new transaction begins. Everything after the Wait element is executed as part of a batch transaction that
includes other resumed interviews.

Interviews aren’t resumed independently. They’re grouped into a single batch that starts resuming within one hour after the first interview
enters the batch. Actions that execute as a result of the grouped interviews are also executed in that transaction. The batch can have
other interviews that resume at the same time, have the same flow version ID, and are executed by the same user ID. This behavior can
cause you to exceed your Apex governor limits if the resumed interview executes DML operations or SOQL queries through. For details,
see Per-Transaction Flow Limits on page 246.

**•** Flow elements, such as Create Records or Apex Action (Legacy)

**•** Apex triggers

**•** Immediate workflow actions

If a Wait element precedes a flow element that executes DML operations or SOQL queries:

**•** Ensure that your flows don’t let a single user execute DML operations or SOQL queries that can exceed limits between Wait elements.

**•** Consider using multiple Wait elements so that the DML operations and SOQL queries are performed in multiple transactions.

**•** Add fault paths for those elements so that the flow returns to the Wait element if the fault message contains: `Too many SOQL`
`queries` or `Too many DML operations` .

If an interview fails after it’s resumed:

**•** Prior interviews in that batch’s transaction are successful.

**•** Operations that the interview executed before it paused are successful.

**•** If a fault path handles the failure, operations that the interview executed between when it resumed and when it failed are successful.
The operation that caused the interview to fail isn’t successful.

**•** If a fault path doesn’t handle the failure, operations that the interview executed between when it resumed and when it failed are
rolled back. The operation that caused the interview to fail isn’t successful.

**•** The remaining interviews in that batch are tried.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Platform Events

[Tip: Make sure to also review the considerations and allocations for platform events.](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_considerations.htm)

**•** Supported Platform Events

Flows can subscribe to custom platform events and these standard platform events.

**–** AIPredictionEvent

**–** BatchApexErrorEvent

**–** FlowExecutionErrorEvent

**–** FOStatusChangedEvent

**–** OrderSummaryCreatedEvent

**–** OrderSumStatusChangedEvent

**–** PlatformStatusAlertEvent

**•** Formulas—To reference a platform event in a formula, pass the event data into a record variable in the Wait element. Then reference
the appropriate field in that record variable.

**•** Value Truncation—When you filter platform event messages, values for conditions can’t be more than 765 characters.

**•** Subscriptions Related List—On the platform event’s detail page, the Subscriptions related list shows which entities are waiting to
receive that platform event’s messages. The related list includes a link to each subscribed process. If flow interviews are waiting for
that platform event's messages, one “Process” subscriber appears in the Subscriptions related list.

**•** Uninstalling Events—Before you uninstall a package that includes a platform event, delete the interviews that are waiting for that
platform event’s messages.

**•** Einstein Predictions—A prediction event is sent for each Einstein prediction result, so use event condition filters if you want your
flow to be triggered only by predictions on a specific object. For example, if your flow uses a Wait element that acts only on predictions
written to Lead records, add a resume event to check that the AIPredictionEvent.TargetId field equals the current record.

If your flow updates a field that is used by an Einstein prediction, Einstein runs the prediction again and writes back the new results.
The new results generate a new prediction event that could trigger your flow again, resulting in a loop. To avoid creating a loop,
only update fields that aren’t used in Einstein predictions.

Platform Cache

When a flow contains a Wait element, make sure that later elements in the flow don't invoke Apex code that stores or retrieves values
from the session cache. The session-cache restriction applies to Apex actions and to changes that the flow makes to the database that
cause Apex triggers to fire.

Time-Based Resume Events

**•** Time-based resume events don’t support minutes or seconds.

**•** If an interview is waiting for a time in the past, Salesforce resumes the interview as soon as possible. Depending on how many actions
Salesforce is processing at the time, actions are executed within one hour.

For example, a flow is configured to email an opportunity owner seven days before the close date. An interview starts for an opportunity
with the close date set to today. Salesforce resumes the interview within an hour.

**•** An org can process up to 1,000 time-based resume events per hour. When a resume event is processed, its associated interview
resumes and any other resume events for that interview are removed from the queue. If an org exceeds this limit, Salesforce defers
the remaining resume events to be processed in the next hour.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

For example, an org has 1,200 resume events scheduled to be processed between 4:00 PM and 5:00 PM. Salesforce processes 1,000
resume events between 4:00 PM and 5:00 PM and the additional 200 resume events between 5:00 PM and 6:00 PM.

**•** You can’t archive a product or price book that’s referenced in a time-based resume event in a paused interview.

Flow-Based Time

For resume events based on a specific time, the resume time is evaluated using the time zone of the user who created the flow.

Record-Based Time

**•** For resume events based on a record field value, the resume time is evaluated using the org’s time zone.

**•** Resume events can’t reference:

**–** `DATE` or `DATETIME` fields that contain automatically derived functions, such as _`TODAY`_ or _`NOW`_ .

**–** Formula fields that include related-object merge fields.

**•** If you change a date field that’s referenced by an unexecuted resume event in a paused interview, Salesforce recalculates the resume
events associated with the interview.

For example, a flow is configured to email an opportunity owner seven days before the opportunity close date, and the close date
is 2/20/2014. The following things could happen.

**–** The close date isn’t updated before the interview resumes. Result: Salesforce resumes the interview on 2/13/2014 and sends
the email.

**–** The close date is updated to 2/10/2014 before the interview resumes. Result: Salesforce reschedules the resume event and the
interview resumes on 2/3/2014.

**–** The close date is updated to a date in the past. Result: Salesforce recalculates the resume event and resumes the interview shortly
after you save the record.

**•** If a resume event references a null date field when the interview executes the Wait element, Salesforce resumes the interview as
soon as possible. Depending on how many actions Salesforce is processing at the time, actions are executed within one hour.

**•** If a resume event references a date field that has a non-null value when the flow interview executes the Wait element and it’s updated
to `null` before the resume event is processed, Salesforce resumes the interview within an hour after the date field is updated.

**•** If a record or object that’s referenced by a resume event is deleted, the resume event is removed from the queue. If the interview
has no other resume events to wait for, the interview is deleted.

**•** Lead Convert Limitations

**–** You can’t convert a lead that’s referenced in a paused interview’s resume event.

**–** If Validation and Triggers from Lead Convert is enabled, existing operations on leads after a Wait element aren’t executed during
lead conversion.

**–** If a campaign member based on a lead is converted before a paused interview that’s associated with that record finishes,
Salesforce still executes the interview.

SEE ALSO:

_Platform Events Developer Guide_ [: Considerations for Defining and Publishing Platform Events](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_considerations.htm)

Flow Limits and Considerations

Flow Operators in Decision, Wait, and Collection Filter Elements

Flow Elements: Wait

_Platform Events Developer Guide_ [: Subscribe to Platform Even Messages with Flows](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_flow.htm)


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Flow Stage Considerations

Before you add stages to your flow, understand how stage references and default active stages
work, as well as considerations for troubleshooting stages.

Stage References

When you reference a stage merge field in a display text field or other label, it resolves to the stage’s
label. Everywhere else, a stage merge field resolves to the stage's fully qualified name:
_`namespace`_ . _`flowName`_ : _`stageName`_ or _`flowName`_ : _`stageName`_ .

Whenever possible, use the stage merge field to refer to stages, such as {!myStage}. When you
reference a stage in a subflow, use the fully qualified name.

Default Active Stages

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When you mark a stage resource **Active by Default**, the flow automatically sets values for the global variables. Use this setting when a
stage applies to every branch of the flow.

At run time, the default active stages are sorted in ascending order. How the flow uses the default active stages to update
`$Flow.ActiveStages` and `$Flow.CurrentStage` depends on whether the flow is a parent flow or a referenced flow.

Parent Flows

The default active stages are added to `$Flow.ActiveStages` in ascending order. `$Flow.CurrentStage` is set to the default
active stage with the lowest order.

When a flow references two flows, one with stages and one without, configure the flow with stages so that it sets the value for
`$Flow.ActiveStage` to null at the end of the flow. Then set the value for `$Flow.CurrentStage` to stage 1 at the start of
the flow.

Referenced Flows

The default active stages are inserted in `$Flow.ActiveStages` in ascending order. `$Flow.CurrentStage` isn’t automatically
updated.

**•** When `$Flow.CurrentStage` is included in `$Flow.ActiveStages`, the default active stages are inserted in
`$Flow.ActiveStages` after `$Flow.CurrentStage` .

For example, Flow1 sets `$Flow.ActiveStages` to “1, 2, 3, 4” and `$Flow.CurrentStage` to “3.” It then uses a Subflow
element to call Flow2. Flow2’s default active stages are “A, B, C.” When Flow2 starts, `$Flow.ActiveStages` becomes “1, 2, 3,
A, B, C, 4.” `$Flow.CurrentStage` is still “3.”

**•** When `$Flow.CurrentStage` isn’t included in `$Flow.ActiveStages`, the default active stages are added to the end of
`$Flow.ActiveStages` .

For example, Flow1 sets `$Flow.ActiveStages` to “1, 2, 3, 4” and doesn’t set `$Flow.CurrentStage` . It then uses a
Subflow element to call Flow2. Flow2’s default active stages are “A, B, C.” When Flow2 starts, `$Flow.ActiveStages` becomes
“1, 2, 3, 4, A, B, C.” `$Flow.CurrentStage` remains unset.

**•** When `$Flow.CurrentStage` is duplicated in `$Flow.ActiveStages`, the default active stages are appended after the
first occurrence.

For example, Flow1 sets `$Flow.ActiveStages` to “1, 2, 2, 3, 4” and `$Flow.CurrentStage` to “2.” It then uses a Subflow
element to call Flow2. Flow2’s default active stages are “A, B, C.” When Flow2 starts, `$Flow.ActiveStages` becomes “1, 2, A,
B, C, 2, 3, 4.” `$Flow.CurrentStage` remains “2.”


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Troubleshooting Stages

The flow error email doesn’t specify the values of `$Flow.ActiveStages` and `$Flow.CurrentStage` at the start of an
interview. To confirm what the initial values are, add temporary elements to display the initial values, such as in a screen display text
field.

SEE ALSO:

Show Users Progress Through a Flow with Stages

Flow Resource: Stage

Two-Column Flow Considerations

If your org has Lightning runtime enabled, you can control whether a flow displays in one column
or two columns. Before you use this feature, understand how the flow layout currently behaves.

Note: Starting in Winter ’23, two-column flow layouts are ignored. For a better layout option,
add Section components to your flow screens. Each Section component lets you organize
record fields and screen components in up to four adjustable-width columns.

These considerations don’t apply to the Section component in flow screens.

Granularity

The layout setting is applied at the flow level. So you can’t control the layout at the screen or field
level. If you set a flow to use two columns, every screen in that flow displays in two columns.

Order of Fields

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can’t manually control which fields go in which columns. If the flow is set to display two columns, the fields alternate in each column.
The odd fields (first, third, fifth, and so on) are placed in the left column. The even fields (second, fourth, sixth, and so on) are placed in
the right column.

If your users navigate screens with the Tab key, they tab through all the fields in the left column and then all the fields in the right column.
You can’t configure the fields to tab left-to-right.

Responsiveness

The flow layout isn’t responsive to the user’s screen dimensions. It uses the same layout whether the user’s screen is 1 inch wide or 20
inches wide.

Tip: If users run a flow from a phone or small tablet, don’t apply a two-column layout to the flow.

Compatibility with Section component

For flows that are distributed via Experience Builder, the Lightning App Builder, or the utility bar, each flow screen that contains a Section
component ignores the Layout property.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

For flows that are distributed via URL, each flow screen that contains a Section component ignores the `flowLayout` URL parameter.

SEE ALSO:

Flow Limits and Considerations

Flow Screen Output Component: Section

Customize a Flow URL to Render Two-Column Screens

Schedule-Triggered Flow Considerations

A schedule-triggered flow starts at the specified time and frequency for a batch of records.
Understand the considerations and special behaviors of schedule-triggered flows, also known as
scheduled flows.

These considerations apply to schedule-triggered flows.

**•** A schedule-triggered flow starts at the specified time and frequency. You can’t launch a
schedule-triggered flow by any other means.

**•** The Start Time field value is based on the Salesforce org’s default time zone.

**•** The View All Data permission is required to activate an autolaunched flow that has a trigger.

**•** The maximum number of schedule-triggered flow interviews per 24 hours is 250,000, or the
number of user licenses in your org multiplied by 200, whichever is greater. One interview is
created for each record retrieved by the schedule-triggered flow’s query.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you specify an object so that the flow runs for a batch of records, then set the time, frequency, and record conditions to avoid
reaching this limit. The maximum limit of records per batch is 200. You can use debug logs to check how many records a
schedule-triggered flow runs on. Track the number of records with the SCHEDULED_FLOW_DETAIL event. If your org reaches the
limit, Salesforce sends a flow error email.

**•** If you delete a schedule-triggered flow from the Scheduled Jobs page in Setup, all future recurrences of that flow are canceled. To
enable future runs, deactivate and reactivate the flow.

**•** If a flow is scheduled to run one time with a date and time that already passed, the flow doesn’t run.

**•** The Default Workflow User runs schedule-triggered flows.

**•** If you need a schedule-triggered flow to invoke Apex code, don’t enable the Require User Access to Apex Classes Invoked by Flow
update. When that release update is activated, schedule-triggered flows fail when they invoke Apex.

**•** A schedule-triggered flow can make callouts only after executing a Wait element. For example, without a Wait element, the flow
can’t access external objects, execute Apex actions that make callouts, or execute actions that are generated from External Services
registrations.

Tip: You can insert a Wait element that pauses the flow for only a moment. Configure the resume event to pause until a
specified time, with a specific time as the time source. For the base time, specify the `$Flow.CurrentDateTime` global
variable. Then set the offset to 0 hours. At run time, a Wait element that’s set up this way typically pauses the flow for less than
a minute.

**•** If you configure an Update Records element to use the ID and all field values from the $Record global variable, enable `Filter`
`inaccessible fields from flow requests` in your org’s process automation settings. Otherwise, the flow fails
because the Update Records element tries to set the values for system fields and other read-only fields.

**•** Synchronous Apex transactions invoked by an asynchronous flow contribute to synchronous per-transaction Apex limits. Asynchronous
flows include scheduled flows and flows with scheduled or asynchronous paths.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**•** At run time, if a schedule-triggered flow has a Create Records, Delete Records, Get Records, or Update Records element that processes
multiple records and some records fail, all records are rolled back. The successful records are retried. If the flow has another Create
Records, Delete Records, Get Records, or Update Records element later in the flow that processes the same failed records, all changes
are rolled back and the flow transaction fails.

**•** The order of your filter conditions doesn’t matter. The SFDC Optimizer evaluates all filters to optimize performance.

SEE ALSO:

Schedule Triggers for Flows That Run for Batches of Records

Troubleshoot Flow Errors

Flow Operations and Read-Only Fields

Considerations for Troubleshooting Flows

Record-Triggered Flow Considerations

A record-triggered autolaunched flow makes additional updates to the triggering record before or
after it’s saved to the database. Understand the considerations and special behaviors of flows that
make before- and after-save updates.

General Considerations

These considerations apply to any record-triggered flows.

**•** Record-triggered flows run custom validation rules.

**•** You can’t reference a screen flow from an autolaunched flow.

**•** The `isChanged` operator isn’t supported on asynchronous paths.

**•** Due to their position in the order of execution, record-triggered flows can behave differently
from similar workflow rules.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Flows that run only when a record is updated to meet the condition requirements are triggered only if all the condition requirements
change from `false` to `true` . If all the condition requirements already evaluate to `true` and still evaluate to `true` after the
record is updated, the flow doesn’t run. Scheduled paths are scheduled only if the previous version of the record didn’t meet the
requirements, and the updated record does meet the requirements.

For example, a record-triggered flow that is set to trigger when a flow is created or updated has the condition Industry equals
Agriculture. The flow is set to run only when a record is updated to meet the condition requirements.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

In this example, a record-triggered flow that is set to trigger when a flow is created or updated has the conditions Industry equals
Agriculture OR Billing State equals CA. The flow is set to run only when a record is updated to meet the condition requirements.

Considerations for Fast Field Updates

These considerations apply to record-triggered flows that are optimized for fast field updates (before-save).

**•** The flow can’t perform actions other than updating the triggering record’s field values.

**•** The flow can’t update values in records that are related to the triggering record.

**•** Only these elements are supported: Assignment, Decision, Get Records, and Loop.

**•** The View All Data permission is required to activate an autolaunched flow that has a trigger.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Considerations for Debug Mode

**•** The `ISCLONE()` formula function always evaluates to `FALSE` when you’re in debug mode. For example, if a record-triggered
flow contains an `ISCLONE()` formula function in the entry criteria or in a Decision element, `ISCLONE()` evaluates to `FALSE`
even when you’re debugging with a cloned record.

SEE ALSO:

Record Triggers for Flows That Make Before-Save Updates

_Apex Developer Guide_ [: Triggers and Order of Execution](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

#### Flow Data Considerations

When designing flows, keep these data considerations in mind.

Limits

**•** Each flow interview that executes the flow element Get Records or Update Records enforces
the SOQL query limit for the maximum number of characters because the element uses a SOQL
query. For each element per flow interview, the SOQL query limit is 100,000 characters. For
example, a flow interview executes the Get Records element that uses the In operator on a
collection of account IDs. If the element contains a collection of account IDs that exceeds 4,700
IDs and specifies other criteria to exceed the 100,000 character limit, the flow interview can fail.

Permissions

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** For flows that interact with the Salesforce database, make sure that your users have permission to create, read, edit, and delete the
relevant records and fields. Otherwise, users receive an insufficient privileges error when they try to launch a flow. For example, a
flow looks up and updates a case record's status. The flow users must have Read and Edit permissions on the `Status` field of the
Case object.

Variables

**•** If you delete a record variable or record collection variable, variable assignments that use the deleted variable are set to `null` .

**•** When a process or flow launches another flow, that flow’s input variables can be assigned values during the launch. However, for a
text, picklist, or multi-select picklist variable that isn’t a collection, a value of `null` is converted to an empty string.

**•** Storing field values automatically in the Get Record element is available only for screen flows and autolaunched flows.

Date and Date/Time

**•** At run time, time zones for date/time values can differ from what you see in Flow Builder. During run time, date/time values reflect
the time zone settings of the user who’s running the flow.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

#### Flow Lightning Runtime Considerations

When running flows, keep these considerations in mind.

Note: In Lightning runtime, flow users always run the active flow version. Flow admins with
the Manage Flow permission run the latest flow, so they can test the latest flow version
without activating it for flow users. A flow admin also runs the latest flow version that is
referenced via a Subflow element.

Flow Interviews

A _flow interview_ is an instance of a flow, much like a record is an instance of an object. The flow
interview can do many things, including look up and manipulate Salesforce data. In an interview,
you can pass data into variables and other resources. The data can come from a variety of sources,
such as Salesforce records that the flow queries, information that a user enters in a screen input
field, or something that you manually enter.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Interviews don’t perform actions—such as sending emails or creating, editing, or deleting records—until the associated transaction is
complete. Transactions are complete when the interview either finishes or executes a Screen, Local Action, or Wait element. In addition
to data elements, the Post to Chatter, Submit for Approval, and Quick Actions core actions also create and update records.

When an interview is in flight, the data in the interview isn’t saved to the Salesforce database. If the flow executes an element that creates
or updates records, such as Update Records or Post to Chatter, only the information configured in that element is saved to the Salesforce
database.

When an interview executes a Wait element or a user pauses it, all the interview data is serialized and saved to the database as a Paused
Flow Interview record. When the interview resumes, the Paused Flow Interview record is deleted.

Limitations of Lightning Runtime for Flows

When Lightning runtime is enabled for your Salesforce org, flows in Lightning Experience don’t load in:

**•** Web tabs

**•** List buttons that are set to display an existing window with or without a sidebar

When Lightning runtime is enabled for your org, flows in Salesforce Classic don’t load in custom buttons or links that are set to display
in an existing window with or without a sidebar.

In number input fields, users can enter up to 17 digits, including digits before and after a decimal point.

At runtime, validation error messages persist on screen flow components even if a user corrects the errors. The user can complete the
flow interview despite the messages.

SEE ALSO:

Lightning Runtime vs. Classic Runtime for Flows

Flow Element: Subflow


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Flow Runtime Accessibility Considerations

We strive to make the run-time experience of screen flows follow the best practices in Section 508
of the Rehabilitation Act and the Web Content Accessibility Guidelines (WCAG) 2.0 Level AA. But
we have some exceptions.

If you use screen readers or other assistive technology while running screen flows, consider these
known issues.

**•** The title of the screen doesn’t change when you click Next or Previous, so it’s not always obvious
that you’ve switched to a different page.

**•** Flow screen components that don’t have defined labels can’t be read properly by assistive
technology.

**•** Unless you use the ARIA alert role or another method of identifying errors for assistive technology,
these types of custom error messages can’t be detected by assistive technology.

**–** Error messages that are text components with conditional visibility

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**–** Error messages that are displayed for components when the associated Validate Input formula expression evaluates to false

**•** Screen readers base pronunciation on their language setting. When that language setting differs from the flow’s language, screen
readers can’t correctly read the flow screens. This limitation affects flows run from:

**–** Run and Debug buttons in Flow Builder

**–** URLs

**–** Custom buttons and links

**–** Web tabs

**•** Error messages for some Salesforce-provided components aren’t associated with their corresponding input fields. This limitation
means that screen readers can’t read error messages associated with them. Affected Salesforce-provided components:

**–** Dependent Picklists

**–** Email

**–** Lookup

**–** Phone

**–** Toggle

**–** URL

**•** When a user doesn’t complete a required field in a Dependent Picklists component, the resulting error messages can’t be read by
screen readers or other assistive technology. Sometimes, one of the error messages is announced one time, but later attempts to
focus on the field don’t cause the error message to be announced again.

**•** When a user clicks Finish in the Resume window from the Paused Flow Interviews Lightning component on a desktop (LEX), focus
isn’t set to the Refresh icon button.

**•** When a flow screen is initially displayed, the focus is set to the first visible screen field. Exceptions:

**–** If the flow screen contains an error, the focus is set to the first field with an error.

**–** If the flow screen contains only Display Text components, the focus is set to the body of the flow.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**•** When screen components or their parts are rendered after the screen is initially displayed, they’re never focusable. For example, if
a component asynchronously fetches a list of tasks to display, the focus can’t be set to any of the tasks. If a screen component uses
conditional visibility and appears only after user input, the focus can’t be set to any part of the screen component.

SEE ALSO:

Flow Limits and Considerations

Flow Screen Input Component: Display Image

Flow Management Considerations

When managing flows, consider the administration and activation limits.

Viewing Flows

In Lightning Experience, the Flows page in Setup doesn’t display any flows if a user sets the Sharing
Settings of the All Flows list view to Only I can see this list view.

Activating Flows

When you activate a new version of a flow, the previously activated version (if one exists) is
automatically deactivated. Any running flow interview continues to run using the version with
which it was initiated.

Deleting Flows

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To delete an active flow version, first deactivate it. If a flow has paused interviews, it can’t be deleted until those interviews are finished
or deleted. You can delete flows that have never been activated at any time.

Flow Type

If a flow has versions with different types, the active (or latest) version determines the flow type.

Deploying Flows

In production orgs, you can enable the setting to deploy a new active version of a process or flow via change sets or Metadata API. The
setting doesn't appear in non-production orgs (such as scratch, sandbox, and developer orgs), because you can always deploy a new
active version.

SEE ALSO:

Deploy Processes and Flows as Active

Flow Limits and Considerations


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

#### Considerations for Packaging Flows

You can include a flow in a managed or unmanaged package. Before you create, update, or deploy
a package that contains a flow, understand the limitations and behaviors of packages.

Creating Packages

**•** If you want to deploy a flow with a change set, the change set must include all components
that the flow references.

**•** When you package a flow, all components and fields that the flow references must be available
in the same package or a dependent package.

**•** If these elements are used in a flow, the packageable components that they reference aren’t
included in the package automatically. To deploy the package successfully, manually add the
referenced components to the package.

**–** Post to Chatter

**–** Send Email

**–** Submit for Approval

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

For example, if you deploy a flow that posts to a particular Chatter group, manually add the referenced Chatter group to the package.

**•** If a flow references a Lightning component that depends on a CSP Trusted Site, the trusted site isn’t included in the package
automatically.

**•** When you upload a package or package version, the active flow version is included. If the flow doesn’t have an active version, the
latest version is packaged.

Updating Packages

**•** To update a managed package with a different flow version, activate that version and upload the package. Or, deactivate all versions
of the flow, make sure that the latest flow version is the one to distribute, and then upload the package. If you activate a flow version
by mistake and upload the package, that flow version is distributed to everyone.

**•** If you install a flow from an unlocked package with the same API name, the new flow overrides the existing flow in the target org.

**•** You can’t include flows in package patches.

Other Considerations

**•** Flow Builder displays Apex actions from managed packages only if the associated method is marked global.

**•** Flow Builder displays email alerts from managed packages only if the email alert isn’t protected.

**•** If you register your namespace after you reference a flow in a Visualforce page or Apex code, add the namespace to the flow name
before you install the package.

**•** If a flow is installed from a managed package, error emails for that flow’s interviews don’t include details about the individual flow
elements. The email is sent to either the user who installed the flow or the Apex exception email recipients.

**•** You can’t package flow triggers.

**•** In a packaging org, you can’t delete a flow after you upload it to a released or beta first generation managed package. You can delete
a flow version from a packaging org after you upload it to a released or beta first-generation managed package, if all these criteria
are met:

**–** Salesforce Customer Support activated the Managed Component Deletion permission.

**–** The flow version isn’t the most recently packaged version of the flow.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**–** The flow version isn’t active.

**–** The flow version is not the only version.

**•** Images in rich text for screens aren’t supported in packages.

#### Change Set Considerations for Flows

Before you use change sets to deploy a flow, understand the limits and behaviors that are related
to component dependencies, deployment, and flow triggers.

Creating Change Sets

**•** If you want to deploy a flow with a change set, the change set must include any component
the flow references.

**•** When you view the dependent components for the change set, the Component Dependencies
page lists the dependencies for _all_ versions of the flow. Add all interdependent components
for the relevant flow version to the outbound change set.

**•** If a flow element references these components, the Component Dependencies page doesn’t
display that component. To deploy the flow successfully, manually add those referenced
components to the change set.

**–** Post to Chatter

**–** Send Email

**–** Submit for Approval

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

For example, if you deploy a flow that includes a Submit for Approval element, manually add the referenced approval process.

**•** If a flow references a Lightning component that depends on a CSP Trusted Site, the trusted site isn’t included in the package or
change set.

Deploying Change Sets

**•** You can include only one version of a flow in a change set.

**•** An active flow in a change set is deployed to its destination as inactive. Manually activate the flow after deployment.

**•** If the flow has no active version when you upload the outbound change set, the latest inactive version is used.

**•** Deploying or redeploying a flow with a change set creates a version of the flow in the destination Salesforce org.

**•** In production orgs, you can enable the setting to deploy a new active version of a process or flow using change sets or Metadata
API. The setting doesn’t appear in non-production orgs (such as scratch, sandbox, and developer orgs), because you can always
deploy a new active version.

Flow Triggers

**•** Flow triggers aren’t available in change sets.

SEE ALSO:

Deploy Processes and Flows as Active


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

#### Considerations for Flows Installed from Packages

Keep these considerations in mind when you distribute, upgrade, or remove a flow that you installed
from a package.

**•** Flow Builder can’t open a flow that is installed from a managed package, unless the flow is a
template or overridable.

**•** If you install a managed package that contains multiple flow versions in a fresh destination org,
only the latest flow version is deployed.

**•** If you install a non-template flow from a managed package, error emails for that flow’s interviews
don’t include any details about the individual flow elements. The email is sent to either the user
who installed the flow or the Apex exception email recipients.

**•** If you install a flow from an unmanaged package that has the same name but a different version
number as a flow in your org, the newly installed flow becomes the latest version of the existing
flow. However, if the packaged flow has the same name and version number as a flow already
in your org, the package install fails. You can’t overwrite a flow.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If you install a flow from an unlocked package that has the same name as a flow in your org, the newly installed flow overrides the
existing flow.

Status

An active flow in a package is active after it’s installed. The previous active version of the flow in the destination org is deactivated in
favor of the newly installed version. Any in-progress flows based on the now-deactivated version continue to run without interruption
but reflect the previous version of the flow.

Distributing Installed Flows

**•** When you create a custom button, link, or web tab for a flow that’s installed from a managed package, include the namespace in
the URL. The URL format is `/flow/namespace/flowuniquename` .

**•** When you embed a flow that’s installed from a managed package in a Visualforce page, set the name attribute to this format:
`namespace.flowuniquename` .

Upgrading Installed Flows

Upgrading a managed package in your org installs a new flow version only if there’s a newer flow version from the developer. After
several upgrades, you can end up with multiple flow versions.

Removing Installed Flows

**•** You can’t delete a flow from an installed package. To remove a packaged flow from your org, deactivate it and then uninstall the
package.

**•** In a packaging org, you can’t delete a flow after you upload it to a released or beta first generation managed package. You can delete
a flow version from a packaging org after you upload it to a released or beta first-generation managed package, if all these criteria
are met:

**–** Salesforce Customer Support activated the Managed Component Deletion permission.

**–** The flow version isn’t the most recently packaged version of the flow.

**–** The flow version isn’t active.

**–** The flow version is not the only version.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

**•** If you have multiple versions of a flow installed from multiple unmanaged packages, you can’t remove only one version by uninstalling
its package. Uninstalling a package—managed or unmanaged—that contains a single version of the flow removes the entire flow,
including all versions.

**•** Delete flows from an unlocked package manually—you can’t delete them by removing them from the unlocked package.

Translating Installed Flows

You can translate flow definition names only on the Translate page.

SEE ALSO:

[Use Managed Packages to Develop Your AppExchange Solution](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/managed_packaging_intro.htm)

Select Flow and Process Error Email Recipients

Considerations for Packaging Flows

_Salesforce DX Developer Guide_ [Components Available in Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/packaging_packageable_components.htm)

_[First-Generation Managed Packaging Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_install.htm)_ Install a Managed Package

Select Flow and Process Error Email Recipients

#### Considerations for Troubleshooting Flows

Keep these considerations in mind when reviewing a flow error email or using the debug option
in Flow Builder.

Be careful when debugging flows that contain delete elements. Even if the flow is inactive, it triggers
the delete operation.

Debugging a Flow

**•** If you debug a flow without choosing to run the flow in rollback mode, the flow performs its
actions, including any DML operations and Apex code execution. Remember, closing or restarting
a running flow doesn’t roll back its previously executed actions, callouts, and changes committed
to the database.

**•** You can’t pass values into input variables of type collection, record, and record collection.

**•** Clicking **Pause** or executing a Wait element closes the flow and ends debugging.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** When you debug a flow as another user, the flow’s record changes and actions are performed as that user. Also, the user’s profile
and permission sets determine the object permissions and field-level access of the flow. However, flows that always run in system
context ignore the user’s object permissions and field-level access.

**•** When you click **Finish** in a flow, the debug details incorrectly state “Selected Navigation Button: NEXT.”

**•** When you debug a schedule-triggered flow, the flow starts only for one record.

**•** When you debug a record-triggered flow, only what’s within the flow is tested. This smaller scope can lead to scenarios where the
flow executes as intended while debugging, but not at run time. This behavior difference can be due to other triggered flows and
processes. To see how a record-triggered flow behaves in a real-world scenario, make sure to test it in a sandbox org.

Tracking More Information About a Flow Interview

**•** To store more information about an interview when it’s saved as a Salesforce record, build a custom object that references the
interview’s GUID. An interview is assigned an 18-character Salesforce ID only when it’s paused and saved as a Salesforce record. Each
interview, whether in-flight or paused, has a GUID.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Troubleshooting Stages

The flow error email doesn’t specify the values of `$Flow.ActiveStages` and `$Flow.CurrentStage` at the start of an
interview. To confirm what the initial values are, add temporary elements to display the initial values, such as with a text field.

Considerations for Flow Error Emails

Review these considerations for the email sent to the admin or Apex exception email recipients
regarding flow interview errors and Screen and Subflow elements.

General

**•** If the user who started the flow doesn’t have a first name, `null` replaces the user's first name
in the How the Interview Started section.

**•** Variable assignments display in this pattern: `{!variable} (prior value) =`
`field/variable (new value)` . If the variable had no prior value, the parentheses
display as empty. For example: `{!varStatus} () = Status (Delivered)`

**•** If you install a non-template flow from a managed package, error emails for that flow’s interviews
don’t include any details about the individual flow elements. The email is sent to either the user
who installed the flow or the Apex exception email recipients.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Failed flow interviews for these flow types that are built with the free-form layout in Flow Builder are saved and available to open in
Flow Builder.

**–** Screen flows

**–** Record-triggered flows

**–** Schedule-triggered flows

**–** Autolaunched flows that aren’t triggered

**•** Failed flow interviews aren’t saved if:

**–** The flow is installed as part of a managed package and isn’t a template.

**–** The failure occurs after the flow interview is paused and then resumed at least one time.

**–** The error is handled because the element that encounters the error is connected to a fault connector.

**–** The failure occurs during an Apex test method.

**–** The flow is a standard flow.

**–** The value of the flow’s metadata field `status` is `Draft` or `InvalidDraft` .

**–** The failed flow interview exceeds 1 MB.

**–** The failed flow interviews already saved in the database exceeds 1 GB.

**•** Failed flow interviews don’t count toward data, file, or paused flow interview storage limits. When failed flow interviews are saved,
they’re available for up to 14 days and then automatically deleted from the database.

**•** These limits apply when failed flow interviews are saved.

**–** For any specific flow, no more than 100 failed flow interviews are saved in a 24-hour period.

**–** For a batch of up to 200 failed flow interviews in the same transaction, one interview is saved.

**–** Across all the flows in an organization, no more than 3,000 failed flow interviews are saved in a 24-hour period.

**–** Failed flow interviews exceeding 1 MB aren’t saved.

**–** Failed flow interviews aren’t saved if more than 1 GB of failed flow interviews are already saved in the database.


Automate Your Business Processes with Salesforce Flow Flow Limits and Considerations

Screen elements

Password fields display in plain text

Subflow elements

**•** The merge field annotation ( `{!variable}` as opposed to just `variable` ) is missing for variables in a referenced flow. For
example, when an interview enters a subflow and gives details about the inputs, the subflow's variable is `subVariable` instead
of `{!subVariable}` .

**•** If the error occurs in a referenced flow, the email is sent to the author of the parent flow, but the subject references the name of the
referenced flow.

**•** If you see multiple Entered flow _`ReferencedFlowName`_ version _`ReferencedFlowVersion`_ messages with no Exited
_`ReferencedFlowName`_ version _`ReferencedFlowVersion`_ messages in between them, the flow user navigated backwards.
To prevent this scenario, adjust the navigation options in the first screen of the referenced flow so that the user can’t click **Previous** .

SEE ALSO:

Troubleshoot Flow Errors

Select Flow and Process Error Email Recipients

#### Run-Time Changes by Release and API Version

These versioned updates affect only flows that are configured to run on specific API versions. With versioned updates you can test and
adopt run-time behavior changes for individual flows at your convenience.

[Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)

Available in: **Essentials**, **Professional**, **Enterprise**, **Performance**, **Unlimited**, and **Developer** Editions

To change the run-time API version of a flow, open it in Flow Builder and edit the flow version properties.

##### Winter ’25 (API Version 62.0)

These updates affect only flows that are configured to run on API version 62.0 and later.

Summer ’24 (API Version 61.0)
These updates affect only flows that are configured to run on API version 61.0 and later.

##### Winter ’25 (API Version 62.0)

These updates affect only flows that are configured to run on API version 62.0 and later.

[Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)

Available in: **Essentials**, **Professional**, **Enterprise**, **Performance**, **Unlimited**, and **Developer** Editions

Enforce Sharing Rules when Apex Launches a Flow

This versioned update enforces sharing rules when an Apex class that’s declared using the with sharing keyword launches an autolaunched
flow that runs in the default context. To enforce sharing, the Apex class must be declared using the with sharing keyword.


Automate Your Business Processes with Salesforce Flow Flow Reference

Previously, the flow ran in system context without sharing even when an Apex class was declared using the with sharing keyword
launched the flow.

With this versioned update, the flow runs more securely in the default context when an Apex class that’s declared using the with sharing
keyword launches an autolaunched flow. The flow enforces the sharing rules of the user that executes the Apex class. Previously, when
sharing rules weren’t enforced, the flow was able to access all data.

This versioned update restricts data access for autolaunched flows that are run in the default context and launched by an Apex class.
The Apex class must be declared using the with sharing keyword. Data access is restricted to the sharing rules of the user that executed
the Apex class.

For example, a query can return fewer rows than it did in system context without sharing. An operation can fail because the user doesn’t
have the correct permissions.

Set Screen Action Outputs to Null Correctly

In API version 62.0 and later, this versioned update makes sure that if a flow run by a screen action has an output that isn’t set by using
an Assignment element, its outputs are set to null, as expected. Screen components using that output are now updated automatically.

Set Conditionally Hidden Screen Component Outputs to Null Correctly

In API version 62.0 and later, this versioned update makes sure that if a conditionally hidden screen component has a collection as an
output, its outputs are set to null, as expected.

##### Summer ’24 (API Version 61.0)

These updates affect only flows that are configured to run on API version 61.0 and later.

[Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)

Available in: **Essentials**, **Professional**, **Enterprise**, **Performance**, **Unlimited**, and **Developer** Editions

Evaluate Null Text Values

With this versioned update, a null text value evaluates to null in a flow. Previously, a null text value evaluated to an empty string value.
For example, an empty picklist value evaluates to a null text value when the flow runs on API version 61.0 and later.

Flow Reference

Bookmark this page for quick access to information about flow elements, resources, events, and
more.

Flow Resources
Each _resource_ represents a value that you can reference throughout the flow.

Flow Elements
An element represents an action that the flow can execute. Examples include reading or writing
Salesforce data, displaying information and collecting data from flow users, executing business
logic, or manipulating data.


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

Provided Flow Core Actions
Perform an action outside of the flow. Choose from Salesforce-provided actions, like Submit for Approval or Send Email, or from your
org’s quick actions and local actions. To add one of these actions to your flow, add an Action element. Then, in the Action field,
search for the appropriate action.

Standard Flow Screen Components
Salesforce provides several standard screen components that extend the types of input fields available in screens.

Flow Connectors
A connector determines the path that a flow takes at run time.

Flow Operators
Operators behave differently, depending on what you’re configuring. In Assignment elements, operators let you change resource
values. In conditions and filters, operators let you evaluate information and narrow the scope of a flow operation.

Flow Version Properties
A flow version’s properties consist of its label, description, interview label, and type. These properties drive the field values that appear
on the flow’s detail page.

Flow Resources

Each _resource_ represents a value that you can reference throughout the flow.

In Flow Builder, the Manager panel displays the resources that are available in the flow.

You can create some resources by clicking **New Resource** . Some resources, such as global constants
and global variables, are provided by the system. Other resources are automatically created when
you add an element to a flow. For example, when you add a Decision element, a resource for each
decision outcome is automatically created.

**Flow** **Description** **Creatable from**
#### **Resource the Resources Tab**

Actions Output values that are stored automatically from Action
elements.

Choice Create a choice option to use in a screen component, such as
a Radio Buttons or Multi-Select Picklist component.

Collection Generate a set of choices by using an existing collection of
Choice records.
Set

Constant Store a fixed value that you can use throughout a flow.

Decision When you add a Decision element to a flow, its outcomes are
Outcome available as Boolean resources. If an outcome path has already

been executed in the flow interview, the resource's value is
`True` .

_`Element`_ Any element that you add to a flow is available as a resource
with the `was visited` operator in decision outcome

criteria. An element is considered visited when it’s executed
in the flow interview.


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

**Flow** **Description** **Creatable from the**
**Resource** **Resources Tab**

Any element that you add to a flow that supports a fault connector is available as a
Boolean resource. If the element is already successfully executed in the flow interview,
the resource's value is `True` . If the element wasn’t executed or was executed and
resulted in an error, the resource's value is `False` .

Formula Calculate a value when the formula is used in the flow.

Global Fixed, system-provided values, such as `EmptyString`, `True`, and `False` .
Constant

Global Variable System-provided variables that reference information about the Salesforce org or
running user, such as the user’s ID or the API session ID.

Wait
Configuration

When you add a Wait element to a flow, its configurations are available as Boolean
resources. If a configuration’s wait conditions are met, the resource’s value is `True` .
If the configuration has no wait conditions set, the resource’s value is always `True` .

Picklist Choice Generate a set of choices by using the values of a picklist or multi-select picklist field.
Set

Picklist Values System-provided values for picklist fields in record variables and record collection
variables. Available only for Assignment elements and conditions.

Record Choice Generate a set of choices by using a filtered list of records.
Set

Screen Any screen component that you add to a flow is available as a resource. The resource
Component value depends on the type of screen component. The value for a Text component is

what the user enters. The value for a Picklist component is the stored value of the
choice that the user selects. The value for a Display Text component is the text that’s
displayed to the user.

Stage Represent the user’s progress throughout the flow. To identify which stages are
relevant to the user throughout the flow, assign the stages to the stage system

variables. You can reference stages in flow logic or in the UI, such as with a progress
indicator. For example, in a payment flow, the stages are payment details, shipping
details, billing details, and order confirmation.

Text Template Store text that can be changed and used throughout the flow. To format the text, use
HTML tags.

Variable Store a value that can be changed throughout the flow.

SEE ALSO:

Flow Builder Tour


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Resource: Choice

Create a choice option to use in a screen component, such as a Radio Buttons or Multi-Select Picklist
component.

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
API Name

```

An API name can include underscores and alphanumeric characters without
spaces. It must begin with a letter and can’t end with an underscore. It also
can’t have two consecutive underscores.

`Description` Helps you differentiate this choice from other resources.

##### Choice Label A user-friendly label for the choice.

```
Data Type

##### `Choice Value`

```

Controls which screen components this choice can be used in. For example,
you can’t use a Text choice in a Currency radio button. You can’t change the
data type of a previously saved choice.

If the user selects this choice, the screen component is set to this value.

Exceptions:

**•** If no choice value is configured, the screen component is set to the
choice label.

**•** If the choice value references a formula resource, the screen component
is set to the choice label.

`Display text` Displays a text input component below the choice. This option isn't available
`input` if the choice's data type is `Boolean` .

Configure Text Input

These fields appear when you select `Display text input` .

**Field** **Description**

`Input` A user-friendly label for the text input component.

```
Label

```

`Require` Requires the user to enter a value in the text input component before progressing or finishing the flow.

`Validate` Evaluates whether the user entered an acceptable value.

`Error` If the user didn’t enter an acceptable value, this message displays under the text input component. Available only
`Message` when `Validate` is selected.

`Formula` Boolean formula expression that evaluates whether the user entered an acceptable value. Available only when
`Validate` is selected.

Example: To let users choose a particular service level, create choices for Gold, Silver, and Bronze. In a screen, display the choices
with a description of the features included. Then, in the same screen, let the user choose from a Radio Buttons screen component.


Automate Your Business Processes with Salesforce Flow Flow Reference

Formatting Choices

**•** Add rich text formatting using the toolbar.

**•** If you open the Display Text screen component, Choice resource labels, help text, Pause confirmation screens, or input validation,
Flow Builder converts existing HTML to rich text. Unsupported HTML is removed. The following HTML tags are converted to rich text:
<a>, <b>, <br>, <font>, <i>, <li>, <p>, <span>, <u>, and <div>. HTML that is pasted into the rich text editor isn't supported.

SEE ALSO:

Flow Resources

Standard Flow Screen Components

Using Choice Resources with Flow Screen Components

Flow Resource: Collection Choice Set

Use an existing collection of records or external data to generate a set of choices.

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
API Name

```

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate this resource from other resources.

```
Record

##### `Collection`

```

The collection you want to use to generate the choices. You can reference
an Apex-defined collection from an external service, Apex action, or
another screen component.

Configure Each Choice

For each record that meets the filter conditions, the flow creates a choice using values from the record. Identify which fields to use for
each choice’s label and value.

**Field** **Description**

```
Choice Label

```

Determines which field to use as the label for each generated choice. Select a field that enables users
to differentiate between the generated choices.

Make sure to choose a field that contains data. If the selected field has no value for a given record, the
corresponding choice’s label is blank at run time.

`Data Type` Data type of the choice’s value. You can’t change the data type of a previously saved collection choice
set.

```
Choice Value

```

Determines which field’s value to store when the user selects this choice at run time. The value is
determined by the most recent user selection of a choice within the generated set.

`Data Type` determines the available options. If you don’t select a field as the choice value, the
choice label is used instead.


Automate Your Business Processes with Salesforce Flow Flow Reference

Tip: In most cases, set the choice label to _`Name`_ and the choice value to _`ID`_ .

Example: Collection choice sets are useful when a flow reuses the same dataset over multiple screens. For example, you’re
designing a support flow for a company’s IT department that handles support requests related to employee hardware. The flow
references the same employee hardware data over several screens. To get the employee hardware information, use a Get Records
action, which populates a record collection. To define the conditions relevant to the support request, use a collection filter on the
record collection. Next, to display the user choices, add a collection choice set that uses the filtered collection. Create a relevant
collection filter and collection choice set for each branch of the support flow.

With collection choice sets, the server is queried only when the Get Records element is first executed. In comparison, record choice
sets require a server query with each use.

SEE ALSO:

Standard Flow Screen Components

Using Choice Resources with Flow Screen Components

Flow Resources

Flow Resource: Constant

Store a fixed value that can be used but not changed throughout a flow.

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
API Name

```

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate the constant from other resources.

`Data Type` Determines the type of value that the constant can store. You can’t change
the data type of a previously saved constant.

`Value` The constant’s value. This value doesn’t change throughout the flow.

SEE ALSO:

Flow Resources


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Resource: Formula

Calculate a value when the formula is used in the flow.

**Field** **Description**

```
API Name

```

The requirement for uniqueness applies only to elements within
the current flow. Two elements can have the same API name,
provided they're used in different flows. An API name can include
underscores and alphanumeric characters without spaces. It must
begin with a letter and can’t end with an underscore. It also can’t
have two consecutive underscores.

`Description` Helps you differentiate this formula from other resources.

`Data Type` The data type for the value returned by the formula. You can’t
change the data type of a previously saved variable.

```
Decimal Places

##### `Formula`

```

SEE ALSO:

Controls the number of digits to the right of the decimal point up
to 17 places. If you leave this field blank or set it to zero, only whole
numbers appear when your flow runs.

Available only when the data type is Number or Currency.

The formula expression that the flow evaluates at run time. The
returned value must be compatible with `Data Type` .

Some formula functions aren’t supported in Flow Builder.

##### Formula Operators and Functions by Context

Which Functions Aren’t Supported in Flow Formulas?

Flow Resources

Creating Flow Formulas with Flow Formula Builder

Flow Resource: Global Variables

A system-provided variable holds information that can be referenced throughout the flow. For
example, it can contain information about the Salesforce org, flow, running user, or triggering
record.

Example: Use `{!$User.Id}` to access the ID of the user who’s running the flow interview.


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


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference

Global Variable Considerations for Flows

###### • $Flow is the only global variable available in screen component visibility conditions.

**•** In a record-triggered flow, the `$Record` global variable doesn’t contain the triggering record’s values for fields whose values are
derived from other records. Examples of derived fields include `Contact.Name` and `User.MediumPhotoUrl` .

**•** Multi-select picklist, time, and location global variables are available only in formulas.

**•** If a field in the database has no value, the corresponding merge field returns a blank value. For example, if no value is set for your
org’s Country field, `{!$Organization.Country}` returns no value.

**•** `$Label` global variables take longer to load in the flow resource selection list. When selecting a `$Label` global variable, if the
`$Label` option isn’t visible in the flow resource selection list, close the window and try again in a few minutes.

SEE ALSO:

Flow Operations and Read-Only Fields

Salesforce Data Considerations for Flows

###### Flow Resource: $Flow Global Variables

###### A $Flow global variable provides information about the running interview. Some variables contain

system-provided values. You can update the other variables throughout the flow by using
Assignments or by storing output values in the variables.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**Global Variable**

**Supported** **Description** **Value Set By**
**Resource**
**Types**

###### $Flow.ActiveStages Stage $Flow.CurrentDate Text, Date, and

Date/Time

A collection of stages that are Assignment
relevant to the current path of the
flow.

For example, each item in a
progress indicator corresponds to

a stage in
###### $Flow.ActiveStages .

Date when the flow interview System
executes the element that
references the global variable.

###### $Flow.CurrentRecord Text ID of a related record. The value Assignment

must be a single ID for a valid


Automate Your Business Processes with Salesforce Flow Flow Reference

**Global Variable** **Supported** **Description** **Value Set By**
**Resource Types**

object. All custom objects and most standard
objects are valid.

When a user pauses the flow interview or the
interview executes a Wait element, the interview
is associated with this record by creating a
FlowRecordRelation record. If the ID isn’t valid,
the interview fails to pause.

`$Flow.CurrentStage` Stage

The currently selected stage. Assignment

For example, the selected item in a progress
indicator corresponds to
`$Flow.CurrentStage` .

`$Flow.CurrentDateTime` Text, Date, and Date and time when the flow interview executes System
Date/Time the element that references the global variable.

`$Flow.FaultMessage` Text System fault message that can help flow System
administrators troubleshoot runtime issues.

`$Flow.InterviewGuid` Text Unique identifier for the interview. System

`$Flow.InterviewStartTime` Text, Date, and Date and time when the flow interview started. System
Date/Time For a flow launched by a Subflow element,

`$Flow.InterviewStartTime` indicates
when the initial master flow started.

Example: A flow is used internally by call center personnel. For each flow element that interacts with the Salesforce database, a
fault connector leads to a screen. A Display Text screen component displays the system fault message and instructs the flow user
to provide that message to the IT department.

```
  Sorry, but you can't

       read or update records at this time.

  Please open a case with IT, and include the following error message:

  {!$Flow.FaultMessage}

```

Example: If a customer asks to be forgotten, make sure to delete all references to information that could personally identify the
customer, including data in paused flow interviews. When an interview executes a Wait element or is paused by a user, all the
interview data is serialized and saved to the database as a Paused Flow Interview record. When the interview is resumed, the
Paused Flow Interview record is deleted.

To identify which paused interviews include personal data for a contact, lead, or user, build a custom object to track the interview’s
GUID and the affected contact, lead, or user. When an interview references personal data, such as a lead’s email or credit card
number, create a record of the custom object using the lead’s ID and `{!$Flow.InterviewGuid}` . Before the final screen,
delete all records of the custom object referencing the interview’s GUID. That way, the custom object tracks only interviews that
are saved to the database.


Automate Your Business Processes with Salesforce Flow Flow Reference

When a customer asks to be forgotten, create a report that lists all the custom object records where LeadId matches the customer’s
record. Then for each custom object record, delete the flow interview that corresponds to the provided GUID.

SEE ALSO:

Customize What Happens When a Flow Fails

Flow Resources

Flow Resource: Global Constant

Fixed, system-provided values.

Example: When you create a Boolean variable, the supported values are
`$GlobalConstant.True` and `$GlobalConstant.False` .

Null Versus Empty String

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

At run time, `{!$GlobalConstant.EmptyString}` and `null` are treated as separate, distinct values.

**•** `{!$GlobalConstant.EmptyString}` indicates a text value with zero characters. It’s used to determine whether a field or
variable is blank.

**•** `null` indicates that a value doesn’t exist. It’s used to determine whether a field or variable value is available.

**•** To check if a field or variable has been populated with data in a condition, use **Equals** for the operator, and
**{!$GlobalConstant.EmptyString}** for the value.

**•** To check if a field or variable value isn’t available, in a condition, use **Is Null** for the operator and **{!$GlobalConstant.True}** for the
value.

Example: To check if a Get Records element found records, in a Decision element outcome condition, use the Get Records record
collection for the resource, **Is Null** for the operator, and **{!$GlobalConstant.False}** for the value.

Considerations

**•** If you don’t give a text field or variable a starting value, the value is `null` at run time. If you want the value to be treated as an
empty string, set it to `{!$GlobalConstant.EmptyString}` .

**•** For a text field or component placed on a Screen element, the Is Null operator always evaluates to false. To determine if the field or
component has no value, use **Equals** for the operator and **{!$GlobalConstant.EmptyString}** for the value.

**•** If a condition compares two text variables, make sure that their default values are either set to
`{!$GlobalConstant.EmptyString}` or left empty ( `null` ).


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** To check for both a `null` or `{!$GlobalConstant.EmptyString}` value at the same time, use the ISBLANK formula
function.

SEE ALSO:

Flow Resources

Flow Resource: Picklist Choice Set

Generate a set of choices by using the values of a picklist or multi-select picklist field.

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
API Name

```

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate this resource from other resources.

`Object` The object whose fields you want to select from. You can’t change the
object for a previously saved picklist choice set.

```
Data Type

```

Determines whether you can choose from picklist fields or multi-select
picklist fields. You can’t change the data type of a previously saved picklist
choice set.

`Field` The picklist or multi-select picklist field to use to generate the list of
choices.

`Sort Order` Controls the order that the choices appear in. The choices sort based on
the translated picklist value for the running user’s language.

Example: In a flow that simplifies the process of creating an account, users identify the company’s industry.

Rather than creating one choice for each industry, you add a picklist choice set to the flow and populate a Picklist screen component
with it. When a user runs the flow, the picklist choice set finds all the values in the database for the Industry field (1) on the Account
object (2).


Automate Your Business Processes with Salesforce Flow Flow Reference

In addition to being easier than the standalone choice resource to configure, a picklist choice set reduces maintenance. When
someone adds options to the Account Industry field, the flow automatically reflects the changes. You don’t have to manually
update the flow.

Considerations

You can’t do the following when using a picklist choice set.

**•** Filter out values that come back from the database. The flow always displays every picklist value for the field, even if you’re using
record types to narrow down the picklist choices in page layouts.

**•** Customize the label for each option. The flow always displays the label for each picklist value.

**•** Customize the stored value for each option. The flow always stores the API value for each picklist value.

Picklists for Knowledge Articles aren’t supported.

Labels and Values for Translated Fields

When a picklist field has been translated:

**•** Each choice’s label uses the version of the picklist value in the running user’s language.

**•** Each choice’s stored value uses the version of the picklist value in the org’s default language.

SEE ALSO:

Standard Flow Screen Components

Using Choice Resources with Flow Screen Components

Flow Resources

Place Record Fields Directly on Flow Screens


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Resource: Record Choice Set

Generate a set of choices by using a filtered list of records.

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
API Name

```

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate this resource from other resources.

`Object` The object whose records you want to use to generate the choices. You
can’t change the object for a previously saved record choice set.

Filter _`Object`_ Records

Determines which records are included in the choice set. For example, to generate a list of all accounts in San Francisco, use filters to
include only accounts whose Billing City is San Francisco.

Tip: Without filter conditions, a choice is generated for every record of the selected object. If you don’t apply filter conditions,
make sure to sort the records in ascending or descending order.

Sort _`Object`_ Records

Determines how to sort the filtered list of records and how many records to include in the choice set.

**Field** **Description**

`Sort Order` Controls the order that the choices appear in.

`Sort By` When the sort order is ascending or descending, select the field to order the choices by.

`Maximum Number of` The maximum number of choices to display for the screen component that uses this record choice
`Choices` set. By default, the maximum is 200.

Configure Each Choice

For each record that meets the filter conditions, the flow creates a choice using values from the record. Identify which fields to use for
each choice’s label and value.

**Field** **Description**

```
Choice Label

```

Determines which field to use as the label for each generated choice. Select a field that enables users
to differentiate between the generated choices.

Make sure to choose a field that contains data. If the selected field has no value for a given record, the
corresponding choice’s label is blank at run time.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

`Data Type` Data type of the choice’s value. You can’t change the data type of a previously saved record choice
set.

```
Choice Value

```

Determines which field’s value to store when the user selects this choice at run time. The value is
determined by the most recent user selection of a choice within the generated set.

`Data Type` determines the available options. If you don’t select a field as the choice value, the
choice label is used instead.

Store More _`Object`_ Field Values

When a choice is selected, store field values from the associated record in flow variables that you can reference later.

Note: When a Checkbox Group, Multi-Select Picklist, or Choice Lookup screen component uses a record choice set, only values
from the last record that the user selects are stored in the flow variables. If multiple Checkbox Group or Multi-Select Picklist
components on one screen use the same record choice set, the variable assignments come from the last record selected from all
of those components.

Example: In a support flow for a computer hardware manufacturer, users identify a product to find its latest updates. You create
a record choice set that displays all products whose product ID starts with a specific string of characters. However, the flow users
are more likely to know the product’s name than its ID. So for `Choice Label`, select the field that contains the product name,
and for `Choice Value`, select the ID field. Elsewhere in the flow, you want to display the associated description. To do so, you
store the Description field value from the user-selected record in a variable.

SEE ALSO:

Flow Operators in Data Elements and Record Choice Sets

Standard Flow Screen Components

Using Choice Resources with Flow Screen Components

Flow Resources

Flow Resource: Stage

Represent the user’s progress throughout the flow. To identify which stages are relevant to the user
throughout the flow, assign the stages to the stage system variables. You can reference stages in
flow logic or in the UI, such as with a progress indicator. For example, in a payment flow, the stages
are payment details, shipping details, billing details, and order confirmation.

**Field** **Description**

`Label` A user-friendly label for the stage. Merge fields aren’t supported.

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

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and

can’t end with an underscore. It also can’t have two consecutive
underscores.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

`Description` Helps you differentiate this stage from other resources.

`Order` Required. Determines how to sort this stage among the other stages in the flow. The order must be
unique among all other stages in the flow.

`Active by default` Adds this stage to `{!$Flow.ActiveStages}` when an interview starts.

Usage

When ordering your stages, leave gaps between the numbers in case you later want to add a stage between two other stages. For
example, if you use 10, 20, and 30 as the order, you can insert a stage at order 15 without updating the original three stages.

Most of the time, stages resolve to the fully qualified name: `namespace.flowName:stageName` or `flowName:stageName` .
Stages resolve to the label in:

**•** Display contexts, such as choice labels and Display Text screen components

**•** Attributes in screen components that require Lightning runtime

SEE ALSO:

Plan the Stages in Your Flow

Identify the Relevant Stages in Your Flow

Flow Stage Considerations

Flow Resources

Sample Flows That Display Stages

These Online Purchase flows display stages as sections on a progress indicator. Each sample flow displays stages differently based on
how the flow is configured.

Sample Flow That Displays Stages as Breadcrumbs
This Online Purchase flow shows visitors what parts of the flow they’ve completed by displaying all stages up to the current stage.
This flow displays only the stages that the user has visited.

Sample Flow That Displays All the Active Stages
This Online Purchase flow shows visitors all active stages and the current stage so that they know what to expect throughout this
flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

Sample Flow That Displays Stages as Breadcrumbs

This Online Purchase flow shows visitors what parts of the flow they’ve completed by displaying
all stages up to the current stage. This flow displays only the stages that the user has visited.

**Example**

This flow includes stages for users to review their cart, enter shipping details, enter billing details,
enter payment details, and confirm their order. Since we’re displaying the stages as breadcrumbs,
only the first stage is active by default.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When the flow starts, Review Cart is automatically set to `$Flow.CurrentStage` and is the only stage in `$Flow.ActiveStages` .

Each time the flow moves to a different stage, an Assignment element resets the current stage and adds the new stage to the active
stages.

Note: This sample uses an Aura component to display the flow’s stages. For details, see Represent Your Flow’s Stages Visually.


Automate Your Business Processes with Salesforce Flow Flow Reference

The first screen displays only one active stage, which is also the user’s current stage: Review Cart.

Next, the flow moves to a new stage: Shipping Details. To make sure that the active stages and current stage respect the change, the
flow updates the global variables with an assignment.

`$Flow.ActiveStages` now contains the Review Cart and Shipping Details stages, and `$Flow.CurrentStage` is set to the
Shipping Details stage.

Often, a user’s shipping details and billing details are the same. On the Shipping Details screen, the user can indicate that the billing
address is different.

The flow uses the value of the Different Billing Address checkbox to determine where to go next. If the shipping and billing details are
the same, the flow continues to the Payment Details assignment. If the billing and shipping details are different, the flow moves to the
Billing Details assignment.

To make sure that the active stages and current stage respect the change, the flow updates the global variables with an assignment.

Now `$Flow.ActiveStages` contains the Review Cart, Shipping Details, and Billing Details stages, and `$Flow.CurrentStage`
is set to the Billing Details stage.


Automate Your Business Processes with Salesforce Flow Flow Reference

After the shipping and billing details are complete, the flow moves to the Payment Details stage. To make sure that the active stages
and current stage respect that change, the flow updates the global variables with an assignment.

`$Flow.ActiveStages` contains the Review Cart, Shipping Details, Billing Details (if the billing and shipping details are different),
and Payment Details stages. The `$Flow.CurrentStage` global variable is set to the Payment Details stage.

Finally, the flow moves to the last stage: Order Confirmation. To make sure that the active stages and current stage respect the change,
the flow updates the global variables with an assignment.

`$Flow.ActiveStages` now contains the Review Cart, Shipping Details, Billing Details (if the billing and shipping details are different),
Payment Details, and Order Confirmation stages. The `$Flow.CurrentStage` global variable is set to the Order Confirmation stage.


Automate Your Business Processes with Salesforce Flow Flow Reference

Sample Flow That Displays All the Active Stages

This Online Purchase flow shows visitors all active stages and the current stage so that they know
what to expect throughout this flow.

**Example**

This flow includes stages for users to review their cart, enter shipping details, enter billing details,
enter payment details, and confirm their order. To give users an idea of the steps they go through
in the flow, we’re displaying all the applicable stages when the flow starts. Every user goes through
the Review Cart, Shipping Details, Payment Details, and Order Confirmation stages, so those stages
are all active by default.

Not all users enter billing details, because a user's shipping and billing details can be the same. To
insert an optional stage in the flow's active stages, create another flow and reference it by using a
####### Subflow element

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When the flow starts, Review Cart is automatically set to `$Flow.CurrentStage`, and `$Flow.ActiveStages` contains Review
Cart, Shipping Details, Payment Details, and Order Confirmation.

Each time the flow moves to a different stage, an Assignment element resets the current stage.


Automate Your Business Processes with Salesforce Flow Flow Reference

Note: This sample uses an Aura component to display the flow’s stages. For details, see Represent Your Flow’s Stages Visually.

The first screen displays all active stages and the user’s current stage: Review Cart.

Next, the flow moves to a new stage: Shipping Details. To make sure that the current stage respects the change, the flow updates the
global variable with an assignment. `$Flow.CurrentStage` is set to the Shipping Details stage.

Often, a user’s shipping details and billing details are the same. On the Shipping Details screen, the user can indicate that the billing
address is different.


Automate Your Business Processes with Salesforce Flow Flow Reference

The flow uses the value of the Different Billing Address checkbox to determine where to go next. If the shipping and billing details are
the same, the flow continues to the Payment Details assignment. If the billing and shipping details are different, the flow uses a Subflow
element to reference the Billing Details flow.

The Billing Details flow includes an optional stage for users to enter billing details between shipping and payment details.

When a referenced flow starts, its default active stages are automatically inserted in `$Flow.ActiveStages` after the current stage.

When the Billing Details flow starts, `$Flow.CurrentStage` is Shipping Details. The Billing Details stage is inserted into
`$Flow.ActiveStages` immediately after the current stage. Now `$Flow.ActiveStages` contains the Review Cart, Shipping
Details, Billing Details, Payment Details, and Order Confirmation stages.

The flow uses an assignment to set the current stage to Billing Details.

The `$Flow.CurrentStage` global variable is set to the Billing Details stage.

After the shipping and billing details are complete, the flow moves to the Payment Details stage. To make sure that the current stage
respects that change, the flow updates the system variable with an assignment.

The `$Flow.CurrentStage` global variable is set to the Payment Details stage.


Automate Your Business Processes with Salesforce Flow Flow Reference

Finally, the flow moves to the last stage: Order Confirmation. To make sure that the current stage respects the change, the flow updates
the global variable with an assignment.

`$Flow.ActiveStages` now contains the Review Cart, Shipping Details, Billing Details (if the billing and shipping details are different),
Payment Details, and Order Confirmation stages. The `$Flow.CurrentStage` global variable is set to the Order Confirmation stage.

Flow Resource: Text Template

Store text that can be changed and used throughout the flow.

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
API Name

```

The requirement for uniqueness applies only to elements within the current
flow. Two elements can have the same API name, provided they're used
in different flows.An API name can include underscores and alphanumeric
characters without spaces. It must begin with a letter and can’t end with
an underscore. It also can’t have two consecutive underscores.

`Description` Helps you differentiate this text template from other resources.

##### Text Template The text for the template. To reference information from other resources,

use merge fields.

Rich Text

Plain Text

Control the font, size, color, and alignment of text. Add merge fields, HTML
links, bullet points, or numbered lists. Rich text is on by default. Click

to change to Rich Text.

Send email core actions use plain text. Some custom actions from
AppExchange or built by Salesforce developers also expect plain text. Click

to change to Plain Text.


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: You’re designing a flow that registers people for an event. You create a text template that includes a registrant's name,
address, and other information. Then you use the template in an email confirmation that the flow sends when it finishes.

SEE ALSO:

Flow Resources

Flow Resource: Variable

Store a value that can be used or changed throughout the flow.

**Field** **Description**

`Apex Class` The Apex class that defines fields for the Apex-defined data type. Only
fields with the @AuraEnabled annotation are available in a flow.

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

The requirement for uniqueness applies only to elements within the
current flow. Two elements can have the same API name, provided they're
used in different flows. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

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
`(collection)` that are compatible with its data type. When the data type is Record, the
collection variable can only store values for the associated object’s records.

For example, store multiple email addresses in a collection variable, and
reference the collection variable to send an email.

```
Object

Decimal Places

Availability

Outside the

Flow

```

The object whose field values you can store in the variable. You can’t
change the object of a previously saved variable.

Available only when the data type is Record.

Controls the number of digits to the right of the decimal point up to 17
places. If you leave this field blank or set it to zero, only whole numbers
appear when your flow runs.

Available only when the data type is Number or Currency.

When a variable is available for input, it can be set at the start of the flow,
such as when a flow is started from a Lightning page, a process, or another


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

flow. When a variable is available for output, it can be accessed throughout the flow, such as by a
Lightning web component or another flow.

The default value of the field depends on the release or API version in which the variable is created.

**•** If the variable was created in Summer ’12 or later, or in API version 25.0 or later, by default the
variable isn’t available for input or output.

**•** If the variable was created in Spring ’12 or earlier, or in API version 24.0 or earlier, by default the
variable is available for both input and output.

Disabling input or output access for an existing variable can break the functionality of applications
and pages that call the flow and access the variable. For example, you can access variables from URL
parameters, processes, and other flows.

This field doesn’t affect how variables are assigned or used within the same flow, for example, through
these types of elements: Assignment, Create Records, Get Records, and Apex Action.

```
Default Value

```

SEE ALSO:

Determines the variable value when the flow starts. If you leave this field blank, the value is `null` .

Not available for Picklist and Multi-Select Picklist variables.

Sample Flow That Loops Through a Collection

Flow Element: Loop

Flow Operators in Assignment Elements

Flow Resources

Flow Variable Considerations

Flow Element: Transform

Add Values to a Collection Variable

After you create a collection variable, populate it with values to reference throughout your flow.
You can’t use a Get Records element to populate a collection variable, but there are some
workarounds.

To use values from outside the flow, make sure that the collection variable is available for input.
When the values come from outside the flow, the values can be set only when the flow interview
starts.

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

Sample Flow That Populates a Collection Variable

Populate a collection variable by populating a record collection variable. Then individually assign
the record collection variable’s values to the collection variable.

In this scenario, you’re designing a flow to send an email to every employee who lives in San
Francisco.

The Send Email core action lets you easily send emails from a flow. However, the Recipients parameter
only accepts text variables and text collection variables. Since multiple users live in San Francisco,
use a collection variable (rather than entering the email address for each individual user).

You can't use a Get Records element to populate collection variables. First populate a User-based
record collection variable with field values, including `Email`, from the employees who live in San
Francisco. Then add those emails to the collection variable.

After the collection variable is populated, use the collection variable as the value for the Send Email
element’s `Email Addresses (collection)` parameter.

This flow already contains these resources.

**•** A User-based record collection variable called `employeesInSF`

**•** A User-based record variable called `loopVariable`

**•** A Text-based collection variable called `emails_employeesInSF`


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

The example flow:

**1.** Finds all user records whose `City` is "San Francisco" and populates `employeesInSF` with those records’ `Email` .

**2.** Loops through the record collection variable so that it can look at each individual user record. The loop copies the values of each
item in `employeesInSF` to `loopVariable` .

**3.** For each iteration, assigns the user's `Email` to a collection variable that has a Data Type of Text.

**4.** When the loop ends, the flow sends an email to the users whose emails are now stored in `emails_employeesInSF` .

SEE ALSO:

Add Values to a Collection Variable


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Elements

An element represents an action that the flow can execute. Examples include reading or writing
Salesforce data, displaying information and collecting data from flow users, executing business
logic, or manipulating data.

Flow Builder gives you the option of building flows in free-form or in auto-layout. In free-form, the
#### Elements tab shows the types of elements that you can add to the flow by dragging them onto

the canvas. In auto-layout, click to display the types of elements that you can add. For a list of
all elements already added to the flow, see the Elements section of the Manager tab.

Flow Elements: Action
Launch an action that's available in Salesforce by adding an Action element to your flow.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow Element: Add Prompt Instructions
Provide data in the form of prompt instructions that are merged into a prompt template in Prompt Builder. This element is available
only in template-triggered prompt flows.

Flow Element: Apex Action
Call an Apex class. Apex classes are available as Apex actions only if one of the methods is annotated with `@InvocableMethod` .

Flow Element: Apex Action (Legacy)
Call an Apex class that uses a legacy Apex interface. Apex classes are available as legacy Apex actions only if the `Process.Plugin`
interface has been implemented.

Flow Element: Assignment
Set values in variables, including collection variables, record variables, record collection variables, and global variables.

Flow Element: Collection Filter
Apply criteria to a collection, and then output a new collection that contains only the items that meet the criteria.

Flow Element: Collection Sort
Reorder the items within a collection and optionally limit the number of items that remain in the collection after the sort.

Flow Element: Create Records
Create or update multiple Salesforce records by using a record collection variable. Create or update exactly one Salesforce record
by using a record variable or other values from the flow.

Flow Element: Custom Error
Create targeted error messages in record-triggered flows to display in a window on the overall record page or as an inline error on
a specific field for your users. The change that triggered the flow is rolled back until the error is fixed.

Flow Element: Get Records
Find Salesforce records that meet filter conditions, and store values from the records in variables.

Flow Element: Decision
Evaluate a set of conditions, and route users through the flow based on the outcomes of those conditions. This element performs
the equivalent of an if-then statement.

Flow Element: Delete Records
Identify Salesforce records to delete by using the IDs stored in a record variable or record collection variable, or by specifying conditions.

Flow Element: Email Alert
Send an email using an Email Alert action where you specify an email template and a static list of recipients. You add an Action
element to your flow and search for the name of your already configured Email Alert action.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Loop
Start a loop path for iterating over items in a collection variable. For each iteration, the flow temporarily stores the item in the loop
variable. To execute actions on each item’s field values, use other elements in the loop.

Flow Elements: Wait
Resume a flow interview after specific conditions are met, a specified amount of time passes, or until a specific date.

Flow Element: Recommendation Assignment
Generate Einstein Next Best Action recommendations by combining data from records in the recommendation object, records in
other objects, values in collections, and manually entered values.

Flow Element: Screen
Collect information from or display information to a user who runs the flow.

Flow Element: Start
Connect the Start element to the flow element that you want to execute first at run time. In an autolaunched flow, you can open
the Start element to add a trigger that launches the flow. Without a trigger, you must set up other things to invoke the autolaunched
flow, such as custom buttons, processes, Apex classes, or Einstein Bots.

Flow Element: Subflow
Launch another active flow that’s available in your org. A flow launched by another flow is called the _referenced flow_ .

Flow Element: Transform
Select the flow resources for mapping and transforming source data to target data. You can use the Transform element in screen
flows, autolaunched flows with no triggers, and record-triggered flows.

Flow Element: Update Records
Identify Salesforce records to update, and set the values to change in those records. To do so, use the IDs and field values stored in
a record variable or record collection variable, or use specify conditions to identify the records and set the field values individually.

Flow Builder Elements for Marketing Cloud
A Flow Builder element represents an action that a flow can execute. Examples include decisions based on criteria and creating and
deleting Salesforce data. Some Flow Builder elements are available only in Marketing Cloud, such as Send Email Message and Send
SMS Message.

SEE ALSO:

Flow Resources

Flow Builder Tour

Add and Edit Elements

Flow Elements: Action

Launch an action that's available in Salesforce by adding an Action element to your flow.

Usage

Add an Action element on page 74 to your flow. Then, in the Action field, search for and select the
action you want to perform or filter by category or type of action. Flow Builder displays descriptions
for action inputs and outputs. See Provided Flow Core Actions on page 382. If something goes
wrong, go back to select a different action.


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

Set Input Values for the Selected Action

To set the input values for the referenced action, use values from earlier in the flow. Assign values for all required inputs. To assign values
to optional inputs, select **Include** or **Include with Specified Value** for the toggle associated with the input.

Store Output Values

To use the referenced action's outputs, either use automatic output or assign manual variables. You can’t store output values using both
automatic output and manually assigned variables.

To use automatic output to reference the action's outputs later in the flow, select the desired output from the resource: Outputs from
_`ElementName`_ .

To manually assign the referenced action's outputs to variables, expand **Advanced**, and assign variables to the needed outputs. To
return the referenced action's outputs from a flow, manually assign variables defined with **Available for output** selected.

SEE ALSO:

Flow Elements

Add and Edit Elements

Provided Flow Core Actions

_Trailhead_ [: Data and Actions in Flows](https://trailhead.salesforce.com/content/learn/modules/data-and-actions-in-flows)

Flow Element: Add Prompt Instructions

Provide data in the form of prompt instructions that are merged into a prompt template in Prompt
Builder. This element is available only in template-triggered prompt flows.

Template-triggered prompt flows aren’t compatible with prompt templates created in Winter ’24.

EDITIONS

Available in: Lightning
Experience

Available in: **Unlimited+**
Edition

Available for an additional
cost in: **Enterprise** and
**Unlimited** Editions with the
Einstein for Sales, Einstein for
Platform, or Einstein for
Service add-on.

Example: The first Add Prompt Instructions element adds the text _`Hello!`_ . The next Add Prompt instructions element appends
the {!contact} record variable resource. When the flow finishes, the $Output global variable contains the text, _`Hello! Mary`_,
where _`Mary`_ is the value that {!contact} references. The same text is merged into the associated prompt template in Prompt
Builder.

Handle Missing Data in Prompt Instructions

Consider logic or actions that return no data in prompt instructions. Consider these options:

**•** Incorporate an alternative or default value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Add instructions that don’t use the data.

**•** Clear the prompt instructions, so nothing is passed outside the flow.

**•** Include prompt instructions that address the missing data.

For example, your prompt instructions depend on accounts that meet filter criteria, but the flow finds no accounts. We recommend
using logic to handle the missing data. The Decision element can check for data, and the Add Prompt Instructions element can send
contextual instructions that no data is available.

Get Record IDs

When you insert a resource that references the Get Records element in the Add Prompt Instructions element, the $Output global variable
stores only the record IDs. For example, the Get Records element retrieves a collection of accounts. Its flow resource {!Get_Accounts} is
inserted into the Add Prompt Instructions. The $Output global variable stores only the account IDs.

SEE ALSO:

Template-Triggered Prompt Flows

Flow Element: Apex Action

Call an Apex class. Apex classes are available as Apex actions only if one of the methods is annotated
with `@InvocableMethod` .

Add an Action element to the flow. Filter the list of actions by type rather than category. If your
##### canvas is in free-form layout, select Apex . If your canvas is in auto-layout, select Apex Action . Select

the action that you want to configure. For details about creating Apex actions, see
“ `InvocableMethod` [Annotation” in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

Set Input Values

When you set the inputs for the Apex action, use values from earlier in the flow.

Apex actions don’t support lookup fields in record variables as input values.

Store Output Values

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To reference output values that are stored automatically, specify the API name of the Action element. To store the action’s output values
manually, select **Manually assign variables (advanced)** . The values are assigned when the code is executed.

Usage

If a flow invokes Apex, the running user must have the corresponding Apex class assignment in their profile or permission set.

If the invoked method creates, updates, or deletes a record, that action isn’t performed until the interview’s transaction completes.
Transactions are complete when the interview either finishes or executes a Screen, Local Action, or Wait element.

Flow Builder doesn’t display descriptions for input and output values. For details about each parameter, ask the Apex developer for more
information.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Builder displays Apex actions from managed packages only if the associated method is marked global.

SEE ALSO:

Add and Edit Elements

Let Flows Execute Apex Actions

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Element: Apex Action (Legacy)

Call an Apex class that uses a legacy Apex interface. Apex classes are available as legacy Apex actions
only if the `Process.Plugin` interface has been implemented.

Add an Action element to your flow. Filter the list of actions by type rather than by category. Select
##### Apex Action (Legacy), and then select the action that you want to configure.

Tip: If your developer hasn’t already implemented the `Process.Plugin` interface on
the desired class, we recommend using the `@InvocableMethod` annotation instead.
Unlike the `Process.Plugin` interface, the `@InvocableMethod` annotation supports
sObject, Collection, Blob, and Time data types and bulkification. It’s also easier to implement.
To compare the interface and the annotation, see Let Flows Execute Apex Actions on page
171.

Set Input Values

When you set the inputs for the Apex action, use values from earlier in the flow.

Store Output Values

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To use the legacy Apex action’s outputs later in the flow, store them in variables. The values are assigned when the code is executed.

Usage & Limitations

If the Apex class creates, updates, or deletes a record, the action isn’t performed until the interview’s transaction is completed. Transactions
are complete when the interview either finishes or executes a Screen, Local Action, or Wait element.

Flow Builder doesn’t display descriptions for input and output values. For details about each parameter, ask the Apex developer for more
information.

Legacy Apex actions aren’t organized by the tag in the plug-in code.

Cloud Flow Designer lets you save an Apex Plug-in element without setting values for its required input parameters. If you open the
corresponding legacy Apex action in Flow Builder, you can’t save changes to the element unless you set values for the required input
parameters.


Automate Your Business Processes with Salesforce Flow Flow Reference

Important: Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be
added in free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

SEE ALSO:

Add and Edit Elements

Let Flows Execute Apex Actions

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_namespace_process.htm)_ : Process Namespace

Flow Element: Assignment

Set values in variables, including collection variables, record variables, record collection variables,
and global variables.

Usage

To update the value of a variable, add an Assignment element to your flow. Specify the API name
of a variable, an operator, and the value to use.

To update the value of more than one variable in an Assignment element, click Add Assignment.
For each row, specify the variable, the operator, and the value to assign. At run time, variable
assignments are made consecutively in the order they're listed in the element.

**Field** **Description**

`Variable` The API name of the variable you want to assign a value to. Select an
existing variable, or create one.

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
Operator

Value

```

The operation to perform for the assignment. The available operators
depend on the data type of the specified `Variable` . See Flow Operators
in Assignment Elements

The value to use in the assignment or the API name of a resource that
contains the value to use in the assignment. `Variable` and `Value`
in the same row must have compatible data types.

Example: **Update a Record Variable and Add It to a Record Collection**

To set the field values for a record variable and then add the record variable to a record collection, use an Assignment element on
a Loop element's For Each path. To create all the records at the same time, use the record collection variable with a Create Records
element outside of the loop.

This example updates the Account ID, Amount, Description, and Stage fields of the NewOpportunity record variable and then
adds the record variable to the NewOpportunities record collection variable.

This example contains five variables:

**•** NewOpportunity: **Data Type** is _`Record`_ and **Object** is _`Opportunity`_ .

**•** AccountId: **Data Type** is _`Text`_ .

**•** OpportunityAmount: **Data Type** is _`Currency`_ .


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** OpportunityDescription: **Data Type** is _`Text`_ .

**•** NewOpportunites: **Data Type** is _`Record`_ and **Object** is _`Opportunity`_ . **Allows multiple values** is selected.

The Assignment element in this example has five rows:

**•** The first row sets the record variable's account ID to a variable value:

**–** **Variable** is _`NewOpportunity > Account ID`_

**–** **Operator** is _`Equals`_

**–** **Value** is _`AccountId`_

**•** The second row sets the record variable's amount to a variable value:

**–** **Variable** is _`NewOpportunity > Amount`_

**–** **Operator** is _`Equals`_

**–** **Value** is _`OpportunityAmount`_

**•** The third row sets the record variable's description to a variable value:

**–** **Variable** is _`NewOpportunity > Description`_

**–** **Operator** is _`Equals`_

**–** **Value** is _`OpportunityDescription`_

**•** The fourth row sets the record variable's stage to a literal value from the picklist associated with the Stage field:

**–** **Variable** is _`NewOpportunity > Stage`_

**–** **Operator** is _`Equals`_

**–** **Value** is _`Proposal`_

**•** The fifth row adds the record variable to the record variable collection:

**–** **Variable** is _`NewOpportunities`_

**–** **Operator** is _`Add`_

**–** **Value** is _`NewOpportunity`_

**Here's an Assignment element that sets properties of an opportunity record variable and then adds the variable to an**
**opportunities record collection**


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: **Set the Value of an Error Message in a Fault Path**

To set a variable equal to a relevant error message, use an Assignment element on a Fault path. Next, use a Go To connector to
go to a Screen element that displays errors to the flow user. The Screen element uses the variable from the Assignment element
in a Display Text component.

This example sets the value of the ErrorMessage variable to a string that identifies the problem and what to do about it.

This example contains one variable: ErrorMessage where **Data Type** is _`Text`_ .

This example contains one row:

**•** **Variable** is _`ErrorMessage`_

**•** **Operator** is _`Equals`_

**•** **Value** is _`We couldn't find a record with the specified record ID. Check the record`_

```
       ID and try again.

```

**Here's an Assignment element that sets the value of a variable to a literal string**

SEE ALSO:

Flow Elements

Flow Operators in Assignment Elements

Flow Element: Create Records

Flow Element: Loop

Move and Connect Elements to Change a Flow Route

Flow Resources

Flow Element: Collection Filter

Apply criteria to a collection, and then output a new collection that contains only the items that
meet the criteria.

**Field** **Description**

##### Collection The collection variable that is filtered. This field accepts any collection variable

within the same flow.

`Condition` Determines the logic that evaluates conditions.

```
Requirements
```
**•** Choose `All Conditions Are Met` to include values that meet all
the specified criteria.


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

**•** Choose `Any Condition Is Met` to include values that meet any of the specified criteria.

**•** Choose `Custom Condition Logic Is Met` to include values that meet the logic entered in
`Condition Logic` .

**•** Choose `Formula Evaluates to True` to include values where `Formula` is true for that value.

`Condition` Only appears if `Condition Requirements` is set to `Custom Condition Logic Is Met` .
`Logic` Enter logic such as _`1 AND (2 OR 3)`_ .

```
Formula

```

Only appears if `Condition Requirements` is set to `Formula Evaluates to True` . Enter a
formula that can evaluate to TRUE or FALSE, such as _`{!currentItemFromSourceCollection.Id}`_
_`== {!varContactID}`_ .

`Field` The field evaluated by this condition. Doesn’t appear if `Condition Requirements` is set to `Formula`
`Evaluates to True` .

`Operator` The available operators depend on the data type of the selected `Field` .

```
Value

```

Usage

`Field` and `Value` in the same row must have compatible data types.

Options:

You can filter any collection found in Flow Builder, including collection variables that contain single values, collection variables that
contain records, and Apex-defined collection variables.

Collection Filter outputs a collection with the filtered results and doesn’t change the contents of the source collection. The output
collection is null until its corresponding Collection Filter runs.

Note: The output collection variable is named after the Collection Filter element's API name.

Example:

**•** For example, if a Collection Filter element is named _`FilterLeads`_, its output collection is called _`Leads from`_
_`FilterLeads`_ .

**•** The Collection Filter element also creates a single variable called _`CurrentItem_FilterLeads`_ . It acts as a loop variable
for the Collection Filter element's input collection.

**•** You can reference the single variable in a formula resource. For example, you can create a Filter element formula condition
where you set condition requirements to _`Formula Evaluate to True`_ : AND ({currentItem_FilterLeads.LastViewedDate}
< {!$Flow.CurrentDateTime,{!currentItem_FilterLeads.IsConverted})

If you filter your collection with a formula, the formula must evaluate to a boolean (true or false) value. For more formula considerations,
see Flow Formula Considerations in Salesforce Help.

If you delete a Collection Filter element, the _`CurrentItem_FilterLeads`_ variable remains in the flow. You can safely delete this
single record variable after you remove the collection filter element.

Considerations for Defining Filter Criteria

**•** When you define multiple filter criteria, the filter logic usually defaults to AND. But if multiple filters have the same field selected and
use the equals operator, the filters are combined with OR.


Automate Your Business Processes with Salesforce Flow Flow Reference

For example, your filters check whether a case Type equals Problem, Type equals Feature Request, and Escalated equals true. At run
time, the filters are combined to be `Type = (Problem OR Feature Request) AND Escalated = true` .

**•** The available filter operators depend on the data type of the selected fields. For details, see Flow Operators in Data Elements and
Record Choice Sets.

SEE ALSO:

Flow Formula Considerations

Flow Operators in Data Elements and Record Choice Sets

Creating Flow Formulas with Flow Formula Builder

Flow Element: Collection Sort

Reorder the items within a collection and optionally limit the number of items that remain in the
collection after the sort.

**Field** **Description**

##### Collection The collection variable that is sorted. This field accepts any collection variable

`Variable` within the same flow.

`Sort By` The field that the collection is sorted by. This field is only shown if the collection
variable contains more than one field.

`Sort Order` Sort the collection in ascending or descending order.

`Put empty` When selected, this element sorts records with an empty or null value in the
`string and` Sort By field at the start of the collection. Otherwise, they’re placed at the end.

```
null

values

first

```

`How Many` Select `Set the maximum number of items` to determine the
`Items to` number of items that remain in the collection after the sort.

```
Keep After

Sorting

```

Usage

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When the Collection Sort element removes values or changes their order, it makes those changes directly in the selected collection
variable.

If the collection variable contains more than one field, click `Add Sort Option` to sort by additional fields in order of greater to
lesser priority. You can sort by up to 3 fields at a time.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Create Records

Create or update multiple Salesforce records by using a record collection variable. Create or update
exactly one Salesforce record by using a record variable or other values from the flow.

Note: Looking for the Fast Create and Record Create elements from Cloud Flow Designer?
The Create Records element combines the functionality of both elements. For the equivalent
of the Record Create element, create one record and set the record fields using separate
variables, resources, and literal values. Choosing the other options is the equivalent of the
Fast Create element.

How many records you choose to create or update and how to set the field values determine what
to enter in the rest of the Create Records element.

To create a collection of records

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To create multiple records, you must use the values from a record collection variable. Earlier in the flow, populate the record collection
variable with the new records’ field values. Make sure the ID field is blank.

To dynamically create some records and update others in a collection, enable **Update Existing Records** . Choose a field on the records
in the record collection variable that uniquely identifies each record. The flow uses this field to check whether the records exist. Choose
how to process the remaining records if the flow fails to create or update a record.

When you use a record collection variable to create or update multiple records at once, you reduce the number of DML requests in your
flow. That means you’re more likely to stay within your org’s limits. For more information, see Flow Bulkification in Transactions.

To create a single record

If you’ve populated a record variable with the field values for the new record, choose to set the record fields by using all the values from
a record variable. Then select the record variable to use. Make sure the ID field is blank.

To dynamically create or update a record, enable **Update Existing Records** . Choose a field on the record in the record variable that
uniquely identifies the record. The flow uses this field to check whether the record exists.

To manually map values from various resources in the flow, choose to set the record fields by using separate variables, resources, and
literal values. Choose the object that you want to create a record for, and set the field values for the record. Optionally, store the ID of
the created record in a Text variable if you manually created the variable. For example, when you need the record’s ID to create child
records or to provide a link to the created record.

To dynamically check for a duplicate record to update or create, enable **Check for Matching Records** .

Example: A user enters a name and address into the flow. Verify that a matching user exists by using the Get Records element.
If a matching contact doesn’t exist, create a record for that user by using the Create Records element.

Usage

To prevent the flow from failing, make sure that:

**•** All required fields are populated with values. The Create Records element populates potentially required fields for you. The fields
shown are required in the master record type. For custom objects, confirm the required fields in the object definition.

**•** For record variables the ID field values are blank. The flow populates the ID fields after the record is created.

Note: The record isn’t created until the interview’s transaction is completed. Transactions are complete when the interview either
finishes or executes a Screen, Local Action, or Wait element.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

**•** If a Create Records element uses a record collection, doesn’t have a fault path, and the flow fails, no records are created, and the
flow stops, generating an error.

**•** If a Create Records element uses a record collection and has a fault path, only the successful records are created. The IDs of the
successful records aren’t populated for the records in the record collection in the flow. The IDs are populated on the records in the
org.

**•** The Create Records element can’t update matching records that are locked for editing. If Flow Builder finds a matching record and
attempts to update a field in the record, a warning appears.

**•** The Create Records element can’t update read-only fields in matching records. If Flow Builder finds a matching record and attempts
to update a field that's always read only or that you don’t have permission to update, a warning appears.

**•** The Create Records element can’t update fields in matching records for objects that don’t support the update function. If Flow Builder
finds a matching record and attempts to update a field in an object that doesn’t support the update function, an error appears, and
you can’t activate the flow. To determine whether an object can be updated, see _Object Reference for the Salesforce Platform_ .

SEE ALSO:

Flow Operators in Data Elements and Record Choice Sets

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Elements

Check for Duplicate Records

To prevent duplicate records, check for records that match a set of criteria and specify what happens
if the flow finds matching records. Some field-level configurations and validations in your org
override the settings in the Create Records element.

**1.** Enable **Check for Matching Records** .

**2.** In Condition Requirements, select an option.

**3.** Configure the first condition.

**4.** Add more conditions as needed.

**5.** In the If a single matching record exists area, select an option.

**Option** **Description**

**Update the matching record** Update the matching record with the values that you
specified in the Create Records element.

**Skip the matching record** Don’t create or update any records.

**6.** In the If multiple matching record exists area, select an option.

**Option** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**Update the most recently modified matching** Update the most recently modified matching record with the values that
**record** you specified in the Create Records element.

**Skip all matching records** Don’t create or update any records.

**7.** Save your work.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Custom Error

Create targeted error messages in record-triggered flows to display in a window on the overall
record page or as an inline error on a specific field for your users. The change that triggered the
flow is rolled back until the error is fixed.

You can create a custom error message only in the before-save or after-save path of a
record-triggered flow. You can’t run an error message asynchronously, and the error message can’t
be called from another flow type.

**FIELD** **DESCRIPTION**

`Label` Identifies the error message on the canvas.

`API Name` The API name must be unique within the current flow. Two elements can
have the same API name if they’re used in different flows. The name can

include underscores and alphanumeric characters without spaces. It must
begin with a letter and can’t end with an underscore. It also can’t have
two consecutive underscores.

`Description` Describes the error message.

EDITIONS

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Where to Show

the Error

Message

```

Select **In a window on a record page** to display the error message as
an overall message. Select **As an inline error on a field** to display the
error message on the field that is causing the error.

`Error Message` Enter text or select a resource to create an error message to display to the
user when there’s an error on a record change. The error message can

have up to 255 characters. You can use Translation Workbench to translate
your error messages.

Usage

Use the Custom Error element to roll back a change that triggered a flow and inform the user exactly what caused the error. The user
can fix the problem and try again. For example, when a user deletes a record that triggers a flow, the flow can return an error message
that tells the user why the deletion wasn’t allowed.

Considerations

**•** A Custom Error element can contain only one record page error message. To create another record page error message in the same
flow, use another Custom error element.

**•** A field can have only one error message, but each field can have an error message.

**•** Compound fields aren’t supported.

**•** If an executed fault path has a Custom Error element, the change that triggered the flow is rolled back.

**•** Custom error messages use the same functionality as the addError() Id method in Apex.

SEE ALSO:

_Salesforce Developers_ [: Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_id.htm?_ga=2.201080110.1837804536.1690896507-579833793.1688039438#apex_System_Id_addError)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Element: Get Records

Find Salesforce records that meet filter conditions, and store values from the records in variables.

Note: Looking for the Fast Lookup and Record Lookup elements from Cloud Flow Designer?
The Get Records element combines the functionality of both elements. For the equivalent of
the Record Lookup element, store only the first record in separate variables. Choosing the
other options is the equivalent of the Fast Lookup element.

Identify the object whose records you want to find, and specify conditions to narrow down the list
of returned records. How many records you choose to store and where to store the field values
determines what to enter in the rest of the Get Records element. When you add a Get Records
element to a screen flow or an autolaunched flow, we automatically store all the record values in
a flow variable. When the flow moves to the next element, the values are assigned to the variable.

To store record values manually in a screen flow or autolaunched flow, select **Choose fields and**
**assign variables (advanced)** .

To store field values manually for only the first record

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Tip: If you choose to store values from only the first record, filter by a unique field, such as ID. Otherwise, you can’t guarantee
which record’s field values are stored.

You can store field values from the first record together in a record variable or in separate variables.

To store the values together, select the record variable, and identify the fields whose values you want to store.

To store the values in separate variables, select each field you want to store, and select the variable to store each field value in.

To store field values manually for more than one record

To store field values for multiple records, you must store the values in a record collection variable.

When you use a record collection variable to create, update, or delete multiple records at once, you reduce the number of DML requests
in your flow. That means you’re more likely to stay within your org’s limits. For more information, see Flow Bulkification in Transactions.

Example:

**•** Find the product name or description for a product with a specific bar code.

**•** Confirm stock availability for a particular item.

**•** Verify a caller’s identity.

Considerations for Defining Filter Criteria

**•** When you define multiple filters, the filter logic usually defaults to AND. However, if multiple filters have the same field selected and
use the equals operator, the filters are combined with OR.

For example, your filters check whether a case’s Type equals Problem (1), Type equals Feature Request (2), and Escalated equals true
(3). At run time, the filters are combined to `(1 OR 2) AND 3` .

**•** The available filter operators depend on the data type of the selected fields. For details, see Flow Operators in Data Elements and
Record Choice Sets.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** To use a Data Cloud object as the data source, your org must include a data mapping for the object. Data mapping relates Data Lake
Object (DLO) fields to Data Model Object (DMO) fields. If your org doesn’t include a mapping, you can’t select a Data Cloud data
space or object in the Get Records element.

SEE ALSO:

Flow Operators in Data Elements and Record Choice Sets

Flow Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Flow Element: Decision

Evaluate a set of conditions, and route users through the flow based on the outcomes of those
conditions. This element performs the equivalent of an if-then statement.

Outcomes

For each path that the flow can take, create an outcome. For each outcome, specify the conditions
that must be met for the flow to take that path. To relabel the path that the flow takes if no outcome’s
conditions are met, click **Default Outcome** .

**Field** **Description**

`Label` Identifies the connector for this outcome on the canvas.

`Outcome` The requirement for uniqueness applies only to elements within the current
`API Name` flow. Two elements can have the same API name, provided they're used in
different flows. An API name can include underscores and alphanumeric
characters without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

`Condition` Determines whether the flow takes this outcome’s path. Sets logic and conditions
`Requirements` for each outcome that determine if the flow follows its path.

```
to Execute

Outcome

```

`When to` Available on record-triggered flows. Determines whether this outcome’s path
`Execute` is taken, based on whether the triggering record is updated to meet the
`Outcome` condition requirements. For example, the opportunity update that triggered
the flow to run changed its stage to Closed Won from any value that isn’t Closed
Won.

This option checks if the triggering record didn't previously meet the condition
requirements and if the $Record variable now meets the condition requirements.
If your flow changes any of the $Record variable’s fields before it runs the
configured Decision element, the Decision checks if the $Record’s new field
values now meet the condition requirements.


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

Example: Using a Decision element, determine whether to:

**•** Give customers a return shipping address or instructions on how to resolve the problem when an item is determined to be
faulty.

**•** Offer a customer a loan based on the results of a credit scoring formula.

**•** Inform sales leaders when an opportunity’s stage is changed to Closed Won.

Tip: Configure your flow so that it does different things based on what a user selects for a Picklist screen component. To do
so, add a decision after the screen to create the branches of the flow based on the choices available in the picklist. Then you
can represent each choice in your decision and connect it to a branch of your flow.

Usage

When a flow executes a Decision element, it evaluates each decision outcome in order. For the first outcome whose conditions are met,
the flow takes the associated path. If no outcome’s conditions are met, the flow takes the path for the default outcome.

SEE ALSO:

Flow Elements

Define Conditions in a Flow

Flow Operators in Decision, Wait, and Collection Filter Elements

Move and Connect Elements to Change a Flow Route

Flow Element: Delete Records

Identify Salesforce records to delete by using the IDs stored in a record variable or record collection
variable, or by specifying conditions.

Note: Looking for the Fast Delete and Record Delete elements from Cloud Flow Designer?
The Delete Records element combines the functionality of both elements.

**•** For the equivalent of the Fast Delete element, use the IDs from a record variable or record
collection variable.

**•** For the equivalent of the Record Delete element, specify the conditions to identify the
records to delete.

How you choose to identify the records to delete determines what to enter in the rest of the Delete
Records element.

**•** Use a record variable or record collection variable.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you store the IDs of the records to delete in a record variable or record collection variable, choose to use the IDs from a record
variable or record collection variable. Then select the variable to use.

Important: For the variable that you select, make sure that each record’s ID value is set. The flow identifies which records to
delete based on the ID value.

When you use a record collection variable to delete multiple records at once, you reduce the number of DML requests in your flow.
That means you’re more likely to stay within your org’s limits. For more information, see Flow Bulkification in Transactions.

**•** Specify conditions.

To use conditions to identify the records to delete, choose the object, and add at least one condition to filter down the list of records.


Automate Your Business Processes with Salesforce Flow Flow Reference

Example: When a customer accepts a quote, delete the remaining quotes from the opportunity.

Considerations for Defining Filter Criteria

**•** When you define multiple filters, the filter logic usually defaults to AND. However, if multiple filters have the same field selected and
use the equals operator, the filters are combined with OR.

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

