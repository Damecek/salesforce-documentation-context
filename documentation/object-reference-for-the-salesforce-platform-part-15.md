Otherwise, they’re available in the specified API version and later.

**PublicComplaintFeed on page 55**
Feed tracking is available for the object.

**PublicComplaintHistory on page 63**
History is available for tracked fields of the object.

**PublicComplaintOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PublicComplaintShare on page 67**
Sharing is available for the object.

### PurchaseQuantityRule

Represents a rule that restricts the quantity of a product that can be purchased. The rule can be an increment, minimum, or maximum
rule. This object is available in API version 52.0 and later.


Standard Objects PurchaseQuantityRule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PurchaseQuantityRule object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Increment

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Quantity of product that can be added with each increase.

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


Standard Objects PurchaseQuantityRule

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

```
Maximum

Minimum

Name

OwnerId

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Maximum quantity that can be purchased.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Minimum quantity that can be purchased.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the purchase quantity rule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects PushTopic PushTopic

Represents a query that is the basis for notifying Streaming API clients of changes to records in an org. This object is available in API
version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** To receive notifications, users must have read access on both the object in the PushTopic query and the PushTopic itself.

Fields

**Field** **Details**

```
ApiVersion

Description

IsActive

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. API version to use for executing the query specified in `Query` . It must be an API
version greater than 20.0. If your query applies to a custom object from a package, this value
must match the package's `ApiVersion` .

Example value: 66.0

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the PushTopic. Limit: 400 characters

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the record currently counts towards the organization's allocation.


Standard Objects PushTopic

**Field** **Details**

```
Name

NotifyForFields

NotifyForOperationCreate

NotifyForOperationDelete

NotifyForOperationUndelete

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Descriptive name of the PushTopic, such as `MyNewCases` or
`TeamUpdatedContacts` . Limit: 25 characters. This value identifies the channel and
must be unique.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies which fields are evaluated to generate a notification.

Possible values are:

**•** `All`

**•** `Referenced` (default)

**•** `Select`

**•** `Where`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a create operation should generate a notification, otherwise, `false` . Defaults to
`true` . This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a delete operation should generate a notification, otherwise, `false` . Defaults to
`true` . Clients must connect using the `cometd/29.0` (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

**Type**
boolean


Standard Objects PushTopic

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
`true` if an undelete operation should generate a notification, otherwise, `false` . Defaults
to `true` . Clients must connect using the `cometd/29.0` (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

```
NotifyForOperationUpdate

NotifyForOperations

Query

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if an update operation should generate a notification, otherwise, `false` . Defaults
to `true` . This field is available in API version 29.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies which record events may generate a notification.

In API version 29.0 and later, this field is read-only, and doesn’t contain information about
delete and undelete events. Use `NotifyForOperationCreate`,
`NotifyForOperationDelete`, `NotifyForOperationUndelete` and
`NotifyForOperationUpdate` to specify which record events should generate a
notification.

Possible values are:

**•** `All` (default)

**•** `Create`

**•** `Extended`

**•** `Update`

A value of `Extended` means that neither create or update operations are set to generate
events.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The SOQL query statement that determines which record changes trigger events
to be sent to the channel.


### Standard Objects PushUpgradeCustomization

**Field** **Details**

Limit: 1,300 characters

Usage

The PushTopic defines when notifications are generated in the channel. Determine which fields to configure by checking out these links
in the _Streaming API Developer Guide_ .

**•** [PushTopic Queries](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/pushtopic_queries.htm)

**•** [Events](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/events.htm)

**•** [Notifications](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/notifications.htm)

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/intro_stream.htm)_

### PushUpgradeCustomization

Customized push upgrades allow a package subscriber to block push upgrades to their org. Package developers control which subscribers
can opt into customized push upgrades. Each push upgrade customization maps to a specific package and to a specific subscriber org.
This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomUpgradeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of push upgrade customization.

Possible values are:

**•** `BlockedBySubscriber` —Blocked By Subscriber

**•** `None`

The default value is `None` .


Standard Objects PushUpgradeCustomization

**Field** **Details**

```
ExpirationDays

HasRestrictionEnabled

IsCustomUpgradeAllowed

IsRestrictionOverridden

PushUpgradeBlockInitiatedDate

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days that a subscriber is allowed to block push upgrades.

Enter _`-1`_ to set customized push upgrades to never expire.

The default value is `null` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the subscriber org has blocked push upgrades.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the package developer has allowed a subscriber to opt into customized
push upgrades.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether customized push upgrades have been overridden by Salesforce Customer
Support for the subscriber org.

The default value is `false` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that `IsCustomUpgradeAllowed` was set to _`true`_ .


### Standard Objects QueuedExecutionEventLog QueuedExecutionEventLog

Queued Execution events contain details about queued executions—for example, batch Apex. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

DatabaseTotalTime

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

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
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DB_CPU_TIME. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
string


Standard Objects QueuedExecutionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

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
event in a given transaction has the same REQUEST_ID.

**Type**
string

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


Standard Objects QueuedExecutionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

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
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.


### Standard Objects QueueRoutingConfig

**Field** **Details**

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

### QueueRoutingConfig

Represents the settings that determine how work items are routed to agents. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
CapacityPercentage

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects QueueRoutingConfig

**Field** **Details**

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a specific type of
work item from this service channel.

Voice calls must have a capacity percentage of _`100`_ . If an agent receives a voice call, the
agent won’t receive new work items until the call ends, because at that point the agent’s
capacity will have reached 100%.

This field is available in API version 33.0 and later.

```
CapacityWeight

DeveloperName

DropAdditionalSkillsTimeout

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a work item from this
service channel.

For example, if an agent has a capacity of _`6`_, and cases are assigned a capacity weight of _`2`_,
an agent can be assigned up to 3 cases before the agent is at capacity and can’t receive new
work items. Voice calls must use the entire capacity weight.

This field is available in API version 33.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

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

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
int


Standard Objects QueueRoutingConfig

**Field** **Details**

**Properties**
Create, Filter, Group Nillable, Sort, Update

**Description**

The number of seconds to wait before a skill marked as **Additional Skill** is dropped from
Omni-Channel routing. The case is then routed to the best-matched agent even if they don’t
have all the skills.

```
IsAttributeBased

Language

MasterLabel

OverflowAssigneeId

PausedCapacityPercentage

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this routing is attribute-based. Available in API version 45.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the presence status.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user or queue that’s set as the Overflow Assignee.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects QueueRoutingConfig

**Field** **Details**

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a paused work
item from this service channel. The paused capacity feature is available with status-based
capacity and Enhanced Omni-Channel only.

```
PausedCapacityWeight

PushTimeout

RoutingModel

RoutingPriority

ServiceChannelId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a paused work item
from this service channel. The paused capacity feature is available with status-based capacity
and Enhanced Omni-Channel only.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds set for push timeout. **0** is returned when push timeout isn’t enabled.
Available in API version 36.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The routing type that determines how work items are routed (pushed) to agents. Possible
values are `Least Active` and `Most Available` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority in which work items from the service channels that are related to this routing
configuration are routed to agents. Work items from routing configurations that have lower
priority values (for example, _`0`_ ) are routed to agents first.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects Question

**Field** **Details**

**Description**
The ID of the service channel that’s associated with this configuration. This field is available
in API version 32.0 and earlier.

### Question

Represents a question in a zone that users can view and reply to.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available if the Answers permission and AnswersEnabled preference or PortalFeed permission and PortalFeedEnabled
preference are enabled in your org.

Fields

**Field** **Details**

```
BestReplyId

BestReplySelectedById

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the reply that has been identified as the best answer to the question. Use
the user interface to identify the best answer for a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who selected the best answer to the question.

This field is available in API version 24.0 and later. In API version 24.0 through version
29.0, you must update this field using the UI. In API version 30.0 and later, you can
update this field using the API.


Standard Objects Question

**Field** **Details**

```
Body

CommunityId

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the question.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the question. After you create a question, you can’t
change the zone ID associated with that question.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to
view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal
users (agents) appears to portal users in the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.


Standard Objects Question

**Field** **Details**

```
HasSingleFieldForContent

LastReferencedDate

LastReplyDate

LastReplyId

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the content of a Chatter Answers question is:

**•** Included in only one field: `Title` if the content is unformatted and less than
255 characters; or `Body` if the content is formatted or more than 255 characters
( `true` )

**•** Included in two fields: `Title` and `Body` ( `false` )

This field also determines if content displays in one or two fields in Chatter Answers
question feeds.

This field is available in API version 25.0 and later.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last reply (child Reply object) was posted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last reply (child Reply object) posted to the question.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


Standard Objects Question

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null,
this record might only have been referenced ( `LastReferencedDate` ) and not
viewed.

```
MostReportAbusesOnReply

NumReplies

NumReportAbuses

NumSubscriptions

Origin

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most number of user-reported abuses on a Reply associated with the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies (child Reply object) that users have submitted for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of user-reported abuses on the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of users following the question.

This field is available in API version 24.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects QuestionDataCategorySelection

**Field** **Details**

**Description**
The source of the question, such as `Chatter Answers` .

This field is available in API version 24.0 and later.

```
Title

UpVotes

VoteScore

```

Usage

Use this object to track questions in a zone.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The descriptive title of the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for the question.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the question, used to sort questions and articles on the Popular
tab in the application user interface. The internal algorithm that determines the score
gives older votes less weight than newer votes, simulating exponential decay. The
score itself doesn’t display in the application user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate
function with this field.

### QuestionDataCategorySelection

A data category selection represents a data category that classifies a question.

This object can be used to associate a question with a data category from a data category group or to query the categorization for a
question.


Standard Objects QuestionDataCategorySelection

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To create, read or update data category selection, you must have create, read or update permission on the categorized question. Users
who can update question can also delete its category selection. Users who can create questions can only select categories visible to
their role.

Fields

**Field Name** **Details**

```
DataCategoryGroupName

DataCategoryName

ParentId

```

Usage

**Type**
DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category group which has a category associated with
the question.

**Type**
DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category associated with the question.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the question associated with the data category selection.

Every question can be categorized in a data category. You can use the QuestionDataCategorySelection object to query and manage
question categorization. Client applications can create categorization for a question. They can also delete, query, and retrieve question
categorization.

Warning: Even though the API lets you select more than one category for QuestionDataCategorySelection, the Answers tab only
supports one data category selection for questions. Selecting multiple categories through QuestionDataCategorySelection may


### Standard Objects QuestionReportAbuse

result in unexpected behavior in the Answers tab, such as losing your multiple selections. You should only select one data category
when using QuestionDataCategorySelection.

Sample Code—Java

In the following example, the `selectCategory` method adds a category to a question data category selection. The
`retrieveCategorySelections` method returns all the categories from a question data category selection.

```
   public void selectCategory(ID parentId, String categoryGroupName, String categoryName) {

      try {

        QuestionDataCategorySelection categorySelection = new

   QuestionDataCategorySelection();

        categorySelection.setParentId(parentId);

        categorySelection.setDataCategoryGroupName(categoryGroupName);

        categorySelection.setDataCategoryName(categoryName);

        binding.create(new SObject[]{categorySelection});

      } catch (RemoteException e) {

        System.out.println("An unexpected error has occurred." + e.getMessage());

      }

   }

   public String[] retrieveCategorySelections(String parentId) {

      QueryResult qr = null;

      try {

        qr = binding.query("SELECT DataCategoryName FROM QuestionDataCategorySelection

   WHERE Id = '" + parentId + "'");

      } catch (RemoteException e) {

        System.out.println("An unexpected error has occurred." + e.getMessage());

      }

      String[] categoryNames = new String[qr.getRecords().length];

      for (int index = 0; index < qr.getRecords().length; index++) {

        categoryNames[index] =

   ((QuestionDataCategorySelection)qr.getRecords()[index]).getDataCategoryName();

      }

      return categoryNames;

   }

```

Salesforce Knowledge uses a similar object for article data category selection. See Article Type __DataCategorySelection
__DataCategorySelection for SOQL examples using this object.

SEE ALSO:

Article Type__DataCategorySelection

### QuestionReportAbuse

Represents a user-reported abuse on a Question in a Chatter Answers zone. This object is available in API version 24.0 and later.


### Standard Objects QuestionSubscription

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

QuestionId

Reason

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Question from which the user reported abuse.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Question from which the user reported abuse.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Question, such as `Spam`, `Hateful`, or
`Inappropriate` .

Use this object to track user-reported abuse on questions created in a Chatter Answers zone.

### QuestionSubscription

Represents a subscription for a user following a Question. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects QuestionSubscription

Fields

**Field** **Details**

```
CommunityId

Name

QuestionCreatedDate

QuestionId

SubscriberId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the zone associated with the Question the user is following. This field
can’t be updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the question subscription.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Required. Creation date of the Question which the user is following. This field can’t
be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Question which the user is following. This field can’t be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the User who is following the Question. This field can’t be updated.


### Standard Objects QueueSobject

Usage

Things to consider when following a Question:

**•** A user can only follow questions that they have permission to view.

**•** Administrators and users with the “Modify All Data” permission can configure other users to follow questions that the other user has
read access to.

**•** Administrators and users with the “Modify All Data” permission can configure users to stop following questions.

Queries on QuestionSubscription:

**•** Users with the “Read” permission on Question can see which questions other users are following.

**•** A query must include a LIMIT clause and the limit can’t exceed 1,000.

**•** A query using a `WHERE` clause can only filter by fields on Question.

### QueueSobject

Represents the mapping between a queue Group and the types associated with the queue, including custom objects.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

### A queue is a Group whose Type is Queue . To create a Group, you must have the Manage Users permission.

Fields

**Field** **Details**

```
QueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a queue.

This field is a relationship field.

**Relationship Name**
### Queue

**Relationship Type**
Lookup

**Refers To**
Group


### Standard Objects QuickText

**Field** **Details**

```
 SobjectType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
A list of object types that can be associated with the queue specified by the `QueueId` .

Use this object to associate a queue with the sObject that can be associated with the queue, including custom objects.

Warning: You can't update or insert more than 18 queues at once when using the Bulk API.

SEE ALSO:

Overview of Salesforce Objects and Fields

### QuickText

This object stores a snippet of text that allows users to send a quick response to a customer. Use quick text to create greetings, answers
to common questions, short notes, and more. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Channel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
A customizable picklist that can be used to group multiple related quick text
records together

**Type**
multipicklist


Standard Objects QuickText

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
A multi-select picklist that can be used to specify where specific quick text
messages are available, such as in Chat or in the Email publisher in Case Feed.

```
FolderId

FolderName

IsInsertable

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Returns the ID of the folder that contains the quick text. Available in API version
44.0 and later.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the quick text. Available in API version 44.0 and
later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the quick text is available in the channels selected in the `Channel`
field. If `false`, the quick text is not available. The label in the UI is **Include in**
**selected channels** . By default:

**•** This field is set to `true` on quick text records created from the Quick Text
page or via the API.

**•** This field is set to `false` on quick text records created during the Einstein
Reply Recommendations reply publishing process.


Standard Objects QuickText

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Message

Name

OwnerId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it's possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
textarea

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Sort (unavailable in API
version 25.0 and later), Update

**Description**
The content of the quick text record

**Type**
string

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Group, idLookup, Sort
(unavailable in API version 25.0 and later), Update

**Description**
A descriptive label for the quick text record

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Queue that owns the quick text record

This is a polymorphic relationship field.

**Relationship Name**
Owner


Standard Objects QuickText

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
SourceType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
(Used with Einstein Reply Recommendations.) Indicates how the text was
composed. This field is not available in the UI.

Possible values are:

**•** `EINSTEIN_GENERATED` —Text was generated by Einstein Reply
Recommendations

**•** `USER_EDITED` —Text was generated by Einstein Reply Recommendations,
and then edited by a user

**•** `USER_GENERATED` —User wrote the text

Use this object to create and manage the quick text messages available to users. You can categorize multiple quick text records into
groups using the Category field. The Category field can also be a parent to multiple custom-dependent Picklist fields to create a hierarchical
structure of categories.

QuickText is also used in Einstein Reply Recommendations, a feature that recommends stock replies for support agents to use in chats
in the Lightning Service Console. During setup, Einstein Reply Recommendations scans past chats to generate a list of commonly used
replies. Each generated reply is a ReplyText record. The admin then publishes, or converts, the replies to quick text, creating a corresponding
QuickText record for each reply. Therefore, certain QuickText fields are used only on quick text records that originated as a ReplyText
record.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuickTextChangeEvent (API version 48.0)**
Change events are available for the object.

**QuickTextHistory**

History is available for tracked fields of the object.

**QuickTextOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects QuickTextUsage

**QuickTextShare**

Sharing is available for the object.

### QuickTextUsage

Represents the usage of quick text on a record, including which quick text was used, who used it, and how they used it. Quick text is a
snippet of text that allows users to send a quick response to a customer. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
AppContext

Channel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the quick text was used. Possible values are:

**•** `Aloha` —Salesforce Classic

**•** `Lightning` —Lightning Experience

**•** `Unknown`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The channel in which the quick text was used. Possible values are:

**•** `Email`

**•** `Event`

**•** `Generic`

**•** `Internal`

**•** `Knowledge`

**•** `Live Agent`


Standard Objects QuickTextUsage

**Field** **Details**

**•** `Messaging`

**•** `Phone`

**•** `Portal`

**•** `Social`

**•** `Task`

```
FolderId

LaunchSource

LoggedTime

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the quick text at the time it was used.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the user started the quick text. Possible values are:

**•** `Floater`

**•** `Keyboard shortcut`

**•** `Macro`

**•** `Toolbar`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the quick text was used.

**Type**
string


Standard Objects QuickTextUsage

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the quick text.

```
OwnerId

QuickTextID

UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the quick text.

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
Filter, Group, Sort

**Description**
ID of the quick text.

This is a relationship field.

**Relationship Name**
QuickText

**Relationship Type**
Lookup

**Refers To**
QuickText

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that used the quick text.

This is a relationship field.


### Standard Objects Quote

**Field** **Details**

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**QuickTextUsageChangeEvent (API version 62.0)**
Change events are available for the object.

**QuickTextUsageOwnerSharingRule**

Sharing rules are available for the object.

**QuickTextUsageShare**

Sharing is available for the object.

### Quote

Represents a quote, which is a record showing proposed prices for products and services. Available in API version 18.0 and later.

### Quotes can be created from and synced with opportunities, and emailed as PDFs to customers

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

AdditionalAddress

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account that’s associated with the quote.

**Type**
address


Standard Objects Quote

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
Compound form of the additional address. Read-only. See Address Compound
Fields for details on compound address fields.

```
AdditionalCity

AdditionalCountry

AdditionalCountryCode

AdditionalLatitude

AdditionalLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's additional address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's additional address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s additional address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `AdditionalLongitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Quote

**Field** **Details**

**Description**
Used with `AdditionalLatitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –180 and 180
with up to 15 decimal places.

```
AdditionalName

AdditionalPostalCode

AdditionalState

AdditionalStateCode

AdditionalStreet

BillToContactId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name associated with the quote's additional address. Limited: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's additional address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's additional address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s additional address.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Street name for the quote's additional address.

**Type**
reference


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
ID of the contact that the order is billed to. This field is available in API version
56.0 and later. This field is available with Subscription Management.

```
BillingAddress

BillingCity

BillingCountry

BillingCountryCode

BillingLatitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the billing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's billing address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's billing address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Quote

**Field** **Details**

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a
billing address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

```
BillingLongitude

BillingName

BillingPostalCode

BillingState

BillingStateCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Entity that the quote is billed to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's billing address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s billing address.


Standard Objects Quote

**Field** **Details**

```
BillingStreet

CalculationStatus

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the quote's billing address.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Price calculations are performed by Salesforce. Tax calculations are performed
by a third-party tax provider integration with Salesforce. Both of these
calculations are asynchronous, and you can use this field to see the status of
the asynchronous processes.

This field is available with Subscription Management or Revenue Cloud.

Possible values are:

**•** `CompletedWithPricing` —Indicates that pricing is complete and
tax will now be calculated.

**•** `CompletedWithTax` —Indicates that pricing and tax calculation are
complete.

**•** `CompletedWithoutPricing` —Indicates that pricing and tax
calculation were skipped.

**•** `ConfigurationFailed` —Indicates that configuration failed. Available
in API version 62.0

**•** `ConfigurationInProgress` —Indicates that the configuration is
in progress. Available in API version 62.0

**•** `GroupRampConfigurationFailed` —Indicates that the checks for
group ramps have failed. Available in API version 65.0 and later.

**•** `NotStarted`

**•** `PriceCalculationFailed` —Indicates that pricing failed. Available
in API version 58.0 and later.

**•** `PriceCalculationInProgress` —Available in API version 58.0
and later.

**•** `PriceCalculationQueued` —The request is sent to the asynchronous
price calculation process, but the process hasn’t started. Available in API
version 58.0 and later.

**•** `QuoteRequestFailed` —Indicates that the requested quote changes
weren’t saved. Available in API version 62.0

**•** `QuoteRequestPartiallySaved` —Indicates that the requested
quote changes were partially saved. Available in API version 62.0


Standard Objects Quote

**Field** **Details**

**•** `ReconciliationFailed` —Indicates that the arrangement of quote
data failed. Available in API version 62.0

**•** `ReconciliationInProgress` —Indicates that the arrangement of
data is in progress. For a sales rep, this value appears as `Saving` on the
quote page. Available in API version 62.0

**•** `SaveFailedOrIncomplete` —Some or all of the records couldn’t be
saved. For example, some of the quote line item records weren’t saved.
Available in API version 58.0 and later.

**•** `Saving`

**•** `TaxCalculationFailed`

**•** `TaxCalculationInProcess`

**•** `TaxCalculationSuccess` —Available in API versions 56.0 and 57.0

**•** `TaxCalculationWaiting`

The default value is `NotStarted` .

```
CanCreateQuoteLineItems

ContactId

ContractId

CurrencyIsoCode

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
This field isn’t used.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact that’s associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract that’s associated with the quote.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist


Standard Objects Quote

**Field** **Details**

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

If the organization has multicurrency and a `Pricebook2Id` specified on the
quote, then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

This value is copied from the related Opportunity and can't be changed.

```
Description

Discount

Email

ExpirationDate

Fax

```

**Type**
textarea

**Properties**
Nillable

**Description**
Text description of the quote. Limit: 32,000 characters.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The difference between the QuoteLineItem record’s subtotal and its discounted
total, divided by the QuoteLineItem’s subtotal. Expressed as a percentage.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the contact who’s associated with the quote.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The date when this quote is no longer valid.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update


Standard Objects Quote

**Field** **Details**

**Description**
The fax number for the contact who’s associated with the quote.

```
GrandTotal

IsSyncing

LastReferencedDate

LastViewedDate

```

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total price of the quote plus shipping and taxes.

Note:

The `GrandTotal` is a system-calculated summary field and is not directly
referenceable or usable in custom formula fields on the Quote object. Attempts
to do so result in an error message. For example, "Error: Field GrandTotal does
not exist. Check spelling." To perform calculations based on the total value of
a quote, consider using a **Roll-Up Summary** field from related Quote Line Items
or performing calculations directly on the QuoteLineItem on page 4581 object.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the quote is syncing with an opportunity.

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
value is null, the user might have only accessed this record or list view but not
viewed it directly.


Standard Objects Quote

**Field** **Details**

```
LineItemCount

Name

OpportunityId

Phone

Pricebook2Id

QuoteAccountId

```

**Type**
int

**Properties**
Filter, Nillable

**Description**
The number of line items on the quote.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
Required. Name for the quote. Limit: 225 characters.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID for the opportunity associated with the quote.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The phone number of the contact who’s associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the price book associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Quote

**Field** **Details**

**Description**
ID of the account associated with the quote. This field is available in API version
58.0 and later only when the **Create Quotes Without a Related Opportunity**
setting on the Quotes Settings page is enabled.

This field is a relationship field.

**Relationship Name**
QuoteAccount

**Refers To**
Account

```
QuoteNumber

QuoteToAddress

QuoteToCity

QuoteToCountry

```

**Type**
string

**Properties**
Defaulted on create, Filter

**Description**
A system-generated number that identifies the quote.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the quote to address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the address to send the quote to for approval, such as a third
party-agency representing a buyer. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the address to send the quote to for approval. Up to 80 characters
allowed.


Standard Objects Quote

**Field** **Details**

```
QuoteToLatitude

QuoteToLongitude

QuoteToName

QuoteToPostalCode

QuoteToState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `QuoteToLongitude` to specify the precise geolocation of a
quote to address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `QuoteToLatitude` to specify the precise geolocation of a quote
to address. Acceptable values are numbers between –180 and 180 with up to
15 decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address to send the quote to for approval.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the address to send the quote to for approval. Up to 80 characters
allowed.


Standard Objects Quote

**Field** **Details**

```
QuoteToStreet

RecordSource

RecordTypeID

RelatedWorkId

ShippingAddress

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the address to send the quote to for approval.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the source application context for the record.

This field is available with Digital Insurance in API version 66.0 and later.

Possible values are:

**•** `DigitalInsurance`

**•** `Null`

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to the object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Relationship field that’s visible only if Field Service and Quotes are enabled in
the Salesforce org. This field refers to the work order that the quote is created
from. When a mobile worker creates a quote using the New Quote action in
the Field Service mobile app, this field is automatically populated. This field is
used in the related list that shows all of the quotes related to the work order.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects Quote

