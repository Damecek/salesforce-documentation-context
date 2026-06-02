Accessing this object requires View Event Log Files and API Enabled user permissions. Users with View All Data permission can view
event log files.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: You can only delete event log file data if you enable the **Delete event monitoring data** setting in Setup.

Fields

**Field** **Details**

```
ApiVersion

EventType

Interval

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The specific API version for this log file. This field is available in API version 30.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The event type—API, Login, Report, URI, and so forth. Use to determine which files were
generated for your org. For the corresponding `LogFile` schema, see EventLogFile
Supported Event Types.

**Type**
picklist


Standard Objects EventLogFile

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The generation schedule for the event log file. Possible values are:

**•** `Daily`

**•** `Hourly`

This field is available in API version 37.0 and later. This field is available in API version 37.0
and later to customers with hourly Event Log Files.

```
LogDate

LogFile

LogFileContentType

LogFileFieldNames

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the log file’s creation. For daily event log files, tracks usage activity for
a 24-hour period, from 12:00 a.m. to 11:59 p.m. UTC time. For hourly event log files, indicates
the hour in which the log file was generated. For example, for events that occur between
11:00 AM and 12:00 PM on 3/7/2016, this field’s value is 2016-03-07T11:00:00.000Z.

Note: For hourly event log files, we recommend using `CreatedDate` to query
the date and time that an EventLogFile object was created.

**Type**
base64

**Description**
Encoded file data in `.csv` format. The `EventType` field defines the schema for this data.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The content type of the log file; always `.csv` .

**Type**
string

**Properties**
Nillable

**Description**
The ordered list of fields in the log file data.


Standard Objects EventLogFile

**Field** **Details**

Note: `LogFileFieldNames` and `LogFileFieldTypes` are specific to
each `EventType` . For example, `LogFileFieldNames` has a different value
for an API `EventType` and a Login `EventType` .

```
LogFileFieldTypes

LogFileLength

Sequence

```

**Type**
string

**Properties**
Nillable

**Description**
The ordered list of field types in the log file data ( `String`, `Id`, and so forth).

Note: `LogFileFieldNames` and `LogFileFieldTypes` are specific to
each `EventType` . For example, `LogFileFieldTypes` has a different value
for an API `EventType` and a Login `EventType` .

**Type**
double

**Properties**
Filter, Sort

**Description**
The log file length in bytes. You can use this field to plan storage needs for your log files.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number for the portion of the event log file data captured in an hour. For 24-hour event
log file generation, the value of this field is 0. For hourly event log files, the initial value is 1.
This value increases by 1 when events are added in the same hour after the latest event log
file is created. The value resets to 1 in the subsequent hour. For example, you have activity
between 2:00 and 3:00 PM. Two-log files are generated that contain the event log data for
that hour, with `Sequence` values of 1 and 2. For event log data that occurs at 3:01 PM,
the `Sequence` value resets to 1. This field is available in API version 37.0 and later.

EventLogFile Supported Event Types
The `EventType` field in the EventLogFile object supports these events. Some common fields, such as `CPU_TIME` and `RUN_TIME`,
can have null or zero values depending on how the events are generated for a given feature. Sometimes, three quotation marks
appear around event data containing special characters in the CSV file. The third quotation mark is necessary for tools and applications
to parse the field data at the correct field value boundary.


#### Standard Objects EventLogFile Supported Event Types EventLogFile Supported Event Types

The `EventType` field in the EventLogFile object supports these events. Some common fields, such as `CPU_TIME` and `RUN_TIME`,
can have null or zero values depending on how the events are generated for a given feature. Sometimes, three quotation marks appear
around event data containing special characters in the CSV file. The third quotation mark is necessary for tools and applications to parse
the field data at the correct field value boundary.

We generate some text messages in quotes, as in "example message". To preserve the original value, we add two more quotes and the
final value looks like """example message""" in the CSV file.

Note: The Apex Unexpected Exception, API Total Usage, CORS Violation Record, CSP Violation, Hostname Redirects, Insecure
External Assets, Login, and Logout events are available in supported Salesforce editions at no additional cost. To purchase the
remaining event types, contact Salesforce.

Apex Callout Event Type
Apex Callout events contain details about callouts (external requests) during Apex code execution.

Apex Execution Event Type
Apex Execution events contain details about Apex classes that are used.

Apex Inline Event Type
This event type is reserved for future use. This object is available in API version 66.0 and later.

Apex REST API Event Type
Apex REST API events capture information about every Apex REST API request.

Apex SOAP Event Type
Apex SOAP events contain details about custom SOAP web service calls.

Apex Trigger Event Type
Apex Trigger events contain details about triggers that fire in an organization.

Apex Unexpected Exception Event Type
The Apex Unexpected Exception event type captures information about unexpected exceptions in Apex code execution. This event
type is available in the EventLogFile object in API version 45.0 and later. Unexpected exception information is not captured in the
EventLogFile object with `@IsTest` and anonymous Apex.

API Total Usage
API Total usage events contain details about Platform SOAP API, Platform REST API, and Bulk API requests.

Asynchronous Report Run Event Type
Asynchronous Report Run events are created for reporting requests that are scheduled. This category includes dashboard refreshes,
asynchronous reports, schedule reports, and analytics snapshots.

Aura Request Event Type
Aura Request events contain details of requests to Apex methods from Aura and Lightning web components. For example, you can
benchmark request time or identify the URI of an unsuccessful request.

Blocked Redirect Event Type
Blocked redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. The
Blocked Redirect event type is available in the EventLogFile object in API version 63.0 and later.

Bulk API Event Type
Bulk API events contain details about Bulk API requests.


Standard Objects EventLogFile Supported Event Types

Bulk API Request Event Type
The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes.

Bulk API 2.0 Event Type
BulkApi2 events contain details about Bulk API 2.0 requests.

Change Set Operation Event Type
Change Set Operation events contain information from change set migrations.

Composite API Event Type
Composite API events contain details about composite API requests. One composite API event is generated for each composite API
and composite graph API call. This event type is available in API version 64.0 and later.

Composite API Subrequest Event Type
Composite API subrequest events contain details about composite API subrequests. One composite API subrequest event is generated
for each subrequest or collated set of subrequests. For example, if a composite API request contains five subrequests and four of the
subrequests are collated, then two composite API subrequest events are generated. This example also applies to composite graph
API. This event type is available in API version 64.0 and later.

Concurrent Long-Running Apex Limit Event Type
Concurrent Long-Running Apex Limit events contain information about long-running concurrent Apex requests in your org that
Salesforce terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5
seconds are counted towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards
the limit.) When the long-running requests exceed the org default limit, all new Apex invocation requests are denied. This event
type is available in the EventLogFile object in API version 45.0 and later.

Console Event Type
Console events contain information about the performance and use of Salesforce Consoles. The Console events are logged whenever
a Console tab is opened with a sidebar component. Outside of that, when Console tabs are opened, a regular view record detail
event is served just like in Salesforce Classic.

Content Distribution Event Type
Content Distribution events contain information about content distributions and deliveries to users.

Content Document Link Event Type
Content Document Link events contain sharing information for content documents.

Content Transfer Event Type
Content Transfer events contain information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records.

Continuation Callout Summary Event Type
Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction,
their response status codes, execution times, and URL endpoint destinations. This event type is available in the EventLogFile object
in API version 43.0 and later.

CORS Violation Record Event Type
CORS Violation Record events capture information about Cross-Origin Resource Sharing (CORS) violations. Cross-origin requests to
Lightning apps are blocked unless the request comes from a URL listed in your CORS allowlist.

CSP Violation Event Type
CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content
security policy (CSP). The CSP Violation event type is available in the EventLogFile object in API version 63.0 and later.


Standard Objects EventLogFile Supported Event Types

Dashboard Event Type
Dashboard events contain details about report requests from dashboards. These requests are triggered by dashboard refreshes,
subscriptions, and filter changes.

Database Save Event Type
Database Save events track when records are created, updated, or deleted. This object is available in API version 63.0 and later.

Document Attachment Downloads Event Type
Document Attachment Downloads events contain details of document and attachment downloads.

External Cross-Org Callout Event Type
External Cross-Org Callout events represent external data callouts via the cross-org adapter for Salesforce Connect. This event type
is available in the EventLogFile object in API version 40.0 and later.

External Custom Apex Callout Event Type
External Custom Apex Callout events represent external data callouts via custom adapters for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

External Data Source Callout Event Type
External Data Source Callout events represent external data callouts via the Salesforce Connect adapters for Amazon DynamoDB
and Amazon Athena. This event type is available in the EventLogFile object in API version 56.0 and later.

External OData Callout Event Type
External OData Callout events represent external data callouts via the OData 2.0 and OData 4.0 adapters for Salesforce Connect. This
event type is available in the EventLogFile object in API version 40.0 and later.

Flow Execution Event Type
Flow Execution events contain information about flows that were executed including details such as total execution time, number
of interviews, and number of errors.

GraphQL Query Event Type
GraphQL Query events contain information about executed queries, including total execution time, the number of invocations, and
any reported errors.

Group Membership Event Type
Group Membership events capture details about changes to public group and queue membership, such as when members are
added to or removed from the public group or queue.

Hostname Redirects Event Type
Hostname Redirect events contain details about blocked and successful redirections for your previous My Domain hostnames. The
Hostname Redirects event type is available in the EventLogFile object in API version 56.0 and later.

Insecure External Assets Event Type
Insecure External Assets events contain information about external assets. External assets include images or videos accessed by users
over an insecure HTTP protocol. The event lists all your Salesforce pages that contain assets hosted insecurely on third-party sites
that users loaded with a Chrome, Firefox, Microsoft Edge, or Safari browser. The `INSECURE_URI` field contains the URI being
used to load the asset insecurely. The Insecure External Assets event type is available in the EventLogFile object in API version 42.0
and later.

Insufficient Access Event Type
Insufficient Access events contain details about errors relating to insufficient account, case, contact, and opportunity record access,
so that you can troubleshoot and resolve access issues for your users.

Invocable Action Event Type
Invocable Action events capture the calls to Salesforce Invocable Actions. This is particularly useful to monitor actions invoked during
Agentforce flows. This event type is available in API versions 64.0 and later.


Standard Objects EventLogFile Supported Event Types

Knowledge Article View Event Type
Knowledge Article View events contain user activity with your knowledge base.

Lightning Error Event Type
Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile
app. This event type is available in the EventLogFile object in API version 39.0 and later.

Lightning Interaction Event Type
Lightning Interaction events track user actions in Lightning Experience and the Salesforce mobile app, such as the user clicking,
tapping, or scrolling on a page. This event type is available in the EventLogFile object in API version 39.0 and later.

Lightning Logger Event Type
Lightning Logger events contain information from observed Lightning component logs. This event type is available in the EventLogFile
object in API version 58.0 and later.

Lightning Page View Event Type
Lightning Page View events represent information about the page on which the event occurred in Lightning Experience and the
Salesforce mobile app, such as the page's load time. This event type is available in the EventLogFile object in API version 39.0 and
later.

Lightning Performance Event Type
Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This event type is
available in the EventLogFile object in API version 39.0 and later.

Login Event Type
Login events contain details about your org’s user login history.

Login As Event Type
Login As events contain details about what a Salesforce admin did while logged in as another user.

Logout Event Type
Contains details of user sessions ending or being revoked.

Metadata API Operation Event Type
Metadata API Operation events contain details of Metadata API retrieval and deployment requests.

Multiblock Report Event Type
Multiblock Report events contain details about Joined Report reports.

Named Credential Event Type
The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in
the named credential event log file, then you can investigate whether a security breach has occurred. This event type is available in
the EventLogFile object in API version 53.0 and later.

One Commerce Usage Event Type
One Commerce Usage events capture information about your Commerce instance. This event type is available in the EventLogFile
object in API version 51.0 and later.

Package Install Event Type
Package Install events contain details about package installation in the organization.

Permission Update Event Type
Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets
or permission set groups.


Standard Objects EventLogFile Supported Event Types

Platform Encryption Event Type
Platform Encryption event contains information about tenant secret and derived encryption key usage. This event type is available
in API versions 41.0 and later.

Pricing Event Type
Pricing events contain information about pricing procedures that were executed, including details such as pricing procedures used,
the pricing APIs, and pricing details and status.

Queued Execution Event Type
Queued Execution events contain details about queued executions—for example, batch Apex.

Report Event Type
Report events contain information about what happened when a user ran a report. This event type includes all activity that's in the
Report Export event type, plus more. For example, it has user activity for reports exported as both Formatted Report and Details Only
output.

Report Export Event Type
Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports
a report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that
data, see the Report event type.

REST API Event Type
REST API events contain details about REST-specific requests.

Sandbox Event Type
Sandbox events contain details about sandbox copies.

Search Event Type
Search events contain details about the user’s search query. All searches within the app, including Experience Cloud sites, are included.
However, unauthenticated users won’t have a unique Salesforce user ID.

Search Click Event Type
Search Click events contain details about the user’s interaction with the search results in the search results page. Interactions with
search results in the instant result dialog are not recorded by this event. All searches within the app, including Experience Cloud
sites, are included. However, unauthenticated users won’t have a unique Salesforce user ID.

Sites Event Type
Sites events contain details of Site.com requests. Requests can originate from the browser (UI).

SOAP API Event Type
SOAP API events contain details about your org's SOAP API request activity.

Time-Based Workflow Event Type
Time-Based Workflow events contain details about queue activity monitoring.

Transaction Security Event Type
Transaction Security events contain details about policy execution. This event type is supported in API version 55.0 and later.

