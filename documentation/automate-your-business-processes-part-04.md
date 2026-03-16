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