**Field** **Details**

**Description**
Compound form of the shipping address. Read-only. See Address Compound
Fields for details on compound address fields.

```
ShippingCity

ShippingCountry

ShippingCountryCode

ShippingHandling

ShippingLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's shipping address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's shipping address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s shipping address.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update

**Description**
The total shipping and handling costs for the quote.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a
shipping address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.


Standard Objects Quote

**Field** **Details**

```
ShippingLongitude

ShippingName

ShippingPostalCode

ShippingState

ShippingStateCode

ShippingStreet

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the quote's shipping address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's shipping address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Quote

**Field** **Details**

**Description**
Street name for the quote's shipping address.

```
Status

Subtotal

Tax

TotalPrice

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**

The status of the quote. The standard options are:

**•** —None—

**•** Draft

**•** Needs Review

**•** In Review

**•** Approved

**•** Rejected

**•** Presented

**•** Accepted

**•** Denied

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The sum of sales price multiplied by quantity for line items, not including the
discount.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update

**Description**
The total taxes for the quote.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total of the quote line items after discounts and before taxes and shipping.


Standard Objects Quote

**Field** **Details**

```
TotalPriceWithTax

TotalTaxAmount

```

Usage

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalPrice` and `TotalTaxAmount` . This field is available in
API version 55.0 and later. This field is available if Subscription Management is
enabled in your org.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all taxes. This field is available in API version 55.0 and later.
This field is available if Subscription Management is enabled in your org.

This field is a calculated field.

Use Quote to manage proposed product prices for customers. To update a Quote, your client application needs “Edit” permission.

**•** Client applications can create, update, delete, and query Attachment records associated with a quote via the API.

**•** You can sync a quote and its parent Opportunity.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteFeed (API version 39.0)**
Feed tracking is available for the object.

**QuoteHistory (API version 57.0)**
History is available for tracked fields of the object.

**QuoteOwnerSharingRule (API version 41.0)**
Sharing rules are available for the object.


### Standard Objects QuoteAction

**QuoteShare (API version 41.0)**
Sharing is available for the object.

SEE ALSO:

QuoteLineItem

QuoteDocument

Opportunity

### QuoteAction

Indicates the type of sales transaction that’s being quoted; for example, a renewal sale. This object is available in API version 59.0 and
later.

If a quote doesn't have a quote action, Salesforce treats it as a quote of the `Add` type. When such a quote is used to create an order,
Salesforce automatically creates an order action of the `Add` type.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in orgs with Revenue Cloud. It’s also available in Industries Automotive and Industries Field Service.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of the currency. Use only one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` . Must be unique within your
organization. Label is **Currency ISO Code** .

The default value is `USD` .

[See Supported Currencies (ICU) for a list of currency codes Salesforce supports. This field is](https://help.salesforce.com/s/articleView?id=xcloud.admin_supported_currencies.htm&type=5&language=en_US)
available in Revenue Cloud in API version 66.0 and later.

**Type**
dateTime


Standard Objects QuoteAction

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

Name

QuoteId

SourceAssetId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user accessed this record or list view indirectly, but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name given to the quote action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote related to this quote action.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects QuoteAction

**Field** **Details**

**Description**
The asset changed by this sales transaction. For example, if the quote action is a quantity
amendment, this field contains the ID of the asset that’s amended.

This field is a relationship field.

**Relationship Name**
SourceAsset

**Relationship Type**
Lookup

**Refers To**
Asset

```
Subtype

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The subtype of the action on the quote line item.

Valid values are:

**•** `DowngradeFrom` —Available in API version 66.0 and later.

**•** `DowngradeTo` —Available in API version 66.0 and later.

**•** `FieldAmendment`

**•** `Rollback`

**•** `StartDateAdjustment`

**•** `SwapIn` —Available in API version 66.0 and later.

**•** `SwapOut` —Available in API version 66.0 and later.

**•** `TransferFrom`

**•** `TransferTo`

**•** `UpgradeFrom` —Available in API version 66.0 and later.

**•** `UpgradeTo` —Available in API version 66.0 and later.

This field is available with Revenue Cloud in API version 64.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of sales transaction that the related quote is for.

Valid values are:

**•** `Add`


### Standard Objects QuoteAdjustmentGroup

**Field** **Details**

**•** `Amend`

**•** `Association` —Available in API version 66.0 and later.

**•** `Cancel`

**•** `No Change`

**•** `Renew`

**•** `Transfer` —Available with Revenue Cloud in API version 65.0 and later.

### QuoteAdjustmentGroup

Group containing a set of adjustments applied to a quote. This object is available in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.

Fields

**Field** **Details**

```
AdjustmentSource

AdjustmentType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the origin of the price adjustment.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually; for example, by a sales rep.

**•** `Promotion` —The adjustment is part of a promotion; for example, a holiday sale
discount.

**•** `Rule` —The adjustment is due to a price rule.

**•** `System` —The adjustment originates from the system, for example, a volume discount.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects QuoteAdjustmentGroup

**Field** **Details**

**Description**
Indicates the type of mathematical adjustment to be applied to the quote.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override. Available in API
version 59.0 and later.

```
AdjustmentValue

Description

Name

Priority

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The specified `AdjustmentType` amount that is applied to the quote. For example, when
`AdjustmentType` is `AdjustmentAmount`, `AdjustmentValue` is the cash
amount of the price adjustment. When `AdjustmentType` value is
`AdjustmentPercentage`, `AdjustmentValue` is the percent value of the price
adjustment. When `AdjustmentType` is `OverrideAmount`, `AdjustmentValue`
overrides the total amount of the quote.

**Type**
textarea

**Properties**
Nillable

**Description**
User-entered information about the quote adjustment group.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The user-defined name of the quote adjustment group.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects QuoteAdjustmentGroup

**Field** **Details**

**Description**
A numeric value that represents the order of precedence of the quote adjustment group. It
can also represent the order of precedence when applying the `AdjustmentType` values.

For example, a quote can have two adjustments: a $100 discount and a 10% discount. This
field indicates which adjustment to apply first.

```
QuoteId

TotalAmount

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote related to the adjustments in this group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total of all quote adjustments in this quote adjustment group, excluding tax.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteAdjustmentGroupChangeEvent on page 68**
Change events are available for the object.

**QuoteAdjustmentGroupFeed on page 55**
Feed tracking is available for the object.

**QuoteAdjustmentGroupHistory on page 63**
History is available for tracked fields of the object.

**QuoteAdjustmentGroupOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects QuoteDocument

**QuoteAdjustmentGroupShare on page 67**
Sharing is available for the object.

### QuoteDocument

Represents a quote in document format. Available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContentVersionDocumentId

CurrencyIsoCode

Discount

Document

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID for the document’s version.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist

**Description**
Available only for organizations with the multicurrency feature enabled.

Contains the ISO code for any currency allowed by the organization. If the
organization has multicurrency and a `Pricebook2Id` specified on the quote,
then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The discount for the quote used in the document.

**Type**
base64


Standard Objects QuoteDocument

**Field** **Details**

**Properties**
Create, Nillable

**Description**
The binary data of the document stored in the QuoteDocument object.

```
DocumentTemplate

GrandTotal

Name

QuoteId

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the template used to generate the document.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Grand total for the quote used in the document.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Name of the quote document.

**Type**
reference

**Properties**
Create, Filter, GroupSort

**Description**
ID for the quote used for the document.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the document.

Possible values are:

**•** `Completed`


### Standard Objects QuoteLineGroup

**Field** **Details**

**•** `Failed`

**•** `Generating`

**•** `In Progress`

**•** `None`

**•** `Queued`

The default value is `None` .

Usage

Use the QuoteDocument object to store a document that can be used to present the quote information to the customer.

SEE ALSO:

### Quote

QuoteLineItem

### QuoteLineGroup

Stores the group information for line items in a quote. It also stores the aggregated line field information (subtotal). It contains a
parent-child relationship to quote. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
Description

EndDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the group.

**Type**
date


Standard Objects QuoteLineGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

```
Name

QuoteId

SegmentType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period for the segment.

Possible values are:

**•** `Custom`

**•** `FreeTrial` —Free Trial

**•** `Prorated`

**•** `Yearly`

The default value is `Yearly` .


Standard Objects QuoteLineGroup

**Field** **Details**

```
SortOrder

StartDate

SummarySubtotal

Type

UnitPriceUplift

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total amount of all the line items in the group.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the group.

Possible values are:

**•** `CPQQuoteGroup` —CPQ Line Grouping

The default value is `CPQQuoteGroup` .

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage increase of the quote line group's unit price.


### Standard Objects QuoteLineItem QuoteLineItem

Represents a quote line item, which is a member of the list of Product2 products associated with a quote, along with other information
about those line items on that quote. Available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The user must have “Edit” permissions on quote records to create or update quote line items on a quote. The user must have “Edit”
permissions on quote records to delete a quote line item.

Some of the fields are available when you turn on Subscription Management.

Fields

**Field** **Details**

```
BatchIdentifier

BillingFrequency

BillingReference

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier for a product bundle in a transaction processing batch. This value makes sure that
quote lines from the same bundles process together.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period that indicates how often the quote line item is billed. This field is available
in API version 55.0 and later. This field is available when Subscription Management is enabled.

Possible values are:

**•** `Annual`

**•** `Monthly`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
Reference to the original quote for which this quote line item is created. This field is available
in API version 61.0 and later.

```
CurrencyIsoCode

CustomProductName

Description

Discount

DiscountAmount

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Available only for organizations enabled for multiple currencies. Contains the ISO code for
any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 specified on the quote (the
`Pricebook2Id` field isn’t blank), then the currency value of this field must match the
currency of the PricebookEntry objects for any associated quote line items.

This value comes from the related quote and can't be changed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Custom product name for the quote line item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the line item. Limit: 225 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional discount percentage, specified by the sales representative at the line level.
Editable number from 0 to 100.

**Type**
currency


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The fixed amount discount to apply to the quote line item. Available in API version 59.0 and
later.

```
DoesAutomaticallyRenew

Division

EffectiveGrantDate

EndDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the quote line item is set to automatically renew (True) or not (False).

The default value is `false` .

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
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the resources associated with the quote line item are granted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription ends. This field is available in API version 55.0 and later. This field is available if
Subscription Management is enabled in your org.

You can indicate a subscription’s length by using either `StartDate` and `EndDate`, or
by using `StartDate` and `SubscriptionTerm` . If you provide a value for both


Standard Objects QuoteLineItem

**Field** **Details**

`EndDate` and `SubscriptionTerm`, `EndDate` is used to determine the subscription’s
length.

```
EndDateTime

EndQuantity

EndTime

HasQuantitySchedule

HasRevenueSchedule

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time of the quote line item, which is derived from the End Date and End
Time fields in the time zone specified in the Start and End Time Zone field. If the time zone
isn't specified, the default is Coordinated Universal Time (UTC).

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
If the quote line item is sold on a subscription, this field indicates the end quantity when
the subscription ends. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end time of the quote line item.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a quantity schedule.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a revenue schedule. If this object has a revenue schedule, the `GrandTotal` and
`TotalPrice` fields can't be updated. In addition, the `Quantity` field can't be updated
if this object has a quantity schedule. The system ignores any attempt to update this field.
The update isn't rejected but the updated value is ignored.

```
HasSchedule

IsPrimarySegment

LastReferencedDate

LastViewedDate

LegalEntityId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the line item uses schedules.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the segment for the quote line item is a primary segment (true) or not
(false).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user only accessed this record or list view ( `LastReferencedDate` ) but not viewed
it.

**Type**
reference


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the legal entity record associated with the quote line item.

This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

```
LineNumber

ListPrice

ListPriceTotal

Margin

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. An automatically generated number identifying the quote line item. In the form
of `QL-XXXXX` .

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Corresponds to the `UnitPrice` on the PricebookEntry that is associated with
this line item, which can be in the standard price book or a custom price book. A client app
can use this information to show whether the unit price (or sales price) of the line item differs
from the price book entry list price.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The `ListPrice` times the `Quantity` . This field is a calculated field.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional margin percentage, specified by the sales representative at the line item level.


Standard Objects QuoteLineItem

**Field** **Details**

This field is available in Revenue Cloud in API version 65.0 and later.

```
MarginAmount

NetTotalPrice

NetUnitPrice

OpportunityLineItemId

ParentQuoteLineItemId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional margin amount, specified by the sales representative at the line item level.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This field is a calculated field equal to `TotalAdjustmentAmount` plus
`TotalLineAmount` .

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The unit price after all price adjustments are applied.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the related opportunity line item. This field is populated by the API during creation of
the quote line item. Not editable. Available in API version 40.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the related line item in the parent quote.


Standard Objects QuoteLineItem

**Field** **Details**

This field is populated by the API during creation of the quote line item.

This field is available in version 58.0 and later. This field is available when Subscription
Management is enabled.

This field is a relationship field.

**Relationship Name**
ParentQuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

```
PartnerDiscountPercent

PartnerUnitPrice

PeriodBoundary

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The partner’s discount percent applied to the quote lines. Available in API version 59.0 and
later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price after applying the discount given to the partner for the quote line item.
Available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period boundary helps determine the start and end date of the billing periods.

This field is available in API version 55.0 and later. This field is available with Subscription
Management and Revenue Cloud.

Possible values are:

**•** `AlignToCalendar` —the period starts on the first day of the term unit; for example,
the first day of the month.

**•** `Anniversary` —The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.


Standard Objects QuoteLineItem

**Field** **Details**

**•** `DayOfPeriod` —the period starts on the day indicated by `PeriodBoundaryDay` .

**•** `LastDayOfPeriod` —the period starts on the last day of the pricing term unit.

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** For termed selling models where the `PeriodBoundary` value is `Anniversary`,
the value of the `PeriodBoundary` field is automatically converted to
`DayOfPeriod` .

**•** Start date adjustment operation on an asset preserves the original value without
conversion.

```
PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when `PeriodBoundary` is `DayOfPeriod` . Indicates day of the week or
month that marks the period boundary. Must be an integer from 1 through 31.

This field is available in API version 55.0 and later. This field is available with Subscription
Management and Revenue Cloud.

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** When `PeriodBoundary` field value is converted from `Anniversary` to
`DayOfPeriod` for termed selling models, the value of the `PeriodBoundaryDay`
field is automatically populated with the day value from AssetActionSource.StartDate.

**•** Start date adjustment operation on an asset preserves the original value without
conversion.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
The field is populated based on input in the StartDate, PeriodBoundary, and
PeriodBoundaryDay when BillingFrequency is Annual and PricingTermUnit is Annual or by
manual user entry. Possible values are:

**•** `1-January`

**•** `2-February`


Standard Objects QuoteLineItem

**Field** **Details**

**•** `3-March`

**•** `4-April`

**•** `5-May`

**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** For termed selling models where `PeriodBoundary` field value is `Anniversary`
and `PricingTermUnit` field value is `ANNUAL`, `SEMI_ANNUAL`, or `QUARTERLY`,
the value of the `PeriodBoundaryStartMonth` field is automatically recalculated
by using AssetActionSource.StartDate.month.

**•** Start date adjustment operation on an asset preserves the original value without
conversion.

```
PricebookEntryId

PriceRevisionPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated PricebookEntry. Exists only for orgs with Products enabled. In
API 38.0 and earlier, if `Product2Id` is populated with `PricebookEntryId` data,
you receive an error message. In API 39.0 and later, `Product2Id` is nulled, and
`PricebookEntryId` is populated with the `PricebookEntryId` data.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price uplift policy associated with this quote line item.

This field is a relationship field.

**Relationship Name**
PriceRevisionPolicy


Standard Objects QuoteLineItem

**Field** **Details**

**Refers To**
PriceRevisionPolicy

Label is **Price Revision Policy** .

This field is available in Revenue Cloud in API version 65.0 and later.

```
PricingContractId

PriceWaterfallIdentifier

PricingTerm

PricingTermCount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contract used for pricing that's associated with the quote line item.

This field is a relationship field.

**Relationship Name**
PricingContract

**Refers To**
Contract

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing
of the detail record. Available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. For example, if a monthly subscription is priced
yearly, this field is 12.

This field is available in API version 55.0 and later. This field is available with Subscription
Management.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

```
PricingTermUnit

Product2Id

ProductInstanceIdentifier

ProductSellingModelId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of time for the pricing term. This field is available in API version 55.0 and later. This
field is available with Subscription Management.

Possible values are:

**•** `Annual` —Available in API version 58.0 and later. UI label is `Years` .

**•** `Months` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with this QuoteLineItem. In API 38.0 and earlier, if
`Product2Id` is populated with `PricebookEntryId` data, you receive an error
message. In API 39.0 and later, `Product2Id` is nulled, and `PricebookEntryId` is
populated with the `PricebookEntryId` data.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product instance that’s added to a quote. Each quote line item created for the
same product instance has the same product instance identifier value.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

This field is a relationship field.


Standard Objects QuoteLineItem

**Field** **Details**

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

```
ProrationPolicyId

Quantity

QuantityUnitOfMeasureId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. This field is available in API version 55.0 and later. This
field is available with Subscription Management.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The number of units for the line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unit of measure for the quantity, start quantity, and end quantity.

This field is a relationship field.

**Relationship Name**
QuantityUnitOfMeasure

**Refers To**
UnitOfMeasure


Standard Objects QuoteLineItem

**Field** **Details**

```
QuoteActionId

QuoteId

QuoteLineGroupId

QuoteLineItemRecipientId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related quote action. This field is available in API version 58.0 and later. This
field is available with Subscription Management and Revenue Lifecycle Management.

This field is a relationship field.

**Relationship Name**
QuoteAction

**Relationship Type**
Lookup

**Refers To**
QuoteAction

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the quote line group for the quote line item.

This field is a relationship field.

**Relationship Name**
QuoteLineGroup

**Refers To**
QuoteLineGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recipient for the quote line item.

This field is a relationship field.


Standard Objects QuoteLineItem

**Field** **Details**

**Relationship Name**
QuoteLineItemRecipient

**Refers To**
QuoteLineItemRecipient

```
RampIdentifier

RelatedQuoteLineItemId

SegmentIdentifier

SegmentName

SegmentType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp ID used to group quote line item segments.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The quote line item ID related to the order item created.

This field is a relationship field.

**Relationship Name**
RelatedQuoteLineItem

**Refers To**
OrderItem

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the segment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the quote line item segment.

**Type**
picklist


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period for the segment.

Possible values are:

**•** `Custom`

**•** `FreeTrial` —Free Trial

**•** `Prorated`

**•** `Yearly`

The default value is `Yearly` .

```
SellingModelType

ServiceDate

SortOrder

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the quote line item is sold as a one-time purchase, an evergreen
subscription, or as a termed subscription. This field is available in API version 55.0 and later.
This field is available with Subscription Management.

Possible values are:

**•** `Evergreen`

**•** `OneTime`

**•** `TermDefined`

The default value is `OneTime` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the product revenue is recognized and the product quantity is shipped.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of where the line item is in the sorted order such as 1, 2, 3. The SortOrder value
determines the order in which a quote line item appears in the Quote Line Items related list


Standard Objects QuoteLineItem

**Field** **Details**

and the Quote PDF. Client apps can use this value to match the sort order in Salesforce. This
field is only available in API versions 21.0 and greater.

```
StartDate

StartDateTime

StartEndTimeZone

StartTime

StartQuantity

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription starts. This field is available in API version 55.0 and later. This field is available
with Subscription Management.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date and time of the quote line item, which is derived from the Start Date and Start
Time fields in the time zone specified in the Start and End Time Zone field. If the time zone
isn't specified, the default is Coordinated Universal Time (UTC).

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone for the quote line item's start and end dates, times, and datetimes.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start time of the quote line item.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
If the quote line item is sold on a subscription, this field indicates the item quantity when
the subscription starts. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

```
StartingPriceTotal

StartingUnitPriceSource

Status

SubscriptionTerm

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The starting unit price times the quantity.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was entered manually or calculated. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

Possible values are:

**•** `Manual`

**•** `System`

**•** `Inherited`

**Type**
dynamic picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the quote line item. This field is available in API version 60.0 and
later. The `QuoteLineItemStatus` permission is required to access this field.

Possible values are:

**•** `In Progress`

**•** `Pending`

**•** `Approved`

**•** `Rejected`

Default value is `In Progress` .

**Type**
int


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The number of terms in the subscription.

You can indicate a subscription’s length by using either `StartDate` and `EndDate`, or
by using `StartDate` and `SubscriptionTerm` . If you provide a value for both
`EndDate` and `SubscriptionTerm`, `EndDate` is used and `SubscriptionTerm`
is ignored.

```
SubscriptionTermUnit

Subtotal

TotalAdjustment

TotalAdjustmentAmount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of time used to define the subscription. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

Possible values are:

**•** `Annual` —UI label is `Years`

**•** `Months`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The line item's `Quantity` multiplied by the `UnitPrice` . In Revenue Cloud, `Subtotal`
is set to `TotalLineAmount` when `TotalLineAmount` has a value.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The total discount percentage applied at the line item level. This percentage is calculated
by using the formula: (Total Line Amount - Net Total Price) / Total Line Amount.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
The sum of the adjustments applied to the quote line item, inclusive of quantity, prorated
for the duration of the subscription.

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

```
TotalCost

TotalLineAmount

TotalMargin

TotalMarginAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total cost of all products sold in the quote, calculated by multiplying the quantity by
the unit cost.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price of the quote line item, before price adjustments, inclusive of quantity, prorated
for the duration of the subscription. This price is a calculated field equal to `ListPrice`
times `Quantity` times `PricingTermCount` .

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The effective margin percentage at the line item level. This percentage is calculated by using
the formula: (Net Total Price - Total Cost) / Net Total Price.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The effective margin amount at the line item level. This amount is calculated by subtracting
total cost from net total price.


Standard Objects QuoteLineItem

**Field** **Details**

This field is available in Revenue Cloud in API version 65.0 and later.

```
TotalPrice

UnitCost

UnitPrice

UnitPriceUplift

ValidationResult

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Calculated by applying the `Discount` to the `Subtotal` . This field is nillable,
but you can't set both `TotalPrice` and to null in the same update. To insert the for a
quote line item via the API (given only a unit price and the quantity), calculate this field as
the unit price multiplied by the quantity. This field is read only if the quote line item has a
revenue schedule.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit cost of a product sold as part of the quote.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The price per unit for the quote line item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage increase of the quote line item's unit price.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the quote line item was configured and priced by Revenue Lifecycle
Management.


Standard Objects QuoteLineItem

**Field** **Details**

A quote can be activated only after all its quote line items are configured and priced by
Revenue Lifecycle Management.

Valid values are:

**•** `Warning` —Indicates that the quote line item wasn’t configured and priced by Revenue
Lifecycle Management.

Available in API version 60.0 and later.

```
Visibility

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies how Salesforce shows a quote line item in the Transaction Line Editor and a quote
document.

Possible values are:

**•** `Always` —Quote line items are always displayed in the Transaction Line Editor.

**•** `Never` —Quote line items aren't displayed in the Transaction Line Editor or in the quote
document.

**•** `Quote Document Only` —Quote line items are displayed only in the quote
document, but not in the Transaction Line Editor.

**•** `Transaction Line Editor Only` —Quote line items are displayed only in
the Transaction Line Editor, but not in the quote document.

The default value is `Always` .

A quote record can have QuoteLineItem records only if the quote has a Pricebook2. A QuoteLineItem must correspond to a Product2
that is listed in the quote's Pricebook2.

Note: If the multicurrency option is enabled, the `CurrencyIsoCode` field is present. It can't be modified, it’s always set to
the value of the `CurrencyIsoCode` of the parent quote.

Effects on Quotes

Quotes with related QuoteLineItem objects are affected in the following ways:

**•** Creating a QuoteLineItem increments the quote value by the `TotalPrice` of the QuoteLineItem.

**•** When you create or update a QuoteLineItem, the API verifies that the line item corresponds to a PricebookEntry in the Pricebook2
associated with the quote.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects QuoteLineItemRecipient

**QuoteLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteLineItemHistory (API version 57.0)**
History is available for tracked fields of the object.

SEE ALSO:

### Quote

QuoteDocument

Opportunity

### QuoteLineItemRecipient

Represents a site, employee, or other entity for which services are being quoted. This could include details such as the recipient's name,
contact information, associated site or location, and any specific requirements or preferences for the quoted services. This object is
available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BroadbandConnectionType

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the broadband connection that's available at the address.

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


Standard Objects QuoteLineItemRecipient

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

```
MaxDownloadSpeed

MaxUploadSpeed

Name

QuoteId

RecipientType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum download speed available at the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum upload speed available at the address.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the customer's site or location.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the recipient.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
picklist


Standard Objects QuoteLineItemRecipient

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of recipient of the service.

Possible values are:

**•** `Location`

**•** `Subscriber`

The default value is `Location` .

```
ServiceAddrValidationDate

Service Account

ServiceAddrValidationMsg

ServiceAddrValidationResult

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the address was validated.

**Type**
entityid

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the Account Entity where the product is used, serviced, or installed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message sent after the validation of the address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the address validation.

Possible values are:

**•** `Fail`

**•** `Partial Success`

**•** `Success`


Standard Objects QuoteLineItemRecipient

**Field** **Details**

The default value is `Success` .

```
ServiceAddress

ServiceCity

ServiceCountry

ServiceGeocodeAccuracy

```

**Type**
address

**Properties**
Filter