UI Telemetry Navigation Timing Event Type
UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from
[the UI Telemetry Resource Timing Event on page 2414 and includes requests initiated with either the Fetch API or the XMLHttpRequest](https://fetch.spec.whatwg.org/)
[API. This object is available in API version 61.0 and later.](https://xhr.spec.whatwg.org/)

UI Telemetry Resource Timing Event
UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 61.0 and later.](https://fetch.spec.whatwg.org/)


Standard Objects EventLogFile Supported Event Types

Unique Query Event Type
Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This event type is available in API versions 64.0 and later.

URI Event Type
URI events contain details about user interaction with the web browser UI.

Visualforce Request Event Type
Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI).

Wave Change Event Type
Wave Change events represent route or page changes made in the CRM Analytics user interface. A Wave Change event type is
captured every time the user opens a new CRM Analytics asset or tab, switches between tabs, or changes dashboard pages. Wave
Change events are logged when opening new tabs and switching back to previously opened tabs.

Wave Download Event Type
Wave Download events represent downloads made from lens explorations and dashboard widgets in the CRM Analytics user interface.
A Wave Download event type is captured when a user downloads images ( .png ), Microsoft [®] Excel [®] data ( .xls ), or comma-separated
values ( .csv ) files.

Wave Interaction Event Type
Wave Interaction events represent route or page changes made in the CRM Analytics user interface. A Wave Interaction event type
is captured when a tab is closed. It also collates the interaction statistics over the life of the tab, including total open time, read time,
and so on. These statistics are aggregated as you go to other tabs and return, and logged only once when the tab is closed.

Wave Performance Event Type
Wave Performance events help you track trends in your Analytics performance.

SEE ALSO:

EventLogFile

##### Apex Callout Event Type

Apex Callout events contain details about callouts (external requests) during Apex code execution.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

METHOD

ORGANIZATION_ID

PLANNER_IDENTIFIER

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `ApexCallout` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The HTTP method of the callout.

**Example**
For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
string


Standard Objects EventLogFile Supported Event Types

**Description**
The ID of the agent planner.

```
REQUEST_ID

REQUEST_SIZE

RESPONSE_SIZE

RUN_TIME

SESSION_KEY

STATUS_CODE

SUCCESS

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the callout request body, in bytes.

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
Not used for this event type. Use the `TIME` field instead.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP status code for the response.

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Description**
Indicates if the HTTP callout was sent and a response was
returned (1) or not (0).

```
TIME

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

URI_ID_DERIVED

URL

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds (ms).

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The type of Apex callout.

For example: `REST` or `AJAX` .

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The callout endpoint URL.

**Example**

```
                              www.salesforce.com

```

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Execution Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Apex Execution events contain details about Apex classes that are used.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.


Standard Objects EventLogFile Supported Event Types

```
CALLOUT_TIME

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

ENTRY_POINT

EVENT_TYPE

EXEC_TIME

```

**Type**
Number

**Description**
Time spent waiting on webservice callouts, in milliseconds.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The entry point for this Apex execution.

**Example**

**•** `GeneralCloner.cloneAndInsertRecords`

**•** `VF- /apex/CloneUser`

**Type**
String

**Description**
The type of event. The value is always `ApexExecution` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The end-to-end Apex execution time (in milliseconds).

```
IS_LONG_RUNNING_REQUEST

LOGIN_KEY

NUMBER_SOQL_QUERIES

ORGANIZATION_ID

PLANNER_IDENTIFIER

```

**Type**
Boolean

**Description**
Indicates whether the request is counted against your org’s
concurrent long-running Apex request limit ( `true` ) or not
( `false` ).

Note: Asynchronous Apex jobs (batch, queueable,
scheduled, and future), background processes, and bulk
API requests aren’t counted against the concurrent
long-running limit.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of SOQL queries that were executed during the
event.

This value is the aggregate across all namespaces, and can
exceed the per-namespace limits. For test executions, the
aggregate total value across all test methods executed in the
request is used. If you’re using this value to track limit
consumption, consider filtering out test execution quiddities
(indicated by the QUIDDITY field).

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
string

**Description**
The ID of the agent planner.


Standard Objects EventLogFile Supported Event Types

```
QUIDDITY

```

**Type**
String

**Description**
The type of outer execution associated with this event.

**Example**

**•** `A` –ACS Batch Apex

**•** `B` –Bulk API and Bulk API 2.0

**•** `BA` –Start method of a Batch Apex job

**•** `C` –Scheduled Apex

**•** `CI` –Commerce Integration

**•** `DL`   - Discoverable Login page

**•** `E` –Inbound Email Service

**•** `F` –Future

**•** `FC` –Function Callback

**•** `H` –Apex REST

**•** `I` –Invocable Action

**•** `K` –Quick Action

**•** `L` –Lightning

**•** `M` –Remote Action

**•** `P` –Not used in API version 63.0 and later.

**•** `PEPC` –Platform Event Publish Callback

**•** `PI` –Post install script for a managed package

**•** `Q` –Queueable

**•** `QTXF` –Transaction Finalizer for Queueable

**•** `R` –Synchronous uncategorized (which is where all
transactions not specified elsewhere end up)

**•** `S` –QueryLocator Batch Apex (Batch Apex jobs run faster
when the start method returns a QueryLocator object that
doesn't include related records via a subquery. See Batch
[Apex Best Practices in Using Batch Apex.)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_best_practices)

**•** `TA` –Tests Async

**•** `TD` –Tests Deployment

**•** `TS` –Tests Synchronous

**•** `UD` –Undefined is the default when an event hasn’t been
assigned a more descriptive quiddity.

**•** `V` –Visualforce

**•** `W` –SOAP Webservices

**•** `X` –Execute Anonymous

Note: Implementations of the Process.Plugin interface
use the quiddity value **R** .


Standard Objects EventLogFile Supported Event Types

```
REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered
long-running requests for the purposes of the Concurrent
Long-Running Apex Limit.

Note: HTTP callout processing time isn't included when
calculating the 5-second limit. We pause the timer for
the callout and resume it when the callout completes.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Inline Event Type

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

This event type is reserved for future use. This object is available in API version 66.0 and later.

Note: Because this event type is reserved for future use, it captures no data.

##### Apex REST API Event Type

Apex REST API events capture information about every Apex REST API request.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide. For information about](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)
[Apex REST, see Introduction to Apex REST.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_rest_intro.htm)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CLIENT_IP

CONNECTED_APP_ID

CLIENT_NAME

CPU_TIME

DB_BLOCKS

DB_CPU_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The 15-character ID of the connected app associated with the
API call. For example, `0H4RM00000000Kr0AI` .

**Type**
String

**Description**
The name of the client that’s using Salesforce services.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.


Standard Objects EventLogFile Supported Event Types

```
DB_TOTAL_TIME

ENTITY_NAME

EVENT_TYPE

EXCEPTION_MESSAGE

LOGIN_KEY

MEDIA_TYPE

METHOD

```

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Set

**Description**
API objects that are accessed.

For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
String

**Description**
The type of event. The value is always `ApexRestApi` .

**Type**
String

**Description**
The returned exception message, used to debug issues. Provide
this message when seeking support.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The media type of the response.

**Type**
String

**Description**
The HTTP method of the request.


Standard Objects EventLogFile Supported Event Types

For example: `GET`, `POST`, `PUT`, and so on.

```
NUMBER_FIELDS

ORGANIZATION_ID

QUERY

REQUEST_SIZE

REQUEST_STATUS

```

**Type**
Number

**Description**
The number of fields or columns, where applicable.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The data that was queried.

**Type**
Number

**Description**
The size of the callout request body, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.


Standard Objects EventLogFile Supported Event Types

```
REQUEST_ID

RESPONSE_SIZE

ROWS_PROCESSED

RUN_TIME

SESSION_KEY

STATUS_CODE

TIMESTAMP

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP status code for the response.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Number

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex SOAP Event Type

Apex SOAP events contain details about custom SOAP web service calls.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CLASS_NAME

CLIENT_IP

CLIENT_NAME

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

```

**Type**
String

**Description**
The Apex class name. If the class is part of a managed package,
this string includes the package namespace.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The name of the client that’s using Salesforce services. This
field is an optional parameter that can be passed in API calls.
If blank, the caller didn't specify a client in the CallOptions
header.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The type of event. The value is always `ApexSoap` .


Standard Objects EventLogFile Supported Event Types

```
LIMIT_USAGE_PERCENT

LOGIN_KEY

METHOD_NAME

ORGANIZATION_ID

QUERY

REQUEST_ID

REQUEST_STATUS

```

**Type**
Number

**Description**
The percentage of Apex SOAP calls that were made against
the organization’s limit.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The name of the calling Apex method.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The SOQL query, if one was performed.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.


Standard Objects EventLogFile Supported Event Types

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered
long-running requests for the purposes of the Concurrent
Long-Running Apex Limit.

Note: HTTP callout processing time isn't included when
calculating the 5-second limit. We pause the timer for
the callout and resume it when the callout completes.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers


Standard Objects EventLogFile Supported Event Types

and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Trigger Event Type

Apex Trigger events contain details about triggers that fire in an organization.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

```

**Type**
String

**Description**
The ID of the bot.


Standard Objects EventLogFile Supported Event Types

```
BOT_SESSION_IDENTIFIER

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

ENTITY_NAME

EVENT_TYPE

EXEC_TIME

```

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Description**
The IP address of the client that is using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds is used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The name of the object affected by the trigger.

**Type**
String

**Description**
The type of event. The value is always `ApexTrigger` .

**Type**
Number

**Description**
The end-to-end Apex execution time (in milliseconds).


Standard Objects EventLogFile Supported Event Types

```
LOGIN_KEY

ORGANIZATION_ID

PLANNER_IDENTIFIER

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
ID

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.


Standard Objects EventLogFile Supported Event Types

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

TRIGGER_ID

TRIGGER_NAME

```

**Type**
Number

**Description**
This field is always null. To view the end-to-end Apex execution
time (in milliseconds), refer to the `EXEC_TIME` field.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

**Type**
String

**Description**
The 15-character ID of the trigger that was fired.

**Type**
String

**Description**
For triggers coming from managed packages,
`TRIGGER_NAME` includes a namespace prefix separated
with a `.` character. If no namespace prefix is present, the
trigger is from an unmanaged trigger.


Standard Objects EventLogFile Supported Event Types

Examples:

**•** `examplePackage.managedExampleTrigger`                              Managed trigger from the examplePackage namespace

**•** `unmanagedExampleTrigger`                              - Unmanaged trigger

```
TRIGGER_TYPE

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The type of this trigger.

**Possible Values**

**•** AfterInsert

**•** AfterUpdate

**•** BeforeInsert

**•** BeforeUpdate

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
ID

**Description**
The 15-character ID of the user who is using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .


Standard Objects EventLogFile Supported Event Types

```
USER_TYPE

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.


Standard Objects EventLogFile Supported Event Types

##### Apex Unexpected Exception Event Type

The Apex Unexpected Exception event type captures information about unexpected exceptions in Apex code execution. This event type
is available in the EventLogFile object in API version 45.0 and later. Unexpected exception information is not captured in the EventLogFile
object with `@IsTest` and anonymous Apex.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

EXCEPTION_CATEGORY

```

**Type**
String

**Description**
The type of event. The value is always `ApexUnexpectedException` .

**Type**
String

**Description**
The category of the unexpected Apex exception. Provides a breakdown of unhandled
exceptions based on the type. For example, the `LimitException` exception type is
split into subcategories that indicate if you exceeded a limit, such as the total heap size or
CPU time.

Possible values:

**•** Subcategories of `LimitException` that indicate the Apex limit you’ve exceeded.
Examples:

**–** `LimitException: CpuTime` : Maximum CPU time on the Salesforce servers.

**–** `LimitException: HeapSize` : Total heap size.

**–** `LimitException: Queries` : Total number of SOQL queries issued.

**–** `LimitException: QueryRows` : Total number of records retrieved by SOQL
queries.

**–** `LimitException: DmlStatements` : Total number of DML statements
issued.

**–** `LimitException: Callouts` : Total number of callouts (HTTP requests or
web services calls) in a transaction.

[See Execution Governors and Limits for other limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**•** `CustomException` [: Unhandled custom exception.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_exception_custom.htm)

**•** [An Apex exception that isn’t limit-related; see Exception Class and Built-In Exceptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

This field is available in API version 57.0 and later.

**Example**

```
  LimitException: CpuTime

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
EXCEPTION_MESSAGE

EXCEPTION_TYPE

ORGANIZATION_ID

REQUEST_ID

STACK_TRACE

TIMESTAMP

```

**Type**
Text

**Description**
The exception’s message.

**Example**
Divide by 0

**Type**
String

**Description**
The class type of the unexpected exception.

**Example**

```
  System.MathException

```

**Type**
Id

**Description**
The 15-character ID of the org.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Text

**Description**
The stack trace for the exception.

Note: If the exception is thrown from a managed package, `STACK_TRACE` is
omitted.

**Example**

```
  Class.OpportunityUtility.insert: line 22, column 1

  AnonymousBlock: line 1, column 1

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2024-08-08T06:08:02.755+0000` .

```
TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

EventLogFile Supported Event Types

EventLogFile

##### API Total Usage

API Total usage events contain details about Platform SOAP API, Platform REST API, and Bulk API requests.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

API_CLIENT_CATEGORY

**Type**
String

**Description**
The category of the client making the API request.

Possible values are:


Standard Objects EventLogFile Supported Event Types

**•** `AGENTFORCE_AGENT` —API request is from an
Agentforce agent.

**•** `EXTERNAL_APPLICATION` —API request is from an
external app defined in the org.

**•** `LIGHTNING_UI` —API request is from the Lightning UI.

**•** `SALESFORCE` —API request is from an internal Salesforce
app or service.

**•** `UNKNOWN` —API request is from an unrecognized category.

**•** `SALESFORCE_HOSTED_MCP` —API request is from a
Salesforce Hosted MCP Server.

```
API_FAMILY

API_RESOURCE

API_VERSION

CLIENT_IP

CLIENT_NAME

```

**Type**
String

**Description**
The API family. Possible values are `REST`, `SOAP`, `Bulk`,
`ApexREST`, `DirectApexREST` or `DirectAura` .
`ApexREST` indicates an Apex REST call. `DirectApexREST`
indicates an Apex REST Agent Action call. `DirectAura`
indicates an AuraEnabled Apex Agent Action call.

**Type**
String

**Description**
The API method or resource. For example,
`describeSObjects` for SOAP, or

```
   /v21.0/sobjects/Account/001xx000003DGQW
```

for REST.

**Type**
Number

**Description**
The API version. For example, `21.0` .

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The name of the client making the API request. Includes values
passed via the Sforce-Call-Options header.

```
CONNECTED_APP_ID

CONNECTED_APP_NAME

COUNTS_AGAINST_API_LIMIT

ENTITY_NAME

EVENT_TYPE

HTTP_METHOD

```

**Type**
String

**Description**
The ID of the connected app making the API request.

If the connected app ID includes the prefix _`0H4`_, append it to
the connected app ID in the My Domain URL to access app
details
( `https://` _**`MyDomainName`**_ `.my.salesforce.com/` _**`0H4`**_ `xxxxxxxxxxxx` ).
If, however, the connected app ID uses the prefix _`888`_, contact
Salesforce Customer Support for app details.

**Type**
String

**Description**
The name of the connected app making the API request.

**Type**
Boolean

**Description**
Whether the request counted against the API limit ( `true` ) or
not ( `false` ).

**Type**
Set

**Description**
The name of the object accessed by the API request.

For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
String

**Description**
The type of event. The value is always `ApiTotalUsage` .

**Type**
String

**Description**
The HTTP method. For example, `GET` .


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

REQUEST_ID

STATUS_CODE

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_NAME

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The HTTP response status code for the request.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the API.

For example: `00530000009M943`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The username of the user who's using Salesforce services
through the API.

##### Asynchronous Report Run Event Type

Asynchronous Report Run events are created for reporting requests that are scheduled. This category includes dashboard refreshes,
asynchronous reports, schedule reports, and analytics snapshots.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
AVERAGE_ROW_SIZE

CLIENT_IP

CPU_TIME

DASHBOARD_ID

```

**Type**
Number

**Description**
The average row size of all rows in the Asynchronous Report
Run event, in bytes. A large average size, coupled with a high
`ROW_COUNT`, can indicate that a user is downloading
information for fraudulent purposes. For example, a salesperson
who downloads all sales leads before departing for a
competitor.

**Example**

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the dashboard that was run.

```
DB_TOTAL_TIME

DB_BLOCKS

DB_CPU_TIME

DISPLAY_TYPE

ENTITY_NAME

EVENT_TYPE

```

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
String

**Description**
The report display type, indicating the run mode of the report.

Possible values are:

**•** `D` —Dashboard

**•** `S` —Show Details

**•** `H` —Hide Details

**Type**
String

**Description**
The name of the object affected by the trigger.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always
`AsynchronousReportRun` .

```
LOGIN_KEY

NUMBER_BUCKETS

NUMBER_COLUMNS

NUMBER_EXCEPTION_FILTERS

ORGANIZATION_ID

ORIGIN

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of buckets that were used in the report.

**Type**
Number

**Description**
The number of columns in the report.

**Type**
Number

**Description**
The number of exception filters that are used in the report.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The context in which the report executed, such as from a UI
(Classic, Lightning, Mobile), through an API (synchronous,
asynchronous, Apex), or through a dashboard.

**Possible Values**

**•** `ReportOpenedFromMobileDashboard` : Report
executed when a user clicked a dashboard component on
a mobile device and drilled down to a report.


Standard Objects EventLogFile Supported Event Types

**•** `DashboardComponentUpdated` : Report executed
when a user refreshed a dashboard component.

**•** `DashboardComponentPreviewed` : Report
executed from a Lightning dashboard component preview.

**•** `ReportRunUsingSynchronousApi` : Report
executed from a synchronous API.

**•** `ReportRunUsingAsynchronousApi` : Report
executed from an asynchronous API.

**•** `ReportRunUsingApexSynchronousApi` : Report
executed from the synchronous Apex API.

**•** `ReportRunUsingApexAsynchronousApi` : Report
executed from the asynchronous Apex API.

**•** `ReportExported` : Report executed from a printable
view or report export that was not asynchronous nor an
API export.

**•** `ReportRunFromClassic` : Report executed from the
Run Report option of Salesforce Classic.

**•** `ReportRunFromMobile` : Report executed from the
Run Report option of the mobile Salesforce app.

**•** `ReportRunFromLightning` : Report executed from
the Run option in Lightning Experience from a non-mobile
browser.

**•** `ReportRunFromRestApi` : Report executed from the
REST API.

**•** `ReportPreviewed` : Report executed when a user got
preview results while using the report builder.

**•** `ReportScheduled` : Report was scheduled.

**•** `ProbeQuery` : Report executed from a probe query.

**•** `ReportRunFromReportingSnapshot` : Report
executed through Snapshot Analytics.

**•** `ReportExportedAsynchronously` : Report was
exported asynchronously.

**•** `ReportExportedUsingExcelConnector` : Report
was exported using the Excel connector.

**•** `ChartRenderedOnVisualforcePage` : Report
executed from a rendered chart on a VisualForce Page.

**•** `ChartRenderedInEmbeddedAnalyticsApp` :
Report executed from a rendered chart in an embedded
Analytics app.

**•** `ReportRunAndNotificationSent` : Report
executed through the notifications API.

**•** `ChartRenderedOnHomePage` : Report executed from
a rendered chart on the home page.


Standard Objects EventLogFile Supported Event Types

**•** `ReportResultsAddedToWaveTrending` : Report
executed when a user trended a report in CRM Analytics.

**•** `ReportAddedToCampaign` : Report was added from
an Add to Campaign action.

**•** `ReportResultsAddedToEinsteinDiscovery` :
Report executed synchronously from Einstein Discovery.

**•** `Unknown` : Report execution origin is unknown.

**•** `Test` : Report execution resulted from a test.

```
RENDERING_TYPE

REPORT_ID

REPORT_ID_DERIVED

REQUEST_ID

```

**Type**
String

**Description**
Describes the format of the report output in Salesforce Classic.
If the report was exported in Lightning Experience, this field is
blank.

**Possible Values**

**•** `W` : Web (HTML)

**•** `E` : Email

**•** `P` : Printable

**•** `X` : Excel

**•** `C` : Comma-separated values (CSV)

**•** `J` : JavaScript Object Notation (JSON)

**•** `D` : Dummy data

**Type**
Id

**Description**
The 15-character ID of the report that was run.

**Type**
Id

**Description**
The 18-character case insensitive ID of the report that was run.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
REQUEST_STATUS

ROW_COUNT

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The number of rows that were processed in the Asynchronous
Report Run event. High row counts, coupled with a high
`AVERAGE_ROW_SIZE`, can indicate that a user is
downloading information for fraudulent purposes. For example,
a salesperson who downloads all sales leads before departing
for a competitor.

**Example**

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .


Standard Objects EventLogFile Supported Event Types

```
SORT

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The sort column and order that was used in the report.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.


Standard Objects EventLogFile Supported Event Types

For example: `00590000000I1SNIA0` .

```
USER_TYPE

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.


Standard Objects EventLogFile Supported Event Types

##### Aura Request Event Type

Aura Request events contain details of requests to Apex methods from Aura and Lightning web components. For example, you can
benchmark request time or identify the URI of an unsuccessful request.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION_MESSAGE

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

EASY_SUITE_VALUE

```

**Type**
String

**Description**
The action (Apex method) names and times for all the actions
in the request in the format:

```
   action1Name=action1Time;action2Name=action2Time...

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The org’s Small Business Suite Edition, if applicable. This field
populates only for Small Business Suite editions and Salesforce
Foundations. Otherwise, it will be empty. Available in API
version 66.0 and later.

For example:

**•** `Freemium` —Salesforce Free Suite

**•** `Starter` —Salesforce Starter Suite

**•** `Pro` —Salesforce Pro Suite

**•** `C360SuiteEE` —Salesforce Foundations

```
EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REQUEST_ID

REQUEST_METHOD

```

**Type**
String

**Description**
The type of event. The value is always `AuraRequest` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Example**

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The HTTP method of the request, such as GET or POST.


Standard Objects EventLogFile Supported Event Types

```
REQUEST_STATUS

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
URI

URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URI of the resource that’s receiving the request.

For example: `/aura` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
String

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:


Standard Objects EventLogFile Supported Event Types

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Blocked Redirect Event Type

Blocked redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. The Blocked
Redirect event type is available in the EventLogFile object in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The blocked redirects event is available in the API but not in the
Event Monitoring Analytics app.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Blocked redirect events capture these redirections when the target URL isn’t a RedirectWhitelistUrl or when the target URL fails a syntax
check.


Standard Objects EventLogFile Supported Event Types

**•** An anchor link within a page or component that includes a redirection. For example, `<a`

`href="/?startURL=targetUrl">linkText</a>` includes a redirection via the startURL parameter.

**•** A parameter within a page that redirects the user. For example, this form action redirects the user through the saveURL parameter:
`<form action="/xyz?saveURL=targetURL">` .

Within pages and components, a direct anchor link to an external URL is always allowed, even if the target URL isn’t a RedirectWhitelistUrl.
For those direct anchor links, if the target URL fails a syntax check, the user receives an error but the redirection isn’t captured as a blocked
redirect event. An example of a direct anchor link is `<a` `href="targetUrl">linkText</a>` .

For hyperlinks within URL and Long Text Area fields, blocked redirections to untrusted URLs are captured as blocked redirect events only
when the user who clicked the hyperlink accessed Salesforce via Salesforce Classic. If those users see a warning message and can proceed
to the untrusted URL, that event isn’t captured as a blocked redirect event.

Note: To help preserve performance, Salesforce uses throttling, a technique that limits the number of generated blocked redirect
events when the volume is exceptionally high. Therefore, if your org generates a high volume of blocked redirections over a short
period of time, some of those redirections can fail to generate a blocked redirect event.

Fields

**Field** **Details**

```
BLOCKED_URI

BLOCKED_URI_DOMAIN

EVENT_TYPE

MALFORMED_URL

```

**Type**
String

**Description**
The full string of the target for the redirection.

**Example**
https://www.example.com/shop.htm

**Type**
String

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow future redirections to the
`BLOCKED_URI`, `BLOCKED_URI_DOMAIN` [is the value to add to RedirectWhitelistUrl.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm?q=%22Trusted%20URL%22)

**Example**
www.example.com

**Type**
String

**Description**
The type of event. The value is always `BlockedRedirect` .

**Type**
Boolean

**Description**
Indicates whether this redirection was blocked because the target URL failed a syntax check
( `1` ) or not ( `0` ).

Here are examples of malformed URLs.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** https://www.example.com/$t61'3

**•** https://malformed^url.example.com

```
ORIGIN

REFERRER

REMOTE_ADDRESS

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The origin that caused the request to the `BLOCKED_URI` . For example, if a form on an
Experience Cloud Visualforce site page redirects a user to an untrusted URL via the `saveURL`
parameter, `ORIGIN` contains the base URL of that site.

**Type**
String

**Description**
The absolute or partial address from which the request to the `BLOCKED_URI` came. The
`Referrer-Policy` HTTP Header of the request determines how much of the URL is
shared.

**Type**
String

**Description**
Remote IP address of the client making the request.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  0000000062_0000x8Lz
```

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   2022-07-27T11:32:59.555Z.

```

Usage

Only one blocked redirect log file is available at a time. When the daily incremental event log file is generated during the daily background
process, the new file replaces the existing file.

If the log file doesn’t exist, either the log generation process hasn’t run yet or there’s no redirection data to report for that 24-hour
window. The log file is generated only when at least one redirection occurred for the day.

To collect blocked redirect logs for multiple days, schedule a daily query of the Blocked Redirect event type via REST API. For example,
you can configure a cron job in Unix or a scheduled task in Windows to run the query.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Bulk API Event Type

Bulk API events contain details about Bulk API requests.

Note: This event type does not include Bulk API 2.0 requests. For information about the BulkApi2 event type, see Bulk API 2.0
Event Type on page 2159.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BATCH_ID

CLIENT_IP

```

**Type**
String

**Description**
The 15-character ID of the Bulk API batch.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

ENTITY_TYPE

EVENT_TYPE

JOB_ID

LOGIN_KEY

MESSAGE

NUMBER_FAILURES

OPERATION_TYPE

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of entity that the Bulk API used.

**Type**
String

**Description**
The type of event. The value is always `BulkApi` .

**Type**
String

**Description**
The 15-character ID of the Bulk API job.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
EscapedString

**Description**
Any success or error message that’s associated with the request.

**Type**
Number

**Description**
The number of failures that were returned with the request.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of Bulk API operation that was performed.

```
ORGANIZATION_ID

REQUEST_ID

ROWS_PROCESSED

RUN_TIME

SESSION_KEY

SUCCESS

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Boolean

**Description**
Whether the batch was successful.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .


Standard Objects EventLogFile Supported Event Types

##### Bulk API Request Event Type

The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes.

Note: This event type doesn’t include Bulk API 2.0 requests. For information about the BulkApi2 event types, see Bulk API 2.0
Event Type on page 2159.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_VERSION

BATCH_ID

CLIENT_IP

CLIENT_NAME

CONCURRENCY_MODE

CONNECTED_APP_ID

```

**Type**
Number

**Description**
The API version.

**Type**
String

**Description**
The 15-character ID of the Bulk API batch.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
EscapedString

**Description**
The name of the client making the request.

**Type**
String

**Description**
The concurrency mode selected by the user.

**Type**
String

**Description**
The ID of the connected app making a request.


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

ERROR_MESSAGE

EVENT_TYPE

JOB_ID

LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

REQUEST_ID

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
EscapedString

**Description**
The type of entity that the Bulk API used.

**Type**
String

**Description**
The type of event. The value is always BulkApiRequest.

**Type**
String

**Description**
The 15-character ID of the Bulk API job.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of Bulk API operation.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_PATH

RUN_TIME

SESSION_KEY

STATUS_CODE

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The path of the request.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP Status code indicating whether the batch was
successful.

**Type**
Boolean

**Description**
Whether the batch was successful.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

##### Bulk API 2.0 Event Type

```

BulkApi2 events contain details about Bulk API 2.0 requests.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
Id

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The ID of the user making the request.

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Note: This event type does not include Bulk API requests. For information about the BulkApi event type, see Bulk API Event Type
on page 2152.

You can monitor the following Bulk API 2.0 parameters:

**•** The type of data processed via Bulk API 2.0 operations, and how much of that data was processed.

**•** Bulk API 2.0 limits.

**•** For jobs, track how long it takes to complete, database, and CPU usage.

**•** Understand users and the operations they performed.

**•** Detailed errors and failures.


Standard Objects EventLogFile Supported Event Types

BulkApi2 events represent the steps in the Bulk API 2.0 workflow and changes in job state.

For a Bulk API 2.0 **Ingest** job, an event is emitted when a job is marked:

**•** created

**–** Note: For multi-part requests, there is no “created” event emitted, only an uploadComplete event.

**•** uploadComplete

**•** inProgress

**•** with a processing update

**•** complete

**•** aborted

**•** deleted

For a Bulk API 2.0 **Query** job, an event is emitted when a job is marked:

**•** created

**•** uploadComplete

**•** inProgress

**•** with a processing update

**•** complete

**•** aborted

**•** deleted

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

ENTITY_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal
IP (such as a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates
the amount of activity taking place in the app server layer.

**Type**
String

**Description**
The type of entity that Bulk API 2.0 used.


Standard Objects EventLogFile Supported Event Types

For example, `Account` or `Contact` .

```
EVENT_TYPE

JOB_ID

JOB_STATUS

LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

RECORDS_FAILED

RECORDS_PROCESSED

```

**Type**
String

**Description**
The type of event. The value is always `BulkApi2` .

**Type**
String

**Description**
The 15-character ID of the Bulk API 2.0 job.

**Type**
String

**Description**
The job’s current status.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with
a login event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of Bulk API 2.0 operation that was performed.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Number

**Description**
The total number of records that failed.

For example: `150` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
Number of records processed for this event.

For example: `980` .

Note: The number of records processed is reported differently for ingest
and query jobs.

For _ingest_ jobs:

**•** Events with a status of `InProgress` report (if applicable) the number
of records processed.

For _query_ jobs:

**•** Events with a status of `JobComplete` or `InProgress` report (if
applicable) the number of records processed.

```
RESULT_SIZE_MB

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
Number

**Description**
Number of megabytes returned in query. Empty for ingest jobs.

For example: `670` .

Note: RESULT_SIZE_MB currently does not emit events, but is shown here
as a placeholder for future enhancement.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.
Each event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events
within a session. When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case-safe ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or
the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case-safe ID of the user who’s using Salesforce services through
the UI or the API.

For example: `00590000000I1SNIA0` .

##### Change Set Operation Event Type

Change Set Operation events contain information from change set migrations.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CHANGE_SET_NAME

CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

OPERATION

```

**Type**
String

**Description**
The name of the change set.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always
`ChangeSetOperation` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The operation that’s being performed.

**Possible Values**

**•** DELETE


Standard Objects EventLogFile Supported Event Types

**•** DEPLOY

**•** UPLOAD

**•** VALIDATE

```
ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TARGET_ORG_ID

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Id

**Description**
The 15-character ID of the organization that’s receiving the
change set.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Composite API Event Type

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Composite API events contain details about composite API requests. One composite API event is generated for each composite API and
composite graph API call. This event type is available in API version 64.0 and later.


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

ALL_OR_NONE

CLIENT_IP

CPU_TIME

EVENT_TYPE

FAILURE_REASON

IS_REQUEST_COLLATION_ON

LOGIN_KEY

NUM_GRAPH_DEPTH

**Type**
boolean

**Description**
Indicates whether the entire request is rolled back when the update of any object fails (true),
or if the call should continue with the independent update of other objects in the request
(false). The default is false. If true, it overrides the ALL_OR_NONE setting in subrequests.

**Type**
String

**Description**
The IP address of the client that’s using the API.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request.

**Type**
String

**Description**
The type of the event. The value is always CompositeApi.

**Type**
String

**Description**
An error code giving the reason for a failed request.

**Type**
boolean

**Description**
The setting for subrequest collation.

**Type**
String

**Description**
Identifies all related events in a given user’s login session. It starts with a login event and
ends with either a logout event or the user session expiring. For example:

```
  GeJCsym5eyvtEK2I

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The depth of the graph. When multiple graphs are present, this number is the depth of the
deepest graph.

NUM_RETRIES

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

**Type**
Number

**Description**
Number of attempted retries while processing the graph.

**Type**
Id

**Description**
The 15-character ID of the organization that made the request. For example:

```
  00D000000000123

```

**Type**
String

**Description**
A unique ID identifying the composite API request.

**Type**
Number

**Description**
The amount of time in milliseconds to complete the request.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
For example: `20130715233322.670`

**Type**
String

**Description**
The date and time that the event was generated.

**Type**
DateTime

**Description**
The date and time, in ISO8601-compatible format (YYYY-MM-DDTHH:MM:SS.sssZ), that the
event was generated. The timezone is GMT. For example:

```
  2015-07-27T11:32:59.555Z

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

SEE ALSO:

**Type**
String

**Description**
The resource URI.

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user that’s using the API. For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user that’s using the API. For example:

```
  00590000000I1SNIA0

```

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_composite_composite.htm)_ : Composite

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_composite_graph.htm)_ : Composite Graph

_REST API Developer Guide_ [: Using Composite Resources](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/using_composite_resources.htm)

##### Composite API Subrequest Event Type

Composite API subrequest events contain details about composite API subrequests. One composite API subrequest event is generated
for each subrequest or collated set of subrequests. For example, if a composite API request contains five subrequests and four of the
subrequests are collated, then two composite API subrequest events are generated. This example also applies to composite graph API.
This event type is available in API version 64.0 and later.

Fields

**Field** **Details**

CANCELLED_REASON

**Type**
String

**Description**
If the subrequest was canceled, shows the reason.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

INITIAL_REFERENCE_IDS

IS_CANCELLED

LOGIN_KEY

METHOD

**Type**
String

**Description**
The IP address of the client that’s using the API.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request.

**Type**
Number

**Description**
Time (in nanoseconds) spent waiting for database processing in aggregate for all operations
in the subrequest or set of collated subrequests. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
String

**Description**
The type of the event. The value is always CompositeApiSubrequest.

**Type**
String

**Description**
The original reference IDs of subrequests that were collated into the current subrequest.

**Type**
boolean

**Description**
True if the subrequest call was canceled.

**Type**
String

**Description**
Identifies all related events in a given user’s login session. It starts with a login event and
ends with either a logout event or the user session expiring. For example:

```
  GeJCsym5eyvtEK2I

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The HTTP method of the request.

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

RUN_TIME

SESSION_KEY

STATUS_CODE

**Type**
Id

**Description**
The 15-character ID of the organization that made the request. For example:

```
  00D000000000123

```

**Type**
String

**Description**
A unique ID identifying the composite API request.

**Type**
String

**Description**
The status of the subrequest or collated set of subrequests. For example:

**•** S—Success. Salesforce handled the request successfully. If an Apex controller throws an
exception, this status is also returned.

**•** F—Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** U—Undefined

**•** A—Authorization Error

**•** R—Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** N—Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time in milliseconds to complete the request.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
For example: `20130715233322.670`

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The HTTP status code for the response.

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

**Type**
boolean

**Description**
True if the subrequest call succeeded.

**Type**
String

**Description**
The date and time that the event was generated.

**Type**
DateTime

**Description**
The date and time, in ISO8601-compatible format (YYYY-MM-DDTHH:MM:SS.sssZ), that the
event was generated. The timezone is GMT. For example:

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
The resource URI.

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user that’s using the API. For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user that’s using the API. For example:

```
  00590000000I1SNIA0

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

USER_TYPE

SEE ALSO:

**Type**
String

**Description**
The category of user license. Possible values are:

**•** CsnOnly—Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** CspLitePortal—CSP Lite Portal license. Users whose access is limited because they’re
organization customers and they access the application through a customer portal or
an Experience Cloud site.

**•** CustomerSuccess—Customer Success license. Users whose access is limited because
they’re organization customers and they access the application through a customer
portal.

**•** Guest—Users whose access is limited so that your customers can view and interact with
your site without logging in.

**•** PowerCustomerSuccess—Power Customer Success license. Users whose access is limited
because they’re organization customers and they access the application through a
customer portal. Users with this license type can view and edit data that they directly
own or data owned by or shared with users below them in the customer portal role
hierarchy.

**•** PowerPartner—Power Partner license. Users whose access is limited because they’re
partners and they typically access the application through a partner portal or site.

**•** SelfService—Users whose access is limited because they’re organization customers and
they access the application through a self-service portal.

**•** Standard—Standard user license. This user type also includes Salesforce Platform and
Salesforce Platform One user licenses and admins for this org.

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_composite_composite.htm)_ : Composite

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_composite_graph.htm)_ : Composite Graph

_REST API Developer Guide_ [: Using Composite Resources](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/using_composite_resources.htm)

##### Concurrent Long-Running Apex Limit Event Type

Concurrent Long-Running Apex Limit events contain information about long-running concurrent Apex requests in your org that Salesforce
terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted
towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the
long-running requests exceed the org default limit, all new Apex invocation requests are denied. This event type is available in the
EventLogFile object in API version 45.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
EVENT_TYPE

NUMBER_REQUESTS

ORGANIZATION_ID

REQUEST_ID

REQUEST_URI

REQUESTS_LIMIT

```

**Type**
String

**Description**
The type of event. The value is always `ConcurrentLongRunningApexLimit` .

**Type**
Number

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
URI of the long-running Apex request that Salesforce terminated.

**Example**
/apex/ApexClassName

**Type**
Number

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `NUMBER_REQUESTS` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.)

See _Apex Developer Guide_ [: Lightning Platform Apex Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section)

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

Usage

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

For example, you can monitor Concurrent Long-Running Apex Limit log counts to get a benchmark or plot a count by hour. To identify
where the limit was exceeded, see the REQUEST_URI field. Then, cross-reference this data with Apex Execution event data where the
average RUN_TIME exceeds 5 seconds. To identify synchronous requests only, cross-reference event data with the QUIDDITY field in
Apex Execution event data. For example, QUIDDITY NOT IN (A,BA,F,Q,S) and CALLOUT_TIME (>5000).

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

_Salesforce Developers Blog_ [: Designing Force.com Applications That Avoid Hitting Concurrent Request Limits](https://developer.salesforce.com/blogs/engineering/2013/05/force-com-concurrent-request-limits.html)

##### Console Event Type

Console events contain information about the performance and use of Salesforce Consoles. The Console events are logged whenever
a Console tab is opened with a sidebar component. Outside of that, when Console tabs are opened, a regular view record detail event
is served just like in Salesforce Classic.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

COMPONENT_ID

COMPONENT_ID_DERIVED

CONSOLE_ID

CONSOLE_ID_DERIVED

CPU_TIME

DB_TOTAL_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Id

**Description**
The 15-character ID of the component.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the component.

**Type**
Id

**Description**
The 15-character ID of the console.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the console.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LICENSE_CONTEXT

LOGIN_KEY

ORGANIZATION_ID

RECORD_ID

RECORD_ID_DERIVED

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `Console` .

**Type**
String

**Description**
The license context in which a user is using a console.

**Example**
service, salesandservice, sales

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the record that’s associated with the
console.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the record that’s
associated with the console.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_STATUS

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.


Standard Objects EventLogFile Supported Event Types

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Distribution Event Type

Content Distribution events contain information about content distributions and deliveries to users.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The action that’s used when a delivery is viewed.

**Possible Values**

**•** `VIEW`

**•** `INSERT`

**•** `UPDATE`

```
DELIVERY_ID

DELIVERY_LOCATION

EVENT_TYPE

ORGANIZATION_ID

RELATED_ENTITY_ID

REQUEST_ID

```

**Type**
Id

**Description**
The 15-character ID of the content delivery.

**Type**
String

**Description**
The location of the delivery.

**Type**
String

**Description**
The type of event. The value is always
`ContentDistribution` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the record that’s associated with the
delivery distribution.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

VERSION_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Document Link Event Type

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The 15-character ID of the content version.

Content Document Link events contain sharing information for content documents.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
DOCUMENT_ID

EVENT_TYPE

ORGANIZATION_ID

REQUEST_ID

SHARED_WITH_ENTITY_ID

SHARING_OPERATION

```

**Type**
Id

**Description**
The 15-character ID of the document that’s being shared.

**Type**
String

**Description**
The type of event. The value is always
`ContentDocumentLink` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Id

**Description**
Who the document was shared with.

**Type**
String

**Description**
The type of sharing operation on the document.

**Possible Values**

**•** `INSERT`

**•** `UPDATE`

**•** `DELETE`


Standard Objects EventLogFile Supported Event Types

```
SHARING_PERMISSION

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
What permissions the document was shared with.

**Possible Values**

**•** `V` : Viewer

**•** `C` : Collaborator

**•** `I` : Inferred—that is, the sharing permissions were inferred
from a relationship between the viewer and document.
For example, a document’s owner has a sharing permission
to the document itself. Or, a document can be a part of a
content collection, and the viewer has sharing permissions
to the collection rather than explicit permissions to the
document directly.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.


Standard Objects EventLogFile Supported Event Types

For example: `00590000000I1SNIA0` .

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Transfer Event Type

Content Transfer events contain information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
DOCUMENT_ID

DOCUMENT_ID_DERIVED

EVENT_TYPE

FILE_PREVIEW_TYPE

FILE_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the document that’s being shared.

**Type**
Id

**Description**
The 18-character case insensitive ID of the document that’s
being shared.

**Type**
String

**Description**
The type of event. The value is always `ContentTransfer` .

**Type**
String

**Description**
The content type of the file preview.

**Type**
String

**Description**
The content type of the file version.


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

REQUEST_ID

SIZE_BYTES

TIMESTAMP

TIMESTAMP_DERIVED

TRANSACTION_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the file transfer, in bytes.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The operation that was performed, including operations on
files and attachments to records. For example, you can track
operations in the Attachments related list on a case.

**Possible Values**

**•** `VersionDownloadAction` and
`VersionDownloadApi` represent downloads via the
user interface and API respectively.


Standard Objects EventLogFile Supported Event Types

**•** `VersionRenditionDownload` represents a file
preview action.

**•** `saveVersion` represents a file that’s being uploaded.

```
USER_ID

USER_ID_DERIVED

VERSION_ID

VERSION_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Continuation Callout Summary Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The 15-character ID of the content version.

**Type**
Id

**Description**
The 18-character case insensitive ID of the content version.

Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction, their
response status codes, execution times, and URL endpoint destinations. This event type is available in the EventLogFile object in API
version 43.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CONTINUATION_ID

DURATION

EVENT_TYPE

ORGANIZATION_ID

ORIGIN_REQUEST_ID

REQUEST_FORM_SIZE

REQUEST_ID

```

**Type**
String

**Description**
A unique ID identifying a sequence of events within a request.

**Example**
SFDC-Continuation-14e3cg85-961d-389e-7bz1-3d171543162a

**Type**
Number

**Description**
Total duration of continuation, in milliseconds.

**Type**
String

**Description**
The type of event. The value is always `ContinuationCalloutSummary` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The ID of the request that initiated a callout.

**Example**
TID:5ILoVKlztX_rDDJcp7

**Type**
String

**Description**
Continuation request form size, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
RESPONSE_SIZE

STATUS_CODE

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The size of the callout response, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
String

**Description**
The HTTP status or internal code returned by the remote endpoint. A status code of 200
indicates that the request was successful. Other status code values indicate the type of
problem that was encountered. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Examples**

**•** 2000—The timeout was reached, and the server didn’t get a chance to respond.

**•** 2001—There was a connection failure.

**•** 2002—Exceptions occurred.

**•** 2003—The response hasn’t arrived (which also means that the Apex asynchronous
callout framework hasn’t resumed).

**•** 2004—The response size is too large (greater than 1 MB).

**Type**
Boolean

**Description**
Indicates whether the continuation was successful ( `1` ) or not ( `0` ).

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
URL

USER_ID

USER_ID_DERIVED

VF_CONTROLLER_SIZE

```

SEE ALSO:

**Type**
String

**Description**
The callout endpoint URL. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Example**
http://prod.location.amazonaws.com:1000/orders/order/_search

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
Continuation Visualforce controller size, in bytes. Depending on how many HTTP requests
were used in a continuation, this field can contain up to three space-separated values.

EventLogFile Supported Event Types

EventLogFile

##### CORS Violation Record Event Type

CORS Violation Record events capture information about Cross-Origin Resource Sharing (CORS) violations. Cross-origin requests to
Lightning apps are blocked unless the request comes from a URL listed in your CORS allowlist.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
EVENT_TYPE

HOST

ORGANIZATION_ID

ORIGIN

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `CorsViolation` .

**Type**
String

**Description**
The URL of the requested Salesforce resource.

If JavaScript code at `https://www.example.com`
requests a resource from
`https://www.salesforce.com`, the origin is
`https://www.example.com` and the host is
`https://www.salesforce.com` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The URL of the site making the cross-origin request to
Salesforce.

If JavaScript code at `https://www.example.com`
requests a resource from
`https://www.salesforce.com`, the origin is
`https://www.example.com` and the host is
`https://www.salesforce.com` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP

TIMESTAMP_DERIVED

##### CSP Violation Event Type

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content security
policy (CSP). The CSP Violation event type is available in the EventLogFile object in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The CSP violation event is available in the API but not in the
Event Monitoring Analytics app.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: To help preserve performance, Salesforce uses throttling, a technique that limits the number of generated CSP violation
events when the volume is exceptionally high. Therefore, if your org generates a high volume of CSP violations over a short period
of time, some of those violations can fail to generate a CSP violation event.

Fields

**Field** **Details**

```
BLOCKED_URI

BLOCKED_URI_DOMAIN

```

**Type**
String

**Description**
The full string of the blocked resource. If the call to the blocked resource used a URL,
`BLOCKED_URI` is the full URL. Or, for violations with a `DIRECTIVE` of `script-src`
directives, `inline` or `eval` .

**Examples**

**•** https://www.example.com/images/picture.png

**•** file://host1:0002/media/video.mp4

**•** inline

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow resources to be loaded from
the `BLOCKED_URI`, `BLOCKED_URI_DOMAIN` is the `endpointUrl` value to add or
update in the CspTrustedSite Metadata API.

**Example**
www.example.com

```
COLUMN_NUMBER

CONTEXT

DIRECTIVE

DISPOSITION

```

**Type**
Number

**Description**
The column number in the document or worker script at which the violation occurred. This
value is relevant only when `DIRECTIVE` is `script-src` .

For those violations, use this value with `LINE_NUMBER` to identify the location of the
violation.

**Example**

**Type**
String

**Description**
The content security policy (CSP) context for the request. The CSP context controls which
pages can load content from a CspTrustedSite.

CSP violation events capture details about blocked resource requests from only Lightning
Experience pages, this value is always `Lightning` .

**Type**
String

**Description**
The CSP directive that blocked the resource request.

**Possible Values**

**•** `font-src`

**•** `frame-src`

**•** `img-src`

**•** `media-src`

**•** `style-src`

**•** `script-src`

[For information on these directives and a full list of all CSP directives, see MDN Web Docs:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
[Content-Security-Policy.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The CSP violation handling instruction for the user agent at the time of the violation.

**Possible Values**

**•** `enforce` —Enforce the policy violation. For violations with this `DISPOSITION`, the
resource request was blocked.

**•** `report` —Report the policy violation. For violations with this `DISPOSITION`, the
resource request wasn’t blocked, but the violation was reported.

```
EVENT_TYPE

LINE_NUMBER

REQUEST_ID

RESOURCE_SAMPLE

```

**Type**
String

**Description**
The type of event. The value is always `CspViolation`

**Type**
Number

**Description**
The line number in the document or worker script at which the violation occurred. This value
is relevant only when `DIRECTIVE` is `script-src` . For those violations, use this value
with `COLUMN_NUMBER` to identify the location of the violation.

**Example**

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  0000000062_0000x8Lz
```

**Type**
String

**Description**
A sample of the resource that caused the violation, usually the first 40 characters, or the
empty string.

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
                    LoginHint.saveHintEdit();

                    function handleLogin(){document.login.un…

```

```
SOURCE

SOURCE_FILE

TIMESTAMP

TIMESTAMP_DERIVED

```

Usage

**Type**
String

**Description**
The page where this CSP violation originated. For example, if your CSP policy prevented an
image from loading on a Visualforce page, `SOURCE` contains the URL of that page.

**Example**

```
  https:// MyDomainName .my.salesforce.com/apex/HelloWorld

```

**Type**
String

**Description**
The URL of the script in which the violation occurred. If the violation didn’t occur in a script,
`SOURCE_FILE` is null.

**Example**
https://www.example.com/script_xyz.js

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.

**Example**

```
  2022-07-27T11:32:59.555Z.

```

Only one CSP violation event log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file.

If the event log file doesn’t exist, either the log generation process hasn’t run yet or there’s no violation data to report for that 24-hour
window. The event log file is generated only when at least one violation occurred for the day.


Standard Objects EventLogFile Supported Event Types

To collect CSP violation logs for multiple days, schedule a daily query of the CSP Violation event type via REST API. For example, you can
configure a cron job in Unix or a scheduled task in Windows to run the query.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Dashboard Event Type

Dashboard events contain details about report requests from dashboards. These requests are triggered by dashboard refreshes,
subscriptions, and filter changes.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DASHBOARD_COMPONENT_ID

DASHBOARD_ID

DASHBOARD_ID_DERIVED

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Id

**Description**
The 15-character ID of the dashboard component.

**Type**
String

**Description**
The 15-character ID of the dashboard that was run.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the dashboard that was
run.

```
DASHBOARD_TYPE

EVENT_TYPE

IS_SCHEDULED

IS_SUCCESS

LOGIN_KEY

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of dashboard.

**Possible Values**

**•** `R` : Run as running user

**•** `C` : Run as context user

**•** `S` : Run as specific user

**Type**
String

**Description**
The type of event. The value is always `Dashboard` .

**Type**
Boolean

**Description**
1 if the dashboard component ran successfully, 0 if it didn’t.

**Type**
Boolean

**Description**
1 if the dashboard component ran successfully, 0 if it didn’t.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
REPORT_ID

REPORT_ID_DERIVED

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the report that was run.

**Type**
Id

**Description**
The 18-character case insensitive ID of the report that was run.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

VIEWING_USER_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Database Save Event Type

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user the dashboard is running as.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user the dashboard
is running as.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The ID of the user who’s viewing the dashboard.

Database Save events track when records are created, updated, or deleted. This object is available in API version 63.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
DML_TYPE

EVENT_TYPE

FIRST_ENTITY_ID

KEY_PREFIX

LOGIN_KEY

NUM_ROWS

ORGANIZATION_ID

REQUEST_ID

```

**Type**
String

**Description**
The type of DML statement.

**Type**
Id

**Description**
The type of event.

**Type**
String

**Description**
The first ID that is logged when an update occurs. If a single record is updated, the ID of that
row is logged. If multiple records are updated, only one ID is logged.

**Type**
String

**Description**
The key prefix of the entity type that was saved.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session.

**Type**
String

**Description**
The number of entities that were saved.

**Type**
Id

**Description**
The 15-character ID of the organization.

**Type**
String

**Description**
Globally unique id for a given request.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SAMPLE_FACTOR

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
Number

**Description**
The ratio of saved entities that were logged. A value of 1 means every entity saved was logged.
A value of 100 means that 1 out of 100 entities saved was logged.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**

```
  d7DEq/ANa7nNZZVD

```

**Type**
String

**Description**
The Timestamp at which the log event was generated.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
Id

**Description**
The ID of the user who’s using Salesforce services through the UI or the API.

**Example**

```
  005XXXXXXXXXXXX

```

##### Document Attachment Downloads Event Type

Document Attachment Downloads events contain details of document and attachment downloads.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
ENTITY_ID

EVENT_TYPE

FILE_TYPE

ORGANIZATION_ID

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the entity that’s associated with the
document or attachment.

**Type**
String

**Description**
The type of event. The value is always
`DocumentAttachmentDownoads` .

**Type**
String

**Description**
The type of the file or attachment.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### External Cross-Org Callout Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

External Cross-Org Callout events represent external data callouts via the cross-org adapter for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: For the cross-org adapter for Salesforce Connect, event monitoring currently doesn’t track search callouts.

Fields

**Field** **Details**

```
ACTION

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** upsert

**•** delete

```
ENTITY

EVENT_TYPE

EXECUTE_MS

FETCH_MS

FILTER

HAVING

```

**Type**
String

**Description**
Name of the external object being accessed.

**Example**
Order

**Type**
String

**Description**
Type of event. Value is always `ExternalCrossOrgCallout` .

**Type**
Number

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries.

**Example**
WHERE CustomerId='123456'

**Type**
Text

**Description**
Reserved for future use.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
LIMIT

MESSAGE

OFFSET

ORDERBY

ORGANIZATION_ID

```

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed query callout. Value is always empty for
upsert and delete callouts.

**Example**
System.UnexpectedException: Query is either selecting too many fields or the filter conditions
are too complicated

**Type**
Number

**Description**
Number of rows to skip when paging through a result set.

Corresponds to `OFFSET` in SOQL queries. If a SOQL query doesn’t define an `OFFSET`, the
value is -1.

**Example**
0 (default)

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Examples**

**•** ORDER BY ShipName

**•** ORDER BY ShipName DESC

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

ROWS

ROWS_FETCHED

SELECT

STATUS

SUBQUERIES

```

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
Total number of records in the result set. Value is always 0 for upsert and delete callouts.

**Example**

**Type**
Number

**Description**
Reserved for future use.

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Example**
SELECT Id,Name,CustomerID,OrderDate

**Type**
Boolean

**Description**
Whether the query was successful. Value is always empty for upsert and delete callouts.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**Type**
Number

**Description**
The number of subqueries that the query is split into.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_MS

USER_ID

USING_MRU

```

**Type**
Number

**Description**
Reserved for future use.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Example**

**Type**
Id

**Description**
15-character ID of the user accessing the external system.

**Example**
00530000009M943

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Reserved for future use.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### External Custom Apex Callout Event Type

External Custom Apex Callout events represent external data callouts via custom adapters for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

ENTITY

EVENT_TYPE

EXECUTE_MS

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query

**•** upsert

**•** delete

**Type**
String

**Description**
Name of the external object being accessed.

**Example**
Order

**Type**
String

**Description**
Type of event. Value is always `ExternalCustomApexCallout` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

```
FETCH_MS

FILTER

LIMIT

MESSAGE

OFFSET

```

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries.

**Example**
Filter:[columnName=CustomerID, columnValue=537, subfilters=null, tableName=Order,
type=EQUALS]

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed call.

**Example**
System.UnexpectedException: Query is either selecting too many fields or the filter conditions
are too complicated

**Type**
Number

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in SOQL
queries.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
0 (default)

```
ORDERBY

ORGANIZATION_ID

REQUEST_ID

ROWS

ROWS_FETCHED

```

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Examples**
(Order:[columnName=OrderDate, direction=ASCENDING, tableName=Order])

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
Total number of records in the result set.

The value is always -1 if the custom adapter’s `DataSource.Provider` class doesn’t
declare the `QUERY_TOTAL_SIZE` capability.

**Example**

**Type**
Number

**Description**
Number of rows fetched by the callout. Available in API version 42.0 and later.

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SELECT

STATUS

THROUGHPUT

TIMESTAMP

SUBQUERIES

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Example**
(ColumnSelection:[aggregation=NONE, columnName=Name, tableName=Order],
ColumnSelection:[aggregation=NONE, columnName=CustomerID, tableName=Order],
ColumnSelection:[aggregation=NONE, columnName=OrderDate, tableName=Order])

**Type**
Boolean

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**•** Empty—Failed with no logged status or message

**Type**
Number

**Description**
Number of records retrieved in one second.

**Example**
302.57

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
Number

**Description**
Reserved for future use.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
TOTAL_MS

USER_ID

```

SEE ALSO:

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Example**

**Type**
Id

**Description**
15-character ID of the user accessing the external system.

**Example**
00530000009M943

EventLogFile Supported Event Types

EventLogFile

##### External Data Source Callout Event Type

External Data Source Callout events represent external data callouts via the Salesforce Connect adapters for Amazon DynamoDB and
Amazon Athena. This event type is available in the EventLogFile object in API version 56.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**
For Amazon DynamoDB data source:

**•** query

**•** insert

**•** delete

**•** update


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** upsert

For Amazon Athena data source:

**•** query

```
DATA_SOURCE_NAME

EVENT_TYPE

EXTERNAL_OBJECT

FETCH_MS

FILTER

LIMIT

MESSAGE

```

**Type**
String

**Description**
Name of the external data source being accessed.

**Type**
String

**Description**
Type of event. Value is always `ExternalDataSourceCallout` .

**Type**
String

**Description**
Name of the external object being accessed.

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external data source.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in queries.

**Type**
Number

**Description**
[Maximum number of rows to return for a query. Corresponds to Limit parameter in](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)
[ExecuteStatement operation for an Amazon DynamoDB data source.](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)

**Type**
String

**Description**
Error or warning message associated with the failed call.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
NEXT_LINK

OFFSET

OPERATION

ORDERBY

ORGANIZATION_ID

PARENT_CALLOUT

```

**Type**
String

**Description**
Next link that the callout used to request a subsequent page of rows. A next link is provided
in a previous response when the response includes only part of the result set.

For requests to AWS data sources, this field stores the `nextToken` parameter that contains
a unique hash string.

**Type**
Number

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in
queries to Amazon Athena. This field is not supported by queries to Amazon DynamoDB.

**Type**
String

**Description**
The operation that’s being performed.

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in queries.

**Example**

**•** Country ASC

**•** CustomerName DESC

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
If the callout requested a subsequent page of rows, this field identifies the initial callout
whose request resulted in the multi-page result set.

**Example**
4EoZtuBzzRIXSk-ysRdf1F-1


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PROVIDER_TYPE

REQUEST_ID

RESPONSE_SIZE

ROWS_FETCHED

SEARCH

SELECT

```

**Type**
String

**Description**
Whether the callout was made by Salesforce Connect adapter for Amazon DynamoDB or
Amazon Athena.

**Possible Values**

**•** `amazonDynamodb`

**•** `amazonAthena`

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
Number of records fetched by the callout. The records fetched by a callout can be a subset
of a large result set.

**Example**

**Type**
String

**Description**
Search query string.

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in queries.

To query, Salesforce Connect adapter uses PartiQL with Amazon DynamoDB and SQL with
Amazon Athena.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
CustomerID,OrderDate,OrderID,ShipCity,ShipCountry

```
STATUS

STATUS_CODE

TABLE_NAME

THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Boolean

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**Type**
Number

**Description**
The HTTP response status code for the request.

**Type**
String

**Description**
Name of the table being queried in the AWS data source.

**Type**
Number

**Description**
Number of records retrieved in one second.

**Example**
3025.67

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TOTAL_MS

USER_ID

```

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Type**
Id

**Description**
15-character ID of the user accessing the external data source.

**Example**
00530000009M943

##### External OData Callout Event Type

External OData Callout events represent external data callouts via the OData 2.0 and OData 4.0 adapters for Salesforce Connect. This
event type is available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

BYTES

ENTITY

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query

**•** upsert

**•** delete

**Type**
Number

**Description**
Size of the result set in bytes.

**Type**
String

**Description**
Name of the external object being accessed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
Order

```
EVENT_TYPE

EXECUTE_MS

EXPAND

FETCH_MS

FILTER

LIBRARY

```

**Type**
String

**Description**
Type of event. Value is always `ExternalODataCallout` .

**Type**
Number

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

**Type**
String

**Description**
Reserved for future use.

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries and
`$filter` in OData queries.

**Example**
CustomerID eq 12345

**Type**
String

**Description**
Reserved for future use.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
LIMIT

MESSAGE

NEXT_LINK

OFFSET

ORDERBY

```

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries
and `$top` in OData queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed call.

**Example**
The OData query result was too large, so the external data didn’t load.

**Type**
String

**Description**
OData next link that the callout used to request a subsequent page of rows. A next link is
provided in a previous response from the OData producer when the response includes only
part of the result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
http://services.example.org/Warehouse.svc/Orders?$count=true&
$select=CustomerID,OrderID,RequiredDate,ShippedDate&$top=301&$skiptoken=10447

**Type**
Number

**Description**
Number of rows to skip when paging through a result set.

Corresponds to `OFFSET` in SOQL queries and `$skip` in OData queries.

**Example**

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries and `$orderby`
in OData queries.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Examples**

**•** ShipName

**•** ShipName desc

```
ORGANIZATION_ID

PARENT_CALLOUT

PROVIDER_TYPE

RATE_LIMIT_USAGE_PERCENT

REQUEST_ID

```

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
If the callout requested a subsequent page of rows, this field identifies the initial callout
whose request resulted in the multi-page result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
4EoZtuBzzRIXSk-ysRdf1F-1

**Type**
String

**Description**
Whether the OData 2.0 or OData 4.0 adapter made the callout.

**Possible Values**

**•** OData—OData 2.0 adapter

**•** OData4—OData 4.0 adapter

**Type**
Number

**Description**
Consumed percentage of the org’s limit of OData callouts per hour.

**Example**
2.5—2.5% of the hourly callout limit has been consumed

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
4A13-HSKv3CKs-0FKfceaV

```
REQUESTS

ROWS

ROWS_FETCHED

SEARCH

SELECT

STATUS

```

**Type**
Number

**Description**
Reserved for future use.

**Type**
Number

**Description**
Total number of records in the result set. Available in API version 42.0 and later.

**Example**

**Type**
Number

**Description**
Number of records fetched by the callout. The records fetched by a callout can be a subset
of a large result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**

**Type**
String

**Description**
Search query string. Corresponds to condition expressions in SOSL.

**Example**
contains(CustomerID,'10248') eq true or contains(ShipName,'10248') eq true

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries
and `$select` in OData queries.

**Example**
CustomerID,OrderDate,OrderID,ShipCity,ShipCountry

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

```
THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_MS

USER_ID

```

**Type**
Number

**Description**
Number of records retrieved in one second.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
3025.67

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Type**
Id

**Description**
15-character ID of the user accessing the external system.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
00530000009M943

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Flow Execution Event Type

Flow Execution events contain information about flows that were executed including details such as total execution time, number of
interviews, and number of errors.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

EVENT_TYPE

TIMESTAMP

REQUEST_ID

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
The type of event. The value is always `FlowExecution` .

**Type**
String

**Description**
The time that the flow was executed in GMT.

For example: `20210606032436.520` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `TID:000000000000c00fff` .

```
ORGANIZATION_ID

USER_ID

PLANNER_IDENTIFIER

PROCESS_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the user who executed the flow through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable event
orchestration process in the background and automatically executes different types of
actions based on the event type. This value is available in API version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s executed when a user
completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This value is
available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein Activity
Capture detects and captures a new activity, such as an email. This type of flow runs in
the background without user interaction. This value is available with Sync Email as
Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API version
44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for an approval process. This
value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout in a
store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request to be contacted by
customer support. This flow is used to create contact request records. This value is
available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate survey
questions with different stages in customer lifecycles. This value is available in API version
49.0 and later and only when the Customer Lifecycle Designer license is enabled.

**•** `CustomEvent` —A process that is invoked when it receives a platform event message.
In the UI, it’s an event process. This value is available in API version 41.0 and later.

**•** `DataCaptureFlow`                   - In the UI, Data Capture flows configure the Form tab in the
Field Service mobile app. When the Data Capture flow is launched, its Flow metadata is
publicly available in JavaScript format. This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents assessment
questions from Discovery Framework. Launches when invoked by a user on a mobile
device. This type of flow collects or displays information, requires user interaction, and
works offline or online. This value is available in API version 62.0 and later.

**•** `EvaluationFlow` —A flow for evaluating custom entry and exit conditions in an
orchestration. Uses the `isOrchestrationConditionMet` output variable and
discards values from any other output variables. This value is available in API version 54.0
and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value is
available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI label is
Field Service Embedded Flow. This value is available in API version 41.0 and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more screens
or local actions, choices, or dynamic choices. In the UI and Salesforce Help, it’s a screen
flow. Screen flows can be launched from the UI, such as with a flow action, Lightning
page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is available
in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration and
updates for single sign-on with the authentication provider framework. Available in API
version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates and
creates indicator results for a selected indicator performance period. This value is available
with the Outcome Management license in API version 60.0 and later.

**•** `IndividualObjectLinkingFlow` —A flow that associates individuals with
interactions such as voice calls, messaging sessions, or case-related emails. This value is
available in API version 58.0 and later.

**•** `InvocableProcess` —A process that another process or the Invocable Actions
resource in REST API invokes. This value is available in API version 38.0 and later.

**•** `Journey` —An audience-driven flow for Marketing Cloud. This value is available in API
version 57.0 and later.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `LoginFlow` —A flow for login. This value is available in API version 51.0 and later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app that’s
invokable by loyalty program processes. This value is available in API version 54.0 and
later.

**•** `Orchestrator` —An orchestration that organizes flows into groups of steps contained
in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder and the
flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy` —Build recommendations for your users. A
recommendation launches its assigned flow. This value is available in API version 54.0
[and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=platform.nba_building_flow_builder_strategy.htm&type=5&language=en_US)

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business logic.
This value is available in API version 52.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created in
Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper. From
the UI, this type of flow is created in the Survey Builder and requires an associated survey
flow type. This value is available in API version 49.0 or later and only when the Customer
Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In the UI
and Salesforce Help, it’s a record change process.

These values are reserved for future use.

**•** `ActionPlan`

**•** `AppProcess`

**•** `ApprovalWorkflow`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `JourneyBuilderIntegration`

**•** `LoginFlow`

**•** `ManagedContentFlow`

**•** `OrchestrationFlow`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

```
FLOW_VERSION_ID

```

**Type**
Id

**Description**
The ID of the flow version that was executed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
FLOW_LOAD_TIME

TOTAL_EXECUTION_TIME

NUMBER_OF_INTERVIEWS

NUMBER_OF_ERRORS

TIMESTAMP_DERIVED

```

**Type**
Number

**Description**
The time in milliseconds to load the flow’s metadata.

**Type**
Number

**Description**
The total time in milliseconds to start and finish all flow interviews.

**Type**
Number

**Description**
The number of flow interviews that started after the flow version was executed.

**Type**
Number

**Description**
The number of errors for all flow interviews after the flow version was executed.

**Type**
DateTime

**Description**
The time that the flow was executed in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

##### GraphQL Query Event Type

GraphQL Query events contain information about executed queries, including total execution time, the number of invocations, and any
reported errors.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_TYPE

```

**Type**
String

**Description**
The name of the application that the user accessed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CLIENT_IP

CPU_TIME

ELAPSED_TIME_MS

EVENT_TYPE

EXCEPTION

LOGIN_KEY

OPERATION_NAME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
Number

**Description**
The time, in milliseconds, that it took for the GraphQL query to complete.

**Type**
String

**Description**
The type of event.

**Type**
String

**Description**
Exception message if the request encountered an error. Empty indicates successful execution.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The name of the GraphQL query. If the query was anonymous (i.e., no name was provided
in the query string), this field will usually be empty or null in the logs.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
ORGANIZATION_ID

QUERY

QUERY_LENGTH

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The GraphQL JSON query.

**Type**
Number

**Description**
The length of the GraphQL JSON query in characters.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `TID:000000000000c00fff` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The time that the flow was executed in GMT.

For example: `20210606032436.520` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
CHECK

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` )

For example: `2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: /home/home.jsp.

**Type**
String

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who executed the flow through the UI or the API.

For example: `00530000009M943` .

**Type**
String

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.


Standard Objects EventLogFile Supported Event Types

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

```
VARIABLES

```

**Type**
String

**Description**
A JSON string containing the name-value pairs of the variables used in the GraphQL operation.

##### Group Membership Event Type

Group Membership events capture details about changes to public group and queue membership, such as when members are added
to or removed from the public group or queue.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services.

**Example**

```
  96.43.144.26

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity that took place in the app server layer.

```
EVENT_TYPE

GROUP_ID

GROUP_TYPE

LOGIN_KEY

MEMBER_ID

```

**Type**
String

**Description**
The type of event. The value is always `GroupMembership` .

**Type**
Id

**Description**
ID of the group whose membership changed.

**Example**

```
  00GXXXXXXXXXXXX

```

**Type**
String

**Description**
The type of group. Valid values are:

**•** `R` —Public group

**•** `Q` —Queue

**Example**

```
  R

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
Id

**Description**
The ID of the member added to or removed from the group. Public groups can contain
individual users, other groups, or users in a specified role or territory. Queues can contain
individual users, roles, public groups, territories, connections, or partner users.

**Example**
`005XXXXXXXXXXXX` or `00GXXXXXXXXXXXX`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
OPERATION

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The operation that occurred, such as a member being added to or removed from a group.
Valid values are:

**•** `AddedGroupMember`

**•** `DeletedGroupMember`

**Example**

```
  DeletedGroupMember

```

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Example**

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**

```
  d7DEq/ANa7nNZZVD

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The access time of Salesforce services in GMT.

**Example**

```
                   20130715233322.670

```

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
The URI of the page that’s receiving the request.

**Example**

```
  /home/home.jsp

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Example**

```
  005XXXXXXXXXYAY

```

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Example**

```
  005XXXXXXXXXXXX

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   005XXXXXXXXXXXXIA0

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Hostname Redirects Event Type

Hostname Redirect events contain details about blocked and successful redirections for your previous My Domain hostnames. The
Hostname Redirects event type is available in the EventLogFile object in API version 56.0 and later.

Note: The HostnameRedirects event type is disabled by default. To enable this event type, use the `logRedirections` field
on the MyDomainSettings Metadata API type or enable the **Log Redirections** setting in the Routing section of the My Domain
Setup page.

This event is free for all customers with a 24-hour data retention period. The hostname redirections event is available in the API but not
in the Event Monitoring Analytics app. You can also download the latest hostname redirections event log file through a button on the
My Domain page.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

TIMESTAMP

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `HostnameRedirects` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   0000000062_0000x8Lz
```

```
ORGANIZATION_ID

USER_ID

RUN_TIME

CPU_TIME

URI

SESSION_KEY

LOGIN_KEY

MESSAGE

```

**Type**
ID

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000345

```

**Type**
ID

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
Number

**Description**
This field is unused in the HostnameRedirects event type. The value is always `0` .

**Type**
Number

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

```
DOMAIN

SOURCE_HOSTNAME

TARGET_HOSTNAME

PATH

REDIRECT_REASON

```

**Type**
Url

**Properties**
Filter, Sort

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
The hostname of the URL from which the redirection originated.

**Example**
If `https://` _**`oldMyDomainName`**_ `.my.salesforce.com` is redirected to
`https://` _**`newMyDomainName`**_ `.my.salesforce.com`, the value of this field is

```
  oldMyDomainName .my.salesforce.com

```

**Type**
String

**Description**
The hostname of the URL to which the user or API was redirected.

**Example**
If `https://` _**`oldMyDomainName`**_ `.my.salesforce.com` is redirected to
`https://` _**`newMyDomainName`**_ `.my.salesforce.com`, the value of this field is

```
  newMyDomainName .my.salesforce.com

```

**Type**
String

**Description**
The path of the originating URL request, up to the first question mark (?). The path is also
used in the redirection target URL. However, this field doesn’t include the query string, if
present.

**Example**
If the user is redirected from
`https://MyOldCompany.my.site.com/shop?q=sneakers` to
`https://MyNewCompany.my.site.com/shop?q=sneakers`, the value of
this field is `/shop` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The reason for the hostname redirect event.

**Possible Values**

**•** `Redirected due to a hostname mismatch.` —The referring hostname
was redirected to the current My Domain equivalent.

**•** `Redirection suppressed to prevent Lightning Out`
`integration failure.` —The `*.force.com` site URL can’t be redirected for
[use with Lightning Out. To prevent issues, the original URL was processed as-is. To avoid](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out)
issues after `*.force.com` site hostname redirections are stopped, update hard-coded
references to the hostname in your Lightning Out integrations. For a Lightning Out code
[example that uses a site hostname, see Share Lightning Out Apps with Unauthenticated](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out_public_apps)
[Users in the Salesforce Lightning Component Library.](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out_public_apps)

**•** `Redirection was blocked because redirections for this`
`hostname are disabled.—` Only your last set of My Domain login hostnames
is redirected. Those redirections are blocked when the My Domain Routing option
**Redirect previous My Domain URLs to your current My Domain** is deselected or
because you removed your previous My Domain. That option applies to legacy
(non-enhanced) hostnames in production orgs until Spring ’25. In non-production orgs,
that option has no impact on redirections for legacy hostnames in Winter ’25 and later.
Non-production orgs include sandboxes, Developer Edition orgs, demo orgs, patch orgs,
scratch orgs, and Trailhead Playgrounds. For information

If the `SOURCE_HOSTNAME` is a legacy `*.force.com` site hostname, the redirection
was blocked because the **Redirect** _`previousSiteHostnames`_ **URLs to your**
**current My Domain site URLs** Routing option was deselected on the My Domain Setup
page. That option is available in production orgs until Spring ’25. In non-production orgs,
that option was removed in Winter ’25. Non-production orgs include sandboxes,
Developer Edition orgs, demo orgs, patch orgs, scratch orgs, and Trailhead Playgrounds.

**•** `Redirection was blocked because redirections for the`
`legacy SOURCE_HOSTNAME are no longer supported.` —If your org
was created before June 2022, Salesforce served the org on a different set of hostnames
until enhanced domains were deployed. The `SOURCE_HOSTNAME` is one of those
hostnames. For non-production orgs, redirections for those hostnames stopped in Winter
’25.

```
IS_BLOCKED_REDIRECTION

```

**Type**
Boolean

**Description**
Indicates whether the redirection was blocked.

**Possible Values**

**•** `1` —The redirection was blocked and returned an HTTP 404 response.

**•** `0` —The redirection proceeded and returned an HTTP 301 or 307 response.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REFERRER

ORIGIN

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The absolute or partial address from which the request to the `SOURCE_HOSTNAME` came.
The `Referrer-Policy` HTTP Header of the request determines how much of the URL
is shared.

For example, if a user clicked a link to the `SOURCE_HOSTNAME` from a web page, and
that web page is on a different domain:

**•** if the `Referrer-Policy` HTTP Header is `no-referrer-when-downgrade`,
`REFERRER` includes the origin, path, and query-string parameters up to the first hash
( `#` ), if present.

**•** if the `Referrer-Policy` HTTP Header is
`strict-origin-when-cross-origin`, `REFERRER` includes the origin only.

**•** if the `Referrer-Policy` HTTP Header is `same-origin`, `REFERRER` is null.

**Examples**

**•** https://www.example.com

**•** https://www.example.com/page/page/index.htm

**•** https://www.example.com/page/index.htm?q="Salesforce"

**Type**
String

**Description**
The origin (protocol, hostname, and port) that caused the request to the
`SOURCE_HOSTNAME` . For example, if a website on a different domain makes an
XMLHttpRequest (XHR) to `SOURCE_HOSTNAME`, `ORIGIN` contains the base URL of that
website.

The port isn’t included in the origin information with all requests. `ORIGIN` can be null in
a number of situations, including but not limited to cross-origin requests and origins with a
restrictive `Referrer-Policy` header. For example, if the request to the
`SOURCE_HOSTNAME` is sent from a site external to Salesforce with a `RequestMode`
of `no-cors`, `ORIGIN` is null.

**Examples**

**•** https://www.example.com

**•** https://www.example.com:443

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   2022-07-27T11:32:59.555Z.

```

```
USER_ID_DERIVED

CLIENT_IP

URI_ID_DERIVED

```

Usage

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
The IP address of the client that made this request.

**Possible Values/Example**

```
  111.43.144.26

```

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

Use the information in the Hostname Redirects event log to determine the hostnames to update in your org after you deploy a change
to your My Domain name. You can also use the log to develop communications to your customers and users about the changed
hostnames. For example, you can encourage users to use the new hostnames and update their bookmarks. For more information on
[the steps to take after a My Domain change, see Update Your Org and Test My Domain Changes in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_deploy_update_test.htm&type=5&language=en_US)

To access the log, use the HostnameRedirects event type from the EventLogFile object. Alternatively, you can download the current
hostname redirections event log by clicking **Download Redirections Log** on the My Domain Setup page.

Each event, or each row in the redirection log, represents a redirection for a specific requested URL. Subsequent requests to the same
URL within the hour following that request, however, aren’t logged. If your last My Domain change included enhanced domains
[deployment, the log includes redirections for the old hostnames listed on My Domain URL Format Changes with Enhanced Domains](https://help.salesforce.com/s/articleView?id=products.domain_name_url_format_changes_enable_enhanced.htm&type=5&language=en_US)
[Deployment in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_format_changes_enable_enhanced.htm&type=5&language=en_US)

Note: To keep the size of the log file manageable, the log includes one entry for each redirected hostname and path combination
within an hour. As a result, the log includes all redirected hostname and path combinations, but only includes the first redirection
within each hour.

For example, if `https://MyCompany.my.site.com/shop` is redirected at 02:01 PM and
`https://MyCompany.my.site.com/shop?q=sneakers` is redirected for another user at 02:02 PM, only the
redirection that occurred at 02:01 PM is captured for `MyCompany.my.site.com/shop` for that hour. But if
`https://MyCompany.my.site.com/help` is redirected at 2:05 PM, that redirection is captured on a new line because
the `MyCompany.my.site.com/help` hostname and path combination differs from `MyCompany.my.site.com/shop` .


Standard Objects EventLogFile Supported Event Types

Similarly, if the redirection of `https://MyCompany.my.site.com/contactUs` is blocked at 07:02 AM and
`https://MyCompany.my.site.com/contactUs` is redirected at 07:11 AM, only the blocked redirection for
`MyCompany.my.site.com/contactUs` is captured in the log for that hour.

Only one hostname redirection log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file. When you download the redirections log from the My Domain Setup page,
you get the latest daily log file in CSV format.

If the log file doesn’t exist, either the log generation process hasn’t run yet or there’s no redirection data to report for that 24-hour
window. The log file is generated only when at least one redirection occurred for the day.

To collect hostname redirection logs for multiple days, schedule a daily query of the Hostname Redirects event type via REST API. For
example, you can configure a cron job in Unix or a scheduled task in Windows to run the query.

Salesforce CLI Example

To use Salesforce CLI to query the Hostname redirects log, use the `sf data query` command to query the HostnameRedirects
EventType.

[First, download and install Salesforce CLI.](https://developer.salesforce.com/tools/salesforcecli)

**Example**
This Unix example authorizes Salesforce CLI to access your org and sets `orgAlias` to your org login URL. This method prompts
you to log in to your org via a browser to grant Salesforce CLI access. To query event log files, log in as a user with the View Event
Log Files and API Enabled permissions.

```
     sf org web login --alias orgAlias --instance-url https:// MyDomainName .my.salesforce.com

```

**Example response**

After you authenticate with a user via a browser, this response confirms that Salesforce CLI is authorized for use in your org.

```
     Successfully authorized admin@mycompany.com with org ID 00D00000000000aIW

```

Then export the HostnameRedirects log to a CSV file.

**Example**
This example exports the HostnameRedirects EventType to a CSV file in your org, where `orgAlias` is your org's alias within
Salesforce CLI.

```
     ORGALIAS= orgAlias ; QUERYRESULT=$(sf data query --target-org "$ORGALIAS" --query "SELECT

      LogDate, LogFile FROM EventLogFile WHERE EventType='HostnameRedirects' ORDER BY

     CreatedDate DESC LIMIT 1" --json); QUERYSTATUS=$(echo "$QUERYRESULT"|grep \"status\"|cut

      -d : -f 2|cut -d, -f 1); if [[ "$QUERYSTATUS" -eq 0 ]]; then LOGDATE=$(echo

     "$QUERYRESULT"|grep LogDate|cut -d \" -f 4|cut -d T -f 1); if [[ "$LOGDATE" == "" ]];

     then echo "No daily event log file exists for hostname redirects."; else

     DOWNLOADPATH=$(echo "$QUERYRESULT"|grep \"url\"|cut -d \" -f 4); ORGDISPLAY=$(sf org

     display --target-org "$ORGALIAS" --json 2> /dev/null); SESSION=$(echo "$ORGDISPLAY"|grep

     accessToken|cut -d \" -f 4); ORGURL=$(echo "$ORGDISPLAY"|grep instanceUrl|cut -d \" -f

     4); curl -H "Authorization: Bearer ${SESSION}" --silent ${ORGURL}${DOWNLOADPATH}/LogFile

      > HostnameRedirectEvent-${LOGDATE}.csv; fi; else echo "$QUERYRESULT"; fi

```

**Example CSV formatted response**

```
     "EVENT_TYPE","TIMESTAMP","REQUEST_ID","ORGANIZATION_ID","USER_ID","RUN_TIME",

     "CPU_TIME","URI","SESSION_KEY","LOGIN_KEY","MESSAGE","DOMAIN","SOURCE_HOSTNAME",

     "TARGET_HOSTNAME","PATH","REDIRECT_REASON","IS_BLOCKED_REDIRECTION","REFERRER",

```


Standard Objects EventLogFile Supported Event Types

```
     "ORIGIN","TIMESTAMP_DERIVED","USER_ID_DERIVED","CLIENT_IP","URI_ID_DERIVED"

     "HostnameRedirects","20220803011210","4kTkZZ1PzwSSHDkCagbl7-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","","ExperienceCloudSubdomain.force.com",

     "","","","0","https://partner.example.com/pagename.html","",

     "2022-08-03T01:12:10.015Z","","198.51.100.0"," "

     "HostnameRedirects","20220803022225","4kTkSZ1PzwSTHDkCagbl9-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","",

     "SalesforceSitesSubdomain.secure.force.com","","","","0","",

     "https://partner2.example.com","2022-08-03T02:22:25.015Z","","2001:DB8::",""

     "HostnameRedirects","20220803025230","4kNP4KyC_ddbI0GxqZ8Lz-","00D000000000aIW",

     "","0","","","","","Redirection prevented due to a hostname mismatch.","",

     "oldMyDomainName.my.salesforce.com","currentMyDomainName.my.salesforce.com","",

     "","0","https://www.example.com/login_hub.htm","https://www.example.com",

     "2022-08-03T02:52:30.015Z","","203.0.113.0",""

     "HostnameRedirects","20220803081241","4kTkSZ1PzwSTHDkCagbl9-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","",

     "SalesforceSitesSubdomain.secure.force.com","","","","0",

     "https://myDomainName.my.site.com/store/Page1","","2022-08-03T08:12:41.015Z","",

     "Salesforce.com IP",""

     "HostnameRedirects","20220803113801","4kNQs7BYKbSbIWGxqZ8Lz-","00D000000000aIW",

     "","0","","","","","Redirection prevented due to a hostname mismatch.","",

     "oldMyDomainName.lightning.force.com","currentMyDomainName.lightning.force.com",

     "","","0",

     "https://sandboxMyDomainName--SandboxName.sandbox.lightning.force.com/r/

     product__c/a00000000000000IAI/view",

     "https://sandboxMyDomainName--SandboxName.sandbox.lightning.force.com",

     "2022-08-03T11:38:01.015Z","","Salesforce.com IP",""

```

For more information on Salesforce CLI, see the Salesforce CLI Setup Guide, Salesforce CLI Command Reference, and the Salesforce DX
Developer Guide.

REST API Example

[To use REST API to query the Hostname Redirects event log, use the Query resource to retrieve field values from a record. Specify the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_query.htm#topic-title)
fields you want to retrieve in the fields parameter and use the GET method of the resource.

**Example**
This example retrieves the HostnameRedirects event log based on `Field` and `EventType` via a GET request. Replace `token`
with your access token. In a production org, replace `MyDomainName` with your My Domain name. In a sandbox, replace
`MyDomainName.my.salesforce.com` with your org’s My Domain login hostname.

```
     curl https:// MyDomainName .my.salesforce.com/services/data/v66.0/query?q=SELECT+

     LogDate%2C+LogFile+FROM+EventLogFile+WHERE+EventType%3D%27HostnameRedirects%27

     +ORDER+BY+CreatedDate+DESC+LIMIT+1 -H "Authorization: Bearer token"

```

**Example raw response**

```
     {"totalSize":1,"done":true,"records":[{"attributes":

     {"type":"EventLogFile","url":"/services/data/v56.0/sobjects/EventLogFile/

     0AT00000003KxUSWA0"},"LogDate":"2022-08-03T00:00:00.000+0000","LogFile":"

     /services/data/v56.0/sobjects/EventLogFile/0AT00000003KxUSWA0/LogFile"}]}

```


Standard Objects EventLogFile Supported Event Types

The log file can be downloaded by using curl with the same Authorization header while setting the URL path to the `LogFile` value
from the output.

[For more information on accessing event log files via REST API, see Using Event Monitoring in the REST API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/using_resources_event_log_files.htm)

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Insecure External Assets Event Type

Insecure External Assets events contain information about external assets. External assets include images or videos accessed by users
over an insecure HTTP protocol. The event lists all your Salesforce pages that contain assets hosted insecurely on third-party sites that
users loaded with a Chrome, Firefox, Microsoft Edge, or Safari browser. The `INSECURE_URI` field contains the URI being used to load
the asset insecurely. The Insecure External Assets event type is available in the EventLogFile object in API version 42.0 and later.

Assets over HTTP can be manipulated through man-in-the-middle and other types of attacks. These attacks can trick users into sending
their Salesforce credentials to malicious sites. Always use HTTPS in your custom code and templates for any asset you’re loading from
external sites.

Important: Because HTTPS connections are required to load external assets, Insecure External Assets events no longer apply. In
Spring ’25 and later, this event type captures no data.

To view blocked redirections and content security policy (CSP) violations for your org, use the BrowserPolicyViolation object.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ASSET_TYPE

```

**Type**
String

**Description**
Type of insecure asset.

**Possible Values**

**•** `Base URI`

**•** `Connect`

**•** `Font`

**•** `Frame Ancestor` : External page that embeds the Salesforce page in an iframe

**•** `Frame`

**•** `Image`

**•** `Media`

**•** `Object`

**•** `Other`

**•** `Plugin Types`

**•** `Script`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `Style`

```
CLIENT_IP

CPU_TIME

DISPOSITION

DOCUMENT_URI

EVENT_TYPE

INSECURE_URI

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Description**
If the insecure external asset is related to your content security policy (CSP), the HTTP header
that identified the insecure asset.

Available in API version 61.0 and later.

**Possible Values**

**•** `enforce` —The `Content-Security-Policy` header identified the insecure
external asset.

**•** `report` —The `Content-Security-Policy-Report-Only` header identified
the insecure external asset.

**Type**
String

**Description**
URL of the page that contains the insecure asset, excluding the query parameter.

**Example**
https://company.my.salesforce.com/00XXXXXXXXX

**Type**
String

**Description**
The type of event. The value is always `InsecureExternalAssets` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Insecure external asset URL being used to load an asset insecurely. For example, loading
Javascript libraries using **`http:`** `//ajax.googleapis.com/` in your custom code
logs an Insecure External Asset Event with the `INSECURE_URI` field set to this URL. Find
this reference in your code and update it to use **`https:`** `//ajax.googleapis.com/`
instead.

**Example**
http://pbs.twimg.com/profile_images/5699091412070816/Z4Stwts_normal.jpeg

```
LOGIN_KEY

NETWORK_ID

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The ID of the Experience Cloud site related to the request, if applicable.

Available in API version 61.0 and later.

**Type**
String

**Description**
The 15-character ID of the org.

**Example**
00D000000000123

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

UNIQUE_ID

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
Type of Salesforce page.

**Possible Values**

**•** `Appserver` —Page without My Domain subdomain (for example,
https://na44.salesforce.com)

**•** `Communities` —Customer Experience Cloud site

**•** `Email` —Email preview

**•** `Login` —Login page (for example, https://login.salesforce.com)

**•** `Mydomain` —Page on My Domain subdomain (for example,
https://mycompany.my.salesforce.com)

**•** `Sites` —Customer site

**•** `Static` —Static content (for example, https://sfdcstatic.com)

**•** `Unknown` —other type of page

**Type**
String

**Description**
The 32-character ID of the event log file in which the insecure external asset event data is
found.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
44e128a5-ac7a-4c9a-be4c-224b6bf81b20

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

Usage

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

`UNIQUE_ID` is used by Salesforce Customer Support to troubleshoot any issues that occur.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Insufficient Access Event Type

Insufficient Access events contain details about errors relating to insufficient account, case, contact, and opportunity record access, so
that you can troubleshoot and resolve access issues for your users.

Note: The Insufficient Access event type is disabled by default. You can enable this event type for a period of 24 hours by contacting
Salesforce Customer Support.


Standard Objects EventLogFile Supported Event Types

These insufficient access error scenarios are logged:

**•** The user can’t share a case, contact, or opportunity because the user doesn’t have permission to share the parent account or the
recipient of the share doesn’t currently have read access to the parent account.

**•** The user can’t change ownership of a case, contact, or opportunity because the user doesn’t have permission to share the parent
account or the new owner doesn’t currently have read access to the parent account.

**•** The user can’t change the parent account of a case, contact, or opportunity because the user doesn’t have permission to share the
new parent account or the owner of the case, contact, or opportunity doesn’t have read access to the new parent account.

Insufficient access errors resulting from bulk operations involving two or more records aren’t logged.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

[For more information on interpreting Insufficient Access events, see this knowledge article.](https://help.salesforce.com/s/articleView?id=000396437&type=1&language=en_US)

Fields

**Field** **Details**

```
ACCESS_ERROR

ACTUAL_LOGGED_IN_USER_ID

ENTITY_TYPE

```

**Type**
String

**Description**
The type of insufficient access error that the user received. Valid values are:

**•** `DATA_NOT_AVAILABLE` —The record is no longer accessible. For example, a record
was deleted and moved to the Recycle Bin.

**•** `INVALID_TYPE` —The record type doesn’t exist.

**•** `NO_ACCESS` —The user doesn’t have the required access level to complete the
attempted action on the record.

**Example**

```
  NO_ACCESS

```

**Type**
Id

**Description**
The 15-character ID of the user who initiated the action that caused the insufficient access
error. For example, a user attempts to transfer ownership of a record to a teammate, but the
operation fails because the teammate doesn’t have the required access. In this scenario, the
`ACTUAL_LOGGED_IN_USER_ID` is the user who attempted to transfer access, and the
`USER_ID` is their teammate.

**Example**

```
  005XXXXXXXXXXXX

```

**Type**
String

**Description**
The object for which the user received the insufficient access error. Access errors for the
account, case, contact, and opportunity objects are supported.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
Account

```
ERROR_DESCRIPTION

ERROR_TIMESTAMP

EVENT_TYPE

ORGANIZATION_ID

RECORD_ID

REQUEST_ID

```

**Type**
String

**Description**
Description of the insufficient access error that the user received.

**Example**
User 005XXXXXXXXXXXX doesn't have full access for the record 001XXXXXXXXXXXX.

**Type**
String

**Description**
The time in GMT that the insufficient access error occurred.

**Example**

```
  20130715233322.670

```

**Type**
String

**Description**
The type of event. The value is always `InsufficientAccess` .

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The ID of the record that the user doesn’t have access to.

**Example**

```
  001XXXXXXXXXXXX

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   3nWgxWbDKWWDIk0FKfF5DV

```

```
REQUESTED_ACCESS_LEVEL

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
String

**Description**
The access level required by the user’s attempted action on the record. Valid values are:

**•** `DELETE`

**•** `FULL`

**•** `READ`

**•** `TRANSFER`

**•** `WRITE`

**Example**

```
  FULL

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
Id

**Description**
The 15-character ID of the user for whom the insufficient access error occurred, either when
the user couldn’t access a record, the user couldn’t complete an operation, or the user was
the intended recipient of a record transfer that failed because the user didn’t have the required
access.

**Example**

```
  005XXXXXXXXXXXX

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_ID_DERIVED

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user for whom the insufficient access error
occurred, either when the user couldn’t access a record or the user was the intended recipient
of a record transfer that wasn’t completed.

**Example**

```
  005XXXXXXXXXXXXIA0

```

EventLogFile Supported Event Types

EventLogFile

_Knowledge Article_ [: Interpret Insufficient Access Event Logs](https://help.salesforce.com/s/articleView?id=000396437&type=1&language=en_US)

##### Invocable Action Event Type

Invocable Action events capture the calls to Salesforce Invocable Actions. This is particularly useful to monitor actions invoked during
Agentforce flows. This event type is available in API versions 64.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION_NAME

ACTION_TYPE

ACTION_VERSION

AGENT_ACTION

```

**Type**
String

**Description**
Name of the action.

**Type**
String

**Description**
InvocableActionType being referenced.

**Type**
String

**Description**
The invocable action version.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The API name of the agent action that invoked the action. This
field is available in API version 66.0 or later.

```
API_CALLER

BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

DURATION

EVENT_TYPE

FLOW_PROCESS_TYPE

FLOW_VERSION_ID

INVOCATION_SOURCE

```

**Type**
String

**Description**
Identifier of the API caller. This is only populated when the
action is invoked from a REST API call. This field is available in
API version 66.0 or later.

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
Time (in nanos) taken to process this set of requests.

**Type**
String

**Description**
The type of event. The value is always `InvocableAction` .

**Type**
String

**Description**
The process type of the calling flow.

**Type**
String

**Description**
The ID of the version of the calling flow.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
Indicates the source type that invoked the action. Valid values
are:

**•** Agent Action

**•** Apex

**•** Bot

**•** Flow

**•** Internal

**•** Prompt Template

**•** REST

This field is available in API version 66.0 or later.

```
INVOKING_APEX_CLASS_NAME

ORGANIZATION_ID

PLANNER_IDENTIFIER

PROMPT_TEMPLATE

REQUEST_COUNT

REQUEST_ID

```

**Type**
String

**Description**
The fully qualified name of the Apex class that invoked the
action. This field is available in API version 66.0 or later.

**Type**
Id

**Description**
The number of invoked requests.

**Type**
string

**Description**
The ID of the agent planner.

**Type**
string

**Description**
The API name of the prompt template that invoked the action.
This field is available in API version 66.0 or later.

**Type**
Number

**Description**
The number of invoked requests.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same REQUEST_ID.

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

##### Knowledge Article View Event Type

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format (YYYY-MM-DDTHH:MM:SS.sssZ). For example:
2015-07-27T11:32:59.555Z. Timezone is GMT.

**Type**
String

**Description**
ID of the user employing salesforce.com services, whether
through the user interface or API

Knowledge Article View events contain user activity with your knowledge base.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ARTICLE_ID

ARTICLE_STATUS

```

**Type**
Id

**Description**
The 15-character ID of the article.

For example: `00Dxx0000001gEb` .

**Type**
Character

**Description**
Possible values are:

**•** `D` —Draft


Standard Objects EventLogFile Supported Event Types

**•** `O` —Online

**•** `A` —Archived

```
ARTICLE_VERSION

ARTICLE_VERSION_ID

CONTEXT

ENTITY

EVENT_TYPE

LANGUAGE

```

**Type**
Number

**Description**
Article version number.

For example: `2` .

**Type**
Id

**Description**
The 15-character ID of the article version.

For example: `ka0R00000005rt6` .

**Type**
String

**Description**
Context of the request.

**Description**
Possible values are:

**•** `Apex`

**•** `API`

**•** empty string

**Type**
String

**Description**
Entity requested.

For example: `Knowledge__kav` .

**Type**
String

**Description**
The type of event. The value is always
`KnowledgeArticleView` .

**Type**
String

**Description**
iso-code of the language.

For example: `en_US` /


Standard Objects EventLogFile Supported Event Types

**Example**

```
LARGE_LANGUAGE_MODEL

LAST_VERSION

ORGANIZATION_ID

REQUEST_ID

SESSION_ID

TIMESTAMP

```

**Type**
String

**Description**
The name of the large language model (LLM) that generated
the knowledge article version.

**Type**
Boolean

**Description**
`True` if it is the last version.

Possible values are:

**•** `True`

**•** `False`

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
Session ID of the request.

For example:
`gV7pCSW2vGaaJNFi3GSpuPIjNbKVbSxRvx34LJsIvuc=` .

**Example**

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

##### Lightning Error Event Type

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Character

**Description**
User type of the request.

Possible values are:

**•** `A` —App

**•** `C` —Customer Portal

**•** `P` —Partner Portal

**•** `G` —guest

**•**

Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile app.
This event type is available in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

COMPONENT_NAME

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**

```
  96.43.144.26

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The internal name of the standard component that generated the error. The Salesforce
developer assigned the name when the standard component was created.

**Example**
`SaveEdit`, `Lead.CCPM_sendSMS`, `ChangeOwnerOne`

```
CONNECTION_TYPE

DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

```

**Type**
String

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
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

```
DEVICE_SESSION_ID

EVENT_TYPE

LOGIN_KEY

MESSAGE

ORGANIZATION_ID

```

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. If the user reloads a page,
it starts a new session.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
String

**Description**
The type of event. The value is always `LightningError` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The error message generated.

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
OS_NAME

OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
Context of the page where the event occurred.

**Example**

```
  clients:cardsContainer

```

**Type**
Id

**Description**
The unique entity identifier of the event.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`Task`, `Account`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PAGE_START_TIME

PAGE_URL

REQUEST_ID

SDK_APP_TYPE

SDK_APP_VERSION

```

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

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

```
  5.0

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SDK_VERSION

SESSION_KEY

STACK_TRACE

TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_ID

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When a user logs out and logs in again, a new session is started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The stack trace contains the location in the code where the error occurred along with the
calling frames that led to the error.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
ID of the Lightning event type.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

```
UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

```

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
The source of the error event.

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

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of error event.

**Example**
`error`, `info`, `warn`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Lightning Interaction Event Type

Lightning Interaction events track user actions in Lightning Experience and the Salesforce mobile app, such as the user clicking, tapping,
or scrolling on a page. This event type is available in the EventLogFile object in API version 39.0 and later.

Warning: The Lightning Interaction Event type is a best effort logging of user interactions but is not intended to meet privacy
and security audit requirements. Not all interactions or CRUD operations are tracked and data loss may occur.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   United States/California

```

```
CLIENT_ID

CLIENT_IP

COMPONENT_NAME

CONNECTION_TYPE

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such
as a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**

```
  96.43.144.26

```

**Type**
String

**Description**
The internal name of the standard component that the user interacted with. The Salesforce
developer assigned the name when the standard component was created.

**Example**
`SaveEdit`, `Lead.CCPM_sendSMS`, `ChangeOwnerOne`

**Type**
String

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `WIFI`

```
DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

DURATION

EVENT_TYPE

```

**Type**
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
Number

**Description**
The duration in milliseconds since the page start time.

**Type**
String

**Description**
The type of event. The value is always `LightningInteraction` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
GRANDPARENT_UI_ELEMENT

LOGIN_KEY

ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

```

**Type**
String

**Description**
Grandparent scope of the page element where the event occurred.

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Context of the page where the event occurred.

**Example**

```
                   clients:cardsContainer

```

Note: A value of `UNKNOWN` means that the page hasn't finished loading, so the
context can't be identified.

```
PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_START_TIME

PAGE_URL

```

**Type**
Id

**Description**
The unique entity identifier of the event.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`task`, `contacts`

Note: A value of `UNKNOWN` means that the page hasn't finished loading or the
page isn't displaying a record, so the entity type can't be identified.

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record
IDs can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

Note: A value of `UNKNOWN` means that the page hasn't finished loading, so the
URL can't be identified.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PARENT_UI_ELEMENT

RECORD_ID

RECORD_TYPE

RELATED_LIST

REQUEST_ID

SDK_APP_TYPE

```

**Type**
String

**Description**
Parent scope of the page element where the event occurred.

**Type**
String array

**Description**
The IDs of one or more records that the user interacted with. For more information on the
user interaction, see `UI_EVENT_TYPE` and `UI_EVENT_SOURCE` fields.

**Example**

```
  ["5004100000JaGGLAA3", "5004100000Dn79CAAR",

  "50041000007KeugAAC"]

```

**Type**
String

**Description**
The type of record object that the user interacted with.

**Example**
`Account`, `Opportunity`

**Type**
String

**Description**
The type of related list that the user clicked.

**Example**

```
  Opportunity

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The mobile SDK application type.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

```
SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

TARGET_UI_ELEMENT

TIMESTAMP

```

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The target page element where the event occurred.

**Example**

```
  tabitem-link

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

UI_EVENT_ID

UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
The user action on the record or records in `RECORD_ID` . This field’s value indicates whether
the user’s action was on a single record or multiple records. For example, `read` indicates
that one record was read (such as on a record detail page); `reads` indicates that multiple
records were read (such as in a list view).

**Examples**

**•** `click`

**•** `create`

**•** `delete`

**•** `hover`

**•** `read`

**•** `update`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of interaction with the records in `RECORD_ID` .

**Example**
`crud`, `system`, `user`, `userInteraction`

**Type**
String

**Description**
The numeric code for the type of client used to make the request (for example, the browser,
application, or API) as a string.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through
the UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

##### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Lightning Logger Event Type

Lightning Logger events contain information from observed Lightning component logs. This event type is available in the EventLogFile
object in API version 58.0 and later.

To enable Lightning Logger events, from Setup, in the Quick Find box, enter _`event`_, and then select **Event Monitoring Settings** . Turn
on Lightning Logger Events.

Note: The browser sends Lightning Logger event logs to the server in batches. Batches are sent when the user interacts with the
page and when the page closes or refreshes. If the user experiences connectivity issues or if their login session expires due to
browser inactivity, any pending Lightning Logger event logs on the browser are erased. There isn’t a way to retrieve these lost
logs.

The limit for Lightning Logger events is 30,000 events per minute per organization. Burst capacity may support up to 45,000-50,000
events per minute, but this is not guaranteed. The `MESSAGE` field shows details about what's logged when the limit is hit.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The name of the application the user accessed.

```
BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

CONNECTION_TYPE

```

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
Chrome, IE, Safari, Gecko

**Type**
String

**Description**
The user’s browser version in `major.minor` format. Some
browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of
<Country>/<State|Province>.

**Example**
United States/California

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP, such as a login from AppExchange, is
shown as “Salesforce.com IP”.

**Example**

```
   96.43.144.26

```

**Type**
String

**Description**
The type of connection.


Standard Objects EventLogFile Supported Event Types

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

```
DEVICE_MODEL

DEVICE_PLATFORM

```

**Type**
String

**Description**
The name of the device model.

**Example**
iPad, iPhone

**Type**
String

**Description**
The type of application experience in
`name:experience:form` format.

**Possible Values**
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


Standard Objects EventLogFile Supported Event Types

```
DEVICE_SESSION_ID

EVENT_TYPE

LOGIN_KEY

MESSAGE

ORGANIZATION_ID

OS_NAME

```

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load
time. When the user reloads a page, a new session is started.

**Example**
321a1ddfaf924803a075f1e69fc87bc06f53ccd0

**Type**
String

**Description**
The type of event. The value is always `LightningLogger` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session.
It starts with a login event and ends with either a logout event
or the user session expiring.

**Example**
GeJCsym5eyvtEK2I

**Type**
String

**Description**
The message passed to the `lightning/logger log()`
method. The message can be a JSON object or a string. String
length is limited to 4 KB (4096 characters).

If you hit the logger limit, subsequent events are muted for a
minute. During this time, the message field is replaced with
this text: `Rate limiting hit for this`
`organization.` Lightning Logger events resume when
the limit resets in the next minute.

**Type**
String

**Description**
The 15-character ID of the org.

**Example**
00D000000000123

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The operating system name, derived from the User Agent.

**Example**
Android, iOS, OSX, Windows

```
OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_URL

REQUEST_ID

```

**Type**
String

**Description**
The operating system version, derived from the User Agent.

**Type**
String

**Description**
The name of the component hosting the main page content.

**Example**
clients:cardsContainer

**Type**
Id

**Description**
The entity ID (if any) of the record being displayed.

**Example**
0013000000I3zJAAAZ

**Type**
String

**Description**
The entity type of the page being displayed.

**Example**
Task, contacts

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce
mobile app page that the user opened. The page can contain
one or more Lightning components. Multiple record IDs can
be associated with `PAGE_URL` .

**Example**
/sObject/0064100000JXITSAA5/view

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

**Example**
3nWgxWbDKWWDIk0FKfF5DV

```
SDK_APP_TYPE

SDK_APP_VERSION

SDK_VERSION

SEQUENCE

SESSION_KEY

```

**Type**
String

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
String

**Description**
The mobile SDK version number.

**Example**
2.1.0

**Type**
Number

**Description**
An auto-incremented sequence number of the current event
since the session started.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. Use this value to identify all events
in Lightning Experience within a session. When the user logs
out and logs in again, a new session is started.

**Example**
cdd09305cb6babf34059e27f70e47f1b11dec868

```
TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_RELATIVE_TIMESTAMP

UI_EVENT_TIMESTAMP

USER_ID

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**
20130715233322.670

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format (YYYY-MM-DDTHH:MM:SS.sssZ).

**Example**
2015-07-27T11:32:59.555Z. The timezone is GMT.

**Type**
Number

**Description**
Difference in milliseconds between when the message was
logged and when the browser tab was opened.

**Example**
29322.23

**Type**
Number

**Description**
The time at which this event occurred, measured in
milliseconds.

**Example**

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services
through the UI or API.


Standard Objects EventLogFile Supported Event Types

**Example**
00530000009M943

```
USER_ID_DERIVED

USER_TYPE

##### Lightning Page View Event Type

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using
Salesforce services through the UI or the API.

**Example**
00590000000I1SNIA0

**Type**
String

**Description**
The category of user license of the user accessing Salesforce
services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

##### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

Lightning Page View events represent information about the page on which the event occurred in Lightning Experience and the Salesforce
mobile app, such as the page's load time. This event type is available in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

CONNECTION_TYPE

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as `Salesforce.com IP` .

**Example**

```
  96.43.144.26

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

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

```
DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

```

**Type**
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
                   321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

```
DURATION

EFFECTIVE_PAGE_TIME

EFFECTIVE_PAGE_TIME_DEVIATION

EFFECTIVE_PAGE_TIME_DEVIATION_ERROR_TYPE

EFFECTIVE_PAGE_TIME_DEVIATION_REASON

```

**Type**
Number

**Description**

If the page completes loading, then `DURATION` indicates the duration of time in milliseconds
between `PAGE_START_TIME` and when the loading completes. In this case, `DURATION`
corresponds to `EFFECTIVE_PAGE_TIME` .

If the page doesn't complete loading, then `DURATION` indicates the duration of time in
milliseconds between `PAGE_START_TIME` and when the user navigates to another page.

**Type**
Double

**Description**
Indicates how many milliseconds it takes for the page to load before a user can interact with
the page. Multiple factors can affect effective page time (EPT), such as network speed,
hardware performance, or page complexity.

**Type**
Boolean

**Description**
When a deviation is detected, `EFFECTIVE_PAGE_TIME_DEVIATION` records `true` .
The default value is `false` .

**Type**
String

**Description**
Indicates the origin of an error. This field is populated when
EFFECTIVE_PAGE_TIME_DEVIATION_REASON contains the PAGE_HAS_ERROR value.

**Possible Values**

**•** `CUSTOM` —An error originating from the customer's system or network.

**•** `SYSTEM` —An error originating in Salesforce.

**Type**
String

**Description**
The reason for deviation in page loading time.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `PageHasError` —An undefined page loading error occurred.

**•** `PageNotLoaded` —If a customer navigates away from a page while loading processes
are in progress, the page doesn't finish loading.

**•** `PreviousPageNotLoaded` —When navigating to a new page, and the previous
page hasn't completed loading, the next page is considered to have a deviation.
Incomplete loading processes on a previous page can affect how the next page loads.

**•** `InteractionsBeforePageLoaded` —A user interacts with a page element
before the page is fully loaded.

**•** `PageInBackgroundBeforeLoaded` —A background loading process runs on a
page. Background processes run when a user navigates away from a page to another
browser tab. The browser de-prioritizes the page in the background until the user activates
the page’s tab. Because a user can leave a page in the background for a long time, the
page is expected to have a high Effective Page Time (EPT).

```
EVENT_TYPE

GRANDPARENT_UI_ELEMENT

LOGIN_KEY

ORGANIZATION_ID

OS_NAME

```

**Type**
String

**Description**
The type of event. The value is always `LightningPageView` .

**Type**
String

**Description**
The grandparent scope of the page element where the event occurred.

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

```
OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_FLEXI_PAGE_NAME_OR_ID

```

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
The name of the component hosting the main content of the page.

**Example**

```
  clients:cardsContainer

```

**Type**
Id

**Description**
The ID of the record that the user accessed which triggered the event on the page.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`Task`, `contacts`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The page name or identifier.

**Example**

```
                   runtime_sales_seller_home__SellerHome_L

```

```
PAGE_FLEXI_PAGE_TYPE

PAGE_START_TIME

PAGE_URL

PARENT_UI_ELEMENT

PREVPAGE_APP_NAME

PREVPAGE_CONTEXT

```

**Type**
String

**Description**
The page type.

**Example**

```
  HomePage

```

**Type**
Number

**Description**
The time when the page starts loading, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
String

**Description**
The parent scope of the page element where the event occurred.

**Type**
String

**Description**
The internal name of the previous application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The context of the previous page where the event occurred.

**Example**

```
                   clients:cardsContainer

```

```
PREVPAGE_ENTITY_ID

PREVPAGE_ENTITY_TYPE

PREVPAGE_URL

REQUEST_ID

SDK_APP_TYPE

```

**Type**
Id

**Description**
The unique previous page entity identifier of the event.

**Type**
String

**Description**
The previous page entity type of the event.

**Example**
`Task`, `contacts`

**Type**
String

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened.

**Example**

```
  /sObject/006410000

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `NATIVE`

**•** `REACTNATIVE`

```
SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

TARGET_UI_ELEMENT

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The target page element where the event occurred.

**Example**

```
  tabitem-link

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The timezone is GMT.

```
UI_EVENT_ID

UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

UI_EVENT_TIMESTAMP

USER_AGENT

USER_ID

```

**Type**
String

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
This field is being deprecated and is mostly null, except in mobile app views where it indicates
the page type of views where the context is “native.”

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of client used to make the request (for example, the browser, application, or API)
as a string.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
                   00530000009M943

```

```
USER_ID_DERIVED

USER_TYPE

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

EventLogFile Supported Event Types

EventLogFile


Standard Objects EventLogFile Supported Event Types

##### Lightning Performance Event Type

Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This event type is available
in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String

**Description**
The API client ID.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CONNECTION_TYPE

DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

```

**Type**
String

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
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

```
DEVICE_SESSION_ID

DURATION

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

OS_NAME

```

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
Number

**Description**
The duration in milliseconds since the page start time.

**Type**
String

**Description**
The type of event. The value is always `LightningPerformance` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

```
OS_VERSION

PAGE_START_TIME

REQUEST_ID

SDK_APP_TYPE

SDK_APP_VERSION

```

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   5.0

```

```
SDK_VERSION

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_ID

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `ltng:pageView`

**•** `ltng:performance`

Note: Any other value, such as `ltng:bootstrap`, is for internal usage only.

```
UI_EVENT_SOURCE

UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

USER_AGENT

USER_ID

```

**Type**
String

**Description**
The user action on the record or records. This field’s value indicates whether the user’s action
was on a single record or multiple records. For example, `read` indicates that one record
was read (such as on a record detail page); `reads` indicates that multiple records were read
(such as in a list view).

**Example**

**•** `click`

**•** `create`

**•** `delete`

**•** `hover`

**•** `read`

**•** `update`

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of performance event.

**Example**
`bootstrap`, `defs`, `performance`

**Type**
String

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
                   00530000009M943

```

```
USER_ID_DERIVED

USER_TYPE

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

EventLogFile Supported Event Types

EventLogFile


Standard Objects EventLogFile Supported Event Types

##### Login Event Type

Login events contain details about your org’s user login history.

Note: The Login event type is used by EventLogFile (ELF). It isn’t a real-time event. For the LoginEvent real-time event, which is
[part of Real-Time Event Monitoring (RTEM), see LoginEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm) _Platform Events Developer Guide_ .

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_TYPE

API_VERSION

AUTHENTICATION_CONTEXT_CLASS_REFERENCE

```

**Type**
String

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
String

**Description**
If provided by a third-party identity provider, the authentication
method indicated in the Authentication Context Class
Reference (ACR) claim.

**•** SAML providers—Stores the value of the
`AuthnContextClassRef` statement in the SAML
response.

**•** OpenID Connect providers—Stores the value of the ACR
claim in the ID token


Standard Objects EventLogFile Supported Event Types

This field is available in API version 66.0 and later.

```
AUTHENTICATION_METHOD_REFERENCE

AUTHENTICATION_SERVICE_ID

BROWSER_TYPE

CIPHER_SUITE

```

**Type**
String

**Description**
If provided by a third-party identity provider, the authentication
method indicated in the Authentication Method Reference
(AMR) claim.

**•** SAML providers—Stores the value of any attribute named
`AMR` or `authmethodsreferences` in the SAML
response.

**•** OpenID Connect providers—Stores the value of the AMR
claim in the ID token.

This field is available in API version 51.0 and later.

**Type**
Id

**Description**
The 15-character ID for the authentication service used to log
in. This field stores IDs for these authentication services.

**•** SAML single sign-on providers

**•** Token exchange handlers

Available in API version 60.0 and later.

**Type**
String

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10.12; rv%3A50.0) Gecko/20100101

    Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10_11_6) AppleWebKit/537.36 (KHTML,

    like Gecko) Chrome/51.0.2704.84

    Safari/537.36

```

**Type**
String

**Description**
The TLS cipher suite used for the login. Values are
OpenSSL-style cipher suite names, with hyphen delimiters. For


Standard Objects EventLogFile Supported Event Types

[more information, see OpenSSL Cryptography and SSL/TLS](https://www.openssl.org/source/)
[Toolkit.](https://www.openssl.org/source/)

```
CLIENT_IP

COUNTRY_CODE

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

FORWARDED_FOR_IP

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The country code associated with the IP address of the user
logging in.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String

**Description**
The type of event. The value is always `Login` .

**Type**
String

**Description**
The value in the `X-Forwarded-For` header of HTTP
requests sent by the client. For logins that use one or more
HTTP proxies, the `X-Forwarded-For` header is sometimes
used to store the origin IP and all proxy IPs.


Standard Objects EventLogFile Supported Event Types

The `FORWARDED_FOR_IP` field stores whatever value the
client sends, which might not be an IP address. The maximum
length is 256 characters. Longer values are truncated. The
`FORWARDED_FOR_IP` field isn’t populated for logins
completed via OAuth flows or single sign-on (SSO).

Available in API version 61.0 and later.

```
HTTP_REFERER

LOGIN_KEY

LOGIN_STATUS

LOGIN_SUB_TYPE

LOGIN_TYPE

```

**Type**
String

**Description**
The referring URI of the page that’s receiving the request.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The status of the login attempt. For successful logins, the value
is LOGIN_NO_ERROR. All other values indicate errors or
authentication issues. For details, see Login Event Type —
LOGIN_STATUS Values on page 2308.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The type of login flow used. See the `LoginSubType` field
[of LoginHistory in the Object Reference guide for the list of](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)
possible values.

Label is **Login Subtype** .

**Type**
String

**Description**
The type of login used to access the session.

Possible values are:

**•** `7` —AppExchange


Standard Objects EventLogFile Supported Event Types

**•** `A` —Application

**•** `s` —Certificate-based login

**•** `k` —Chatter Communities External User

**•** `n` —Chatter Communities External User Third Party SSO

**•** `x` —Cross Tenant Login (for internal use only)

**•** `r` —Employee Login to Community

**•** `z` —Lightning Login

**•** `l` —Networks Portal API Only

**•** `6` —Remote Access Client

**•** `i` —Remote Access 2.0

**•** `I` —Other Apex API

**•** `R` —Partner Product

**•** `w` —Passwordless Login

**•** `3` —Customer Service Portal

**•** `q` —Partner Portal Third-Party SSO

**•** `9` —Partner Portal

**•** `5` —SAML Idp Initiated SSO

**•** `m` —SAML Chatter Communities External User SSO

**•** `b` —SAML Customer Service Portal SSO

**•** `c` —SAML Partner Portal SSO

**•** `h` —SAML Site SSO

**•** `8` —SAML Sfdc Initiated SSO

**•** `E` —SelfService

**•** `j` —Third Party SSO

```
LOGIN_URL

ORGANIZATION_ID

REQUEST_ID

```

**Type**
String

**Description**
The URL of the login page.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_STATUS

RUN_TIME

SESSION_KEY

SOURCE_IP

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started. For Login Event Type, this
field is usually null because the event is captured before a
session is created.

**Example**
d7DEq/ANa7nNZZVD

**Type**
IP


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the incoming client request that first reaches
Salesforce during a login. For example, `126.7.4.2` . For
clients that redirect through one or more HTTP proxies, this
field stores the IP address of the first proxy to reach Salesforce.
To better identify the origin IP for these cases, check the
`FORWARDED_FOR_IP` field instead.

```
TIMESTAMP

TIMESTAMP_DERIVED

TLS_PROTOCOL

URI

URI_ID_DERIVED

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Time zone
is GMT.

**Type**
String

**Description**
The TLS protocol used for the login.

**Example**
There are 3 possible values.

**•** 1.0

**•** 1.1

**•** 1.2

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

```
USE_API_TOKEN

USER_ID

USER_ID_DERIVED

USER_NAME

USER_TYPE

```

**Type**
String

**Description**
Login with API Token - T token, or P password.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The username that’s used for login.

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.


Standard Objects EventLogFile Supported Event Types

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

Login Event Type — LOGIN_STATUS Values
When users attempt to log in to your org, the success or failure of their login attempts is tracked in event log file data. Specifically,
the LOGIN_STATUS field in the Login event type contains the result of these login attempts. The data in LOGIN_STATUS can help
you determine whether your users’ login attempts were successful. This field is available in the Login event type in the EventLogFile
object in API version 39.0 and later.

SEE ALSO:

Login Event Type — LOGIN_STATUS Values

EventLogFile Supported Event Types

EventLogFile

Login Event Type — LOGIN_STATUS Values

When users attempt to log in to your org, the success or failure of their login attempts is tracked in event log file data. Specifically, the
LOGIN_STATUS field in the Login event type contains the result of these login attempts. The data in LOGIN_STATUS can help you
determine whether your users’ login attempts were successful. This field is available in the Login event type in the EventLogFile object
in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

**API Error Code** **Details (If Available)**

LOGIN_CHALLENGE_ISSUED Failed: Computer activation required

LOGIN_CHALLENGE_PENDING Failed: Computer activation pending

LOGIN_DATA_DOWNLOAD_ONLY

LOGIN_END_SESSION_TXN_SECURITY_POLICY


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_ERROR_API_TOO_OLD

Failed: API Version Removed. The API version specified for login is
below the minimum supported value, and has been removed. Update
to a newer, supported API version.

LOGIN_ERROR_APPEXCHANGE_DOWN Unable to process your login request

LOGIN_ERROR_ASYNC_USER_CREATE

LOGIN_ERROR_AVANTGO_DISABLED

LOGIN_ERROR_AVANTGO_TRIAL_EXP

LOGIN_ERROR_CLIENT_NO_ACCESS

LOGIN_ERROR_CLIENT_REQ_UPDATE Failed: Client update required

LOGIN_ERROR_CSS_FROZEN

LOGIN_ERROR_CSS_PW_LOCKOUT

LOGIN_ERROR_DUPLICATE_USERNAME

LOGIN_ERROR_EXPORT_RESTRICTED Restricted country

LOGIN_ERROR_GLOBAL_BLOCK_DOMAIN Restricted domain

LOGIN_ERROR_HT_DOWN

LOGIN_ERROR_HTP_METHD_INVALID Failed: Invalid HTTP method

LOGIN_ERROR_INSECURE_LOGIN Failed: Login over insecure channel

LOGIN_ERROR_INVALID_GATEWAY Invalid gateway

LOGIN_ERROR_INVALID_ID_FIELD

LOGIN_ERROR_INVALID_PASSWORD Invalid password

LOGIN_ERROR_LOGINS_EXCEEDED Maximum logins exceeded

LOGIN_ERROR_MUST_USE_API_TOKEN Failed: API security token required

LOGIN_ERROR_MUTUAL_AUTHENTICATION Mutual authentication failed

LOGIN_ERROR_NETWORK_INACTIVE Invalid - Experience Cloud site offline

LOGIN_ERROR_NO_HT_ACCESS

LOGIN_ERROR_NO_NETWORK_ACCESS No Experience Cloud site access

LOGIN_ERROR_NO_NETWORK_INFO

LOGIN_ERROR_NO_PORTAL_ACCESS Invalid profile association

LOGIN_ERROR_NO_SET_COOKIES

LOGIN_ERROR_OFFLINE_DISABLED Offline disabled

LOGIN_ERROR_OFFLINE_TRIAL_EXP Offline trial expired


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_ERROR_ORG_CLOSED Organization closed

LOGIN_ERROR_ORG_DOMAIN_ONLY Restricted domain

LOGIN_ERROR_ORG_IN_MAINTENANCE Organization is in maintenance

LOGIN_ERROR_ORG_INACTIVE Organization is inactive

LOGIN_ERROR_ORG_IS_DOT_ORG Organization is a DOT

LOGIN_ERROR_ORG_LOCKOUT Organization locked

LOGIN_ERROR_ORG_SIGNING_UP

LOGIN_ERROR_ORG_SUSPENDED Organization suspended

LOGIN_ERROR_OUTLOOK_DISABLED Outlook integration disabled

LOGIN_ERROR_PAGE_REQUIRES_LOGIN

LOGIN_ERROR_PASSWORD_EMPTY

LOGIN_ERROR_PASSWORD_LOCKOUT Password lockout

LOGIN_ERROR_PORTAL_INACTIVE Invalid - Portal disabled

LOGIN_ERROR_RATE_EXCEEDED Login rate exceeded

LOGIN_ERROR_RESTRICTED_DOMAIN Restricted IP

LOGIN_ERROR_RESTRICTED_TIME Restricted time

LOGIN_ERROR_SESSION_TIMEOUT

LOGIN_ERROR_SSO_PWD_INVALID Invalid password

LOGIN_ERROR_SSO_SVC_DOWN Your company's authentication service is down

LOGIN_ERROR_SSO_URL_INVALID The Single Sign-On Gateway URL is invalid

LOGIN_ERROR_STORE

LOGIN_ERROR_STORE_DOWN

LOGIN_ERROR_SWITCH_SFDC_INSTANCE

LOGIN_ERROR_SWITCH_SFDC_LOGIN

LOGIN_ERROR_SYNCOFFLINE_DISBLD Failed: Mobile disabled

LOGIN_ERROR_SYSTEM_DOWN

LOGIN_ERROR_UNKNOWN_ERROR Login invalid

LOGIN_ERROR_USER_API_ONLY Failed: API-only user

LOGIN_ERROR_USER_FROZEN User is frozen

LOGIN_ERROR_USER_INACTIVE User is inactive


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_ERROR_USER_NON_MOBILE Failed: Mobile license required

LOGIN_ERROR_USER_STORE_ACCESS

LOGIN_ERROR_USERNAME_EMPTY

LOGIN_ERROR_WIRELESS_DISABLED Wireless disabled

LOGIN_ERROR_WIRELESS_TRIAL_EXP Wireless trial expired

LOGIN_LIGHTNING_LOGIN Lightning Login required

LOGIN_NO_ERROR

LOGIN_OAUTH_API_DISABLED Failed: OAuth API access disabled

LOGIN_OAUTH_CONSUMER_DELETED Failed: Consumer Deleted

LOGIN_OAUTH_DS_NOT_EXPECTED Failed: Activation secret not expected

LOGIN_OAUTH_EXCEED_GET_AT_LMT Failed: Get Access Token Limit Exceeded

LOGIN_OAUTH_INVALID_CODE_CHALLENGE Failed: Invalid Code Challenge

LOGIN_OAUTH_INVALID_CODE_VERIFIER Failed: Invalid Code Verifier

LOGIN_OAUTH_INVALID_DEVICE Failed: Device Id missing or not registered

LOGIN_OAUTH_INVALID_DS Failed: Activation secret invalid

LOGIN_OAUTH_INVALID_DSIG Failed: Signature Invalid

LOGIN_OAUTH_INVALID_IP Failed: IP Address Not Allowed

LOGIN_OAUTH_INVALID_NONCE Failed: Invalid Nonce

LOGIN_OAUTH_INVALID_SIG_METHOD Failed: Invalid Signature Method

LOGIN_OAUTH_INVALID_TIMESTAMP Failed: Invalid Timestamp

LOGIN_OAUTH_INVALID_TOKEN Failed: Invalid Token

LOGIN_OAUTH_INVALID_VERIFIER Failed: Invalid Verifier

LOGIN_OAUTH_INVALID_VERSION Failed: Version Not Supported

LOGIN_OAUTH_MISSING_DS Activation secret missing

LOGIN_OAUTH_NO_CALLBACK_URL Failed: Invalid Callback URL

LOGIN_OAUTH_NO_CONSUMER Missing Consumer Key Parameter

LOGIN_OAUTH_NO_TOKEN Missing OAuth Token Parameter

LOGIN_OAUTH_NONCE_REPLAY Failed: Nonce Replay Detected

LOGIN_OAUTH_PACKAGE_MISSING Package for this consumer is not installed in your organization

LOGIN_OAUTH_PACKAGE_OLD Installed package for this consumer is out of date


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_OAUTH_UNEXPECTED_PARAM Failed: Unexpected parameter

LOGIN_ORG_TRIAL_EXP Trial Expired

LOGIN_READONLY_CANNOT_VALIDATE

LOGIN_SAML_INVALID_AUDIENCE Failed: Audience Invalid

LOGIN_SAML_INVALID_CONFIG Failed: Configuration Error/Perm Disabled

LOGIN_SAML_INVALID_FORMAT Failed: Assertion Invalid

LOGIN_SAML_INVALID_IN_RES_TO Failed: InResponseTo Invalid

LOGIN_SAML_INVALID_ISSUER Failed: Issuer Mismatched

LOGIN_SAML_INVALID_ORG_ID Failed: Invalid Organization Id

LOGIN_SAML_INVALID_PORTAL_ID Failed: Invalid Portal Id

LOGIN_SAML_INVALID_RECIPIENT Failed: Recipient Mismatched

LOGIN_SAML_INVALID_SESSION_LEVEL

LOGIN_SAML_INVALID_SIGNATURE Failed: Signature Invalid

LOGIN_SAML_INVALID_SITE_URL Failed: Invalid Site URL

LOGIN_SAML_INVALID_STATUS Failed: Status Invalid

LOGIN_SAML_INVALID_SUB_CONFIRM Failed: Subject Confirmation Error

LOGIN_SAML_INVALID_TIMESTAMP Failed: Assertion Expired

LOGIN_SAML_INVALID_USERNAME Failed: Username Or SSO Id Invalid

LOGIN_SAML_INVALID_VERSION

LOGIN_SAML_MISMATCH_CERT Failed: Signature Invalid/Configured Certificate Mismatch

LOGIN_SAML_MISSING_ORG_ID Failed: Missing Organization Id for Portal login

LOGIN_SAML_MISSING_PORTAL_ID Failed: Missing Portal Id

LOGIN_SAML_PROVISION_ERROR Failed: SAML Provision Error

LOGIN_SAML_REPLAY_ATTEMPTED Failed: Replay Detected

LOGIN_SAML_SITE_INACTIVE Failed: Specified Site is Inactive

LOGIN_TWOFACTOR_REQ Multi-factor (formerly called two-factor) is required

Usage

Use LOGIN_STATUS to determine whether your users’ login attempts were successful. For example, you can determine whether a
departed employee attempted to log in successfully or unsuccessfully.


Standard Objects EventLogFile Supported Event Types

SEE ALSO:

Login Event Type

EventLogFile Supported Event Types

EventLogFile

##### Login As Event Type

Login As events contain details about what a Salesforce admin did while logged in as another user.

Note: Login As Event Type is used by EventLogFile (ELF). It isn’t a real-time event. For the LoginAsEvent real-time event, which
[is part of Real-Time Event Monitoring (RTEM), see LoginAsEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginasevent.htm) _Platform Events Developer Guide_ .

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: Bolster your security posture by receiving alerts and blocking potentially malicious LoginAsEvent activities with a Transaction
Security policy.

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DELEGATED_USER_ID

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or API. In this case, the user who’s doing the
impersonation.


Standard Objects EventLogFile Supported Event Types

```
DELEGATED_USER_ID_DERIVED

DELEGATED_USER_NAME

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using
Salesforce services through the UI or API. In this case, the user
who’s doing the impersonation.

**Type**
String

**Description**
The username of the user who’s using Salesforce services
through the UI or API. In this case, the user who’s doing the
impersonation.

**Type**
String

**Description**
The type of event. The value is always `LoginAs` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The amount of time that the request took in milliseconds.

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`


Standard Objects EventLogFile Supported Event Types

```
USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Logout Event Type

Contains details of user sessions ending or being revoked.

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Note: Logout Event Type is used by EventLogFile (ELF). It isn’t a real-time event. For the LogoutEvent real-time event, which is
[part of Real-Time Event Monitoring (RTEM), see LogoutEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_logoutevent.htm) _Platform Events Developer Guide_ .

These scenarios count as logout events.

**•** Logging out via the UI

**•** Session expiration

**•** Revoking access for a connected app

**•** Calling the Salesforce revocation endpoint

**•** Salesforce disabling a connected app

**•** Note: For batch operations where multiple sessions are revoked at once, Salesforce records only one logout event. You can
tell that it’s a batch operation because there’s no user ID.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_TYPE

```

**Type**
String

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex


Standard Objects EventLogFile Supported Event Types

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

```
API_VERSION

APP_TYPE

BROWSER_TYPE

CLIENT_IP

```

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
Number

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
String

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10.12; rv%3A50.0) Gecko/20100101

    Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10_11_6) AppleWebKit/537.36 (KHTML,

    like Gecko) Chrome/51.0.2704.84

    Safari/537.36

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CLIENT_VERSION

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

PLATFORM_TYPE

```

**Type**
Number

**Description**
The version of the client that was in use upon logging out.

**Type**
String

**Description**
The type of event. The value is always `Logout` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Number

**Description**
The code for the client platform. If a timeout caused the logout,
this field is null.

**Example Values**

**•** `1000` : Windows

**•** `1008` : Windows 2003

**•** `1013` : Windows 8.1

**•** `1015` : Windows 10

**•** `2003` : Macintosh/Apple OSX

**•** `4000` : Linux


Standard Objects EventLogFile Supported Event Types

**•** `5005` : Android

**•** `5006` : iPhone

**•** `5007` : iPad

**•** `5200` : Android 10.0

```
REQUEST_ID

RESOLUTION_TYPE

SESSION_KEY

SESSION_LEVEL

SESSION_TYPE

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The screen resolution of the client. If a timeout caused the
logout, this field is null.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The security level of the session that was used when logging
out.

**Possible Values**

**•** `1` : Standard Session

**•** `10` : High-Assurance Session

**Type**
String

**Description**
The session type that was used when logging out.

**Possible Values**

**•** `A` : API


Standard Objects EventLogFile Supported Event Types

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

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

When a customer logs out by using the **Logout** button, the
`TIMESTAMP` field records the actual logout time. However,
when a customer is logged out automatically, Salesforce
detects the event by using a process that runs every 15
minutes. `TIMESTAMP` values can reflect a logout time up to
15 minutes later than the actual automatic logout time.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

```
USER_ID_DERIVED

USER_INITIATED_LOGOUT

USER_TYPE

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Boolean

**Description**
The value is 1 if the user intentionally logged out of the
organization by clicking the **Logout** button. If the user’s session
timed out due to inactivity or another implicit logout action,
the value is 0.

**Type**
String

**Description**
The category of user license of the user that logged out.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard


Standard Objects EventLogFile Supported Event Types

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Metadata API Operation Event Type

Metadata API Operation events contain details of Metadata API retrieval and deployment requests.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_VERSION

CLIENT_ID

CLIENT_IP

CPU_TIME

EVENT_TYPE

```

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always
`MetadataApiOperation` .

```
LOGIN_KEY

OPERATION

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

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
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.


Standard Objects EventLogFile Supported Event Types

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Multiblock Report Event Type

Multiblock Report events contain details about Joined Report reports.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

HAS_CHART

LOGIN_KEY

MASTER_REPORT_ID

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The type of event. The value is always `MultiblockReport` .

**Type**
Boolean

**Description**
True if the report has a chart.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The 15-character ID of the master report.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:


Standard Objects EventLogFile Supported Event Types

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.


Standard Objects EventLogFile Supported Event Types

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Named Credential Event Type

The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in the
named credential event log file, then you can investigate whether a security breach has occurred. This event type is available in the
EventLogFile object in API version 53.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CALLER_PACKAGE_NAMESPACE

CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

NAMED_CREDENTIAL_NAME

```

**Type**
String

**Description**
If an Apex callout using a Named Credential endpoint is initiated from a package, then this
field contains the package’s namespace. If the callout isn’t initiated from a package, then
this field is empty.

**Example**
Acme

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Description**
The type of event. The value is always `NamedCredential` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The name of the named credential that’s the endpoint of the Apex callout.

**Example**
My_Named_Credential


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
ORGANIZATION_ID

PLANNER_IDENTIFIER

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
ID

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case-safe ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case-safe ID of the user who’s using Salesforce services through the UI or
the API.

For example: `00590000000I1SNIA0` .

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

EventLogFile Supported Event Types

EventLogFile

##### One Commerce Usage Event Type

One Commerce Usage events capture information about your Commerce instance. This event type is available in the EventLogFile object
in API version 51.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Package Install Event Type

Package Install events contain details about package installation in the organization.


Standard Objects EventLogFile Supported Event Types

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

EVENT_TYPE

FAILURE_TYPE

IS_MANAGED

IS_PUSH

IS_RELEASED

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `PackageInstall` .

**Type**
String

**Description**
A general categorization of any error that’s encountered.

**Type**
Boolean

**Description**
True if the operation is performed on a managed package.

**Type**
Boolean

**Description**
True if the package was installed as a result of a push upgrade.

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Description**
True if the operation is performed on a released package.

```
IS_SUCCESSFUL

LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

PACKAGE_NAME

REQUEST_ID

```

**Type**
Boolean

**Description**
True if the package was successfully installed.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of package operation.

**Possible Values**

**•** INSTALL

**•** UPGRADE

**•** EXPORT

**•** UNINSTALL

**•** VALIDATE_PACKAGE

**•** INIT_EXPORT_PKG_CONTROLLER

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The name of the package that’s being installed.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Permission Update Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets or
permission set groups.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: This event type tracks if Salesforce updates object or field permissions in standard profiles, in addition to changes you make
to your custom profiles, permission sets, and permission set groups.

Fields

**Field** **Details**

```
CONTEXT

DESCRIPTION

```

**Type**
String

**Description**
Reserved for future use.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
A description of the update that occurred in the profile, permission set, or permission set
group.

**Example**

```
                   UserPerm: ConvertLeads disabled

```

```
EVENT_TYPE

FEATURE_ID

LOGIN_KEY

ORGANIZATION_ID

PERMISSION_TYPE

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `PermissionUpdate` .

**Type**
Id

**Description**
The ID of the feature, such as a profile, permission set, or permission set group, that was
updated.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The type of permission, such as user, object, or field, or setup entity access, such as tab
settings or Apex class access, that was updated.

**Example**

```
  EntityObject

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
                   3nWgxWbDKWWDIk0FKfF5DV

```

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

UPDATE_TYPE

USER_ID

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**

```
  d7DEq/ANa7nNZZVD

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
For object permissions, user permissions, and setup entity access, the type of update that
occurred. For example, a permission was updated or deleted.

For other changes in profiles, permission sets, or permission set groups, this information is
tracked in the `DESCRIPTION` field.

**Example**

```
  delete

```

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 15-character ID of the user who made the permission update.

**Example**

```
                   005XXXXXXXXXXXX

##### Platform Encryption Event Type

```

Platform Encryption event contains information about tenant secret and derived encryption key usage. This event type is available in
API versions 41.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

```

**Type**
String

**Description**
The name and type of the event.

**Possible Values**

**•** TS Imported: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, imported by a customer.

**•** TS Generated: A tenant secret generated by the Shield Key
Management Service (KMS).

**•** Key Derived: An encryption key derived from a tenant
secret for encryption or decryption.

**•** TS Wrapped: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, encrypted for storage.

**•** Key Delivered: A data encryption key delivered for
encryption or decryption.

**•** TS Stored: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, stored encrypted in the database.

**•** TS Read: An encrypted tenant secret generated by the
Shield Key Management Service (KMS), or encrypted
customer-supplied key material, that is loaded for
encryption or decryption.

**•** TS Unwrapped: An encrypted tenant secret generated by
the Shield Key Management Service (KMS), or encrypted


Standard Objects EventLogFile Supported Event Types

customer-supplied key material, unwrapped for use by the
KMS.

**•** TS Exported: An encrypted tenant secret exported by a
customer.

**•** TS Destroyed: A tenant secret and related data encryption
key destroyed by a customer.

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CLIENT_IP

CPU_TIME

EVENT_TYPE

KEY_ID

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

**Description**
The IP address of the client that is using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always
`PlatformEncryption` .

**Type**
String

**Description**
The 15-character ID of the tenant secret.

**Example**
02GD000000096Cb


Standard Objects EventLogFile Supported Event Types

```
KEY_ID_DERIVED

KEY_TYPE

LOGIN_KEY

METHOD

ORGANIZATION_ID

```

**Type**
String

**Description**
The 18-character ID of the derived encryption key.

**Example**
02GD000000096CbMAI

**Type**
String

**Description**
The type of tenant secret.

**Possible Values**

**•** Data

**•** DeterministicData

**•** Analytics

**•** OauthSecret (internal use only)

**•** SearchIndex

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The string that identifies a change in tenant secret Active state.
For example, tenant secrets become active when they’re
created, and are made inactive when they’re exported.

**Examples**

**•** TS Exported: User ID

**•** TS Generated: HSM or BYOK

**•** TS Unwrapped: Tenant Secret or BYOK

**Type**
ID

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
PLANNER_IDENTIFIER

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Pricing Event Type

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Pricing events contain information about pricing procedures that were executed, including details such as pricing procedures used, the
pricing APIs, and pricing details and status.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

```
CPU_TIME

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

PRICING_API_ENDPOINT

PRICING_DETAILS

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `Pricing` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000062` .

**Type**
String

**Description**
The starting point of the Pricing API or Headless Pricing API.

For example: `Pricing API` .

**Type**
String

**Description**
The details of the pricing event that describes if the pricing API
was executed or failed.

For example: `Pricing element was processed.` .


Standard Objects EventLogFile Supported Event Types

```
PRICING_ERROR_CODE

PRICING_LOG_NAME

PRICING_PROCEDURE

PRICING_STATUS

REQUEST_ID

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The API error code that appears when pricing execution fails.
If there is no error, the value is null.

For example: `INTERNAL_ERROR` .

**Type**
String

**Description**
The detailed pricing log message generated.

For example: `The Headless Pricing API was`
`run in:{0}` .

**Type**
String

**Description**
The name of the pricing procedure used to perform pricing
calculations.

For example: `Default Pricing Procedure` .

**Type**
String

**Description**
The status of the request for pricing execution.

For example: `Completed or Failed` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

For example: `1851629863` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

```
TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The time that the pricing was executed in GMT.

For example: `20170606170000.000` .

**Type**
DateTime

**Description**
The time that the pricing was executed in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2017-06-06T1700.000Z` . Timezone is
GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who executed pricing through
the UI or the API.

For example: `005SG000000eu6j`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.


Standard Objects EventLogFile Supported Event Types

For example: `001xx0000000useAAA` .

##### Queued Execution Event Type

Queued Execution events contain details about queued executions—for example, batch Apex.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

ENTRY_POINT

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds that it took to complete the batch
apex request. This field indicates the amount of activity taking
place in the app server layer, allowing you to identify pieces
of Apex or Visualforce code that need refactoring.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String

**Description**
The name of the Apex class that serves as the execution point
for the batch job.

[Note: This field contains data only for Batch Apex. It is](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch.htm)
unpopulated for Future and Queueable processes.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
TaskPhoneExtensionBatchUpdate

```
EVENT_TYPE

JOB_ID

LOGIN_KEY

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The type of event. The value is always `QueuedExecution` .

**Type**
String

**Description**
The ID of the batch Apex job.

**Example**
7073000000lDquo

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Report Event Type

Report events contain information about what happened when a user ran a report. This event type includes all activity that's in the
Report Export event type, plus more. For example, it has user activity for reports exported as both Formatted Report and Details Only
output.

Note: Exporting a report directly from the report result captures the event in both the Report and Report Export logs.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
AVERAGE_ROW_SIZE

```

**Type**
Number

**Description**
The average row size of all rows in the Report event, in bytes.
A large average size, coupled with a high `ROW_COUNT`, can
indicate that a user is downloading information for fraudulent


Standard Objects EventLogFile Supported Event Types

purposes. For example, a salesperson who downloads all sales
leads before departing for a competitor.

**Example**

```
CLIENT_IP

CPU_TIME

DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

DISPLAY_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The report display type, indicating the run mode of the report.

Possible values are:

**•** `D` —Dashboard

**•** `S` —Show Details

**•** `H` —Hide Details

```
ENTITY_NAME

EVENT_TYPE

LOGIN_KEY

NUMBER_BUCKETS

NUMBER_COLUMNS

NUMBER_EXCEPTION_FILTERS

ORGANIZATION_ID

```

**Type**
String

**Description**
The name of the object affected by the trigger.

**Type**
String

**Description**
The type of event. The value is always `Report` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of buckets that were used in the report.

**Type**
Number

**Description**
The number of columns in the report.

**Type**
Number

**Description**
The number of exception filters that are used in the report.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

```
ORIGIN

```

**Type**
String

**Description**
The context in which the report executed, such as from a UI
(Classic, Lightning, Mobile), through an API (synchronous,
asynchronous, Apex), or through a dashboard.

**Possible Values**

**•** `ReportOpenedFromMobileDashboard` : Report
executed when a user clicked a dashboard component on
a mobile device and drilled down to a report.

**•** `DashboardComponentUpdated` : Report executed
when a user refreshed a dashboard component.

**•** `DashboardComponentPreviewed` : Report
executed from a Lightning dashboard component preview.

**•** `ReportRunUsingSynchronousApi` : Report
executed from a synchronous API.

**•** `ReportRunUsingAsynchronousApi` : Report
executed from an asynchronous API.

**•** `ReportRunUsingApexSynchronousApi` : Report
executed from the synchronous Apex API.

**•** `ReportRunUsingApexAsynchronousApi` : Report
executed from the asynchronous Apex API.

**•** `ReportExported` : Report executed from a printable
view or report export that was not asynchronous nor an
API export.

**•** `ReportRunFromClassic` : Report executed from the
Run Report option of Salesforce Classic.

**•** `ReportRunFromMobile` : Report executed from the
Run Report option of the mobile Salesforce app.

**•** `ReportRunFromLightning` : Report executed from
the Run option in Lightning Experience from a non-mobile
browser.

**•** `ReportRunFromRestApi` : Report executed from
REST API.

**•** `ReportPreviewed` : Report executed when a user got
preview results while using the report builder.

**•** `ReportScheduled` : Report was scheduled.

**•** `ProbeQuery` : Report executed from a probe query.


Standard Objects EventLogFile Supported Event Types

**•** `ReportRunFromReportingSnapshot` : Report
executed through Snapshot Analytics.

**•** `ReportExportedAsynchronously` : Report was
exported asynchronously.

**•** `ReportExportedUsingExcelConnector` : Report
was exported using the Excel connector.

**•** `ChartRenderedOnVisualforcePage` : Report
executed from a rendered chart on a VisualForce Page.

**•** `ChartRenderedInEmbeddedAnalyticsApp` :
Report executed from a rendered chart in an embedded
Analytics app.

**•** `ReportRunAndNotificationSent` : Report
executed through the notifications API.

**•** `ChartRenderedOnHomePage` : Report executed from
a rendered chart on the home page.

**•** `ReportResultsAddedToWaveTrending` : Report
executed when a user trended a report in CRM Analytics.

**•** `ReportAddedToCampaign` : Report was added from
an Add to Campaign action.

**•** `ReportResultsAddedToEinsteinDiscovery` :
Report executed synchronously from Einstein Discovery.

**•** `Unknown` : Report execution origin is unknown.

**•** `Test` : Report execution resulted from a test.

```
RENDERING_TYPE

REPORT_ID

```

**Type**
String

**Description**
Describes the format of the report output in Salesforce Classic.
If the report was exported in Lightning Experience, this field is
blank.

**Possible Values**

**•** `W` : Web (HTML)

**•** `E` : Email

**•** `P` : Printable

**•** `X` : Excel

**•** `C` : Comma-separated values (CSV)

**•** `J` : JavaScript Object Notation (JSON)

**•** `D` : Dummy data

**Type**
Id

**Description**
The 15-character ID of the report that was run.


Standard Objects EventLogFile Supported Event Types

```
REPORT_ID_DERIVED

REQUEST_ID

REQUEST_STATUS

ROW_COUNT

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the report that was run.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The number of rows that were processed in the Report event.
High row counts, coupled with a high
`AVERAGE_ROW_SIZE`, can indicate that a user is
downloading information for fraudulent purposes. For example,
a salesperson who downloads all sales leads before departing
for a competitor.

**Example**


Standard Objects EventLogFile Supported Event Types

```
RUN_TIME

SESSION_KEY

SORT

TIMESTAMP

TIMESTAMP_DERIVED

UI_NUMBER_COLUMNS

URI

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The sort column and order that was used in the report.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Number

**Description**
The number of columns in the report. The fields that have
multiple components (for example, addresses) are considered
as a single column.

**Type**
String

**Description**
The URI of the page that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through


Standard Objects EventLogFile Supported Event Types

a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

Usage

**Example: Identify Large Report Exports by User**

Get Report event type data from the EventLogFile object using REST:

```
   /services/data/v40.0/query?q=SELECT+Id+,+EventType+,+LogFile+,+LogDate+,+LogFileLength+FROM+EventLogFile+WHERE+

      LogDate+>+Yesterday+AND+EventType+=+'Report'

```

After you download the report data to a ReportData database table, query it and filter on reports that were exported with high row
counts and size:

```
   SELECT USER_ID FROM ReportData WHERE (RENDERING_TYPE=C OR RENDERING_TYPE=X OR

   RENDERING_TYPE=P) AND ROW_COUNT>150000 AND AVERAGE_ROW_SIZE>1500

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Report Export Event Type

Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports a
report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that data,
see the Report event type.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CLIENT_INFO

CPU_TIME

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REPORT_DESCRIPTION

```

**Type**
String

**Description**
Information about the client that’s using Salesforce services.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `ReportExport` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
Information about the report that was run.


Standard Objects EventLogFile Supported Event Types

```
REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### REST API Event Type

REST API events contain details about REST-specific requests.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CLIENT_NAME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The name of the client that’s using Salesforce services. This
field is an optional parameter that can be passed in API calls.

```
CONNECTED_APP_ID

CPU_TIME

DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

ENTITY_NAME

```

**Type**
Reference

**Description**
The 15-character ID of the connected app associated with the
API call. For example, `0H4RM00000000Kr0AI` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Set

**Description**
The name of the object accessed by the API request.


Standard Objects EventLogFile Supported Event Types

For example: `Account`, `Opportunity`, `Contact`, and
so on.

```
EVENT_TYPE

EXCEPTION_MESSAGE

LOGIN_KEY

MEDIA_TYPE

METHOD

NUMBER_FIELDS

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of event. The value is always `RestApi` .

**Type**
String

**Description**
The returned exception message, used to debug issues. Provide
this message when seeking support.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The media type of the response.

**Type**
String

**Description**
The HTTP method of the request.

For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Number

**Description**
The number of fields or columns, where applicable.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
QUERY

REQUEST_SIZE

REQUEST_STATUS

REQUEST_ID

RESPONSE_SIZE

```

**Type**
String

**Description**
The data that was queried.

**Type**
Number

**Description**
The size of the callout request body, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the callout response, in bytes.


Standard Objects EventLogFile Supported Event Types

```
ROWS_PROCESSED

RUN_TIME

SESSION_KEY

STATUS_CODE

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP response status code for the request.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .


Standard Objects EventLogFile Supported Event Types

```
URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Number

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.


Standard Objects EventLogFile Supported Event Types

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Sandbox Event Type

Sandbox events contain details about sandbox copies.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CURRENT_SANDBOX_ORG_ID

EVENT_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the current sandbox organization.

**Type**
String

**Description**
##### The type of event. The value is always Sandbox .


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

PENDING_SANDBOX_ORG_ID

REQUEST_ID

SANDBOX_ID

STATUS

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the target sandbox org.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Id

**Description**
The 15-character ID of the sandbox organization.

**Type**
String

**Description**
The status of the sandbox copy.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.


Standard Objects EventLogFile Supported Event Types

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Search Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Search events contain details about the user’s search query. All searches within the app, including Experience Cloud sites, are included.
However, unauthenticated users won’t have a unique Salesforce user ID.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

NUM_RESULTS

```

**Type**
String

**Description**
##### The type of event. The value is always Search .

**Type**
Number

**Description**
Number of results returned by the search query.

**Possible Values**

**•** 0

**•** 25

**•** 1000


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

PREFIXES_SEARCHED

QUERY_ID

REQUEST_ID

SEARCH_QUERY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
Space-separated list of key prefixes that were searched.

**Example**
001 006 ka0

**Type**
String

**Description**
Unique ID of the search query.

**Example**
-2vx8relit08r

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The first 100 characters of the search query.

**Example**
Salesforce

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
USER_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Search Click Event Type

**Type**
Id

**Description**
The 15-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Search Click events contain details about the user’s interaction with the search results in the search results page. Interactions with search
results in the instant result dialog are not recorded by this event. All searches within the app, including Experience Cloud sites, are
included. However, unauthenticated users won’t have a unique Salesforce user ID.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLICKED_RECORD_ID

EVENT_TYPE

ORGANIZATION_ID

```

**Type**
String

**Description**
The 15-character ID of the result the user clicked in the search
results page.

**Example**
a07B00000031pRV

**Type**
String

**Description**
The type of event. The value is always `SearchClick` .

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

```
QUERY_ID

RANK

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
String

**Description**
Unique ID of the search query.

**Example**
-2vx8relit08r

**Type**
Number

**Description**
Ranking of the result clicked in the search results page.

**Example**

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Sites Event Type

Sites events contain details of Site.com requests. Requests can originate from the browser (UI).

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

HTTP_HEADERS

HTTP_METHOD

IS_API

IS_ERROR

IS_FIRST_REQUEST

IS_GUEST

IS_SECURE

```

**Type**
String

**Description**
The type of event. The value is always `Sites` .

**Type**
String

**Description**
The HTTP headers that were sent in the request.

**Type**
String

**Description**
The HTTP method of the request.

For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Boolean

**Description**
True if this page was an API or Web Services request.

**Type**
Boolean

**Description**
True if this page was an error page.

**Type**
Boolean

**Description**
1 if this page is the first Visualforce transaction in the request,
or 0 if it isn't.

**Type**
Boolean

**Description**
True if this page was a guest (unauthenticated) request.

**Type**
Boolean

**Description**
True if this request is secure.


Standard Objects EventLogFile Supported Event Types

```
LOGIN_KEY

ORGANIZATION_ID

PAGE_NAME

QUERY

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The name of the Visualforce page that was requested.

**Type**
String

**Description**
The SOQL query, if one was performed.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.


Standard Objects EventLogFile Supported Event Types

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
REQUEST_TYPE

RUN_TIME

SESSION_KEY

SITE_ID

```

**Type**
String

**Description**
The request type.

Possible values are:

**•** `page` —a normal request for a page

**•** `content_UI` —a content request for a page that
originated in the user interface

**•** `content_apex` —a content request initiated by an
Apex call

**•** `PDF_UI` —a request for a page in PDF format through
the user interface

**•** `PDF_apex` —a request for PDF format by an Apex call
(usually a Web Service call)

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Id

**Description**
The 15-character ID of the Site.com site.


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### SOAP API Event Type

SOAP API events contain details about your org's SOAP API request activity.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
API_TYPE

API_VERSION

CLIENT_IP

CLIENT_NAME

CPU_TIME

```

**Type**
String

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The name of the client that’s using Salesforce services. This
field is an optional parameter that can be passed in API calls.
If blank, the caller didn't specify a client in the CallOptions
header.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

```
DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

ENTITY_NAME

EVENT_TYPE

EXCEPTION_MESSAGE

```

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Set

**Description**
The name of the object accessed by the API request.

For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
String

**Description**
The type of event. The value is always `API` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The exception message for a SOAP API request. An exception
message gives details about errors in handling an API request,
such as why an API request failed.

For example: `common.exception.ApiException:`

```
                              startDate cannot be more than 30 days
```

`ago` .

```
LOGIN_KEY

METHOD_NAME

ORGANIZATION_ID

QUERY

REQUEST_ID

REQUEST_SIZE

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The name of the calling Apex method.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The data that was queried.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The size of the callout request body, in bytes.

```
REQUEST_STATUS

RESPONSE_SIZE

ROWS_PROCESSED

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

```
TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

```
USER_TYPE

```

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.


Standard Objects EventLogFile Supported Event Types

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Time-Based Workflow Event Type

Time-Based Workflow events contain details about queue activity monitoring.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

Note: Time-Based Workflow events only support workflow rules, and not flow scheduled path time-queue records. Event logs
do not show flow scheduled path time-queue records.

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DATA

EVENT_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The record details of time queue activity.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always
`TimeBasedWorkflow` .

```
LOG_GROUP_ID

LOGIN_KEY

NUMBER_OF_RECORDS

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
Marks log records that are committed or rolled back.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of processed records.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

```
TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The type of time-based workflow event.

**•** `UIDEL` —An entry was deleted from the Time-Based
Automations page in Setup.

**•** `ERRDEL` —An entry was deleted from the workflow
queue, because there was an error reading the record that
triggered the workflow rule. The associated
time-dependent actions weren’t processed.

**•** `DELETE` —An entry was deleted from the workflow
queue, because it’s no longer relevant. For example, the
criteria are no longer met by the associated record. If the
evaluation date for the entry changed, the entry is re-added
with the updated evaluation date.

**•** `PROC` —An entry was deleted from the workflow queue
after processing a time-dependent action.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .


Standard Objects EventLogFile Supported Event Types

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Transaction Security Event Type

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Transaction Security events contain details about policy execution. This event type is supported in API version 55.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

CPU_TIME

EVALUATION_TIME_MS

EVENT_TIMESTAMP

EVENT_TYPE

LOGIN_KEY

```

**Type**
String

**Description**
The IP address of the client that is using Salesforce services. A
Salesforce internal IP, such as a login from AppExchange, is
shown as “Salesforce.com IP”.

For example: `96.43.144.26`

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in milliseconds used to evaluate the policy.

**Type**
String

**Description**
The time at which the Transaction Security event was
generated in ISO8601-compatible format
(YYYY-MM-DDTHH:MM:SS.sssZ). This value can be earlier than
TIMESTAMP_DERIVED by the amount of time taken to log the
event.

For example: `2015-07-27T11:32:59.555Z`

**Type**
String

**Description**
The type of event. The value is always
`TransactionSecurity` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I`


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

PLANNER_IDENTIFIER

POLICY_ID

POLICY_ID_DERIVED

REQUEST_ID

RESULT

RUN_TIME

```

**Type**
ID

**Description**
The 15-character ID of the organization.

For example: `00D000000000123`

**Type**
String

**Description**
The ID of the agent planner.

**Type**
ID

**Description**
The 15-character ID of the policy being evaluated.

For example: `00530000009M943`

**Type**
ID

**Description**
The 18-character case-insensitive ID of the policy being
evaluated.

For example: `00590000000I1SNIA0`

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV`

**Type**
String

**Description**
The outcome of evaluating the policy.

For example: `TRIGGEREDzzz` or `NOT TRIGGERED`

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.


Standard Objects EventLogFile Supported Event Types

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD`

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670`

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp`

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
ID

**Description**
The 15-character ID of the user who is using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
ID


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0`

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### UI Telemetry Navigation Timing Event Type

UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from the
[UI Telemetry Resource Timing Event on page 2414 and includes requests initiated with either the Fetch API or the XMLHttpRequest API.](https://fetch.spec.whatwg.org/)
This object is available in API version 61.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

For information about navigation timing attributes, including a diagram of the order that attributes follow, see section 4.1 of the W3
[Standards on Navigation Timing Level 2.](https://www.w3.org/TR/navigation-timing-2/)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
                   United States/California

```

```
CLIENT_ID

CLIENT_IP

CONNECT_END

CONNECT_START

CONNECTION_TYPE

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as `Salesforce.com IP` .

**Example**

```
  96.43.144.26

```

**Type**
Number

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
Number

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

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

```
DECODED_BODY_SIZE

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

```

**Type**
Number

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
String

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
DOM_COMPLETE

DOM_CONTENT_LOADED_EVENT_END

DOM_CONTENT_LOADED_EVENT_START

DOM_INTERACTIVE

DOMAIN_LOOKUP_END

DOMAIN_LOOKUP_START

```

**Type**
Number

**Description**
The time in milliseconds when the page’s `readyState` property is set to `complete` .
Indicates that the page and its subresources have finished loading.

**Type**
Number

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler completes.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

**Type**
Number

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler starts.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

**Type**
Number

**Description**
The time in milliseconds when the page’s `readyState` is set to `interactive` . Indicates
that the page has finished loading, but subresources, such as images and scripts, are still
loading.

**Type**
Number

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

```
DURATION

ENCODED_BODY_SIZE

EVENT_TYPE

FETCH_START

FIRST_INTERIM_RESPONSE_START

INITIATOR_TYPE

```

**Type**
Number

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`LOAD_EVENT_END` time.

**Type**
Number

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
String

**Description**
The type of event. The value is always `UITelemetryNavigationTiming` .

**Type**
Number

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
String

**Description**
The HTML element that initiates the resource load.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
`css`, `image`, `link`

```
LOAD_EVENT_END

LOAD_EVENT_START

LOGIN_KEY

NAVIGATION_TYPE

NEXT_HOP_PROTOCOL

```

**Type**
Number

**Description**

The time in milliseconds when the page’s `load` event handler completes.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
Number

**Description**

The time in milliseconds when the page’s `load` event handler begins.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The type of navigation timing data.

**Possible Values**

**•** `navigate` : a user interaction or a script initiated navigation.

**•** `reload` : a reload initiated navigation.

**•** back_forward: navigation traverses the browser’s history.

**•** `prerender` : a prerender hint initiated navigation.

**Type**
String

**Description**
The Application-Layer Protocol Negotiation (ALPN) Protocol ID that fetches the resource.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**
`http/0.9`, `http/1.0`, `h2`, `h2c`, `h3`

```
ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The name of the component hosting the main content of the page.

**Example**

```
  clients:cardsContainer

```

**Type**
String

**Description**
The unique entity identifier of the event.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
`task`, `contacts`

```
PAGE_URL

REDIRECT_COUNT

REDIRECT_END

REDIRECT_START

RENDER_BLOCKING_STATUS

```

**Type**
String

**Description**
The relative URL of the top-level Lightning Experience page that the user opened. The page
can contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
Number

**Description**
The total number of redirects since the last non-redirect navigation in the current browsing
context.

**Type**
Number

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
String

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Possible Values**

**•** `blocking` : the resource can block rendering.

**•** code `non-blocking` : the resource doesn’t block rendering.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

REQUEST_START

RESPONSE_END

RESPONSE_START

RESPONSE_STATUS

SDK_APP_TYPE

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
Number

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
Number

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
Number

**Description**
The HTTP response status code.

**Example**

```
  200

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

```
SDK_APP_VERSION

SDK_VERSION

SECURE_CONNECT_START

SERVER_REQUEST_ID

SESSION_KEY

```

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
Number

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

To calculate the Transport Layer Security (TLS) time, subtract the
`SECURE_CONNECT_START` time from the `REQUEST_START` time.

**Type**
String

**Description**
The request ID for the server request that’s used to find associated server logs.

**Example**

```
  346000000087551ecb

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Example**

```
                   cdd09305cb6babf34059e27f70e47f1b11dec868

```

```
START_TIME

TIMESTAMP

TIMESTAMP_DERIVED

TRANSFER_SIZE

UI_EVENT_RELATIVE_TIMESTAMP

UI_EVENT_TIMESTAMP

```

**Type**
Number

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
(YYYY-MM-DDTHH:MM:SS.sssZ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
Number

**Description**
The size in octets of the resource, including the response header and the response payload
body.

**Type**
Number

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Example**

```
  29322.23

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The time at which this event occurs, measured in milliseconds.

**Example**

```
                   1479769912796

```

```
UI_ROOT_ACTIVITY_ID

UI_THREAD_RESPONSE_DELAY

UNLOAD_EVENT_END

UNLOAD_EVENT_START

URL

USER_ID

```

**Type**
String

**Description**
The ID of the root activity when the event occurs.

**Type**
Number

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

**Type**
Number

**Description**

The time in milliseconds when the page’s `unload` event handler completes.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
Number

**Description**

The time in milliseconds when the page’s `unload` event handler starts.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
String

**Description**
The URL of the request.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   00530000009M943

```

```
USER_ID_DERIVED

USER_TYPE

WORKER_START

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

**Type**
Number

**Description**
If a service worker is installed, the time in milliseconds when the active service worker receives
the `fetch` event.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### UI Telemetry Resource Timing Event

UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 61.0 and later.](https://fetch.spec.whatwg.org/)

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

For information about resource timing attributes, including a diagram of the order that attributes follow, see section 4.6 of the W3
[Standards on Resource Timing.](https://www.w3.org/TR/resource-timing/)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   United States/California

```

```
CLIENT_ID

CLIENT_IP

CONNECT_END

CONNECT_START

CONNECTION_TYPE

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP.”

**Example**

```
  96.43.144.26

```

**Type**
Number

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
Number

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

```
DECODED_BODY_SIZE

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

DOMAIN_LOOKUP_END

```

**Type**
Number

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
String

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

```
DOMAIN_LOOKUP_START

DURATION

ENCODED_BODY_SIZE

EVENT_TYPE

FETCH_START

FIRST_INTERIM_RESPONSE_START

```

**Type**
Number

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
Number

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`RESPONSE_END` time.

**Type**
Number

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
String

**Description**
The type of event. The value is always `UITelemetryResourceTiming` .

**Type**
Number

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

```
INITIATOR_TYPE

LOGIN_KEY

NEXT_HOP_PROTOCOL

ORGANIZATION_ID

OS_NAME

```

**Type**
String

**Description**
The HTML element that initiates the resource load.

**Example**
`css`, `image`, `link`

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The Application-Layer Protocol Negotiation (ALPN) Protocol ID that fetches the resource.

**Possible Values**
`http/0.9`, `http/1.0`, `h2`, `h2c`, `h3`

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
`Android`, `iOS`, `OSX`, `Window`

```
OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_URL

REDIRECT_END

```

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The name of the component hosting the main content of the page.

**Example**

```
  clients:cardsContainer

```

**Type**
String

**Description**
The unique entity identifier of the event.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`task`, `contacts`

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience page that the user opened. The page can
contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

```
REDIRECT_START

RENDER_BLOCKING_STATUS

REQUEST_ID

REQUEST_START

RESPONSE_END

```

**Type**
Number

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
String

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Possible Values**

**•** `blocking` : the resource can block rendering.

**•** code `non-blocking` : the resource doesn’t block rendering.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
Number

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

```
RESPONSE_START

RESPONSE_STATUS

SDK_APP_TYPE

SDK_APP_VERSION

```

**Type**
Number

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
Number

**Description**
The HTTP response status code.

**Example**

```
  200

```

**Type**
String

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

```
  5.0

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SDK_VERSION

SECURE_CONNECT_START

SERVER_REQUEST_ID

SESSION_KEY

START_TIME

TIMESTAMP

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
Number

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

To calculate the Transport Layer Security (TLS) time, subtract the
`SECURE_CONNECT_START` time from the `REQUEST_START` time.

**Type**
String

**Description**
The requestId for the server request that’s used to find associated server logs.

**Example**

```
  346000000087551ecb

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
Number

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP_DERIVED

TRANSFER_SIZE

UI_EVENT_RELATIVE_TIMESTAMP

UI_EVENT_TIMESTAMP

UI_ROOT_ACTIVITY_ID

UI_THREAD_RESPONSE_DELAY

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
(YYYY-MM-DDTHH:MM:SS.sssZ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
Number

**Description**
The size in octets of the resource, including the response header and the response payload
body.

**Type**
Number

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Example**

```
  29322.23

```

**Type**
Number

**Description**
The time at which this event occurs, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The ID of the root activity when the event occurs.

**Type**
Number

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
URL

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URL of the request.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
WORKER_START

```

SEE ALSO:

**Type**
Number

**Description**
The time in milliseconds when the active service worker receives the `fetch` event, if a
service worker is installed.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

EventLogFile Supported Event Types

EventLogFile

##### Unique Query Event Type

Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This event type is available in API versions 64.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

LOGIN_KEY

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

PLANNER_IDENTIFIER

QUERY_IDENTIFIER

QUERY_TYPE

SESSION_KEY

SQL_ID

##### URI Event Type

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The text of the SOQL query run or the Id of the report or list
view run.

**Type**
String

**Description**
The input type to the optimizer that was translated.

**Possible Values**

**•** soql

**•** filter

**•** report

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The unique identifier generated for the database query.

URI events contain details about user interaction with the web browser UI.


Standard Objects EventLogFile Supported Event Types

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REFERRER_URI

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The type of event. The value is always `URI` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The referring URI of the page that’s receiving the request.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.


Standard Objects EventLogFile Supported Event Types

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request. For more
granular URI information for Lightning Experience and the


Standard Objects EventLogFile Supported Event Types

Salesforce app, see the Lightning Error, Lightning Interaction,
Lightning Page View, and Lightning Performance event types.

**Examples**
`/aura` (Lightning Experience), `/lightning` (Lightning
Experience and the Salesforce app), `/home/home.jsp`
(Salesforce Classic)

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.


Standard Objects EventLogFile Supported Event Types

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Visualforce Request Event Type

Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI).

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CONTROLLER_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The type of controller that’s used by the requested Visualforce
page.

**Possible Values**

**•** `0` : NOT_SPECIFIED—The controller type is not specified.

**•** `1` : STANDARD—The controller is a standard controller.

**•** `2` : CUSTOM—The controller is a custom controller or
controller extension.

**•** `3` : JAVA—For internal use only.

**•** `4` : STANDARD_SET—The controller is a standard list
controller.

**•** `5` : SPRING—Not used.

```
CPU_TIME

DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

HTTP_METHOD

IS_AJAX_REQUEST

IS_FIRST_REQUEST

LOGIN_KEY

MANAGED_PACKAGE_NAMESPACE

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of event. The value is always
`VisualforceRequest` .

**Type**
String

**Description**
The HTTP method of the request.

For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Boolean

**Description**
The value is `true` if the request is a partial page request.

**Type**
Boolean

**Description**
1 if this page is the first Visualforce transaction in the request,
or 0 if it isn't.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
If the page is part of a managed package, the namespace of
that package.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
PAGE_NAME

QUERY

REQUEST_ID

REQUEST_SIZE

REQUEST_STATUS

```

**Type**
String

**Description**
The name of the Visualforce page that was requested.

**Type**
String

**Description**
The query string used to access the requested Visualforce page.

**Example**
Let’s assume that the requested Visualforce page
( `/apex/myAccountDetailPage?id=001xx000003GYv6AAG` )
shows details of the account whose ID is in the URL. The value
of `QUERY` in this case is `?id=001xx000003GYv6AAG` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the request body, in bytes. Value is -1 if the request
body content is larger than 2GB, or if the request has no body
(for example, a typical GET request).

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined


Standard Objects EventLogFile Supported Event Types

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
REQUEST_TYPE

RESPONSE_SIZE

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The request type.

Possible values are:

**•** `page` —a normal request for a page

**•** `content_UI` —a content request for a page that
originated in the user interface

**•** `content_apex` —a content request initiated by an
Apex call

**•** `PDF_UI` —a request for a page in PDF format through
the user interface

**•** `PDF_apex` —a request for PDF format by an Apex call
(usually a Web Service call)

**Type**
Number

**Description**
The size of the response, in bytes.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Number

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .


Standard Objects EventLogFile Supported Event Types

```
USER_TYPE

VIEW_STATE_SIZE

```

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The size of the Visualforce view state, in bytes.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Wave Change Event Type

Wave Change events represent route or page changes made in the CRM Analytics user interface. A Wave Change event type is captured
every time the user opens a new CRM Analytics asset or tab, switches between tabs, or changes dashboard pages. Wave Change events
are logged when opening new tabs and switching back to previously opened tabs.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ANALYTICS_MODE

CLIENT_IP

```

**Type**
String

**Description**
The location in which the dashboard is displayed. In the
Salesforce mobile app, embedded dashboards are logged as
`embedded` first. When a user interacts with the dashboard,
a full-screen dashboard is displayed to allow for user
interaction, and is logged as `mobileNative` .

Possible values are:

**•** `studio` —Analytics Studio

**•** `tab` —Analytics tab

**•** `embedded`    - Embedded in Aura or Lightning.

**•** `embeddedInCommunities`    - Embedded in
Experience Cloud.

**•** `mobileNative`    - CRM Analytics mobile app for
iOS/Android or Salesforce mobile app for iOS/Android

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

EVENT_TYPE

IS_MOBILE

IS_NEW

LOGIN_KEY

ORGANIZATION_ID

PAGE_CONTEXT

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `WaveChange` .

**Type**
Boolean

**Description**
If `true`, the dashboard is displayed in the Tableau CRM mobile
app for iOS and Android, in the Salesforce mobile app for iOS
and Android, or in a mobile browser.

**Type**
Boolean

**Description**
The field indicates that this action opens a new tab or goes
back to a previously opened tab. If the change routes to a new
page, the value of this field is true. If it routes to an existing
page, this field is false.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The context of the page in which the dashboard is displayed.
In the Salesforce mobile app, embedded dashboards are
logged as `aura` first. When a user interacts with the
dashboard, a full-screen dashboard is displayed to allow for
user interaction, and is logged as `iOS` or `android` .

Possible values are:

**•** `aura` —Lightning Components

**•** `vf` —Visualforce

**•** `iOS`                              - CRM Analytics or Salesforce mobile app for iOS

**•** `android`                              - CRM Analytics or Salesforce mobile app for
Android

```
PAGE_ID

RECORD_ID

REOPEN_COUNT

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**

The ID of the CRM Analytics dashboard page.

This field is only available in v58.0 and higher.

**Type**
String

**Description**
The Salesforce ID of the CRM Analytics object.

**Type**
Number

**Description**
If `IS_NEW` is false, the number of times that an existing page
opens.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.


Standard Objects EventLogFile Supported Event Types

```
SAVED_VIEW_ID

SESSION_KEY

TAB_ID

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

```

**Type**
String

**Description**
The ID of the CRM Analytics dashboard saved view.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The ID of the particular Analytics tab in the user interface.

For example: `dashboard-0FKB0000000Ec64GDK` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The CRM Analytics object type.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .


Standard Objects EventLogFile Supported Event Types

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

VIEW_MODE

WAVE_SESSION_ID

WAVE_TIMESTAMP

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943` .

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The view mode for the CRM Analytics asset. Possible values
include `view`, `edit`, `present`, `json`, or `print` .

**Type**
String

**Description**
The ID of a particular session of CRM Analytics. Use this field
to determine which log lines originated from a particular
session.

**Type**
Number

**Description**
The time at which this log line was generated.


Standard Objects EventLogFile Supported Event Types

##### Wave Download Event Type

Wave Download events represent downloads made from lens explorations and dashboard widgets in the CRM Analytics user interface.
A Wave Download event type is captured when a user downloads images ( .png ), Microsoft [®] Excel [®] data ( .xls ), or comma-separated
values ( .csv ) files.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ASSET_ID

ASSET_TYPE

CLIENT_IP

CPU_TIME

DATASET_IDS

```

**Type**
ID

**Description**
The ID of the asset the user downloads from.

**Type**
String

**Description**
The type of the asset the user downloads from.

**Values**

**•** `Lens` —A _lens_ is a view into a dataset used in an exploratory mode or to get insight to
a specific business question. The lens can be saved and shared independently. It can
also be clipped to a dashboard.

**•** `Dashboard` —A _dashboard_ is a curated set of charts, metrics, and tables based on the
data in one or more lenses.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**
96.43.144.26

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Comma-separated list of IDs of utilized data sets.

```
DOWNLOAD_ERROR

DOWNLOAD_FORMAT

EVENT_TYPE

LOGIN_KEY

NUMBER_OF_RECORDS

ORGANIZATION_ID

```

**Type**
String

**Description**
The message for the error blocking the download request, if any.

**Type**
String

**Description**
The data format of the export.

**Values**

**•** `png` —Image

**•** `csv` —Comma-separated values

**•** `xls`  - Microsoft Excel

**Type**
String

**Description**
The type of event. The value is always `WaveDownload` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Example**
GeJCsym5eyvtEK2I

**Type**
Number

**Description**
The number of records exported.

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**
00D000000000123


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**
3nWgxWbDKWWDIk0FKfF5DV

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**
d7DEq/ANa7nNZZVD

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

**Example**

```
  /home/home.jsp

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

WAVE_SESSION_ID

WAVE_TIMESTAMP

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The type of Salesforce user.

**Type**
String

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
Number

**Description**
The time at which this log line was generated.

##### Wave Interaction Event Type

Wave Interaction events represent route or page changes made in the CRM Analytics user interface. A Wave Interaction event type is
captured when a tab is closed. It also collates the interaction statistics over the life of the tab, including total open time, read time, and
so on. These statistics are aggregated as you go to other tabs and return, and logged only once when the tab is closed.


Standard Objects EventLogFile Supported Event Types

Note: Because Wave Interaction events are logged only when the tab or browser window is closed, these events might not match
Wave Change events exactly if a user allows their Salesforce session to time out before closing.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

NUM_CLICKS

NUM_SESSIONS

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `WaveInteraction` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of clicks performed on a page in the CRM Analytics
user interface.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The number of times a user returned to a particular page.

```
ORGANIZATION_ID

READ_TIME

RECORD_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TAB_ID

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Number

**Description**
The amount of time a user spent on a particular tab.

**Type**
String

**Description**
The Salesforce ID of the CRM Analytics object.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The ID of the particular Analytics tab in the user interface.

**Example**
dashboard-0FKB0000000Ec64GDK

```
TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_TIME

TYPE

URI

URI_ID_DERIVED

USER_ID

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Number

**Description**
The total amount of time a tab was open in milliseconds.

**Type**
String

**Description**
The CRM Analytics object type.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