**Description**
The address where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the recipient receives the service.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the accuracy level of the geocoded address coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip` —Extended Zip

**•** `NearAddress` —Near Address

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`


Standard Objects QuoteLineItemRecipient

**Field** **Details**

**•** `Zip`

```
ServiceLatitude

ServiceLongitude

ServicePostalCode

ServiceState

ServiceStreet

ServiceabilityCheckDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the recipient receives the service.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the recipient receives the service.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street where the recipient receives the service.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

**Description**
The date and time when the serviceability check was done.

```
ServiceabilityData

SiteName

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The information about serviciability, such as broadband connection, download, and upload
speeds available at the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the customer's site or location.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[QuoteLineItemRecipientHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

### QuoteLinePriceAdjustment

Indicates the calculated price adjustment that is applied to the quote line, for example, a calculated volume discount or the prorated
value of a manual discount. Use the quote line price adjustment to inform potential customers about the type, value, and total amount
of their discounts. This object is available in API version 56.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.


Standard Objects QuoteLinePriceAdjustment

Fields

**Field** **Details**

```
AdjustmentAmountScope

AdjustmentSource

AdjustmentType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total` —The adjustment applies to the line item's total and isn’t multiplied by the
quantity. The adjustment amount is prorated for the duration of the subscription.

**•** `Unit` —The adjustment is multiplied by the line item’s quantity, prorated for the duration
of the subscription.

**•** `UnproratedTotal` —The adjustment applies to the line item's total and isn’t
multiplied by the quantity. The adjustment amount isn’t prorated for the duration of the
subscription.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The source of the adjustment.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually; for example, by a sales rep.

**•** `Promotion` —Reserved for future use.

**•** `Rule` —The adjustment results from a system rule, such as a price rule or product rule.

**•** `System` —The adjustment is determined by the pricing configuration for the product;
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of adjustment to apply to a quote line.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.


Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override. Available in API
version 59.0 and later.

```
AdjustmentValue

AppliedPromotionDate

CouponCode

Description

Name

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The value of the adjustment. Used together with `AdjustmentAmountScope` to
determine the amount of the adjustment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time on which the promotion was applied to the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the coupon code that was applied.

**Type**
textarea

**Properties**
Nillable

**Description**
The system-entered description of the quote line price adjustment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-entered name of the quote line price adjustment.


Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

```
PriceAdjustmentCauseId

Priority

QuoteAdjustmentGroupId

QuoteLineItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. `Null` if `AdjustmentSource` is
`Discretionary`, indicating a manual adjustment.

For example, if the price adjustment is due to a price adjustment tier, this field contains the
ID of the `PriceAdjustmentTier` record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**reference**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the quote adjustment group, which totals all price adjustments for the quote.

This field is a relationship field.

**Relationship Name**
QuoteAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
QuoteAdjustmentGroup

**Type**
reference


### Standard Objects QuoteLineRelationship

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote line item that this price adjustment applies to.

This field is a relationship field.

**Relationship Name**
QuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

```
TotalAmount

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total amount of the adjustment that applies to the quote line item, inclusive of quantity,
prorated for the duration of the subscription.

### QuoteLineRelationship

Describes the relationship between quote line items, such as items in a bundle. When you create a QuoteLineRelationship object, it’s
immutable: it can’t be edited or removed. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Subscription Management or Revenue Cloud is enabled.

Fields

**Field** **Details**

```
AssociatedQuantScaleMethod

```

**Type**
picklist


Standard Objects QuoteLineRelationship

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How to scale the quantity of the associated quote line, relative to the main quote line. If this
field has a non-null value, you can't edit the associated quote line's quantity.

Possible values are:

**•** `Constant`                   - The associated quote’s line quantity remains the same in relation to the
main quote line’s quantity. For example, the main quote line has a quantity of one and
the associated quote line has a quantity of one. If you increase the quantity of the main
quote line to two, the associated quote line’s quantity remains at one.

**•** `Proportional`                   - The associated order’s item quantity increases or decreases based
on the main quote line’s quantity. For example, the main quote line has a quantity of
one and the associated quote line has a quantity of two. If you increase the quantity of
the main quote line to two, the associated quote line’s quantity increases to four.

The default value is `Proportional` .

```
AssociatedQuoteLineId

AssociatedQuoteLinePricing

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle
component.

**Relationship Name**
AssociatedQuoteLine

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the associated quote line item is priced relative to the main quote line item.

Possible values are:

**•** `IncludedInBundlePrice`  - The associated quote line’s cost is $0 because it’s
included in the bundle’s price.


Standard Objects QuoteLineRelationship

**Field** **Details**

**•** `NotIncludedInBundlePrice`                   - The associated quote line has a cost because
it’s not included in the bundle’s price.

```
AssociatedQuoteLineRole

IsPriceInclusive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Describes the position of the associated quote line item in the relationship.

Possible values are:

**•** `BundleComponent`  - The associated quote line item is part of a bundle.

**•** `SetComponent`  - The associated quote line item is part of a set.

**•** `ClassificationComponent`  - The associated quote line item is a product
classification component.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether child products are included in the root bundle price. If set to `true`, the
price of each child product is zero.

The default value is `false` .

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


Standard Objects QuoteLineRelationship

**Field** **Details**

```
MainQuoteLineId

MainQuoteLineRole

Name

ProductRelatedComponentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the main quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle parent.

**Relationship Name**
MainQuoteLine

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main quote line item in the relationship.

Possible values are:

**•** `Bundle` —The main quote line item is the bundle parent.

**•** `Set` —The main quote line item is the set parent.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the quote line relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the product related component.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent


Standard Objects QuoteLineRelationship

**Field** **Details**

**Refers To**
ProductRelatedComponent

```
ProductRelationshipTypeId

QuoteId

RootQuoteLineId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of record that describes the relationship between the main and
associated quote lines.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the quote to which the main and associated quote lines belong.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The root quote line for the quote line relationship. In a bundle relationship, the root quote
line is the root bundle.

This field is a relationship field.


### Standard Objects QuoteItemTaxItem

**Field** **Details**

**Relationship Name**
RootQuoteLine

**Refers To**
QuoteLineItem

Associated Objects

This object has the following associated objects.

**QuoteLineRelationshipFeed**

Feed tracking is available for the object.

**QuoteLineRelationshipHistory**

History is available for tracked fields of the object.

### QuoteItemTaxItem

The tax that is applied to a quote line item. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Subscription Management is enabled in your org. This object is also available in Enterprise, Unlimited, and
Developer Editions of Revenue Cloud.

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The tax amount for the quote line item.

**Type**
picklist


Standard Objects QuoteItemTaxItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.

Possible values are:

**•** `BHD` —Bahraini Dinar

**•** `EUR` —Euro

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

The default value is 'USD'.

```
Description

Name

QuoteLineItemId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
User-defined description of the tax. For example, state sales tax or value-added tax (VAT).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the tax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related quote line item.

This is a relationship field.

**Relationship Name**
QuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem


### Standard Objects QuoteLineWorkSource

**Field** **Details**

```
Rate

TaxEffectiveDate

Type

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If the tax is a percentage tax, then this field contains the percent value. If the tax is a fixed
amount, then this field is null.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date used to calculate the tax rate.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Whether the tax is estimated or calculated by the tax provider.

Possible values are:

**•** `Actual`

**•** `Estimated`

### QuoteLineWorkSource

Represents an association between a quote and work sources, such as assets, quote line items, order products, or work type groups. This
object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects QuoteLineWorkSource

Fields

**Field** **Details**

```
AssetId

OrderItemId

QuoteId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Asset

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order product associated with the quote work source.

This field is a relationship field.

**Relationship Name**
OrderItem

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)


### Standard Objects QuoteRecipientGroup

**Field** **Details**

```
QuoteLineItemId

WorkTypeGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
QuoteLineItem

**Refers To**
QuoteLineItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the work source

This field is a relationship field.

**Relationship Name**
WorkTypeGroup

**Refers To**
WorkTypeGroup

### QuoteRecipientGroup

Represents a recipient group for which offers or products with the same configuration are being added. This also includes reusing these
groups to add or remove recipients. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActualMemberCount

```

**Type**
int


Standard Objects QuoteRecipientGroup

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The actual number of members in the quote recipient group.

```
Description

ExpectedMemberCount

LastReferencedDate

LastViewedDate

Name

QuoteId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the quote recipient group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The expected number of members in the quote recipient group.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the quote recipient group.

**Type**
reference


### Standard Objects QuoteRecipientGroupMember

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a quote recipient group.

This field is a relationship field.

**Relationship Name**
### Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

```
Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the quote recipient group is active.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Active` .

### QuoteRecipientGroupMember

Represents a junction between a quote line item recipient and a quote recipient group. This object is available in API version 64.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

```

**Type**
dateTime


Standard Objects QuoteRecipientGroupMember

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user referenced this record.

```
LastViewedDate

Name

OwnerId

QuoteLineItemRecipientId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user viewed this record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the quote recipient group member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of a quote recipient group member.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote line item recipient associated with the quote recipient group.

This field is a relationship field.

**Relationship Name**
QuoteLineItemRecipient


### Standard Objects RecentFieldChange

**Field** **Details**

**Refers To**
QuoteLineItemRecipient

```
QuoteRecipientGroupId

### RecentFieldChange

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote line item recipient group associated with the quote recipient group.

This field is a relationship field.

**Relationship Name**
QuoteRecipientGroup

**Refers To**
QuoteRecipientGroup

Use this virtual object to see how an opportunity has changed in the past seven days. Learn the previous value of a field, who made the
change, and when the change was made. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To use RecentFieldChange, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.

Fields

**Field** **Details**

```
ChangeDate

```

**Type**
dateTime

**Properties**

**Description**
The date and time that the specified field was changed.


Standard Objects RecentFieldChange

**Field** **Details**

```
CurrencyIsoCode

FieldName

ParentId

PreviousCurrencyValue

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency value. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as USD, GBP, or JPY.

The default value is 'USD'.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the opportunity field that you want the previous value of. Possible values are:

**•** `Amount`

**•** `CloseDate`

**•** `StageName`

**•** `ForecastCategory`

**•** `NextStep`

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity that you want the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Nillable


Standard Objects RecentFieldChange

**Field** **Details**

**Description**
The previous value of a currency field on an opportunity.

```
PreviousDateOnlyValue

PreviousTextValue

ValueChangedById

```

Usage

**Type**
date

**Properties**
Group, Nillable

**Description**
The previous value of a date field on an opportunity.

**Type**
string

**Properties**
Group, Nillable

**Description**
The previous value of a text field on an opportunity.

**Type**
reference

**Properties**
Group

**Description**
The ID of the user who changed the specified field's value during the specified time period.

This is a relationship field.

**Relationship Name**
ValueChangedBy

**Relationship Type**
Lookup

**Refers To**
User

One recentFieldChange record is returned for each field that was changed in the past seven days. The supported fields are Amount,
Close Date, Forecast Category, Next Step, and Stage Name. Only the most recent previous value is returned.

Example: To see the most recent previous amount for an opportunity, use the following query. Replace `006R0000XXXXXXXXXX`
with the ID of the opportunity.

```
   select PreviousTextValue from RecentFieldChange where ParentId = '006R0000003JkHBIA0'

   and FieldName = 'StageName'

```


### Standard Objects RecentlyViewed

If the sales rep didn't change the opportunity stage name in the past seven days, no values are returned. If the sales rep changed
the opportunity amount several times in the past seven days, only the most recent previous value is returned.

Example: To see the most recent previous amount, close date, forecast category, next step, and stage name for an opportunity,
use the following query. Replace `006R0000XXXXXXXXXX` with the ID of the opportunity.

```
      select PreviousTextValue, PreviousCurrencyValue, PreviousDateOnlyValue from

      RecentFieldChange where ParentId = '006R0000XXXXXXXXXX' and FieldName IN ('StageName',

      'Amount', 'CloseDate')

```

If the opportunity amount, close date, forecast category, next step, and stage name didn’t change in the past seven days, no values
are returned.

### RecentlyViewed

Represents records or list views that the current user has recently viewed or referenced (by viewing a related record). List views are
available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `update()`

Special Usage Rules

The RecentlyViewed object doesn’t support the Event, Task, Report, KnowledgeArticle, and Article objects.

The RecentlyViewed object supports only certain objects, and supports list views only for those supported objects. Supported objects
have the fields `LastReferencedDate` and `LastViewedDate` .

Note: RecentlyViewed records for users who are members of several communities can’t be retrieved automatically into a map
via Apex. This is because records of a user with different networks can result in duplicate IDs that maps don’t support.

Fields

**Field** **Details**

```
Alias

Email

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias on the record.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort


Standard Objects RecentlyViewed

**Field** **Details**

**Description**
The email address on the record.

```
FirstName

Id

IsActive

LastName

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name on the record. If the recently viewed record is a user, the value is the user’s
first name.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the recently viewed record or list view.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the recently viewed record is an active user ( `true` ) or not ( `false` ). This
field contains a value only if the recently viewed record is a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name on the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.

**•** Viewing or opening a record.

**•** Selecting a record in a lookup search or related list search.


Standard Objects RecentlyViewed

**Field** **Details**

```
LastViewedDate

Name

NetworkId

Phone

ProfileId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name on the recently viewed record or list view. If the recently viewed record is a user,
contact, or lead, the value is a concatenation of the `firstname` and `lastname` field
values.

**Type**
reference

**Properties**
Filter,Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can add a `NetworkId` only when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 27.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number on the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the user’s profile ID.

This field is a relationship field.


Standard Objects RecentlyViewed

**Field** **Details**

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

```
Title

Type

UserRoleId

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the title of the user; for example CFO or
CEO.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object type for this recently viewed record or list view. Valid values include any standard
or custom objects that RecentlyViewed supports.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user role associated with this object.

This field is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

This object provides a heterogeneous list of different object types. The list consists of recently viewed records, records that were recently
referenced (a related record was viewed), or recently viewed list views. A record is considered viewed when the user sees the record


### Standard Objects Recommendation

details, but not when the user sees the record in a list with other records. Use this object to programmatically construct a list of recently
viewed items specific to the current user. For example, use this object on a custom user interface or for search auto-complete options.
You can also retrieve a filtered list of records by object type ( `Type` ). The RecentlyViewed data is periodically truncated down to 200
records and 200 list views. RecentlyViewed data is retained for 90 days, after which it’s removed on a periodic basis.

Use this query in your code to retrieve a list of all the records and list views that were recently viewed. The results are ordered from most
to least recent.

```
   SELECT Id, Name

   FROM RecentlyViewed

   WHERE LastViewedDate !=null

   ORDER BY LastViewedDate DESC

```

Use this query to retrieve data that was either viewed or referenced, but only for a limited set of objects.

```
   SELECT Id, Name

   FROM RecentlyViewed

   WHERE Type IN ('Account', 'Contact', 'Plan__c')

   ORDER BY LastViewedDate DESC

```

This query retrieves a list of all recently viewed contacts with contact-specific fields, such as the contact’s account name, and the custom
website field. Records are ordered from most to least recent.

```
   SELECT Account.Name, Title, Email, Phone, Website__c

   FROM Contact

   WHERE LastViewedDate != NULL

   ORDER BY LastViewedDate DESC

### Recommendation

```

Represents the recommendations surfaced as offers and actions for Einstein Next Best Action. This object is available in API version 45.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

You must have the Modify All Data or Manage Next Best Action Recommendations user permission to create and edit recommendations.

Fields

**Field** **Details**

```
AcceptanceLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects Recommendation

**Field** **Details**

**Description**
Label that appears as the accept option on the surfaced recommendation. Maximum size is
80 characters.

```
ActionReference

Description

ExternalId

ImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Flow referenced for this recommendation. Label is **Action** .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Text description of the recommendation. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores an identifier for the recommendation source, such as product, so Einstein can group
all responses for a given recommendation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Image referenced by this recommendation. Label is **Image** .

This is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset


Standard Objects Recommendation

**Field** **Details**

```
IsActionActive

LastReferencedDate

LastViewedDate

Name

NetworkId

RecommendationKey

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow referenced in the Action field is active (true) or not (false). Read
only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recommendation. Maximum size is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects RecommendationResponse

**Field** **Details**

**Description**
Track responses to a recommendation when it doesn’t have an ID. Maximum size is 255
characters.

```
RejectionLabel

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label that appears as the reject option on the surfaced recommendation. Maximum size is
80 characters.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RecommendationChangeEvent (API version 48.0)**
Change events are available for the object.

### RecommendationResponse

Represents the user responses to a presented offer or recommendation for Einstein Next Best Action. This object is available in API version
51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated() query()`, `retrieve()`,

Special Access Rules

You must have one of these user permissions to read, delete, or update recommendation responses:

**•** Modify All Data

**•** Manage Next Best Action Recommendations

**•** Manage Next Best Action Strategies

Fields

**Field** **Details**

```
ActionReference

```

**Type**
string


Standard Objects RecommendationResponse

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The full name of an action flow at the time of the response. The full name includes the action’s
namespace.

```
ContextRecord

ContextRecordName

ContextRecordType

NetworkId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of context record that contains the Einstein Next Best Action component. For example,
if the Einstein Next Best Action component is on a case record the ContextRecord is the ID
of the case record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the context record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the ContextRecord field.
For example, Account, Case, or Contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable). This is
a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup


Standard Objects RecommendationResponse

**Field** **Details**

**Refers To**
Network

```
OnBehalfOf

OnBehalfOfName

OnBehalfOfType

RecommendationKey

RecommendationName

RecommendationType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The user ID or record that is indirectly reacting to the recommendation.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the value stored for `OnBehalfOf` at time of response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the OnBehalfOf field. For
example, Account, Case, or Contact.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
RecommendationId if available, otherwise a generated string that represents the
recommendation name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Name of the recommendation returned from the recommendation strategy.

**Type**
string


### Standard Objects RecordAction

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Object type of the recommendation. It can be Recommendation or any object type mapped
to the Recommendation object. For example, if you map Product to Recommendation, the
RecommendationType is Product.

```
Response

StrategyReference

StrategyVersion

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The user’s response to the recommendation.

Possible values are:

**•** `Accepted`

**•** `Rejected`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The full name of a recommendation strategy flow at the time of the response. The response
is formatted as `namespace` underscore `prefix` double underscore `flowname`, such
as `namespace_prefix__flowname` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The recommendation strategy version that’s active at the time of the response.

The RecommendationResponse object can’t be customized with additional fields.

### RecordAction

Represents a relationship between a record and an action, such as a flow. Create a RecordAction for every action that you want to
associate with a particular record. Available in API version 42.0 and later.


Standard Objects RecordAction

Note: Access to the RecordAction object is determined by a user’s access to the associated parent record.

Supported Calls

`create()`, `delete()`,, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
ActionDefinition

ActionType

FlowDefinition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required in Lightning Flow for Service implementations that use version 44.0 or later of the
API. The API name of the action to associate with the record; for example, the API name of
a flow. Use this field rather than FlowDefinition. To distinguish a quick action from a flow
with the same API name, we prepend "QuickAction" to the API name of every quick action.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required in Lightning Flow for Service implementations that use version 46.0 or later of the
API. The type of action. Possible values are:

**•** `Flow` (default)

**•** `QuickAction`

For versions of the API prior to version 46.0, this field is set to Flow.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional in Lightning Flow for Service implementations using version 42.0 or 43.0 of the API.
An upgrade to Winter '19 or later, which uses API version 44.0 or later, copies FlowDefinition


Standard Objects RecordAction

**Field** **Details**

to ActionDefinition. For versions 42.0 and 43.0, this field is the API name of the flow that’s
associated with the record.

```
FlowInterviewId

IsMandatory

IsUiRemoveHidden

Order

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The flow interview ID of the paused or completed flow. This field can’t be set in
Process Builder.

This is a relationship field.

**Relationship Name**
FlowInterview

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Optional. Specifies whether the action is mandatory. The default value is false.

Note: At runtime, we show a reminder when the user closes a mandatory flow
without completing it. We don't show the reminder for quick actions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Optional. Specifies whether the ability to remove the action is hidden in the UI. The default
value is false. If true, the UI hides the ability to remove the action. However, actions can still
be deleted using the API.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects RecordAction

**Field** **Details**

**Description**
Required. The order of the action among all actions associated with this record.

```
ParticipantRoleId

Pinned

RecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The participant role that's associated with the record action.

This field is a polymorphic relationship field and is available in API version 58.0 and later.

**Relationship Name**
ParticipantRole

**Relationship Type**
Lookup

**Refers To**
ParticipantRole

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Specifies whether the action is pinned to the top or bottom of the component. If
an action is pinned, users see the Remove option in the UI unless `IsUiRemoveHidden`
is set to true. Possible values are:

**•** None (default)

**•** Top

**•** Bottom

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Record associated with the action. In version 46.0 and above, we support most
[object types. To learn about supported objects, see the Lightning Flow for Service Developer’s](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/guided_engagement_support.htm)
[Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/guided_engagement_support.htm)

This is a relationship field.

**Relationship Name**
Record


Standard Objects RecordAction

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssetRelationship, AssignedResource, AssociatedLocation, Campaign,
CampaignMember, CarePreauth, CarePreauthItem, Case, ChangeRequest, CollaborationGroup,
Contact, ContactRequest, Contract, CoverageBenefit, CoverageBenefitItem,
EnhancedLetterhead, Incident, Lead, Location, MemberPlan, OperatingHours, Opportunity,
Order, PlanBenefit, PlanBenefitItem, Problem, Pricebook2, PricebookEntry, Product2,
ProductItem, ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, PurchaserPlan, PurchaserPlanAssn,
RebateMemberAggregateItem, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, Shipment, SkillRequirement, SocialPersona,
SocialPost, TimeSlot, User, Visit, VoiceCall, WorkOrder, WorkOrderLineItem, WorkType,
WorkTypeGroup

ChangeRequest, Incident, Problem are available in API version 53.0 and later.

RebateMemberAggregateItem is available in API version 54.0 and later.

```
Status

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The current state of the action. Possible values are:

**•** `New` (default)

**•** `Paused`

**•** `Complete`

**•** `Started`

**•** `Unlinked` —The action was unlinked because the flow was paused and the current
record for the flow interview changed.

Paused and unlinked statuses do not apply to quick actions. This field can’t be set in Process
Builder.

The RecordAction object works with the Actions & Recommendations component in Lightning Experience. Although this junction object
can be used to create relationships between records and actions in Salesforce Classic, those relationships can’t be displayed in Salesforce
Classic.

Note: API version 44.0 added a field, ActionDefinition, so that a RecordAction in future releases can support other types of actions
in addition to flows. API version 44.0 and later maintain the FlowDefinition field to support processes that reference this field in
earlier API versions. Upgrading an org to Winter '19 or later, which uses API version 44.0 or later, copies the FlowDefinition field to
the ActionDefinition field. FlowDefinition will be deprecated in a future release, so use ActionDefinition instead.


Standard Objects RecordAction

When an action is deleted that’s referenced in an ActionDefinition or FlowDefinition, the RecordAction object is deleted. RecordAction
objects are also deleted when the associated parent record is deleted, or when a flow is paused and the current record context has
changed. When an action is completed, the associated RecordAction object is also deleted.

Deleted RecordActions are removed from the list when the page is refreshed.

[For more information about the Actions & Recommendations component and how it works with RecordActions, see the Lightning Flow](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)
[for Service Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)

Java Example

Here’s an example of how to associate flows to a record using the RecordAction object.

```
   public void associateNewCustomerFlowWithAccount(Account a) {

     try {

       RecordAction newRecordAction = new RecordAction();

       newRecordAction.setRecordId(a.getId());

       newRecordAction.setActionDefinition(“New_Customer_Flow”);

       newRecordAction.setOrder(1);

       SaveResult[] results = connection

           .create(new SObject[] { newRecordAction });

     } catch (ConnectionException ce) {

       ce.printStackTrace();

     }

   }

```

Data Model


### Standard Objects RecordActionHistory

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

### **RecordActionHistory**

History is available for tracked fields of the object.

### RecordActionHistory

Represents the lifecycle of a RecordAction as it goes through different states. Available in API version 44.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.


Standard Objects RecordActionHistory

Fields

**Field** **Details**

```
ActionDefinitionApiName

ActionDefinitionLabel

ActionType

IsMandatory

LoggedTime

ParentRecordId

```

**Type**
string

**Description**
Required. The API name of the action associated with the record. To distinguish a quick action
from a flow with the same API name, we prepend "QuickAction" to the API name of every
quick action.

**Type**
string

**Description**
Required. The label of the action that took place.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist

**Description**
Required. The type of action associated with the record. Possible values are:

**•** `Flow` (default)

**•** `QuickAction`

**Type**
boolean

**Properties**
Defaulted on create

**Description**
Optional. Specifies whether the action is mandatory. The default value is false.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The timestamp when the state change occurred.

**Type**
reference

**Properties**
Filter, Sort


Standard Objects RecordActionHistory

**Field** **Details**

**Description**
Required. The parent record for the associated action.

This is a relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssetRelationship, AssociatedLocation, Case, ChangeRequest,
CollaborationGroup, Contact, ContactRequest, Contract, EnhancedLetterhead, Incident, Lead,
Location, OperatingHours, Opportunity, Order, Pricebook2, PricebookEntry, Problem, Product2,
ProductItem, ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, RebateMemberAggregateItem, ResourceAbsence,
Scorecard, ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shipment, SkillRequirement, SocialPersona, SocialPost, TimeSlot,
User, Visit, VoiceCall, WorkType

ChangeRequest, Incident, Problem are available in API version 53.0 and later.

RebateMemberAggregateItem is available in API version 54.0 and later.

```
Pinned

RecordActionId

State

```

**Type**
picklist

**Properties**
Defaulted on create, Nillable, Restricted picklist

**Description**
Optional. Specifies whether the action is pinned to the top or bottom, or unpinned. Possible
values are:

**•** None

**•** Top

**•** Bottom

**Type**
string

**Properties**
Filter, Sort

**Description**
Required. The ID of the RecordAction.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist


Standard Objects RecordActionHistory

**Field** **Details**

**Description**
Required. The state of the action. A state change triggers the logging of a history event.
Possible values are:

**•** `Started` (default)

**•** `Paused`

**•** `Resumed`

**•** `Completed`

**•** `Unlinked` —The action was unlinked because the flow was paused and the current
record for the flow interview changed.

```
UserId

```

Usage

**Type**
reference

**Description**
Required. The user that conducted the action.

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

The RecordActionHistory object represents the lifecycle of an action on a record as it goes through different states.

The RecordActionHistory object is a big object. For this reason, when you use synchronous SOQL, SOAP, REST, Bulk, or Apex APIs to read
this object, queries must follow a specific pattern or they fail. Queries must match one of these patterns and use fields in this precise
order when more than one field is used.

**•** ParentRecordId

**•** ParentRecordId, LoggedTime (DESC)

**•** ParentRecordId, LoggedTime (DESC), RecordActionId

For example, this SOQL query follows the ParentRecordId, LoggedTime (DESC) pattern.

```
SELECT ActionDefinitionApiName, User, State FROM RecordActionHistory WHERE

      ParentRecordId = {CaseId} ORDER BY ParentRecordId, LoggedTime DESC

```

Asynchronous SOQL queries do not need to follow a pattern, and can query any field.

Apex triggers cannot reference big object records. Use SOQL queries if you want to query RecordActionHistory records in Apex.

[For more information about the Actions & Recommendations component and how it works with RecordActions, see the Lightning Flow](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)
[for Service Developer Guide. Learn more about big objects and how to query them in the Query Big Objects module on Trailhead.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)


### Standard Objects RecordsetFilterCriteria

Java Example

Here’s a Java example of how to query a RecordActionHistory object.

```
   public void queryHBPOs(String parentRecordId) {

     try {

      SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");

        // query for the RecordActionHistory associated with ParentRecord

        QueryResult queryResults = connection.query("SELECT ActionDefinitionApiName,

   LoggedTime, State " +

         "FROM RecordActionHistory WHERE ParentRecordId = '" + parentRecordId + "' LIMIT

   50");

        if (queryResults.getSize() > 0) {

         for (int i=0;i<queryResults.getRecords().length;i++) {

          // cast the SObject to a strongly-typed RecordActionHistory

          RecordActionHistory raa = (RecordActionHistory)queryResults.getRecords()[i];

         System.out.println("ActionDefinitionApiName: " + raa.getActionDefinitionApiName()

    + " - LoggedTime: "+ format.format(raa.getLoggedTime().getTime()) + " - State: " +

            raa.getState());

         }

        }

     } catch (Exception e) {

        e.printStackTrace();

     }

     }

### RecordsetFilterCriteria

```

Represents a set of filters that can be used to match service appointments or assets based on your criteria fields. For example, you can
create recordset filter criteria so that only service appointments that satisfy the filter criteria are matched to the filtered shifts, and likewise
only maintenance work rules that satisfy your criteria are matched to assets. This object is available in API version 50.0 and later. Assets
and maintenance work rules are available in API version 52.0 and later.

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


Standard Objects RecordsetFilterCriteria

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the recordset filter criteria.

```
FilteredObject

IsActive

LastReferencedDate

LastViewedDate

LogicalOperator

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object used to define the filter criteria. Available in API version 52.0 or later.

Possible values are:

**•** `Asset`

**•** `ServiceAppointment`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the recordset filter criteria is associated with shifts or maintenance work
rules ( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects RecordsetFilterCriteria

**Field** **Details**

**Description**
Defines the logic to evaluate multiple recordset filter criteria rules. Available in API version
53.0 and later.

Possible values are:

**•** `AND`

**•** `OR`

```
Name

OwnerId

SourceObject

```

Usage Rate Field

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the recordset filter criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The source object that the filtered criteria are applied to. Shifts and maintenance work rules
are available in API version 52.0 and later. Appointment bundle objects are available in API
version 53.0 and later.

Possible values are:

**•** `ApptBundleAggrPolicy` —Appointment Bundle Aggregation Policy

**•** `ApptBundleConfig` —Appointment Bundle Config

**•** `Shift`

**•** `ContractLineOutcome`

**•** `MaintenanceWorkRule`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


### Standard Objects RecordsetFilterCriteriaRule

**Field** **Details**

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day.

Usage Rate Unit

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS

Let's say an employee is open to working a 9 am to 5 pm shift on a Sunday but only for emergency appointments. In this case, the
`SourceObject` is `Shift` and the `FilteredObject` is `ServiceAppointment` . The service appointments available for
### that shift are filtered for emergency appointments using the RecordsetFilterCriteriaRule object.

RecordSetFilterCriteria isn’t available for report types.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**RecordsetFilterCriteriaFeed**

Feed tracking is available for the object.

**RecordsetFilterCriteriaHistory**

History is available for tracked fields of the object.

**RecordsetFilterCriteriaOwnerSharingRule**

Sharing rules are available for the object.

**RecordsetFilterCriteriaShare**

Sharing is available for the object.

### RecordsetFilterCriteriaRule

Represents a rule using fields from the designated source object to create filters on the filtered, or target, object. RecordsetFilterCriteriaRule
is associated with the RecordsetFilterCriteria object. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects RecordsetFilterCriteriaRule

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
CriteriaField

LastReferencedDate

LastViewedDate

NextOccurence

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The field the filter rule is applied to. Asset fields are available in API version 52.0 and later.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment` . The format is, for
example, `Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` . All standard and
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects RecordsetFilterCriteriaRule

**Field** **Details**

**Description**
This field’s value is compared to the Usage Field to determine if the rule is true.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment` . The format is, for
example, `Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` . All standard and
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

```
Operator

RecordsetFilterCriteriaId

RecordsetFilterCriteriaRuleNumber

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The relational operator between `CriteriaField` and `Value` . Available in API version
52.0 or later.

Possible values are:

**•** `Equals` —Default

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the RecordsetFilterCriteria record to associate this rule with.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically assigned number of the recordset filter criteria rule.


Standard Objects RecordsetFilterCriteriaRule

**Field** **Details**

```
Type

Value

Usage Rate Field

Usage Rate Unit

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of criteria rule. Possible values are:

**•** `Criteria` —Default

**•** `Usage`

**•** `UsageCounter— Usage(Counter)`

**•** `UsageDuration— Usage(Duration)`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The expected value of `CriteriaField` applied to the filter rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day. Possible
values are derived from the source object’s standard and custom fields. Possible standard
source objects are `Asset` and `ServiceAppointment` . The format is, for example,
`Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS


### Standard Objects RecordsetFltrCritMonitor

Usage

If you want to create a filter rule for service appointments with a dispatched status, set `CriteriaField` to
`ServiceAppointment.Status` and `Value` to `Dispatched` . Then add the ID from a RecordsetFilterCriteria record to
`RecordsetFilterCriteriaId` to associate this rule with a filter criteria for shifts.

### RecordsetFltrCritMonitor

Monitors whether the value of an asset attribute is within the threshold of a recordset filter criteria (RFC). You can monitor one or more
RFCs for an Asset. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
AssetId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the asset to link the RFC to.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the RFC associated with the recordset filter criteria monitor.


Standard Objects RecordsetFltrCritMonitor

**Field** **Details**

```
IsWithinThreshold

Name

LastReferencedDate

LastViewedDate

RecordsetFilterCriteriaId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the value of the asset attribute is within the threshold of the RFC.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria monitor.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the recordset filter criteria.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup


### Standard Objects RecordType

**Field** **Details**

**Refers To**
RecordsetFilterCriteria

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RecordsetFltrCritMonitorChangeEvent on page 68**
Change events are available for the object.

**RecordsetFltrCritMonitorHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

AttributePicklistValue

### RecordType

Represents a record type.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

Important: Don’t use record types as an access control mechanism. Profile assignment governs create and edit access for an
object but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular record type can't
create records with that record type, but can access records associated with that record type. Users with access to an object can
read all record type information for that object. We strongly recommend against storing sensitive information in the record type
description, name, or label. Instead, store sensitive information in a separate object or fields to which you’ve applied appropriate
access controls.

**Field** **Details**

```
BusinessProcessId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects RecordType

**Field** **Details**

**Description**
Required for Opportunity and Lead record types in API version 17.0 and later. ID of an
associated BusinessProcess.

```
Description

DeveloperName

IsActive

IsPersonType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of this record. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Record Type Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Only active record types can
be applied to records. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this record has been designated as a person account ( `true` ) or not
( `false` ). Visible only if the organization has the person account feature enabled.


Standard Objects RecordType

**Field** **Details**

```
 Name

NamespacePrefix

 SobjectType

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Label of the record type in the user interface. Limit: 80 characters. Label is **Record**
**Type Label** .

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
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object to which this record type applies, including custom objects.

Use this object to offer different BusinessProcess records and subsets of picklist values to different users based on their Profile. Your client
application can describe or query RecordType records.

Client applications can create or update values in `RecordTypeId` on these objects, specifying a valid record type ID associated with
these objects.


### Standard Objects RecordTypeLocalization

Note: You can’t create or update the `RecordTypeId` field on the CampaignMember records. Set the CampaignMember
record type using the `CampaignMemberRecordTypeId` field on Campaign.

A client application can retrieve the list of valid record type IDs for a given object by querying the RecordType.

### RecordTypeLocalization

Represents the translated value of a label for a record type when the Translation Workbench is enabled for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, Unlimited, or Performance Edition and be enabled for the
Translation Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
Language

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**
The language for this translated label.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed


### Standard Objects RecordVisibility (Pilot)

**Field** **Details**

managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 ParentId

 Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the RecordType associated with the label that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the record type. Label is **Translation** .

Use this object to translate the labels of your record types into other supported languages.

### RecordVisibility (Pilot)

Represents the visibility attributes that determine a record’s read access. This object is read only and is available in API version 46.0 and
later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you need a CRM Analytics license or to contact Salesforce to participate in the pilot program. You must also have
the “View All Data” or “Enable RecordVisibility API” user permission.

Note: We provide the RecordVisibility object to selected customers through a pilot program that requires agreement to specific
terms and conditions. To be nominated to participate in the program, contact Salesforce. Pilot programs are subject to change,
and we can’t guarantee acceptance. The RecordVisibility object isn’t generally available unless or until Salesforce announces its
general availability in documentation or in press releases or public statements. We can’t guarantee general availability within any


Standard Objects RecordVisibility (Pilot)

particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features. You
[can provide feedback and suggestions for the RecordVisibility object in the group in the Trailblazer Community.](https://success.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000DN7N)

Fields

**Field Name** **Details**

```
RecordId

VisibilityAttribute

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The ID of the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The visibility attributes that determine the read access of a given record. For
example, a user ID, parent record ID, or group ID.

The output of visibility attributes is in JSON format and must be deserialized.

Use this object to query the attributes that determine the visibility of one or more records. You can’t create, delete, or update any records
using this object.

Up to 200 record IDs can be queried. You can include an `ORDER BY` clause for any field that is being selected in the query.

This sample query returns the visibility attributes for the indicated record.

```
SELECT RecordId, VisibilityAttribute

FROM RecordVisibility

WHERE RecordId=[single ID] // or Record IN [list of IDs]

```

The `RecordId` and `VisibilityAttribute` fields must be a part of the fields that are being selected despite `RecordId`
being used in the filter criteria as well.

RecordVisibility is a foreign key on the records. This query returns the visibility attributes for Account records:

```
SELECT Id, Name, RecordVisibility.VisibilityAttribute

FROM Account

```

You can’t filter `RecordId` fields when using RecordVisibility as a lookup or foreign key.

You can use `RecordVisibilityContext` to filter `WITH` clauses in queries. For more information, see `WITH` _[filteringExpression](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_with.htm)_
in the _SOQL and SOSL Reference_ .


### Standard Objects RedirectWhitelistUrl RedirectWhitelistUrl

Represents a trusted URL for external user redirections. Redirections to a different Salesforce org, including its publicly served pages and
content, are allowed from your Salesforce org only when the URL is a RedirectWhitelistUrl. For non-Salesforce URLs, a session setting
controls whether redirections from pages and components built in Salesforce Classic are restricted to RedirectWhitelistUrl objects. Except
for cross-org redirections, you can’t restrict redirections that originate from pages and components built with Lightning Experience. This
object is available in API version 48.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only authenticated internal and external users with the View Setup and Customize Application permissions can access or edit this object.

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
The unique name of the custom help section in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. The label corresponds to the section title in the user interface.
Limit: 80 characters.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the label.


Standard Objects RedirectWhitelistUrl

**Field** **Details**

```
MasterLabel

NamespacePrefix

Url

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the trusted URL.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The trusted URL.

These formats are accepted: `example.com`, `*.example.com`, and
`https://example.com` .

The host section of the URL can include an asterisk ( `*` ) as a wildcard. Otherwise, the URL
cannot be malformed. Examples of malformed URLs that fail a syntax check are
`malformed^url.example.com`, and `https://{subdomain}.example.com` .

To add a URL to a `RedirectWhitelistUrl` based on parameters, build the URL before
you update the `Url` field.


### Standard Objects Refund

Usage

Only redirections are restricted to the URLs in this object. A direct anchor link to an external URL is always allowed, even if that URL isn’t
in the allowlist. An example of a direct anchor link is `<a href="` _**`targetUrl`**_ `">` _**`linkText`**_ `</a>` .

Redirections include parameters that redirect the user and anchor links that include a redirection. For example, this anchor link includes
a redirection: `<a href="/?startURL=` _**`targetUrl`**_ `">` _**`linkText`**_ `</a>` . And this form action redirects the user through the
`saveURL` parameter: `<form action="/xyz?saveURL=` _**`targetURL`**_ `">` .

If the _`targetUrl`_ belongs to another Salesforce org, the redirection is permitted only when the target URL is a RedirectWhitelistUrl.

If the _`targetUrl`_ isn’t a Salesforce org URL, the redirection is checked against the RedirectWhitelistUrl object only when both of these
conditions are met.

**•** The redirection originates from a Salesforce Classic page or component.

**•** Either the `redirectBlockModeEnabled` or `redirectionWarning` [SessionSettings field in the SecuritySettings Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_securitysettings.htm)
API is `true` .

Note: Salesforce verifies the initial redirection outside of Salesforce against the RedirectWhitelistUrl object. However, Salesforce
can’t verify subsequent redirections. For example, if a link on a Visualforce page takes the user to https://www.example.com,
Salesforce verifies that you allowed redirections to https://www.example.com. If that URL then redirects the user to
https://spam.example.com, Salesforce can’t check that redirection, because it occurs outside of Salesforce.

For non-Salesforce URLs, you can choose whether to alert users about untrusted external redirections or to block those redirections
entirely via the `redirectBlockModeEnabled` and `redirectionWarning` fields on the SecuritySettings metadata API type.
These restrictions apply only to redirections from pages and components built in Salesforce Classic.

There’s one last special case to cover. For Salesforce org URLs, Salesforce always allows redirections to URLs within the same org, including
redirections from previous My Domain URLs. When the `enableCrossOrgRedirect` field on the SecuritySettings metadata API
type is `false`, Salesforce checks user redirections to other Salesforce orgs via a direct link, a post-action URL, or a post-login URL. If the
URL isn’t a RedirectWhitelistURL, the user isn’t redirected. An example of a direct link is `<a`

`href="https://www.example.com”>example.com</a>` . Post-action URLs and post-login URLs use a protected URL
redirect parameter, such as `retURL`, `startURL`, `saveURL`, `cancelURL`, and `targetURL` .

### Refund

Represents a refund made against a payment. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Note: You can only delete a payment in draft state, which you specify in the **Status** field.

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.


Standard Objects Refund

Fields

**Field** **Details**

```
AccountId

Amount

Balance

CancellationDate

CancellationEffectiveDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer account containing the payment that this refund targets.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of this refund.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Remaining balance following refund line applications. Equal to the Amount field – the Net
Applied field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the refund was canceled. This is a required parameter for void services.

**Type**
dateTime


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the cancellation of this refund takes effect.

```
CancellationGatewayDate

CancellationGatewayRefNumber

CancellationGatewayResultCode

CancellationSfResultCode

ClientContext

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the cancellation transaction was processed in the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique ID for the cancellation transaction. Generated by the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code for the cancellation transaction. Generated by the payment
gateway. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

**Type**
textarea

**Properties**
Nillable


Standard Objects Refund

**Field** **Details**

**Description**
Contains caller context for payment APIs. Useful for re-establishing context during an
asynchronous payment transaction.

```
Comments

CurrencyIsoCode

Date

EffectiveDate

Email

GatewayDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The date and time that this refund was created.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Defines the date and time when the refund application becomes effective.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the person who initiated the refund.

**Type**
dateTime


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that a successful gateway communication caused the creation of this refund.

```
GatewayRefNumber

GatewayResultCode

GatewayResultCodeDescription

ImpactAmount

IpAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the GatewayResultCode. Useful for providing additional context as to why the
gateway returned a specific result code.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows the refund’s financial impact against the customer’s accounts receivable. If the refund
amount is valid, it equals the Amount field. Equals 0 when the refund amount is void. Has a
null value when the refund is canceled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the person who initiated the payment.


Standard Objects Refund

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MacAddress

NetApplied

OrderPaymentSummaryId

PaymentGatewayId

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
record can have been referenced (LastReferencedDate) but not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the refund.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Equals the Total Applied field minus the Total Unapplied field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summary record that shows the balances of each authorization, capture, and
refund made against an order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Refund

**Field** **Details**

**Description**
The payment gateway used to process this refund.

This is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

```
PaymentGroupId

PaymentID

PaymentIntentID

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment group for the payment being refunded.

This is a relationship field.

**Relationship Name**
PaymentGroup

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment record.

This field is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
reference


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment intent record.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup

**Refers To**
PaymentIntent

```
PaymentMethodId

Phone

ProcessingMode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method used to create the payment being refunded.

This is a relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the refund.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:


Standard Objects Refund

**Field** **Details**

**•** `External` : Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` : Salesforce made and recorded an external call to the payment gateway.

```
RefundNumber

SfResultCode

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this refund.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline` : The gateway call failed but the transaction can be attempted again. For
example, the customer had insufficient funds or briefly lost their connection.

**•** `Indeterminate` : The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` : The gateway call failed and can’t work even if tried again. Gateway
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview` : The customer bank requires more information before completing
the payment.

**•** `Success` : The gateway call succeeded.

**•** `SystemError` : Salesforce ended the payment request before receiving a response.
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError` : Customer payment data was incorrect, such as a misspelling in
the credit card address or an incorrect CVV.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects RefundLinePayment

**Field** **Details**

**Description**
Defines the state of this refund.

Possible values are:

**•** `Canceled` : This refund has been voided and can no longer be allocated.

**•** `Draft` : The refund can be edited before posting it and allocating it to a target.

**•** `Processed` : This refund has been finalized and can be allocated against a target.

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

```
TotalApplied

TotalUnapplied

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of Amount fields across all of this refund’s applied refund lines.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of Amount fields across all of this refund’s unapplied refund lines.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how this refund is used.

Possible values are:

**•** `NonReferenced` : Standalone refund not linked to any payment.

**•** `Referenced` : Refund made against a payment.

### RefundLinePayment

A refund line that has been applied to a payment. This object is available in API version 48.0 and later.


Standard Objects RefundLinePayment

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated.

Fields

**Field** **Details**

```
Amount

AppliedDate

AssociatedAccountId

AssociatedRefundLinePaymentId

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
The total amount applied to or unapplied from a payment by the refund line.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that the refund was applied to the linked payment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The account for the payment that received the refund.

This is a relationship field.

**Relationship Name**
AssociatedAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference


Standard Objects RefundLinePayment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The refundLine that was unapplied. Populated only when RefundLinePayment’s Type has a
value of Unapplied.

This is a relationship field.

**Relationship Name**
AssociatedRefundLinePayment

**Relationship Type**
Lookup

**Refers To**
RefundLinePayment

```
Comments

Date

EffectiveDate

EffectiveImpactAmount

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can add comments to provide additional information on the refund line payment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
By default, the day the refund line payment record was created. Users can also enter a different
date.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Defines the date and time when the refund line application or unapplication becomes
effective.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects RefundLinePayment

**Field** **Details**

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied. If there’s an unapplied line related to this record,
EffectiveImpactAmount has a value of 0.

Note: EffectiveImpactAmount evaluates only the applied and unapplied line pair.
Therefore, the effective impact amount could be different for different lines within
the same refund.

```
HasBeenUnapplied

ImpactAmount

PaymentBalance

PaymentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shows whether this refund line has been unapplied.

Possible values are:

**•** `No`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The payment record’s balance following the application or unapplication of this refund line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The payment record that this refund line targets. Refund applications and unapplications
are made against this payment.


Standard Objects RefundLinePayment

**Field** **Details**

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

```
RefundBalance

RefundId

RefundLinePaymentNumber

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The refund record’s balance following the application or unapplication of this payment
refund line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent refund of this refund line.

This is a relationship field.

**Relationship Name**
Refund

**Relationship Type**
Lookup

**Refers To**
Refund

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this refund line.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


### Standard Objects RegisteredExternalService

**Field** **Details**

**Description**
Defines whether this line represents a refund that’s been applied or unapplied from a payment.

Possible values are:

**•** `Applied`

```
 UnappliedDate

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this refund line was unapplied from a payment.

When you’re ready to apply a refund’s balance to a payment, create a refund line ( `RefundLinePayment` ). The refund line represents
the balance taken from the payment and applied toward the invoice. You can apply a refund’s balance when you create the refund
record or afterward. The refund line must have the same currency as the parent refund.

A refund has an amount, which represents the total amount taken from the refund, and a balance, which represents the remaining
amount after the refund line has been applied to a payment. A refund’s amount can’t be less than the sum of all of its refund line amounts.
You can apply any portion of a refund’s balance to a payment.

You can apply a refund to transactions on the same account or to different transacations across different

accounts.

### RegisteredExternalService

Represents a registered external service used for checkout integrations by data integrators. This object is available in API version 49.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects RegisteredExternalService

Special Access Rules

The RegisteredExternalService object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
ConfigUrl

Description

DeveloperName

DocumentationUrl

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to the configuration page for the integration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the external service provider.

This field is available in API version 59.0 and later.

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

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to documentation for the registered external service.


Standard Objects RegisteredExternalService

**Field** **Details**

```
ExtensionPointName

ExternalServiceProviderId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field is available in API version 55.0 and later. Name of an extension point.

Possible values are:

**•** `Commerce_Domain_Cart_Calculate`

**•** `Commerce_Domain_Checkout_CreateOrder`

**•** `Commerce_Domain_Inventory_CartCalculator`

**•** `Commerce_Domain_Inventory_Service`

**•** `Commerce_Domain_OrderManagement_Product`

**•** `Commerce_Domain_Pricing_CartCalculator`

**•** `Commerce_Domain_Pricing_Service`

**•** `Commerce_Domain_Promotions_CartCalculator`

**•** `Commerce_Domain_Promotions_ShippingCalculator`

**•** `Commerce_Domain_Shipping_CartCalculator`

**•** `Commerce_Domain_Shipping_SplitShipment`

**•** `Commerce_Domain_Tax_CartCalculator`

**•** `Commerce_Domain_Tax_Service`

**•** `Commerce_Endpoint_Account_Address`

**•** `Commerce_Endpoint_Account_Addresses`

**•** `Commerce_Endpoint_Cart_Item` —This field value is available in API version
62.0 and later.

**•** `Commerce_Endpoint_Cart_ItemCollection` —This field value is available
in API version 62.0 and later.

**•** `Commerce_Endpoint_Catalog_Product`

**•** `Commerce_Endpoint_Catalog_Products`

**•** `Commerce_Endpoint_Search_ProductSearch`

**•** `Commerce_Endpoint_Search_Products`

**•** `Commerce_Endpoint_Search_ProductsByCategory`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of an Apex class functioning as a provider. The Apex class can either implement one
of the following interfaces:


Standard Objects RegisteredExternalService

**Field** **Details**

**•** sfdc_checkout.CartInventoryValidation

**•** sfdc_checkout.CartPriceCalculations

**•** sfdc_checkout.CartShippingCharges

**•** sfdc_checkout.CartTaxCalculations

[or the Apex class can extend one of the base classes for an extension. See Available Extensions.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)

```
ExternalServiceProviderType

IconUri

IsApplication

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of external service provider. For an extension, you set the type to `Extension`,
and you specify an `extensionPointName` . For example, for a Pricing Cart Calculator
extension, you specify `Commerce_Domain_Pricing_CartCalculator` as the
`extensionPointName` . For an integration, you set the type to one of the other possible
values, such as `Price`, and you omit `extensionPointName` .

Possible values are:

**•** `Extension` (this value is available in API version 55.0 and later)

**•** `Inventory`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URI of icon for the extension provider.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the extension provider is contained within a managed package.

The default value is `false` .

This field is available in API version 59.0 and later.


Standard Objects RegisteredExternalService

**Field** **Details**

```
Language

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language for labels displayed
in an application.

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
Create, Filter, Group, Sort, Update

**Description**
The primary label for the registered external service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects RelatedListColumnDefinition

**Field** **Details**

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

### RelatedListColumnDefinition

Represents information about a column in a related list. A related list specifies a set of records for a related object, based on specific
criteria. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Alias

ColumnSoql

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique alias of the column in the related list.

**Type**
string


Standard Objects RelatedListColumnDefinition

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query string used in a SELECT clause for the column.

```
DataType

DurableId

FieldDefinitionId

IsDefault

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The field type of the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FieldDefinition associated with the column, if applicable.

This is a relationship field.

**Relationship Name**
FieldDefinition

**Relationship Type**
Lookup

**Refers To**
FieldDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects RelatedListColumnDefinition

**Field** **Details**

**Description**
Indicates whether the column appears on the related list by default `(true)` or not
`(false)` .

The default value is `false` .

```
IsDescribable

Label

LookupId

RelatedListDefinitionId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in `describeLayout` call results `(true)`
or not `(false)` .

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lookup ID for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the RelatedListDefinition that contains the column.

This is a relationship field.

**Relationship Name**
RelatedListDefinition

**Relationship Type**
Lookup

**Refers To**
RelatedListDefinition


### Standard Objects RelatedListDefinition

Usage

**Find all available columns on a related list definition.**

```
     SELECT Alias, ColumnSoql, DurableId FROM RelatedListColumnDefinition WHERE

### `RelatedListDefinitionId = 'Account.Opportunities'` RelatedListDefinition

```

Represents information about a related list. A related list specifies a set of records for a related object, based on specific criteria. This
object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DefaultSort

DurableId

EntityDefinitionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The default sort string for the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects RelatedListDefinition

**Field** **Details**

**Description**
The ID of the entity containing the related list.

This is a relationship field.

**Relationship Name**
EntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

```
IsCustomizable

IsDescribable

IsLayoutable

Label

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether columns on the related list can be customized `(true)` or not `(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in `describeLayout` call results `(true)`
or not `(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can be assigned to a layout `(true)` or not `(false)` .

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the related list.


### Standard Objects RemoteKeyCalloutEvent

**Field** **Details**

```
ParentEntityDefinitionId

RelatedListId

RelatedListName

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ParentEntityDefinition that’s associated with the rows in the related list.

This is a relationship field.

**Relationship Name**
ParentEntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the related list in the API.

**Find all available related lists for a given entity, for example, an Account record.**

```
  SELECT DurableId, Label, RelatedListName FROM RelatedListDefinition WHERE

  ParentEntityDefinitionId = 'Account'

### RemoteKeyCalloutEvent

```

[The documentation has moved to RemoteKeyCalloutEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_remotekeycalloutevent.htm) _Platform Events Developer Guide_ .


### Standard Objects Reply Reply

Represents a reply that a user has submitted to a question in an answers zone.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Body

CommunityId

CreatorFullPhotoUrl

CreatorName

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Body of this reply.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the question and its reply. This field is available in API
version 27.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to
view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Reply

**Field** **Details**

**Description**

Name of the user who posted the question or reply. Only the first name of internal
users (agents) appears to portal users in the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later

```
CreatorSmallPhotoUrl

DownVotes

Name

NumReportAbuses

QuestionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of down votes for a reply.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
When creating a Reply, the `Name` field is automatically populated with a truncated,
plain text version of the Reply `Body` field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of reported abuses on the reply by users.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ReplyEmailSettings

**Field** **Details**

**Description**
ID of the Question to which this reply was made.

```
UpVotes

VoteTotal

```

Usage

Use this object to track replies to a Question.

### ReplyEmailSettings

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for a reply.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of all votes for a reply, including up and down votes.

Represents a reply mail management configuration, which is used to configure emails that are received by an email sending domain.
This object is available in API version 62.0 and later.

When you send an email campaign in Marketing Cloud, you often receive several replies to your messages, including unsubscribe
requests and automatic out-of-office replies. Reply mail management (RMM) reduces the time and effort required to review these
messages, and provide a better experience by automatically handling opt-outs and forwarding messages to the appropriate teams.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutoReplyMessage

```

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects ReplyEmailSettings

**Field** **Details**

**Description**

The content of the reply message. This reply is sent when a message is received at the sending
address.

```
DeveloperName

DomainName

FwdEmailAddress

IsAutoReplyEnabled

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The domain that the reply mail management settings apply to. This field is unique within
your organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address to forward a copy of each incoming message to. This value is honored
only if the value of `IsEmailForwardingEnabled` is `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ReplyEmailSettings

**Field** **Details**

**Description**

Indicates whether to forward automatic replies, such as out-of-office messages, to the address
specified in the `FwdEmailAddress` field. This value is honored only if the value of
`IsEmailForwardingEnabled` is `true` .

The default value is `false` .

```
IsDeleteAutoRepliesEnabled

IsEmailForwardingEnabled

IsUnsubscribeManualRequestsEnabled

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to delete automatic replies, such as out-of-office messages. This value is
honored only if the value of `IsEmailForwardingEnabled` is `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to forward email replies to the address specified in the
`FwdEmailAddress` field.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether subscribers can opt out of your campaigns by replying to your email with
a keyword such as `unsubscribe` .

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The combined language and locale ISO code, which controls the language of the
ReplyEmailSettings object.


### Standard Objects ReplyReportAbuse

**Field** **Details**

```
MasterLabel

### ReplyReportAbuse

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this ReplyEmailSettings value. This value is the internal label that doesn’t get
translated.

Represents a user-reported abuse on a Reply in a Chatter Answers zone. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

Reason

ReplyId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Reply from which the user reported abuse.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Reply, such as `Spam`, `Hateful`, or
`Inappropriate` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ReplyText

**Field** **Details**

**Description**
The ID of the Reply from which the user reported abuse.

Usage

Use this object to track user-reported abuse on replies created in a Chatter Answers zone.

### ReplyText

A text reply generated by Einstein Reply Recommendations that is based on closed chat transcripts. Admins review replies and publish
them to quick text, editing them as needed. Einstein recommends relevant published replies to support agents in the Lightning Service
Console, and agents can insert replies into chats or messaging sessions. This object is available in API version 49.0 and later.

Important: Because the replies generated by Einstein are taken from closed chats with your customers, they may contain customer
data. You can edit replies before they are recommended to agents.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   update()

```

Fields

**Field** **Details**

```
Language

Name

RawTextMessage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language used in the reply. This field is available in API version 51.0 and later. Possible
values are languages supported in Einstein Reply Recommendations.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Eight-digit auto-generated number identifying the reply.

**Type**
textarea


Standard Objects ReplyText

**Field** **Details**

**Properties**

**Description**
The text of the reply.

```
Source

Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates who last modified the reply.

Possible values are:

**•** `EINSTEIN_GENERATED` —Reply was generated by Einstein and has not been edited.

**•** `USER_EDITED` —Reply was generated by Einstein and then edited by a user.

**•** `USER_GENERATED` —This value is not currently in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the reply.

Possible values are:

**•** `NEW` —Einstein has generated the reply and it hasn’t yet been published.

**•** `PUBLISHED` —The reply has been published to quick text. When the reply
recommendation model is activated, the reply can be recommended to support agents.

**•** `PUBLISH_FAILED`  - An attempt to publish the reply to quick text failed. Publishing
failure can be due to validation errors, access errors, or corrupted files. To hide the reply
from the list of generated replies, delete it.

To get started with Einstein Reply Recommendations, create a predictive model that analyzes closed chats for frequently used text
snippets. When the model is ready, Einstein generates a list of these snippets as ReplyText records for you to review and publish, or
convert, to quick text. ReplyText records appear on the Einstein Reply Recommendations Setup page.

You can select one or more replies to publish at a time. If you publish a single reply, you can edit the reply text during publishing. If you
publish multiple replies at once, you can edit each reply’s text on the quick text page after publishing is complete. Replies aren’t
recommended to support agents until you activate your reply recommendation model.

When a reply is published, a corresponding QuickText record is created. During publishing, select a quick text folder to add the replies
to and make sure that agents have access to the folder. To edit a reply after it is published, edit the related quick text record.

Einstein generates the list of replies only once, when your model finishes building. It’s not possible to generate a new list.


### Standard Objects Report

**Copyright**

Rights of ALBERT EINSTEIN are used with permission of The Hebrew University of Jerusalem. Represented exclusively by Greenlight.

### Report

Represents a report, a set of data that meets certain criteria, displayed in an organized way. Access is read-only. This object is available
in API version 20.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Fields

**Field** **Details**

```
Description

DeveloperName

FolderName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the report. Limit: 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
### are reflected in a subscriber’s organization. Label is Report Unique Name .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects Report

**Field** **Details**

**Description**
Name of the folder that contains the report. Available in API version 35.0 and later.

```
Format

IsDeleted

LastReferencedDate

LastRunDate

LastViewedDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Indicates the format of the report. This field is available in API version 29.0 and
later. Can have one of these values:

**•** **Tabular** for reports in that format. In the application, the label is `Tabular` .

**•** **Summary** for reports in that format. In the application, the label is `Summary` .

**•** **Matrix** for reports in that format. In the application, the label is `Matrix` .

**•** **Multiblock** for reports in joined format. In the application, the label is `Joined` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
datetime

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
Returns the date the report was last run. Label is **Last Run** .

**Type**
datetime


Standard Objects Report

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
Name

NamespacePrefix

OwnerId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The report label used in the user interface.

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

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the folder that contains the report. There are 2 special folders:

**•** Private, where the ID is the user ID


Standard Objects Report

**Field** **Details**

**•** Public, where the ID is the org ID

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

Supported Query Scopes

Use these scopes to help specify the data your SOQL query returns.

**allPrivate**
Records saved in all users’ private folders.

[Requires the user permission "Manage All Private Reports and Dashboards" and Enhanced Analytics Folder Sharing. If your organization](https://help.salesforce.com/HTViewHelpDoc?id=analytics_sharing_enable.htm&language=en_US)
was created after the Summer ’13 release, you already have Enhanced Analytics Folder Sharing. Available in API version 36.0 and
later.

**created**
Records created by the user running the query.

**everything**
All records except records saved in other users’ private folders.

**mine**
Records saved in the private folder of the user running the query.

**organizationOwned**
Records saved in Unfiled Public Reports. In Lightning Experience, the Unfiled Public Reports folder is called Public Reports.

Usage

Use the report object to get report metadata. Query, search, or retrieve specific metadata on reports. Report object fields are read-only.

Example: Reports with “Sales” in Their Name

This SOQL query returns reports that contain the name “Sales” and lists their developer names, format, ID, and report name.

```
   SELECT DeveloperName,Format,Id,Name FROM Report WHERE Name LIKE '%Sales%'

```

Example: Reports in an Inactive User’s Private Folder

This SOQL query returns reports saved in a specific user’s private folder.

```
   SELECT Id FROM Report USING SCOPE allPrivate WHERE OwnerId = ‘005A0000000Bc2deFG’

```


### Standard Objects ReportEventLog

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ReportFeed**

Feed tracking is available for the object.

SEE ALSO:

ReportTag

Dashboard

### ReportEventLog

Report event logs contain information about what happened when a user ran a report. This event type includes all activity that's in the
Report Export event type, and additional information. For example, it has user activity for reports exported as both Formatted Report
and Details Only output. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AverageRowSize

BucketCount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average row size of all rows in the Report event, in bytes. A large average size, coupled
with a high `RowCount`, can indicate that a user is downloading information for fraudulent
purposes. For example, a salesperson who downloads all sales leads before departing for a
competitor. For example: `700` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ReportEventLog

**Field** **Details**

**Description**
The number of buckets that were used in the report.

```
ClientIp

ColumnCount

CpuTime

DatabaseBlocks

DatabaseCpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of columns in the report.

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


Standard Objects ReportEventLog

**Field** **Details**

```
DatabaseTotalTime

DisplayType

ExceptionFilterCount

LoginKey

ObjectName

```

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
The report display type, indicating the run mode of the report.

Possible values are:

**•** `D` —Dashboard

**•** `S` —Show Details

**•** `H` —Hide Details

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of exception filters that are used in the report.

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


Standard Objects ReportEventLog

**Field** **Details**

**Description**
The name of the object referenced by the report.

```
Origin

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context in which the report executed, such as from a UI (Classic, Lightning, Mobile),
through an API (synchronous, asynchronous, Apex), or through a dashboard.

Possible values are:

**•** `ReportOpenedFromMobileDashboard` : Report executed when a user clicked
a dashboard component on a mobile device and drilled down to a report.

**•** `DashboardComponentUpdated` : Report executed when a user refreshed a
dashboard component.

**•** `DashboardComponentPreviewed` : Report executed from a Lightning dashboard
component preview.

**•** `ReportRunUsingSynchronousApi` : Report executed from a synchronous API.

**•** `ReportRunUsingAsynchronousApi` : Report executed from an asynchronous
API.

**•** `ReportRunUsingApexSynchronousApi` : Report executed from the synchronous
Apex API.

**•** `ReportRunUsingApexAsynchronousApi` : Report executed from the
asynchronous Apex API.

**•** `ReportExported` : Report executed from a printable view or report export that was
not asynchronous nor an API export.

**•** `ReportRunFromClassic` : Report executed from the Run Report option of Salesforce
Classic.

**•** `ReportRunFromMobile` : Report executed from the Run Report option of the mobile
Salesforce app.

**•** `ReportRunFromLightning` : Report executed from the Run option in Lightning
Experience from a non-mobile browser.

**•** `ReportRunFromRestApi` : Report executed from REST API.

**•** `ReportPreviewed` : Report executed when a user got preview results while using
the report builder.

**•** `ReportScheduled` : Report was scheduled.

**•** `ProbeQuery` : Report executed from a probe query.

**•** `ReportRunFromReportingSnapshot` : Report executed through Snapshot
Analytics.

**•** `ReportExportedAsynchronously` : Report was exported asynchronously.


Standard Objects ReportEventLog

**Field** **Details**

**•** `ReportExportedUsingExcelConnector` : Report was exported using the
Excel connector.

**•** `ChartRenderedOnVisualforcePage` : Report executed from a rendered chart
on a VisualForce Page.

**•** `ChartRenderedInEmbeddedAnalyticsApp` : Report executed from a rendered
chart in an embedded Analytics app.

**•** `ReportRunAndNotificationSent` : Report executed through the notifications
API.

**•** `ChartRenderedOnHomePage` : Report executed from a rendered chart on the
home page.

**•** `ReportResultsAddedToWaveTrending` : Report executed when a user trended
a report in CRM Analytics.

**•** `ReportAddedToCampaign` : Report was added from an Add to Campaign action.

**•** `ReportResultsAddedToEinsteinDiscovery` : Report executed synchronously
from Einstein Discovery.

**•** `Unknown` : Report execution origin is unknown.

**•** `Test` : Report execution resulted from a test.

```
RenderingType

ReportIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the format of the report output in Salesforce Classic. If the report was exported in
Lightning Experience, this field is blank.

Possible values are:

**•** `W` : Web (HTML)

**•** `E` : Email

**•** `P` : Printable

**•** `X` : Excel

**•** `C` : Comma-separated values (CSV)

**•** `J` : JavaScript Object Notation (JSON)

**•** `D` : Dummy data

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the report that was run.


Standard Objects ReportEventLog

**Field** **Details**

```
RequestIdentifier

RequestStatus

RowCount

RunTime

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
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of rows that were processed in the Report event. High row counts, coupled
with a high `AverageRowSize`, can indicate that a user is downloading information for
fraudulent purposes. For example, a salesperson who downloads all sales leads before
departing for a competitor. For example: `150` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.


Standard Objects ReportEventLog

**Field** **Details**

```
SessionKey

SortOrder

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The sort column and order that was used in the report.

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


### Standard Objects ReportExportEventLog

**Field** **Details**

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

### ReportExportEventLog

Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports a
report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that data,
see the Report event type. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects ReportExportEventLog

Fields

**Field** **Details**

```
ClientInfo

ClientIp

CpuTime

LoginKey

ReportDescription

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the client that’s using Salesforce services.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

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

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the report that was run.

**Type**
string


Standard Objects ReportExportEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
RunTime

SessionKey

Timestamp

Uri

UserIdentifier

```

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


### Standard Objects ReportTag

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

### ReportTag

Associates a word or short phrase with a Report. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

```

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


### Standard Objects ReputationLevel

**Field Name** **Details**

```
Type

```

Usage

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

ReportTag stores the relationship between its parent TagDefinition and the Report being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

SEE ALSO:

Report

### ReputationLevel

Represents a reputation level defined for an Experience Cloud site. This object is available in API version 32.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.

Fields

**Field Name** **Details**

```
Label

```

**Type**
string


### Standard Objects ReputationLevelLocalization

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the reputation level.

```
LevelNumber

ParentId

Threshold

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The rank of the reputation level.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site the reputation level applies to.

**Type**
double

**Properties**
Filter, Sort

**Description**
The lower limit of reputation points associated with this reputation level. The
maximum number of reputation points a user can accrue is 999,999,999,999,999.

### ReputationLevelLocalization

Represents the translated value of a reputation level. Reputation level localization only applies for reputation levels in Experience Cloud
sites. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

This object is available only if digital experiences is enabled in your org and reputation is enabled in your Experience Cloud site.


Standard Objects ReputationLevelLocalization

Fields

**Field Name** **Details**

```
Language

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The language the reputation level is translated into. The picklist contains the
following fully-supported languages:

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

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


### Standard Objects ReputationPointsRule

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

### ReputationPointsRule

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the reputation level this translated value applies to.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the reputation level. Label is **Translation Text** .

Represents the reputation point rules for an Experience Cloud site. Each rule specifies an action that members can earn points from and
the points associated with those actions in a particular site. This object is available in API version 32.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.


Standard Objects ReputationPointsRule

Fields

**Field Name** **Details**

```
ParentId

Points

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site that the point rule applies to.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**

The reputation points associated with the member action this rule is for. The
maximum value this field can contain is 999,999.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The member action associated with this rule, limited to one of these actions:

**•** Write a post ( `FeedItemWriteAPost` )

**•** Write a comment ( `FeedItemWriteAComment` )

**•** Receive a comment ( `FeedItemReceiveAComment` )

**•** Like something ( `FeedItemLikeSomething` )

**•** Receive a like ( `FeedItemReceiveALike` )

**•** Share a post ( `FeedItemShareAPost` )

**•** Someone shares your post ( `FeedItemSomeoneSharesYourPost` )

**•** Mention someone ( `FeedItemMentionSomeone` )

**•** Receive a mention ( `FeedItemReceiveAMention` )

**•** Ask a question ( `FeedItemPostQuestion` )

**•** Answer a question ( `FeedItemAnswerAQuestion` )

**•** Receive an answer ( `FeedItemReceiveAnAnswer` )

**•** Mark an answer as best ( `FeedItemMarkAnswerAsBest` )

**•** Someone marks your answer as best
( `FeedItemYourAnswerMarkedBest` )

**•** Endorse someone for knowledge on a topic
( `EndorseSomeoneForKnowledgeOnATopic` )


### Standard Objects ResourceAbsence

**Field Name** **Details**

**•** Someone endorses you for knowledge on a topic
( `EndorsedForKnowledgeOnATopic` )

**•** Upload a profile picture ( `ProfilePhotoUpload` ) This action is available
in API version 45.0 and later.

### ResourceAbsence

Represents a time period in which a service resource is unavailable to work in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
AbsenceNumber

Address

City

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the absence.

**Type**
address

**Properties**
Filter

**Description**
The compound form of the address associated with the absence.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ResourceAbsence

**Field Name** **Details**

**Description**
The city of the address associated with the absence. Maximum length is 40
characters.

```
Country

Description

End

GeocodeAccuracy

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the absence.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence ends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates. This field is available in the API only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last modified. Its label in the user
interface is `Last Modified Date` .


Standard Objects ResourceAbsence

**Field Name** **Details**

```
LastViewedDate

Latitude

Longitude

Postal Code

ResourceId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the absence. Maximum length is
20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The absent service resource.


Standard Objects ResourceAbsence

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
Resource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
Start

State

Street

Type

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the address associated with the absence.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The type of absence: _`Meeting`_, _`Training`_, _`Medical`_, or _`Vacation`_ . The
default value is _`Vacation`_ . You can add custom values if needed, but the name
_`Break`_ is reserved for the Field Service managed package.


### Standard Objects ResourcePreference

Usage

Resource absences you define periods of time when a service resource is unavailable to work. Unless you’re using the Field Service
managed package, service resources can still be assigned to appointments that conflict with their absences.

Tip: Create a trigger that sends an approval request to a supervisor when a service resource creates an absence.

If you’re not using the Field Service managed package, a calendar view isn’t available for individual service resources.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ResourceAbsenceChangeEvent (API version 48.0)**
Change events are available for the object.

**ResourceAbsenceFeed**

Feed tracking is available for the object.

**ResourceAbsenceHistory**

History is available for tracked fields of the object.

### ResourcePreference

Represents an account’s preference for a specified service resource on field service work.

Resource preferences indicate which service resources can be assigned to field service work. You can designate service resources as
preferred, required, or excluded on specific accounts, assets, locations, work orders, or work order line items. Work orders inherit their
associated account’s resource preferences.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ResourcePreference

**Field Name** **Details**

**Description**
The date when the resource preference was last modified.

```
LastViewedDate

PreferenceType

RelatedRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource preference was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Resource preference type. Values include:

**•** Preferred: Indicates that the customer would like their field service work
assigned to the resource.

**•** Required: Indicates that the resource must be assigned to the customer’s
field service work.

**•** Excluded: Indicates that the customer doesn’t want their field service work
assigned to the resource.

Resource preferences serve more as a suggestion than a requirement. You can
still assign a service appointment to any resource regardless of the related work
order’s resource preferences.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The work order or account with the resource preference.

This field is a polymorphic relationship.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Accounts, Assets, Locations, Work Orders, or Work Order Line Items


### Standard Objects RestApiEventLog

**Field Name** **Details**

```
ResourcePreferenceNumber

ServiceResourceId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the resource preference.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that is preferred, required, or excluded.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ResourcePreferenceChangeEvent (API version 54.0)**
Change events are available for the object.

**ResourcePreferenceFeed**

Feed tracking is available for the object.

**ResourcePreferenceHistory**

History is available for tracked fields of the object.

### RestApiEventLog

REST API event logs contain details about REST-specific requests. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects RestApiEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

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


Standard Objects RestApiEventLog

**Field** **Details**

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

```
ExceptionMessage

FieldCount

LoginKey

MediaType

Method

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The exception message for a REST API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

**Type**
double

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


Standard Objects RestApiEventLog

**Field** **Details**

**Description**
The HTTP method of the request. For example: `GET`, `POST`, `PUT`, and so on.

```
ObjectName

RequestIdentifier

RequestSize

RequestStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request. For example: `Account`,
`Opportunity`, `Contact`, and so on.

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
The size of the callout response, in bytes.

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


Standard Objects RestApiEventLog

**Field** **Details**

This field can have a blank value.

```
ResponseSize

RowsProcessed

RunTime

SessionKey

StatusCode

Timestamp

```

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
Numbers of rows that are processed by the REST API.

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
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP response status code for the request.

**Type**
dateTime


Standard Objects RestApiEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Uri

UserIdentifier

UserType

```

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

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.


### Standard Objects RetentionStoreUsage

**Field** **Details**

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### RetentionStoreUsage

Represents the total usage of the org's retention store measured at specific points in time. This object is available in API version 66.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AttributeDetail

MetricType

Name

```

**Type**
textarea

**Properties**
Nillable

**Description**
(For future use) Additional metadata or contextual details about the usage measurement.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Categorizes the type of usage being measured. Only DATA type is currently captured.

**•** `DATA` : Total storage capacity usage (in bytes).

**•** `FILES` : Files and attachments storage capacity usage (in bytes).

**•** `RECORDS` : Retained record count (in rows).

Only DATA type is currently captured.

**Type**
string


Standard Objects RetentionStoreUsage

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the retention storage usage record.

```
OwnerId

RetentionType

UnitOfMeasure

Usage

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the account owner associated with the storage.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Identifies which retention system this usage record belongs to.

Possible values are:

**•** `ARCHIVE`

**•** `PRIVACY_CENTER`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the unit of measurement for the Usage field value.

Possible values are:

**•** `BYTES`

**•** `ROWS`

**Type**
long


### Standard Objects ReturnOrder

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The numeric usage value in the unit of measure specified in `UnitOfMeasure` .

```
UsageDateTime

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the usage measurement was captured.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RetentionStoreUsageOwnerSharingRule on page 65**
Sharing rules are available for the object.

**RetentionStoreUsageShare on page 67**
Sharing is available for the object.

### ReturnOrder

Represents the return or repair of inventory or products in Field Service, or the return of order products in Order Management. This object
is available in API version 42.0 and later.

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Order Management must be enabled. If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category Activated. The default Statuses corresponding to Activated are Submitted
and Approved.


Standard Objects ReturnOrder

Fields

**Field Name** **Details**

```
AccountId

CaseId

ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the return order.

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
The case associated with the return order.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the return order.

This is a relationship field.

**Relationship Name**
Contact


Standard Objects ReturnOrder

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
CurrencyIsoCode

Description

DestinationLocationId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the
currency of the OrderSummary associated with the ReturnOrder.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup


Standard Objects ReturnOrder

**Field Name** **Details**

**Refers To**
Location

```
ExpectedArrivalDate

ExpirationDate

GrandTotalAmount

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the items are expected to arrive at the destination location.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Authorizations can’t be captured after their expiration dates.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges
on the return order. This includes all return order line items associated with the
return order. This amount is equal to TotalAmount + TotalTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
The date when the return order was last viewed.

```
LifeCycleType

OrderId

OrderSummaryId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the order summary is managed by Salesforce Order
Management (MANAGED) or by an external system (UNMANAGED). An
unmanaged order summary is stored in Salesforce for reference purposes.

**•** Some Order Management APIs reject input records that are associated with
unmanaged order summaries.

**•** Order Management does not update financial bucket fields on some records
that are associated with unmanaged order summaries.

**•** A user with the EditUnmanagedOrderSummaries or B2BCommerceIntegrator
permission can edit certain fields on objects related to unmanaged order
summaries that are normally only accessible via APIs.

Possible values are:

**•** `MANAGED` —Managed

**•** `UNMANAGED` —Unmanaged

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order associated with the return order. When you associated a return order
with an order, you can associate the return order’s line items with order products.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order summary associated with the return order.

This field is available in API version 50.0 and later.

```
OwnerId

ProductRequestId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the return order.

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
The product request associated with the return order. When you associated a
return order with a product request, you can associate the return order’s line
items with the product request’s line items.

A return order might be related to a product request if the return order tracks
the return of unused products or products to be repaired or replaced. For example,
a technician creates a product request for three motors to prepare for a field visit.
If the technician finds that only two motors are needed, they can create a return
order to return the third to the original location, and list the product request in
this field.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest


Standard Objects ReturnOrder

**Field Name** **Details**

This field is available only if Field Service or Health Cloud is enabled.

```
ProductServiceCampaignId

RefundInstructionsHint

ReturnOrderNumber

ReturnedById

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the return order

This field is available only if Field Service is enabled.

**Type**
textarea

**Properties**
Nillable

**Description**
Stores a JSON representation of the payment credit and refund sequences for
ensure credit, ensure refund, and the change orders associated with it.

This field is available in API version 65.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the return order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user returning the items.

This is a relationship field.

**Relationship Name**
ReturnedBy

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects ReturnOrder

**Field Name** **Details**

```
ShipFromAddress

ShipFromCity

ShipFromCountry

ShipFromGeocodeAccuracy

ShipFromLatitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The return shipping address. This address tracks the location of the items at the
start of the return or repair. For example, if a customer is returning an item, the
Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the return shipping address. This address tracks the location of
the items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the return shipping address. See Compound
Fields Considerations and Limitations for details on geolocation compound fields.
This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Used with Longitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places. See Compound Fields Considerations and Limitations for details
on geolocation compound fields. This field is available in the API only.

```
ShipFromLongitude

ShipFromPostalCode

ShipFromState

ShipFromStreet

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places. See Compound Fields Considerations and Limitations for details
on geolocation compound fields. This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the return shipping address. This address tracks the location
of the items at the start of the return or repair. For example, if a customer is
returning an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.


Standard Objects ReturnOrder

**Field Name** **Details**

```
ShipmentType

SourceLocationId

Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment associated with the return order. Available values are:

**•** `Standard` (default value)

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

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
The status of the return order. Available values are:

**•** `Draft`

**•** `Submitted`

**•** `Approved`

**•** `Canceled`

**•** `Closed`


Standard Objects ReturnOrder

**Field Name** **Details**

If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category `Activated` .
The default Statuses corresponding to Activated are Submitted and Approved.

```
StatusCategory

TaxLocaleType

TotalAmount

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status category of the return order. Processing of the return order depends on
this value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `Activated`

**•** `Canceled`

**•** `Closed`

**•** `Draft`

**•** `Pending`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original order associated with the return
order. Gross usually applies to taxes like value-added tax (VAT), and Net usually
applies to taxes like sales tax.

Possible values are:

**•** `Automatic` (displays most prices and taxes as combined values)

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the return order line items, including products,
fees, and delivery charges, on the ReturnOrder.


Standard Objects ReturnOrder

**Field Name** **Details**

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalDeliveryAdjustAmount

TotalDeliveryAdjustAmtWithTax

TotalDeliveryAdjustTaxAmount

TotalDeliveryAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order. This value only includes adjustments to return order line items of
type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order, inclusive of tax. This value only includes adjustments to return order
line items of type code Charge. This amount is equal to
TotalDeliveryAdjustAmount + TotalDeliveryAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjustAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Total of the delivery charges on the return order. This value only includes return
order line items of type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalDeliveryAmtWithTax

TotalDeliveryTaxAmount

TotalFeeAdjustAmount

TotalFeeAdjustAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the return order, inclusive of tax. This
value only includes return order line items of type code Charge. This amount is
equal to TotalDeliveryAmount + TotalDeliveryTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the return order.
This value only includes adjustments to return order line items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Total amount of the price adjustments applied to the fees on the return order,
inclusive of tax. This value only includes adjustments to return order line items
of type Fee. This amount is equal to TotalFeeAdjustAmount +
TotalFeeAdjustTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

```
TotalFeeAdjustTaxAmount

TotalFeeAmount

TotalFeeAmtWithTax

TotalFeeTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjustAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the fees on the return order. This value only includes return order line
items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the fees on the return order, inclusive of tax. This value only
includes return order line items of type Fee. This amount is equal to
TotalFeeAmount + TotalFeeTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

```
TotalProductAdjustAmount

TotalProductAdjustAmtWithTax

TotalProductAdjustTaxAmount

TotalProductAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order. This value only includes adjustments to return order line items of type
code Product.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order, inclusive of tax. This value only includes adjustments to return order line
items of type code Product. This amount is equal to TotalProductAdjustAmount
+ TotalProductAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Total of the product charges on the return order. This value only includes return
order line items of type code Product.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalProductAmtWithTax

TotalProductTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the product charges on the return order, inclusive of tax. This
value only includes return order line items of type code Product. This amount is
equal to TotalProductAmount + TotalProductTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.


Standard Objects ReturnOrder

Usage

You can use return orders to track customer returns, customer repairs, or the return of inventory from a technician’s van stock to a
warehouse or supplier. Customers can initiate a return from a community, or agents can create return orders in response to a customer
call or technician request.

Return orders are composed of return order line items, which allow you to add details about the items being returned. To represent the
returned items, each line item must list one or more of the following: product, product item, asset, product request line item, and order
product. Return orders can be associated with a product request, case, account, contact, and order if needed. This versatility lets you use
return orders to track a wide range of return scenarios.

Example

```
   {

     "RefundInstructionsHint": {

      "PaymentCreditSequence": [

       {

        "OrderPaymentSummaryId": "0bMxx0000000000001",

        "Amount": 50,

        "CreditType": "GIFT_CARD",

        "Rank": 1

       },

       {

        "OrderPaymentSummaryId": "0bMxx0000000000002",

        "Amount": 50,

        "CreditType": "CHECK",

        "Rank": 2

       }

      ]

     },

     "RefundSequence": [

      {

       "OrderPaymentSummaryId": "0bMxx0000000000001",

       "Amount": 50,

       "Rank": 1

      },

      {

       "OrderPaymentSummaryId": "0bMxx0000000000002",

       "Amount": 50,

       "Rank": 2

      }

     ],

     "ChangeOrders": [

      {

       "ChangeOrderId": "801xx000003Gd01111",

       "FeeChangeOrderId": null,

       "NetAmount": -75

      }

     ]

   }

```


### Standard Objects ReturnOrderItemAdjustment

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderFeed**

Feed tracking is available for the object.

**ReturnOrderHistory**

History is available for tracked fields of the object.

**ReturnOrderOwnerSharingRule**

Sharing rules are available for the object.

**ReturnOrderShare**

Sharing is available for the object.

### ReturnOrderItemAdjustment

Represents a price adjustment on a return order line item. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Order Management must be enabled.

Fields

**Field** **Details**

```
Amount

Description

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects ReturnOrderItemAdjustment

**Field** **Details**

**Description**
Description of the adjustment.

```
OrderItemAdjustLineSummaryId

ReturnOrderId

ReturnOrderItemAdjustmentNumber

ReturnOrderLineItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item adjustment line summary associated with the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order associated with the return order line item to which the adjustment
applies.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order line item to which this adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem


### Standard Objects ReturnOrderItemTax

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

```
TotalAmtWithTax

TotalTaxAmount

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.

### ReturnOrderItemTax

Represents the tax on a return order line item or return order item adjustment. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Order Management must be enabled.


Standard Objects ReturnOrderItemTax

Fields

**Field** **Details**

```
Amount

Description

OrderItemTaxLineItemSummaryId

Rate

ReturnOrderId

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the return order item tax.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the return order item tax.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item tax line item summary associated with the order item summary that
corresponds to the return order line item to which the tax applies.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Tax rate used to calculate the Amount.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated return order.

This is a relationship field.

**Relationship Name**
ReturnOrder


Standard Objects ReturnOrderItemTax

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

```
ReturnOrderItemAdjustmentId

ReturnOrderItemTaxNumber

ReturnOrderLineItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this object represents a tax on an adjustment, this value is the ID of the return order item
adjustment to which the tax applies. If this value is null, the adjustment applies to a return
order line item.

This is a relationship field.

**Relationship Name**
ReturnOrderItemAdjustment

**Relationship Type**
Lookup

**Refers To**
ReturnOrderItemAdjustment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item tax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents a tax on a return order line item, this value is the ID of that return
order line item. If this object represents a tax on an adjustment, this value is the ID of the
return order line item to which the adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup


### Standard Objects ReturnOrderLineItem

**Field** **Details**

**Refers To**
### ReturnOrderLineItem

```
TaxEffectiveDate

Type

```

Associated Objects

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows whether the amount on the tax line is an estimate or the final calculated amount.
Doesn’t set a value by default. Users can define automation to set and change the value as
needed.

Possible values are:

**•** `Actual`

**•** `Estimated`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.

### ReturnOrderLineItem

Represents a specific product that is returned or repaired as part of a return order in Field service, or a specific order item that is returned
as part of a return order in Order Management. This object is available in API version 42.0 and later.

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ReturnOrderLineItem

Special Access Rules

Field Service or Order Management must be enabled.

Fields

**Field Name** **Details**

```
AssetId

ChangeOrderItemId

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the return order line item. One or more of the following
fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId, and
ProductRequestLineItemId.

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
Create, Filter, Group, Nillable, Sort

**Description**
ID of the change order item associated with the return order line item.

This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
ChangeOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for the currency of the original Order associated with the
ReturnOrderLineItem.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

```
Description

DestinationLocationId

GrossUnitPrice

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
Unit price, including tax, of the product represented by the associated order item
summary.

This field is available in API version 50.0 and later.

```
LastReferencedDate

LastViewedDate

OrderItemId

OrderItemSummaryId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
OrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
ID of the order item summary associated with the return order line item.

This field is available in API version 50.0 and later.

```
ProcessingPlan

Product2Id

ProductItemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the preferred fate of the items following their return. Available values
are:

**•** `Repair` —Repair the items and return them to the owner

**•** `Discard` —Discard the items

**•** `Salvage` —Salvage the items’ working parts

**•** `Restock` —Return the items to your inventory

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product item representing the location of the product at the start of the
return. One or more of the following fields must be filled out: AssetId, OrderItemId,
Product2Id, ProductItemId, and ProductRequestLineItemId.

This is a relationship field.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

```
ProductRequestLineItemId

ProductServiceCampaignId

ProductServiceCampaignItemId

QuantityExpected

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product request line item associated with the return order line item. One or
more of the following fields must be filled out: AssetId, OrderItemId, Product2Id,
ProductItemId, and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product service campaign associated with the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the return order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
The quantity of items expected to be returned.

This field is available in API version 50.0 and later.

```
QuantityReceived

QuantityRejected

QuantityReturned

QuantityUnitOfMeasure

ReasonForRejection

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual quantity of items received for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity of items rejected for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of items being returned. If multiple types of products are being
returned, track each product in a different return order line item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the returned items; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
Reason for rejecting returned items on this return order line item.

Possible values are:

**•** `Damaged Item`

**•** `Expired Warranty`

**•** `Missing Item or Part`

**•** `Wrong Item`

The default value is `Missing Item or Part` .

This field is available in API version 50.0 and later.

```
ReasonForReturn

ReasonForChangeText

RepaymentMethod

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the items are being returned. Available values are:

**•** `Damaged`

**•** `Defective`

**•** `Duplicate Order`

**•** `Wrong Item`

**•** `Wrong Quantity`

**•** `Not Satisfied`

**•** `Outdated`

**•** `Other`

The default value is `Damaged` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Details about the reason for return change

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
The method by which the customer or owner will be reimbursed for the items
being returned. Available values are:

**•** `Replace` —The items will be replaced

**•** `Refund` —The items will be returned and the owner will be refunded

**•** `Credit` —The items will be returned and the owner will receive credit for
them

**•** `Return` —The items will be returned to the owner (for example, following
their repair)

```
ReturnOrderId

ReturnOrderLineItemNumber

SourceLocationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The return order that the return order line item belongs to.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number that identifies the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

This is a relationship field.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

```
TotalAdjustmentAmount

TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

TotalAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all price adjustments applied to the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the return order line item,
inclusive of tax. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
Total, including adjustments and tax, of the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalLineAmount

TotalLineAmountWithTax

TotalLineTaxAmount

TotalPrice

```

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total, not including adjustments or tax, of the return order line item.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the return order line item, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the return order line item. Equal to
UnitPrice times Quantity.

This is a calculated field.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

```
TotalTaxAmount

Type

TypeCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the return order line item. Matches the type of the associated order item
summary. Delivery Charge indicates that the return order line item represents a
delivery charge. Fee indicates that it represents another type of fee, such as a
return fee. Order Product indicates that it represents any other type of product,
service, or charge. Each type corresponds to one type code, shown here in
parentheses.

Possible values are:

**•** `Delivery Charge (Charge)`

**•** `Fee (Charge)` This value is available in API v56.0 and later.

**•** `Order Product (Product)`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type code of the return order line item. Matches the type code of the associated
order item summary. Processing depends on this value. Charge indicates that
the return order line item represents a delivery charge. Product indicates that it
represents an other type of product, service, or charge. Each type category
corresponds to one or more types.

Possible values are:

**•** `Charge`

**•** `Product`

This field is available in API version 50.0 and later.


### Standard Objects ReturnOrderOwnerSharingRule

**Field Name** **Details**

```
UnitPrice

```

Associated Objects

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Unit price of the return order line item.

This field is available in API version 50.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderLineItemFeed**

Feed tracking is available for the object.

**ReturnOrderLineItemHistory**

History is available for tracked fields of the object.

### ReturnOrderOwnerSharingRule

Represents the rules for sharing a return order with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 42.0 and later.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.


Standard Objects ReturnOrderOwnerSharingRule

Fields

**Field** **Details**

```
Description

DeveloperName

GroupId

Name

ServiceResourceAccessLevel

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A return order owned by a User in the source Group
triggers the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
picklist


### Standard Objects RevenueAsyncOperation

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### RevenueAsyncOperation

Represents the status of an asynchronous process initiated by a REST request in Subscription Management. This object is available in
API versions 57.0 to 59.0. Use AsyncOperationTracker instead of RevenueSyncOperation in API version 59.0 and later.

For example, `asset-management/assets/collection/actions/initiate-amend-quantity` creates a
### RevenueAsyncOperation record when it initiates an asynchronous process. The ID of the record is returned in the REST response.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.

Fields

**Field** **Details**

```
AsyncOperationNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects RevenueAsyncOperation

**Field** **Details**

**Description**
A unique identifier for this revenue async operation record.

```
CorrelationIdentifier

ExpiresAt

FailedJobItems

FinishedAt

JobType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the API request associated with this revenue async operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items that weren’t successfully processed by the sync operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The REST request that initiated the asynchronous process.

Valid values are:

**•** `ASMAdServerCheckAvailability`

**•** `ASMAdServerIntegration`

**•** `ASMApplyMediaPlanTemplateJob`


Standard Objects RevenueAsyncOperation

**Field** **Details**

**•** `ASMApplyTargetingTemplateJob`

**•** `ASMBulkEditLineItemDetail` . This field is available in API version 67.0 and
later.

**•** `ASMCalcLinearMediaSpotPrc` . This field is available in API version 66.0 and
later.

**•** `ASMCreateAmendQuoteJob`

**•** `ASMFileProcessorJob` . This field is available in API version 66.0 and later.

**•** `ASMLinearSpotGenerationJob` . This field is available in API version 67.0 and
later.

**•** `ASMMediaPlanAsTemplate`

**•** `ASMMediaPlanClone`

**•** `ASMMediaPlanCopyJob`

**•** `AbandonedCart` . This field is available in API version 67.0 and later.

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion`

**•** `AutomaticRefunds`

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `CreditMemoRecovery` . This field is available in API version 66.0 and later.

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`

**•** `InvoicedDocgenJob`

**•** `InvoicedDocgenPostProcessJob`

**•** `InvoicedDocfenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `InvoiceEstimatedTaxCallout`

**•** `LoadSalesRecipientData` . This field is available in API version 66.0 and later.

**•** `MultisiteAutoQuote` . This field is available in API version 66.0 and later.

**•** `PST Base Job - Top-Level`

**•** `PSTConfig - Configuration`

**•** `PSTPersist - Save`

**•** `PSTPrice - Price`

**•** `PearAmendQtyAssets`

**•** `PearCancelAssets`

**•** `PearRenewAssets`

**•** `PersonalizationRecommender` . This field is available in API version 67.0 and
later.

**•** `PlaceOrder`


Standard Objects RevenueAsyncOperation

**Field** **Details**

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PostOrderCampaign` . This field is available in API version 67.0 and later.

**•** `PlaceQuote`

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment`

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `SmsDltTemplateIngestion` . This field is available in API version 66.0 and later.

**•** `StandaloneBillingSchedulesCreation`

**•** `StatementOfAccountGeneration` . This field is available in API version 66.0 and
later.

**•** `TestSerialMessageStepJob`

**•** `TransactionLineBom`

**•** `VoidCreditMemo` . This field is available in API version 66.0 and later.

**•** `energyAgreementSetup` . This field is available in API version 66.0 and later.

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.


Standard Objects RevenueAsyncOperation

**Field** **Details**

```
ParentOperationId

ReferenceEntityId

StartedAt

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

This field is a relationship field.

**Relationship Name**
ParentOperation

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a polymorphic field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
CreditMemo, Order, Product2, Quote

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when Salesforce started the asynchronous process.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**Description**
The status of the asynchronous process.

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures`

**•** `Failure`

**•** `InProgress`

**•** `Submitted`

```
SubmittedAt

SuccessfulJobItems

TotalJobItems

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items successfully processed by the sync operation.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of items processed by the sync operation, including both successfully
processed items and failed items.

### RevenueTransactionErrorLog

Contains information about errors that occurred while processing a request. The error record persists until another error with the same
category, primary record, and (optionally) related record occurs. This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects RevenueTransactionErrorLog

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_revenuetransactionerrorlog.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_revenuetransactionerrorlog.htm)

Fields

**Field** **Details**

```
AsyncOperationTrackerId

BillingScheduleGroupId

Category

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the async operation tracker record created by the request. Async operation tracker
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
AsyncOperationTracker

**Relationship Type**
Lookup

**Refers To**
AsyncOperationTracker

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the group related to the billing schedule with errors. This field is available in API
version 64.0 and later.

This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Refers To**
BillingScheduleGroup

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**Description**
Provides context about the source of error. For example, if an error occurs while processing
an `/assets/collection/actions/initiate-cancellation` request, the
category is `InitiateCancel` .

Valid values are:

**•** `ApplyAPI`

**•** AutomatedNegativeInvoiceLineConversion

**•** AutomaticRefunds

**•** `ConvertNegativeInvoiceLineToCredit` —Available in API version 56.0
and later.

**•** `Core Invoice Generation Failure`

**•** `CreditInvoiceAPI`

**•** `CreditMemoRecoveryApi` —Available in API version 66.0 and later.

**•** `CreditTaxIntegrationAPI`

**•** `BulkCurrencyConversion` —Available in API version 66.0 and later.

**•** `InitiateAmendment` —Available in API version 56.0 and later.

**•** `InitiateCancel`

**•** `InitiateRenewal`

**•** `InsufficientAccess` —Insufficient Access to start invoice run.

**•** `InvoiceBatchRun`

**•** `InvoiceBatchRunDebitConversion` —Available in API version 66.0 and later.

**•** `InvoiceBatchRunInvoiceGeneration`

**•** `InvoiceBatchRunPostProcessor`

**•** `InvoiceBatchRunPreProcessor`

**•** `InvoiceBatchRunRecovery`

**•** `InvoiceBatchRunSelectionStep`

**•** `InvoiceBatchRunSplitInvoiceGeneration` —Available in API version
66.0 and later.

**•** `InvoiceBatchRunSummarizer`

**•** `InvoiceBatchRunTaxProcessor`

**•** `MaterialLineGeneration` —Available in API version 58.0 and later.

**•** `Invalid Tax API Input`

**•** `Invalid Tax Integration Input`

**•** `LoadSalesRecipientData` —Available in API version 66.0 and later.

**•** `OrderTaxCalculationFailure` —Available in API version 61.0.

**•** `OrderToAsset`

**•** `OrderItemToAsset` —Available in API version 59.0 and later.

**•** `OrderToBillingSchedule`

**•** `PaymentSale`


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**•** `PaymentScheduleGeneration` —Available in API version 56.0 and later

**•** `ProcessAutoQuote` —Available in API version 66.0 and later.

**•** `PstBaseStepFailure` —Available in API version 66.0 and later.

**•** `QuotePriceCalculationFailure` —Available in API version 61.0.

**•** `QuoteTaxCalculationFailure` —Available in API version 61.0.

**•** `QuoteToOrder` —Available in API version 56.0 and later.

**•** `Post Tax API Failure`

**•** `Post-Credit Tax Failure`

**•** `Pre-Credit Tax Failure`

**•** `SetupEnergyAgreement` —Available in API version 66.0 and later.

**•** `StandaloneCreditAPI`

**•** `StatementOfAccountGeneration` —Available in API version 66.0 and later.

**•** `Tax API Failure`

**•** `TransactionToContract` —Available in API version 59.0 and later.

**•** `Unknown Failure` —Available in API version 56.0 and later.

**•** `VoidCreditMemo` —Available in API version 66.0 and later.

**•** `VoidPostedInvoiceAPI`

```
ConfiguratorErrorMessage

ErrorCode

ErrorLogNumber

```

**Type**
textarea

**Properties**
Nillable

**Description**
The text of the error message. This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code; for example, INVALID_INPUT.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated unique ID that identifies the error.


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

```
ErrorMessage

OwnerId

PrimaryRecord2Id

PrimaryRecordId

```

**Type**
textarea

**Description**
Contains information about the error and how to resolve it.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who made the request that resulted in the creation of the error log.

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
The ID of the record that’s associated with this error. For example, if the error occurred while
creating an invoice line from an order line, the primary2 ID is the ID of the order line. This
field is available in API version 66.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryRecord2

**Refers To**
Account, CreditMemoInvApplication, CreditMemoLine, CreditMemoLineInvoiceLine,
CreditMemoLineTax, DebitMemo, DebitMemoLine, InvoiceLine, InvoiceLineTax,
LegalEntyAccountingPeriod, Order, PaymentLineInvoice, PaymentLineInvoiceLine,
RefundLinePayment

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**Description**
The ID of the record that’s associated with this error. For example, if the error occurred while
creating an invoice from an order, the primary ID is the ID of the order.

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryRecord

**Relationship Type**
Lookup

**Refers To**
Asset, BillingBatchScheduler, BillingSchedule, CardPaymentMethod, CreditMemo, Invoice,
InvoiceBatchRun, InvoiceBatchRunRecovery, Order, Payment, PaymentBatchRun,
PaymentGateway, Quote, Refund

```
PrimaryTextRecord

RelatedRecord2Id

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier of the primary record associated with the error log. For example, if the error
occurred while creating an invoice from an order, the primary text Record ID is the ID of the
order.

There are two other fields in the same entity, PrimaryRecord and PrimaryRecord2, that are
polymorphic fields, so they’re limited to storing IDs from objects in their respective domains.
Use this text field for all objects. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Optional. The ID of a record that can provide additional context about the error. For example,
if `PrimaryRecord2Id` is the ID of an invoice line, this field could be the ID of an invoice
line tax. This field is available in API version 66.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord2

**Refers To**
CreditMemoLine, CreditMemoLineInvoiceLine, CreditMemoLineTax, DebitMemo,
GeneralLedgerAccount, GeneralLedgerAcctAsgntRule, InvoiceLine, InvoiceLineTax, Payment,
PaymentLineInvoice, PaymentLineInvoiceLine, Refund, RefundLinePayment


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

```
RelatedRecordId

Request

RequestIdentifier

RevenueAsyncOperationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. The ID of a record that can provide additional context about the error. For example,
if `PrimaryRecordId` is the ID of an order, this field could be the ID of an order item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
BillingBatchScheduler, BillingSchedule, BillingScheduleGroup, CreditMemo, CreditMemoLine,
Invoice, InvoiceLine, OrderItem, Payment, PaymentSchedule, PaymentScheduleItem,
QuoteLineItem, Refund

**Type**
textarea

**Properties**
Nillable

**Description**
Optional. A field providing additional information linking the error with the request. This
field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID returned by the request. Use this ID to identify the revenue transaction error
log records for a specific request. This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the revenue async operation record created by the request. Revenue async operation
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 57.0 and later.

This field is a relationship field.


### Standard Objects RpaFlowResultEvent

**Field** **Details**

**Relationship Name**
RevenueAsyncOperation

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation

```
Severity

### RpaFlowResultEvent

```

Reserved for future use.

### RpaRobot

Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The severity type for the error message. This field is available in API version 66.0 and later.

Valid values are:

**•** `Error`

**•** `Warning`

### RpaRobotAsgnMaintWindow

Reserved for future use.

### RpaRobotAsgnSessionInf

Reserved for future use.

### RpaRobotDefinition

Reserved for future use.


### Standard Objects RpaRobotMaintWindow RpaRobotMaintWindow

Reserved for future use.

### RpaRobotMaintWindowDef

Reserved for future use.

### RpaRobotPool

Reserved for future use.

### RpaRobotPoolAsgnRobot

Reserved for future use.

### RpaRobotPoolDefinition

Reserved for future use.

### RpaRobotPoolFlowAsgn

Reserved for future use.

### RpaRobotSessionInfo

Reserved for future use.

### RpaRobotSessionInfoDef

Reserved for future use.

### RuleTerritory2Association

Represents a record-assignment rule and its association to an object, such as Account. Available if Sales Territories has been enabled.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


### Standard Objects SalesAIScoreCycle

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
IsInherited

RuleId

Territory2Id

### SalesAIScoreCycle

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the rule is an _inherited_ rule ( `true` ) or a _local_ rule ( `false` ).
Rule inheritance flows from the parent territory where the rule is created to the
rule’s descendent territories (if any) in the territory model hierarchy. A local rule
is created within a single territory and affects that territory only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory where the rule was created.

Represents the cycle type and ID used to score records. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


### Standard Objects SalesAIScoreModelFactor

Special Access Rules

To see score cycle information, users need a Sales Cloud Einstein license with the View Scoring Model Factors permission enabled. The
permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field** **Details**

```
CycleType

Name

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The cycle used to create scores on opportunity records can be one of two types.

**•** `OpportunityScoreModeling` —Provides model factors, which Sales Cloud
Einstein uses to build a scoring model.

**•** `OpportunityScoreScoring` —Provides scores and key factors to individual
records, which are based on Sales Cloud Einstein’s scoring model.

Note: When the value `OpportunityScoreModeling` is returned, use the
Sales AI Score Model Factor object to get information about the model factors.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the cycle. Currently, the name is a system-generated unique value.

### SalesAIScoreModelFactor

Represents the factors that Sales Cloud Einstein uses to build a scoring model. Scoring models are used by features, such as Opportunity
Scoring, to score individual records. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To see model factor information, users need a Sales Cloud Einstein license with the “View Scoring Model Factors” permission enabled.
The permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this
object.


Standard Objects SalesAIScoreModelFactor

Fields

**Field** **Details**

```
Factor

FactorSummaryOrgLanguage

Name

OperatorType

PrimarySourceFieldName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A factor that contributes to a scoring model. For example, a factor could indicate that an
amount increase has a positive effect on an opportunity score (AmountIncreasePositive). Or,
it could indicate that a change to the close date has a negative effect on an opportunity
score (CloseDateChangeNegative).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the factor in English. For example, the factor field value AmountChangePositive
is summarized as “Amount change has positive effect”.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the model factor. Currently, the name is a system-generated value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operator used to analyze field values. For example, the factor HighSuccessLeadSource
uses the Lead Source field as the primary source field. When building the scoring model,
Einstein uses the Equals operator to determine `PrimarySourceFieldValue =`
`Internet` . The other supported operator is `IsNull` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects SalesAIScoreModelFactor

**Field** **Details**

**Description**
The name of the primary field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field.

```
PrimarySourceFieldValue

PrimarySourceFieldValueText

SalesAiScoreCycleId

ScoreCorrelation

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the PrimarySourceFieldValueText, such as a record ID or value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the primary source field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field, and the value of the
Industry field is manufacturing.

Note: This field’s value is retrieved from the `PrimarySourceFieldValue`
field. If the `PrimarySourceFieldValue` field is a record ID, then

`PrimarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull`, then `PrimarySourceFieldValue`
returns `true` and `PrimarySourceFieldValueText` returns `null` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the score cycle used to generate model factors. Each score cycle can have multiple
model factors associated to it.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The strength between a model factor and a score. If score correlation value is closer to `+1`,
it’s more likely that the model factor contributing toward a high score. If score correlation
value is closer to `-1`, it’s more likely that the model factor is contributing toward a low score.


Standard Objects SalesAIScoreModelFactor

**Field** **Details**

```
SecondarySourceFieldName

SecondarySourceFieldValue

SecondarySourceFieldValueText

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the secondary field used in the model factor. For example, the factor
HighAmountActivity uses Task as the primary field and Event as the secondary field. Not all
model factors use a secondary source field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the SecondarySourceFieldValueText, such as a record ID or value.
Not all model factors use a secondary source field. This field is available in API version 50.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the model factor is based on two source fields, this field represents the value of the
secondary source field. For example, the factor HighSuccessMultipleSameFieldValue might
use the opportunity’s related product as the primary field and pricebook as the secondary
field. The product and pricebook names are indicated by the PrimarySourceFieldValueText
and SecondarySourceFieldValueText, respectively. Not all model factors use a secondary
source field. This field is available in API version 50.0 and later.

Note: This field’s value is retrieved from the `SecondarySourceFieldValue`
field. If the `SecondarySourceFieldValue` field is a record ID, then

`SecondarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull`, then `SecondarySourceFieldValue`
returns `true` and `SecondarySourceFieldValueText` returns `null` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Determines whether the model factor is active or inactive.


### Standard Objects SalesforceLoginAsEventLog

Usage

Use the SalesAIScoreModelFactor object to run a query that retrieves the latest highest influencing model factors.

```
   SELECT Id,Factor,ScoreCorrelation,FactorSummaryOrgLanguage

   FROM SalesAIScoreModelFactor

   WHERE Status='Active' and SalesAIScoreCycle.CycleType='OpportunityScoreModeling'

   ORDER BY ScoreCorrelation desc

### SalesforceLoginAsEventLog

```

Salesforce LoginAs Event provides details about the Salesforce User's login into Customer Org as Customer's authorized user. This object
is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ActualUserIdentifier

CaseIdentifier

IpAddress

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The actual user's identifier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce case ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SalesChannel

**Field** **Details**

**Description**
IP address of the browser.

```
OperationType

RequestIdentifier

Timestamp

### SalesChannel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of operation. For example, login or logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

Represents the origin of an order. For example, a web storefront, physical store, marketplace, or mobile app. If you integrate Salesforce
Order Management with Salesforce B2C Commerce, set up a SalesChannel corresponding to each Site in your B2C Commerce
implementation. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.


Standard Objects SalesChannel

Fields

**Field** **Details**

```
Description

ExternalChannelNumber

LastReferencedDate

LastViewedDate

OwnerId

SalesChannelName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the SalesChannel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External system identifier for the SalesChannel.

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
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this SalesChannel. Default value is the user logged in
to the API to perform the create.

**Type**
string


Standard Objects SalesChannel

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the SalesChannel.

```
Type

TypeCategory

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the SalesChannel. Each Type corresponds to one Type Category. You can customize
the Type picklist to represent your business processes, but the Type Category picklist is fixed
because some order processing is based on those values. If you customize the Type picklist,
include at least one value for each Type Category. This field is available in API version 53.0
and later.

Default values are:

**•** `B2B`

**•** `B2C`

**•** `Other`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type Category of the SalesChannel. Each Type Category corresponds to one or more Types.
This field isn’t visible in the UI. This field is available in API version 53.0 and later.

Possible values are:

**•** `B2B`

**•** `B2C`

**•** `Other`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesChannelChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects SalesforceContract

**SalesChannelShare on page 67(API version 66.0)**
Sharing is available for the object.

SEE ALSO:

Order

OrderSummary

### SalesforceContract

Read-only virtual object used in the Your Account App. Represents contract information related to your organization’s Salesforce
subscription.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
AutoRenewCode

BillingAddressCity

BillingAddressCountry

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines if contract renews automatically

Possible values are:

**•** `No`

**•** `Yes`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

```
BillingAddressPostalCode

BillingAddressState

BillingAddressStreet

BillingCompany

BillingEmail

BillingFrequency

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the billing company.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Define billing periods.

```
BillingName

BillingPhone

ContractId

ContractNumber

CreditCardExpirationMonth

CreditCardExpirationYear

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contact name for this contract.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Phone number for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID for this contract.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Number of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Month the credit card expires.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Year the credit card expires.

```
CreditCardNumber

CreditCardType

EndDate

ExternalId

FirstNameOnCreditCard

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
16-digit credit card number.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Credit card provider.

Possible values are:

**•** `AmericanExpress`  

**•** `JCB`

**•** `MasterCard`

**•** `Visa`

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Cardholder’s first name on the credit card.

```
LastNameOnCreditCard

PaymentTerm

PaymentType

SalesforceContractStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Cardholder’s last name on the credit card.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment terms definition.

Possible values are:

**•** `Net0` —Due upon receipt

**•** `Net10` —DD-Germany: Net 10

**•** `Net30`  

**•** `Net30EOM` —JP-Net 30 EOM

**•** `Net45`  

**•** `Net60`  

**•** `Net60EOM` —JP-Net 60 EOM

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment type definition.

Possible values are:

**•** `Check`

**•** `CreditCard`  

**•** `DirectDebit`  

**•** `WireTransfer`  

**Type**
picklist


Standard Objects SalesforceContract

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the contract

Possible values are:

**•** `Activated`

**•** `Draft`

**•** `Expired`

**•** `Terminated`

**•** `inApproval`                   

```
ShippingAddressCity

ShippingAddressCountry

ShippingAddressPostalCode

ShippingAddressState

ShippingAddressStreet

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. City maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. State maximum size is 80 characters.

**Type**
string


### Standard Objects SalesforceInvoice

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address. Maximum of 255 characters.

```
StartDate

SubscriptionDaysLeft

```

Usage

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Start date of the contract.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Days remaining for this subscription.

Used by Your Account to manage contracts related to your organization’s Salesforce subscription. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

### **SalesforceInvoice**

**SalesforcePayment**

**SalesforceQuote**

### SalesforceInvoice

Read-only virtual object used in the Your Account App. Represents information about your organization’s invoices with Salesforce.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`


Standard Objects SalesforceInvoice

Fields

**Field** **Details**

```
Balance

DueDate

ExternalId

InvoiceCurrency

InvoiceDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Currency associated with this invoice.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate` . For example, an invoice with an `InvoiceDate` of April 1 and Net 30 payment
terms would have a `DueDate` of May 1.


Standard Objects SalesforceInvoice

**Field** **Details**

```
InvoiceNumber

SalesforceContractId

SalesforceInvoiceStatus

TotalAmount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
System-created ID for this invoice.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce Contract ID

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup

**Refers To**
SalesforceContract

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the invoice.

Possible values are:

**•** `DueSoon`  

**•** `Paid`

**•** `PastDue`  

**•** `Pending`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` of the invoice items.


### Standard Objects SalesforcePayment

Usage

Used by Your Account to manage invoices for your organization’s Salesforce contract. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

### **SalesforcePayment**

**SalesforceQuote**

### SalesforcePayment

Read-only virtual object used in the Your Account App. Represents information about payments related to your organization’s Salesforce
invoice.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
AppliedAmount

AppliedDate

Memo

```

**Type**
double

**Properties**
Nillable, Sort

**Description**
Payment amount applied to your Salesforce invoice.

**Type**
date

**Properties**
Nillable, Sort

**Description**
Date the payment is applied to your Salesforce invoice.

**Type**
string

**Properties**
Nillable, Sort


Standard Objects SalesforcePayment

**Field** **Details**

**Description**
Credit memo ID. Credit memos are issued for overpayment, rebates, and so forth.

```
PaymentCurrency

SalesforcePaymentName

SalesforcePaymentType

```

Usage

**Type**
string

**Properties**
Nillable, Sort

**Description**
Type of currency used for the payment.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Payment name.

**Type**
picklist

**Properties**
Nillable, Sort

**Description**
Payment method. Possible values are:

**•** `Boleto`

**•** `Check`

**•** `Credit Card`

**•** `Credit Memo`

**•** `Direct Debit`

**•** `Unknown`

**•** `Wire Transfer`

Used by Your Account to manage payments for your organization’s Salesforce contract. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
SalesforcePayment.


### Standard Objects SalesforceQuote

**SalesforceContract**

**SalesforceInvoice**

### **SalesforceQuote** SalesforceQuote

Read-only virtual object used in the Your Account App. Represents information about your organization’s quotes with Salesforce.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ExternalId

QuoteNumber

SalesforceContractId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A system-generated number that identifies the quote.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contract that’s associated with the quote.

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup


### Standard Objects SalesStoreCatalog

**Field** **Details**

**Refers To**
SalesforceContract

```
SalesforceQuoteStatus

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the quote.

Possible values are:

**•** `Complete`

**•** `Expired`

**•** `NeedsApproval`  

**•** `NeedsSignature`  

**•** `Processing`

Used by Your Account to manage quotes related to your organization’s Salesforce contract. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

**SalesforceInvoice**

**SalesforcePayment**

### SalesStoreCatalog

Represents the catalog associated with a store. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a store.


### Standard Objects SalesTransactionItemShape

Fields

**Field** **Details**

```
CurrencyIsoCode

ImplementorType

ProductCatalogId

SalesStoreId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of implementor. WebStoreCatalog is the only available implementor type for
SalesStoreCatalog.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID that references the product catalog.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID that references the store.

### SalesTransactionItemShape

Defines the business logic for a sales transaction shape item, for example, an item in an order. This object is available in API version 57.0
and later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.


Standard Objects SalesTransactionItemShape

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
BasisTransactionItemShapeId

BillingFrequency

EndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the sales transaction shape item to use as a reference when pricing this transaction.
For example, when pricing an order, this field refers to the order being canceled. This field
is available if Subscription Management is enabled.

This field is a relationship field.

**Relationship Name**
BasisTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period that indicates how often the sales transaction shape item is billed. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `Annual`

**•** `Monthly`

**•** `Quarterly`

**•** `Semi-Annual`

**Type**
date


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The last day the sales transaction shape item is available. For example, the last day of the
subscription. This field is available if Subscription Management is enabled.

```
ListPrice

ListPriceTotal

NetUnitPrice

ObligatedAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The list price for the sales transaction shape item. This value is inherited from the related
price book entry.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The list price, inclusive of quantity. This calculated field is equal to `ListPrice` times
`Quantity` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final unit price of the product, after all adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**

**Description**
In a subscription, the amount a subscriber is billed for products used during the subscription
period that the subscriber returns before the subscription end date. This field's value is the
price for use of the product.

This field is available in version 57.0 and later. This field is available when Subscription
Management is enabled.


Standard Objects SalesTransactionItemShape

**Field** **Details**

Note:

**•** A subscriber must submit a quantity amendment in order to change the
subscription's product quantity. A quantity amendment request is only valid until
the subscription end date.

**•** A subscriber is eligible for a refund only for the periods when the products weren’t
used.

**•** The subscription's proration policy indicates whether the obligated amount and
the refund are prorated for partial periods.

```
ParentTransactionItemShapeId

PeriodBoundary

PeriodBoundaryDay

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the parent TransactionItemShape.

This field is a relationship field.

**Relationship Name**
ParentTransactionItemShape

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The period boundary helps determine the start and end date of the billing periods. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `AlignToCalendar` —The period starts on the first day of the term unit, for example,
the first day of the month.

**•** `Anniversary`  - The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod`  - The period starts on the day indicated by `PeriodBoundaryDay` .

**•** `LastDayOfPeriod`  - The period starts on the last day of the pricing term unit; for
example, the last day of the month.

**Type**
int


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required when `PeriodBoundary` is `DayOfPeriod` . Indicates day of the week or
month that marks the period boundary. Must be an integer from 1 through 31. This field is
available if Subscription Management is enabled.

```
PeriodBoundaryStartMonth

PricebookEntryId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency is Annual or by manual user entry. Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`

**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related price book entry. The related price book entry contains all the pricing
information about the product being sold.

This field is a polymorphic relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Refers To**
PricebookEntryInterface

```
PricingTermCount

PricingTransactionType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available if Subscription Management is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of pricing transaction, for example, a new sale, an amendment, or a renewal.
This field is available if Subscription Management is enabled.

Possible values are:

**•** `AmendmentAtLastNegotiatedPrice`  - Calculate the price of the amended
sales transaction shape item using the same price book and price adjustments as the
new sale item. For example, an order item that is amended using a pricing transaction
type of `AmendmentAtLastNegotiatedPrice` is priced using the same price
book information and price adjustments as the new sale item. The amended order item
has the same price as the new sale order item.

**•** `AmendmentStartingFromListPrice`  - Calculate the price of the amended
sales transaction shape item using current price book information, disregarding any
pricing information or adjustments that were applied to the new sale item. Typically, an
amended transaction item has a different price than the new sale transaction item.

**•** `Cancellation`  - Calculate the price of the canceled transaction. For example, let’s
say that a 1-year subscription was purchased on January 1, then canceled on July 31.
The price of the canceled products and services from August 1 through Dec 31 is
calculated.

**•** `NewSale`  - The price of a new transaction is calculated.

**•** `RenewalAtLastNegotiatedPrice`  - Calculate the price of the renewal sales
transaction shape item using the same price book and price adjustments as the new
sale item. For example, an order item that is renewed using a pricing transaction type
of `RenewalAtLastNegotiatedPrice` is priced using the same price book
information and price adjustments as the new sale item. The renewal order item has the
same price as the new sale order item.

**•** `RenewalAtListPrice`  - Calculate the price of the renewal sales transaction shape
item using current price book information, disregarding any pricing information or


Standard Objects SalesTransactionItemShape

**Field** **Details**

adjustments that were applied to the new sale item. Typically, a renewal transaction
item has a different price than the new sale transaction item.

```
ProductId

ProductSellingModelId

ProrationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related product.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. The product selling model defines one method
by which a product can be sold; for example, as a one-time sale, an evergreen subscription,
or a termed subscription. This field is available if Subscription Management is enabled.

This field is a relationship field.

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
The ID of the related proration policy. The proration policy defines how the price is calculated
for each subscription period; for example, whether partial periods are allowed, and how
remainder amounts are handled. This field is available if Subscription Management is enabled.


Standard Objects SalesTransactionItemShape

**Field** **Details**

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

```
Quantity

SalesItemType

SalesTransactionItemShapeName

SalesTransactionShapeId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Number of units in the sales transaction shape item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of sale.

Possible values are:

**•** `Charge`  - An item that acts as a fee and can’t be fulfilled. For example, a delivery
charge, a shipping fee, or a membership fee.

**•** `Product`  - An item that is a good or service that can be fulfilled. For example, a widget
or a widget warranty.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Required. The name of the sales transaction shape item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the sales transaction shape. A sales transaction shape is the way in which
the sales transactions occur. For example, a cart, an order, or a quote.


Standard Objects SalesTransactionItemShape

**Field** **Details**

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

```
StartDate

StartingPriceTotal

StartingUnitPrice

StartingUnitPriceSource

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The start date of the subscription. This field is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The starting unit price, inclusive of quantity, prorated for the duration of the subscription.
This field has two ways to obtain its value. The value can be manually entered or automatically
calculated. The calculation is equal to `StartingUnitPrice` times `Quantity` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The unit price before any adjustments.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was inherited, entered manually, or calculated.

Possible values are:

**•** `Inherited`  - The starting unit price is copied from a previous transaction; for example,
from the order item being renewed.

**•** `Manual`  - The starting unit price is entered manually, for example, by a sales rep.


Standard Objects SalesTransactionItemShape

**Field** **Details**

**•** `System`                   - The starting unit price is calculated using pricing information that was
configured by an administrator; for example, a pricing tier.

```
StockKeepingUnit

SubscriptionTerm

TotalAdjustmentAmount

TotalAdjustmentDistAmount

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The SKU assigned to the related product.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. You can indicate a subscription’s length using
either the start and end dates, or by using the start date and the subscription term. This field
is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the related sales transaction shape items, inclusive of
quantity, prorated for the duration of the subscription. Includes distributed price adjustment
items and price adjustment items applied directly. This calculated field is equal to the sum
of `TotalAdjustmentAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the sales transaction shape
item, prorated for the duration of the subscription. Doesn’t include price adjustment items
that are applied directly. A distributed price adjustment is automatically created to apply a
transaction-level adjustment to the transaction items. For example, let’s say that you have
an order with two order items: one for a file storage service and another for a video streaming
service. A 10% volume discount and a 15% manual discount are applied to the entire order.
An additional 20% discount is applied to the file storage service. To distribute the order-level
discounts, the system creates a 10% price adjustment item and a 15% price adjustment item


### Standard Objects SalesTransactionShape

**Field** **Details**

for each order item. In this example, the file storage service’s sales transaction shape item
has the following field values:

**•** `TotalAdjustmentAmount`                   - The sum of all item-level adjustments, including
the 10% price adjustment item, the 15% price adjustment item, and the 20% price
adjustment item.

**•** `TotalAdjustmentDistAmount`                   - The sum of the distributed item-level
adjustments, including the 10% price adjustment item and the 15% price adjustment
item.

```
TotalLineAmount

TotalPrice

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price before price adjustments, inclusive of quantity, prorated for the duration of
the subscription. This calculated field is equal to `StartingPriceTotal` times
`PricingTermCount` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This calculated field is equal to `TotalAdjustmentAmount` plus
`StartingPriceTotal` .

### SalesTransactionShape

Defines the business logic for a sales transaction; for example, an order, a quote, or a cart. This object is available in API version 57.0 and
later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.


Standard Objects SalesTransactionShape

Fields

**Field** **Details**

```
AccountId

SalesTransactionShapeName

TotalAdjustmentAmount

TotalAdjustmentDistAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier for the account associated with this sales transaction shape. This field
is available when OrgPermissions or Platform is enabled.

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
Create, Filter, Group, idLookup, Sort

**Description**
The name of the sales transaction shape. For example, Quote.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the sales transaction shape, inclusive of quantity,
prorated for the duration of the subscription. Includes distributed price adjustment items
and price adjustment items applied directly. This calculated field is equal to the sum of
`TotalAdjustmentAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the related sales transaction
shape items, inclusive of quantity, prorated for the duration of the subscription. Does not


### Standard Objects SalesTransactionType

**Field** **Details**

include price adjustment items that are applied directly. This calculated field is equal to the
sum of `TotalAdjustmentDistAmount` on the related sales transaction shape items.

```
TotalAmount

TotalListAmount

TotalProductAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final price of the sales transaction shape, after all adjustments, inclusive of quantity,
prorated for the duration of the subscription. This calculated field equal to the sum of
`TotalPrice` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the list price of the related sales transaction shape items, inclusive of quantity,
prorated for the duration of the subscription. This calculated field is equal to the sum of
`ListPriceTotal` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price of all related sales transaction shape items of type Product, before price
adjustments, inclusive of quantity, prorated for the duration of the subscription. This calculated
field is equal to the sum of `TotalLineAmount` on the related sales transaction shape
items of type Product.

### SalesTransactionType

Represents the type of sales transaction, such as an initial, renewal, or amendment sale, and its related pricing configuration.. This object
is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SalesTransactionType

Special Access Rules

This object is available when Revenue Cloud is enabled.

Fields

**Field** **Details**

```
Description

Name

PricingProcedureId

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the sales transaction type.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the sales transaction type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The pricing procedure related to the sales transaction type.

This field is a relationship field.

**Relationship Name**
PricingProcedure

**Refers To**
ExpressionSetDefinition

This object has the following associated objects.

**SalesTransactionTypeShare on page 67**
Sharing is available for the object.


### Standard Objects SalesTrxnItemRelationShape SalesTrxnItemRelationShape

Describes the relationship between sales transaction shape items; for example, a bundle or set. This object is available in API version 57.0
and later.

Supported Calls

`create() describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AssocSalesTrxnItemShapeId

AssocSalesTrxnItemShapeRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the associated sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle component.

**Relationship Name**
AssocSalesTrxnItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated sales transaction shape item in the relationship.

Possible values are:

**•** `BundleComponent` —The associated sales transaction shape item is part of a bundle.

**•** `SetComponent` —The associated sales transaction shape item is part of a set.


Standard Objects SalesTrxnItemRelationShape

**Field** **Details**

```
AssociatedItemShapePricing

MainSalesTrxnItemShapeId

MainSalesTrxnItemShapeRole

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes how the associated sales transaction shape item is priced, relative to the main
sales transaction shape item.

Possible values are:

**•** `IncludedInBundlePrice`  - The associated sales transaction shape item’s cost
is $0 because it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice`  - The associated sales transaction shape item
has a cost because it’s not included in the bundle’s price.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the main sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle parent.

**Relationship Name**
MainSalesTrxnItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the position of the main sales transaction shape item in the relationship.

Possible values are:

**•** `AddOnComponent`  - The main sales transaction shape item is an add on component.
Available in API version 58.0 and later.

**•** `Bundle`  - The main sales transaction shape item is the bundle parent.

**•** `Set`  - The main sales transaction shape item is the set parent.


Standard Objects SalesTrxnItemRelationShape

**Field** **Details**

```
ProductRelationshipTypeId

QuantityScaleMethod

SalesTransactionShapeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that describes the relationship between the main and associated sales
transaction shape items.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How to scale the quantity of the associated sales transaction shape item, relative to the main
sales transaction shape item. The value is informative; the system doesn’t check whether the
scaled quantities are correct. If this field has a non-null value, you can't edit the associated
sales transaction shape item’s quantity.

Possible values are:

**•** `Constant` —The associated sales transaction’s item quantity remains the same in
relation to the main sales transaction shape item’s quantity. For example, let’s say that
the main sales transaction shape item has a quantity of one and the associated sales
transaction shape item has a quantity of one. If you increase the quantity of the main
sales transaction shape item to two, the associated sales transaction shape item’s quantity
remains at one.

**•** `Proportional` —The associated sales transaction’s item quantity increases or
decreases based on the main sales transaction shape item’s quantity. For example, let’s
say that the main sales transaction shape item has a quantity of one and the associated
sales transaction shape item has a quantity of two. If you increase the quantity of the
main order item to two, the associated order item’s quantity increases to four.

The default value is `Proportional` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects SalesWorkQueueSettings

**Field** **Details**

**Description**
The ID of the related sales transaction shape.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

```
SalesTrxnItemRelationShapeName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Name of the relationship of the sales transaction shape item.

### SalesWorkQueueSettings

Represents settings used to customize work queue options for third-party scoring. Third-party scoring enables custom number fields
on person accounts, contacts, and leads. You must be a Sales Engagement customer to update this object. Previously, you could only
use the Einstein Intelligence Score for third-party scoring. Available starting in Version 47.0.

Note: This object can’t be packaged.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
FeatureName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A value that represents the name of the work queue settings.


### Standard Objects SandboxStatusEventLog

**Field** **Details**

To use custom number fields in the work queue, the value must be entered as
`ThirdPartyScore` .

```
TargetEntity

TargetField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The related record object of the custom number field. Acceptable SObjects include
PersonAccount, Contact, and Lead.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the DeveloperName of the custom number field related to the
TargetEntity. Custom fields must have a custom number data type.

**•** To use Einstein Intelligence Score for lead scoring, enter
`ScoreIntelligence.Score` for the DeveloperName.

**•** To remove custom number fields from the work queue, enter `None` .

### SandboxStatusEventLog SandboxStatusEventLog stores details about Sandbox copies. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
CurrentSandboxOrganizationIdentifier

```

**Type**
string


Standard Objects SandboxStatusEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the current sandbox organization.

```
PendingSandboxOrganizationIdentifier

RequestIdentifier

SandboxOrganizationIdentifier

Status

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the sandbox copy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: 20130715233322.670.


### Standard Objects SamlSsoConfig

**Field** **Details**

```
UserIdentifier

### SamlSsoConfig

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: 00530000009M943YAS

.

Represents a SAML Single Sign-On configuration.This object is available in API version 32.0 and later.

Single sign-on is a process that allows network users to access all authorized network resources without having to log in separately to
each resource. Single sign-on allows you to validate usernames and passwords against your corporate user database or other client
application rather than having separate user passwords managed by Salesforce.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission or both the Customize Application and Modify
All Data permissions can access this object.

Fields

**Field Name** **Details**

```
AttributeFormat

AttributeName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For SAML 2.0 only and when `identityLocation` is set to `Attribute` .
Possible values include `unspecified`, `emailAddress`, or `persistent` .
All legal values can be found in the “Name Identifier Format Identifiers” section
[of the Assertions and Protocols SAML 2.0 specification.](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

**Type**
string


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the identity provider’s application. Get this name value from your
identity provider.

```
Audience

DeveloperName

ErrorUrl

ExecutionUserID

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The Issuer, also called the “Entity ID.” The value is a URL that uniquely identifies
the SAML identity provider.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
When there's an error during login, specify the URL of the page where users are
directed. It must be publicly accessible, such as a public site Visualforce page.
The URL can be absolute or relative.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Description**

The user that runs the Apex handler class. The user must have the “Manage Users”
permission. A user is required if you specify a SAML JIT handler class.

This is a relationship field.

**Relationship Name**
ExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

```
IdentityLocation

IdentityMapping

Issuer

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The location in the assertion where a user is identified. Valid values are:

**•** `SubjectNameId` —The identity is in the `<Subject>` statement of the
assertion.

**•** `Attribute` —The identity is specified in an `<AttributeValue>`,
located in the `<Attribute>` of the assertion.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The identifier that the service provider uses for the user during Just-in-Time user
provisioning. Valid values are:

**•** `Username` —The user’s Salesforce username.

**•** `FederationId` —The federation ID from the user object; the identifier
that’s used by the service provider for the user.

**•** `UserId` —The user ID from the user’s Salesforce organization.

**Type**
string

**Properties**
Filter, idLookup, Group, Sort

**Description**
Also called the “Entity ID.” The value is a URL that uniquely identifies the SAML
identity provider.


Standard Objects SamlSsoConfig

**Field Name** **Details**

```
Language

LoginUrl

LogoutUrl

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL where Salesforce sends a SAML request to start the
login sequence.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL to direct users to where they click the Logout link.
The default is `https://salesforce.com` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The text that’s used to identify the Visualforce page in the Setup area of Salesforce.

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


Standard Objects SamlSsoConfig

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
OptionsSpInitBinding

OptionsUseConfigRequestMethod

OptionsUseSameDigestAlgoForSigning

OptionsRequireMfaSaml

```

**Type**
boolean

**Properties**
Filter

**Description**

The service provider initiated request binding, either HTTP Redirect ( `true` ) or
HTTP POST ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, applies the selected Request Signature Method (RSM) during single
logout. If `false`, the default RSM ( `RSA-SHA1` ) is applied.

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, uses a SAML digest algorithm based on the selected Request Signature
Method (RSM). For example, if the selected RSM is `RSA-SHA256`, the digest
algorithm is set to `SHA-256` .

If `false`, uses the default digest algorithm ( `SHA-1` ), regardless of the selected
RSM.

This field is available in API version 55.0 and later. You can edit this field only for
legacy SAML configurations created before the Spring ’22 release. For
configurations created after Spring ’22, this field is `true` by default.

**Type**
boolean


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this SAML
configuration based on the MFA status of each user. For this setting to trigger
MFA, you must apply MFA directly to users via one of two methods. 1) Assign
the user permission Multi-Factor Authentication for User Interface Logins. 2)
Enable the org setting Require multi-factor authentication (MFA) for all direct UI
logins to your Salesforce org.

```
OptionsUserProvisioning

RequestSignatureMethod

SamlJitHandlerId

```

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, Just-in-Time user provisioning is enabled, which creates users on the
fly the first time that they try to log in. Specify `Federation ID` for the
`identityMapping` value to use this feature.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The method that’s used to sign the SAML request. Valid values are:

**•** `RSA-SHA1`

**•** `RSA-SHA256`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of an existing Apex class that implements the
`Auth.SamlJitHandler` interface.

This is a relationship field.

**Relationship Name**
SamlJitHandler

**Relationship Type**
Lookup


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Refers To**
ApexClass

```
SingleLogoutBinding

SingleLogoutUrl

ValidationCert

Version

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Determines where to put the LogoutRequest or LogoutResponse in the SAML
request during single logout (SLO). The value is base64 encoded. Valid values
are:

**•** `RedirectBinding`  - Sent in the query string, deflated.

**•** `PostBinding`  - Sent in the POST body, not deflated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SAML single logout endpoint. This URL is the endpoint where Salesforce
sends LogoutRequests (when Salesforce initiates a logout), or LogoutResponses
(when the identity provider initiates a logout).

**Type**
string

**Properties**
Filter, Sort

**Description**
The certificate that’s used to validate the request. Get this certificate value from
your identity provider.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The SAML version. Valid values are:

**•** `SAML1_1`

**•** `SAML2_2`


### Standard Objects SavedPaymentMethod SavedPaymentMethod

Represents a payment method saved by an authenticated customer. This object is available in API version 58.0 and later

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountHolderEmail

AccountHolderName

AsyncGatewayRefNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address of the payment method holder.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Full name of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
The payment transaction ID created by the payment gateway for asynchronous payments.
This field is available in API version 66.0 and later.

**•** For Adyen, use the pspReference.

**•** For Stripe, use the fingerprint value.


Standard Objects SavedPaymentMethod

**Field** **Details**

```
BankAccountHolderType

BankAccountType

BankCode

BankName

BillingAddress

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines whether the bank account is held by a business or an individual.

Possible values are:

**•** `Business`

**•** `Individual`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Characterizes the bank account, such as a checking or savings account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Code that represents the bank who issued the payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the bank that issued the payment method.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The billing address of the account holder of the payment method. This is the compound
form of the billing address. Read-only. For details on compound address fields, see Address
Compound Fields.


Standard Objects SavedPaymentMethod

**Field** **Details**

```
BillingCity

BillingCountry

BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

BillingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the billing address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

**Type**
string


Standard Objects SavedPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 20 characters.

```
BillingState

BillingStreet

ExpiryMonth

ExpiryYear

ExtendedPaymentMethodType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 80 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Month the payment method expires.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Year the payment method expires.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Other saved payment methods used for the transaction. This field is required when the value
of the `Type` field is `extd_altrn_payment_method_type` or `extd_wallet` .
This field is available in API version 66.0 and later.


Standard Objects SavedPaymentMethod

**Field** **Details**

```
GatewayReference

GatewayToken

IsDefault

IsMerchantCreated

IsSharedWithinSameAccount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A reference to the saved payment owner at the payment gateway. For example, a Stripe
customer ID.

**Type**
encryptedstring

**Properties**
Nillable

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the card
payment method during transactions. `GatewayToken` is for use with APIs earlier than
version 52.0. For version 53.0 and latter, use the GatewayTokenEncrypted field. To secure
the token, use the `GatewayTokenEncrypted` field.

An error message appears if you try to record a `GatewayToken` for a card payment
method that already has a `GatewayToken` or `GatewayTokenEncrypted` value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Customer’s default payment method.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the merchant saved the payment method on behalf of the payer. The
Payer must provide consent to the merchant to save this information.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects SavedPaymentMethod

**Field** **Details**

**Description**
Indicates whether the saved payment method is visible to all contacts in an account ( `true` )
or only to the contact who created it ( `false` ). The default value is `false` .

This field is available in API version 64.0 and later.

```
Issuer

Last4

LastReferencedDate

LastViewedDate

MerchantAccountId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Financial institution issuing the payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Last four digits of the payment method account number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record or list view related to this
record, but didn’t access it directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user referenced this record but didn’t view it directly.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifies the Salesforce Payments Merchant Account.


Standard Objects SavedPaymentMethod

**Field** **Details**

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

```
Name

Network

Nickname

PaymentGatewayId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the saved payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Saved payment method card network, for example Visa or Union Pay.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional name or label to easily identify the payment method.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The payment gateway that is used to create a gateway token. For transactions with a saved
payment method in Salesforce, this field stores the payment gateway ID used in the
transaction. This field is a relationship field.

This field is a relationship field.

**Relationship Name**
PaymentGateway


Standard Objects SavedPaymentMethod

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

```
PaymentMethodSubType

ProcessingMode

ReferenceOwnerId

StandardEntryClassCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of the Card payment method. This field
is available in API version 66.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the payment was made outside of the Salesforce platform. This field is
available in API version 66.0 and later.

Possible values are:

**•** `External`

**•** `Salesforce`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Account or Contact record that owns the payment method.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceOwner

**Relationship Type**
Lookup

**Refers To**
Account or Contact

**Type**
picklist


Standard Objects SavedPaymentMethod

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A three-letter code that indicates how a customer or a business initiated and authorized an
ACH payment.

Possible values are:

**•** `CCD` —Corporate credit or debit entry

**•** `PPD` —Prearranged payment or deposit entry

**•** `TEL` —Telephone-initiated entry

**•** `WEB` —Internet or mobile-initiated entry

```
Status

Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the saved payment method.

Possible values are:

**•** `Active`

**•** `AwaitingPayment`

**•** `Errored` —Failed

**•** `Expired`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of saved payment method.

Possible values are:

**•** `au_becs_debit`

**•** `bacs_debit`

**•** `bancontact`

**•** `card`

**•** `extd_apm_type`

**•** `extd_wallet`

**•** `ideal`

**•** `sepa_debit`

**•** `us_bank_account`  - ACH Direct Debit


### Standard Objects SavedPaymentMethodEvent

**Field** **Details**

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates if the payment method is used on or off session.

Possible values are:

**•** `OffSession`

**•** `OnSession`

**•** `RestrictedOffSession`

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**SavedPaymentMethodChangeEvent on page 68**
Change events are available for the object.

**SavedPaymentMethodFeed on page 55**
Feed tracking is available for the object.

**SavedPaymentMethodHistory on page 63**
History is available for tracked fields of the object.

**SavedPaymentMethodOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SavedPaymentMethodShare on page 67**
Sharing is available for the object.

### SavedPaymentMethodEvent

Represents a saved payment method platform event. Subscribe to these events so you can listen and respond to them when they’re
published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API
version 59.0 and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)

Supported Calls

```
describeSObjects()

```


### Standard Objects SchedulingAdherenceDetail

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
ChangeType

SavedPaymentMethodId

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of saved payment method event, which triggers an event notification. You can write
code to operate conditionally on the value of this field. For example, you can ignore a create
change but get notified of updates.

Possible values are:

**•** `Create` –Saved payment method created.

**•** `Delete` –Saved payment method deleted.

**•** `Update` –Saved payment method property changed.

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the SavedPaymentMethod record for which the event occurs.

This field is a relationship field.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

### SchedulingAdherenceDetail

Represents the breakdown of daily shift adherence data by agent status. This object is available in API version 54.0 and later.


Standard Objects SchedulingAdherenceDetail

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
IsShrinkage

Name

SchedulingAdherenceSummaryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the linked status is considered as shrinkage time ( `true` ) or not ( `false` ).
Shrinkage time is time, such as breaks, when an agent doesn’t receive work.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this detail record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Scheduling Adherence Summary.

This is a relationship field.

**Relationship Name**
SchedulingAdherenceSummary

**Relationship Type**
Lookup

**Refers To**
SchedulingAdherenceSummary


### Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
StatusId

StatusName

TotalStatusMinutes

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the agent status represented by this detail record.

This is a relationship field.

**Relationship Name**
Status

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the agent status represented by this detail record.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present with this status.

### SchedulingAdherenceSummary

Represents daily shift adherence data for a service resource in a service territory and job profile on a specific date. This object is available
in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects SchedulingAdherenceSummary

Special Access Rules

The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
AdherencePercentage

ConformancePercentage

Date

JobProfileId

```

**Type**
double

**Properties**
Filter, Sort

**Description**
Percentage of time that the agent was present during the scheduled shift time.

This is a calculated field.

**Formula**

```
  AdherencePercentage =

  TotalAdherenceMinutes / TotalScheduledMinutes

```

**Type**
double

**Properties**
Filter, Sort

**Description**
Percentage of time when the agent was present versus the duration of scheduled shifts. The
time that the agent is present can extend beyond the scheduled shift.

This is a calculated field.

**Formula**

```
  ConformancePercentage =

  TotalPresenceMinutes / TotalScheduledMinutes

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date for which the adherence data is calculated.

**Type**
reference


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the job profile.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

```
JobProfileName

Name

OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the job profile.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this summary record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the schedule adherence summary.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
ServiceResourceId

ServiceResourceName

ServiceTerritoryId

ServiceTerritoryName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service resource.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service resource.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service territory.


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
TotalAdherenceMinutes

TotalInteractionMinutes

TotalPresenceMinutes

TotalScheduledMinutes

TotalShrinkageMinutes

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present during a shift.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was actively receiving work.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total minutes of agent presence time.

This is a calculated field.

**Formula**

```
  TotalPresenceMinutes =

  TotalInteractionMinutes + TotalShrinkageMinutes

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Total minutes of scheduled shift time for the agent.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present but not receiving work, such as break times.


### Standard Objects SchedulingConstraint

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SchedulingAdherenceSummaryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SchedulingAdherenceSummaryShare on page 67**
Sharing is available for the object.

### SchedulingConstraint

Represents scheduling constraints on each service resource. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The org requires the Workforce Engagement license. To view records, the user requires the Workforce Engagement Agent permission
set. To create, edit, or delete records, the user requires the Workforce Engagement Planner permission set.

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MaxNonstandardShiftsPerMonth

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last modified. Its label in the user interface is
Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last viewed.

**Type**
int


Standard Objects SchedulingConstraint

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of non-standard shifts assigned to an agent in a month.

This field is available in API version 54.0 and later.

```
MaxShiftsPerDay

MaxShiftsPerMonth

MaxShiftsPerWeek

MaxWorkingHoursPerDay

MaxWorkingHoursPerMonth

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a day.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a week.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a day.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a month.


Standard Objects SchedulingConstraint

**Field** **Details**

```
MaxWorkingHoursPerWeek

Name

OwnerId

RestTimeMinutes

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a week.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling constraint record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the scheduling constraint.

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
The minimum rest time, in minutes, between an agent’s consecutive shifts.

This field is available in API versions 56.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects SchedulingObjective

**SchedulingConstraintOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SchedulingConstraintShare on page 67**
Sharing is available for the object.

### SchedulingObjective

Represents business goals that the scheduling tools consider. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.

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
Create, Nillable, Update

**Description**
The scheduling objective description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects SchedulingRule

**Field** **Details**

**Description**
Possible values are the supported languages for Workforce Engagement.

```
MasterLabel

SchedulingCategory

SchedulingObjectiveType

### SchedulingRule

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling objective name.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The record that the scheduling objective applies to.

Possible values are:

**•** `A` —Appointment

**•** `B` —Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of scheduling objective.

Possible values are:

**•** `AgentPreference` —Scheduling tools consider agents’ service resource preferences.
In the UI, this value appears as Maximized Preferences.

**•** `BalanceNonStandardShifts` —Scheduling tools balance the number of shifts
across available agents within a time period.

**•** `BalanceShifts` —Scheduling tools balance the number of non-standard shifts
across available agents within a time period.

Represents scheduling rules that are hard constraints in the scheduling logic engine. This object is available in API version 52.0 and later.


Standard Objects SchedulingRule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The scheduling rule description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name value of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the scheduling rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling rule name.


### Standard Objects SchedulingRuleParameter

**Field** **Details**

```
SchedulingCategory

SchedulingRuleType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shifts.

Possible values are:

**•** `A` —Appointment

**•** `B` —Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The scheduling rule type.

Possible values are:

**•** `A` —Active Resources

**•** `B` —Match Skills

**•** `C` —Availability

**•** `LimitNonstandardShifts` —Specifies a rule type that limits how many
non-standard shifts can be assigned to each agent. This type is available in API version
54.0 and later.

**•** `M` —Match Territory

**•** `Q` —Match Queues

**•** `RestTimeMinutes` —Specifies a rule type that requires the agent to have a minimum
rest time between consecutive shifts. This type is available in API version 56.0 and later.

**•** `W` —Work Limit

### SchedulingRuleParameter

Represents scheduling rule parameters associated with a scheduling rule. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects SchedulingRuleParameter

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user needs to have the Workforce
Engagement Planner permission set.

Fields

**Field** **Details**

```
SchedulingParameterKey

SchedulingRuleId

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The scheduling rule parameter name.

Possible values are:

**•** `ConsiderAbsence` —Consider absences when determining a service resource’s
availability. This type is available in API version 56.0 and later.

**•** `ConsiderSTM` —Consider service territory membership when determining a service
resource’s availability. Service territory membership defines the resource’s working hours
in a location. This type is available in API version 56.0 and later.

**•** `C` —Constraint Field Name

**•** `L` —Limit Type

**•** `R` —Resolution

**•** `T` —Time Resolution

**•** `W` —Work Unit

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The scheduling rule ID.

This is a relationship field.

**Relationship Name**
SchedulingRule

**Relationship Type**
Lookup

**Refers To**
SchedulingRule

**Type**
string


### Standard Objects Scontrol

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The scheduling rule parameter value.

### Scontrol

A custom s-control, which is custom content that is hosted by the system but executed by the client application.

Important: Visualforce pages supersede s-controls. Organizations that haven’t previously used s-controls can’t create them.
Existing s-controls are unaffected, and can still be edited. We recommend that you move your s-controls to Visualforce. We continue
to support the Scontrol object.

Represents a custom s-control, which is custom content that the system hosts, but client applications execute. An s-control can contain
any type of content that you can display or run in a Web browser.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Enterprise, Developer, or Unlimited Edition and be enabled for custom s-controls.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Binary

BodyLength

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Binary content of this custom s-control, such as an ActiveX control or a Java archive. Can be
specified when created, but not when updated. Limit: 5 MB.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects Scontrol

**Field** **Details**

**Description**
The length of the custom s-control. Label is **Binary Length** .

```
ContentSource

Description

DeveloperName

EncodingKey

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the source of the s-control content, either custom HTML, a snippet (s-controls that
are included in other s-controls), or a URL.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the custom s-control.

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
are reflected in a subscriber’s organization. Label is **S-Control Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Picklist of character set encodings, including ISO-08859-1, UTF-8, EUC, JIS, Shift-JIS, Korean
(ks_c_5601-1987), Simplified Chinese (GB2312), and Traditional Chinese (Big5).


Standard Objects Scontrol

**Field** **Details**

```
Filename

HtmlWrapper

Name

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An uploaded object to display when the custom s-control is added to a custom link. Can be
a Java applet, an ActiveX control, or any other type of desired content.

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. HTML page that will be delivered when the user views this custom s-control. This
HTML page can be the entire content of the custom s-control, or it can reference the binary.
Limit: 1,048,576 characters. Label is **HTML Body** .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Name of this custom s-control. Label is **Label** .

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


### Standard Objects ScontrolLocalization

**Field** **Details**

```
SupportsCaching

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the s-control supports caching ( `true` ) or not ( `false` ).

Use custom s-controls to manage custom content that extends application functionality. All users can view custom s-controls, but the
“Customize Application” permission is required to create or update custom s-controls.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ScontrolLocalization

The translated value of the field label for an s-control.

Important: Visualforce pages supersede s-controls. Organizations that haven’t previously used s-controls can’t create them.
Existing s-controls are unaffected, and can still be edited.

When the Translation Workbench is enabled for your organization, provides the translation of the field label of an s-control.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, or Unlimited Edition and be enabled for the Translation
Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
LanguageLocaleKey

```

**Type**
picklist


Standard Objects ScontrolLocalization

**Field** **Details**

**Properties**
Create,

Filter,

Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in
English.

The following end-user only languages are available.

**•** Arabic: `ar`


Standard Objects ScontrolLocalization

**Field** **Details**

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

**•** Arabic (Syria): `ar_SY`

**•** Arabic (Tunisia): `ar_TN`

**•** Arabic (United Arab Emirates): `ar_AE`

**•** Arabic (Yemen): `ar_YE`


Standard Objects ScontrolLocalization

**Field** **Details**

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

**•** Georgian: `ka`

**•** German (Austria): `de_AT`

**•** German (Belgium): `de_BE`

**•** German (Luxembourg): `de_LU`


Standard Objects ScontrolLocalization

**Field** **Details**

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

**•** Serbian (Latin): `sh`

**•** Spanish (Argentina): `es_AR`

**•** Spanish (Bolivia): `es_BO`

**•** Spanish (Chile): `es_CL`


Standard Objects ScontrolLocalization

**Field** **Details**

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

The values in this field are not related to the default locale selection.

```
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed


### Standard Objects Scorecard

**Field** **Details**

managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 ScontrolId

 Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Scontrol that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated field label of the s-control. Label is **Translation** .

Use this object to translate your s-controls into a supported language. Users with the Translation Workbench enabled can view s-control
translations, but either the “Customize Application” or “Manage Translation” permission is required to create or update s-control
translations.

SEE ALSO:

CategoryNodeLocalization

WebLinkLocalization

### Scorecard

Use scorecards to measure partner performance and establish benchmarks for channel programs within Experience Cloud. Display any
report summary results that your channel account manager or executive team wants to see. This object is available in API version 40.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects Scorecard

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the scorecard.

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

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the scorecard visible to end users.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the scorecard.

This is a polymorphic relationship field.


### Standard Objects ScorecardAssociation

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

The Scorecard object is used in tandem with the ScorecardMetric and ScorecardAssociation objects.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ScorecardOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ScorecardShare on page 67**
Sharing is available for the object.

### ScorecardAssociation

Represents a connection between a specific scorecard and the associated account, channel program, or channel program level. This
object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects ScorecardAssociation

**Field** **Details**

```
LastViewedDate

Name

ScorecardId

TargetEntityId

```

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

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Scorecard Association.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the scorecard that the association is related to. Several metrics can be tied to a
single scorecard.

This is a relationship field.

**Relationship Name**
Scorecard

**Relationship Type**
Lookup

**Refers To**
Scorecard

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated object that a specific scorecard is associated with.

This is a polymorphic relationship field.

**Relationship Name**
TargetEntity


### Standard Objects ScorecardMetric

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, ChannelProgram, ChannelProgramLevel

### ScorecardMetric

